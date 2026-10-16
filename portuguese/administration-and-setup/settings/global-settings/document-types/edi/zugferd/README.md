# ZUGFeRD Feldzuordnung Überblick

## Einführung

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) ist ein deutscher E-Invoicing-Standard, der auf der UN/CEFACT Cross Industry Invoice (CII) und dem ISO-Standard 19005-3 (PDF/A-3) basiert. Er ermöglicht den Austausch strukturierter Rechnungsdaten in einer PDF-Datei.

DocBits extrahiert Felder aus ZUGFeRD-Dokumenten und gleicht sie mit Infor ERP-Systemen (M3, LN) unter Verwendung von OAGIS BOD-Standards ab.

## Unterstützte ZUGFeRD-Versionen

DocBits unterstützt mehrere Versionen des ZUGFeRD-Standards:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Vollständige Header-Feldzuordnung

### Invoice Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Invoice type code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice issue date |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Invoice notes |

### Tipo e subtipo do documento (orientado pelo TRA)

> A mesma lógica se aplica ao **Factur-X** — Factur-X 1.x usa o mesmo vocabulário CII que o ZUGFeRD 2.x, então o bloco dinâmico abaixo é emitido para ambos.

Além do `INVOICE_TYPE_CODE` bruto, o XSLT de TRANSFORMATION padrão emite uma árvore `<INVOICE>` canônica com dois campos derivados:

| Campo DocBits | Origem | Lógica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (ou `HeaderExchangedDocument/TypeCode` para ZUGFeRD 1.0) | UNCL 1001 `381` ou `261` → **Credit Note**; qualquer outro código → **Invoice** |
| `INVOICE_SUB_TYPE` | Presença de `BuyerOrderReferencedDocument/IssuerAssignedID` (sob `ApplicableHeaderTradeAgreement` para 2.x / `ApplicableSupplyChainTradeAgreement` para 1.0) | Não vazio → **Purchase Invoice**; vazio/ausente → **Cost Invoice** |

`INVOICE_SUB_TYPE` diferencia faturas vinculadas a PO das faturas de custo direto para roteamento de AP.

### Document References

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Purchase order number |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note reference |

### Dates

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice date |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Delivery/ship date |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Payment due date |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Billing period start |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Billing period end |

### Supplier (Seller) Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Global Location Number |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Address line 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | VAT registration number |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Buyer Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Global Location Number |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | VAT ID |

### Payment Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Payment terms description |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Payment method code |

### Currency & Amounts (Header Level)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Total net amount |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Total tax amount |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Amount due |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Prepaid amount |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total allowances |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total charges |

### Detalhamento de impostos (classificado por faixa)

O XSLT de TRANSFORMATION padrão distribui os blocos `ApplicableTradeTax` em três faixas baseadas em alíquota, em vez de usar índices posicionais. Cada bloco é associado a uma faixa pelo seu `RateApplicablePercent`:

| Faixa | Campos DocBits | Regra de Seleção |
| :--- | :--- | :--- |
| Faixa 1 (Padrão) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | alíquota ≥ 19 |
| Faixa 2 (Reduzida) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < alíquota < 19 |
| Faixa 3 (Zero) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | alíquota = 0 |

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Percentual de IVA da faixa padrão |
| `ApplicableTradeTax/BasisAmount` (faixa 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Valor líquido da faixa padrão |
| `ApplicableTradeTax/CalculatedAmount` (faixa 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Valor do imposto da faixa padrão |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Percentual de IVA da faixa reduzida |
| `ApplicableTradeTax/BasisAmount` (faixa 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Valor líquido da faixa reduzida |
| `ApplicableTradeTax/CalculatedAmount` (faixa 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Valor do imposto da faixa reduzida |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Percentual de IVA da faixa zero |
| `ApplicableTradeTax/BasisAmount` (faixa 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Valor líquido com alíquota zero |
| `ApplicableTradeTax/CalculatedAmount` (faixa 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Valor do imposto da faixa zero |

## Mapeamento completo de itens de linha (tabela)

### Line Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Buyer's item number |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Seller's item number |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Global ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |

### Line References

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Line-level PO number |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | PO line number |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Delivery line |

### Quantities & Units

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Unit of measure code |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Number of packages |

### Pricing

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Gross unit price |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Price basis quantity |

### Line Amounts

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Line net amount |

### Line Tax

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | VAT rate |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Tax type code |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Tax category |

### Allowances & Charges (Line Level)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Discount amount |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Discount percentage |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Surcharge amount |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Reason for allowance |

### Additional Line Fields

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Country of origin |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Product characteristic |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Line delivery date |