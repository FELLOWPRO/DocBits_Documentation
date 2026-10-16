# Mappatura ZUGFeRD 2.3.2

## Panoramica

ZUGFeRD 2.3.2 è una versione di manutenzione dello standard 2.3 e garantisce la compatibilità con i più recenti aggiornamenti CII.

## Mappatura dei campi di intestazione

### Identificazione della fattura

| Percorso CII di ZUGFeRD           | Campo DocBits    | Campo Infor BOD    | Tipo   | Descrizione                     |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------------------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Numero di fattura               |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Data di emissione della fattura |

### Tipo e sottotipo di documento (gestiti da TRA)

L'XSLT di TRANSFORMATION predefinito genera due campi derivati:

| Campo DocBits      | Origine                                                                                                    | Logica                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` o `261` → **Credit Note**; qualsiasi altro codice → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Valorizzato → **Purchase Invoice**; vuoto o assente → **Cost Invoice**          |

### Ripartizione fiscale (classificata per fascia)

I blocchi `ApplicableTradeTax` vengono distribuiti su tre fasce basate sull'aliquota (non posizionali `[1]`/`[2]`/`[3]`): i campi per l'aliquota standard (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) raccolgono le aliquote ≥ 19; i campi per l'aliquota ridotta (`*_2`) raccolgono 0 < aliquota < 19; i campi per l'aliquota zero (`*_3`) raccolgono aliquota = 0. Per l'elenco completo dei campi consulta [Ripartizione fiscale di ZUGFeRD](./#ripartizione-fiscale-classificata-per-fascia).

| Percorso CII di ZUGFeRD                               | Campo DocBits | Campo Infor BOD | Tipo   | Descrizione                                |
| ----------------------------------------------------- | ------------- | --------------- | ------ | ------------------------------------------ |
| `ApplicableTradeTax/RateApplicablePercent` (fascia 1) | `TAX_RATE`    | `TaxPercent`    | NUMBER | IVA con aliquota standard (≥ 19)           |
| `ApplicableTradeTax/BasisAmount` (fascia 1)           | `NET_AMOUNT`  | `TaxableAmount` | AMOUNT | Importo netto con aliquota standard        |
| `ApplicableTradeTax/CalculatedAmount` (fascia 1)      | `TAX_AMOUNT`  | `TaxAmount`     | AMOUNT | Importo dell'imposta con aliquota standard |

## Mappatura delle righe

| Percorso CII di ZUGFeRD                  | Campo DocBits  | Campo Infor BOD    | Tipo   | Descrizione               |
| ---------------------------------------- | -------------- | ------------------ | ------ | ------------------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | Numero di riga            |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | Descrizione dell'articolo |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | Quantità fatturata        |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | Prezzo unitario netto     |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | Totale della riga         |
