# EMVCo MPM (Merchant-Presented QR)

## Overview

**EMVCo MPM** (Merchant-Presented Mode) is the global QR code specification maintained by EMVCo — the same body behind chip-card and contactless payment standards. A single TLV (Tag-Length-Value) envelope is shared across more than a dozen national instant-payment schemes, so one parser unlocks **Pix** (Brazil), **UPI** (India), **PayNow** (Singapore), **PromptPay** (Thailand), **QRIS** (Indonesia), **QR Ph** (Philippines), **VietQR** (Vietnam), **FPS** (Hong Kong), **DuitNow** (Malaysia), **NETS** (Singapore) and many more.

### Feature Overview

Every EMVCo MPM payload shares the same wrapper: it begins with `000201` (Payload Format Indicator = 01) and ends with `6304<CRC>` where `<CRC>` is a 4-hex CRC16-CCITT-FALSE checksum. Inside, TLV-encoded tags 26–51 carry **Merchant Account Info** templates identified by a **GUI sub-tag** — that GUI tag is how DocBits detects which national scheme the QR belongs to. The CRC is validated and the result is exposed as a boolean so merchants can detect tampered or damaged QR codes.

#### Key Benefits

* **One extractor, many schemes**: a single generic TLV parser handles the whole EMVCo MPM family.
* **National schemes identified**: the output includes a named scheme (e.g. `pix`, `upi`, `paynow`) so downstream logic can branch cleanly.
* **CRC validity exposed**: `emvmpm_crc16_valid` surfaces tampered or corrupt QR codes.
* **Currency normalisation**: ISO 4217 numeric currency codes are automatically mapped to alpha-3 (20+ currencies; unmapped numeric codes pass through untouched).

***

### Detection

- Magic shape: starts with `000201` and ends with `6304<4-hex CRC16-CCITT-FALSE>`
- Generic TLV (Tag-Length-Value) decoder walks every tag
- National schemes are identified by the **GUI sub-tag** inside the Merchant Account Info templates (tags 26–51)

### Recognised National Schemes

| GUI sub-tag | Scheme | Country |
|-------------|--------|---------|
| `br.gov.bcb.pix` | **Pix** | Brazil |
| `UPI` | **UPI** | India |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapore |
| `SG.COM.NETS` | **NETS** | Singapore |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonesia |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Philippines |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Thailand |
| `A000000727` | **VietQR** | Vietnam |

Unrecognised GUI / AID values still parse — the extractor falls back to the generic EMVCo MPM field set.

### Extracted Fields

All fields use the `emvmpm_` prefix:

| Field | Description |
|-------|-------------|
| `emvmpm_scheme` | Detected national scheme (e.g. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) or `generic` |
| `emvmpm_merchant_name` | Merchant name (tag 59) |
| `emvmpm_merchant_city` | Merchant city (tag 60) |
| `emvmpm_country_code` | Country code ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Transaction amount (decimal, tag 54) |
| `emvmpm_currency` | Currency alpha-3 (converted from the tag-53 numeric code) |
| `emvmpm_additional_data` | Nested object: bill number, reference label, terminal label, purpose of transaction (tag 62 sub-tags) |
| `emvmpm_crc16_valid` | Boolean — `true` if the CRC16 checksum matches |

### Sample API Response (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### How to Enable

EMVCo MPM parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
