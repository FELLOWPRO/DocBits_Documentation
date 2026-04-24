# SPAYD / Short Payment Descriptor (Češki)

## Pregled

**SPAYD** (Short Payment Descriptor), poznat i kao **SPD**, je standardni QR kod za plaćanja definisan od strane Češkog udruženja banaka. Štampa se praktično na svakoj češkoj poslovnoj fakturi i delimično se koristi u Slovačkoj. DocBits dekodira SPAYD payload-e i vraća kompletnu instrukciju za plaćanje — uključujući češke specifične simbole (variable, specific, constant) — u API odgovoru dokumenta.

### Pregled funkcije

SPAYD payload je lista parova ključ:vrednost razdvojenih zvezdicama. Vrednosti su percent-kodirane, tako da su UTF-8 imena primalaca i poruke očuvani. DocBits podržava uobičajenu `ACC` varijantu (IBAN plus opcionalni BIC, razdvojeni `+`), `ALT-ACC` (alternativni IBAN-ovi, razdvojeni zarezima) i čuva bilo koje nepoznate ključeve specifične za dobavljača u posebnom polju (`spayd_raw_pairs`), tako da nizvodni potrošači nikada ne gube podatke.

#### Ključne prednosti

* **Kompletna pokrivenost čeških plaćanja**: IBAN/BIC plus VS/SS/KS simboli se izdvajaju u imenovana polja.
* **Unicode-bezbedno**: percent-kodirana UTF-8 imena primalaca i poruke prolaze netaknuta.
* **Kompatibilno sa budućnošću**: nepoznati ključevi se čuvaju u `spayd_raw_pairs`.

***

### Detekcija

- Magični prefiks: `SPD*1.0*`
- Payload je lista razdvojena sa `*` parova `KEY:value`, npr. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Vrednosti su **percent-kodirane** (RFC 3986)
- `ACC` može nositi `IBAN+BIC` (razdvojene sa `+`); `ALT-ACC` nosi alternativne IBAN-ove razdvojene zarezima

### Izdvojena polja

Sva polja koriste prefiks `spayd_`:

| Polje | Opis |
|-------|------|
| `spayd_iban` | Primarni IBAN (iz `ACC`) |
| `spayd_bic` | BIC (iz `ACC`, ako postoji) |
| `spayd_alt_ibans` | Lista alternativnih IBAN-ova (iz `ALT-ACC`) |
| `spayd_amount` | Iznos (decimalno, iz `AM`) |
| `spayd_currency` | Valuta (iz `CC`, obično `CZK`) |
| `spayd_variable_symbol` | Varijabilni simbol (`VS`) — broj fakture/reference |
| `spayd_specific_symbol` | Specifični simbol (`SS`) |
| `spayd_constant_symbol` | Konstantni simbol (`KS`) |
| `spayd_recipient_name` | Ime primaoca (iz `RN`) |
| `spayd_due_date` | Datum dospeća (iz `DT`, `YYYYMMDD`) |
| `spayd_message` | Slobodna poruka (iz `MSG`) |
| `spayd_raw_pairs` | Nepoznati ili specifični za dobavljača parovi `KEY:value`, očuvani doslovno |

### Primer API odgovora

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

### Kako omogućiti funkciju

Parsiranje SPAYD je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
