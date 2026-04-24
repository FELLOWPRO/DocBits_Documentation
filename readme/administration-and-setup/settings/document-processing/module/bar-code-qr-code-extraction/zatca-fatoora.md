# ZATCA Fatoora (Saudijska Arabija)

## Pregled

**ZATCA Fatoora** je QR kod za e-fakturisanje koji je propisala Uprava za Zekat, poreze i carine Saudijske Arabije. Od **decembra 2021. (Faza 1)** svaka B2C faktura izdata u Kraljevstvu mora nositi Fatoora QR sa pet osnovnih polja fakture; a od **januara 2023. (Faza 2)** QR dodatno nosi kriptografsku omotnicu potpisa. DocBits dekodira obe faze i vraća svako polje plaćanja Faze 1 kao imenovano svojstvo u API odgovoru dokumenta.

### Pregled funkcije

ZATCA Fatoora koristi format **binarnog TLV** (1 bajt ID-a taga, 1 bajt dužine, vrednost) upakovanog u **Base64**. Sav tekst je UTF-8, pa se arapska imena prodavaca čisto dekodiraju. Ekstraktor izlaže tagove 1–5 Faze 1 kao strukturirana polja i — kada su prisutni — tagove 6–9 Faze 2 kao Base64 stringove za nizvodne alate za usklađenost. **Verifikacija potpisa i hash-a je namerno van obima**; to pripada namenskim stack-ovima za usklađenost e-fakturisanja.

#### Ključne prednosti

* **Obavezna pokrivenost usklađenosti**: svaka saudijska B2C faktura se parsira.
* **Podrška za arapski**: UTF-8 imena prodavaca prolaze bez ponovnog kodiranja.
* **Faza 1 i Faza 2**: obe faze se detektuju; faza se izlaže u izlazu.
* **Omotnica Faze 2 očuvana**: hash, potpis, javni ključ i potpis sertifikata se čuvaju kao Base64 stringovi za alate za usklađenost.

***

### Detekcija

- Base64 upakovani binarni TLV (tagovi 1–9, 1 bajt ID-a taga + 1 bajt dužine + vrednost)
- Detekcija faze: `zatca_phase = 1` kada su prisutni samo tagovi 1–5; `zatca_phase = 2` kada su prisutni i tagovi 6–9

### Raspored TLV tagova

| Tag | Faza | Sadržaj |
|-----|------|---------|
| 1 | 1 | Ime prodavca (UTF-8, podržava arapski) |
| 2 | 1 | Broj registracije PDV-a |
| 3 | 1 | Vremenska oznaka fakture (ISO 8601) |
| 4 | 1 | Ukupno fakture |
| 5 | 1 | Ukupno PDV |
| 6 | 2 | Hash XML fakture (Base64) |
| 7 | 2 | Digitalni potpis (Base64) |
| 8 | 2 | Javni ključ (Base64) |
| 9 | 2 | Potpis sertifikata (Base64) |

### Izdvojena polja

Sva polja koriste prefiks `zatca_`:

| Polje | Opis |
|-------|------|
| `zatca_seller_name` | Ime prodavca (UTF-8) |
| `zatca_vat_number` | Broj registracije PDV-a |
| `zatca_invoice_timestamp` | Datum/vreme fakture |
| `zatca_invoice_total` | Ukupno fakture (decimalno) |
| `zatca_vat_total` | Ukupno PDV (decimalno) |
| `zatca_phase` | `1` (Faza 1) ili `2` (Faza 2) |
| `zatca_invoice_hash` | Hash XML fakture — samo Faza 2, Base64 |
| `zatca_signature` | Digitalni potpis — samo Faza 2, Base64 |
| `zatca_public_key` | Javni ključ — samo Faza 2, Base64 |
| `zatca_certificate_signature` | Potpis sertifikata — samo Faza 2, Base64 |

{% hint style="info" %}
**Van obima**: DocBits ne verifikuje kriptografski potpis, hash ili lanac sertifikata. Ta verifikacija je posebno pitanje usklađenosti i treba da se rukuje ZATCA-sertifikovanim stack-om za e-fakturisanje.
{% endhint %}

### Primer API odgovora (Faza 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Kako omogućiti funkciju

Parsiranje ZATCA Fatoora je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
