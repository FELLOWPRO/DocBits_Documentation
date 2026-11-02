# Panoramica della mappatura dei campi ZUGFeRD

## Introduzione {#einfuhrung}

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) è uno standard tedesco di fatturazione elettronica basato su UN/CEFACT Cross Industry Invoice (CII) e sullo standard ISO 19005-3 (PDF/A-3). Consente lo scambio di dati strutturati delle fatture all’interno di un file PDF.

DocBits estrae i campi dai documenti ZUGFeRD e li confronta con i sistemi ERP Infor (M3, LN) utilizzando gli standard OAGIS BOD.

## Versioni ZUGFeRD supportate {#unterstutzte-zugferd-versionen}

DocBits supporta diverse versioni dello standard ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Mappatura completa dei campi di intestazione {#vollstandige-header-feldzuordnung}

### Identificazione della fattura

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Codice tipo fattura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data di emissione della fattura |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Invoice notes |

### Tipo e sottotipo del documento (gestito da TRA)

> La stessa logica si applica a **Factur-X** — Factur-X 1.x utilizza lo stesso vocabolario CII di ZUGFeRD 2.x, quindi il blocco dinamico riportato di seguito viene emesso per entrambi.

Oltre a `INVOICE_TYPE_CODE` grezzo, l'XSLT di TRANSFORMATION predefinito emette un albero `<INVOICE>` canonico con due campi derivati:

| Campo DocBits | Sorgente | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (oppure `HeaderExchangedDocument/TypeCode` per ZUGFeRD 1.0) | UNCL 1001 `381` o `261` → **Credit Note**; qualsiasi altro codice → **Invoice** |
| `INVOICE_SUB_TYPE` | Presenza di `BuyerOrderReferencedDocument/IssuerAssignedID` (sotto `ApplicableHeaderTradeAgreement` per 2.x / `ApplicableSupplyChainTradeAgreement` per 1.0) | Non vuoto → **Fattura d'acquisto**; vuoto/assente → **Fattura costi** |

`INVOICE_SUB_TYPE` distingue le fatture collegate a un ordine d'acquisto dalle fatture di costo dirette ai fini dell'instradamento AP.

### Riferimenti dei documenti

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numero dell'ordine di acquisto |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Riferimento della bolla di consegna |

### Date

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice date |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Data di consegna/spedizione |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Data di scadenza del pagamento |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Inizio del periodo di fatturazione |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Fine del periodo di fatturazione |

### Informazioni sul fornitore (venditore)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Numero di posizione globale |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Address line 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | VAT registration number |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Informazioni sull’acquirente

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Numero di posizione globale |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | VAT ID |

### Informazioni di pagamento

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Descrizione dei termini di pagamento |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Codice del metodo di pagamento |

### Valuta e importi (intestazione)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Importo netto totale |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Importo totale dell'imposta |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Amount due |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Prepaid amount |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total allowances |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total charges |

### Ripartizione fiscale (classificata per fascia)

L'XSLT di TRANSFORMATION predefinito distribuisce i blocchi `ApplicableTradeTax` su tre fasce basate sull'aliquota anziché su indici posizionali. Ogni blocco viene assegnato a una fascia in base al suo `RateApplicablePercent`:

| Fascia | Campi DocBits | Regola di selezione |
| :--- | :--- | :--- |
| Fascia 1 (Standard) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | aliquota ≥ 19 |
| Fascia 2 (Ridotta) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < aliquota < 19 |
| Fascia 3 (Zero) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | aliquota = 0 |

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (fascia 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Percentuale IVA aliquota standard |
| `ApplicableTradeTax/BasisAmount` (fascia 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Importo netto aliquota standard |
| `ApplicableTradeTax/CalculatedAmount` (fascia 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Importo imposta aliquota standard |
| `ApplicableTradeTax/RateApplicablePercent` (fascia 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Percentuale IVA aliquota ridotta |
| `ApplicableTradeTax/BasisAmount` (fascia 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Importo netto aliquota ridotta |
| `ApplicableTradeTax/CalculatedAmount` (fascia 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Importo imposta aliquota ridotta |
| `ApplicableTradeTax/RateApplicablePercent` (fascia 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Percentuale IVA aliquota zero |
| `ApplicableTradeTax/BasisAmount` (fascia 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Importo netto ad aliquota zero |
| `ApplicableTradeTax/CalculatedAmount` (fascia 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Importo imposta aliquota zero |

## Mappatura completa delle voci di riga (tabella)

### Identificazione della riga

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numero dell'articolo dell'acquirente |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Numero dell'articolo del venditore |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Global ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |

### Riferimenti della riga

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numero PO a livello di linea |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | PO line number |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Delivery line |

### Quantità e unità

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Codice unità di misura |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Numero di pacchi |

### Prezzi

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Prezzo unitario netto |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Prezzo unitario lordo |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Price basis quantity |

### Importi della riga

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Importo netto della riga |

### Imposte della riga

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | VAT rate |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Codice tipo imposta |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Tax category |

### Sconti e addebiti (riga)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Discount amount |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Discount percentage |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Surcharge amount |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Motivo dell'indennità |

### Campi aggiuntivi della riga

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Paese d'origine |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Product characteristic |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Data di consegna della linea |

## Regole effettivamente utilizzate e attivazione

Se una nota di credito elettronica appare come Invoice, seguite la [guida alla diagnosi della classificazione](../credit-note-recognized-as-invoice.md). Descrive la sorgente personalizzata o predefinita effettivamente utilizzata, i codici del tipo, Extraction Paths e l’attivazione in sicurezza.

## Guide per paese

Consultate le guide per paese per le etichette esatte dei formati, la sintassi, i limiti delle versioni e lo stato di configurazione esaminato. [Formati eDocs, versioni e guide per paese](../supported-electronic-documents/README.md).
