# eDocs country formats and versions

The [version 2 package](../edocs-ui-v2/README.md) revises the films to show real country-specific DocBits rule lists, Transformation code, Extraction Paths and the preview panel. Its delivery registry identifies revised variants; the review player uses version 2 when available. The original diagram renderer and its provenance below remain available as version 1.

Forty country/international explainers accompany the support guides. Each film uses country-specific narration and three teaching scenes. The settings screenshots come from the real development UI; diagrams do not reproduce product controls.

Languages: en, de, es, fr, it, nl, pl, pt, zh. The matrix distinguishes family, syntax, publication version, profile, classification and mapping components. It records catalogue presence, not legal certification or an end-to-end test of every file. Costa Rica is explicitly unconfirmed.

## Delivery status

All nine languages include the 40 country/international guides and the clarified version/profile scope. Available media is listed in `delivery.json`; the review player shows a localized pending message without requesting missing files.

| Language | Country guides | Real screenshots | Narrated films + WebVTT |
| --- | --- | --- | --- |
| EN, DE, ES, FR, IT | 40 each | 40 each | 40 each |
| NL | 40 | 40 | 39; Vietnam pending |
| PL, ZH | 40 each | 40 each | 40 each |
| PT | 40 | 40 | 37; Austria, Thailand and Brazil pending |

The Dutch Vietnam speech submission lost its response before a request ID was saved. The existing cache guard is preserved; no duplicate paid submission was made. Portuguese Austria, Thailand and Brazil also retain ambiguous speech-submission checkpoints. These four films remain pending; do not resubmit paid speech until the existing submissions have been reconciled. The earlier credit-note diagnostic guides and their media remain complete in all nine languages.

The complete isolated renderer sources and tests are in `renderer-source.tar.gz`. Extract into a new directory; `renderer-source.sha256.json` lists every source file. Changed renderer modules are also readable in `renderer/`. Pinned fonts and logo can be restored from the retained local cache using the unchanged font/brand locks and the provisioning instructions in `../edocs-credit-note/`. Never put credentials in this package.

Run one language at a time in the locked `core6274-video-snapshot` image. From the extracted workspace, mount the workspace at `/repo`. Its existing image working directory is `scripts/settings_assistant/explainer_videos`. Acquire speech only when authorized, with the credential file mounted read-only at `/run/tts-credential`:

```sh
python country_batch.py --locale en --speech-only
python country_batch.py --locale en --workers 6
```

Speech uses the retained asynchronous provider adapter and full request hashes. Identical common narration shares a cache entry across countries; distinct text, language or voice settings remain distinct. Persisted request IDs are resumed. Media builds run offline and never trim or stretch speech. A measured constant gain corrects residual loudness after two-pass normalization; final AAC loudness and true peak remain independently checked.

`translations/` retains all narration and documentation wording. `evidence/` contains the sanitized catalogue, configuration metadata, pinned API revisions and limits of the check. `capture.cjs` performs read-only development UI capture with a disposable language context; it never saves organization settings. Scripts retain their task-host path hints and require matching local dependencies.

## Review

The published GitBook guides embed the available version 2 films from the DocBits video CDN before the format matrix, with direct MP4 and WebVTT links. See `../edocs-ui-v2/publication/` for the verified immutable assets. The historical local review player still opens the original attachments and supports captions and transcripts.

Per-language QA in `qa/` records full decode, streams, timing, captions, loudness, clipping, source freshness, real browser playback/seek/end, keyboard access, 380 px layout and HTTP byte ranges for the delivered films. `report.json` denotes a complete media locale; `partial-report.json` explicitly lists missing films and screenshots. Contact sheets cover each delivered film and its three scenes; the Dutch partial sheet marks the unavailable Vietnam film. Screenshot sheets contain every delivered UI capture. **Direct listening and native-speaker pronunciation review were not performed.** Text/language provenance and machine checks do not certify pronunciation.

Version 2 publication uses the retained create-only CDN publisher, as documented in `../edocs-ui-v2/README.md`. A reachable attachment is not evidence of an inline player: verify playback on the actual GitBook page. This documentation delivery does not update the application runtime video catalog.
