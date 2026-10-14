# ZATCA Fatoora (Saudi Arabia)

## Overview

**ZATCA Fatoora** is the e-invoicing QR code mandated by the Zakat, Tax and Customs Authority of Saudi Arabia. Since **December 2021 (Phase 1)** every B2C invoice issued in the Kingdom must carry a Fatoora QR with the five core invoice fields, and since **January 2023 (Phase 2)** the QR additionally carries a cryptographic signature envelope. DocBits decodes both phases and returns every Phase 1 payment field as a named property in the document API response.

### Feature Overview

ZATCA Fatoora uses a **binary TLV** format (1-byte tag ID, 1-byte length, value) wrapped in **Base64**. All text is UTF-8, so Arabic seller names decode cleanly. The extractor exposes Phase 1 tags 1–5 as structured fields and — when present — Phase 2 tags 6–9 as Base64 strings for downstream compliance tooling. **Signature and hash verification are intentionally out of scope**; they belong to dedicated e-invoicing compliance stacks.

#### Key Benefits

* **Mandatory compliance coverage**: every Saudi B2C invoice is parsed.
* **Arabic support**: UTF-8 seller names round-trip without re-encoding.
* **Phase 1 and Phase 2**: both phases are detected; the phase is exposed in the output.
* **Phase 2 envelope preserved**: hash, signature, public key and certificate signature are retained as Base64 strings for compliance tooling.

***

### Detection

- Base64-wrapped binary TLV (tags 1–9, 1-byte tag ID + 1-byte length + value)
- Phase detection: `zatca_phase = 1` when only tags 1–5 are present; `zatca_phase = 2` when tags 6–9 are also present

### TLV Tag Layout

| Tag | Phase | Content |
|-----|-------|---------|
| 1 | 1 | Seller name (UTF-8, supports Arabic) |
| 2 | 1 | VAT registration number |
| 3 | 1 | Invoice timestamp (ISO 8601) |
| 4 | 1 | Invoice total |
| 5 | 1 | VAT total |
| 6 | 2 | XML invoice hash (Base64) |
| 7 | 2 | Digital signature (Base64) |
| 8 | 2 | Public key (Base64) |
| 9 | 2 | Certificate signature (Base64) |

### Extracted Fields

All fields use the `zatca_` prefix:

| Field | Description |
|-------|-------------|
| `zatca_seller_name` | Seller name (UTF-8) |
| `zatca_vat_number` | VAT registration number |
| `zatca_invoice_timestamp` | Invoice date/time |
| `zatca_invoice_total` | Invoice total (decimal) |
| `zatca_vat_total` | VAT total (decimal) |
| `zatca_phase` | `1` (Phase 1) or `2` (Phase 2) |
| `zatca_invoice_hash` | XML invoice hash — Phase 2 only, Base64 |
| `zatca_signature` | Digital signature — Phase 2 only, Base64 |
| `zatca_public_key` | Public key — Phase 2 only, Base64 |
| `zatca_certificate_signature` | Certificate signature — Phase 2 only, Base64 |

{% hint style="info" %}
**Out of scope**: DocBits does not verify the cryptographic signature, hash or certificate chain. That verification is a dedicated compliance concern and should be handled by a ZATCA-certified e-invoicing stack.
{% endhint %}

### Sample API Response (Phase 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### How to Enable

ZATCA Fatoora parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
