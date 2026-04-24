# EMVCo MPM (QR prikazan od strane trgovca)

## Pregled

**EMVCo MPM** (Merchant-Presented Mode) je globalna specifikacija QR kodova koju održava EMVCo — isto telo iza standarda za čip-kartice i beskontaktna plaćanja. Jedan TLV (Tag-Length-Value) okvir deli više od tuceta nacionalnih sistema trenutnih plaćanja, tako da jedan parser pokriva **Pix** (Brazil), **UPI** (Indija), **PayNow** (Singapur), **PromptPay** (Tajland), **QRIS** (Indonezija), **QR Ph** (Filipini), **VietQR** (Vijetnam), **FPS** (Hong Kong), **DuitNow** (Malezija), **NETS** (Singapur) i mnoge druge.

### Pregled funkcije

Svaki EMVCo MPM payload deli isti okvir: počinje sa `000201` (Payload Format Indicator = 01) i završava se sa `6304<CRC>`, gde je `<CRC>` 4-heksa CRC16-CCITT-FALSE kontrolna suma. Unutar, TLV-kodirani tagovi 26–51 nose **Merchant Account Info** šablone identifikovane **GUI pod-tagom** — taj GUI tag je način na koji DocBits otkriva kom nacionalnom šemu QR pripada. CRC se validira i rezultat je izložen kao boolean, tako da trgovci mogu da otkriju izmenjene QR kodove.

#### Ključne prednosti

* **Jedan ekstraktor, mnogo šema**: jedan generički TLV parser obrađuje celu EMVCo MPM porodicu.
* **Nacionalne šeme identifikovane**: izlaz uključuje imenovanu šemu (npr. `pix`, `upi`, `paynow`), tako da nizvodna logika može čisto da se razgrana.
* **CRC validnost izložena**: `emvmpm_crc16_valid` otkriva izmenjene ili pokvarene QR kodove.
* **Normalizacija valute**: ISO 4217 numerički kodovi valuta se automatski mapiraju na alpha-3 (20+ valuta; nemapirani numerički kodovi prolaze nepromenjeni).

***

### Detekcija

- Magični oblik: počinje sa `000201` i završava se sa `6304<4-hex CRC16-CCITT-FALSE>`
- Generički TLV dekoder prolazi kroz svaki tag
- Nacionalne šeme se identifikuju preko **GUI pod-taga** u šablonima Merchant Account Info (tagovi 26–51)

### Prepoznate nacionalne šeme

| GUI pod-tag | Šema | Zemlja |
|-------------|------|--------|
| `br.gov.bcb.pix` | **Pix** | Brazil |
| `UPI` | **UPI** | Indija |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapur |
| `SG.COM.NETS` | **NETS** | Singapur |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonezija |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filipini |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Tajland |
| `A000000727` | **VietQR** | Vijetnam |

Neprepoznate GUI / AID vrednosti se i dalje parsiraju — ekstraktor se vraća na generički skup polja EMVCo MPM.

### Izdvojena polja

Sva polja koriste prefiks `emvmpm_`:

| Polje | Opis |
|-------|------|
| `emvmpm_scheme` | Detektovana nacionalna šema (npr. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) ili `generic` |
| `emvmpm_merchant_name` | Ime trgovca (tag 59) |
| `emvmpm_merchant_city` | Grad trgovca (tag 60) |
| `emvmpm_country_code` | Kod zemlje ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Iznos transakcije (decimalno, tag 54) |
| `emvmpm_currency` | Valuta alpha-3 (konvertovana iz tag-53 numeričkog koda) |
| `emvmpm_additional_data` | Ugnježđeni objekat: broj računa, referentna oznaka, oznaka terminala, svrha transakcije (pod-tagovi tag 62) |
| `emvmpm_crc16_valid` | Boolean — `true` ako se CRC16 kontrolna suma poklapa |

### Primer API odgovora (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Kako omogućiti funkciju

Parsiranje EMVCo MPM je pokriveno opštim prekidačem **Ekstrakcija barkodova / QR kodova** — nije potrebna standardu-specifična konfiguracija.

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem je uključite.

Za kompletnu listu standarda za plaćanje putem QR koda pogledajte stranicu [Pregled](./README.md).
