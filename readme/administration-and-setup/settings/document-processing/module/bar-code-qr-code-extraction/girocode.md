# GiroCode (EPC069-12)

## Overview

**GiroCode** is the SEPA payment QR code defined by the European Payments Council in specification **EPC069-12**. It is the de-facto standard on invoices from German and Austrian banks (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) and is also issued in the Netherlands, Belgium and Finland. DocBits decodes both revisions (**v001** and **v002**) and returns the full SEPA payment payload in the document API response.

### Feature Overview

A GiroCode contains everything needed to initiate a SEPA credit transfer: the beneficiary BIC and IBAN, the beneficiary name, amount, purpose, and either a structured creditor reference or an unstructured remittance text. DocBits normalises the payload so that **amounts written with either `.` or `,` as decimal separator** — a common deviation from the spec by German QR generators — are accepted without error.

#### Key Benefits

* **Broad German / Austrian coverage**: every major retail bank prints GiroCodes on customer invoices.
* **Both revisions supported**: v001 (BIC mandatory) and v002 (BIC optional for EEA payments).
* **Decimal-separator tolerant**: accepts `227.01` and `227,01` interchangeably.

***

### Detection

- Magic prefix: `BCD\n001` (v001) or `BCD\n002` (v002)
- Line-separated structured payload following the EPC069-12 specification
- **v002** makes the BIC optional when the IBAN is inside the Single Euro Payments Area

### Extracted Fields

All fields use the `girocode_` prefix:

| Field | Description |
|-------|-------------|
| `girocode_bic` | Beneficiary BIC (mandatory in v001, optional in v002 for EEA payments) |
| `girocode_creditor_name` | Beneficiary name |
| `girocode_iban` | Beneficiary IBAN |
| `girocode_amount` | Amount (decimal) — both `.` and `,` separators accepted |
| `girocode_currency` | Currency (typically `EUR`) |
| `girocode_purpose` | SEPA purpose code |
| `girocode_structured_reference` | Structured creditor reference (ISO 11649 RF-reference) |
| `girocode_unstructured_remittance` | Free-text remittance information |
| `girocode_version` | `001` or `002` |

### Sample API Response

Real-world example (Dr. Meindl u. Partner invoice):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### How to Enable

GiroCode parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
