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
    default = _configuration(repo, commit, ".gitbook.yaml")
    spaces = _configuration(repo, commit, "gitbook-docs.yaml")
    structure = spaces.get("site", {}).get("structure", [])
    if not isinstance(structure, list):
        raise ValueError("English space structure must be a list")
    english = [
        item["content"]
        for item in structure
        if isinstance(item, dict)
        and isinstance(item.get("content"), dict)
        and item["content"].get("language") == "en"
    ]
    if len(english) != 1:
        raise ValueError("Expected exactly one English GitBook space")
    active = _directory(english[0].get("directory"))
    root = _directory(default.get("root", "./"))
    if root != active:
        raise ValueError(
            f"Default Git Sync root {root!r} differs from active English "
            f"directory {active!r}; align .gitbook.yaml with gitbook-docs.yaml"
        )
    return active


def _object(repo: Path, commit: str, path: str) -> bytes | None:
    return _git(
        repo, "rev-parse", "--verify", "--end-of-options", f"{commit}:{path}",
        optional=True,
    )


def check(repo: Path, base: str, head: str) -> list[str]:
    """Report legacy-only changes; never copy or rewrite published content."""
    base_commit, head_commit = _commit(repo, base), _commit(repo, head)
    active = _english_directory(repo, head_commit)
    raw = _git(repo, "diff", "--name-only", "--no-renames", "-z", base_commit, head_commit)
    changed = set(raw.decode("utf-8", "surrogateescape").split("\0")) - {""}
    errors = []
    for source in sorted(path for path in changed if path.startswith("readme/")):
        relative = source.removeprefix("readme/")
        target = str(PurePosixPath(active) / relative)
        source_object = _object(repo, head_commit, source)
        target_object = _object(repo, head_commit, target)
        if source_object == target_object:
            continue
        if target not in changed or (source_object is not None and target_object is None):
            errors.append(
                f"{source}: English GitBook imports {target}. Update the reviewed "
                "published counterpart, preserving newer public content; a legacy-only "
                "readme change does not publish."
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
