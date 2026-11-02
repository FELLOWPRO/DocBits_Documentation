# SPAYD / Short Payment Descriptor (Czech)

## Overview

**SPAYD** (Short Payment Descriptor), also known as **SPD**, is the standard payment QR code defined by the Czech Banking Association. It is printed on virtually every Czech business invoice and is also used in part of Slovakia. DocBits decodes SPAYD payloads and returns the complete payment instruction — including Czech-specific symbols (variable, specific, constant) — in the document API response.

### Feature Overview

A SPAYD payload is a star-separated list of key:value pairs. Values are percent-encoded, so UTF-8 recipient names and messages are preserved. DocBits supports the common `ACC` variant (IBAN plus optional BIC, plus-separated), `ALT-ACC` (alternative IBANs, comma-separated), and preserves any unknown vendor-specific keys in a dedicated `spayd_raw_pairs` field so downstream consumers never lose data.

#### Key Benefits

* **Full Czech payment coverage**: IBAN/BIC plus VS/SS/KS symbols are extracted into named fields.
* **Unicode-safe**: percent-encoded UTF-8 recipient names and messages round-trip cleanly.
* **Forward-compatible**: unknown keys are preserved in `spayd_raw_pairs`.

***

### Detection

- Magic prefix: `SPD*1.0*`
- Payload is a `*`-separated list of `KEY:value` pairs, e.g. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Values are **percent-encoded** (RFC 3986)
- `ACC` may carry `IBAN+BIC` (plus-separated); `ALT-ACC` carries comma-separated alternative IBANs

### Extracted Fields

All fields use the `spayd_` prefix:

| Field | Description |
|-------|-------------|
| `spayd_iban` | Primary IBAN (from `ACC`) |
| `spayd_bic` | BIC (from `ACC`, if present) |
| `spayd_alt_ibans` | List of alternative IBANs (from `ALT-ACC`) |
| `spayd_amount` | Amount (decimal, from `AM`) |
| `spayd_currency` | Currency (from `CC`, typically `CZK`) |
| `spayd_variable_symbol` | Variable symbol (`VS`) — invoice / reference number |
| `spayd_specific_symbol` | Specific symbol (`SS`) |
| `spayd_constant_symbol` | Constant symbol (`KS`) |
| `spayd_recipient_name` | Recipient / beneficiary name (from `RN`) |
| `spayd_due_date` | Due date (from `DT`, `YYYYMMDD`) |
| `spayd_message` | Free-text message (from `MSG`) |
| `spayd_raw_pairs` | Any unknown or vendor-specific `KEY:value` pairs, preserved verbatim |

### Sample API Response

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### How to Enable

SPAYD parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
