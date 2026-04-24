# Bar-Code / QR Code Extraction

## **Overview**

This feature enables automatic extraction of information from **both barcodes and QR codes** embedded in documents. It is an all-or-nothing setting — enabling it activates extraction for both types.

## How to Enable Bar-Code / QR Code Extraction

To enable the Bar-Code / QR Code Extraction feature, follow these steps:

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable Bar-Code / QR Code Extraction.

## **Supported Code Types**

DocBits supports extraction of the following code types:

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Payment QR Code Standards

Beyond generic QR decoding, DocBits recognises **seven distinct Payment QR Code standards** and auto-extracts their payment fields into the document API response. Customers no longer need to decode these QR strings manually — every standard comes with its own field prefix (e.g. `swissqr_*`, `girocode_*`) so values flow straight into matching, validation, and export.

| # | Standard | Region | Field prefix | Typical use |
|---|----------|--------|--------------|-------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Switzerland | `swissqr_*` | Every Swiss invoice since 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | SEPA payments |
| 3 | [SPAYD / SPD](spayd.md) | CZ, partially SK | `spayd_*` | Czech Banking Association standard |
| 4 | [PagoPA](pagopa.md) | IT (public admin) | `pagopa_*` | Mandatory on Italian PA invoices |
| 5 | [Crypto Payment URIs](crypto-uris.md) | Global crypto | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK + more | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Saudi Arabia | `zatca_*` | Mandatory on every KSA invoice |

**Detection is automatic.** Each decoded QR string is inspected for its magic prefix (e.g. `SPC\n0200` for Swiss QR Bill v2.0, `PAGOPA|002|` for PagoPA) and only recognised standards are parsed into structured fields.

### **Related Pages**

[Barcode Extraction Details](bar-code-extractions.md)
