"""Verify public GitBook preview attachments against the committed media bytes."""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import urllib.request

from prepare_locale import FOLDERS, PACKAGE, ROOT

SECTION = "administration-and-setup/settings/global-settings/document-types/edi"


def get(url, headers=None):
    request = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0", **(headers or {})}
    )
    return urllib.request.urlopen(request, timeout=45)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("locale", choices=FOLDERS)
    parser.add_argument("--commit", default="codex/trl72-edocs-docs")
    parser.add_argument("--countries", default="germany,costa-rica")
    args = parser.parse_args()
    status = json.loads(
        subprocess.check_output(
            [
                "gh",
                "api",
                "repos/FELLOWPRO/DocBits_Documentation/commits/"
                + args.commit.replace("/", "%2F")
                + "/status",
            ],
            cwd=ROOT,
        )
    )
    context = f"GitBook (./{FOLDERS[args.locale]}) - docs.docbits.com/"
    record = next(r for r in status["statuses"] if r["context"].startswith(context))
    assert record["state"] == "success", record
    preview = record["target_url"].rstrip("/")
    targets = [("credit-note-recognized-as-invoice", "edocs-credit-note")]
    delivery = json.loads((PACKAGE / "delivery.json").read_text())
    countries = args.countries.split(",") if args.countries else []
    for country in countries:
        if country in delivery["countries"].get(args.locale, []):
            targets.append(
                (
                    "supported-electronic-documents/" + country,
                    "edocs-support-" + country,
                )
            )
    receipts = []
    section = SECTION
    if args.locale == "zh":
        section = section.replace("administration-and-setup", "guan-li-yu-she-zhi")
    overview_url = f"{preview}/{section}/supported-electronic-documents?review={status['sha'][:12]}"
    with get(overview_url) as response:
        assert response.status == 200
        overview_markup = response.read().decode()
    catalogue = json.loads(
        (ROOT / "media/edocs-country-support/evidence/catalog.json").read_text()
    )
    guide_slugs = [country["slug"] for country in catalogue["countries"]]
    overview_links = {
        html.unescape(value).split("?")[0].split("#")[0].rstrip("/")
        for value in re.findall(r'href="([^"]+)"', overview_markup)
    }
    for slug in guide_slugs:
        assert any(
            link.endswith("/supported-electronic-documents/" + slug)
            for link in overview_links
        ), (overview_url, slug)
    for page, stem in targets:
        filename = f"{stem}-{args.locale}-v2.mp4"
        # A request made before import completion can leave a cached 404.
        # Key this read-only check to the commit, without changing page content.
        page_url = f"{preview}/{section}/{page}?review={status['sha'][:12]}"
        print(json.dumps(dict(checking=page_url)), flush=True)
        with get(page_url) as response:
            assert response.status == 200
            markup = response.read().decode()
        urls = re.findall(r'href="([^"]*' + re.escape(filename) + r'[^"]*)"', markup)
        assert urls, (page_url, filename)
        url = html.unescape(urls[0])
        expected = ROOT / FOLDERS[args.locale] / ".gitbook/assets" / filename
        with get(url) as response:
            data = response.read()
            mime = response.headers.get_content_type()
            assert response.status == 200 and mime == "video/mp4"
            assert data == expected.read_bytes()
        with get(url, {"Range": "bytes=0-1023"}) as response:
            assert response.status == 206 and len(response.read()) == 1024
            content_range = response.headers["Content-Range"]
            assert content_range == f"bytes 0-1023/{len(data)}"
        receipts.append(
            dict(
                preview=page_url,
                url=url,
                status=200,
                mime=mime,
                bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                range206=True,
                content_range=content_range,
            )
        )
    evidence = PACKAGE / "qa" / args.locale
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / "gitbook.json").write_text(
        json.dumps(
            dict(
                commit=status["sha"],
                import_state="success",
                overview=overview_url,
                linked_country_guides=len(guide_slugs),
                attachments=receipts,
            ),
            indent=2,
        )
        + "\n"
    )
    print(json.dumps(dict(locale=args.locale, preview=preview, verified=len(receipts))))


if __name__ == "__main__":
    main()
