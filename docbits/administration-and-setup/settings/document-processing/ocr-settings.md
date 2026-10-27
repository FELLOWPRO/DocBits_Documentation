# OCR Settings

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR & E-Text Explained: Settings, Quality & Header Extraction
{% endembed %}

## Overview

In the **OCR (Optical Character Recognition)** settings, you can configure how OCR is applied during document processing. This includes specifying the minimum required quality, choosing whether to use embedded text (e-text), selecting the OCR version, and more. This page provides a detailed explanation of all available settings.

## How to Access OCR Settings

To access the OCR settings:

*   Navigate to: **Settings** → **Document Processing** → **OCR Settings**

    <figure><img src="../../../.gitbook/assets/settings_ocr.png" alt="Settings Document Processing list with an arrow pointing to OCR Settings"><figcaption></figcaption></figure>

## OCR Quality

In this section, you can set the minimum document quality required for OCR processing by adjusting the quality slider. Move the slider left or right to decrease or increase the quality threshold, respectively.

If a document does not meet the defined quality level, DocBits provides three options for handling it:

* **Run Anyway**\
  The document will be processed regardless of its quality.
* **Run Again After Confirmation**\
  **DocBits** will pause and prompt you to confirm whether to proceed with processing.
* **Throw Error**\
  Document processing will stop entirely, and an error message will be displayed, indicating that the document did not meet the required quality threshold.

<figure><img src="../../../.gitbook/assets/ocr_settings_1.png" alt="OCR Quality slider set to 75 percent with the low-quality handling dropdown showing Run anyway, Run again after confirmation and Throw error"><figcaption></figcaption></figure>

## General OCR Settings

* **Use E-Text if Available**\
  When enabled, **DocBits** will use embedded electronic text (e.g., from PDFs) instead of performing OCR. This improves both speed and accuracy, as the text is extracted directly without requiring OCR processing.
* **Use DESKEW if Available**\
  This option automatically corrects the alignment of scanned documents. Straightening skewed images helps improve OCR accuracy.
*   **AI OCR Version**\
    Allows you to select a specific version of the AI-based OCR engine.\
    This can be useful if:

    * You are not achieving the desired results with the currently selected version.
    * You are troubleshooting issues related to OCR performance or accuracy.

    <figure><img src="../../../.gitbook/assets/ocr_settings_2.png" alt="General OCR settings with the AI OCR Version dropdown listing versions 1.2, 2.0 and 2.1"><figcaption></figcaption></figure>

## OCR Settings for Tables

* **Use AI Data for Tables if Available**\
  When enabled, DocBits will use OCR data for tables instead of embedded electronic text (E-Text) — even if the **Use E-Text if Available** setting is turned on.

## OCR Settings for Header Fields

* **Use Rules Extraction**\
  DocBits will apply your predefined extraction rules for identifying header fields.
* **Use AI Extraction**\
  DocBits will use AI to automatically detect and extract header fields.

**Execution Order:**\
If both options are enabled, **DocBits** will perform extraction in the following order:\
**Rules Extraction → AI Extraction**\
\
<mark style="color:red;">**Note**</mark>: For best results and consistent behavior, enable both options. This allows **DocBits** to use both rule-based and AI-based methods in combination during header extraction.

## Extraction Insights

At the bottom of the OCR settings page, the **Extraction Insights** section contains one switch, **Show extraction insights panel**. It is off by default and applies to the whole organisation.

When you turn it on, the field validation page gets an extra icon (tooltip **Show extraction insights**) that opens the **Extraction insights** panel. The panel explains how each field of the open document was extracted, so users can see why DocBits chose a value:

* **Extraction method** — a label on every field shows how the value was found: **Trained rule**, **AI extracted**, **Calculated** (computed from the supplier lookup) or **From e-invoice** (read directly from the XML of an electronic document).
* **Confidence** — each field shows a confidence level from **Low confidence** and **Worth checking** up to **Likely correct**, **Confident** and **Highly confident**. Use **Sort by → Needs attention** to list the fields that deserve a second look first.
* **Technical details** — **Show technical details** reveals the matched rule, its score and the components behind it (**Label match**, **Context pattern**, **Coordinates**, **Final confidence**), the training history and the competing candidate rules.
* **Filter and sort** — type in **Filter fields…** to narrow the list, and sort by document order, field name, needs attention or most confident.
* **Refresh** — reloads the insights of the current document.
* **Clean up duplicates** — appears when fields have more than one rule. After you confirm, DocBits keeps the winning rule of each field and deletes the duplicates. An administrator can restore deleted rules.

If a document has no extraction data yet, the panel shows **No extraction data available**.

{% hint style="info" %}
The panel only explains an extraction that already happened. Turning it on or off does not change how documents are processed.
{% endhint %}

The limit for the number of pages that are OCRed is not part of this page. It is the **Pages to process** setting in [Classification and Extraction](classification-and-extraction/README.md#document-processing).
