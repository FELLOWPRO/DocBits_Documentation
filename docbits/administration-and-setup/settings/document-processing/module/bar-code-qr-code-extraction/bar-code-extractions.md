# Bar Code Extractions

## Overview

This feature enables automatic detection of barcodes on documents. When activated, all supported barcode types are scanned and extracted during processing.

## How to Enable Bar-Code Extraction

To enable the Bar-Code Extraction feature, follow these steps:

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code Extraction** option.
   * Toggle the slider to enable Bar-Code Extraction.\\

## **Additional Settings**

### **Barcode Assignment**

#### **Purpose:** Allows validators to manually assign an extracted barcode value to a specific document field during field validation.

#### How to Enable **Barcode Assignment**

To enable the **Barcode Assignment** feature, follow these steps:

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Barcode Assignment** option.
   * Toggle the slider to enable **Barcode Assignment**.\\

#### **How it works:**

* Enables an “Assign Barcode” option in the field validation screen.\\
* Users can select a detected barcode value and map it to a document field like PO Number or Invoice Number.\\

### Split of Document by Barcode / QR Code

**Purpose:** Automatically splits multi-page documents into separate documents based on the presence of specific barcodes or QR codes.

#### How to Enable Split of Document by Barcode / QR Code

To enable the **Split of Document by Barcode / QR Code feature**, follow these steps:

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Classification and Extraction**.
2. **Enable the Feature**:
   * Locate the **Document Splitting** option.
   * For **Split**, select **Split by Barcode / QR Code**.
   * For **Barcode Type**, choose one or more supported barcode types from the list.
   * For **Barcode Pattern**, define the pattern that should trigger a split. You can use a **regular expression** (regex) to match dynamic barcode values.

**How it works:**

* You select the barcode types that should trigger a split.
* You define a pattern the barcode must match — this can be a fixed string or a regex (e.g., `^INV\d{6}$` to match barcodes like `INV123456`).
* During document processing, each time a page contains a matching barcode, a **new document is created** starting from that page.

### Supported Code Types

See the [Overview Page](./) for the full list of supported barcode and QR code formats.
