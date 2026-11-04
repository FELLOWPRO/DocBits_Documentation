# Krypto-Payment-URIs (BIP21 / BIP321)

## Überblick

Krypto-Payment-URIs sind der inoffizielle, aber weit verbreitete Standard, um Zahlungsanforderungen für Kryptowährungen in QR-Codes zu codieren. DocBits erkennt sowohl **BIP21** (die ursprüngliche Bitcoin-Payment-URI) als auch **BIP321** (die modernisierte Erweiterung von 2024) für die fünf am häufigsten genutzten Blockchains: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** und **Litecoin**.

### Funktions-Überblick

Eine Krypto-QR-Payload ist eine URI mit einem Schema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), einer Empfängeradresse und URL-artigen Parametern. DocBits extrahiert alle Standard-BIP21-Parameter (`amount`, `label`, `message`) sowie die BIP321-Erweiterungen (`lightning=`-Fallback, `pj=` / `pjos=` Payjoin-Endpunkte). Gemäss BIP21-Spezifikation dürfen Parameter mit `req-`-Präfix von Clients abgelehnt werden, wenn sie nicht unterstützt werden — DocBits legt sie deshalb in einem separaten Feld (`crypto_required_params`) ab, damit Clients eigenständig entscheiden können.

#### Hauptvorteile

* **Multi-Chain**: Bitcoin, Lightning, Zcash, Ethereum und Litecoin mit einem Extraktor.
* **BIP21 + BIP321**: Beide Versionen werden erkannt; die Version wird in der Ausgabe mitgeliefert.
* **Schemaerkennung case-insensitive**: `BITCOIN:` und `bitcoin:` werden gleich behandelt.

***

### Erkennung

- Schemabasierte Erkennung (Gross-/Kleinschreibung irrelevant): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standard-URI-Format: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Unterstützte Parameter

**BIP21-Kernparameter:**
- `amount` — angeforderter Betrag in der nativen Kryptowährungseinheit
- `label` — lesbare Empfängerbezeichnung
- `message` — Freitext-Nachricht

**BIP321-Erweiterungen:**
- `lightning=<BOLT11>` — Lightning-Rechnung als Fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — Payjoin-Endpunkte
- `req-*` — verpflichtende Parameter (werden in `crypto_required_params` bewahrt)

### Extrahierte Felder

Alle Felder verwenden das Präfix `crypto_`:

| Feld | Beschreibung |
|------|--------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` oder `litecoin` |
| `crypto_address` | Empfängeradresse |
| `crypto_amount` | Angeforderter Betrag (Dezimal) |
| `crypto_currency` | Native Währung (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Empfängerbezeichnung (falls gesetzt) |
| `crypto_message` | Freitext-Nachricht (falls gesetzt) |
| `crypto_lightning_fallback` | BOLT11-Lightning-Rechnung (aus BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Payjoin-Endpunkt (aus `pj=` / `pjos=`) |
| `crypto_required_params` | Alle `req-*`-Parameter, für Client-Entscheidungen erhalten |
| `crypto_uri_version` | `bip21` oder `bip321` |

### Beispiel einer API-Antwort

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

### So aktivieren Sie die Funktion

Die Krypto-URI-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
