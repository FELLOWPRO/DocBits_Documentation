# Ekstrakcja kodów kreskowych / QR

## **Przegląd**

Ta funkcja umożliwia automatyczne wyodrębnianie informacji z **kodów kreskowych i kodów QR** osadzonych w dokumentach. Jest to ustawienie „wszystko albo nic" — włączenie aktywuje ekstrakcję dla obu typów.

## Jak włączyć Ekstrakcję kodów kreskowych / QR

Aby włączyć funkcję, wykonaj następujące kroki:

1. **Otwórz Ustawienia**:
   * Na pulpicie wybierz **Ustawienia**.
   * Wybierz **Przetwarzanie dokumentów**, a następnie **Moduł**.
2. **Włącz funkcję**:
   * Przewiń do opcji **Ekstrakcja kodów kreskowych / QR**.
   *   Przełącznik ustaw na włączony.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Obsługiwane typy kodów**

DocBits obsługuje ekstrakcję następujących typów kodów:

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

## Standardy płatniczych kodów QR

Oprócz ogólnego dekodowania kodów QR, DocBits rozpoznaje **siedem odrębnych standardów płatniczych kodów QR** i automatycznie wyodrębnia ich pola płatności do odpowiedzi API dokumentu. Klienci nie muszą już ręcznie dekodować tych ciągów — każdy standard ma własny prefiks pola (np. `swissqr_*`, `girocode_*`), dzięki czemu wartości trafiają bezpośrednio do matchingu, walidacji i eksportu.

| # | Standard | Region | Prefiks pola | Typowe zastosowanie |
|---|----------|--------|--------------|---------------------|
| 1 | [Szwajcarski QR Bill](swiss-qr-code.md) | Szwajcaria | `swissqr_*` | Każda szwajcarska faktura od 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | Płatności SEPA |
| 3 | [SPAYD / SPD](spayd.md) | CZ, częściowo SK | `spayd_*` | Standard Czeskiego Stowarzyszenia Banków |
| 4 | [PagoPA](pagopa.md) | IT (administracja publiczna) | `pagopa_*` | Obowiązkowy na fakturach PA we Włoszech |
| 5 | [Kryptowalutowe URI płatności](crypto-uris.md) | Globalnie (krypto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK i inne | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Arabia Saudyjska | `zatca_*` | Obowiązkowy na każdej fakturze KSA |

**Wykrywanie jest automatyczne.** Każdy zdekodowany ciąg QR jest sprawdzany pod kątem jego magicznego prefiksu (np. `SPC\n0200` dla szwajcarskiego QR Bill v2.0 lub `PAGOPA|002|` dla PagoPA); tylko rozpoznane standardy są analizowane do pól strukturalnych.

### **Powiązane strony**

[Szczegóły ekstrakcji kodów kreskowych](bar-code-extractions.md)
