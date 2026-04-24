# Kripto URI plaćanja (BIP21 / BIP321)

## Pregled

Kripto URI plaćanja su neformalni, ali široko usvojeni standard za kodiranje zahteva za plaćanje u kriptovalutama unutar QR kodova. DocBits prepoznaje i **BIP21** (originalni Bitcoin URI plaćanja) i **BIP321** (modernizovanu ekstenziju iz 2024.), na pet najzastupljenijih blockchain-ova: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** i **Litecoin**.

### Pregled funkcije

Kripto QR payload je URI sa šemom (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), adresom primaoca i skupom parametara u stilu URL-a. DocBits izdvaja sve standardne BIP21 parametre (`amount`, `label`, `message`) i novije BIP321 ekstenzije (`lightning=` fallback, `pj=` / `pjos=` payjoin endpoint-i). Prema BIP21 specifikaciji, parametri sa prefiksom `req-` mogu biti odbačeni od strane potrošača ako nisu podržani — DocBits ih stoga čuva u posebnom polju (`crypto_required_params`), tako da klijenti mogu da odluče kako da ih tretiraju.

#### Ključne prednosti

* **Multi-chain podrška**: Bitcoin, Lightning, Zcash, Ethereum i Litecoin u jednom ekstraktoru.
* **BIP21 + BIP321**: obe verzije se prepoznaju; verzija se izlaže u izlazu.
* **Šema case-insensitive**: `BITCOIN:` i `bitcoin:` se tretiraju identično.

***

### Detekcija

- Detekcija bazirana na šemi (case-insensitive): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standardni URI format: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Podržani parametri

**BIP21 osnovni parametri:**
- `amount` — traženi iznos u nativnoj jedinici
- `label` — čitljiva oznaka primaoca
- `message` — slobodan tekst

**BIP321 ekstenzije:**
- `lightning=<BOLT11>` — Lightning faktura kao fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — payjoin endpoint-i
- `req-*` — obavezni parametri (očuvani u `crypto_required_params`)

### Izdvojena polja

Sva polja koriste prefiks `crypto_`:

| Polje | Opis |
|-------|------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` ili `litecoin` |
| `crypto_address` | Adresa primaoca |
| `crypto_amount` | Traženi iznos (decimalno) |
| `crypto_currency` | Simbol nativne valute (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Oznaka primaoca (ako je postavljena) |
| `crypto_message` | Slobodan tekst (ako je postavljen) |
| `crypto_lightning_fallback` | BOLT11 Lightning faktura (iz BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Payjoin endpoint (iz `pj=` / `pjos=`) |
| `crypto_required_params` | Svi `req-*` parametri, očuvani za odluku klijenta |
| `crypto_uri_version` | `bip21` ili `bip321` |

### Primer API odgovora

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

### Kako omogućiti funkciju

Parsiranje kripto URI je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
