"""Prepare one v2 credit-note variant and its exact main/source mirror."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import hashlib

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "media/edocs-ui-v2"
WORK = ROOT / "output/edocs-ui-v2"
PIPELINE = WORK / "pipeline/scripts/settings_assistant/explainer_videos"
FOLDERS = dict(
    en="docbits",
    de="deutsch",
    es="espanol",
    fr="french",
    it="italian",
    nl="dutch",
    pl="polish",
    pt="portuguese",
    zh="chinese",
)
PAGE = "administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md"
NOTES = {
    "en": "The video shows a read-only check in DocBits using FACTURX 1.0.05 / ZUGFeRD 2.1 as an example. Mappings and versions can differ in your organisation. Always check the active Transformation for the detected format.",
    "de": "Das Video zeigt eine lesende Prüfung in DocBits am Beispiel FACTURX 1.0.05 / ZUGFeRD 2.1. Zuordnungen und Versionen können in Ihrer Organisation abweichen. Prüfen Sie immer die aktive Transformation des erkannten Formats.",
    "es": "El vídeo muestra una revisión de solo lectura en DocBits con FACTURX 1.0.05 / ZUGFeRD 2.1 como ejemplo. Las asignaciones y versiones pueden variar en su organización. Compruebe siempre la Transformation activa del formato detectado.",
    "fr": "La vidéo montre une vérification en lecture seule dans DocBits, avec FACTURX 1.0.05 / ZUGFeRD 2.1 comme exemple. Les correspondances et les versions peuvent différer dans votre organisation. Vérifiez toujours la Transformation active du format détecté.",
    "it": "Il video mostra una verifica in sola lettura in DocBits, usando FACTURX 1.0.05 / ZUGFeRD 2.1 come esempio. Le mappature e le versioni possono variare nella vostra organizzazione. Verificate sempre la Transformation attiva del formato rilevato.",
    "nl": "De video toont een controle in DocBits zonder wijzigingen, met FACTURX 1.0.05 / ZUGFeRD 2.1 als voorbeeld. Toewijzingen en versies kunnen in uw organisatie verschillen. Controleer altijd de actieve Transformation voor het gedetecteerde formaat.",
    "pl": "Film pokazuje sprawdzenie w DocBits bez wprowadzania zmian, na przykładzie FACTURX 1.0.05 / ZUGFeRD 2.1. Mapowania i wersje mogą się różnić w Twojej organizacji. Zawsze sprawdzaj aktywną Transformation dla wykrytego formatu.",
    "pt": "O vídeo mostra uma verificação apenas de leitura no DocBits, usando FACTURX 1.0.05 / ZUGFeRD 2.1 como exemplo. Os mapeamentos e as versões podem variar na sua organização. Verifique sempre a Transformation ativa do formato detetado.",
    "zh": "视频以 FACTURX 1.0.05 / ZUGFeRD 2.1 为例，展示在 DocBits 中进行只读检查的过程。您组织中的映射和版本可能不同。请始终检查所识别格式的活动 Transformation。",
}

EXAMPLE_NOTES = {
    "en": "The older example XSLT shown in the video contains branches for 381 and 389. Check the actual Transformation to establish which codes this specific version preserves; the general code list does not prove coverage in every historical mapping.",
    "de": "Das gezeigte ältere XSLT-Beispiel enthält Zweige für 381 und 389. Prüfen Sie an der tatsächlichen Transformation, welche Codes diese konkrete Version erhält; die allgemeine Codeliste belegt keine Abdeckung in jeder historischen Zuordnung.",
    "es": "El ejemplo XSLT antiguo del vídeo contiene ramas para 381 y 389. Compruebe en la Transformation real qué códigos conserva esta versión concreta; la lista general de códigos no demuestra su cobertura en todas las asignaciones históricas.",
    "fr": "L’ancien exemple XSLT montré dans la vidéo contient des branches pour 381 et 389. Vérifiez dans la Transformation réelle les codes conservés par cette version précise ; la liste générale ne prouve pas leur prise en charge dans toutes les anciennes correspondances.",
    "it": "Il precedente esempio XSLT mostrato nel video contiene rami per 381 e 389. Verificate nella Transformation effettiva quali codici conserva questa versione specifica; l’elenco generale dei codici non ne dimostra la copertura in tutte le mappature storiche.",
    "nl": "Het oudere XSLT-voorbeeld in de video bevat vertakkingen voor 381 en 389. Controleer in de werkelijke Transformation welke codes deze specifieke versie behoudt; de algemene codelijst bewijst geen dekking in elke historische toewijzing.",
    "pl": "Starszy przykład XSLT pokazany w filmie zawiera gałęzie dla kodów 381 i 389. Sprawdź w rzeczywistej Transformation, które kody zachowuje ta konkretna wersja; ogólna lista kodów nie dowodzi ich obsługi w każdym historycznym mapowaniu.",
    "pt": "O exemplo XSLT antigo apresentado no vídeo contém ramos para 381 e 389. Verifique na Transformation real quais os códigos preservados por esta versão específica; a lista geral de códigos não comprova a sua cobertura em todos os mapeamentos históricos.",
    "zh": "视频中的旧版 XSLT 示例包含针对 381 和 389 的分支。请检查实际的 Transformation，确认这一具体版本保留哪些代码；通用代码列表不能证明每个历史映射都支持这些代码。",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args, **kwargs):
    return subprocess.check_output(["git", *args], cwd=ROOT, **kwargs).decode().strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("locale", choices=FOLDERS)
    p.add_argument("--accept", action="store_true")
    args = p.parse_args()
    locale = args.locale
    out = PIPELINE / "out-v2/edocs_credit_note"
    mirror = ROOT / FOLDERS[locale]
    provenance = json.loads((out / f"{locale}.provenance.json").read_text())
    for name, expected in provenance["source_inputs"].items():
        assert digest(PIPELINE / name) == expected, name
    qa = json.loads((out / f"{locale}.qa.json").read_text())
    assert qa["full_decode"] and qa["faststart"] and qa["bytes"] < 10000000
    assert (
        provenance["ui_picture"]["total_frames"]
        == provenance["ui_picture"]["real_ui_background_frames"]
    )
    filename = f"edocs-credit-note-{locale}-v2"
    for extension in ("mp4", "vtt"):
        shutil.copyfile(
            out / f"{locale}.{extension}",
            mirror / ".gitbook/assets" / f"{filename}.{extension}",
        )
    page = mirror / PAGE
    text = page.read_text()
    if NOTES[locale] not in text:
        at = text.index("{% file ")
        text = text[:at] + NOTES[locale] + "\n\n" + text[at:]
    if EXAMPLE_NOTES[locale] not in text:
        at = text.index("{% file ")
        text = text[:at] + EXAMPLE_NOTES[locale] + "\n\n" + text[at:]
    for extension in ("mp4", "vtt"):
        text = text.replace(
            f"edocs-credit-note-{locale}.{extension}", f"{filename}.{extension}"
        )
    page.write_text(text)
    destination = PACKAGE / "captures" / locale
    destination.mkdir(parents=True, exist_ok=True)
    capture = json.loads((WORK / "captures" / locale / "capture.json").read_text())
    for row in capture["captures"]:
        source = WORK / "captures" / locale / row["file"]
        assert digest(source) == row["sha256"]
        shutil.copyfile(source, destination / row["file"])
    shutil.copyfile(
        WORK / "captures" / locale / "capture.json", destination / "capture.json"
    )
    evidence = PACKAGE / "qa" / locale / "credit-note"
    evidence.mkdir(parents=True, exist_ok=True)
    for suffix in (
        "qa.json",
        "audio.json",
        "provenance.json",
        "timing.json",
        "contact.png",
    ):
        shutil.copyfile(out / f"{locale}.{suffix}", evidence / suffix)
    delivery_path = PACKAGE / "delivery.json"
    delivery = json.loads(delivery_path.read_text())
    delivery["credit_note"][locale] = dict(
        version=2,
        mp4_sha256=digest(out / f"{locale}.mp4"),
        vtt_sha256=digest(out / f"{locale}.vtt"),
        duration_ms=qa["duration_ms"],
        listening_review="not performed",
    )
    delivery_path.write_text(json.dumps(delivery, ensure_ascii=False, indent=2) + "\n")
    if args.accept:
        browser = json.loads((WORK / "browser" / locale / "browser.json").read_text())
        assert (
            browser["ended"]
            and browser["range206"]
            and browser["metadata"]["language"] == locale
        )
        shutil.copyfile(
            WORK / "browser" / locale / "browser.json", evidence / "browser.json"
        )
        shutil.copyfile(
            WORK / "browser" / locale / "browser-380.png", evidence / "browser-380.png"
        )
        for sheet in (WORK / "credit-sheets" / locale).glob("*.png"):
            shutil.copyfile(sheet, evidence / sheet.name)
        review = dict(
            visual="All 12 real UI captures and all 13 composed shots inspected, including enlarged code and mobile sample",
            browser="passed",
            technical="passed",
            listening="not performed",
            ui_kind="screenshot walkthrough, not continuous recording",
            configuration_mutations=[],
        )
        (evidence / "review.json").write_text(json.dumps(review, indent=2) + "\n")
        if locale != "en":
            branch = "codex/trl72-edocs-" + locale
            parent = git("rev-parse", branch)
            index = WORK / f"source-{locale}.index"
            env = dict(os.environ, GIT_INDEX_FILE=str(index))
            git("read-tree", parent, env=env)
            for relative in (
                PAGE,
                f".gitbook/assets/{filename}.mp4",
                f".gitbook/assets/{filename}.vtt",
            ):
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
                input=f"docs(edocs,{locale}): show real UI in credit-note video v2\n".encode(),
            )
            git("update-ref", "refs/heads/" + branch, commit, parent)
            for relative in (
                PAGE,
                f".gitbook/assets/{filename}.mp4",
                f".gitbook/assets/{filename}.vtt",
            ):
                assert git("rev-parse", f"{branch}:readme/{relative}") == git(
                    "hash-object", str(mirror / relative)
                )
            print(json.dumps(dict(locale=locale, branch=branch, commit=commit)))
    print(json.dumps(dict(locale=locale, ready=True, accepted=args.accept)))


if __name__ == "__main__":
    main()
