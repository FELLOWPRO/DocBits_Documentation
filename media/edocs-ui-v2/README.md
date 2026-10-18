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

The completed Chinese Germany request returned overlapping character timestamps
in romanized text. `materialize_segment_alignment.py` recovers this existing
audio offline, verifies the original MP3 decodes to the exact cached PCM, and
preserves the original provider timestamps. It selects the renderer's measured
segment captions with native Chinese text, without claiming word timing or
submitting speech again. The request ID, unchanged audio hashes and fallback
reason are recorded in `qa/zh/germany-segment-alignment.json`. The original
provider response remains only in the local cache because it can contain a
transient signed media URL. The frozen renderer and its source locks are unchanged.

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

## Inline playback in GitBook

The published guides use the DocBits video CDN. A GitBook `{% file %}` block is
only a download card; it does not display an inline video player. Each delivered
country film now appears before the format matrix, and the credit-note guide
also embeds its localized film. Keep the direct MP4 and WebVTT links below the
player. Existing screenshots and media bytes are unchanged.

Use the retained renderer and publisher with their original source hashes and
media QA. `publish_existing.py` checks that the build provenance, QA and original
attachment hashes still match, then calls the retained create-only publisher.
It performs no rendering or paid speech requests. From this repository root,
with the publisher dependencies available:

```sh
python media/edocs-ui-v2/publish_existing.py \
  --page edocs_country_germany --locale de --upload \
  --credential-file /absolute/path/to/doc2api.env
```

Omit `--locale` to publish all delivered locales of that page. Omit `--upload`
to recheck anonymous CDN access without loading credentials. Manifests and public
verification receipts are written to `output/edocs-inline-video/`. The checked-in
`publication/manifest.json` and `publication/receipt.json` record this migration.
Existing different objects require a new immutable version; never overwrite them.

The GitBook page must contain an embed, for example:

```markdown
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_germany/v2/de.mp4" %}

[Deutschland — Erklärvideo zum Land](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_germany/v2/de.mp4)

[WebVTT](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/edocs_country_germany/v2/de.vtt)
```

The historical `prepare_locale.py` and `prepare_countries.py` scripts package the
original local attachments. Their output alone is not final publication: use the
verified CDN URLs and an embed before committing documentation links. New video
binaries must not be added to Git or uploaded to GitBook.

Check the rendered GitBook preview in a real browser, including its nested player:
play, seek and inspect playback progress and errors. Anonymous HTTP 200/206 and a
working local review player do not establish that a published page has an inline
player. WebVTT remains separately downloadable; the MP4 embed does not promise a
native caption selector. The German Germany preview was played through to its
end without media errors. Direct listening and pronunciation approval remain
separate from these playback checks.
