# PagoPA

## Pregled

**PagoPA** je QR standard za plaćanja italijanske javne uprave. Svaka faktura izdata od strane italijanskog organa javne uprave (opštine, univerziteti, zdravstvo, poreske uprave) nosi PagoPA QR kod. DocBits dekodira payload i vraća četiri obavezna polja za plaćanje u API odgovoru dokumenta.

### Pregled funkcije

PagoPA payload-i su kompaktni i strogo strukturirani: tačno **pet polja razdvojenih znakom pipe** u jednom redu. Iznosi su kodirani u **centima** (ceo broj) i automatski se konvertuju u euro decimale od strane ekstraktora. Vodeće nule u `codice_avviso` (18-cifreno obaveštenje o plaćanju) se čuvaju — nikada ne treba da se parsira kao ceo broj, pošto je identifikator fiksne širine.

#### Ključne prednosti

* **Obavezna pokrivenost** za fakture italijanske JU: `codice_avviso` i fiskalni kod poverioca izdvojeni u imenovana polja.
* **Bezbedno numeričko rukovanje**: 18-cifreni `codice_avviso` zadržava vodeće nule; iznos u centima je takođe izložen kao float u evrima.

***

### Detekcija

- Magični prefiks: `PAGOPA|002|`
- Tačno **5 polja razdvojenih pipe** nakon prefiksa: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Samo EUR** — nijedna druga valuta nije validna prema specifikaciji

### Izdvojena polja

Sva polja koriste prefiks `pagopa_`:

| Polje | Opis |
|-------|------|
| `pagopa_codice_avviso` | 18-cifreno obaveštenje o plaćanju — vodeće nule očuvane (string) |
| `pagopa_fiscal_code_creditor` | 11-cifreni fiskalni kod poverioca (string) |
| `pagopa_amount_cents` | Iznos u centima (ceo broj) |
| `pagopa_amount` | Iznos u evrima (decimalno, izveden iz `pagopa_amount_cents`) |
| `pagopa_auth` | Opcioni indikator auth/verzije iz payload-a |

### Primer API odgovora

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Kako omogućiti funkciju

Parsiranje PagoPA je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
