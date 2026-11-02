# Crypto Payment URIs (BIP21 / BIP321)

## Overview

Crypto Payment URIs are the informal but widely-adopted standard for encoding cryptocurrency payment requests inside QR codes. DocBits recognises both **BIP21** (the original Bitcoin payment URI) and **BIP321** (the modernised 2024 extension), across the five most common blockchains: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** and **Litecoin**.

### Feature Overview

A crypto QR payload is a URI with a scheme (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), a recipient address and a set of URL-style parameters. DocBits extracts all standard BIP21 parameters (`amount`, `label`, `message`) and the newer BIP321 extensions (`lightning=` payment fallback, `pj=` / `pjos=` payjoin endpoints). Per the BIP21 specification, parameters prefixed with `req-` may be rejected by consumers if unsupported — DocBits therefore keeps them in a separate field (`crypto_required_params`) so clients can decide how to handle them.

#### Key Benefits

* **Multi-chain support**: Bitcoin, Lightning, Zcash, Ethereum and Litecoin in one extractor.
* **BIP21 + BIP321**: both versions are recognised; the version is exposed in the output.
* **Scheme is case-insensitive**: `BITCOIN:` and `bitcoin:` are treated identically.

***

### Detection

- Scheme-based detection (case-insensitive): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standard URI format: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Supported Parameters

**BIP21 core parameters:**
- `amount` — requested amount in the native cryptocurrency unit
- `label` — human-readable label for the recipient
- `message` — free-text message

**BIP321 extensions:**
- `lightning=<BOLT11>` — Lightning invoice fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — payjoin endpoints
- `req-*` — required parameters (preserved in `crypto_required_params`)

### Extracted Fields

All fields use the `crypto_` prefix:

| Field | Description |
|-------|-------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` or `litecoin` |
| `crypto_address` | Recipient address |
| `crypto_amount` | Requested amount (decimal) |
| `crypto_currency` | Native currency symbol (e.g. `BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Recipient label (if set) |
| `crypto_message` | Free-text message (if set) |
| `crypto_lightning_fallback` | BOLT11 Lightning invoice (from BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Payjoin endpoint (from `pj=` / `pjos=`) |
| `crypto_required_params` | Any `req-*` parameters, preserved for client-side decision |
| `crypto_uri_version` | `bip21` or `bip321` |

### Sample API Response

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### How to Enable

Crypto URI parsing is covered by the general **Bar-Code / QR Code Extraction** module toggle — no standard-specific configuration is required.

1. **Navigate to Settings**:
   * From the Dashboard, go to **Settings**.
   * Select **Document Processing** and then choose **Module**.
2. **Enable the Feature**:
   * Scroll down to locate the **Bar-Code / QR Code Extraction** option.
   * Toggle the slider to enable it.

For a full list of Payment QR Code standards, see the [Overview](./README.md) page.
