#!/usr/bin/env python3
"""Validate the English import root and publication paths for a main-branch diff."""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import subprocess
import sys

import yaml


def _git(repo: Path, *args: str, optional: bool = False) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, check=False,
    )
    if result.returncode:
        if optional:
            return None
        raise ValueError("Git could not read " + " ".join(args))
    return result.stdout


def _commit(repo: Path, reference: str) -> str:
    result = _git(
        repo, "rev-parse", "--verify", "--end-of-options", reference + "^{commit}",
        optional=True,
    )
    if result is None:
        raise ValueError(f"Cannot resolve Git commit {reference!r}")
    return result.decode("ascii").strip()


def _configuration(repo: Path, commit: str, path: str) -> dict:
    raw = _git(repo, "show", f"{commit}:{path}", optional=True)
    if raw is None:
        raise ValueError(f"Missing configuration: {path}")
    try:
        value = yaml.safe_load(raw)
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML in {path}") from error
    if not isinstance(value, dict):
        raise ValueError(f"Expected a mapping in {path}")
    return value


def _directory(value: object) -> str:
    if not isinstance(value, str) or not value.strip() or "\\" in value:
        raise ValueError("English directory must be a relative POSIX path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe English directory: {value!r}")
    return "" if str(path) == "." else str(path)


def _english_directory(repo: Path, commit: str) -> str:
    """English content root: the `root:` GitBook reads from main's .gitbook.yaml."""
    root = _directory(_configuration(repo, commit, ".gitbook.yaml").get("root"))
    if not root:
        raise ValueError("English directory root must name a folder, not the repository root")
    return root


def _object(repo: Path, commit: str, path: str) -> bytes | None:
    return _git(
        repo, "rev-parse", "--verify", "--end-of-options", f"{commit}:{path}",
        optional=True,
    )


def check(repo: Path, base: str, head: str) -> list[str]:
    """Reject additions or edits under the retired readme/ folder on main.

    English publishes from the active directory only; readme/ is retired, so
    removing its files is fine and anything still written there never publishes.
    """
    base_commit, head_commit = _commit(repo, base), _commit(repo, head)
    active = _english_directory(repo, head_commit)
    raw = _git(repo, "diff", "--name-only", "--no-renames", "-z", base_commit, head_commit)
    changed = set(raw.decode("utf-8", "surrogateescape").split("\0")) - {""}
    errors = []
    for source in sorted(path for path in changed if path.startswith("readme/")):
        if _object(repo, head_commit, source) is None:
            continue
        target = str(PurePosixPath(active) / source.removeprefix("readme/"))
        errors.append(
            f"{source}: readme/ is retired on main and does not publish. "
            f"English GitBook imports {target}; make the change there instead."
        )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base", default="HEAD^1")
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args(argv)
    try:
        errors = check(args.repo, args.base, args.head)
    except (ValueError, OSError) as error:
        print(f"English publication source error: {error}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("English publication source and changed paths are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
