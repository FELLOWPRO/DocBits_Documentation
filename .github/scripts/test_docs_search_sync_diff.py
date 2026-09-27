"""Tests for docs_search_sync.py's diff-mode git handling (CORE-6111
review). Exercises real git repos (tempdir, stdlib subprocess) rather than
hand-built name-status text, so the NUL-parsing fix is checked against
what git actually emits — including its C-style path quoting, which is
exactly what `-z` sidesteps.

Nothing here hits the network — `_call_endpoint` is monkeypatched in
every test that goes through `run_diff`/`ingest_md_file`/`delete_md_file`.

Run with either:
    python3 .github/scripts/test_docs_search_sync_diff.py
    python3 -m pytest .github/scripts/test_docs_search_sync_diff.py
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
import unittest.mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import docs_search_sync as sync  # noqa: E402


def _run(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=True
    )


class _GitRepoTestCase(unittest.TestCase):
    """A throwaway git repo under readme/, with helpers to write/commit
    files and capture what run_diff would have sent to /docs/ingest and
    /docs/delete without ever calling the network."""

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.repo = self._tmpdir.name
        _run(self.repo, "init", "-q", "-b", "main")
        _run(self.repo, "config", "user.email", "test@example.com")
        _run(self.repo, "config", "user.name", "Test")

        self._orig_repo_root = sync.REPO_ROOT
        sync.REPO_ROOT = self.repo
        sync._page_blob_url_cache.clear()

        # A placeholder commit outside readme/ so the very first real
        # commit under test has something to diff against.
        self._write(".gitkeep", "")
        self.initial_sha = self._commit("init")

        self.calls: list[tuple[str, dict]] = []

        def _fake_call_endpoint(path, payload, *, dry_run):
            self.calls.append((path, payload))
            return {}

        self._call_endpoint_patcher = unittest.mock.patch.object(
            sync, "_call_endpoint", side_effect=_fake_call_endpoint
        )
        self._call_endpoint_patcher.start()

    def tearDown(self):
        self._call_endpoint_patcher.stop()
        sync.REPO_ROOT = self._orig_repo_root
        self._tmpdir.cleanup()

    def _write(self, rel_path: str, content: str) -> None:
        abs_path = os.path.join(self.repo, rel_path)
        os.makedirs(os.path.dirname(abs_path) or self.repo, exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as handle:
            handle.write(content)

    def _remove(self, rel_path: str) -> None:
        os.remove(os.path.join(self.repo, rel_path))

    def _rename(self, old_rel: str, new_rel: str) -> None:
        abs_new = os.path.join(self.repo, new_rel)
        os.makedirs(os.path.dirname(abs_new) or self.repo, exist_ok=True)
        os.rename(os.path.join(self.repo, old_rel), abs_new)

    def _commit(self, message: str) -> str:
        _run(self.repo, "add", "-A")
        _run(self.repo, "commit", "-q", "-m", message)
        return _run(self.repo, "rev-parse", "HEAD").stdout.strip()

    def _diff_z_records(self, before: str, after: str):
        result = _run(
            self.repo,
            "diff",
            "--name-status",
            "--find-renames",
            "-z",
            before,
            after,
            "--",
            "readme",
        )
        return sync._parse_name_status_z(result.stdout)


class TestNameStatusZParsingHandlesUmlautsAndSpaces(_GitRepoTestCase):
    def test_added_file_with_umlauts_and_spaces_in_the_name(self):
        self._write("readme/Überblick Setup.md", "# Überblick\ntext\n")
        after = self._commit("add umlaut file")

        records = self._diff_z_records(self.initial_sha, after)

        self.assertEqual(records, [("A", ["readme/Überblick Setup.md"])])

    def test_deleted_file_with_umlauts_and_spaces_in_the_name(self):
        self._write("readme/Prüfung Übersicht.md", "# x\ntext\n")
        before = self._commit("add")
        self._remove("readme/Prüfung Übersicht.md")
        after = self._commit("delete")

        records = self._diff_z_records(before, after)

        self.assertEqual(records, [("D", ["readme/Prüfung Übersicht.md"])])

    def test_renamed_file_with_umlauts_and_spaces_in_both_names(self):
        # Enough repeated content for git's similarity-based rename
        # detection to actually fire (default threshold 50%).
        body = "# Heading\n" + ("Some prose about configuration. " * 20) + "\n"
        self._write("readme/Alte Übersicht.md", body)
        before = self._commit("add")
        self._rename("readme/Alte Übersicht.md", "readme/Neue Übersicht ändern.md")
        after = self._commit("rename")

        records = self._diff_z_records(before, after)

        self.assertEqual(len(records), 1)
        status, paths = records[0]
        self.assertTrue(status.startswith("R"))
        self.assertEqual(
            paths, ["readme/Alte Übersicht.md", "readme/Neue Übersicht ändern.md"]
        )


class TestRenameIngestsBeforeDeleting(_GitRepoTestCase):
    def test_rename_calls_ingest_before_delete(self):
        body = "# Heading\n" + ("Some prose about configuration. " * 20) + "\n"
        self._write("readme/SUMMARY.md", "# Table of contents\n\n* [X](old.md)\n")
        self._write("readme/old.md", body)
        before = self._commit("add")

        self._rename("readme/old.md", "readme/new.md")
        self._write(
            "readme/SUMMARY.md", "# Table of contents\n\n* [X](new.md)\n"
        )
        after = self._commit("rename")

        sync.run_diff(before, after, "main", dry_run=False)

        paths_in_call_order = [call_path for call_path, _ in self.calls]
        # A page must never have a moment with zero search presence: the
        # new URL is ingested BEFORE the old one is deleted (Codex review).
        assert paths_in_call_order.index("/docs/ingest") < paths_in_call_order.index(
            "/docs/delete"
        )
        ingest_payload = self.calls[paths_in_call_order.index("/docs/ingest")][1]
        assert ingest_payload["url"] == "https://docs.docbits.com/new"
        delete_payload = self.calls[paths_in_call_order.index("/docs/delete")][1]
        assert delete_payload["url"] == "https://docs.docbits.com/old"


class TestSummaryChangeIngestsNewlyPublishedPages(_GitRepoTestCase):
    def test_a_page_not_itself_touched_but_newly_linked_from_summary_is_ingested(self):
        # `orphan.md` exists from the start but SUMMARY.md doesn't link to
        # it yet — not published, so not ingested.
        self._write("readme/SUMMARY.md", "# Table of contents\n\n* [Home](README.md)\n")
        self._write("readme/README.md", "# Home\ntext\n")
        self._write("readme/orphan.md", "# Orphan\nThis page existed all along.\n")
        before = self._commit("initial")

        # SUMMARY.md changes to link the pre-existing orphan page — the
        # orphan.md FILE ITSELF is untouched in this commit.
        self._write(
            "readme/SUMMARY.md",
            "# Table of contents\n\n* [Home](README.md)\n* [Orphan](orphan.md)\n",
        )
        after = self._commit("publish orphan via SUMMARY.md")

        sync.run_diff(before, after, "main", dry_run=False)

        ingested_urls = {
            payload["url"] for path, payload in self.calls if path == "/docs/ingest"
        }
        assert "https://docs.docbits.com/orphan" in ingested_urls

    def test_a_page_not_linked_anywhere_is_never_ingested(self):
        self._write("readme/SUMMARY.md", "# Table of contents\n\n* [Home](README.md)\n")
        self._write("readme/README.md", "# Home\ntext\n")
        before = self._commit("initial")

        self._write("readme/SUMMARY.md", "# Table of contents\n\n* [Home](README.md)\n \n")
        after = self._commit("touch summary, no real link change")

        sync.run_diff(before, after, "main", dry_run=False)

        ingested_urls = {
            payload["url"] for path, payload in self.calls if path == "/docs/ingest"
        }
        assert ingested_urls == set()


if __name__ == "__main__":
    unittest.main()
