"""Full local pilot checks and key-frame extraction. Human review remains explicit."""

import argparse
import json
import subprocess
import wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from cache import verify_entry, write_json
from manifest import validate_manifest
from mux import run
from timing import graphemes, reading_rate
from tts import FALLBACK, LOCALES, PROVIDER_LANGUAGE
from validate import validate_variant
from toolchain import verify

from country_registry import COUNTRY_PAGES, DOCS_LOCALES

ROOT = Path(__file__).resolve().parent


def audio_check(out, locale, timing, page="layouts"):
    """Measure samples and cue coverage; language evidence is provenance, not ASR."""
    expected_locale = "en" if locale in FALLBACK else locale
    provider_locale = PROVIDER_LANGUAGE.get(expected_locale, expected_locale)
    content = json.loads(
        (ROOT / f"content/{page}/locales/{expected_locale}.json").read_text()
    )
    spoken = {s["id"]: s["narration"] for s in content["segments"]}
    rows = []
    for segment in timing:
        entry = ROOT / "cache/tts" / segment["cache_key"]
        verify_entry(entry)
        request = json.loads((entry / "request.json").read_text())
        if (
            request["audio_locale"] != provider_locale
            or request["input"]["language_code"] != provider_locale
            or request["input"]["text"] != spoken[segment["segment_id"]]
        ):
            raise ValueError("Audio language/text provenance mismatch")
        with wave.open(str(entry / "speech.wav")) as source:
            if source.getnframes() != segment["samples"]:
                raise ValueError("Speech sample count mismatch")
            pcm = np.frombuffer(source.readframes(source.getnframes()), dtype="<i2")
        if np.any((pcm == -32768) | (pcm == 32767)):
            raise ValueError("Clipped source PCM")
        speech_end = segment["audio_start_ms"] + len(pcm) / 48
        tail = segment["end_ms"] - speech_end
        cues = segment["captions"]
        if (
            tail < 499
            or cues[0]["start_ms"] > segment["audio_start_ms"]
            or cues[-1]["end_ms"] < speech_end - 1
        ):
            raise ValueError("Speech truncated or outside captions")
        if any(a["end_ms"] != b["start_ms"] for a, b in zip(cues, cues[1:])):
            raise ValueError("Caption gap during speech")
        rows.append(
            {
                "segment_id": segment["segment_id"],
                "speech_ms": round(len(pcm) / 48, 3),
                "caption_start_ms": cues[0]["start_ms"],
                "caption_end_ms": cues[-1]["end_ms"],
                "speech_end_ms": round(speech_end, 3),
                "tail_ms": round(tail, 3),
                "cache_key": segment["cache_key"],
            }
        )
    decoded = subprocess.check_output(
        [
            "ffmpeg",
            "-v",
            "error",
            "-i",
            str(out / page / f"{locale}.mp4"),
            "-vn",
            "-f",
            "f32le",
            "-acodec",
            "pcm_f32le",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-",
        ]
    )
    pcm = np.frombuffer(decoded, dtype="<f4").reshape(-1, 2)
    peak = float(np.max(np.abs(pcm)))
    if not np.isfinite(pcm).all() or peak >= 1:
        raise ValueError("Clipped final decoded audio")
    # Check the middle of each silent lead, away from AAC ringing at speech onset.
    join_peak = max(
        float(
            np.max(
                np.abs(
                    pcm[
                        round(s["start_frame"] * 1600 + 2400) : round(
                            s["start_frame"] * 1600 + 7200
                        )
                    ]
                )
            )
        )
        for s in timing
    )
    if join_peak > 0.001:
        raise ValueError("Unexpected signal at silent segment join")
    return {
        "audio_locale": expected_locale,
        "language_check": "cached request language and exact narration text; not acoustic recognition",
        "decoded_sample_peak": peak,
        "silent_join_peak": join_peak,
        "segments": rows,
        "listening_review": "not performed; pronunciation and subjective clicks require listening",
    }


PAGE_LOCALES = {
    "layouts": ("en", "de", "ja", "hu"),
    "users": LOCALES,
    "sub_organizations": LOCALES,
    "edocs_credit_note": ("en", "de", "es", "fr", "it", "nl", "pl", "pt", "zh"),
}
PAGE_LOCALES.update({page: DOCS_LOCALES for page in COUNTRY_PAGES})


def check_all(out, page="layouts", locales=None):
    verify()
    locales = tuple(locales or PAGE_LOCALES[page])
    review_path = out / "pilot.review.json"
    if set(locales) != set(PAGE_LOCALES[page]):
        # A partial locale build has no candidate manifest yet; media checks still run.
        pass
    elif review_path.exists():
        review = json.loads(review_path.read_text())
        if (
            review["publication_ready"] is not False
            or (out / "pilot.manifest.candidate.json").exists()
        ):
            raise ValueError("Review output must not masquerade as a release candidate")
        validate_manifest(review["manifest"], out, review=True)
    else:
        manifest = json.loads((out / "pilot.manifest.candidate.json").read_text())
        validate_manifest(manifest, out)
    rows = []
    timings = {}
    for locale in locales:
        timing = json.loads((out / page / f"{locale}.timing.json").read_text())
        timings[locale] = timing
        row = validate_variant(out / page, locale, timing)
        row["audio_check"] = audio_check(out, locale, timing, page)
        for s in timing:
            verify_entry(ROOT / "cache/tts" / s["cache_key"])
            for c in s["captions"]:
                if (
                    graphemes(c["text"].replace("\n", " "))
                    / ((c["end_ms"] - c["start_ms"]) / 1000)
                    > reading_rate(locale) + 0.02
                ):
                    raise ValueError("Caption reading speed")
        rows.append(row)
    for fallback in sorted(FALLBACK & set(timings)):
        if "en" not in timings:
            break
        if [s["cache_key"] for s in timings[fallback]] != [
            s["cache_key"] for s in timings["en"]
        ]:
            raise ValueError(f"{fallback.upper()} must reuse exact English audio")
        if any(s["alignment_mode"] != "translated_segment" for s in timings[fallback]):
            raise ValueError(f"{fallback.upper()} caption alignment")
    return rows


def keyframes(out, destination, page="layouts", locales=None):
    locales = tuple(locales or PAGE_LOCALES[page])
    destination.mkdir(parents=True, exist_ok=True)
    rows = [
        f"# {page.capitalize()} — local QA",
        "",
        "Local only. No published assets; browser/release gates are not evaluated.",
        "",
    ]
    for locale in locales:
        timing = json.loads((out / page / f"{locale}.timing.json").read_text())
        qa = json.loads((out / page / f"{locale}.qa.json").read_text())
        rows += [
            f"## {locale}",
            f"{qa['duration_ms']/1000:.3f} seconds; {qa['bytes']:,} bytes; render {qa['render_seconds']:.3f} seconds.",
            "",
        ]
        sheet = Image.new("RGB", (1280, 5 * 270), "#101828")
        draw = ImageDraw.Draw(sheet)
        for index, s in enumerate(timing):
            name = f"{locale}-{s['segment_id']}.png"
            fraction = {
                "scope": 0.7,
                "clone": 0.34,
                "conditions": 0.42,
                "priority": 0.9,
                "target": 0.85,
                "fallback": 0.4,
                "override": 0.9,
                "restore": 0.85,
                "deletion": 0.4,
            }.get(s["segment_id"], 0.75)
            run(
                [
                    "-v",
                    "error",
                    "-ss",
                    str(
                        (s["start_ms"] + fraction * (s["end_ms"] - s["start_ms"]))
                        / 1000
                    ),
                    "-i",
                    out / page / f"{locale}.mp4",
                    "-frames:v",
                    "1",
                    destination / name,
                ]
            )
            for phase, fraction in [("setup", 0.22), ("action", 0.48), ("result", 0.9)]:
                frame_path = destination / f"{locale}-{s['segment_id']}-{phase}.png"
                run(
                    [
                        "-v",
                        "error",
                        "-ss",
                        str(
                            (s["start_ms"] + fraction * (s["end_ms"] - s["start_ms"]))
                            / 1000
                        ),
                        "-i",
                        out / page / f"{locale}.mp4",
                        "-frames:v",
                        "1",
                        frame_path,
                    ]
                )
            rows += [
                f"### {s['segment_id']}",
                f"![{locale} {s['segment_id']}]({name})",
                "",
            ]
            with Image.open(destination / name) as frame:
                drawer = frame.resize((380, 214), Image.Resampling.LANCZOS)
                drawer.save(destination / f"{locale}-{s['segment_id']}-drawer.png")
                frame.thumbnail((420, 237))
                x, y = (index % 3) * 426, (index // 3) * 270
                sheet.paste(frame, (x, y))
                draw.text(
                    (x + 8, y + 240), f"{locale} / {s['segment_id']}", fill="white"
                )
        sheet.save(destination / f"{locale}-contact-sheet.png")
    (destination / "README.md").write_text("\n".join(rows) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument(
        "--page",
        choices=("layouts", "users", "sub_organizations", "edocs_credit_note", *COUNTRY_PAGES),
        default="layouts",
    )
    parser.add_argument("--locale", action="append", choices=LOCALES)
    parser.add_argument("--out", type=Path, default=ROOT / "out")
    parser.add_argument("--keyframes", type=Path)
    args = parser.parse_args()
    if args.all:
        print(json.dumps(check_all(args.out, args.page, args.locale), indent=2))
        print("PILOT QA PASSED")
    if args.keyframes:
        keyframes(
            args.out,
            args.keyframes,
            args.page,
            args.locale,
        )
