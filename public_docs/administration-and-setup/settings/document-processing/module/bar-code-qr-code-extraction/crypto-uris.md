# URI di pagamento crypto (BIP21 / BIP321)

## Panoramica

Gli URI di pagamento crypto sono lo standard informale ma ampiamente adottato per codificare richieste di pagamento in criptovaluta all'interno di QR code. DocBits riconosce sia **BIP21** (l'URI originale di pagamento Bitcoin) sia **BIP321** (l'estensione modernizzata del 2024), sulle cinque blockchain più diffuse: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** e **Litecoin**.

### Panoramica della funzione

Un payload QR crypto è un URI con uno schema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), un indirizzo del destinatario e un insieme di parametri in stile URL. DocBits estrae tutti i parametri BIP21 standard (`amount`, `label`, `message`) e le estensioni più recenti BIP321 (`lightning=` fallback, `pj=` / `pjos=` payjoin). Secondo la specifica BIP21, i parametri con prefisso `req-` possono essere rifiutati dai client se non supportati — DocBits li mantiene quindi in un campo separato (`crypto_required_params`) affinché i client decidano come gestirli.

#### Vantaggi principali

* **Multi-chain**: Bitcoin, Lightning, Zcash, Ethereum e Litecoin con un solo estrattore.
* **BIP21 + BIP321**: entrambe le versioni sono riconosciute; la versione è esposta nell'output.
* **Schema case-insensitive**: `BITCOIN:` e `bitcoin:` sono trattati in modo identico.

***

### Rilevazione

- Rilevazione basata sullo schema (case-insensitive): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Formato URI standard: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Parametri supportati

**Parametri base BIP21:**
- `amount` — importo richiesto nell'unità nativa
- `label` — etichetta leggibile del destinatario
- `message` — testo libero

**Estensioni BIP321:**
- `lightning=<BOLT11>` — fattura Lightning come fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — endpoint payjoin
- `req-*` — parametri obbligatori (preservati in `crypto_required_params`)

### Campi estratti

Tutti i campi utilizzano il prefisso `crypto_`:

| Campo | Descrizione |
|-------|-------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` o `litecoin` |
| `crypto_address` | Indirizzo del destinatario |
| `crypto_amount` | Importo richiesto (decimale) |
| `crypto_currency` | Simbolo della valuta nativa (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Etichetta del destinatario (se impostata) |
| `crypto_message` | Testo libero (se impostato) |
| `crypto_lightning_fallback` | Fattura BOLT11 Lightning (da `lightning=` BIP321) |
| `crypto_payjoin_endpoint` | Endpoint payjoin (da `pj=` / `pjos=`) |
| `crypto_required_params` | Parametri `req-*`, preservati per decisione lato client |
| `crypto_uri_version` | `bip21` o `bip321` |

### Esempio di risposta API

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

### Come abilitare la funzione

Il parsing degli URI crypto è coperto dall'interruttore generale **Estrazione di codici a barre / QR** — non è richiesta alcuna configurazione specifica dello standard.

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   * Spostare il cursore per abilitarla.

Per l'elenco completo degli standard di QR code di pagamento, consultare la [pagina di Panoramica](./README.md).
