"""Offline builds for completed captures in exactly one locale; resumable."""

import argparse
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import json
from pathlib import Path
import subprocess
import sys
import time

PIPELINE = Path("/repo/scripts/settings_assistant/explainer_videos")
sys.path.insert(0, str(PIPELINE))
from manifest import source_inputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", required=True)
    parser.add_argument("--captures", type=Path, required=True)
    parser.add_argument("--delivery", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--all-countries", action="store_true")
    parser.add_argument("--exclude-country", action="append", default=[])
    args = parser.parse_args()
    original = json.loads(args.delivery.read_text())["locales"]
    targets = original["en" if args.all_countries else args.locale]["films"]
    if args.all_countries:
        assert args.locale in ("pl", "pt", "zh") and len(targets) == 40
    assert set(args.exclude_country) <= set(targets)
    targets = [country for country in targets if country not in args.exclude_country]
    pending = set(targets)
    active = {}
    deadline = time.monotonic() + 3600
    log_directory = args.out / "logs" / args.locale
    log_directory.mkdir(parents=True, exist_ok=True)

    def render(country):
        page = "edocs_country_" + country.replace("-", "_")
        provenance = args.out / page / (args.locale + ".provenance.json")
        capture = args.captures / country
        if provenance.exists():
            current = json.loads(provenance.read_text())
            recorded = {
                r["name"]: r["sha256"]
                for r in current["ui_picture"]["capture"]["captures"]
            }
            observed = {
                r["name"]: r["sha256"]
                for r in json.loads((capture / "capture.json").read_text())["captures"]
            }
            if current["source_inputs"] == source_inputs(page) and recorded == observed:
                return country
        with (log_directory / (country + ".log")).open("w") as log:
            subprocess.run(
                [
                    sys.executable,
                    str(PIPELINE / "ui_picture.py"),
                    "--locale",
                    args.locale,
                    "--page",
                    page,
                    "--captures",
                    str(capture),
                    "--out",
                    str(args.out),
                ],
                check=True,
                stdout=log,
                stderr=subprocess.STDOUT,
            )
        return country

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        while pending or active:
            if time.monotonic() > deadline:
                raise TimeoutError(
                    "Capture wait expired; completed builds are retained"
                )
            for country in sorted(pending):
                if len(active) >= args.workers:
                    break
                if (args.captures / country / "complete.json").exists():
                    active[executor.submit(render, country)] = country
                    pending.remove(country)
            if active:
                completed, _ = wait(active, timeout=1, return_when=FIRST_COMPLETED)
                for future in completed:
                    country = future.result()
                    del active[future]
                    print(
                        json.dumps(
                            dict(
                                locale=args.locale,
                                country=country,
                                version=2,
                                ready=True,
                            )
                        ),
                        flush=True,
                    )
            else:
                time.sleep(1)
    print(
        json.dumps(
            dict(locale=args.locale, version=2, count=len(targets), complete=True)
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
