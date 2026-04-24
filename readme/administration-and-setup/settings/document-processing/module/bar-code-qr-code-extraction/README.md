# Estrazione di codici a barre / QR

## **Panoramica**

Questa funzione consente l'estrazione automatica di informazioni da **codici a barre e QR code** incorporati nei documenti. Si tratta di un'impostazione tutto-o-niente — abilitandola si attiva l'estrazione per entrambi i tipi.

## Come abilitare l'Estrazione di codici a barre / QR

Per abilitare la funzione, seguire questi passaggi:

1. **Aprire Impostazioni**:
   * Dalla dashboard, andare su **Impostazioni**.
   * Selezionare **Elaborazione documenti** e poi **Modulo**.
2. **Abilitare la funzione**:
   * Scorrere fino all'opzione **Estrazione di codici a barre / QR**.
   *   Spostare il cursore per abilitare l'estrazione.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Tipi di codice supportati**

DocBits supporta l'estrazione dei seguenti tipi di codice:

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

## Standard di QR code di pagamento

Oltre alla decodifica generica, DocBits riconosce **sette standard distinti di QR code di pagamento** e ne estrae automaticamente i campi nella risposta API del documento. I clienti non hanno più bisogno di decodificare manualmente queste stringhe — ogni standard fornisce un prefisso di campo dedicato (p. es. `swissqr_*`, `girocode_*`), in modo che i valori confluiscano direttamente in matching, validazione ed export.

| # | Standard | Regione | Prefisso campo | Uso tipico |
|---|----------|---------|----------------|------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Svizzera | `swissqr_*` | Ogni fattura svizzera dal 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | Pagamenti SEPA |
| 3 | [SPAYD / SPD](spayd.md) | CZ, parzialmente SK | `spayd_*` | Standard dell'Associazione Bancaria Ceca |
| 4 | [PagoPA](pagopa.md) | IT (PA) | `pagopa_*` | Obbligatorio sulle fatture della PA italiana |
| 5 | [URI di pagamento crypto](crypto-uris.md) | Globale (crypto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK e altri | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Arabia Saudita | `zatca_*` | Obbligatorio su ogni fattura KSA |

**La rilevazione è automatica.** Ogni stringa QR decodificata viene ispezionata per il suo prefisso magico (p. es. `SPC\n0200` per Swiss QR Bill v2.0 o `PAGOPA|002|` per PagoPA); solo gli standard riconosciuti vengono convertiti in campi strutturati.

### **Pagine correlate**

[Dettagli estrazione codici a barre](bar-code-extractions.md)
