# Mappatura dei campi ZUGFeRD 2.3.2

## Panoramica

ZUGFeRD 2.3.2 è stata la versione iniziale dello standard. Sebbene sia datata, molti documenti utilizzano ancora questo formato. DocBits offre il supporto completo per l'estrazione dei dati dai file XML ZUGFeRD 2.3.2.

## Mappatura dei campi di intestazione

### Identificazione della fattura

| Percorso ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Numero fattura |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Codice tipo fattura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data di emissione della fattura |

### Riferimenti ai documenti

| Percorso ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numero ordine di acquisto |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Riferimento contratto |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Riferimento bolla di consegna |

### Informazioni sul fornitore (venditore)

| Percorso ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | ID fornitore |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nome fornitore |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Indirizzo riga 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Codice postale |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Città |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Codice paese |

### Tipo e sottotipo del documento (gestito da TRA)

L'XSLT di TRANSFORMATION predefinito emette due campi derivati:

| Campo DocBits | Sorgente | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` o `261` → **Credit Note**; qualsiasi altro codice → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non vuoto → **Purchase Invoice**; vuoto/assente → **Cost Invoice** |

### Ripartizione fiscale (classificata per fascia)

I blocchi `ApplicableTradeTax` vengono distribuiti su tre fasce basate sull'aliquota (non sugli indici posizionali `[1]`/`[2]`/`[3]`): i campi ad aliquota standard (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) catturano aliquote ≥ 19; i campi ad aliquota ridotta (`*_2`) catturano 0 < aliquota < 19; i campi ad aliquota zero (`*_3`) catturano aliquota = 0. Vedi [Ripartizione fiscale ZUGFeRD](../README.md#tax-breakdown-tier-classified) per l'elenco completo dei campi.

| Percorso ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (fascia 1) | `TAX_RATE` | `TaxPercent` | NUMBER | IVA aliquota standard (≥ 19) |
| `ApplicableTradeTax/BasisAmount` (fascia 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Importo netto aliquota standard |
| `ApplicableTradeTax/CalculatedAmount` (fascia 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Importo imposta aliquota standard |

## Mappatura delle voci di riga

| Percorso ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrizione |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Numero di riga |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numero articolo dell'acquirente |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descrizione dell'articolo |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantità fatturata |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Prezzo unitario netto |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Totale riga |
