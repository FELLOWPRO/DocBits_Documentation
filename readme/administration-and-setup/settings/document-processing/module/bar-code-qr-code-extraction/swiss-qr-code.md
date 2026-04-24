# Swiss QR Bill

## Pregled

**Swiss QR Bill** je nacionalni standard platnog naloga koji je od 30. juna 2020. zamenio narandžaste i crvene švajcarske uplatnice. Svaka domaća švajcarska faktura — bilo od javnih preduzeća, osiguravajućih društava ili poslovnih partnera — danas nosi Swiss QR Bill kod. DocBits automatski dekodira ove kodove i svako polje plaćanja čini dostupnim kroz API odgovor.

### Pregled funkcije

Swiss QR Bill-ovi prate **ISO 20022** standard za plaćanja i izdaju se u dve verzije: **v1.0** (rano uvođenje) i **v2.0** (aktuelna). DocBits ekstraktor podržava obe. Prepoznati payload-i se dekodiraju u kompletan skup polja — poverilac, dužnik, IBAN / QR-IBAN, iznos, valuta, tip reference (QRR, SCOR ili NON), strukturirane i slobodne poruke i alternativne šeme plaćanja.

#### Ključne prednosti

* **Nula ručnog unosa** za švajcarske fakture: IBAN, iznos, referenca i poverilac stižu direktno u dokument.
* **Pokrivene obe verzije**: v1.0 i v2.0 se otkrivaju automatski.
* **Očuvani tipovi referenci**: QRR, SCOR i NON ostaju tačno kao što su odštampani, što održava rad nizvodnog usaglašavanja.

***

### Detekcija

- Magični prefiks: `SPC\n0100` (v1.0) ili `SPC\n0200` (v2.0)
- Usklađen sa ISO 20022
- Parser takođe izlaže `alt-schemes` (alternativne procedure plaćanja) ako postoje

### Izdvojena polja

Sva polja koriste prefiks `swissqr_`:

| Polje | Opis |
|-------|------|
| `swissqr_account` | IBAN ili QR-IBAN poverioca |
| `swissqr_creditor_name` | Naziv poverioca |
| `swissqr_creditor_street` | Ulica / red adrese poverioca |
| `swissqr_creditor_city` | Grad poverioca |
| `swissqr_creditor_postal_code` | Poštanski broj poverioca |
| `swissqr_creditor_country` | Država poverioca (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Naziv dužnika (ako je odštampan) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Adresa dužnika |
| `swissqr_amount` | Iznos (decimalno) |
| `swissqr_currency` | Valuta (ISO 4217) — obično `CHF` ili `EUR` |
| `swissqr_reference` | Strukturirana referenca (QRR ili SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` ili `NON` |
| `swissqr_unstructured_message` | Slobodan tekst poruke |
| `swissqr_bill_information` | Strukturirane informacije o računu (S1 / Swico) |
| `swissqr_alt_schemes` | Alternativne procedure (ako postoje) |

### Primer API odgovora

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

### Kako omogućiti funkciju

Parsiranje Swiss QR Bill je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
