"""Offline contracts for ingestion, reconciliation and the live verifier."""
import io
import os
import sys
import tempfile
import unittest
import urllib.error
from contextlib import ExitStack, redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent))
import docs_search_sync as sync


class RuntimeContracts(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.output = self.stack.enter_context(redirect_stdout(io.StringIO()))
        self.errors = self.stack.enter_context(redirect_stderr(io.StringIO()))
        self.stack.enter_context(patch.object(sync, '_live_urls', return_value=None))

    def test_full_ingest_preserves_images_and_reconciles_only_published_indexable_pages(self):
        with tempfile.TemporaryDirectory() as root:
            readme = Path(root) / 'readme'
            readme.mkdir()
            (readme / 'SUMMARY.md').write_text('* [A](a.md)\n* [Draft](draft.md)\n')
            (readme / 'a.md').write_text('# A\n![Screen](https://docs.docbits.com/screen.png)\n')
            (readme / 'draft.md').write_text('---\nnoIndex: true\n---\n# Draft\n')
            (readme / 'orphan.md').write_text('# Not published\n')
            with patch.object(sync, 'REPO_ROOT', root), patch.object(sync, '_run_git', return_value='sha'), patch.object(sync, '_call_endpoint', return_value={}) as endpoint:
                sync.run_full('main', reconcile_only=False, dry_run=False)
            self.assertEqual([c.args[0] for c in endpoint.call_args_list], ['/docs/ingest', '/docs/reconcile'])
            self.assertIn('![Screen](https://docs.docbits.com/screen.png)', endpoint.call_args_list[0].args[1]['markdown'])
            self.assertEqual(endpoint.call_args_list[-1].args[1]['urls'], ['https://docs.docbits.com/a'])
            self.assertNotIn('::warning::', self.output.getvalue())

    def test_verify_passes_all_supported_languages(self):
        for lang in sync.VERIFY_QUERIES:
            with self.subTest(lang=lang):
                result = {'hits': [{'url': sync.full_url(sync.VERIFY_PAGE, lang)}], 'fallback_bm25_only': False}
                with patch.object(sync, '_call_endpoint', return_value=result) as endpoint:
                    sync.verify_lang(lang, dry_run=False)
                self.assertEqual(endpoint.call_args.args[1]['lang'], lang)

    def test_verify_rejects_missing_page_empty_index_and_bm25_fallback(self):
        for result in [
            {'hits': []},
            {'hits': [{'url': sync.full_url('unrelated', 'de')}]},
            {'hits': [{'url': sync.full_url(sync.VERIFY_PAGE, 'de')}], 'fallback_bm25_only': True},
        ]:
            with self.subTest(result=result), patch.object(sync, '_call_endpoint', return_value=result):
                with self.assertRaises(SystemExit):
                    sync.verify_lang('de', dry_run=False)

    def test_verify_rejects_foreign_space_and_origin_even_with_a_valid_hit(self):
        for lang, wrong_url in [
            ('main', 'https://docs.docbits.com/deutsch/foreign'),
            ('main', 'https://docs.docbits.com.evil.example/foreign'),
            ('de', 'https://docs.docbits.com/deutschland/foreign'),
        ]:
            result = {'hits': [{'url': sync.full_url(sync.VERIFY_PAGE, lang)}, {'url': wrong_url}]}
            with self.subTest(lang=lang, wrong_url=wrong_url), patch.object(sync, '_call_endpoint', return_value=result):
                with self.assertRaises(SystemExit):
                    sync.verify_lang(lang, dry_run=False)

    def test_ingest_retries_transient_gateway_errors_without_changing_payload(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"ok": true}'
        error = urllib.error.HTTPError('https://service/docs/ingest', 502, 'Gateway', {}, io.BytesIO(b'transient'))
        with patch.dict(os.environ, DOCS_INGEST_URL='https://service', DOCS_INGEST_KEY='test-key'), patch.object(sync.urllib.request, 'urlopen', side_effect=[error, response]) as fetch, patch.object(sync.time, 'sleep') as sleep:
            result = sync._call_endpoint('/docs/ingest', {'url': 'https://docs.docbits.com/a'}, dry_run=False)
        self.assertTrue(result['ok'])
        self.assertEqual(fetch.call_count, 2)
        self.assertEqual(fetch.call_args_list[0].args[0].data, fetch.call_args_list[1].args[0].data)
        sleep.assert_called_once_with(5)
        self.assertNotIn('test-key', self.output.getvalue() + self.errors.getvalue())

    def test_client_errors_are_not_retried(self):
        error = urllib.error.HTTPError('https://service/docs/ingest', 422, 'Invalid', {}, io.BytesIO(b'invalid'))
        with patch.dict(os.environ, DOCS_INGEST_URL='https://service', DOCS_INGEST_KEY='test-key'), patch.object(sync.urllib.request, 'urlopen', side_effect=error) as fetch, patch.object(sync.time, 'sleep') as sleep:
            with self.assertRaises(urllib.error.HTTPError):
                sync._call_endpoint('/docs/ingest', {}, dry_run=False)
        self.assertEqual(fetch.call_count, 1)
        sleep.assert_not_called()

    def test_timeout_exhaustion_fails_instead_of_publishing_a_false_success(self):
        with patch.dict(os.environ, DOCS_INGEST_URL='https://service', DOCS_INGEST_KEY='test-key'), patch.object(sync.urllib.request, 'urlopen', side_effect=TimeoutError('timeout')) as fetch, patch.object(sync.time, 'sleep'):
            with self.assertRaises(TimeoutError):
                sync._call_endpoint('/docs/ingest', {}, dry_run=False)
        self.assertEqual(fetch.call_count, 4)
        self.assertIn('::error::', self.errors.getvalue())


if __name__ == '__main__':
    unittest.main()
