"""Contact sheets for every real capture and every composed film shot."""

import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps


def main():
    p = argparse.ArgumentParser()
    p.add_argument("locale")
    p.add_argument("--root", type=Path, default=Path.cwd())
    args = p.parse_args()
    work = args.root / "output/edocs-ui-v2"
    out = work / "sheets" / args.locale
    out.mkdir(parents=True, exist_ok=True)
    countries = sorted((work / "countries" / args.locale).glob("*/complete.json"))
    for start in range(0, len(countries), 5):
        group = countries[start : start + 5]
        sheet = Image.new("RGB", (2200, len(group) * 345), "#0A2531")
        draw = ImageDraw.Draw(sheet)
        for index, marker in enumerate(group):
            country = marker.parent.name
            capture = json.loads((marker.parent / "capture.json").read_text())
            for column, row in enumerate(capture["captures"]):
                image = Image.open(marker.parent / row["file"]).convert("RGB")
                if row["name"].endswith("-code"):
                    image = image.crop((0, 0, image.width, min(image.height, 880)))
                image = ImageOps.contain(image, (540, 312), Image.Resampling.LANCZOS)
                x, y = column * 550, index * 345
                sheet.paste(image, (x, y + 27))
                draw.text((x + 6, y + 6), country + " / " + row["name"], fill="white")
        sheet.save(out / f"captures-{start//5:02}.png")
    rendered = []
    pipeline = work / "pipeline/scripts/settings_assistant/explainer_videos/out-v2"
    for marker in countries:
        page = "edocs_country_" + marker.parent.name.replace("-", "_")
        frames = sorted(
            (pipeline / "pictures" / args.locale / page).glob("[0-9][0-9].png")
        )
        if frames:
            rendered.append((marker.parent.name, frames))
    for start in range(0, len(rendered), 5):
        group = rendered[start : start + 5]
        sheet = Image.new("RGB", (2200, len(group) * 276), "#0A2531")
        draw = ImageDraw.Draw(sheet)
        for row, (country, frames) in enumerate(group):
            draw.text((6, row * 276 + 5), country, fill="white")
            for column, frame in enumerate(frames):
                thumb = Image.open(frame).resize((438, 246), Image.Resampling.LANCZOS)
                sheet.paste(thumb, (column * 440, row * 276 + 25))
        sheet.save(out / f"films-{start//5:02}.png")
    print(
        json.dumps(
            dict(
                locale=args.locale,
                captured=len(countries),
                rendered=len(rendered),
                sheets=str(out),
            )
        )
    )


if __name__ == "__main__":
    main()
