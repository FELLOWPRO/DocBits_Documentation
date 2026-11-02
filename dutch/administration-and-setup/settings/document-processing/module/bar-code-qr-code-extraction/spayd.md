# SPAYD / Short Payment Descriptor (Tsjechisch)

## Overzicht

**SPAYD** (Short Payment Descriptor), ook bekend als **SPD**, is de standaard betalings-QR-code gedefinieerd door de Tsjechische Bankiersvereniging. Deze wordt afgedrukt op vrijwel elke Tsjechische zakelijke factuur en wordt gedeeltelijk ook in Slowakije gebruikt. DocBits decodeert SPAYD-payloads en retourneert de volledige betalingsinstructie — inclusief Tsjechisch-specifieke symbolen (variable, specific, constant) — in de API-respons van het document.

### Functieoverzicht

Een SPAYD-payload is een door sterretjes gescheiden lijst van sleutel:waarde-paren. Waarden zijn percent-encoded, zodat UTF-8-ontvangernamen en -berichten bewaard blijven. DocBits ondersteunt de gangbare `ACC`-variant (IBAN plus optionele BIC, plus-gescheiden), `ALT-ACC` (alternatieve IBANs, komma-gescheiden) en bewaart onbekende leverancier-specifieke sleutels in een apart veld (`spayd_raw_pairs`), zodat downstream consumers geen gegevens verliezen.

#### Belangrijkste Voordelen

* **Volledige dekking Tsjechische betalingen**: IBAN/BIC plus de VS/SS/KS-symbolen worden naar benoemde velden geëxtraheerd.
* **Unicode-veilig**: percent-encoded UTF-8-ontvangernamen en -berichten komen heel door.
* **Voorwaarts compatibel**: onbekende sleutels worden bewaard in `spayd_raw_pairs`.

***

### Detectie

- Magische prefix: `SPD*1.0*`
- Payload is een door `*` gescheiden lijst van `KEY:value`-paren, bijv. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Waarden zijn **percent-encoded** (RFC 3986)
- `ACC` kan `IBAN+BIC` dragen (plus-gescheiden); `ALT-ACC` draagt komma-gescheiden alternatieve IBANs

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `spayd_`:

| Veld | Beschrijving |
|------|--------------|
| `spayd_iban` | Primaire IBAN (uit `ACC`) |
| `spayd_bic` | BIC (uit `ACC`, indien aanwezig) |
| `spayd_alt_ibans` | Lijst met alternatieve IBANs (uit `ALT-ACC`) |
| `spayd_amount` | Bedrag (decimaal, uit `AM`) |
| `spayd_currency` | Valuta (uit `CC`, meestal `CZK`) |
| `spayd_variable_symbol` | Variabel symbool (`VS`) — factuur-/referentienummer |
| `spayd_specific_symbol` | Specifiek symbool (`SS`) |
| `spayd_constant_symbol` | Constant symbool (`KS`) |
| `spayd_recipient_name` | Ontvangernaam (uit `RN`) |
| `spayd_due_date` | Vervaldatum (uit `DT`, `YYYYMMDD`) |
| `spayd_message` | Vrij bericht (uit `MSG`) |
| `spayd_raw_pairs` | Onbekende of leverancier-specifieke `KEY:value`-paren, letterlijk bewaard |

### Voorbeeld API-respons

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

### Hoe de Functie In te Schakelen

Parsing van SPAYD wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
