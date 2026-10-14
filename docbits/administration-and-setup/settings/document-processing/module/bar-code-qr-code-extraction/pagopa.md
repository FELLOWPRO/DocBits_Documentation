# PagoPA

## Overview

**PagoPA** is the payment QR standard of the Italian public administration. Every invoice issued by an Italian public-administration body (municipalities, universities, healthcare, tax authorities) carries a PagoPA QR code. DocBits decodes the payload and returns all four required payment fields in the document API response.

### Feature Overview

PagoPA payloads are compact and strictly structured: exactly **five pipe-separated fields** on a single line. Amounts are encoded in **cents** (integer) and automatically converted to a euro decimal by the extractor. The leading zeros of the `codice_avviso` (18-digit payment notice) are preserved — they must never be parsed as integer because the notice is a fixed-width identifier.

#### Key Benefits

* **Mandatory coverage** for Italian PA invoices: `codice_avviso` and creditor fiscal code are extracted into named fields.
* **Safe numeric handling**: 18-digit `codice_avviso` retains leading zeros; amount in cents is also exposed as a float euro value.

***

### Detection

- Magic prefix: `PAGOPA|002|`
- Exactly **5 pipe-separated fields** after the prefix: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **EUR-only** — no other currency is valid under the specification

### Extracted Fields

All fields use the `pagopa_` prefix:

| Field | Description |
|-------|-------------|
| `pagopa_codice_avviso` | 18-digit payment notice number — leading zeros preserved (string) |
| `pagopa_fiscal_code_creditor` | 11-digit creditor fiscal code (string) |
| `pagopa_amount_cents` | Amount in cents (integer) |
| `pagopa_amount` | Amount in euro (decimal, derived from `pagopa_amount_cents`) |
| `pagopa_auth` | Optional auth/version indicator from the payload |

### Sample API Response

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### How to Enable

PagoPA parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
