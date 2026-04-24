# Bar-Code / QR-Code-Extraktion

## **Überblick**

Diese Funktion ermöglicht die automatische Extraktion von Informationen aus **Barcodes und QR-Codes**, die in Dokumenten eingebettet sind. Es handelt sich um eine Alles-oder-Nichts-Einstellung — das Aktivieren schaltet die Extraktion für beide Code-Typen zugleich frei.

## So aktivieren Sie die Bar-Code / QR-Code-Extraktion

Folgen Sie diesen Schritten, um die Funktion zu aktivieren:

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   *   Schalten Sie den Schieberegler um, um die Bar-Code / QR-Code-Extraktion zu aktivieren.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Unterstützte Code-Typen**

DocBits unterstützt die Extraktion der folgenden Code-Typen:

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**&#x20;
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Payment-QR-Code-Standards

Über die allgemeine QR-Decodierung hinaus erkennt DocBits **sieben eigenständige Payment-QR-Code-Standards** und extrahiert deren Zahlungsfelder automatisch in die Dokumenten-API-Antwort. Kunden müssen diese QR-Strings nicht mehr manuell dekodieren — jeder Standard liefert ein eigenes Feldpräfix (z. B. `swissqr_*`, `girocode_*`), damit die Werte direkt in Matching, Validierung und Export einfließen.

| # | Standard | Region | Feldpräfix | Typischer Einsatz |
|---|----------|--------|------------|-------------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Schweiz | `swissqr_*` | Jede Schweizer Rechnung seit 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | SEPA-Zahlungen |
| 3 | [SPAYD / SPD](spayd.md) | CZ, teilweise SK | `spayd_*` | Standard der tschechischen Bankenvereinigung |
| 4 | [PagoPA](pagopa.md) | IT (öffentliche Verwaltung) | `pagopa_*` | Pflicht auf italienischen PA-Rechnungen |
| 5 | [Krypto-Payment-URIs](crypto-uris.md) | Weltweit (Krypto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK u. a. | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Saudi-Arabien | `zatca_*` | Pflicht auf jeder KSA-Rechnung |

**Die Erkennung erfolgt automatisch.** Jeder dekodierte QR-String wird auf sein Magic-Präfix geprüft (z. B. `SPC\n0200` für Swiss QR Bill v2.0 oder `PAGOPA|002|` für PagoPA); nur erkannte Standards werden in strukturierte Felder überführt.

### **Verwandte Seiten**

[Barcode-Extraktion – Details](bar-code-extractions.md)
