# Real DocBits UI, version 2

These revised films use real, localized development UI captures as their picture
track. The retained settings explainer pipeline supplies narration, timing,
captions, audio normalization, encoding and media validation. Existing speech
is reused unchanged; country films that previously had no speech use the same
retained adapter for their first request.
`ui_picture.py` uses the pipeline's existing external-picture-track interface.
The pictures are a screenshot walkthrough, not a continuous screen recording.

`capture.cjs` opens existing eDocs rules, scrolls the real code editor, opens the
preview panel and displays the negative-sign setting. It never saves, creates,
activates or deletes a rule. Version authors, the user menu, email links and
notifications are hidden. The shared user's language preference is unchanged;
translation runs only in a disposable browser context. Process one locale at a
time. Run `capture_country_pool.py` with `--workers 1` to let the application
finish loading each country's editors before continuing. It never starts a
second locale or changes the shared profile. Inspect every capture and every
composed shot before delivery.

The credit-note example is **FACTURX 1.0.05 / ZUGFeRD 2.1**. Its visible code is
an observed example, not a promise that every version has identical mappings.
The film shows the existing active default. It does not show a created draft,
activation, an imported customer document or a successful test/export result.
The narration explains the checks that the viewer must perform in their own
organisation. The shown older transformation has 381/389 branches; do not infer
the code list of another default or version from this particular screenshot.

All v1 renderer sources, provenance and media remain unchanged. Version 2 uses
new `-v2` attachment names. `delivery.json` records only delivered v2 variants;
the review players use v1 for variants that have not yet been revised. Source
and screenshot hashes are retained with each variant. No existing speech was
resubmitted to make these visual changes. `acquire_countries.py` acquires missing
PL/PT/ZH country narration sequentially and stops on the first error. It refuses
an ambiguous `submitting` checkpoint. The ambiguous NL Vietnam and PT Austria/Thailand/Brazil
speech checkpoints are preserved and must be reconciled before any paid retry.
The optional `--exclude-country` argument selects only distinct remaining
country requests; it does not reset a checkpoint or change narration. The adapter
still refuses an ambiguous request shared with any selected country. Use the
same exclusion for offline building and country preparation. An excluded country
retains its genuine screenshot and a localized notice that its film is pending.

To reproduce, unpack `renderer-source.tar.gz` into a separate workspace, provision
the unchanged locks, pinned fonts/logo and the original speech cache, then run:

```sh
docker run --rm --network none -v "$DOCBITS_VIDEO_WORKSPACE":/repo \
  -v "$DOCBITS_UI_CAPTURES":/captures:ro core6274-video-snapshot \
  python ui_picture.py --locale de --captures /captures/de \
  --out /repo/scripts/settings_assistant/explainer_videos/out-v2
```

The renderer must pass its original environment verification. `qa/` separates
technical, visual and browser checks. **Direct acoustic/native-speaker listening
has not been performed**; pronunciation approval is not claimed. GitBook preview
publication is separate from merging into the live documentation.
