# Electronic credit note classification explainer

Eight causal diagrams explain the diagnosis and safe configuration workflow described in the documentation. These diagrams are educational illustrations; the documentation screenshots come from the real development UI.

Locales: `en`, `de`, `es`, `fr`, `it`, `nl`, `pl`, `pt`, `zh`. Each locale has synthesized narration in its language, captions and labels. No customer data appears in the film.

`content/` contains the script, coverage map, labels and localized speech/captions. `scenes/edocs_credit_note.py` implements the eight scenes. `pipeline.patch` adds this page and its manifest contract to the existing settings explainer pipeline and selects the pinned Simplified Chinese font. Existing application page catalogs and deployments are outside this documentation change.

Use the pipeline from `doc2-api/scripts/settings_assistant/explainer_videos/`, apply the patch to an isolated copy, copy `content/` into `content/edocs_credit_note/`, and copy the scene into `scenes/`. Keep the supplied locks unchanged. Provision the checksum-pinned fonts and logo from the retained cache. Speech acquisition uses the existing opt-in cached `tts.py` adapter; never place credentials in this directory.

Build one locale at a time:

```sh
docker run --rm --network none -v "$DOCBITS_VIDEO_WORKSPACE":/repo core6274-video-snapshot python toolchain.py
docker run --rm --network none -v "$DOCBITS_VIDEO_WORKSPACE":/repo core6274-video-snapshot python build.py --page edocs_credit_note --locale en
```

`DOCBITS_VIDEO_WORKSPACE` is the isolated directory containing `scripts/settings_assistant/explainer_videos/`. Use the verified renderer image available on your host. The image name alone does not establish that its environment matches the lock.

`tests/test_edocs_manifest_contract.py` checks that all nine documentation languages form a valid manifest and that unknown pages, invalid asset paths and durations above 120 seconds remain rejected. It uses tiny synthetic files to test the contract; it does not certify media playback. Set `DOCBITS_VIDEO_SOURCE` to this source-package directory and run:

```sh
docker run --rm --network none -e PYTHONDONTWRITEBYTECODE=1 \
  -v "$DOCBITS_VIDEO_WORKSPACE":/repo:ro \
  -v "$DOCBITS_VIDEO_SOURCE/tests":/edocs-tests:ro -w /repo \
  core6274-video-snapshot python -m pytest -p no:rerunfailures \
  -p no:cacheprovider --noconftest -o addopts= /edocs-tests
```

The original renderer image was unavailable on this host. Rebuilding the original Dockerfile matched Python, FFmpeg and native libraries but differed in the OS package inventory. Restoring Debian packages from the 4 October 2026 snapshot reproduced the existing package digest. The original `toolchain.verify()` then passed without changing or disabling a lock or a check. The recovery Dockerfile and snapshot sources are in `provisioning/`; they reuse the Python and native binaries built from the original pipeline Dockerfile. Provisioning evidence is retained with the local build.

Generated MP4 and VTT files are documentation attachments. Source provenance, media measurements and visual review evidence accompany the local output. Public CDN upload and repository publication are separate steps.

Serve the documentation checkout over localhost and open [review.html](review.html) to switch between the nine films, native captions and transcripts. It reads the actual documentation attachments through relative paths and defaults to German. [QA.md](QA.md) records the completed checks and the outstanding direct listening review. Review evidence is retained in `qa/`.
