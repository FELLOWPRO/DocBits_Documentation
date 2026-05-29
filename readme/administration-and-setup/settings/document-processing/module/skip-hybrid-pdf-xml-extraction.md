# Skip Hybrid PDF XML Extraction

### Overview

The **Skip Hybrid PDF XML Extraction** setting controls how DocBits handles **hybrid PDFs** — PDF invoices that carry an embedded structured e-invoice (ZUGFeRD / Factur-X). It decides whether the **structured XML inside the PDF** is the leading document for automated processing, or whether the **PDF itself** is processed via OCR as the primary document.

This setting is especially relevant for **US customers**. Unlike the EU/DE, the United States has no general B2B e-invoicing mandate, so US organizations typically want the PDF treated as the primary, human-readable invoice — even when a counterpart sends a ZUGFeRD/Factur-X file with embedded XML.

### What Does It Do?

A ZUGFeRD/Factur-X file is a single PDF that also contains a machine-readable XML invoice. By default DocBits detects that embedded XML and uses it as the leading source for extraction (the structured-electronic path).

* **Disabled (default)** — DocBits detects the embedded e-invoice XML and processes the document on the **structured electronic-document path**. The XML is the leading invoice. This is the legally correct behavior for EU/DE, where a structured e-invoice is the relevant invoice and the PDF is only a visualization / reading copy.
* **Enabled** — DocBits **ignores the embedded XML** and routes the document to the **PDF processor (OCR)**. The PDF becomes the primary processing document. This is the typical choice for **US organizations** that want PDF-first processing.

{% hint style="info" %}
This setting only affects **hybrid PDFs** (ZUGFeRD / Factur-X = a `.pdf` with embedded XML). A pure XRechnung / EDI file uploaded as `.xml` is always processed on the structured electronic-document path — there is no PDF that could become the primary document.
{% endhint %}

### Audit & Compliance — the original is always preserved

Enabling this setting does **not** discard the e-invoice. The original artifact is always retained:

* The original ZUGFeRD/Factur-X **PDF — including its embedded XML — remains stored** and downloadable. Nothing is deleted from the document’s stored copy.
* Processing only changes **which content drives extraction** (PDF/OCR vs. embedded XML), not what is archived.

So a US organization can process the PDF as primary while the structured e-invoice stays available for audit.

{% hint style="warning" %}
For EU/DE organizations, leave this setting **disabled**. Under the 2025 e-invoicing rules a structured e-invoice (ZUGFeRD/Factur-X, XRechnung) is the legally relevant invoice; a plain PDF is only a reading copy. Processing the PDF as primary instead of the structured data is not appropriate where a valid e-invoice is present.
{% endhint %}

### How to Use

1. **Open the setting**:
   * Go to **Settings**.
   * Select **Document Processing**.
   * Select **Module**.
   * Open the **Document Type** section.
   * Find **Skip Hybrid PDF XML Extraction** and toggle the slider.
2. **Choose the mode**:
   * **US / PDF-first organizations** → enable the toggle so ZUGFeRD/Factur-X PDFs are processed via OCR as the primary document.
   * **EU/DE organizations** → keep the toggle disabled so the structured e-invoice remains the leading document.
3. **Verify**:
   * Upload a ZUGFeRD/Factur-X PDF and check the document’s processing result — with the toggle enabled it is handled as a regular PDF (OCR); with it disabled the embedded e-invoice data is extracted.

### When to Use This Feature

* **US customers / no e-invoice mandate**: enable it so the familiar PDF is the primary processing document while the embedded e-invoice stays archived.
* **Mixed/PDF-first workflows**: enable it where downstream processes, validation, or review rely on the PDF layout rather than the XML.
* **EU/DE compliance**: leave it disabled so structured e-invoice data drives processing, as required.
