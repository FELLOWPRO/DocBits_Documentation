# Barcode Assignment

### Overview

The **Barcode Assignment** setting lets DocBits use **barcodes inside a file to separate it into individual documents**. This is useful when several documents are scanned together into one large PDF and a barcode marks where one document ends and the next begins.

This setting is **disabled by default**.

### What Does It Do?

When this setting is enabled, DocBits looks for barcodes in an incoming multi-page file and uses them to split that file into separate documents at the marked positions. Each resulting document is then processed on its own.

* **Enabled** — DocBits detects barcodes and automatically separates a combined file into individual documents based on them.
* **Disabled** — The file is processed as a single document; barcodes are not used to split it.

{% hint style="info" %}
This is about **splitting and assigning** pages based on barcodes. Reading the data encoded in a barcode (for example for payment QR codes) is handled separately under **Bar-Code / QR Code Extraction**.
{% endhint %}

### Benefits

* **Faster batch scanning**: Scan a whole stack of documents in one pass, separated by barcode sheets, instead of scanning each document individually.
* **Less manual sorting**: DocBits creates the individual documents for you, so no one has to split the PDF by hand.
* **Fewer mistakes**: Documents are separated at exactly the marked positions every time.

### How to Use

1. Go to **Settings**.
2. Select **Document Processing**.
3. Select **Module**.
4. Open the **Document Type** section.
5. Find **Barcode Assignment** and switch the toggle on.

### When to Use This Feature

* **High-volume scanning**: When you scan many documents together and use barcode separator pages between them.
* **Mixed batches**: When a single incoming file contains several different documents that need to be processed separately.
* **Leave it off** if your documents always arrive as separate files — splitting is then not needed.
