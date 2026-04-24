# EMVCo MPM (Door Handelaar Gepresenteerde QR)

## Overzicht

**EMVCo MPM** (Merchant-Presented Mode) is de wereldwijde QR-codespecificatie onderhouden door EMVCo — hetzelfde orgaan achter chipkaart- en contactloze betalingsstandaarden. Eén enkele TLV-envelop (Tag-Length-Value) wordt gedeeld door meer dan een dozijn nationale instant-betalingssystemen, zodat één parser **Pix** (Brazilië), **UPI** (India), **PayNow** (Singapore), **PromptPay** (Thailand), **QRIS** (Indonesië), **QR Ph** (Filippijnen), **VietQR** (Vietnam), **FPS** (Hongkong), **DuitNow** (Maleisië), **NETS** (Singapore) en meer ontsluit.

### Functieoverzicht

Elke EMVCo MPM-payload deelt dezelfde envelop: hij begint met `000201` (Payload Format Indicator = 01) en eindigt met `6304<CRC>` waar `<CRC>` een 4-hex CRC16-CCITT-FALSE-checksum is. Binnenin dragen TLV-gecodeerde tags 26–51 **Merchant Account Info**-templates geïdentificeerd door een **GUI-subtag** — die GUI-tag is hoe DocBits detecteert tot welk nationaal schema de QR behoort. De CRC wordt gevalideerd en het resultaat blootgesteld als een boolean, zodat handelaren gemanipuleerde QR-codes kunnen detecteren.

#### Belangrijkste Voordelen

* **Eén extractor, veel schema's**: één generieke TLV-parser behandelt de gehele EMVCo MPM-familie.
* **Nationale schema's geïdentificeerd**: de output bevat een benoemd schema (bijv. `pix`, `upi`, `paynow`), zodat downstream logica schoon kan vertakken.
* **CRC-geldigheid blootgesteld**: `emvmpm_crc16_valid` onthult gemanipuleerde of corrupte QR-codes.
* **Valuta-normalisatie**: numerieke ISO 4217-valutacodes worden automatisch gemapt naar alpha-3 (20+ valuta; niet-gemapt numeriek blijft onveranderd).

***

### Detectie

- Magische vorm: begint met `000201` en eindigt met `6304<4-hex CRC16-CCITT-FALSE>`
- Een generieke TLV-decoder loopt door elke tag
- Nationale schema's worden geïdentificeerd via de **GUI-subtag** in Merchant Account Info-templates (tags 26–51)

### Herkende Nationale Schema's

| GUI-subtag | Schema | Land |
|------------|--------|------|
| `br.gov.bcb.pix` | **Pix** | Brazilië |
| `UPI` | **UPI** | India |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapore |
| `SG.COM.NETS` | **NETS** | Singapore |
| `HK.COM.HKICL.FPS` | **FPS** | Hongkong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonesië |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filippijnen |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Thailand |
| `A000000727` | **VietQR** | Vietnam |

Niet-herkende GUI-/AID-waarden worden nog steeds geparseerd — de extractor valt terug op de generieke EMVCo MPM-veldset.

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `emvmpm_`:

| Veld | Beschrijving |
|------|--------------|
| `emvmpm_scheme` | Gedetecteerd nationaal schema (bijv. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) of `generic` |
| `emvmpm_merchant_name` | Handelaarnaam (tag 59) |
| `emvmpm_merchant_city` | Handelaarstad (tag 60) |
| `emvmpm_country_code` | Landcode ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Transactiebedrag (decimaal, tag 54) |
| `emvmpm_currency` | Valuta alpha-3 (geconverteerd uit de tag-53 numerieke code) |
| `emvmpm_additional_data` | Geneste structuur: factuurnummer, referentielabel, terminallabel, doel van de transactie (tag-62 subtags) |
| `emvmpm_crc16_valid` | Boolean — `true` als de CRC16-checksum overeenkomt |

### Voorbeeld API-respons (Pix)

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

### Hoe de Functie In te Schakelen

Parsing van EMVCo MPM wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
