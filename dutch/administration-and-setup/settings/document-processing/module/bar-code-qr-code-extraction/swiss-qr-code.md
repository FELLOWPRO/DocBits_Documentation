# Zwitserse QR Bill

## Overzicht

De **Zwitserse QR Bill** is de nationale betalingsstandaard die sinds 30 juni 2020 de oranje en rode Zwitserse stortingsformulieren heeft vervangen. Elke binnenlandse Zwitserse factuur — of deze nu van een nutsbedrijf, verzekeraar of zakenpartner afkomstig is — draagt vandaag een Zwitserse QR Bill-code. DocBits decodeert deze codes automatisch en stelt elk betalingsveld beschikbaar via de API-respons.

### Functieoverzicht

Zwitserse QR Bills volgen de betalingsstandaard **ISO 20022** en worden in twee versies uitgegeven: **v1.0** (eerste uitrol) en **v2.0** (huidig). De DocBits-extractor ondersteunt beide. Herkende payloads worden gedecodeerd in een volledige set velden — crediteur, debiteur, IBAN / QR-IBAN, bedrag, valuta, referentietype (QRR, SCOR of NON), gestructureerde en vrije berichten, en alternatieve betalingsschema's.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Belangrijkste Voordelen

* **Nul handmatige invoer** voor Zwitserse facturen: IBAN, bedrag, referentie en crediteur stromen rechtstreeks het document in.
* **Beide versies gedekt**: v1.0 en v2.0 worden automatisch gedetecteerd.
* **Referentietypen behouden**: QRR, SCOR en NON blijven exact zoals afgedrukt, wat de downstream reconciliatie werkend houdt.

***

### Detectie

- Magische prefix: `SPC\n0100` (v1.0) of `SPC\n0200` (v2.0)
- Conform ISO 20022
- De parser toont ook `alt-schemes` (alternatieve betalingsprocedures) indien aanwezig

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `swissqr_`:

| Veld | Beschrijving |
|------|--------------|
| `swissqr_account` | IBAN of QR-IBAN van de crediteur |
| `swissqr_creditor_name` | Naam van de crediteur |
| `swissqr_creditor_street` | Straat / adresregel crediteur |
| `swissqr_creditor_city` | Woonplaats crediteur |
| `swissqr_creditor_postal_code` | Postcode crediteur |
| `swissqr_creditor_country` | Land crediteur (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Naam debiteur (indien afgedrukt) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Debiteuradres |
| `swissqr_amount` | Bedrag (decimaal) |
| `swissqr_currency` | Valuta (ISO 4217) — meestal `CHF` of `EUR` |
| `swissqr_reference` | Gestructureerde referentie (QRR of SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` of `NON` |
| `swissqr_unstructured_message` | Vrije tekst/omschrijving |
| `swissqr_bill_information` | Gestructureerde factuurinformatie (S1 / Swico) |
| `swissqr_alt_schemes` | Alternatieve procedures (indien aanwezig) |

### Voorbeeld API-respons

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Hoe de Functie In te Schakelen

Parsing van Zwitserse QR Bill wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

<figure><img src="../../../../../.gitbook/assets/image (443) (1).png" alt=""><figcaption></figcaption></figure>

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
