# GiroCode (EPC069-12)

## Pregled

**GiroCode** je SEPA QR kod za plaćanja definisan od strane European Payments Council u specifikaciji **EPC069-12**. De facto je standard na fakturama nemačkih i austrijskih banaka (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria), a takođe se izdaje u Holandiji, Belgiji i Finskoj. DocBits dekodira obe revizije (**v001** i **v002**) i vraća kompletan SEPA payload plaćanja u API odgovoru dokumenta.

### Pregled funkcije

GiroCode sadrži sve što je potrebno za pokretanje SEPA transfera: BIC i IBAN korisnika, ime korisnika, iznos, svrhu i bilo strukturiranu referencu poverioca, bilo slobodan tekst poruke. DocBits normalizuje payload tako da se **iznosi sa `.` ili `,` kao decimalnim separatorom** — česta deviacija nemačkih generatora od specifikacije — prihvataju bez greške.

#### Ključne prednosti

* **Široka pokrivenost DE / AT**: svaka velika maloprodajna banka štampa GiroCode na fakturama za klijente.
* **Obe revizije podržane**: v001 (BIC obavezan) i v002 (BIC opcionalan u EEA).
* **Tolerancija na decimalni separator**: `227.01` i `227,01` se prihvataju ravnopravno.

***

### Detekcija

- Magični prefiks: `BCD\n001` (v001) ili `BCD\n002` (v002)
- Strukturirani payload po linijama prema specifikaciji EPC069-12
- **v002** čini BIC opcionalnim kada se IBAN nalazi u Jedinstvenoj evrozoni plaćanja

### Izdvojena polja

Sva polja koriste prefiks `girocode_`:

| Polje | Opis |
|-------|------|
| `girocode_bic` | BIC korisnika (obavezan u v001, opcionalan u v002 za EEA) |
| `girocode_creditor_name` | Ime korisnika |
| `girocode_iban` | IBAN korisnika |
| `girocode_amount` | Iznos (decimalno) — `.` i `,` prihvaćeni |
| `girocode_currency` | Valuta (obično `EUR`) |
| `girocode_purpose` | SEPA kod svrhe |
| `girocode_structured_reference` | Strukturirana referenca poverioca (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Slobodan tekst poruke |
| `girocode_version` | `001` ili `002` |

### Primer API odgovora

Realan primer (faktura Dr. Meindl u. Partner):

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

### Kako omogućiti funkciju

Parsiranje GiroCode je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
