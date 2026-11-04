"""Check the deployed service contract before mutating language indices."""
import io
import json
import os
import sys
import unittest
import urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent))
import docs_search_sync as sync


class ServicePreflightTests(unittest.TestCase):
    def test_old_service_rejects_spanish_before_full_sync_can_write(self):
        error = urllib.error.HTTPError('https://service/docs/search', 422, 'Invalid', {}, io.BytesIO(b'{"detail":"only main/de"}'))
        with patch.dict(os.environ, DOCS_INGEST_URL='https://service', DOCS_INGEST_KEY='secret'), patch.object(sys, 'argv', ['sync', 'full', '--lang', 'es']), patch.object(sync.urllib.request, 'urlopen', side_effect=error) as fetch, patch.object(sync, 'run_full') as full:
            with self.assertRaises(urllib.error.HTTPError):
                sync.main()
        full.assert_not_called()
        self.assertEqual(json.loads(fetch.call_args.args[0].data)['lang'], 'es')
        self.assertTrue(fetch.call_args.args[0].full_url.endswith('/docs/search'))

    def test_preflight_checks_all_nine_languages_without_writes_or_secret_output(self):
        output = io.StringIO()
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"hits": [], "fallback_bm25_only": false}'
        with patch.dict(os.environ, DOCS_INGEST_URL='https://service/private?secret=value', DOCS_INGEST_KEY='service-key'), patch.object(sys, 'argv', ['sync', 'preflight', '--lang', 'all']), patch.object(sync.urllib.request, 'urlopen', return_value=response) as fetch, redirect_stdout(output):
            sync.main()
        self.assertEqual({json.loads(call.args[0].data)['lang'] for call in fetch.call_args_list}, set(sync.VERIFY_QUERIES))
        self.assertTrue(all('/docs/search' in call.args[0].full_url for call in fetch.call_args_list))
        self.assertIn('host=service', output.getvalue())
        for secret in ['service-key', 'secret=value', '/private']:
            self.assertNotIn(secret, output.getvalue())

    def test_dry_run_does_not_contact_service(self):
        with patch.object(sys, 'argv', ['sync', 'full', '--lang', 'es', '--dry-run']), patch.object(sync.urllib.request, 'urlopen') as fetch, patch.object(sync, 'run_full'):
            sync.main()
        fetch.assert_not_called()


if __name__ == '__main__':
    unittest.main()
