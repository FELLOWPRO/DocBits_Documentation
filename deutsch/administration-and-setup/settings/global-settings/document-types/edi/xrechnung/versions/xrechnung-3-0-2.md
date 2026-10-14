# XRechnung 3.0.2 CII Field Mapping

## Overview

This document describes the complete field mapping flow for XRechnung 3.0.2 CII (Cross-Industry Invoice) format.

## 1. CII XML Structure

XRechnung CII uses UN/CEFACT Cross-Industry Invoice format with these namespaces:

| Prefix | Namespace | Purpose |
| :--- | :--- | :--- |
| `rsm` | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` | Root container |
| `ram` | `urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100` | Business entities |
| `qdt` | `urn:un:unece:uncefact:data:standard:QualifiedDataType:100` | Qualified types |
| `udt` | `urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100` | Unqualified types |

**Classification URN**: `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0.2`

## 2. CII XML → DocBits Field Extraction

### Header Fields

| CII XML Path | DocBits Field | Data Type |
| :--- | :--- | :--- |
| `ExchangedDocument/ID` | `invoice_id` | String |
| `ExchangedDocument/TypeCode` | `invoice_type` | String |
| `ExchangedDocument/IssueDateTime/DateTimeString` | `invoice_date` | Date (YYYYMMDD) |
| `ApplicableHeaderTradeAgreement/BuyerReference` | `buyer_reference` | String |
| `BuyerOrderReferencedDocument/IssuerAssignedID` | `purchase_order` | String |
| `ActualDeliverySupplyChainEvent/.../DateTimeString` | `ship_date` | Date |
| `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString` | `due_date` | Date |
| `ApplicableHeaderTradeSettlement/InvoiceCurrencyCode` | `currency` | String |

### Dokumenttyp-Klassifizierung

Das TRANSFORMATION-XSLT ersetzt den numerischen `TypeCode`-Wert durch eine sprechende Bezeichnung, bevor er in `invoice_type` übernommen wird:

| UNCL-1001-Code | Bedeutung | DocBits `invoice_type` |
| :--- | :--- | :--- |
| `381` / `261` | Gutschrift / Selbst ausgestellte Gutschrift | **Credit Note** |
| Jeder andere Code (`380`, `383`, `384`, `386`, `389`, `325`, …) | Rechnung / Lastschrift / Proforma / etc. | **Invoice** |

### Supplier Fields

| CII XML Path | DocBits Field |
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

### Customer Fields

| CII XML Path | DocBits Field |
| :--- | :--- |
| `BuyerTradeParty/ID` | `customer_id` |
| `BuyerTradeParty/Name` | `customer_name` |
| `BuyerTradeParty/PostalTradeAddress/LineOne` | `customer_address` |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `customer_vat` |

### Amount Fields

| CII XML Path | DocBits Field |
| :--- | :--- |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxBasisTotalAmount` | `net_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxTotalAmount` | `tax_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/GrandTotalAmount` | `total_amount` |
| `ApplicableTradeTax/RateApplicablePercent` | `tax_rate` |
| `ApplicableTradeTax/BasisAmount` | `taxable_amount` |

### Line Item Fields

| CII XML Path | DocBits Table Column |
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

## 3. DocBits → Infor BOD Export (SyncSupplierInvoice)

### Header Mapping

| DocBits Field | BOD XML Path |
| :--- | :--- |
| `INVOICE_NUMBER` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentID/ID` |
| `INVOICE_DATE` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentDateTime` |
| `VENDOR_ID` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/PartyIDs/ID` |
| `VENDOR_NAME` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/Name` |
| `TOTAL_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/TotalAmount` |
| `NET_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/ExtendedBaseAmount` |
| `TAX_AMOUNT` | (Calculated from ExtendedAmount - ExtendedBaseAmount) |
| `CURRENCY` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/CurrencyExchangeRate/SourceCurrencyCode` |
| `PAYMENT_TERMS` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/PaymentTerm/Term/Description` |
| `PURCHASE_ORDER` | `UserArea/Property/NameValue[@name='PONumber']` |

### Line Item Mapping

| DocBits Column | BOD XML Path |
| :--- | :--- |
| `POSITION` | `SupplierInvoiceDetail/LineNumber` |
| `ITEM_NUMBER` | `SupplierInvoiceDetail/Item/ItemID/ID` |
| `DESCRIPTION` | `SupplierInvoiceDetail/Item/Description` |
| `QUANTITY` | `SupplierInvoiceDetail/InvoicedQuantity` |
| `UNIT` | `SupplierInvoiceDetail/InvoicedQuantity/@unitCode` |
| `UNIT_PRICE` | `SupplierInvoiceDetail/UnitPrice/Amount` |
| `TOTAL_AMOUNT` | `SupplierInvoiceDetail/ExtendedAmount` |
