# Barcode Assignment

### Overview

The **Barcode Assignment** setting adds a barcode tool to the **document validation screen**. It reads the barcodes and QR codes DocBits found in a document and lets you **assign their values to the document’s fields** — for example, filling a purchase-order, reference or delivery-note number from a barcode instead of typing it.

This setting is **disabled by default**.

### What You Get When You Enable It

Once the setting is on, a new **barcode button** (a QR-code icon) appears in the toolbar on the right-hand side of the **validation screen** (`/field_validation_v1/…`). This is the entry point to the whole feature — without the setting, the icon is hidden.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="The barcode (QR-code) icon in the validation toolbar"><figcaption><p>When the setting is enabled, the barcode icon appears in the validation toolbar.</p></figcaption></figure>

Here is the icon in context on the validation screen, next to the document being reviewed:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Validation screen with the barcode icon available"><figcaption><p>The validation screen — the barcode icon (highlighted, right toolbar) is only shown when Barcode Assignment is enabled.</p></figcaption></figure>

### How Barcodes Are Read

DocBits detects the barcodes during document processing and offers their decoded values for assignment. A single document can carry several barcode types — for instance a **QR code**, a **Code 128** and an **EAN-13** — each encoding a different value such as a purchase order, an invoice number or a supplier GLN.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Demo invoice carrying several barcode types"><figcaption><p>Example DocBits demo invoice carrying three barcode types (QR code → purchase order, Code 128 → invoice number, EAN-13 → supplier GLN), each encoding a value you can map to a field.</p></figcaption></figure>

{% hint style="info" %}
Which barcode types are detected is controlled by the **Bar-Code / QR Code Extraction** setting (`Barcode Extraction Types`). If the dialog shows *“no barcodes extracted found”*, make sure barcode extraction is enabled and that the expected types (e.g. `QRCODE`, `CODE128`, `EAN13`) are selected. See [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Using the Barcode Assignment Dialog

1. Open a document on the **validation screen**.
2. Click the **barcode icon** in the right-hand toolbar.
3. The **Barcode Assignment** dialog lists every barcode DocBits detected in the document, shown as `Barcode <n> : <value>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Barcode Assignment dialog listing the detected barcodes"><figcaption><p>The Barcode Assignment dialog lists each detected barcode with a dropdown to choose the target field.</p></figcaption></figure>

4. For each barcode, open its dropdown and pick the field the value should go into.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Choosing the target field for a barcode"><figcaption><p>Each barcode can be mapped to any document field — e.g. Purchase Order, Invoice number, Supplier ID.</p></figcaption></figure>

5. As soon as you select a field, that field is filled with the barcode’s value.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Barcode mapped to the Purchase Order field"><figcaption><p>After selecting a field (here Purchase Order), the field is populated with the barcode value.</p></figcaption></figure>

### How to Enable

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Find **Barcode Assignment** and switch the toggle on.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Barcode Assignment toggle"><figcaption><p>The Barcode Assignment toggle in Settings → Document Processing → Module.</p></figcaption></figure>

### Benefits

* **Faster, error-free entry**: Take values straight from a barcode instead of reading and typing them by hand.
* **Fewer typos**: A scanned value is exactly what is encoded in the barcode.
* **Stays in control**: You decide which barcode goes into which field during validation.

### When to Use This Feature

* **Documents with barcodes**: When your documents carry barcodes/QR codes whose values belong in specific fields (e.g. order or reference numbers).
* **Manual validation workflows**: When a person reviews documents and wants to fill fields quickly from barcodes.
* **Leave it off** if your documents have no usable barcodes, or if you only need automatic barcode/QR **extraction** — see [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**This feature is for reading a barcode/QR value and assigning it to a field during validation.** Automatically extracting structured data from payment codes (such as Swiss QR Bill or GiroCode) — and splitting a multi-page file at barcode separator pages — are handled by a **different** setting: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
