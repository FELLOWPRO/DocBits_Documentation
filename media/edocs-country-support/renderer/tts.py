"""DigitalOcean asynchronous TTS. Network is opt-in; uncertain submits fail closed."""

import argparse
import fcntl
import json
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.request
import wave
from pathlib import Path

from cache import canonical, digest, file_hash, verify_entry, write_json

from country_registry import COUNTRY_PAGES

ROOT = Path(__file__).resolve().parent
ENDPOINT = "https://inference.do-ai.run/v1/async-invoke"
MODEL = "fal-ai/elevenlabs/tts/multilingual-v2"
FALLBACK = {"hu", "sl", "th", "vi"}
# Provider language codes: the voice model knows "pt" only, pt-br shares it.
PROVIDER_LANGUAGE = {"pt-br": "pt"}
LOCALES = (
    "en",
    "de",
    "it",
    "fr",
    "es",
    "nl",
    "zh",
    "bg",
    "cs",
    "hu",
    "ja",
    "ko",
    "pl",
    "pt",
    "pt-br",
    "ro",
    "sk",
    "sl",
    "sv",
    "th",
    "tr",
    "vi",
)


def request_spec(page, segment, text, locale, settings):
    audio_locale = "en" if locale in FALLBACK else PROVIDER_LANGUAGE.get(locale, locale)
    return {
        "adapter_schema": 1,
        "page": "edocs_country" if page in COUNTRY_PAGES else page,
        "segment_id": segment,
        "endpoint": ENDPOINT,
        "model_id": MODEL,
        "audio_locale": audio_locale,
        "resolved_voice_id": settings["resolved_voice_id"],
        "requested_format": "provider_mp3_to_pcm_s16le_48000_mono",
        "input": {
            "text": unicodedata.normalize("NFC", text),
            "language_code": audio_locale,
            **settings["input"],
        },
    }


def normalize_alignment(raw, duration_ms):
    if raw is None or raw == []:
        return []
    if not isinstance(raw, list):
        raise ValueError("Malformed provider timestamps")
    # DO forwards ElevenLabs character-alignment blocks in timestamps.
    # Normalize this observed shape into words, preserving real speech bounds.
    if raw and isinstance(raw[0], dict) and "characters" in raw[0]:
        converted = []
        previous_end = 0
        for block in raw:
            chars = block.get("characters")
            starts = block.get("character_start_times_seconds")
            ends = block.get("character_end_times_seconds")
            if not all(isinstance(v, list) for v in (chars, starts, ends)) or not len(
                chars
            ) == len(starts) == len(ends):
                raise ValueError("Malformed character alignment arrays")
            current = None
            for char, start, end in zip(chars, starts, ends):
                if (
                    not isinstance(char, str)
                    or not isinstance(start, (int, float))
                    or not isinstance(end, (int, float))
                    or not 0
                    <= previous_end
                    <= start
                    <= end
                    <= duration_ms / 1000 + 0.05
                ):
                    raise ValueError("Malformed character alignment bounds")
                previous_end = end
                if char.isspace():
                    if current:
                        converted.append(current)
                        current = None
                elif current:
                    current["text"] += char
                    current["end"] = end
                else:
                    current = {"text": char, "start": start, "end": end}
            if current:
                converted.append(current)
        raw = converted
    words = []
    previous = 0
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError("Malformed provider word")
        start, end = item.get("start"), item.get("end")
        text = item.get("text", item.get("word"))
        if (
            not isinstance(start, (float, int))
            or not isinstance(end, (float, int))
            or not isinstance(text, str)
            or not text.strip()
        ):
            raise ValueError("Malformed provider word fields")
        start, end = round(start * 1000), round(end * 1000)
        if not 0 <= previous <= start < end <= duration_ms + 50:
            raise ValueError("Invalid provider timing bounds")
        words.append({"text": text, "start_ms": start, "end_ms": end})
        previous = end
    return words


class Provider:
    def __init__(self, token):
        self.token = token

    def call(self, suffix="", body=None):
        # Never propagate provider bodies, authorization or signed audio URLs to logs.
        attempts = 1 if body is not None else 3
        for attempt in range(attempts):
            request = urllib.request.Request(
                ENDPOINT + suffix,
                data=canonical(body) if body is not None else None,
                headers={
                    "Authorization": "Bearer " + self.token,
                    "Content-Type": "application/json",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    return json.load(response)
            except (urllib.error.URLError, TimeoutError):
                if attempt + 1 == attempts:
                    raise RuntimeError(
                        "TTS transport failed; persisted job state must be resumed"
                    ) from None
                time.sleep(2**attempt)

    def download(self, url):
        if not isinstance(url, str) or not url.startswith("https://"):
            raise ValueError("Invalid audio download URL")
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url, timeout=60) as response:
                    data = response.read(20_000_001)
                if not 0 < len(data) <= 20_000_000:
                    raise ValueError("Audio download size limit")
                return data
            except urllib.error.URLError:
                if attempt == 2:
                    raise RuntimeError(
                        "Audio download failed; resume cached job"
                    ) from None
                time.sleep(2**attempt)


def synthesize(spec, cache_root, provider=None, offline=True, timeout=300):
    key = digest(canonical(spec))
    directory = Path(cache_root) / key
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "entry.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if (directory / "complete.json").exists():
            return key, verify_entry(directory)
        if offline:
            raise ValueError("Offline TTS cache miss")
        if provider is None:
            raise ValueError("Online mode requires a provider")
        job_path = directory / "job.json"
        if job_path.exists():
            job = json.loads(job_path.read_text())
            if job.get("state") == "submitting":
                raise RuntimeError(
                    "Ambiguous prior submit; reconcile provider request ID before retry"
                )
        else:
            write_json(directory / "request.json", spec)
            write_json(job_path, {"state": "submitting"})
            result = provider.call(body={"model_id": MODEL, "input": spec["input"]})
            rid = result.get("request_id", result.get("id"))
            write_json(
                directory / "submit.json",
                {"request_id": rid, "status": result.get("status")},
            )
            output = result.get("output") or result
            if "audio" in output:
                job = {"state": "completed", "request_id": rid, "output": output}
            elif isinstance(rid, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,128}", rid):
                job = {"state": "queued", "request_id": rid}
            else:
                raise ValueError("Provider returned no usable request ID")
            write_json(job_path, job)
        deadline = time.monotonic() + timeout
        if job["state"] != "completed":
            rid = job["request_id"]
            while time.monotonic() < deadline:
                status = provider.call(f"/{rid}/status").get("status")
                write_json(
                    directory / "poll.json", {"request_id": rid, "status": status}
                )
                if status == "COMPLETED":
                    result = provider.call(f"/{rid}")
                    job = {
                        "state": "completed",
                        "request_id": rid,
                        "output": result.get("output") or result,
                    }
                    write_json(job_path, job)
                    break
                if status in {"FAILED", "CANCELLED"}:
                    raise RuntimeError(
                        "Provider job failed; no automatic paid resubmit"
                    )
                time.sleep(1)
            else:
                raise TimeoutError("TTS deadline exceeded; request ID retained")
        output = job["output"]
        audio_path = directory / "original.mp3"
        if not audio_path.exists():
            audio_path.write_bytes(provider.download(output["audio"]["url"]))
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-y",
                "-i",
                str(audio_path),
                "-ar",
                "48000",
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(directory / "speech.wav"),
            ],
            check=True,
        )
        with wave.open(str(directory / "speech.wav")) as audio:
            samples = audio.getnframes()
        raw = output.get("timestamps")
        alignment = normalize_alignment(raw, round(samples / 48))
        write_json(directory / "raw_alignment.json", raw)
        write_json(directory / "alignment.json", alignment)
        metadata = {
            "request_id": job.get("request_id"),
            "samples": samples,
            "sample_rate": 48000,
            "alignment_mode": "word" if alignment else "segment",
            "files": {
                name: file_hash(directory / name)
                for name in (
                    "request.json",
                    "original.mp3",
                    "speech.wav",
                    "alignment.json",
                    "raw_alignment.json",
                )
            },
        }
        write_json(directory / "complete.json", metadata)
        # Remove transient signed URLs after successful materialization.
        write_json(job_path, {"state": "cached", "request_id": job.get("request_id")})
        return key, metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    parser.add_argument(
        "--page",
        choices=("layouts", "users", "sub_organizations", "edocs_credit_note", *COUNTRY_PAGES),
        default="layouts",
    )
    parser.add_argument("--locale", action="append", choices=LOCALES)
    parser.add_argument(
        "--credential-file", default="/Users/daniel/DocBits/envs/dev/eu/doc2api.env"
    )
    args = parser.parse_args()
    provider = None
    if args.online:
        from dotenv import dotenv_values

        provider = Provider(
            dotenv_values(args.credential_file)["TOUCHLESS_ADVISOR_API_KEY"]
        )
    settings = json.loads((ROOT / "voice_settings.json").read_text())
    for locale in args.locale or ("en", "de", "ja"):
        content = json.loads(
            (ROOT / f"content/{args.page}/locales/{locale}.json").read_text()
        )
        for segment in content["segments"]:
            spec = request_spec(
                args.page,
                segment["id"],
                segment["narration"],
                locale,
                settings[locale],
            )
            key, meta = synthesize(
                spec, ROOT / "cache/tts", provider, offline=not args.online
            )
            print(
                locale,
                segment["id"],
                key[:12],
                meta["samples"],
                meta["alignment_mode"],
                flush=True,
            )


if __name__ == "__main__":
    main()
