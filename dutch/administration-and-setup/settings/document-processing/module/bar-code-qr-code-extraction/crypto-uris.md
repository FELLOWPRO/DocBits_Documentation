# Crypto-betalings-URIs (BIP21 / BIP321)

## Overzicht

Crypto-betalings-URIs zijn de informele maar breed geadopteerde standaard voor het coderen van cryptovaluta-betalingsverzoeken in QR-codes. DocBits herkent zowel **BIP21** (de oorspronkelijke Bitcoin-betalings-URI) als **BIP321** (de gemoderniseerde uitbreiding uit 2024), over de vijf meest voorkomende blockchains: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** en **Litecoin**.

### Functieoverzicht

Een crypto QR-payload is een URI met een schema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), een ontvangeradres en een reeks URL-achtige parameters. DocBits extraheert alle standaard BIP21-parameters (`amount`, `label`, `message`) en de nieuwere BIP321-uitbreidingen (`lightning=` betalingsfallback, `pj=` / `pjos=` payjoin-endpoints). Per BIP21-specificatie kunnen parameters met `req-`-prefix door consumers worden afgewezen als ze niet worden ondersteund — DocBits bewaart ze daarom in een apart veld (`crypto_required_params`) zodat clients zelf kunnen beslissen.

#### Belangrijkste Voordelen

* **Multi-chain-ondersteuning**: Bitcoin, Lightning, Zcash, Ethereum en Litecoin in één extractor.
* **BIP21 + BIP321**: beide versies worden herkend; de versie wordt blootgesteld in de output.
* **Schema is hoofdletterongevoelig**: `BITCOIN:` en `bitcoin:` worden identiek behandeld.

***

### Detectie

- Schema-gebaseerde detectie (hoofdletterongevoelig): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standaard URI-formaat: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Ondersteunde Parameters

**BIP21 basisparameters:**
- `amount` — gevraagd bedrag in de native eenheid
- `label` — leesbaar label van de ontvanger
- `message` — vrije tekst

**BIP321-uitbreidingen:**
- `lightning=<BOLT11>` — Lightning-factuur als fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — payjoin-endpoints
- `req-*` — verplichte parameters (bewaard in `crypto_required_params`)

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `crypto_`:

| Veld | Beschrijving |
|------|--------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` of `litecoin` |
| `crypto_address` | Ontvangeradres |
| `crypto_amount` | Gevraagd bedrag (decimaal) |
| `crypto_currency` | Symbool van de native valuta (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Ontvangerlabel (indien ingesteld) |
| `crypto_message` | Vrije tekst (indien ingesteld) |
| `crypto_lightning_fallback` | BOLT11 Lightning-factuur (uit BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Payjoin-endpoint (uit `pj=` / `pjos=`) |
| `crypto_required_params` | Alle `req-*`-parameters, bewaard voor beslissing client-side |
| `crypto_uri_version` | `bip21` of `bip321` |

### Voorbeeld API-respons

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

### Hoe de Functie In te Schakelen

Parsing van crypto-URIs wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
