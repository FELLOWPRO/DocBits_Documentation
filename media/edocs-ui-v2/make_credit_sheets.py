"""Review every real credit-note capture and every composed picture-track shot."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("locale")
    args = parser.parse_args()
    work = Path.cwd() / "output/edocs-ui-v2"
    destination = work / "credit-sheets" / args.locale
    destination.mkdir(parents=True, exist_ok=True)
    capture = work / "captures" / args.locale
    rows = json.loads((capture / "capture.json").read_text())["captures"]
    pictures = (
        work
        / "pipeline/scripts/settings_assistant/explainer_videos/out-v2/pictures"
        / args.locale
        / "edocs_credit_note"
    )
    groups = {
        "captures": [capture / row["file"] for row in rows],
        "films": sorted(pictures.glob("[0-9][0-9].png")),
    }
    assert len(groups["captures"]) == 12 and len(groups["films"]) == 13
    for label, files in groups.items():
        for start in range(0, len(files), 6):
            sheet = Image.new("RGB", (1800, 720), "#0A2531")
            draw = ImageDraw.Draw(sheet)
            for index, filename in enumerate(files[start : start + 6]):
                frame = ImageOps.contain(
                    Image.open(filename).convert("RGB"), (590, 325)
                )
                x, y = (index % 3) * 600, (index // 3) * 360
                sheet.paste(frame, (x, y + 25))
                draw.text((x + 5, y + 5), filename.name, fill="white")
            sheet.save(destination / f"{label}-{start//6:02}.png")
    print(json.dumps(dict(locale=args.locale, captures=12, shots=13)))


if __name__ == "__main__":
    main()
