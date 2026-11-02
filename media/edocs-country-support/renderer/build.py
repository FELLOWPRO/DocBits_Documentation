"""Build approved local variants (layouts pilot, users locales). No upload or runtime manifest writes."""

import argparse
import json
import os
import subprocess
import time
from pathlib import Path
from cache import write_json, verify_entry
from tts import request_spec, synthesize, FALLBACK, LOCALES
from timing import plan_segment
from vtt import serialize
from mux import assemble, normalize, encode, run, join_sections
from validate import validate_variant
from manifest import build_manifest, source_inputs
from toolchain import verify, install_fonts

from country_registry import COUNTRY_PAGES, DOCS_LOCALES

ROOT = Path(__file__).resolve().parent
PILOT = ("en", "de", "ja", "hu")
# The layouts pilot stays at four variants; users and sub_organizations cover every app locale.
PAGE_LOCALES = {
    "layouts": PILOT,
    "users": LOCALES,
    "sub_organizations": LOCALES,
    "edocs_credit_note": ("en", "de", "es", "fr", "it", "nl", "pl", "pt", "zh"),
}
PAGE_LOCALES.update({page: DOCS_LOCALES for page in COUNTRY_PAGES})


def prepare(locale, out, page="layouts"):
    content = json.loads((ROOT / f"content/{page}/locales/{locale}.json").read_text())
    audio_locale = "en" if locale in FALLBACK else locale
    narration = json.loads(
        (ROOT / f"content/{page}/locales/{audio_locale}.json").read_text()
    )
    settings = json.loads((ROOT / "voice_settings.json").read_text())[audio_locale]
    timing = []
    frame = 0
    for segment, spoken in zip(content["segments"], narration["segments"]):
        if segment["id"] != spoken["id"]:
            raise ValueError("Locale segment mismatch")
        spec = request_spec(
            page, spoken["id"], spoken["narration"], audio_locale, settings
        )
        key, meta = synthesize(spec, ROOT / "cache/tts")
        alignment = json.loads(
            (ROOT / "cache/tts" / key / "alignment.json").read_text()
        )
        # Observed DO Japanese timestamps are transliterated, not native-caption tokens.
        if locale == "ja":
            alignment = []
        plan = plan_segment(segment, locale, meta["samples"], alignment, frame)
        plan["cache_key"] = key
        timing.append(plan)
        frame += plan["frames"]
    if not 900 <= frame <= 3600:
        raise ValueError(
            f"{locale}: duration {frame/30:.3f}s outside corrected-script 30–120s review budget"
        )
    directory = Path(out) / page
    directory.mkdir(parents=True, exist_ok=True)
    write_json(directory / f"{locale}.timing.json", timing)
    cues = [c for s in timing for c in s["captions"]]
    (directory / f"{locale}.vtt").write_text(
        serialize(cues, round(frame * 1000 / 30)), encoding="utf-8", newline="\n"
    )
    return timing


def use_recording(recording, locale, directory, timing):
    """Accept an externally recorded, silent-or-not video as the picture track.

    Only the video stream is used. Speech, loudness, encoding and QA stay the
    pipeline's own; the recording must match the narration timing exactly.
    """
    from validate import probe

    recording = Path(recording)
    video = recording / f"{locale}.mp4"
    captions = recording / f"{locale}.vtt"
    if captions.read_bytes() != (directory / f"{locale}.vtt").read_bytes():
        raise ValueError("Recording captions differ from the narration-derived VTT")
    streams = probe(video)["streams"]
    picture = next(s for s in streams if s["codec_type"] == "video")
    if (picture["width"], picture["height"]) != (1280, 720) or int(
        picture["nb_frames"]
    ) != sum(s["frames"] for s in timing):
        raise ValueError("Recording size or frame count differs from the timing plan")
    from cache import file_hash

    write_json(
        directory / f"{locale}.recording.json",
        {
            "kind": "external_recording",
            "mp4_sha256": file_hash(video),
            "vtt_sha256": file_hash(captions),
            "frames": int(picture["nb_frames"]),
        },
    )
    return video


def build(locale, out, page="layouts", recording=None, poster_at=1.4):
    started = time.monotonic()
    verify()
    font_config = install_fonts()
    timing = prepare(locale, out, page)
    directory = Path(out) / page
    work = Path(out) / "work" / page / locale
    work.mkdir(parents=True, exist_ok=True)
    env = {
        **os.environ,
        "VIDEO_LOCALE": locale,
        "VIDEO_TIMING": str((directory / f"{locale}.timing.json").resolve()),
        "FONTCONFIG_FILE": str(font_config),
        "TZ": "UTC",
        "PYTHONHASHSEED": "6274",
        "OMP_NUM_THREADS": "1",
    }
    render_command = [
        "python",
        "-m",
        "manim",
        "--renderer=cairo",
        "--disable_caching",
        "--save_sections",
        "--format=mp4",
        "--fps",
        "30",
        "-r",
        "1280,720",
        "--media_dir",
        str(work / "media"),
        "-o",
        "silent",
        str(ROOT / f"scenes/{page}.py"),
        page.capitalize(),
    ]
    if recording is not None:
        render_command = ["external-recording", f"{locale}.mp4"]
        silent = use_recording(recording, locale, directory, timing)
    else:
        with (work / "render.log").open("w") as log:
            subprocess.run(
                render_command,
                check=True,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                cwd=ROOT,
            )
        silent = join_sections(work, timing)
    assemble(timing, ROOT / "cache/tts", work / "joined.wav")
    loudness = normalize(work / "joined.wav", work / "normalized.wav")
    if page in COUNTRY_PAGES:
        from country_audio import correct_residual
        loudness["residual_correction"] = correct_residual(work / "normalized.wav")
    encode(
        silent,
        work / "normalized.wav",
        directory / f"{locale}.mp4",
        timing[-1]["end_ms"] / 1000,
        # Browser recordings are full-range (yuvj420p): convert to limited range.
        video_filter=(
            "scale=in_range=pc:out_range=tv:flags=accurate_rnd,format=yuv420p"
            if recording is not None
            else None
        ),
    )
    run(
        [
            "-v",
            "error",
            "-ss",
            str(poster_at),
            "-i",
            directory / f"{locale}.mp4",
            "-frames:v",
            "1",
            directory / f"{locale}.png",
        ]
    )
    qa = validate_variant(directory, locale, timing)
    qa.update(
        {"render_seconds": round(time.monotonic() - started, 3), "loudness": loudness}
    )
    write_json(directory / f"{locale}.qa.json", qa)
    write_json(
        directory / f"{locale}.provenance.json",
        {
            "source_inputs": source_inputs(page),
            "audio_cache": {
                s["segment_id"]: {
                    "key": s["cache_key"],
                    "metadata": verify_entry(ROOT / "cache/tts" / s["cache_key"]),
                }
                for s in timing
            },
            "render_command": [
                str(a).replace(str(ROOT), "<pipeline>").replace(str(out), "<out>")
                for a in render_command
            ],
            "loudness": loudness,
        },
    )
    print(json.dumps(qa), flush=True)
    return qa


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        type=int,
        default=1,
        help="Immutable page version (positive integer)",
    )
    parser.add_argument(
        "--page",
        choices=("layouts", "users", "sub_organizations", "edocs_credit_note", *COUNTRY_PAGES),
        default="layouts",
    )
    parser.add_argument("--locale", choices=LOCALES, action="append")
    parser.add_argument("--out", type=Path, default=ROOT / "out")
    parser.add_argument(
        "--recording",
        type=Path,
        help="Directory with <locale>.mp4/.vtt recorded outside Manim (picture only)",
    )
    parser.add_argument("--poster-at", type=float, default=1.4)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    locales = args.locale or PAGE_LOCALES[args.page]
    if not args.manifest_only:
        for locale in locales:
            if args.prepare_only:
                timing = prepare(locale, args.out, args.page)
                print(locale, timing[-1]["end_ms"])
            else:
                build(locale, args.out, args.page, args.recording, args.poster_at)
    if not args.prepare_only and all(
        (args.out / args.page / f"{locale}.mp4").exists()
        for locale in PAGE_LOCALES[args.page]
    ):
        build_manifest(
            args.page, PAGE_LOCALES[args.page], args.out, version=args.version
        )


if __name__ == "__main__":
    main()
