"""Exercise the new page against the real manifest contract with tiny fixtures."""

import copy
import json
from pathlib import Path
import shutil
import sys

import jsonschema
import pytest

PIPELINE = Path.cwd() / "scripts/settings_assistant/explainer_videos"
sys.path.insert(0, str(PIPELINE))

import manifest
from vtt import serialize


@pytest.fixture
def candidate(tmp_path, monkeypatch):
    source = tmp_path / "source"
    content = source / "content/edocs_credit_note"
    shutil.copytree(PIPELINE / "content/edocs_credit_note", content)
    shutil.copyfile(PIPELINE / "manifest.schema.json", source / "manifest.schema.json")
    cache = source / "cache/tts/sample"
    cache.mkdir(parents=True)
    (cache / "complete.json").write_text('{"files": {}}')
    out = tmp_path / "out"
    directory = out / "edocs_credit_note"
    directory.mkdir(parents=True)
    ids = json.loads((content / "script.yaml").read_text())["segment_ids"]
    locales = ("en", "de", "es", "fr", "it", "nl", "pl", "pt", "zh")
    for locale in locales:
        segments = json.loads((content / f"locales/{locale}.json").read_text())[
            "segments"
        ]
        cues = [
            {
                "segment_id": segment,
                "cue_id": f"{segment}_01",
                "start_ms": index * 4000,
                "end_ms": (index + 1) * 4000,
                "text": segments[index]["caption"],
            }
            for index, segment in enumerate(ids)
        ]
        timing = [
            {"cache_key": "sample", "end_ms": cue["end_ms"], "captions": [cue]}
            for cue in cues
        ]
        (directory / f"{locale}.timing.json").write_text(json.dumps(timing))
        (directory / f"{locale}.vtt").write_text(serialize(cues, 32000))
        (directory / f"{locale}.mp4").write_bytes(
            b"manifest fixture, not playable media"
        )
        (directory / f"{locale}.png").write_bytes(b"poster fixture")
    monkeypatch.setattr(manifest, "ROOT", source)
    data = manifest.build_manifest("edocs_credit_note", locales, out)
    return data, out


def test_nine_documentation_locales_form_a_valid_manifest(candidate):
    data, out = candidate
    manifest.validate_manifest(data, out)
    assert set(data["pages"]["edocs_credit_note"]["variants"]) == {
        "en",
        "de",
        "es",
        "fr",
        "it",
        "nl",
        "pl",
        "pt",
        "zh",
    }
    assert (out / "pilot.manifest.candidate.json").is_file()


@pytest.mark.parametrize("defect", ("unknown_page", "wrong_asset_prefix", "too_long"))
def test_edocs_extension_keeps_manifest_rejections(candidate, defect):
    original, out = candidate
    data = copy.deepcopy(original)
    if defect == "unknown_page":
        data["pages"]["unknown_page"] = data["pages"].pop("edocs_credit_note")
    elif defect == "wrong_asset_prefix":
        data["pages"]["edocs_credit_note"]["variants"]["zh"]["assets"]["mp4"][
            "key"
        ] = "other-prefix/edocs_credit_note/v1/zh.mp4"
    else:
        data["pages"]["edocs_credit_note"]["variants"]["pt"]["duration_ms"] = 120001
    with pytest.raises(jsonschema.ValidationError):
        manifest.validate_manifest(data, out)
