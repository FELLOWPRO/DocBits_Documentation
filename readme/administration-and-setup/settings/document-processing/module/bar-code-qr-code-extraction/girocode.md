# GiroCode (EPC069-12)

## Overzicht

De **GiroCode** is de SEPA-betalings-QR-code gedefinieerd door de European Payments Council in de specificatie **EPC069-12**. Het is de de-facto standaard op facturen van Duitse en Oostenrijkse banken (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) en wordt ook uitgegeven in Nederland, België en Finland. DocBits decodeert beide revisies (**v001** en **v002**) en retourneert de volledige SEPA-betalingspayload in de API-respons van het document.

### Functieoverzicht

Een GiroCode bevat alles wat nodig is om een SEPA-overboeking te initiëren: BIC en IBAN van de begunstigde, naam begunstigde, bedrag, doel, en een gestructureerde crediteurreferentie of een vrije omschrijving. DocBits normaliseert de payload zodanig dat **bedragen met `.` of `,` als decimaalscheidingsteken** — een veelvoorkomende afwijking door Duitse QR-generatoren ten opzichte van de specificatie — foutloos worden geaccepteerd.

#### Belangrijkste Voordelen

* **Brede dekking in DE / AT**: elke grote retailbank drukt GiroCodes op klantfacturen.
* **Beide revisies ondersteund**: v001 (BIC verplicht) en v002 (BIC optioneel in de EEA).
* **Tolerant voor decimaalscheiding**: accepteert `227.01` en `227,01` uitwisselbaar.

***

### Detectie

- Magische prefix: `BCD\n001` (v001) of `BCD\n002` (v002)
- Regel-gescheiden gestructureerde payload volgens EPC069-12
- **v002** maakt de BIC optioneel als de IBAN binnen de Single Euro Payments Area valt

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `girocode_`:

| Veld | Beschrijving |
|------|--------------|
| `girocode_bic` | BIC van de begunstigde (verplicht in v001, optioneel in v002 voor EEA) |
| `girocode_creditor_name` | Naam begunstigde |
| `girocode_iban` | IBAN van de begunstigde |
| `girocode_amount` | Bedrag (decimaal) — `.` en `,` geaccepteerd |
| `girocode_currency` | Valuta (meestal `EUR`) |
| `girocode_purpose` | SEPA-doelcode |
| `girocode_structured_reference` | Gestructureerde crediteurreferentie (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Vrije omschrijving |
| `girocode_version` | `001` of `002` |

### Voorbeeld API-respons

Realistisch voorbeeld (factuur Dr. Meindl u. Partner):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Hoe de Functie In te Schakelen

Parsing van GiroCode wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
