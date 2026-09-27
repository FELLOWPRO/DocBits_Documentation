#!/usr/bin/env python3
"""Sync docs.docbits.com markdown pages into the fulltextsearch docs index
(CORE-6111, Settings-Assistent doc search).

Two modes:

  diff --before SHA --after SHA --lang LANG
      Push mode. Diffs the two commits under readme/, POSTs changed pages
      to /docs/ingest and deleted/renamed-away pages to /docs/delete.

  full --lang LANG [--reconcile-only]
      Walks every markdown page reachable from readme/SUMMARY.md at the
      current checkout. Without --reconcile-only (workflow_dispatch, "full
      backfill"): ingests every page, then reconciles. With
      --reconcile-only (nightly cron): skips re-ingesting content and only
      deletes chunks for URLs no longer published — cheap, catches pages
      the diff-based push step missed (e.g. a squash-merge whose `before`
      SHA doesn't reflect what actually changed).

URL mapping (verified against 3+ live docs.docbits.com pages, see the PR
description): the site's root is `readme/` (see .gitbook.yaml `root: ./`),
each `.md` file's URL is its path relative to that root with the `.md`
suffix stripped, and `README.md` maps to its own directory (or `/` for the
top-level `readme/README.md`). A file not reachable from SUMMARY.md is NOT
published (docs.docbits.com 404s on it, confirmed on
`readme/setup/sso-configuration.md`, an orphan superseded by the nested
`administration-and-setup/.../sso-configuration/` page) — such files are
skipped rather than ingested as dead links.

DOCS_INGEST_URL / DOCS_INGEST_KEY come from the environment (the workflow
maps them from `secrets.DOCS_INGEST_URL` / `secrets.DOCS_INGEST_KEY`).
Never logged, never printed — only sent in the request itself.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
README_ROOT = "readme"
SUMMARY_PATH = os.path.join(README_ROOT, "SUMMARY.md")
BASE_DOCS_URL = "https://docs.docbits.com"
_MD_LINK_RE = re.compile(r"\]\(([^)]+\.md)\)")

# Image hosts the chat is allowed to show. docs.docbits.com itself, and the
# GitBook per-space files CDN — a host named "<numeric-space-id>-files.
# gitbook.io" (confirmed live: main is 578966019-files.gitbook.io, de is
# 2396827744-files.gitbook.io — one GitBook "space" per language variant,
# each with its own numeric id; note the HYPHEN before "files", it is not
# a "<id>.files.gitbook.io" subdomain). Anything else (pasted
# googleusercontent.com links etc.) is dropped rather than shown in chat.
_ALLOWED_IMAGE_HOST_SUFFIXES = ("-files.gitbook.io",)
_ALLOWED_IMAGE_EXACT_HOSTS = ("docs.docbits.com",)

# GitBook's exported HTML image block: <figure><img src="..." alt="...">
# ...</figure>. Attribute order is not guaranteed, so the tag is matched
# first and its attributes parsed separately.
_IMG_TAG_RE = re.compile(r"<img\b([^>]*)>", re.IGNORECASE)
_IMG_ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
# Plain markdown ![alt](src) — also handled since not every image in this
# repo uses the GitBook HTML form.
_MD_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')

# Extracts the real, directly-fetchable CDN url from GitBook's own
# docs.docbits.com/~gitbook/image?url=<encoded>&...&sign=<hmac>&... proxy —
# `sign` is a server-computed HMAC we cannot replicate, but the url it
# wraps needs no such signature (verified: 200 image/* with alt=media
# alone, see the PR description).
_GITBOOK_PROXY_IMG_SRC_RE = re.compile(r'src="(https://[^"]*~gitbook/image\?[^"]*)"')
_GITBOOK_PROXY_INNER_URL_RE = re.compile(r"[?&]url=([^&\"]+)")
_GIT_BLOB_SHA_RE = re.compile(r"git-blob-([0-9a-f]{40})")

# Per-run cache: {page_url: {blob_sha: resolved_absolute_url}}. One page
# has many images; fetch it once, not once per image.
_page_blob_url_cache: dict[str, dict[str, str]] = {}


def published_rel_path(md_path: str) -> str | None:
    """Map a repo-relative markdown path to its URL path segment.

    Returns None for paths outside readme/ (nothing else is published) or
    for filenames that don't end in .md. Returns "" for the top-level
    readme/README.md (the site root).
    """
    prefix = README_ROOT + "/"
    if not md_path.startswith(prefix):
        return None
    rel = md_path[len(prefix) :]
    if rel == "README.md":
        return ""
    if rel.endswith("/README.md"):
        return rel[: -len("/README.md")]
    if rel.endswith(".md"):
        return rel[: -len(".md")]
    return None


def full_url(rel_path: str, lang: str) -> str:
    """Build the live docs.docbits.com URL for a page.

    Verified against live pages (see PR description): the `main` branch
    (English) publishes at the site root with no prefix; other language
    branches publish under a `/{lang}` path segment (confirmed for `de` —
    `docs.docbits.com/de/...`). `lang` is otherwise a generic parameter (a
    branch not yet wired to a live GitBook variant, e.g. `es`, would just
    404 today — that's a docs-hosting decision, not something this script
    special-cases).
    """
    prefix = BASE_DOCS_URL if lang == "main" else f"{BASE_DOCS_URL}/{lang}"
    return prefix if not rel_path else f"{prefix}/{rel_path}"


def published_paths_from_summary() -> set[str]:
    """Every markdown file SUMMARY.md actually links to, as repo-relative
    paths (e.g. {"readme/setup/README.md", "readme/setup/sso.md", ...}).

    A file that exists on disk but isn't reachable from SUMMARY.md is not
    a real docs.docbits.com page — ingesting it would put a dead link in
    search results.
    """
    summary_file = os.path.join(REPO_ROOT, SUMMARY_PATH)
    if not os.path.exists(summary_file):
        return set()
    text = open(summary_file, encoding="utf-8").read()
    base_dir = os.path.dirname(SUMMARY_PATH)
    paths = set()
    for match in _MD_LINK_RE.finditer(text):
        target = match.group(1)
        if target.startswith("http://") or target.startswith("https://"):
            continue
        normalized = os.path.normpath(os.path.join(base_dir, target))
        paths.add(normalized.replace(os.sep, "/"))
    return paths


def extract_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


_NOINDEX_RE = re.compile(r"(?im)^\s*noindex\s*:\s*true\s*$")


def is_no_index(markdown_text: str) -> bool:
    """GitBook front matter can mark a page `noIndex: true` (draft/preview
    pages such as readme/overview-and-basics/diagram-preview/*, or an
    explicitly superseded `*_old.md` page). The site itself keeps such
    pages out of its own search/sitemap, so the docs search index does
    the same — only the YAML front matter block (between the leading
    `---` lines) is checked, so the word appearing in prose doesn't
    accidentally exclude a page.
    """
    if not markdown_text.startswith("---"):
        return False
    end = markdown_text.find("\n---", 3)
    if end == -1:
        return False
    front_matter = markdown_text[:end]
    return bool(_NOINDEX_RE.search(front_matter))


def _run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return result.stdout


def _is_allowed_image_host(url: str) -> bool:
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return host in _ALLOWED_IMAGE_EXACT_HOSTS or any(
        host.endswith(suffix) for suffix in _ALLOWED_IMAGE_HOST_SUFFIXES
    )


def _iter_raw_images(markdown_text: str) -> list[tuple[tuple[int, int], str, str]]:
    """Yield ((start, end), src, alt) for every image reference in document
    order — GitBook's exported `<figure><img src=... alt=...>` HTML form
    and plain markdown `![alt](src)` alike."""
    found: list[tuple[tuple[int, int], str, str]] = []
    for match in _IMG_TAG_RE.finditer(markdown_text):
        attrs = dict(_IMG_ATTR_RE.findall(match.group(1)))
        src = attrs.get("src")
        if src:
            found.append((match.span(), src, attrs.get("alt", "")))
    for match in _MD_IMAGE_RE.finditer(markdown_text):
        found.append((match.span(), match.group(2), match.group(1)))
    found.sort(key=lambda item: item[0][0])
    return found


def _fetch_page_blob_to_url_map(page_url: str) -> dict[str, str]:
    """Fetch the live rendered page and map every git-blob-sha embedded in
    its GitBook-proxied image urls to the underlying, directly-fetchable
    CDN url. Cached per page for the run.

    Returns {} (never raises) when the page can't be fetched — e.g. a
    brand-new page this same push introduced, which GitBook's own
    (separate, async) publish pipeline hasn't rendered yet. Callers treat
    an empty/missing lookup as "can't resolve this image right now" and
    drop it; the next full backfill (which re-fetches every page fresh)
    picks it up once the live site has caught up.
    """
    if page_url in _page_blob_url_cache:
        return _page_blob_url_cache[page_url]

    mapping: dict[str, str] = {}
    try:
        # docs.docbits.com (GitBook-hosted) 403s a bare urllib default
        # User-Agent — a normal browser UA is enough to pass.
        request = urllib.request.Request(
            page_url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; DocBitsSync/1.0)"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            page_html = response.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"::warning::could not fetch {page_url} to resolve images: {exc}")
        _page_blob_url_cache[page_url] = mapping
        return mapping

    for match in _GITBOOK_PROXY_IMG_SRC_RE.finditer(page_html):
        proxied_src = html.unescape(match.group(1))
        inner_match = _GITBOOK_PROXY_INNER_URL_RE.search(proxied_src)
        if not inner_match:
            continue
        inner_url = urllib.parse.unquote(inner_match.group(1))
        blob_match = _GIT_BLOB_SHA_RE.search(inner_url)
        if blob_match and _is_allowed_image_host(inner_url):
            mapping[blob_match.group(1)] = inner_url

    _page_blob_url_cache[page_url] = mapping
    return mapping


def resolve_images_in_markdown(markdown_text: str, md_path: str, page_url: str) -> str:
    """Rewrite every image reference to a directly-fetchable absolute url on
    an allowed host, normalised to plain markdown `![alt](url)` (so
    fulltextsearch's chunker only needs one pattern regardless of the
    source form).

    - Already-absolute src on an allowed host (docs.docbits.com or a
      GitBook per-space files CDN): kept as-is.
    - Already-absolute src on any other host (pasted googleusercontent.com
      links etc.): dropped.
    - Relative src (GitBook's `.gitbook/assets/...` convention): resolved
      via the local file's git blob sha, matched against the live page's
      own rendered image urls (see `_fetch_page_blob_to_url_map`) — the
      one thing only the live site knows is which opaque filename segment
      GitBook assigned this particular upload. Dropped (with a warning,
      never a hard failure) when the local file is missing or the live
      page doesn't have a matching image yet.
    """
    images = _iter_raw_images(markdown_text)
    if not images:
        return markdown_text

    blob_map: dict[str, str] | None = None
    out: list[str] = []
    last_end = 0
    for (start, end), src, alt in images:
        out.append(markdown_text[last_end:start])
        last_end = end

        resolved: str | None = None
        if src.startswith("http://") or src.startswith("https://"):
            if _is_allowed_image_host(src):
                resolved = src
        else:
            local_rel_path = os.path.normpath(
                os.path.join(os.path.dirname(md_path), src)
            )
            local_abs_path = os.path.join(REPO_ROOT, local_rel_path)
            if os.path.exists(local_abs_path):
                blob_sha = _run_git(["hash-object", local_rel_path]).strip()
                if blob_map is None:
                    blob_map = _fetch_page_blob_to_url_map(page_url)
                resolved = blob_map.get(blob_sha)

        if resolved:
            out.append(f"![{alt}]({resolved})")
        else:
            print(f"::warning::dropping unresolvable image '{src}' in {md_path}")

    out.append(markdown_text[last_end:])
    return "".join(out)


def _call_endpoint(path: str, payload: dict, *, dry_run: bool) -> dict:
    if dry_run:
        print(f"[dry-run] POST {path}: {json.dumps(payload)[:200]}")
        return {}
    base_url = os.environ["DOCS_INGEST_URL"].rstrip("/")
    key = os.environ["DOCS_INGEST_KEY"]
    request = urllib.request.Request(
        f"{base_url}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "X-Service-Key": key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        print(f"::error::POST {path} failed ({exc.code}): {body}", file=sys.stderr)
        raise


def ingest_md_file(
    md_path: str,
    lang: str,
    commit_sha: str,
    *,
    dry_run: bool,
    published: set[str] | None = None,
) -> None:
    rel = published_rel_path(md_path)
    if rel is None:
        return
    if published is None:
        published = published_paths_from_summary()
    if md_path not in published:
        print(f"::warning::skip {md_path} — not reachable from SUMMARY.md")
        return
    with open(os.path.join(REPO_ROOT, md_path), encoding="utf-8") as handle:
        markdown_text = handle.read()
    if is_no_index(markdown_text):
        print(f"skip {md_path} — marked noIndex: true")
        return
    title = extract_title(markdown_text, fallback=rel.rsplit("/", 1)[-1] or "DocBits")
    url = full_url(rel, lang)
    markdown_text = resolve_images_in_markdown(markdown_text, md_path, url)
    print(f"ingest {md_path} -> {url}")
    _call_endpoint(
        "/docs/ingest",
        {
            "url": url,
            "title": title,
            "lang": lang,
            "commit_sha": commit_sha,
            "markdown": markdown_text,
        },
        dry_run=dry_run,
    )


def delete_md_file(md_path: str, lang: str, *, dry_run: bool) -> None:
    rel = published_rel_path(md_path)
    if rel is None:
        return
    url = full_url(rel, lang)
    print(f"delete {md_path} -> {url}")
    _call_endpoint("/docs/delete", {"url": url, "lang": lang}, dry_run=dry_run)


def run_diff(before: str, after: str, lang: str, *, dry_run: bool) -> None:
    # Both SHAs must already be present locally — the workflow's checkout
    # step uses fetch-depth: 0 so this is a plain local diff, no network
    # call. (Fetching by bare SHA from origin is not reliably supported
    # across git hosting providers, so we deliberately don't attempt it
    # here — a missing SHA should fail loudly instead.)
    output = _run_git(
        [
            "diff",
            "--name-status",
            "--find-renames",
            before,
            after,
            "--",
            README_ROOT,
        ]
    )
    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R"):
            old_path, new_path = parts[1], parts[2]
            delete_md_file(old_path, lang, dry_run=dry_run)
            ingest_md_file(new_path, lang, after, dry_run=dry_run)
        elif status == "D":
            delete_md_file(parts[1], lang, dry_run=dry_run)
        elif status in ("A", "M"):
            ingest_md_file(parts[1], lang, after, dry_run=dry_run)
        else:
            print(f"::warning::unhandled git status '{status}' for {parts[1:]}")


def run_full(lang: str, *, reconcile_only: bool, dry_run: bool) -> None:
    commit_sha = _run_git(["rev-parse", "HEAD"]).strip()
    published_set = published_paths_from_summary()
    published = sorted(published_set)

    if not reconcile_only:
        for md_path in published:
            ingest_md_file(
                md_path, lang, commit_sha, dry_run=dry_run, published=published_set
            )

    urls = []
    for md_path in published:
        rel = published_rel_path(md_path)
        if rel is None:
            continue
        try:
            with open(os.path.join(REPO_ROOT, md_path), encoding="utf-8") as handle:
                markdown_text = handle.read()
        except OSError:
            continue
        if is_no_index(markdown_text):
            continue
        urls.append(full_url(rel, lang))
    print(f"reconcile lang={lang}: keeping {len(urls)} urls")
    _call_endpoint("/docs/reconcile", {"lang": lang, "urls": urls}, dry_run=dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["diff", "full"])
    parser.add_argument("--lang", required=True)
    parser.add_argument("--before")
    parser.add_argument("--after")
    parser.add_argument("--reconcile-only", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned calls instead of hitting DOCS_INGEST_URL.",
    )
    args = parser.parse_args()

    if not args.dry_run and (
        "DOCS_INGEST_URL" not in os.environ or "DOCS_INGEST_KEY" not in os.environ
    ):
        print(
            "::error::DOCS_INGEST_URL / DOCS_INGEST_KEY are not set — "
            "see the repo secrets setup in the CORE-6111 PR description.",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.mode == "diff":
        if not args.before or not args.after:
            parser.error("diff mode requires --before and --after")
        # A force-push or the very first push on a branch can hand us a
        # null `before` SHA (GitHub's documented all-zeros sentinel) —
        # there is nothing to diff against, so fall back to a full sync.
        if set(args.before) == {"0"}:
            run_full(args.lang, reconcile_only=False, dry_run=args.dry_run)
        else:
            run_diff(args.before, args.after, args.lang, dry_run=args.dry_run)
    else:
        run_full(args.lang, reconcile_only=args.reconcile_only, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
