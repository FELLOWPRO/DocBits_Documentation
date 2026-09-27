"""Tests for docs_search_sync.py's image resolution + host filtering
(CORE-6111). Stdlib only (unittest + unittest.mock) — no pytest/requests
dependency needed, since this repo has none. Run with either:

    python3 -m unittest .github/scripts/test_docs_search_sync.py
    python3 -m pytest .github/scripts/test_docs_search_sync.py

Nothing here hits the network — `_fetch_page_blob_to_url_map` (the one
function that does) is mocked in every resolution test.
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import docs_search_sync as sync  # noqa: E402


class AllowedImageHostTests(unittest.TestCase):
    def test_docs_docbits_com_is_allowed(self):
        self.assertTrue(sync._is_allowed_image_host("https://docs.docbits.com/x.png"))

    def test_gitbook_per_space_files_host_is_allowed(self):
        self.assertTrue(
            sync._is_allowed_image_host(
                "https://578966019-files.gitbook.io/~/files/v0/b/x/o/y?alt=media"
            )
        )
        self.assertTrue(
            sync._is_allowed_image_host(
                "https://2396827744-files.gitbook.io/~/files/v0/b/x/o/y?alt=media"
            )
        )

    def test_pasted_third_party_host_is_not_allowed(self):
        self.assertFalse(
            sync._is_allowed_image_host("https://lh7-us.googleusercontent.com/abc")
        )

    def test_a_host_that_merely_contains_gitbook_io_without_the_files_hyphen_form_is_not_allowed(
        self,
    ):
        self.assertFalse(sync._is_allowed_image_host("https://gitbook.io/x.png"))
        self.assertFalse(sync._is_allowed_image_host("https://evilgitbook.io/x.png"))


class IterRawImagesTests(unittest.TestCase):
    def test_extracts_gitbook_html_figure_form(self):
        markdown = (
            '<figure><img src="../../.gitbook/assets/x.png" '
            'alt="Some Alt"><figcaption></figcaption></figure>'
        )
        images = sync._iter_raw_images(markdown)
        self.assertEqual(len(images), 1)
        _, src, alt = images[0]
        self.assertEqual(src, "../../.gitbook/assets/x.png")
        self.assertEqual(alt, "Some Alt")

    def test_extracts_plain_markdown_form(self):
        markdown = "before ![Alt Text](https://docs.docbits.com/x.png) after"
        images = sync._iter_raw_images(markdown)
        self.assertEqual(len(images), 1)
        _, src, alt = images[0]
        self.assertEqual(src, "https://docs.docbits.com/x.png")
        self.assertEqual(alt, "Alt Text")

    def test_extracts_both_forms_in_document_order(self):
        markdown = (
            "![First](a.png)\n"
            '<figure><img src="b.png" alt="Second"></figure>\n'
            "![Third](c.png)\n"
        )
        images = sync._iter_raw_images(markdown)
        self.assertEqual([src for _, src, _ in images], ["a.png", "b.png", "c.png"])


class ResolveImagesInMarkdownTests(unittest.TestCase):
    def setUp(self):
        sync._page_blob_url_cache.clear()
        self._tmpdir = tempfile.TemporaryDirectory()
        self._orig_repo_root = sync.REPO_ROOT
        sync.REPO_ROOT = self._tmpdir.name

    def tearDown(self):
        sync.REPO_ROOT = self._orig_repo_root
        self._tmpdir.cleanup()

    def _write_local_asset(self, rel_path: str, content: bytes = b"fake-png-bytes"):
        abs_path = os.path.join(self._tmpdir.name, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "wb") as handle:
            handle.write(content)

    def test_already_allowed_absolute_image_is_kept_as_is_without_a_network_call(self):
        markdown = "![Alt](https://docs.docbits.com/already/absolute.png)"
        with patch.object(sync, "_fetch_page_blob_to_url_map") as mock_fetch:
            result = sync.resolve_images_in_markdown(
                markdown, "readme/x.md", "https://docs.docbits.com/x"
            )
        mock_fetch.assert_not_called()
        self.assertIn("https://docs.docbits.com/already/absolute.png", result)

    def test_already_absolute_disallowed_host_is_dropped(self):
        markdown = "![Alt](https://lh7-us.googleusercontent.com/pasted.png)"
        result = sync.resolve_images_in_markdown(
            markdown, "readme/x.md", "https://docs.docbits.com/x"
        )
        self.assertNotIn("googleusercontent.com", result)
        self.assertEqual(result.count("!["), 0)

    def test_relative_image_is_resolved_via_the_live_pages_blob_map(self):
        self._write_local_asset("readme/.gitbook/assets/x.png")
        blob_sha = sync._run_git(["hash-object", "readme/.gitbook/assets/x.png"]).strip()
        resolved_url = (
            "https://578966019-files.gitbook.io/~/files/v0/b/x/o/"
            "spaces%2FS%2Fuploads%2Fgit-blob-" + blob_sha + "%2Fx.png?alt=media"
        )
        markdown = '<figure><img src="../.gitbook/assets/x.png" alt="X"></figure>'
        with patch.object(
            sync,
            "_fetch_page_blob_to_url_map",
            return_value={blob_sha: resolved_url},
        ):
            result = sync.resolve_images_in_markdown(
                markdown, "readme/sub/page.md", "https://docs.docbits.com/sub/page"
            )
        self.assertIn(f"![X]({resolved_url})", result)

    def test_relative_image_whose_local_file_is_missing_is_dropped(self):
        markdown = '<figure><img src="../.gitbook/assets/missing.png" alt="X"></figure>'
        with patch.object(sync, "_fetch_page_blob_to_url_map") as mock_fetch:
            result = sync.resolve_images_in_markdown(
                markdown, "readme/sub/page.md", "https://docs.docbits.com/sub/page"
            )
        mock_fetch.assert_not_called()
        self.assertEqual(result.count("!["), 0)

    def test_relative_image_not_found_on_the_live_page_yet_is_dropped(self):
        self._write_local_asset("readme/.gitbook/assets/x.png")
        markdown = '<figure><img src="../.gitbook/assets/x.png" alt="X"></figure>'
        with patch.object(sync, "_fetch_page_blob_to_url_map", return_value={}):
            result = sync.resolve_images_in_markdown(
                markdown, "readme/sub/page.md", "https://docs.docbits.com/sub/page"
            )
        self.assertEqual(result.count("!["), 0)

    def test_multiple_images_resolve_independently_and_text_around_them_is_preserved(
        self,
    ):
        self._write_local_asset("readme/.gitbook/assets/a.png")
        blob_sha = sync._run_git(["hash-object", "readme/.gitbook/assets/a.png"]).strip()
        resolved_url = "https://578966019-files.gitbook.io/x/git-blob-" + blob_sha
        markdown = (
            "Intro text.\n"
            '<figure><img src="../.gitbook/assets/a.png" alt="A"></figure>\n'
            "Middle text.\n"
            "![B](https://lh7-us.googleusercontent.com/dropped.png)\n"
            "Trailing text.\n"
        )
        with patch.object(
            sync, "_fetch_page_blob_to_url_map", return_value={blob_sha: resolved_url}
        ):
            result = sync.resolve_images_in_markdown(
                markdown, "readme/sub/page.md", "https://docs.docbits.com/sub/page"
            )
        self.assertIn("Intro text.", result)
        self.assertIn("Middle text.", result)
        self.assertIn("Trailing text.", result)
        self.assertIn(resolved_url, result)
        self.assertNotIn("googleusercontent.com", result)


if __name__ == "__main__":
    unittest.main()
