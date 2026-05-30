#!/usr/bin/env python3
"""Generate a DocBits demo invoice PDF carrying several barcode types.

The PDF is used to demonstrate the **Barcode Assignment** feature: each barcode
encodes a value that a validator can map onto a document field (purchase order,
invoice number, supplier GLN, delivery note).

Barcodes are produced with ``zxingcpp`` — the *same* library the DocBits
barcode-service uses to decode them, so a round-trip read is guaranteed as long
as the symbols are rendered large enough to survive PDF rasterisation.

Default barcode set (matches BARCODE_EXTRACTION_TYPES=QRCODE,CODE128,EAN13):
    QRCode   -> Purchase Order   (PO-2026-00847)
    Code128  -> Invoice Number   (INV-2026-1185)
    EAN13    -> Supplier GLN      (4006381333931)

NOTE on DataMatrix: DocBits' barcode-service has a zxing extractor that supports
DataMatrix, but its *fast* path uses pyzbar/ZBar, which does NOT — and requesting
`DATAMATRIX` via BARCODE_EXTRACTION_TYPES makes the fast extractor raise
`'DATAMATRIX' is not a valid ZBarSymbol enum value`, failing the whole extraction.
So for a demo that actually extracts on dev, stick to ZBar-supported types.

Usage:
    python generate_barcode_invoice.py [--out PATH]
"""
from __future__ import annotations

import argparse
from io import BytesIO

import numpy as np
import zxingcpp
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

# --- DocBits brand palette ---------------------------------------------------
TEAL_DARK = (0x18 / 255, 0x33 / 255, 0x3D / 255)   # #18333d header band
TEAL = (0x23 / 255, 0x88 / 255, 0xAE / 255)        # #2388ae accents
GREY = (0.42, 0.45, 0.48)
LIGHT = (0.94, 0.96, 0.97)

# --- Barcode payloads (value <-> the field a validator would map it to) ------
BARCODES = [
    ("QRCode", zxingcpp.BarcodeFormat.QRCode, "PO-2026-00847", "Purchase Order"),
    ("Code128", zxingcpp.BarcodeFormat.Code128, "INV-2026-1185", "Invoice Number"),
    ("EAN-13", zxingcpp.BarcodeFormat.EAN13, "4006381333931", "Supplier GLN"),
]


def make_barcode_image(fmt, text: str, border: int = 6, scale: int = 3) -> ImageReader:
    """Render a barcode to a high-resolution PIL image with a white quiet zone."""
    raw = zxingcpp.write_barcode(fmt, text)
    arr = np.array(raw)
    img = Image.fromarray(arr).convert("L")
    # Upscale with nearest-neighbour so module edges stay crisp after rasterising.
    img = img.resize((img.width * scale, img.height * scale), Image.NEAREST)
    # Add a generous white quiet zone — zxing/pyzbar need it to lock on.
    canvas_img = Image.new("L", (img.width + 2 * border * scale,
                                 img.height + 2 * border * scale), 255)
    canvas_img.paste(img, (border * scale, border * scale))
    buf = BytesIO()
    canvas_img.save(buf, format="PNG")
    buf.seek(0)
    return ImageReader(buf)


def draw_invoice(path: str) -> None:
    width, height = A4
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("DocBits Demo Invoice — Barcode Assignment")

    # --- Header band ---------------------------------------------------------
    c.setFillColorRGB(*TEAL_DARK)
    c.rect(0, height - 36 * mm, width, 36 * mm, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(20 * mm, height - 20 * mm, "DocBits Demo GmbH")
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0.8, 0.88, 0.92)
    c.drawString(20 * mm, height - 27 * mm, "Musterstraße 1  ·  60311 Frankfurt am Main  ·  Germany")
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(1, 1, 1)
    c.drawRightString(width - 20 * mm, height - 22 * mm, "INVOICE")

    # --- Meta box with barcodes ---------------------------------------------
    top = height - 50 * mm
    c.setFillColorRGB(*GREY)
    c.setFont("Helvetica", 9)
    meta = [
        ("Invoice Number", "INV-2026-1185"),
        ("Invoice Date", "30 May 2026"),
        ("Purchase Order", "PO-2026-00847"),
        ("Delivery Note", "DN-2026-55012"),
        ("Supplier GLN", "4006381333931"),
    ]
    label_x, value_x = 20 * mm, 55 * mm
    y = top
    for label, value in meta:
        c.setFillColorRGB(*GREY)
        c.setFont("Helvetica", 9)
        c.drawString(label_x, y, label)
        c.setFillColorRGB(0.1, 0.12, 0.14)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(value_x, y, value)
        y -= 7 * mm

    # Bill-to block
    c.setFillColorRGB(*TEAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120 * mm, top, "Bill To")
    c.setFillColorRGB(0.1, 0.12, 0.14)
    c.setFont("Helvetica", 9)
    for i, line in enumerate(["FELLOWPRO AG", "Beispielallee 42", "80331 München", "Germany"]):
        c.drawString(120 * mm, top - (i + 1) * 5.5 * mm, line)

    # --- Barcode panel (2x2 grid) -------------------------------------------
    # Linear codes (Code128/EAN-13) need physical WIDTH to decode after the
    # PDF is rasterised — the barcode-service reads pyzbar pages at 200 DPI —
    # so we lay the four codes out 2x2 instead of a thin 4-up strip.
    panel_top = top - 40 * mm                 # start below the meta + Bill-To blocks
    panel_h = 74 * mm
    panel_y = panel_top - panel_h             # bottom of panel
    c.setFillColorRGB(*LIGHT)
    c.rect(18 * mm, panel_y, width - 36 * mm, panel_h, fill=1, stroke=0)
    c.setFillColorRGB(*TEAL)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(20 * mm, panel_y + panel_h - 7 * mm, "SCANNABLE CODES")

    cell_w = (width - 36 * mm) / 2
    cell_h = (panel_h - 12 * mm) / 2
    grid_top = panel_y + panel_h - 12 * mm
    n = len(BARCODES)
    for i, (name, fmt, text, field) in enumerate(BARCODES):
        col, row = i % 2, i // 2
        cx = 18 * mm + col * cell_w + cell_w / 2
        # If this is a lone item on the last row (odd count), centre it.
        if i == n - 1 and n % 2 == 1 and i % 2 == 0:
            cx = width / 2
        cell_bottom = grid_top - (row + 1) * cell_h
        reader = make_barcode_image(fmt, text)
        iw, ih = reader.getSize()
        aspect = ih / iw
        draw_w = min(cell_w - 16 * mm, 78 * mm)
        draw_h = draw_w * aspect
        if draw_h > cell_h - 9 * mm:
            draw_h = cell_h - 9 * mm
            draw_w = draw_h / aspect
        c.drawImage(reader, cx - draw_w / 2, cell_bottom + 7 * mm,
                    width=draw_w, height=draw_h, mask="auto")
        c.setFillColorRGB(*GREY)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(cx, cell_bottom + 2.5 * mm, f"{name}  →  {field}  ({text})")

    # --- Line items table ----------------------------------------------------
    table_y = panel_y - 12 * mm
    c.setFillColorRGB(*TEAL_DARK)
    c.rect(18 * mm, table_y, width - 36 * mm, 8 * mm, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 9)
    cols = [(22 * mm, "Pos"), (34 * mm, "Description"),
            (120 * mm, "Qty"), (140 * mm, "Unit Price"), (175 * mm, "Amount")]
    for x, head in cols:
        c.drawString(x, table_y + 2.5 * mm, head)

    rows = [
        ("1", "Premium document processing licence", "10", "120.00", "1,200.00"),
        ("2", "OCR add-on module", "2", "350.00", "700.00"),
        ("3", "Onboarding & training (hrs)", "8", "95.00", "760.00"),
    ]
    ry = table_y - 7 * mm
    c.setFont("Helvetica", 9)
    for r in rows:
        c.setFillColorRGB(0.1, 0.12, 0.14)
        for (x, _), val in zip(cols, r):
            c.drawString(x, ry, val)
        ry -= 7 * mm

    # --- Totals --------------------------------------------------------------
    c.setStrokeColorRGB(*GREY)
    c.line(120 * mm, ry, width - 18 * mm, ry)
    ry -= 7 * mm
    for label, val, bold in [("Net total", "2,660.00", False),
                             ("VAT 19%", "505.40", False),
                             ("Gross total  EUR", "3,165.40", True)]:
        c.setFont("Helvetica-Bold" if bold else "Helvetica", 11 if bold else 9)
        c.setFillColorRGB(*TEAL) if bold else c.setFillColorRGB(*GREY)
        c.drawString(120 * mm, ry, label)
        c.setFillColorRGB(0.1, 0.12, 0.14)
        c.drawRightString(width - 18 * mm, ry, val)
        ry -= 7 * mm

    # --- Footer --------------------------------------------------------------
    c.setFillColorRGB(*GREY)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(width / 2, 14 * mm,
                        "This is a DocBits demo invoice for documentation purposes only. "
                        "Barcodes encode the values shown above.")
    c.showPage()
    c.save()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="../fixtures/docbits_demo_barcode_invoice.pdf",
                    help="output PDF path (default: ../fixtures/...)")
    args = ap.parse_args()
    draw_invoice(args.out)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
