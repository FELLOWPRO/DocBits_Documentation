"""Page-isolated input and final-artifact hashes; candidate manifests only."""

import json
from pathlib import Path
import jsonschema
from cache import canonical, digest, file_hash, write_json
from mux import ENCODING
from vtt import transcript, serialize, validate_cues
from tts import FALLBACK

from country_registry import COUNTRY_PAGES

ROOT = Path(__file__).resolve().parent
ORIGIN = "https://docbits-videos.fra1.cdn.digitaloceanspaces.com"
PREFIX = "settings-assistant/"
ROUTES = {
    "edocs_credit_note": [r"^/settings/manage-xslt/INVOICE(?:/.*)?$"],
    "layouts": [
        r"^/settings/doc-type-settings/[A-Za-z0-9_-]{1,128}/layouts$",
        r"^/settings/doc-type-settings/[A-Za-z0-9_-]{1,128}/layouts/selection-rules/[A-Za-z0-9_-]{1,128}$",
    ],
    "users": [r"^/settings/users$"],
    "sub_organizations": [r"^/settings/sub-organizations$"],
}
ROUTES.update({page: [r"^/settings/manage-xslt/INVOICE(?:/.*)?$"] for page in COUNTRY_PAGES})


def source_inputs(page):
    files = [
        *sorted((ROOT / "content" / page).rglob("*")),
        ROOT / "scenes" / "common.py",
        ROOT / "scenes" / "__init__.py",
        ROOT / "scenes" / f"{page}.py",
        *sorted(ROOT.glob("*.py")),
        *sorted(ROOT.glob("*.json")),
        ROOT / "requirements.lock",
        ROOT / "Dockerfile",
    ]
    return {str(p.relative_to(ROOT)): file_hash(p) for p in files if p.is_file()}


def revision(inputs, inventory):
    input_hash = digest(canonical(inputs))
    return input_hash, digest(
        canonical(
            {
                "build_inputs_sha256": input_hash,
                "artifacts": sorted(inventory, key=lambda x: (x["locale"], x["kind"])),
            }
        )
    )


def build_manifest(page, locales, out, version=1):
    if type(version) is not int or not 1 <= version <= 9007199254740991:
        raise ValueError("Version must be a positive safe integer")
    directory = Path(out) / page
    inventory = []
    timings = {}
    variants = {}
    audio = {}
    for locale in sorted(locales):
        timings[locale] = json.loads((directory / f"{locale}.timing.json").read_text())
        for segment in timings[locale]:
            key = segment["cache_key"]
            audio[key] = json.loads(
                (ROOT / "cache/tts" / key / "complete.json").read_text()
            )["files"]
        for kind, ext in [("mp4", "mp4"), ("vtt", "vtt"), ("poster", "png")]:
            path = directory / f"{locale}.{ext}"
            inventory.append(
                {
                    "locale": locale,
                    "kind": kind,
                    "sha256": file_hash(path),
                    "bytes": path.stat().st_size,
                }
            )
    inputs = {
        "source": source_inputs(page),
        "routes": ROUTES[page],
        "timing": timings,
        "audio": audio,
        "encoding": ENCODING,
    }
    recordings = {
        locale: json.loads((directory / f"{locale}.recording.json").read_text())
        for locale in sorted(locales)
        if (directory / f"{locale}.recording.json").exists()
    }
    if recordings:
        inputs["recording"] = recordings
    input_hash, rev = revision(inputs, inventory)
    for locale in sorted(locales):
        content = json.loads(
            (ROOT / f"content/{page}/locales/{locale}.json").read_text()
        )
        cues = [c for s in timings[locale] for c in s["captions"]]
        assets = {}
        for item in inventory:
            if item["locale"] != locale:
                continue
            kind = item["kind"]
            ext = "png" if kind == "poster" else kind
            assets[kind] = {
                "key": f"{PREFIX}{page}/v{version}/{locale}.{ext}",
                "sha256": item["sha256"],
                "bytes": item["bytes"],
                "mime": {
                    "mp4": "video/mp4",
                    "vtt": "text/vtt; charset=utf-8",
                    "png": "image/png",
                }[ext],
            }
        variants[locale] = {
            "title": content["title"],
            "visual_locale": locale,
            "audio_locale": "en" if locale in FALLBACK else locale,
            "caption_locale": locale,
            "audio_mode": ("english_fallback" if locale in FALLBACK else "localized"),
            "duration_ms": timings[locale][-1]["end_ms"],
            "width": 1280,
            "height": 720,
            "fps": 30,
            "assets": assets,
            "captions": cues,
            "transcript": transcript(cues),
        }
    manifest = {
        "schema_version": 1,
        "route_contract_version": 1,
        "media_origin": ORIGIN,
        "storage_bucket": "docbits-videos",
        "object_prefix": PREFIX,
        "pages": {
            page: {
                "content_revision": version,
                "build_inputs_sha256": input_hash,
                "route_patterns": ROUTES[page],
                "variants": variants,
            }
        },
    }
    validate_manifest(manifest, out, review=True)
    candidate = Path(out) / "pilot.manifest.candidate.json"
    review_path = Path(out) / "pilot.review.json"
    # Keep invalid builds from leaving a stale publication candidate.
    # Never leave a stale or incompatible publication candidate beside them.
    try:
        validate_manifest(manifest, out)
    except jsonschema.ValidationError:
        candidate.unlink(missing_ok=True)
        write_json(
            review_path,
            {
                "publication_ready": False,
                "reason": "Corrected script exceeds runtime 120-second contract",
                "manifest": manifest,
            },
        )
    else:
        review_path.unlink(missing_ok=True)
        write_json(candidate, manifest)
    write_json(Path(out) / "pilot.inputs.json", inputs)
    write_json(
        Path(out) / "pilot.provenance.json",
        {"content_sha256": rev, "build_inputs_sha256": input_hash, "version": version},
    )
    return manifest


def validate_manifest(manifest, out, review=False):
    schema = json.loads((ROOT / "manifest.schema.json").read_text())
    if review:
        schema["$defs"]["variant"]["properties"]["duration_ms"]["maximum"] = 120000
        schema["$defs"]["cue"]["properties"]["start_ms"]["maximum"] = 119999
        schema["$defs"]["cue"]["properties"]["end_ms"]["maximum"] = 120000
    jsonschema.Draft202012Validator(schema).validate(manifest)
    if len(canonical(manifest)) > 8 * 1024 * 1024:
        raise ValueError("Manifest byte budget")
    for page, data in manifest["pages"].items():
        if data["route_patterns"] != ROUTES[page]:
            raise ValueError("Route contract mismatch")
        for locale, variant in data["variants"].items():
            fallback = locale in FALLBACK
            if (
                variant["visual_locale"],
                variant["caption_locale"],
                variant["audio_locale"],
                variant["audio_mode"],
            ) != (
                locale,
                locale,
                "en" if fallback else locale,
                "english_fallback" if fallback else "localized",
            ):
                raise ValueError("Locale mismatch")
            validate_cues(variant["captions"], variant["duration_ms"])
            expected_ids = json.loads(
                (ROOT / "content" / page / "script.yaml").read_text()
            )["segment_ids"]
            actual_ids = []
            for cue in variant["captions"]:
                if not actual_ids or actual_ids[-1] != cue["segment_id"]:
                    actual_ids.append(cue["segment_id"])
            if actual_ids != expected_ids:
                raise ValueError("Caption segment order differs from script")
            if sum(len(cue["text"].encode()) for cue in variant["captions"]) > 24576:
                raise ValueError("Caption text byte budget")
            if variant["transcript"] != transcript(variant["captions"]):
                raise ValueError("Transcript mismatch")
            for kind, asset in variant["assets"].items():
                ext = "png" if kind == "poster" else kind
                expected_mime = {
                    "mp4": "video/mp4",
                    "vtt": "text/vtt; charset=utf-8",
                    "png": "image/png",
                }[ext]
                if asset["mime"] != expected_mime:
                    raise ValueError("Asset MIME mismatch")
                if (
                    asset["key"]
                    != f"{PREFIX}{page}/v{data['content_revision']}/{locale}.{ext}"
                ):
                    raise ValueError("Asset key mismatch")
                path = Path(out) / page / f"{locale}.{ext}"
                if (
                    file_hash(path) != asset["sha256"]
                    or path.stat().st_size != asset["bytes"]
                ):
                    raise ValueError("Artifact checksum mismatch")
                if (
                    asset["bytes"]
                    > {"mp4": 10_000_000, "vtt": 32768, "png": 1_000_000}[ext]
                ):
                    raise ValueError("Asset budget exceeded")
            if (Path(out) / page / f"{locale}.vtt").read_bytes() != serialize(
                variant["captions"], variant["duration_ms"]
            ).encode():
                raise ValueError("Caption artifact mismatch")
            video = {
                "schema_version": 1,
                "video_key": page,
                "content_revision": data["content_revision"],
                "locale": locale,
                **variant,
            }
            video["assets"] = {
                kind: {
                    "url": ORIGIN + "/" + asset["key"],
                    **{k: v for k, v in asset.items() if k != "key"},
                }
                for kind, asset in variant["assets"].items()
            }
            if (
                len(
                    b"data: "
                    + canonical(
                        {
                            "type": "page_video",
                            "video": video,
                            "trace_id": "T" * 128,
                            "docbits_trace_id": "T" * 128,
                        }
                    )
                    + b"\n\n"
                )
                > 65536
            ):
                raise ValueError("SSE frame budget")
