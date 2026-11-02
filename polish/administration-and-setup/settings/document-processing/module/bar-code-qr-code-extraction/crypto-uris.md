# Kryptowalutowe URI płatności (BIP21 / BIP321)

## Przegląd

Kryptowalutowe URI płatności to nieformalny, ale szeroko przyjęty standard kodowania żądań płatności w kryptowalutach w kodach QR. DocBits rozpoznaje zarówno **BIP21** (oryginalny URI płatności Bitcoin), jak i **BIP321** (zmodernizowane rozszerzenie z 2024 r.) dla pięciu najpopularniejszych blockchainów: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** i **Litecoin**.

### Przegląd funkcji

Payload QR krypto to URI ze schematem (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), adresem odbiorcy i zestawem parametrów w stylu URL. DocBits wyodrębnia wszystkie standardowe parametry BIP21 (`amount`, `label`, `message`) oraz nowsze rozszerzenia BIP321 (`lightning=` fallback, `pj=` / `pjos=` endpointy payjoin). Zgodnie ze specyfikacją BIP21 parametry z prefiksem `req-` mogą być odrzucane przez klientów, jeśli nie są obsługiwane — DocBits zachowuje je więc w osobnym polu (`crypto_required_params`), aby klienci mogli zdecydować, jak je obsłużyć.

#### Kluczowe korzyści

* **Wsparcie multi-chain**: Bitcoin, Lightning, Zcash, Ethereum i Litecoin w jednym ekstraktorze.
* **BIP21 + BIP321**: obie wersje rozpoznawane; wersja udostępniana w wyjściu.
* **Schemat niezależny od wielkości liter**: `BITCOIN:` i `bitcoin:` traktowane identycznie.

***

### Wykrywanie

- Wykrywanie na podstawie schematu (niezależne od wielkości liter): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standardowy format URI: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Obsługiwane parametry

**Podstawowe parametry BIP21:**
- `amount` — żądana kwota w natywnej jednostce
- `label` — czytelna etykieta odbiorcy
- `message` — swobodny tekst

**Rozszerzenia BIP321:**
- `lightning=<BOLT11>` — faktura Lightning jako fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — endpointy payjoin
- `req-*` — wymagane parametry (zachowane w `crypto_required_params`)

### Wyodrębnione pola

Wszystkie pola używają prefiksu `crypto_`:

| Pole | Opis |
|------|------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` lub `litecoin` |
| `crypto_address` | Adres odbiorcy |
| `crypto_amount` | Żądana kwota (dziesiętna) |
| `crypto_currency` | Symbol natywnej waluty (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Etykieta odbiorcy (jeśli ustawiona) |
| `crypto_message` | Swobodny tekst (jeśli ustawiony) |
| `crypto_lightning_fallback` | Faktura BOLT11 Lightning (z BIP321 `lightning=`) |
| `crypto_payjoin_endpoint` | Endpoint payjoin (z `pj=` / `pjos=`) |
| `crypto_required_params` | Wszystkie parametry `req-*`, zachowane do decyzji klienta |
| `crypto_uri_version` | `bip21` lub `bip321` |

### Przykładowa odpowiedź API

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

### Jak włączyć funkcję

Parsowanie URI krypto jest objęte ogólnym przełącznikiem **Ekstrakcja kodów kreskowych / QR** — nie jest wymagana konfiguracja specyficzna dla standardu.

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   * Ustaw przełącznik na włączony.

Pełną listę standardów płatniczych kodów QR znajdziesz na stronie [Przegląd](./README.md).
