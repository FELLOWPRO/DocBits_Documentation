# Barcode / QR-Code Extractie

## **Overzicht**

Deze functie maakt automatische extractie van informatie mogelijk van **zowel barcodes als QR-codes** die in documenten zijn ingesloten. Het is een alles-of-niets instelling — inschakelen activeert de extractie voor beide typen.

## Hoe Barcode / QR-Code Extractie In te Schakelen

Volg deze stappen om de Barcode / QR-Code Extractie functie in te schakelen:

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   *   Gebruik de schuifregelaar om Barcode / QR-Code Extractie in te schakelen.
       

       <figure><img src="../../../../../.gitbook/assets/image (443) (1).png" alt=""><figcaption></figcaption></figure>

## **Ondersteunde Code Typen**

DocBits ondersteunt extractie van de volgende code typen:

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Betalings-QR-code Standaarden

Naast de generieke QR-decodering herkent DocBits **zeven afzonderlijke betalings-QR-codestandaarden** en extraheert hun betalingsvelden automatisch in de API-respons van het document. Klanten hoeven deze QR-strings niet meer handmatig te decoderen — elke standaard levert een eigen veldprefix (bijv. `swissqr_*`, `girocode_*`), zodat de waarden rechtstreeks doorstromen naar matching, validatie en export.

| # | Standaard | Regio | Veldprefix | Typisch gebruik |
|---|-----------|-------|------------|-----------------|
| 1 | [Zwitserse QR Bill](swiss-qr-code.md) | Zwitserland | `swissqr_*` | Elke Zwitserse factuur sinds 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | SEPA-betalingen |
| 3 | [SPAYD / SPD](spayd.md) | CZ, gedeeltelijk SK | `spayd_*` | Standaard van de Tsjechische Bankiersvereniging |
| 4 | [PagoPA](pagopa.md) | IT (overheid) | `pagopa_*` | Verplicht op Italiaanse PA-facturen |
| 5 | [Crypto-betalings-URIs](crypto-uris.md) | Wereldwijd (crypto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK e.a. | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Saoedi-Arabië | `zatca_*` | Verplicht op elke KSA-factuur |

**Detectie is automatisch.** Elke gedecodeerde QR-string wordt gecontroleerd op zijn magische prefix (bijv. `SPC\n0200` voor Zwitserse QR Bill v2.0 of `PAGOPA|002|` voor PagoPA); alleen herkende standaarden worden omgezet in gestructureerde velden.

### **Gerelateerde Pagina's**

[Details Barcode Extractie](bar-code-extractions.md)
