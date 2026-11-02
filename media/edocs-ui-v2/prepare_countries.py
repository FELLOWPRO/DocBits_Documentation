"""Prepare and accept country films for one locale with exact mirror parity."""

import argparse
import html
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

from prepare_locale import ROOT, PACKAGE, WORK, PIPELINE, FOLDERS, digest, git

SECTION = "administration-and-setup/settings/global-settings/document-types/edi/supported-electronic-documents/countries"
NOTES = {
    "en": "This read-only walkthrough shows the country’s existing DocBits configuration. Check the effective source and active version, then validate representative invoices, credit notes and exports in your own organisation.",
    "de": "Dieser lesende Rundgang zeigt die in DocBits vorhandene Konfiguration für das Land. Prüfen Sie die verwendete Quelle und aktive Version und testen Sie repräsentative Rechnungen, Gutschriften und Exporte in Ihrer eigenen Organisation.",
    "es": "Este recorrido de solo lectura muestra la configuración existente del país en DocBits. Compruebe la fuente utilizada y la versión activa y valide facturas, notas de crédito y exportaciones representativas en su organización.",
    "fr": "Cette visite en lecture seule montre la configuration existante du pays dans DocBits. Vérifiez la source utilisée et la version active, puis testez des factures, des avoirs et des exports représentatifs dans votre organisation.",
    "it": "Questa panoramica in sola lettura mostra la configurazione esistente del paese in DocBits. Verificate la fonte utilizzata e la versione attiva, quindi provate fatture, note di credito ed esportazioni rappresentative nella vostra organizzazione.",
    "nl": "Deze rondleiding zonder wijzigingen toont de bestaande DocBits-configuratie voor het land. Controleer de gebruikte bron en actieve versie en test representatieve facturen, creditnota’s en exports in uw eigen organisatie.",
    "pl": "Ten przegląd bez wprowadzania zmian pokazuje istniejącą konfigurację kraju w DocBits. Sprawdź używane źródło i aktywną wersję, a następnie przetestuj reprezentatywne faktury, noty kredytowe i eksporty we własnej organizacji.",
    "pt": "Este percurso apenas de leitura mostra a configuração existente do país no DocBits. Verifique a fonte utilizada e a versão ativa e teste faturas, notas de crédito e exportações representativas na sua organização.",
    "zh": "此只读演示展示该国家或地区在 DocBits 中的现有配置。请检查实际使用的来源和活动版本，并在您自己的组织中测试有代表性的发票、贷项通知单和导出。",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("locale", choices=FOLDERS)
    parser.add_argument("--accept", action="store_true")
    parser.add_argument("--new-media", action="store_true")
    parser.add_argument("--exclude-country", action="append", default=[])
    args = parser.parse_args()
    locale = args.locale
    original = json.loads(
        (ROOT / "media/edocs-country-support/delivery.json").read_text()
    )["locales"]
    available = original["en" if args.new_media else locale]["films"]
    if args.new_media:
        assert locale in ("pl", "pt", "zh") and len(available) == 40
    assert set(args.exclude_country) <= set(available)
    assert not args.exclude_country or args.new_media
    available = [
        country for country in available if country not in args.exclude_country
    ]
    translations = json.loads(
        (ROOT / f"media/edocs-country-support/translations/{locale}.json").read_text()
    )
    assert available, "No existing country films in this locale to revise"
    rows = []
    files = []
    mirror = ROOT / FOLDERS[locale]
    for country in available:
        page = "edocs_country_" + country.replace("-", "_")
        out = PIPELINE / "out-v2" / page
        provenance = json.loads((out / f"{locale}.provenance.json").read_text())
        for name, expected in provenance["source_inputs"].items():
            assert digest(PIPELINE / name) == expected, (country, name)
        capture = provenance["ui_picture"]["capture"]
        assert (
            capture["locale"] == locale
            and capture["country"] == country
            and not capture["mutations"]
        )
        ui = provenance["ui_picture"]
        assert ui["real_ui_background_frames"] == ui["total_frames"]
        technical = json.loads((out / f"{locale}.qa.json").read_text())
        audio = json.loads((out / f"{locale}.audio.json").read_text())
        assert (
            technical["full_decode"]
            and technical["faststart"]
            and technical["bytes"] < 10000000
        )
        assert abs(technical["loudness_lufs"] + 16) <= 0.5
        assert audio["audio_locale"] == locale
        filename = f"edocs-support-{country}-{locale}-v2"
        for extension in ("mp4", "vtt"):
            relative = f".gitbook/assets/{filename}.{extension}"
            shutil.copyfile(out / f"{locale}.{extension}", mirror / relative)
            files.append(relative)
        relative = SECTION + "/" + country + ".md"
        path = mirror / relative
        text = path.read_text()
        if args.new_media:
            poster = f".gitbook/assets/edocs-support-{country}-{locale}.png"
            source = WORK / "countries" / locale / country / "rules.png"
            row = next(r for r in capture["captures"] if r["name"] == "rules")
            assert digest(source) == row["sha256"]
            shutil.copyfile(source, mirror / poster)
            files.append(poster)
            marker = "<!-- Country screenshot and narrated film pending; no unavailable media is linked. -->"
            if marker in text:
                country_text = translations["countries"][country]
                caption = translations[
                    (
                        "screen_caption"
                        if capture["representative"]
                        else "screen_empty_caption"
                    )
                ]
                image_ref = os.path.relpath(mirror / poster, path.parent)
                video_ref = os.path.relpath(
                    mirror / f".gitbook/assets/{filename}.mp4", path.parent
                )
                captions_ref = video_ref.removesuffix(".mp4") + ".vtt"
                block = (
                    f"## {translations['screen_title']}\n\n"
                    f'<figure><img src="{image_ref}" alt="{html.escape(country_text["name"], quote=True)}">'
                    f"<figcaption><p>{caption}</p></figcaption></figure>\n\n"
                    f"## {translations['video_title']}\n\n"
                    f"{translations['video_caption']}\n\n{NOTES[locale]}\n\n"
                    f'{{% file src="{video_ref}" %}}\n'
                    f"{country_text['name']} — {translations['video_title']}\n"
                    "{% endfile %}\n\n"
                    f'{{% file src="{captions_ref}" %}}\nWebVTT\n'
                    "{% endfile %}"
                )
                text = text.replace(marker, block)
        if NOTES[locale] not in text:
            at = text.index("{% file ")
            text = text[:at] + NOTES[locale] + "\n\n" + text[at:]
        for extension in ("mp4", "vtt"):
            text = text.replace(
                f"edocs-support-{country}-{locale}.{extension}",
                f"{filename}.{extension}",
            )
        path.write_text(text)
        files.append(relative)
        # All supplied attachment targets must remain inside the documentation.
        assert text.count("{% file ") == text.count("{% endfile %}")
        for reference in re.findall(r'\{% file src="([^"]+)"', text):
            target = (path.parent / reference).resolve()
            assert target.is_relative_to(mirror) and target.is_file(), (
                country,
                reference,
            )
        destination = PACKAGE / "countries" / locale / country
        destination.mkdir(parents=True, exist_ok=True)
        for row in capture["captures"]:
            source = WORK / "countries" / locale / country / row["file"]
            assert digest(source) == row["sha256"]
            shutil.copyfile(source, destination / row["file"])
        shutil.copyfile(
            WORK / "countries" / locale / country / "capture.json",
            destination / "capture.json",
        )
        rows.append(
            dict(
                country=country,
                technical=technical,
                audio=audio,
                provenance=provenance,
                mp4_sha256=digest(out / f"{locale}.mp4"),
                vtt_sha256=digest(out / f"{locale}.vtt"),
            )
        )
    for country in args.exclude_country:
        # A missing narration must not prevent delivery of the genuine screenshot.
        relative = SECTION + "/" + country + ".md"
        path = mirror / relative
        poster = f".gitbook/assets/edocs-support-{country}-{locale}.png"
        source = WORK / "countries" / locale / country
        capture = json.loads((source / "capture.json").read_text())
        row = next(r for r in capture["captures"] if r["name"] == "rules")
        assert capture["locale"] == locale and not capture["mutations"]
        assert digest(source / "rules.png") == row["sha256"]
        shutil.copyfile(source / "rules.png", mirror / poster)
        pending = {
            "pl": "Film z narracją dla tego kraju nie jest jeszcze dostępny.",
            "pt": "O filme narrado deste país ainda não está disponível.",
            "zh": "此国家或地区的配音视频暂未提供。",
        }[locale]
        marker = "<!-- Country screenshot and narrated film pending; no unavailable media is linked. -->"
        image_ref = os.path.relpath(mirror / poster, path.parent)
        name = html.escape(translations["countries"][country]["name"], quote=True)
        block = (
            f"## {translations['screen_title']}\n\n"
            f'<figure><img src="{image_ref}" alt="{name}">'
            f"<figcaption><p>{translations['screen_caption']}</p></figcaption></figure>\n\n"
            f"## {translations['video_title']}\n\n{pending}"
        )
        text = path.read_text()
        if marker in text:
            path.write_text(text.replace(marker, block))
        assert pending in path.read_text() and "{% file " not in path.read_text()
        files.extend([relative, poster])
        destination = PACKAGE / "countries" / locale / country
        destination.mkdir(parents=True, exist_ok=True)
        for row in capture["captures"]:
            assert digest(source / row["file"]) == row["sha256"]
            shutil.copyfile(source / row["file"], destination / row["file"])
        shutil.copyfile(source / "capture.json", destination / "capture.json")
    delivery_path = PACKAGE / "delivery.json"
    delivery = json.loads(delivery_path.read_text())
    delivery["countries"][locale] = available
    if args.exclude_country:
        delivery.setdefault("pending_countries", {})[locale] = args.exclude_country
    delivery_path.write_text(json.dumps(delivery, ensure_ascii=False, indent=2) + "\n")
    evidence = PACKAGE / "qa" / locale / "countries"
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / "media.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n"
    )
    (WORK / f"touched-countries-{locale}.json").write_text(
        json.dumps(files, indent=2) + "\n"
    )
    if args.accept:
        browser = json.loads(
            (WORK / "browser-countries" / locale / "browser.json").read_text()
        )
        assert {r["country"] for r in browser} == set(available)
        assert all(
            r["ended"] and r["range206"] and r["keyboard"] and not r["errors"]
            for r in browser
        )
        shutil.copyfile(
            WORK / "browser-countries" / locale / "browser.json",
            evidence / "browser.json",
        )
        for sheet in (WORK / "sheets" / locale).glob("*.png"):
            shutil.copyfile(sheet, evidence / sheet.name)
        (evidence / "review.json").write_text(
            json.dumps(
                dict(
                    locale=locale,
                    count=len(available),
                    visual="Every actual capture and every composed film shot inspected; passed",
                    technical="passed",
                    browser="Actual documentation attachments: playback/seek/end, native captions, keyboard, 380 px and Range 206 passed",
                    listening="Not performed; pronunciation is not certified",
                    kind="Real UI screenshot walkthrough; no continuous screen recording or document acceptance test claimed",
                ),
                indent=2,
            )
            + "\n"
        )
        if locale != "en":
            branch = "codex/trl72-edocs-" + locale
            parent = git("rev-parse", branch)
            env = dict(
                os.environ, GIT_INDEX_FILE=str(WORK / f"countries-{locale}.index")
            )
            git("read-tree", parent, env=env)
            for relative in files:
                blob = git("hash-object", "-w", str(mirror / relative))
                git(
                    "update-index",
                    "--add",
                    "--cacheinfo",
                    "100644",
                    blob,
                    "readme/" + relative,
                    env=env,
                )
            tree = git("write-tree", env=env)
            commit = git(
                "commit-tree",
                tree,
                "-p",
                parent,
                input=f"docs(edocs,{locale}): show real country UI in version 2 videos\n".encode(),
            )
            git("update-ref", "refs/heads/" + branch, commit, parent)
            for relative in files:
                assert git("rev-parse", f"{branch}:readme/{relative}") == git(
                    "hash-object", str(mirror / relative)
                )
            print(json.dumps(dict(locale=locale, branch=branch, commit=commit)))
    print(
        json.dumps(
            dict(
                locale=locale,
                countries=len(available),
                accepted=args.accept,
                files=len(files),
            )
        )
    )


if __name__ == "__main__":
    main()
