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
import io
from contextlib import redirect_stdout
from pathlib import Path
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
        self.output = io.StringIO()
        self.stdout = redirect_stdout(self.output)
        self.stdout.__enter__()
        sync.REPO_ROOT = self._tmpdir.name

    def tearDown(self):
        sync.REPO_ROOT = self._orig_repo_root
        self._tmpdir.cleanup()
        self.stdout.__exit__(None, None, None)

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
        with patch.object(sync, "_fetch_page_blob_to_url_map", return_value={}):
            result = sync.resolve_images_in_markdown(
                markdown, "readme/x.md", "https://docs.docbits.com/x"
            )
        self.assertIn("dropping unresolvable image", self.output.getvalue())
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


class PublishedImageRegressionTests(unittest.TestCase):
    def setUp(self):
        sync._page_blob_url_cache.clear()

    def test_navigation_summary_is_not_an_ingestable_page_or_a_warning(self):
        output = io.StringIO()
        with redirect_stdout(output), patch.object(sync, "_call_endpoint") as endpoint:
            sync.ingest_md_file(sync.SUMMARY_PATH, 'main', 'sha', dry_run=True, published=set())
        endpoint.assert_not_called()
        self.assertNotIn('::warning::', output.getvalue())

    def test_markdown_escaped_ampersand_matches_the_published_source_url(self):
        original = 'https://files.gitbook.com/image.png?alt=media&token=abc'
        proxy = 'https://docs.docbits.com/~gitbook/image?url=x&sign=s'
        with patch.object(sync, '_fetch_page_blob_to_url_map', return_value={original: proxy}):
            result = sync.resolve_images_in_markdown(
                r'![A](https://files.gitbook.com/image.png?alt=media\&token=abc)',
                'readme/page.md', 'https://docs.docbits.com/page')
        self.assertEqual(result, f'![A]({proxy})')

    def test_indented_code_is_not_an_image_but_list_images_are(self):
        self.assertEqual(sync._iter_raw_images('Text.\n\n    ![Example](missing.png)\n'), [])
        images = sync._iter_raw_images('- A list item\n\n    ![Screen](screen.png)\n')
        self.assertEqual([src for _, src, _ in images], ['screen.png'])

    def test_transient_page_timeout_recovers_without_discarding_the_image(self):
        original = 'https://example.org/screenshot.png'
        proxy = 'https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Fexample.org%2Fscreenshot.png&sign=s'
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = ('<img src="' + proxy + '">').encode()
        output = io.StringIO()
        with redirect_stdout(output), patch.object(sync.urllib.request, 'urlopen', side_effect=[TimeoutError('slow page'), response]) as fetch, patch.object(sync.time, 'sleep') as sleep:
            result = sync.resolve_images_in_markdown(f'![A]({original})', 'readme/page.md', 'https://docs.docbits.com/page')
        self.assertEqual(result, f'![A]({proxy})')
        self.assertEqual(fetch.call_count, 2)
        sleep.assert_called_once_with(2)
        self.assertNotIn('::warning::', output.getvalue())

    def test_transient_page_gateway_error_recovers_before_caching_a_failure(self):
        original = 'https://example.org/screenshot.png'
        proxy = 'https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Fexample.org%2Fscreenshot.png&sign=s'
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = ('<img src="' + proxy + '">').encode()
        error = sync.urllib.error.HTTPError('https://docs.docbits.com/page', 503, 'Unavailable', {}, io.BytesIO())
        with redirect_stdout(io.StringIO()), patch.object(sync.urllib.request, 'urlopen', side_effect=[error, response]) as fetch, patch.object(sync.time, 'sleep'):
            first = sync._fetch_page_blob_to_url_map('https://docs.docbits.com/page')
            second = sync._fetch_page_blob_to_url_map('https://docs.docbits.com/page')
        self.assertEqual(first[original], proxy)
        self.assertEqual(second, first)
        self.assertEqual(fetch.call_count, 2)

    def test_missing_published_page_still_warns_without_retrying_a_404(self):
        error = sync.urllib.error.HTTPError('https://docs.docbits.com/missing', 404, 'Missing', {}, io.BytesIO())
        output = io.StringIO()
        with redirect_stdout(output), patch.object(sync.urllib.request, 'urlopen', side_effect=error) as fetch, patch.object(sync.time, 'sleep') as sleep:
            mapping = sync._fetch_page_blob_to_url_map('https://docs.docbits.com/missing')
        self.assertEqual(mapping, {})
        self.assertEqual(fetch.call_count, 1)
        sleep.assert_not_called()
        self.assertIn('::warning::could not fetch', output.getvalue())

    def test_persistent_page_timeout_still_warns_after_bounded_retries(self):
        output = io.StringIO()
        with redirect_stdout(output), patch.object(sync.urllib.request, 'urlopen', side_effect=TimeoutError('unavailable')) as fetch, patch.object(sync.time, 'sleep') as sleep:
            mapping = sync._fetch_page_blob_to_url_map('https://docs.docbits.com/unavailable')
        self.assertEqual(mapping, {})
        self.assertEqual(fetch.call_count, 3)
        self.assertEqual(sleep.call_count, 2)
        self.assertEqual(output.getvalue().count('::warning::'), 1)

    def test_external_image_uses_existing_signed_same_origin_proxy(self):
        original = "https://lh7-us.googleusercontent.com/screenshot"
        proxy = "https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fscreenshot&width=768&sign=real-signature&sv=3"
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = (
            '<img src="' + proxy.replace('&', '&amp;') + '">'
        ).encode()
        with patch.object(sync.urllib.request, "urlopen", return_value=response) as fetch:
            result = sync.resolve_images_in_markdown(
                f"![Screenshot]({original})", "readme/page.md", "https://docs.docbits.com/page"
            )
        self.assertEqual(result, f"![Screenshot]({proxy})")
        self.assertEqual(fetch.call_count, 1)

    def test_external_markdown_escapes_are_normalized_before_lookup(self):
        original = "https://lh7-us.googleusercontent.com/screen_name"
        proxy = "https://docs.docbits.com/~gitbook/image?url=x&sign=s"
        with patch.object(sync, "_fetch_page_blob_to_url_map", return_value={original: proxy}):
            result = sync.resolve_images_in_markdown(
                r"![Screen](https://lh7-us.googleusercontent.com/screen\_name)",
                "readme/page.md", "https://docs.docbits.com/page"
            )
        self.assertEqual(result, f"![Screen]({proxy})")

    def test_untrusted_proxy_host_cannot_resolve_external_image(self):
        original = "https://example.org/screenshot.png"
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = (
            '<img src="https://evil.example/~gitbook/image?url=https%3A%2F%2Fexample.org%2Fscreenshot.png&amp;sign=x">'
        ).encode()
        with patch.object(sync.urllib.request, "urlopen", return_value=response):
            mapping = sync._fetch_page_blob_to_url_map("https://docs.docbits.com/page")
        self.assertNotIn(original, mapping)

    def test_literal_images_in_fenced_code_are_not_rewritten_or_fetched(self):
        markdown = "```html\n<img src=\"../../.gitbook/assets/POShipmentTable.png\">\n```\n~~~\n![Example](missing.png)\n~~~\n"
        with patch.object(sync, "_fetch_page_blob_to_url_map") as fetch:
            result = sync.resolve_images_in_markdown(markdown, "readme/page.md", "https://docs.docbits.com/page")
        self.assertEqual(result, markdown)
        fetch.assert_not_called()

    def test_inline_code_example_is_not_an_image(self):
        self.assertEqual(sync._iter_raw_images('Use `![Example](missing.png)` here.'), [])

    def test_markdown_angle_destination_and_balanced_parentheses_are_complete(self):
        text = '![A](<../.gitbook/assets/workflow_add_button.png>) ![B](../.gitbook/assets/image%20(28).png)'
        images = sync._iter_raw_images(text)
        self.assertEqual([src for _, src, _ in images], [
            '../.gitbook/assets/workflow_add_button.png', '../.gitbook/assets/image%20(28).png'
        ])

    def test_percent_encoded_local_asset_is_resolved(self):
        with tempfile.TemporaryDirectory() as root:
            asset = Path(root) / 'readme/.gitbook/assets/image (28).png'
            asset.parent.mkdir(parents=True)
            asset.write_bytes(b'png')
            with patch.object(sync, 'REPO_ROOT', root):
                sha = sync._run_git(['hash-object', 'readme/.gitbook/assets/image (28).png']).strip()
                target = 'https://578966019-files.gitbook.io/git-blob-' + sha
                with patch.object(sync, '_fetch_page_blob_to_url_map', return_value={sha: target}):
                    result = sync.resolve_images_in_markdown(
                        '![A](../.gitbook/assets/image%20(28).png)', 'readme/sub/page.md', 'https://docs.docbits.com/sub/page'
                    )
            self.assertEqual(result, f'![A]({target})')


if __name__ == "__main__":
    unittest.main()
