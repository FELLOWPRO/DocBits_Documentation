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

The final offline suite passed **84 tests**, including all 15 verifier subtests.
Production script statement coverage was **82%** for docs_search_sync.py and
**94%** for language_bridge.py (**86%** combined). Validation:

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

- The dedicated k9s test run [40224621191](https://github.com/FELLOWPRO/DocBits_Documentation/actions/runs/40224621191) completed successfully with zero annotations.
- The merged all-language bridge [40225298533](https://github.com/FELLOWPRO/DocBits_Documentation/actions/runs/40225298533) completed on `k9s-xkfm4-runner-cdmnv`; all eight languages reported `warnings=0` and the job has zero warning/error annotations.
- The six PO screenshots are published and independently fetched as HTTP 200 PNGs with the expected image-content git hash. GitBook reuses existing CDN filenames; matching a new source filename is not a valid publication oracle.
- The additional Chinese audit exposed one transient page read timeout. Regression tests reproduce both timeout/503 recovery and persistent 404/timeout diagnostics. Page fetches now retry transient failures before caching an empty result.

Pending: final nine-language full ingest/search verification on the retry-enabled version, manual refresh verification and complete annotation review. Offline tests are not treated as proof of deployment completion.
