# Real DocBits UI, version 2

These revised films use real, localized development UI captures as their picture
track. The retained settings explainer pipeline supplies the unchanged cached
narration, timing, captions, audio normalization, encoding and media validation.
`ui_picture.py` uses the pipeline's existing external-picture-track interface.
The pictures are a screenshot walkthrough, not a continuous screen recording.

`capture.cjs` opens existing eDocs rules, scrolls the real code editor, opens the
preview panel and displays the negative-sign setting. It never saves, creates,
activates or deletes a rule. Version authors, the user menu, email links and
notifications are hidden. The shared user's language preference is unchanged;
translation runs only in a disposable browser context. Process one locale at a
time. Inspect every capture and every composed shot before delivery.

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
and screenshot hashes are retained with each variant. No speech was resubmitted
to make these visual changes. The ambiguous NL Vietnam speech checkpoint is
preserved and must be reconciled before any paid retry.

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
