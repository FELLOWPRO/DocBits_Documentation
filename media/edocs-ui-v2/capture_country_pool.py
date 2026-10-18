"""Read-only captures in disjoint country subsets of exactly one UI locale."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

from prepare_locale import FOLDERS, PACKAGE, ROOT, WORK


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("locale", choices=FOLDERS)
    parser.add_argument("--workers", type=int, choices=(1, 2, 3), default=3)
    args = parser.parse_args()
    catalogue = ROOT / "output/edocs-support/catalog.json"
    countries = json.loads(catalogue.read_text())["countries"]
    destination = WORK / "countries" / args.locale
    destination.mkdir(parents=True, exist_ok=True)
    pending = [
        country["slug"]
        for country in countries
        if not (destination / country["slug"] / "complete.json").is_file()
    ]
    subsets = [pending[index :: args.workers] for index in range(args.workers)]

    def capture(item):
        index, subset = item
        if not subset:
            return
        log = WORK / f"capture-countries-{args.locale}-{index}.log"
        with log.open("w") as stream:
            subprocess.run(
                [
                    "node",
                    str(PACKAGE / "capture_countries.cjs"),
                    args.locale,
                    str(destination),
                    str(catalogue),
                    ",".join(subset),
                ],
                cwd=ROOT,
                stdout=stream,
                stderr=subprocess.STDOUT,
                check=True,
            )
        print(
            json.dumps(dict(locale=args.locale, subset=index, count=len(subset))),
            flush=True,
        )

    # Each browser changes Tolgee only in its disposable context. No shared user
    # preference or organisation configuration changes. Country sets never overlap.
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(capture, enumerate(subsets)))
    for country in countries:
        marker = json.loads(
            (destination / country["slug"] / "complete.json").read_text()
        )
        assert marker["locale"] == args.locale and marker["country"] == country["slug"]
    print(
        json.dumps(dict(locale=args.locale, count=len(countries), complete=True)),
        flush=True,
    )


if __name__ == "__main__":
    main()
