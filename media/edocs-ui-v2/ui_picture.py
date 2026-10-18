"""Compose picture tracks from verified real UI captures; use retained mux/QA.

No product controls or values are drawn. Titles and numbered steps sit outside
the screenshot. Crops only magnify the original pixels. Speech is cache-only.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

from build import ROOT, build, prepare
from cache import file_hash, write_json
from qa import audio_check
from toolchain import install_fonts, verify


def title_font(locale, size=27):
    name = "NotoSansCJKsc-Regular.otf" if locale == "zh" else "NotoSans-Regular.ttf"
    return ImageFont.truetype(str(ROOT / "cache/fonts" / name), size)


def composition(source, title, locale, number, total, destination, crop=None):
    raw = Image.open(source).convert("RGB")
    if crop == "code":
        crop = (100, 170, raw.width, min(raw.height, 820))
    elif crop == "versions":
        crop = (0, 0, raw.width, min(raw.height, 780))
    if crop:
        raw = raw.crop(crop)
    canvas = Image.new("RGB", (1280, 720), "#0A2531")
    draw = ImageDraw.Draw(canvas)
    font = title_font(locale)
    while draw.textlength(title, font=font) > 1080:
        font = title_font(locale, font.size - 1)
        if font.size < 19:
            raise ValueError("Unreadable title: " + title)
    draw.text((26, 13), title, font=font, fill="#F5F5F5")
    draw.text((1176, 15), f"{number}/{total}", font=title_font(locale, 24), fill="#4DB6DA")
    # Every pixel in this region comes from a real, redacted DocBits UI capture.
    picture = ImageOps.contain(raw, (1240, 606), Image.Resampling.LANCZOS)
    canvas.paste(picture, ((1280-picture.width)//2, 60+(606-picture.height)//2))
    draw.line((20, 680, 1260, 680), fill="#4DB6DA", width=2)
    draw.text((26, 687), "DocBits · E-Doc", font=title_font(locale, 17), fill="#9FBDC9")
    canvas.save(destination)


def credit_plan(content, timing, captures):
    labels = content["labels"]
    # Stable real views follow the existing spoken diagnostic sequence.
    views = {
        "symptom": [("format-list", "DocBits · E-Doc · FACTURX / ZUGFeRD"), ("rules", "FACTURX / ZUGFeRD")],
        "codes": [("rules", "FACTURX / ZUGFeRD · 381 / 261 · 383 / 384")],
        "source": [("rules", labels["source"]), ("versions", labels["active"])],
        "transform": [("transformation-code", "FACTURX 1.0.05 / ZUGFeRD 2.1 · INVOICE_TYPE")],
        "paths": [("preview-panel", labels["test"]+" · "+labels["transform"]), ("extraction-paths-code", "Extraction Paths · invoice_type")],
        "activate": [("versions", labels["draft"]+" · "+labels["test"]+" · "+labels["activate"])],
        "safety": [("rules", labels["preserve"]), ("preview-panel", labels["safety"])],
        "sign": [("negative-sign-control", labels["sign"]), ("negative-sign", labels["result"]+" · Infor ERP / SAP")],
    }
    plan = []
    for segment in timing:
        shots = views[segment["segment_id"]]
        used = 0
        for index, (name, title) in enumerate(shots):
            frames = segment["frames"]-used if index == len(shots)-1 else segment["frames"]//len(shots)
            plan.append(dict(capture=name, title=title, frames=frames, segment_id=segment["segment_id"]))
            used += frames
    return plan


def country_plan(content, timing, captures):
    labels = content["labels"]
    if content["status"] == "unconfirmed":
        views = {s["segment_id"]: [("rules", content["country"]+" · "+labels["unconfirmed"])] for s in timing}
    else:
        views = {
            "formats": [("rules", content["country"]+" · "+content["representative"])],
            "workflow": [("transformation-code", labels["transform"]), ("extraction-paths-code", labels["extract"])],
            "accept": [("preview-panel", labels["accept"]), ("rules", labels["limits"])],
        }
    plan = []
    for segment in timing:
        shots = views[segment["segment_id"]]
        used = 0
        for index, (name, title) in enumerate(shots):
            frames = segment["frames"]-used if index == len(shots)-1 else segment["frames"]//len(shots)
            plan.append(dict(capture=name, title=title, frames=frames, segment_id=segment["segment_id"]))
            used += frames
    return plan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", required=True)
    parser.add_argument("--page", default="edocs_credit_note")
    parser.add_argument("--captures", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    verify()
    install_fonts()
    timing = prepare(args.locale, args.out, args.page)
    content = json.loads((ROOT / f"content/{args.page}/locales/{args.locale}.json").read_text())
    capture = json.loads((args.captures / "capture.json").read_text())
    assert capture["locale"] == args.locale and not capture["mutations"]
    assert capture["runtime_language"] == args.locale
    inputs = {row["name"]: row for row in capture["captures"]}
    for row in inputs.values():
        assert file_hash(args.captures / row["file"]) == row["sha256"], row["file"]
    plan = country_plan(content, timing, capture) if args.page.startswith("edocs_country_") else credit_plan(content, timing, capture)
    directory = args.out / args.page
    pictures = args.out / "pictures" / args.locale / args.page
    pictures.mkdir(parents=True, exist_ok=True)
    frames = []
    sections = []
    for index, shot in enumerate(plan):
        filename = pictures / f"{index:02}.png"
        crop = "code" if shot["capture"].endswith("-code") else "versions" if shot["capture"] == "versions" else None
        shot["crop"] = crop
        composition(args.captures / inputs[shot["capture"]]["file"], shot["title"], args.locale, index+1, len(plan), filename, crop)
        frames.append(filename)
        section = pictures / f"{index:02}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-i", str(filename), "-frames:v", str(shot["frames"]), "-an", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "15", "-pix_fmt", "yuv420p", "-color_range", "pc", str(section)], check=True)
        sections.append(section)
    concat = pictures / "concat.txt"
    concat.write_text("".join(f"file '{p.name}'\n" for p in sections))
    recording = pictures / "recording"
    recording.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(recording / f"{args.locale}.mp4")], check=True)
    shutil.copyfile(directory / f"{args.locale}.vtt", recording / f"{args.locale}.vtt")
    result = build(args.locale, args.out, args.page, recording=recording, poster_at=3.5)
    provenance = json.loads((directory / f"{args.locale}.provenance.json").read_text())
    provenance["ui_picture"] = {"version": 2, "kind": "real_ui_screenshot_walkthrough", "capture": capture, "shots": plan, "picture_sha256": file_hash(recording / f"{args.locale}.mp4"), "real_ui_background_frames": sum(s["frames"] for s in plan), "total_frames": sum(s["frames"] for s in timing), "configuration_mutations": [], "listening_review": "not performed"}
    write_json(directory / f"{args.locale}.provenance.json", provenance)
    write_json(directory / f"{args.locale}.audio.json", audio_check(args.out, args.locale, timing, args.page))
    sheet = Image.new("RGB", (1280, ((len(frames)+2)//3)*255), "#0A2531")
    for index, frame in enumerate(frames):
        thumb = Image.open(frame).resize((424,239), Image.Resampling.LANCZOS)
        sheet.paste(thumb, ((index%3)*427, (index//3)*255))
    sheet.save(directory / f"{args.locale}.contact.png")
    # Keep exact timing/provenance and composed keyframes; remove temporary encodes.
    for section in sections:
        section.unlink()
    print(json.dumps({"locale": args.locale, "page": args.page, "version": 2, "shots": len(plan), "technical": result}), flush=True)


if __name__ == "__main__":
    main()
