# Barcode Assignment

### Overview

The **Barcode Assignment** setting adds a barcode tool to the **document validation screen**. It reads the barcodes and QR codes found in a document and lets you **assign their values to the document’s fields** — for example, filling a reference, order or delivery-note number from a barcode instead of typing it.

This setting is **disabled by default**.

### What Does It Do?

When this setting is enabled, a small **barcode button** (a QR-code icon) appears in the toolbar while you validate a document. Clicking it shows the barcodes that DocBits found in the document, and you can map each one to a field. The field is then filled with the value read from the barcode.

* **Enabled** — The barcode button is shown on the validation screen. You can read the barcodes in the document and assign their values to fields.
* **Disabled** — The button is hidden and barcode values are not offered for assignment during validation.

{% hint style="info" %}
**This is for reading a barcode/QR value and assigning it to a field during validation.** Automatically extracting structured data from payment codes (such as Swiss QR Bill or GiroCode) — and splitting a multi-page file at barcode separator pages — are handled by a **different** setting: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Benefits

* **Faster, error-free entry**: Take values straight from a barcode instead of reading and typing them by hand.
* **Fewer typos**: A scanned value is exactly what is encoded in the barcode.
* **Stays in control**: You decide which barcode goes into which field during validation.

### How to Use

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Find **Barcode Assignment** and switch the toggle on.
6. Afterwards, while validating a document, click the **barcode button** in the toolbar and assign the detected barcode values to the matching fields.

### When to Use This Feature

* **Documents with barcodes**: When your documents carry barcodes/QR codes whose values belong in specific fields (e.g. order or reference numbers).
* **Manual validation workflows**: When a person reviews documents and wants to fill fields quickly from barcodes.
* **Leave it off** if your documents have no usable barcodes, or if you only need automatic barcode/QR **extraction** — see [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
