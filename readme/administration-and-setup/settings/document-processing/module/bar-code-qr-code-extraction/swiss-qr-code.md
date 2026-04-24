# Swiss QR Bill

## Overview

The **Swiss QR Bill** is the national payment-slip standard that has replaced the orange and red Swiss payment slips since 30 June 2020. Every domestic Swiss invoice — whether from a utility, an insurer, or a business partner — now carries a Swiss QR Bill QR code. DocBits decodes these codes automatically and makes every payment field available through the API response.

### Feature Overview

Swiss QR Bills follow the **ISO 20022** payment standard and are issued in two versions: **v1.0** (early roll-out) and **v2.0** (current). The DocBits extractor supports both. Recognised payloads decode into a full set of payment fields — creditor, debtor, IBAN / QR-IBAN, amount, currency, reference type (QRR, SCOR or NON), structured and unstructured messages, and alternative payment schemes.

<figure><img src="../../../../../.gitbook/assets/qr_code_extraction_example.png" alt="QR Code Extraction Example"><figcaption></figcaption></figure>

#### Key Benefits

* **Zero manual entry** for Swiss invoices: IBAN, amount, reference and creditor flow directly into the document.
* **Both versions covered**: v1.0 and v2.0 are detected automatically.
* **Reference types preserved**: QRR, SCOR and NON are retained exactly as printed, which keeps downstream reconciliation working.

***

### Detection

- Magic prefix: `SPC\n0100` (v1.0) or `SPC\n0200` (v2.0)
- ISO 20022 compliant
- The parser also surfaces `alt-schemes` (alternative payment procedures) when present

### Extracted Fields

All fields use the `swissqr_` prefix:

| Field | Description |
|-------|-------------|
| `swissqr_account` | IBAN or QR-IBAN of the creditor |
| `swissqr_creditor_name` | Creditor name |
| `swissqr_creditor_street` | Creditor street / address line |
| `swissqr_creditor_city` | Creditor city |
| `swissqr_creditor_postal_code` | Creditor postal code |
| `swissqr_creditor_country` | Creditor country (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Debtor name (if printed) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Debtor address |
| `swissqr_amount` | Amount (decimal) |
| `swissqr_currency` | Currency (ISO 4217) — typically `CHF` or `EUR` |
| `swissqr_reference` | Structured reference (QRR or SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` or `NON` |
| `swissqr_unstructured_message` | Free-text remittance |
| `swissqr_bill_information` | Structured bill information (S1 / Swico) |
| `swissqr_alt_schemes` | Alternative procedures (if present) |

### Sample API Response

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### How to Enable

Swiss QR Bill parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

<figure><img src="../../../../../.gitbook/assets/barcode_qr_code_extraction_toggle.png" alt="Barcode and QR Code Extraction Toggle"><figcaption></figcaption></figure>

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
