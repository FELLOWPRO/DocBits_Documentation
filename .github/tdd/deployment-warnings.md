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
Production script statement coverage was **83%** for docs_search_sync.py and
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

The source image HTTP audit additionally found three dead legacy approval-history
PNGs in Dutch and Polish. PRs [1948](https://github.com/FELLOWPRO/DocBits_Documentation/pull/1948)
and [1950](https://github.com/FELLOWPRO/DocBits_Documentation/pull/1950) replace all six references
with reviewed native settings screenshots and current instructions. Both ordinary
public pages show the matching localized caption and HTTP 200 originals with
exact decoded RGBA pixel equality. GitBook reencodes PNG bytes; byte-hash
mismatches were retained rather than mistaken for different image content.
After repair, all 353 remaining unique external images in the previously warned
page scope returned HTTP 200 image responses, with zero failures.
The updated source mapping audit also resolved all 3,063 image references across
all 299 originally warned pages, with zero warning/error diagnostics. Two
informational page-fetch timeout retries recovered; they are kept in the raw
receipt and are not misclassified as missing images.

The later all-language bridge [40231650927](https://github.com/FELLOWPRO/DocBits_Documentation/actions/runs/40231650927)
completed on k9s with all eight languages reporting zero warnings and no warning
or failure annotations. The targeted Polish bridge [40232007554](https://github.com/FELLOWPRO/DocBits_Documentation/actions/runs/40232007554)
also passed without warning annotations.

Three indexing jobs initially occupied every runner and delayed language
publication. PR [1949](https://github.com/FELLOWPRO/DocBits_Documentation/pull/1949)
increases only the dedicated k9s pool maximum to four; both search matrices
retain a three-job limit. ARC chart 0.14.1 revision 2 is deployed with the
recorded values. Runner-group access was read back: only this repository and
the four trusted workflow/ref entrypoints are allowed.

The final source-aligned all-nine-language manual refresh
[40232258677](https://github.com/FELLOWPRO/DocBits_Documentation/actions/runs/40232258677)
completed successfully at source commit `4ca58cb6e1e51791ee81199496635338484e1094`.
All nine jobs ran on the dedicated local k9s group, passed regression checks,
full ingest/reconcile and a real hybrid-search query, and had zero warning or
failure annotations. Complete job logs also contain no warning/error markers.
Refresh never purged an index. The nine language-folder tree blobs, both repaired
articles, workflow and runtime script matched current main at the final audit.

| Language | Reconciled pages | Search | Warnings |
| --- | ---: | --- | ---: |
| main | 905 | OK | 0 |
| de | 910 | OK | 0 |
| es | 905 | OK | 0 |
| fr | 906 | OK | 0 |
| it | 905 | OK | 0 |
| nl | 905 | OK | 0 |
| pl | 905 | OK | 0 |
| pt | 905 | OK | 0 |
| zh | 905 | OK | 0 |

Total: **8,151 reconciled pages**, with every language verified.

## Retrospective

The original warnings combined outdated Actions runtimes, incomplete Markdown
image resolution and three genuinely dead legacy image URLs. Merely changing
the runner label was insufficient: public-repository access required a dedicated
runner group, and the German push entrypoint used its own branch workflow.
The three-runner pool also delayed publication behind long indexing jobs;
the fourth local runner now permits publication while indexing remains capped
at three jobs.

I checked runner access and actual image responses too late, which caused
avoidable queued jobs and repeated full runs. I also initially treated CDN
filenames as publication evidence, counted mirrored runner log lines, and
searched existing native assets too narrowly before attempting captures.
Those checks now use actual content/pixels, unique source paths and an asset
inventory; rejected capture and HTTP-failure receipts were retained.

Prioritized improvements:

1. Before a full ingest, validate every active workflow/ref, effective runner
   access and publication capacity, then check source image mappings and actual
   image HTTP responses. Finish source repairs before launching final indexing.
2. Keep the offline parser/bridge/verifier regressions and bounded fetch retries.
   Separate recovered retry diagnostics from warnings; count unique source paths
   in mirrored live logs so progress reports remain accurate.
3. Accept deployment only after all-language ingest/reconcile and real search,
   zero warning/failure annotations, matching deployed source blobs, and ordinary
   public-page checks of localized captions and delivered image pixels.
