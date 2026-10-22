# Mapeamento de campos XRechnung 3.0.2 CII

## Visão geral

Este documento descreve o fluxo completo de mapeamento de campos do formato XRechnung 3.0.2 CII (Cross-Industry Invoice).

## 1. Estrutura XML CII

O XRechnung CII utiliza o formato UN/CEFACT Cross-Industry Invoice com os seguintes espaços de nomes:

| Prefixo | Espaço de nomes | Finalidade |
| :--- | :--- | :--- |
| `rsm` | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` | Root container |
| `ram` | `urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100` | Entidades de negócio |
| `qdt` | `urn:un:unece:uncefact:data:standard:QualifiedDataType:100` | Qualified types |
| `udt` | `urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100` | Unqualified types |

**Classification URN**: `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0.2`

## 2. XML CII → Extração de campos do DocBits

### Campos de cabeçalho

| Caminho XML CII | Campo do DocBits | Tipo de dados |
| :--- | :--- | :--- |
| `ExchangedDocument/ID` | `invoice_id` | String |
| `ExchangedDocument/TypeCode` | `invoice_type` | String |
| `ExchangedDocument/IssueDateTime/DateTimeString` | `invoice_date` | Data (YYYYMMDD) |
| `ApplicableHeaderTradeAgreement/BuyerReference` | `buyer_reference` | String |
| `BuyerOrderReferencedDocument/IssuerAssignedID` | `purchase_order` | String |
| `ActualDeliverySupplyChainEvent/.../DateTimeString` | `ship_date` | Date |
| `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString` | `due_date` | Date |
| `ApplicableHeaderTradeSettlement/InvoiceCurrencyCode` | `currency` | String |

### Classificação do tipo de documento

O XSLT de TRANSFORMATION substitui o valor numérico de `TypeCode` por um rótulo amigável antes que ele alcance `invoice_type`:

| Código UNCL 1001 | Significado | DocBits `invoice_type` |
| :--- | :--- | :--- |
| `381` / `261` | Nota de crédito / Nota de crédito autofaturada | **Credit Note** |
| Qualquer outro código (`380`, `383`, `384`, `386`, `389`, `325`, …) | Fatura / débito / proforma / etc. | **Invoice** |

### Campos do fornecedor

| Caminho XML CII | Campo do DocBits |
| :--- | :--- |
| `SellerTradeParty/ID` | `supplier_id` |
| `SellerTradeParty/Name` | `supplier_name` |
| `SellerTradeParty/PostalTradeAddress/LineOne` | `supplier_address` |
| `SellerTradeParty/PostalTradeAddress/CityName` | `supplier_city` |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `supplier_postal_code` |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `supplier_country` |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `supplier_vat` |
| `PayeePartyCreditorFinancialAccount/IBANID` | `iban` |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `bic` |

### Campos do cliente

| Caminho XML CII | Campo do DocBits |
| :--- | :--- |
| `BuyerTradeParty/ID` | `customer_id` |
| `BuyerTradeParty/Name` | `customer_name` |
| `BuyerTradeParty/PostalTradeAddress/LineOne` | `customer_address` |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `customer_vat` |

### Campos de valores

| Caminho XML CII | Campo do DocBits |
| :--- | :--- |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxBasisTotalAmount` | `net_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxTotalAmount` | `tax_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/GrandTotalAmount` | `total_amount` |
| `ApplicableTradeTax/RateApplicablePercent` | `tax_rate` |
| `ApplicableTradeTax/BasisAmount` | `taxable_amount` |

### Campos dos itens de linha

| Caminho XML CII | Coluna da tabela do DocBits |
| :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_NUMBER` |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` |
| `SpecifiedTradeProduct/SellerAssignedID` | `SELLER_ITEM_ID` |
| `SpecifiedTradeProduct/BuyerAssignedID` | `BUYER_ITEM_ID` |
| `SpecifiedLineTradeDelivery/BilledQuantity` | `QUANTITY` |
| `BilledQuantity/@unitCode` | `UNIT` |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` |
| `SpecifiedTradeSettlementLineMonetarySummation/LineTotalAmount` | `TOTAL_AMOUNT` |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT_RATE` |
| `ApplicableTradeTax/CategoryCode` | `VAT_CATEGORY` |

## 3. DocBits → Exportação Infor BOD (SyncSupplierInvoice)

### Mapeamento de cabeçalho

| Campo do DocBits | Caminho XML BOD |
| :--- | :--- |
| `INVOICE_NUMBER` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentID/ID` |
| `INVOICE_DATE` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentDateTime` |
| `VENDOR_ID` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/PartyIDs/ID` |
| `VENDOR_NAME` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/Name` |
| `TOTAL_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/TotalAmount` |
| `NET_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/ExtendedBaseAmount` |
| `TAX_AMOUNT` | (Calculado a partir de ExtendedAmount - ExtendedBaseAmount) |
| `CURRENCY` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/CurrencyExchangeRate/SourceCurrencyCode` |
| `PAYMENT_TERMS` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/PaymentTerm/Term/Description` |
| `PURCHASE_ORDER` | `UserArea/Property/NameValue[@name='PONumber']` |

### Mapeamento dos itens de linha

| Coluna do DocBits | Caminho XML BOD |
| :--- | :--- |
| `POSITION` | `SupplierInvoiceDetail/LineNumber` |
| `ITEM_NUMBER` | `SupplierInvoiceDetail/Item/ItemID/ID` |
| `DESCRIPTION` | `SupplierInvoiceDetail/Item/Description` |
| `QUANTITY` | `SupplierInvoiceDetail/InvoicedQuantity` |
| `UNIT` | `SupplierInvoiceDetail/InvoicedQuantity/@unitCode` |
| `UNIT_PRICE` | `SupplierInvoiceDetail/UnitPrice/Amount` |
| `TOTAL_AMOUNT` | `SupplierInvoiceDetail/ExtendedAmount` |
