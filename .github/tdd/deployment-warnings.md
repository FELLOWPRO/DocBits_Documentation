# Documentation deployment warnings: verification

Journeys derived from the deployment warning report and the requirement to use
local k9s runners.

- Every active documentation job must execute on the dedicated k9s group.
- A published screenshot must survive ingestion through the existing allowed
  hosts, including signed GitBook proxies for external source images.
- Literal image examples in code must remain unchanged; angle-bracketed,
  escaped and URL-encoded image destinations must resolve correctly.
- The language bridge must copy actual local assets without treating external
  URLs as missing files.
- Full ingest must reconcile only published/indexable pages, and the live
  verifier must reject missing results, BM25 fallback and cross-language hits.

## Red and green evidence

The resolver reproducer ran 20 tests with six intended failures before the
first resolver fix. Additional regressions reproduced warnings for SUMMARY.md,
escaped ampersands, indented code and three bridge asset cases. The verifier
reproducer independently exposed three invalid language/origin results being
accepted as successful.

The final offline suite passed **80 tests**, including all 15 verifier subtests.
Production script statement coverage was **81%** for docs_search_sync.py and
**94%** for language_bridge.py (**85%** combined). Validation:

```sh
python -m coverage run --source=.github/scripts -m pytest -q .github/scripts
python -m coverage report --include='*/docs_search_sync.py,*/language_bridge.py'
actionlint -ignore 'label "k9s" is unknown' .github/workflows/*.yml
git diff --check
```

All network calls in unit tests are mocked. Existing diff tests previously
consulted the public sitemap, which could remap a fixture URL and cause a
failure unrelated to Git behavior; they now use a fixed offline sitemap.
Expected error/warning cases are asserted with captured output so running the
regression suite does not create spurious Actions annotations.

## Live evidence

Pending: final merged runner assignment, nine-language full ingest/search
verification, and complete warning/error annotation review. Offline tests are
not treated as proof of deployment completion.
