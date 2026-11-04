# ZUGFeRD + Swiss QR Code Field Mapping

## Overview

When processing PDF invoices that contain both ZUGFeRD XML data and a Swiss QR Code, DocBits extracts data from both sources and intelligently merges them.

## How It Works

1. **ZUGFeRD XML Extraction** - DocBits first extracts fields from the embedded ZUGFeRD XML
2. **Swiss QR Code Detection** - The barcode service detects and parses Swiss QR codes
3. **Smart Merge** - Empty fields are filled from Swiss QR data (fields with values are preserved)
4. **Audit Trail** - Full QR code data is stored in `qr_code_data` for verification

## Field Mapping Table

### Swiss QR Code → DocBits Field Mapping

| Swiss QR Field | DocBits Field | Description |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | Creditor's IBAN (e.g., CH9300762011...) |
| Amount | `total_amount` | Payment amount (e.g., 1234.56) |
| Currency | `currency` | Currency code (CHF or EUR) |
| Reference | `payment_reference` / `esr_reference` | QR reference or ESR number |
| Creditor.Name | `supplier_name` | Supplier company name |
| Creditor.AddressLine1 | `supplier_address` | Street address |
| Creditor.PostalCode | `supplier_plz` | Postal/ZIP code |
| Creditor.City | `supplier_city` | City name |
| Creditor.Country | `supplier_country` | Country code (CH) |
| Debtor.Name | `company_name` | Recipient company name |
| Debtor.AddressLine1 | `company_street` | Recipient street address |
| Debtor.PostalCode | `company_plz` | Recipient postal code |
| Debtor.City | `company_city` | Recipient city |

## Example: Sample Invoice Processing

### Input Document

*   **PDF**: Invoice with embedded ZUGFeRD 1.0 XML + Swiss QR Code barcode

### Swiss QR Code Data Extracted

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Field Extraction Results

| Field | Value | Source | Method |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Extraction Methods

| Method Code | Description |
| :--- | :--- |
| **ED** | Electronic Document (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Swiss QR Code barcode extraction |
| **OCR** | Optical Character Recognition |
| **ML** | Machine Learning extraction |

## Merge Priority

1.  **ZUGFeRD XML** has highest priority (structured, reliable data)
2.  **Swiss QR Code** fills empty fields (guaranteed accurate for payment data)
3.  **OCR/ML** used for fields not in electronic sources

## Supported Swiss QR Code Versions

*   Swiss QR Bill format (ISO 20022)
*   QR-IBAN format (starts with 30, 31)
*   Standard IBAN format
*   With/without structured reference (QRR, SCOR)

## Version Requirement

This feature requires **api version 10.95.6** and **barcode version 1.0.5** or higher.

### Component Versions (Environment)

| Component | Version | Description |
| :--- | :--- | :--- |
| `api` | 10.95.6 | Core API with ZUGFeRD 1.0 extraction support |
| `barcode` | 1.0.5 | Swiss QR Code detection and parsing |
| `Auth` | 1.48.8 | Authentication service |

