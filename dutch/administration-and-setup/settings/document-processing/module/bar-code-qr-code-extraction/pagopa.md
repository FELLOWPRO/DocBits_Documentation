# PagoPA

## Overzicht

**PagoPA** is de QR-betalingsstandaard van de Italiaanse overheid. Elke factuur uitgegeven door een Italiaans PA-orgaan (gemeenten, universiteiten, gezondheidszorg, belastingautoriteiten) draagt een PagoPA QR-code. DocBits decodeert de payload en retourneert de vier verplichte betalingsvelden in de API-respons van het document.

### Functieoverzicht

PagoPA-payloads zijn compact en strikt gestructureerd: precies **vijf door pipes gescheiden velden** op één regel. Bedragen worden gecodeerd in **centen** (integer) en automatisch door de extractor geconverteerd naar euro-decimalen. De voorloopnullen van de `codice_avviso` (18-cijferig betalingsbericht) blijven bewaard — deze mag nooit als integer worden geparseerd, omdat het een identificatie met vaste breedte is.

#### Belangrijkste Voordelen

* **Verplichte dekking** voor Italiaanse PA-facturen: `codice_avviso` en het fiscale code van de crediteur worden in benoemde velden geëxtraheerd.
* **Veilige numerieke afhandeling**: de 18-cijferige `codice_avviso` behoudt de voorloopnullen; het bedrag in centen wordt ook als euro-float blootgesteld.

***

### Detectie

- Magische prefix: `PAGOPA|002|`
- Precies **5 door pipes gescheiden velden** na de prefix: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Alleen EUR** — geen andere valuta is geldig volgens de specificatie

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `pagopa_`:

| Veld | Beschrijving |
|------|--------------|
| `pagopa_codice_avviso` | 18-cijferig betalingsbericht — voorloopnullen bewaard (string) |
| `pagopa_fiscal_code_creditor` | 11-cijferige fiscale code van de crediteur (string) |
| `pagopa_amount_cents` | Bedrag in centen (integer) |
| `pagopa_amount` | Bedrag in euro (decimaal, afgeleid van `pagopa_amount_cents`) |
| `pagopa_auth` | Optionele auth-/versie-indicator uit de payload |

### Voorbeeld API-respons

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Hoe de Functie In te Schakelen

Parsing van PagoPA wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
