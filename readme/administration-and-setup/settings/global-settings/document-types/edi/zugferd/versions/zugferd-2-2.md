# Mappatura dei campi ZUGFeRD 2.2

## Panoramica

ZUGFeRD 2.2 prosegue l'allineamento con EN 16931 e recepisce ulteriori aggiornamenti dello standard CII.

## Mappatura dei campi di intestazione

### Identificazione della fattura

| Percorso CII di ZUGFeRD | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Numero di fattura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data di emissione della fattura |

### Tipo e sottotipo di documento (gestiti da TRA)

L'XSLT di TRANSFORMATION predefinito genera due campi derivati:

| Campo DocBits | Origine | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` o `261` → **Credit Note**; qualsiasi altro codice → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Valorizzato → **Purchase Invoice**; vuoto o assente → **Cost Invoice** |

### Ripartizione fiscale (classificata per fascia)

I blocchi `ApplicableTradeTax` vengono distribuiti su tre fasce basate sull'aliquota (non su indici posizionali): i campi per l'aliquota standard (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) raccolgono le aliquote ≥ 19; i campi per l'aliquota ridotta (`*_2`) raccolgono 0 < aliquota < 19; i campi per l'aliquota zero (`*_3`) raccolgono aliquota = 0. Per l'elenco completo dei campi consulta [Ripartizione fiscale di ZUGFeRD](../README.md#ripartizione-fiscale-classificata-per-fascia).

### Valuta e importi

| Percorso CII di ZUGFeRD | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Valuta della fattura |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Totale netto |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Totale imposte |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Totale complessivo |

## Mappatura delle righe

| Percorso CII di ZUGFeRD | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Numero di riga |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descrizione dell'articolo |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantità fatturata |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Prezzo unitario netto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Totale della riga |
