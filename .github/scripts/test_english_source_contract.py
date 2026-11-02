"""Regression contracts for the English GitBook source and main-branch changes."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".github/scripts/english_source_contract.py"


def test_default_git_sync_root_matches_active_english_space():
    default = yaml.safe_load((ROOT / ".gitbook.yaml").read_text())
    site = yaml.safe_load((ROOT / "gitbook-docs.yaml").read_text())
    english = [
        item["content"]["directory"]
        for item in site["site"]["structure"]
        if item.get("content", {}).get("language") == "en"
    ]
    assert len(english) == 1
    assert Path(default["root"]) == Path(english[0]), (
        "Default Git Sync root must match the active English GitBook directory; "
        "otherwise approved English changes can remain unpublished."
    )


@pytest.fixture
def checker():
    spec = importlib.util.spec_from_file_location("english_source_contract", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(repo, *args):
    return subprocess.run(
        [
            "git", "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false",
            "-c", "user.name=Source contract test",
            "-c", "user.email=source-contract@example.invalid",
            "-C", str(repo), *args,
        ],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def write(repo, relative, data):
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data if isinstance(data, bytes) else data.encode())


def commit(repo):
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "fixture")
    return git(repo, "rev-parse", "HEAD")


@pytest.fixture
def repository(tmp_path):
    git(tmp_path, "init", "-q")
    write(tmp_path, ".gitbook.yaml", "root: ./docbits/\n")
    write(
        tmp_path, "gitbook-docs.yaml",
        "site:\n  structure:\n"
        "    - content:\n        directory: ./docbits\n        language: en\n"
        "    - content:\n        directory: ./deutsch\n        language: de\n",
    )
    write(tmp_path, "readme/page.md", "# Earlier source\n")
    write(tmp_path, "docbits/page.md", "# Public page\n\nNewer public section.\n")
    write(tmp_path, "deutsch/page.md", "# Deutsch\n")
    write(tmp_path, "readme/.gitbook/assets/diagram (EN).png", b"old")
    write(tmp_path, "docbits/.gitbook/assets/diagram (EN).png", b"old")
    return tmp_path, commit(tmp_path)


def test_rejects_legacy_source_only_page_change(checker, repository):
    repo, base = repository
    write(repo, "readme/page.md", "# Approved but not imported\n")
    errors = checker.check(repo, base, commit(repo))
    assert any("readme/page.md" in error and "docbits/page.md" in error for error in errors)


def test_accepts_published_counterpart_without_overwriting_newer_public_sections(
    checker, repository,
):
    repo, base = repository
    write(repo, "readme/page.md", "# Corrected source\n")
    published = "# Corrected public page\n\nNewer public section.\n"
    write(repo, "docbits/page.md", published)
    assert checker.check(repo, base, commit(repo)) == []
    assert (repo / "docbits/page.md").read_text() == published


def test_accepts_canonical_catchup_when_content_is_already_published(checker, repository):
    repo, base = repository
    write(repo, "readme/page.md", (repo / "docbits/page.md").read_bytes())
    assert checker.check(repo, base, commit(repo)) == []


@pytest.mark.parametrize("relative", ["docbits/page.md", "deutsch/page.md"])
def test_accepts_active_source_and_translation_changes(checker, repository, relative):
    repo, base = repository
    write(repo, relative, "# Updated public content\n")
    assert checker.check(repo, base, commit(repo)) == []


def test_rejects_source_only_binary_asset_with_spaces(checker, repository):
    repo, base = repository
    write(repo, "readme/.gitbook/assets/diagram (EN).png", b"\x00\xffnew")
    errors = checker.check(repo, base, commit(repo))
    assert any("docbits/.gitbook/assets/diagram (EN).png" in error for error in errors)


def test_accepts_updated_published_asset(checker, repository):
    repo, base = repository
    for directory in ("readme", "docbits"):
        write(repo, directory + "/.gitbook/assets/diagram (EN).png", b"\x00\xffnew")
    assert checker.check(repo, base, commit(repo)) == []


def test_rejects_new_source_page_without_imported_counterpart(checker, repository):
    repo, base = repository
    write(repo, "readme/Field rules (EN).md", "# New English page\n")
    errors = checker.check(repo, base, commit(repo))
    assert any("docbits/Field rules (EN).md" in error for error in errors)


def test_accepts_new_page_in_both_directories(checker, repository):
    repo, base = repository
    for directory in ("readme", "docbits"):
        write(repo, directory + "/new.md", "# Reviewed new page\n")
    assert checker.check(repo, base, commit(repo)) == []


def test_rejects_unpublished_page_removal(checker, repository):
    repo, base = repository
    (repo / "readme/page.md").unlink()
    assert checker.check(repo, base, commit(repo))


def test_accepts_removal_from_both_directories(checker, repository):
    repo, base = repository
    for directory in ("readme", "docbits"):
        (repo / directory / "page.md").unlink()
    assert checker.check(repo, base, commit(repo)) == []


def test_rejects_deleted_public_target_when_source_remains(checker, repository):
    repo, base = repository
    write(repo, "readme/page.md", "# Still requires publication\n")
    (repo / "docbits/page.md").unlink()
    errors = checker.check(repo, base, commit(repo))
    assert any("docbits/page.md" in error for error in errors)


def test_accepts_no_content_changes(checker, repository):
    repo, base = repository
    assert checker.check(repo, base, base) == []


def test_rejects_default_root_that_disagrees_with_active_space(checker, repository):
    repo, base = repository
    write(repo, ".gitbook.yaml", "root: ./readme/\n")
    with pytest.raises(ValueError, match="root"):
        checker.check(repo, base, commit(repo))


@pytest.mark.parametrize("directory", ["../outside", "/absolute", "docbits/../outside"])
def test_rejects_unsafe_active_directory(checker, repository, directory):
    repo, base = repository
    write(
        repo, "gitbook-docs.yaml",
        f"site:\n  structure:\n    - content:\n        directory: {directory}\n        language: en\n",
    )
    with pytest.raises(ValueError, match="directory"):
        checker.check(repo, base, commit(repo))


def test_rejects_missing_english_space(checker, repository):
    repo, base = repository
    write(repo, "gitbook-docs.yaml", "site:\n  structure: []\n")
    with pytest.raises(ValueError, match="English"):
        checker.check(repo, base, commit(repo))


def test_rejects_duplicate_english_space(checker, repository):
    repo, base = repository
    existing = (repo / "gitbook-docs.yaml").read_text()
    write(repo, "gitbook-docs.yaml", existing + "    - content:\n        directory: ./other\n        language: en\n")
    with pytest.raises(ValueError, match="English"):
        checker.check(repo, base, commit(repo))


def test_cli_reports_unpublished_path_and_returns_failure(checker, repository, capsys):
    repo, base = repository
    write(repo, "readme/page.md", "# Requires publication\n")
    head = commit(repo)
    assert checker.main(["--repo", str(repo), "--base", base, "--head", head]) == 1
    assert "docbits/page.md" in capsys.readouterr().err


def test_cli_accepts_active_source_change(checker, repository, capsys):
    repo, base = repository
    write(repo, "docbits/page.md", "# Public correction\n")
    head = commit(repo)
    assert checker.main(["--repo", str(repo), "--base", base, "--head", head]) == 0
    assert "English publication source" in capsys.readouterr().out


def test_cli_reports_invalid_ref_without_traceback(checker, repository, capsys):
    repo, base = repository
    assert checker.main(["--repo", str(repo), "--base", base, "--head", "missing-ref"]) == 2
    output = capsys.readouterr().err
    assert "missing-ref" in output
    assert "Traceback" not in output


def test_script_entrypoint_rejects_unpublished_change(repository):
    repo, base = repository
    write(repo, "readme/page.md", "# Requires a published counterpart\n")
    head = commit(repo)
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo", str(repo), "--base", base, "--head", head],
        capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "docbits/page.md" in result.stderr
