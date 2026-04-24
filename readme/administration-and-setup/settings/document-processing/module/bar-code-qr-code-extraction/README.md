# Ekstrakcija barkodova / QR kodova

## **Pregled**

Ova funkcija omogućava automatsku ekstrakciju informacija iz **barkodova i QR kodova** ugrađenih u dokumente. Radi se o „sve ili ništa" podešavanju — njenim uključivanjem aktivira se ekstrakcija za oba tipa.

## Kako omogućiti ekstrakciju barkodova / QR kodova

Za aktiviranje funkcije pratite ove korake:

1. **Otvorite Podešavanja**:
   * Sa kontrolne table idite na **Podešavanja**.
   * Izaberite **Obrada dokumenata**, a zatim **Modul**.
2. **Omogućite funkciju**:
   * Pomerite se do opcije **Ekstrakcija barkodova / QR kodova**.
   * Klizačem uključite ekstrakciju.

## **Podržani tipovi koda**

DocBits podržava ekstrakciju sledećih tipova koda:

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

## Standardi plaćanja putem QR koda

Pored opšteg dekodiranja QR kodova, DocBits prepoznaje **sedam različitih standarda za plaćanje putem QR koda** i automatski izdvaja njihova polja za plaćanje u API odgovoru dokumenta. Klijenti više ne moraju ručno da dekodiraju ove stringove — svaki standard dolazi sa sopstvenim prefiksom polja (npr. `swissqr_*`, `girocode_*`), tako da vrednosti direktno stižu u matching, validaciju i izvoz.

| # | Standard | Region | Prefiks polja | Tipična upotreba |
|---|----------|--------|---------------|------------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Švajcarska | `swissqr_*` | Svaka švajcarska faktura od 2020. |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | SEPA plaćanja |
| 3 | [SPAYD / SPD](spayd.md) | CZ, delimično SK | `spayd_*` | Standard Češkog udruženja banaka |
| 4 | [PagoPA](pagopa.md) | IT (javna uprava) | `pagopa_*` | Obavezno na fakturama italijanske JU |
| 5 | [Kripto URI plaćanja](crypto-uris.md) | Globalno (kripto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK i dr. | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Saudijska Arabija | `zatca_*` | Obavezno na svakoj KSA fakturi |

**Detekcija je automatska.** Svaki dekodirani QR string se proverava na svoj magični prefiks (npr. `SPC\n0200` za Swiss QR Bill v2.0 ili `PAGOPA|002|` za PagoPA); samo prepoznati standardi se prevode u strukturirana polja.

### **Povezane stranice**

[Detalji ekstrakcije barkoda](bar-code-extractions.md)
