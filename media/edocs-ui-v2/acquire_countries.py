"""Sequential wrapper around the retained cached TTS adapter for new locales."""

import argparse
import json
from pathlib import Path
import subprocess
import sys

PIPELINE = Path("/repo/scripts/settings_assistant/explainer_videos")
sys.path.insert(0, str(PIPELINE))
from cache import canonical, digest
from country_registry import COUNTRY_PAGES
from tts import request_spec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", required=True, choices=("pl", "pt", "zh"))
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--credential-file", default="/run/tts-credential")
    parser.add_argument("--exclude-country", action="append", default=[])
    args = parser.parse_args()
    excluded = {"edocs_country_" + c.replace("-", "_") for c in args.exclude_country}
    assert excluded <= set(COUNTRY_PAGES), excluded
    pages = [page for page in COUNTRY_PAGES if page not in excluded]
    settings = json.loads((PIPELINE / "voice_settings.json").read_text())[args.locale]
    specs = {}
    for page in pages:
        content = json.loads(
            (PIPELINE / f"content/{page}/locales/{args.locale}.json").read_text()
        )
        for segment in content["segments"]:
            spec = request_spec(
                page, segment["id"], segment["narration"], args.locale, settings
            )
            specs[digest(canonical(spec))] = spec
    missing = []
    for key in specs:
        entry = PIPELINE / "cache/tts" / key
        job = entry / "job.json"
        if job.exists():
            state = json.loads(job.read_text())["state"]
            if state == "submitting":
                raise RuntimeError(
                    f"Ambiguous submission requires reconciliation: {key}"
                )
        if not (entry / "complete.json").is_file():
            missing.append(key)
    print(
        json.dumps(
            dict(locale=args.locale, unique_requests=len(specs), missing=len(missing))
        ),
        flush=True,
    )
    if not args.online:
        return
    for page in pages:
        # Stop on the first error; never retry an ambiguous paid submission.
        subprocess.run(
            [
                sys.executable,
                str(PIPELINE / "tts.py"),
                "--online",
                "--locale",
                args.locale,
                "--page",
                page,
                "--credential-file",
                args.credential_file,
            ],
            check=True,
            cwd=PIPELINE,
        )
        print(json.dumps(dict(locale=args.locale, page=page, cached=True)), flush=True)


if __name__ == "__main__":
    main()
