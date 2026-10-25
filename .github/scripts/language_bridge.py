#!/usr/bin/env python3
"""Bridge a translation branch into the folder GitBook imports.

The translation team and the nightly docs bots write German, Spanish, ...
pages to the language branches (`de`, `es`, `fr`, `it`, `pt`, `pl`, `nl`, `zh`),
under `readme/`. The GitBook language spaces, however, import
`main:<folder>/` (Git Sync, "GitHub -> GitBook"): `deutsch/`, `espanol/`,
`french/`, `italian/`, `portuguese/`, `polish/`, `dutch/`, `chinese/`. Without a bridge,
a translation merged into a language branch never reaches GitBook.

    language_bridge.py sync --lang de --source /path/to/checkout-of-branch-de
    language_bridge.py sync --lang de --source ... --dry-run

`--source` is a checkout of the language branch (its `readme/` directory is
mirrored); `--dest` is the root of a checkout of `main` (default: the current
directory). What is mirrored:

  * `SUMMARY.md` and `README.md`
  * every page listed in the language branch's `SUMMARY.md`
  * the images / attachments those pages reference (`.gitbook/assets/...`)

Nothing is ever deleted in the destination, and pages that are not in the
navigation are left alone.

Why validate: a single markdown error makes GitBook abort the whole import
("Failed to parse Markdown content in ...") and fall back to exporting its old
state over the repository. So a language is only synced when ALL of these hold,
otherwise nothing is written for it and the script exits with status 1:

  * every navigation entry has a file
  * GitBook tags are balanced ({% hint %}/{% endhint %}, tabs, code, ...)
  * the front matter is a well-formed `key: value` block
  * every `{% file src="..." %}` points to an existing file

Images that do not exist anywhere only produce a warning (a broken image does
not stop the import).

Exit status: 0 = synced or nothing to do, 1 = validation failed, 2 = usage.
The last line on stdout is `RESULT key=value ...` for the workflow to parse.
"""

from __future__ import annotations

import argparse
import re
import string
import urllib.parse
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

# language branch -> folder GitBook imports (installationProjectDirectory)
LANGS = {
    "de": "deutsch",
    "es": "espanol",
    "fr": "french",
    "it": "italian",
    "pt": "portuguese",
    "pl": "polish",
    "nl": "dutch",
    "zh": "chinese",
}

NAV_LINE = re.compile(r'^(\s*)\* \[([^\]]*)\]\(([^)\s]+\.md)(?:\s+"(?:\\.|[^"\\])*")?\)\s*$')
PAGE_GROUP_IDS = {
    "overview-and-basics", "end-user-and-partner-section", "administration-and-setup",
    "infor-integration-and-configuration", "advanced-functions-and-tools", "security",
}
ASSET_REF = re.compile(r"\.gitbook/assets/([^\"'<>\n]+)")
FILE_BLOCK = re.compile(r"\{%\s*file\s+src=\"([^\"]+)\"")
STUB_HEADER = re.compile(r"^# [A-Z]{2} - TRANSLATED", re.M)
# paired GitBook block tags that must be balanced
PAIRED_TAGS = ("hint", "tabs", "tab", "code", "stepper", "step", "columns", "column")
FM_KEY = re.compile(r"^[A-Za-z_][\w-]*:")


@dataclass
class Report:
    pages: list[str] = field(default_factory=list)  # destination paths (relative) that change
    assets: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stubs: int = 0

    @property
    def changed(self) -> int:
        return len(self.pages) + len(self.assets)


def parse_summary(text: str) -> list[tuple[int, str, str]]:
    """(indent, title, path) of every markdown link line, in order."""
    out = []
    for line in text.split("\n"):
        m = NAV_LINE.match(line)
        if m:
            out.append((len(m.group(1)), m.group(2), m.group(3)))
    return out


def page_group_errors(text: str) -> list[str]:
    """Localized labels must retain the same URL group IDs in every space.

    Without an explicit ID, GitBook derives the group path from the translated
    title. The language picker then reuses that incompatible path in the next
    space and falls back to its home page.
    """
    headings = re.findall(r"^##\s+(.+)$", text, re.M)
    ids = []
    errors = []
    for heading in headings:
        anchor = re.search(r'<a\b[^>]*\bid=["\x27]([^"\x27]+)["\x27]', heading)
        if anchor:
            ids.append(anchor.group(1))
        else:
            errors.append(f"page group has no stable URL id: {heading}")
    missing = PAGE_GROUP_IDS - set(ids)
    if missing:
        errors.append("page group URL ids missing: " + ", ".join(sorted(missing)))
    unknown = set(ids) - PAGE_GROUP_IDS
    if unknown:
        errors.append("unknown page group URL ids: " + ", ".join(sorted(unknown)))
    if len(ids) != len(set(ids)):
        errors.append("duplicate page group URL ids")
    return errors


def lexical_path(path: Path) -> Path:
    """Resolve `.` and `..` without touching the file system."""
    parts: list[str] = []
    for part in path.parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part != ".":
            parts.append(part)
    return Path(*parts)


def safe_rel(rel: str) -> bool:
    """A relative path that stays below its base: not empty, not absolute, no `..`."""
    if not rel or "\\" in rel or "\0" in rel:
        return False
    parts = PurePosixPath(rel).parts
    return bool(parts) and not PurePosixPath(rel).is_absolute() and ".." not in parts


def has_symlink(base: Path, path: Path) -> bool:
    """True if `base` or any component of `path` below it is a symlink."""
    if base.is_symlink():
        return True
    cur = base
    for part in path.relative_to(base).parts:
        cur = cur / part
        if cur.is_symlink():
            return True
    return False


def contained(base: Path, path: Path) -> bool:
    """`path` is a regular, non-symlinked file that really lives below `base`."""
    try:
        return (
            safe_path(base, path)
            and path.is_file()
            and path.resolve().is_relative_to(base.resolve())
        )
    except (OSError, ValueError):
        return False


def safe_path(base: Path, path: Path) -> bool:
    try:
        return not has_symlink(base, path)
    except ValueError:
        return False


def resolve_asset(candidate: str, *asset_dirs: Path) -> tuple[str, Path] | None:
    """A reference like `image (83).png" alt=...` has no clean delimiter, so
    shorten it until it names a file in one of the asset directories."""
    for k in range(len(candidate), 0, -1):
        name = urllib.parse.unquote(
            re.sub(r"\\([" + re.escape(string.punctuation) + r"])", r"\1", candidate[:k])
        )
        if not safe_rel(name):
            continue
        for d in asset_dirs:
            if contained(d, d / name):
                return name, d / name
    return None


def front_matter_errors(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    lines = text.split("\n")
    try:
        end = lines.index("---", 1)
    except ValueError:
        return ["front matter is not closed"]
    for ln in lines[1:end]:
        if ln.strip() and not (FM_KEY.match(ln) or ln[:1] in " \t-#"):
            return [f"front matter contains a non key/value line: {ln[:50]!r}"]
    try:  # PyYAML is optional; the structural check above is the hard requirement
        import yaml

        yaml.safe_load("\n".join(lines[1:end]))
    except ImportError:
        pass
    except Exception as exc:  # noqa: BLE001 - any parser error is a finding
        return [f"front matter is not valid YAML: {str(exc).splitlines()[0][:60]}"]
    return []


def tag_errors(text: str) -> list[str]:
    errs = []
    for tag in PAIRED_TAGS:
        opened = len(re.findall(r"\{%\s*" + tag + r"\b", text))
        closed = len(re.findall(r"\{%\s*end" + tag + r"\b", text))
        if opened != closed:
            errs.append(f"unbalanced {{% {tag} %}} ({opened} opened, {closed} closed)")
    return errs


def plan_sync(source_readme: Path, dest_dir: Path) -> tuple[Report, dict[Path, Path]]:
    """Decide what to copy and validate the result without writing anything."""
    rep = Report()
    plan: dict[Path, Path] = {}  # destination file -> source file
    summary_src = source_readme / "SUMMARY.md"
    if source_readme.is_symlink() or dest_dir.is_symlink():
        rep.errors.append("readme/ or the destination folder is a symlink")
        return rep, plan
    if not contained(source_readme, summary_src):
        rep.errors.append("source has no readme/SUMMARY.md (or it is a symlink)")
        return rep, plan
    summary_text = summary_src.read_text(encoding="utf-8")
    rep.errors.extend(page_group_errors(summary_text))
    nav = parse_summary(summary_text)
    candidates = list(dict.fromkeys([p for _, _, p in nav] + ["README.md"]))

    pages: list[str] = []
    for p in candidates:
        if not safe_rel(p):
            rep.errors.append(f"unsafe navigation path: {p}")
            continue
        if not safe_path(dest_dir, dest_dir / p):
            rep.errors.append(f"destination is a symlink: {p}")
            continue
        src = source_readme / p
        if not contained(source_readme, src):
            if p != "README.md" or src.exists() or src.is_symlink():
                what = "is a symlink or outside readme/" if (src.exists() or src.is_symlink()) else "without file"
                rep.errors.append(f"navigation entry {what}: {p}")
            continue
        pages.append(p)

    for p in pages:
        src, dst = source_readme / p, dest_dir / p
        if not dst.is_file() or src.read_bytes() != dst.read_bytes():
            plan[dst] = src
            rep.pages.append(p)
    if not safe_path(dest_dir, dest_dir / "SUMMARY.md"):
        rep.errors.append("destination SUMMARY.md is a symlink")
    elif not (dest_dir / "SUMMARY.md").is_file() or summary_src.read_bytes() != (dest_dir / "SUMMARY.md").read_bytes():
        plan[dest_dir / "SUMMARY.md"] = summary_src
        rep.pages.append("SUMMARY.md")

    src_assets, dst_assets = source_readme / ".gitbook" / "assets", dest_dir / ".gitbook" / "assets"
    seen_assets: set[str] = set()
    for p in pages:
        src = source_readme / p
        if not src.is_file():
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        # --- validation of the version that will be in the destination
        rep.errors += [f"{p}: {e}" for e in front_matter_errors(text) + tag_errors(text)]
        if STUB_HEADER.search(text):
            rep.stubs += 1
        for target in FILE_BLOCK.findall(text):
            final = lexical_path((dest_dir / p).parent / target.replace("%20", " "))
            in_assets = final.parent == lexical_path(dst_assets)
            if not (final.is_file() or (in_assets and (src_assets / final.name).is_file())):
                rep.errors.append(f"{p}: {{% file %}} points to a missing file: {target}")
        # --- images and attachments
        for asset_ref in ASSET_REF.finditer(text):
            # An absolute image URL is fetched by GitBook itself. Its path
            # may contain .gitbook/assets, but it is not a branch-local file.
            if re.search(r"https?://[^\s\"'<>]*$", text[:asset_ref.start()]):
                continue
            cand = asset_ref.group(1)
            # Look in the BRANCH's assets first. The destination folder already
            # holds a copy of every asset from an earlier sync, so resolving
            # against it first made the branch's own version invisible: a
            # re-shot screenshot with an unchanged filename never travelled
            # across, and the page kept serving the old image. The destination
            # is only the fallback, for an asset a page shares and the branch
            # itself does not carry.
            hit = resolve_asset(cand, src_assets, dst_assets)
            if hit is None:
                rep.warnings.append(f"{p}: image not found anywhere: {cand[:50]}")
                continue
            name, found = hit
            if name in seen_assets:
                continue
            seen_assets.add(name)
            if found.parent == src_assets or contained(src_assets, found):
                dst = dst_assets / name
                if not safe_path(dest_dir, dst):
                    rep.errors.append(f"{p}: destination asset is a symlink: {name}")
                elif not dst.is_file() or dst.read_bytes() != found.read_bytes():
                    plan[dst] = found
                    rep.assets.append(name)
    return rep, plan


def apply_plan(plan: dict[Path, Path]) -> None:
    for dst, src in plan.items():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst, follow_symlinks=False)


def cmd_sync(args: argparse.Namespace) -> int:
    folder = LANGS.get(args.lang)
    if folder is None:
        print(f"unknown language {args.lang!r}; known: {', '.join(LANGS)}", file=sys.stderr)
        return 2
    source_readme = Path(args.source) / "readme"
    dest_dir = Path(args.dest) / folder
    rep, plan = plan_sync(source_readme, dest_dir)
    for w in rep.warnings[:20]:
        print(f"warning: {w}")
    if rep.errors:
        for e in rep.errors[:50]:
            print(f"error: {e}")
        print(f"RESULT lang={args.lang} status=invalid errors={len(rep.errors)} pages=0 assets=0")
        return 1
    if not args.dry_run:
        apply_plan(plan)
    print(
        f"RESULT lang={args.lang} status={'dry-run' if args.dry_run else 'ok'} "
        f"pages={len(rep.pages)} assets={len(rep.assets)} stubs={rep.stubs} warnings={len(rep.warnings)}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync", help="mirror a language branch into <folder>/")
    s.add_argument("--lang", required=True, help="language branch: " + ", ".join(LANGS))
    s.add_argument("--source", required=True, help="checkout of the language branch")
    s.add_argument("--dest", default=".", help="root of a checkout of main (default: .)")
    s.add_argument("--dry-run", action="store_true", help="validate and report, write nothing")
    s.set_defaults(func=cmd_sync)
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
