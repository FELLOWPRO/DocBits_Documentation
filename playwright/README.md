# DocBits Documentation Screenshots — Playwright Toolkit

Reusable tooling for producing **documentation screenshots** of DocBits features
(and the demo fixtures they need). Built first for the *Barcode Assignment*
feature; intended to grow as more doc pages need real UI captures.

## Layout

```
playwright/
├── scripts/
│   ├── generate_barcode_invoice.py   # builds a demo invoice PDF with real barcodes
│   └── upload_document.py            # uploads a file to a DocBits env (REST + API key)
├── fixtures/                         # generated demo documents (PDFs)
├── screenshots/                      # raw captures
└── output/                           # rendered previews
```

## Why these tools exist (lessons learned)

Capturing a feature like Barcode Assignment end-to-end hits three non-obvious walls:

1. **The browser uploader can’t be fed a file programmatically.** The dashboard
   uses a Quasar `QFile`; injecting a `File` via `DataTransfer` + a `change` event
   shows the filename in the dialog but does **not** result in a server upload.
   → Upload via the REST endpoint instead (see `upload_document.py`).

2. **The HTTP MCP server has no local filesystem access**, so
   `upload_document(file_path=…)` fails with *File not found*. Use
   `file_content_base64`, or the REST endpoint with an API key.

3. **`claude-in-chrome` screenshots are not written to the host filesystem**, so
   they can’t become doc assets directly. Use the **Playwright MCP** (its
   `browser_take_screenshot` saves to a real path), and carry the existing login
   over by copying `localStorage` from the authenticated session.

## Barcode set & extraction

`generate_barcode_invoice.py` renders four barcode types with `zxingcpp` — the
**same** library the DocBits `barcode-service` uses to *decode* them, so a
round-trip read is guaranteed when the symbols are large enough:

| Type        | Encodes          | Example value     |
|-------------|------------------|-------------------|
| QR code     | Purchase Order   | `PO-2026-00847`   |
| Code 128    | Invoice Number   | `INV-2026-1185`   |
| EAN-13      | Supplier GLN     | `4006381333931`   |

For the values to appear in the Barcode Assignment dialog, the org’s
`BARCODE_EXTRACTION_TYPES` preference must include those types, e.g.
`QRCODE,CODE128,EAN13`, and barcode extraction must run during processing.

> ⚠️ **Do NOT add `DATAMATRIX` (or other non-ZBar types) to `BARCODE_EXTRACTION_TYPES` on dev.**
> The barcode-service's *fast* extractor uses pyzbar/ZBar, which raises
> `'DATAMATRIX' is not a valid ZBarSymbol enum value` and **fails the whole
> extraction** (error E015, recoverable → the document loops forever in
> `running`). Stick to ZBar-supported types (QRCODE, CODE128, CODE39, EAN13,
> EAN8, UPCA, UPCE). DataMatrix/PDF417/Aztec are only handled by the separate
> zxing extractor path.

## Typical workflow

```bash
PY=python3   # an interpreter with: zxingcpp, reportlab, pillow, requests, pymupdf

# 1. Generate the demo invoice
$PY scripts/generate_barcode_invoice.py --out fixtures/docbits_demo_barcode_invoice.pdf

# 2. (optional) verify the barcodes decode at the DPIs the service uses
$PY - <<'PYCODE'
import fitz, zxingcpp; from PIL import Image
doc=fitz.open("fixtures/docbits_demo_barcode_invoice.pdf")
for dpi in (200,300):
    pix=doc[0].get_pixmap(dpi=dpi); img=Image.frombytes("RGB",(pix.width,pix.height),pix.samples)
    print(dpi, sorted(r.format.name for r in zxingcpp.read_barcodes(img)))
PYCODE

# 3. Upload to dev (API key NOT committed — pass it explicitly)
DOCBITS_API_KEY=… $PY scripts/upload_document.py \
    --file fixtures/docbits_demo_barcode_invoice.pdf \
    --org-id <ORG_ID> --doc-type INVOICE --wait
```

Then drive the UI with the Playwright MCP (auth carried over from the logged-in
session) to open `/field_validation_v1/<doc_id>`, click the barcode button
(`[data-test="validation-barcode-button"]`), open the dialog
(`[data-test="barcode-assignment-dialog"]`) and screenshot. Move the resulting
PNGs into `readme/.gitbook/assets/`.

## Notes

- **API keys are secrets** — never hard-code them here and never pass them as CLI
  args (they leak via shell history / process listings). The upload helper reads
  the key only from the `DOCBITS_API_KEY` env var, and targets dev/stage only.
- dev’s barcode-extraction Celery worker can back up; a document then sits in
  `running` until the queue drains. Check `BARCODE_EXTRACTION_TYPES` and the
  pending-tasks queue if the dialog stays empty.
- `data-test` hooks added for this feature: `validation-barcode-button`,
  `barcode-assignment-dialog`, `barcode-assignment-row`, `barcode-field-select`.
