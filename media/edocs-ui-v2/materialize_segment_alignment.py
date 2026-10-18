"""Recover existing completed Chinese speech using measured segment captions.

This offline-only helper never submits, downloads, or changes audio. Provider
character timestamps remain intact as evidence; unusable word timing is omitted.
"""

import argparse
import fcntl
import json
from pathlib import Path
import subprocess
import sys
import wave

PIPELINE = Path("/repo/scripts/settings_assistant/explainer_videos")
sys.path.insert(0, str(PIPELINE))
from cache import canonical, digest, file_hash, verify_entry, write_json
from tts import normalize_alignment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", required=True)
    parser.add_argument("--request-id", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if len(args.key) != 64 or any(c not in "0123456789abcdef" for c in args.key):
        raise ValueError("Invalid cache key")
    directory = PIPELINE / "cache/tts" / args.key
    with (directory / "entry.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if (directory / "complete.json").exists():
            raise ValueError("Completed entries are immutable")
        request = json.loads((directory / "request.json").read_text())
        assert digest(canonical(request)) == args.key
        assert request["audio_locale"] == "zh"
        job_path = directory / "job.json"
        job = json.loads(job_path.read_text())
        submit = json.loads((directory / "submit.json").read_text())
        assert job["state"] == "completed"
        assert job["request_id"] == submit["request_id"] == args.request_id
        raw = job["output"]["timestamps"]
        assert raw and all("characters" in block for block in raw)
        with wave.open(str(directory / "speech.wav")) as audio:
            assert audio.getframerate() == 48000
            assert audio.getnchannels() == 1 and audio.getsampwidth() == 2
            samples = audio.getnframes()
            assert samples > 0
            pcm_hash = digest(audio.readframes(samples))
        decoded = subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-i",
                str(directory / "original.mp3"),
                "-ar",
                "48000",
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                "-f",
                "s16le",
                "pipe:1",
            ],
            check=True,
            capture_output=True,
        ).stdout
        assert len(decoded) == samples * 2 and digest(decoded) == pcm_hash
        try:
            normalize_alignment(raw, round(samples / 48))
        except ValueError as error:
            failure = str(error)
        else:
            raise ValueError("Provider timing is usable; no fallback is needed")
        before = {
            name: file_hash(directory / name)
            for name in ("request.json", "original.mp3", "speech.wav", "submit.json")
        }
        # Preserve the original provider response locally. It may contain a
        # transient signed URL, so only its hash is included in the QA receipt.
        original = directory / "job.provider-response.json"
        assert not original.exists()
        original.write_bytes(job_path.read_bytes())
        write_json(directory / "raw_alignment.json", raw)
        write_json(directory / "alignment.json", [])
        metadata = {
            "request_id": args.request_id,
            "samples": samples,
            "sample_rate": 48000,
            "alignment_mode": "segment",
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
        assert verify_entry(directory) == metadata
        assert all(file_hash(directory / name) == sha for name, sha in before.items())
        assert json.loads((original).read_text())["output"]["timestamps"] == raw
        write_json(job_path, {"state": "cached", "request_id": args.request_id})
        receipt = {
            "cache_key": args.key,
            "request_id": args.request_id,
            "locale": "zh",
            "provider_alignment_error": failure,
            "alignment_mode": "segment",
            "duration_seconds": samples / 48000,
            "samples": samples,
            "sample_rate": 48000,
            "provider_block_bounds_seconds": [
                {
                    "start": block["character_start_times_seconds"][0],
                    "end": block["character_end_times_seconds"][-1],
                }
                for block in raw
            ],
            "original_response_sha256": file_hash(original),
            "unchanged_files": before,
            "complete": metadata,
            "new_provider_request": False,
            "audio_modified": False,
            "word_alignment_claimed": False,
            "caption_method": "Native text with measured segment reading holds",
            "listening_review": "not performed",
        }
        write_json(args.receipt, receipt)
        print(json.dumps({"cache_key": args.key, "mode": "segment", "verified": True}))


if __name__ == "__main__":
    main()
