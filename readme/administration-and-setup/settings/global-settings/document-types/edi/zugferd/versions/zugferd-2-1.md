# ZUGFeRD 2.1 (Factur-X 1.0) Field Mapping

## Overview

ZUGFeRD 2.1 is identical to the French standard Factur-X 1.0. It is fully compliant with EN 16931 and is widely used for cross-border transactions between Germany and France.

## Header Field Mapping

### Invoice Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Invoice type code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice issue date |

### Document Type & Sub-Type (TRA-driven)

Alongside the raw `INVOICE_TYPE_CODE`, the default TRANSFORMATION XSLT emits two derived fields:

| DocBits Field | Source | Logic |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` or `261` → **Credit Note**; any other code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non-empty → **Purchase Invoice**; empty/missing → **Cost Invoice** |

### Tax Breakdown (Tier-classified)

`ApplicableTradeTax` blocks are distributed across three rate-based tiers (not positional indexes): standard-rate fields (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capture rate ≥ 19; reduced-rate fields (`*_2`) capture 0 < rate < 19; zero-rate fields (`*_3`) capture rate = 0. See [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) for the full field list.

### Buyer Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |

## Line Item Mapping

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Seller's item number |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Unit of measure |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
