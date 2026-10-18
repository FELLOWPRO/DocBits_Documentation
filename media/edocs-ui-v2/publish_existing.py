"""Publish unchanged, previously reviewed eDocs assets with the retained publisher."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "output/edocs-inline-video"
WORK.mkdir(parents=True, exist_ok=True)
PIPELINE = (
    ROOT / "output/edocs-ui-v2/pipeline/scripts/settings_assistant/explainer_videos"
)
sys.path.insert(0, str(PIPELINE))
import manifest
import publish

FOLDERS = dict(
    en="docbits",
    de="deutsch",
    es="espanol",
    fr="french",
    it="italian",
    nl="dutch",
    pl="polish",
    pt="portuguese",
    zh="chinese",
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(page, locales):
    source = PIPELINE / "out-v2" / page
    out = WORK / "cdn-staging"
    dest = out / page
    dest.mkdir(parents=True, exist_ok=True)
    current_sources = manifest.source_inputs(page)
    country = page.removeprefix("edocs_country_").replace("_", "-")
    for locale in locales:
        provenance = json.loads((source / f"{locale}.provenance.json").read_text())
        assert provenance["source_inputs"] == current_sources, (
            page,
            locale,
            "source freshness",
        )
        technical = json.loads((source / f"{locale}.qa.json").read_text())
        assert technical["full_decode"] and technical["faststart"]
        assert abs(technical["loudness_lufs"] + 16) <= 0.5
        stem = (
            f"edocs-credit-note-{locale}-v2"
            if page == "edocs_credit_note"
            else f"edocs-support-{country}-{locale}-v2"
        )
        for ext in ("mp4", "vtt"):
            asset = ROOT / FOLDERS[locale] / ".gitbook/assets" / f"{stem}.{ext}"
            assert sha(source / f"{locale}.{ext}") == sha(asset), (page, locale, ext)
        for ext in ("mp4", "vtt", "png", "timing.json", "recording.json"):
            src, target = source / f"{locale}.{ext}", dest / f"{locale}.{ext}"
            if not target.exists():
                os.link(src, target)
            else:
                assert sha(src) == sha(target)
    candidate = manifest.build_manifest(page, locales, out, version=2)
    (WORK / "manifests").mkdir(exist_ok=True)
    (WORK / "manifests" / f"{page}.json").write_text(
        json.dumps(candidate, ensure_ascii=False, indent=2) + "\n"
    )
    return candidate, out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--page", required=True, choices=["edocs_credit_note", *manifest.COUNTRY_PAGES]
    )
    parser.add_argument("--locale", action="append", choices=FOLDERS)
    parser.add_argument("--credential-file", type=Path)
    parser.add_argument("--upload", action="store_true")
    args = parser.parse_args()
    delivery = json.loads((ROOT / "media/edocs-ui-v2/delivery.json").read_text())
    if args.page == "edocs_credit_note":
        locales = list(delivery["credit_note"])
    else:
        country = args.page.removeprefix("edocs_country_").replace("_", "-")
        locales = [
            locale
            for locale, countries in delivery["countries"].items()
            if country in countries
        ]
    if args.locale:
        assert set(args.locale) <= set(locales)
        locales = args.locale
    candidate, out = prepare(args.page, locales)
    if args.upload:
        import boto3
        from botocore.config import Config
        from dotenv import dotenv_values

        if args.credential_file is None:
            parser.error("--upload requires --credential-file")
        credentials = dotenv_values(args.credential_file)
        client = boto3.client(
            "s3",
            endpoint_url=publish.ENDPOINT,
            region_name="fra1",
            aws_access_key_id=credentials["S3_KEY"],
            aws_secret_access_key=credentials["S3_SECRET"],
            config=Config(signature_version="s3v4", retries={"max_attempts": 0}),
        )
        publish.upload(candidate, out, client)
    import requests

    with requests.Session() as session:
        session.trust_env = False
        checks = publish.verify(candidate, out, session)
    receipt = {
        "page": args.page,
        "locales": locales,
        "hosting_only": True,
        "unchanged_media": True,
        "source_freshness": "exact match with original build provenance",
        "objects": checks,
    }
    (WORK / "receipts").mkdir(exist_ok=True)
    receipt_path = WORK / "receipts" / f"{args.page}.json"
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(
        json.dumps(
            {
                "page": args.page,
                "locales": locales,
                "verified_objects": len(checks),
                "receipt": str(receipt_path),
            }
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
