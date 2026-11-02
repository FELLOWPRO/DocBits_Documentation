# ZUGFeRD 1.0 Field Mapping

## Overview

ZUGFeRD 1.0 was the initial version of the standard. While it is older, many documents still use this format. DocBits provides full support for extracting data from ZUGFeRD 1.0 XML files.

## Header Field Mapping

### Invoice Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Invoice type code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice issue date |

### Document Type & Sub-Type (TRA-driven)

Alongside the raw `INVOICE_TYPE_CODE`, the default TRANSFORMATION XSLT emits two derived fields. ZUGFeRD 1.0 uses the legacy CII vocabulary, so the XPaths differ from 2.x:

| DocBits Field | Source (1.0 schema) | Logic |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryDocument/HeaderExchangedDocument/TypeCode` | UNCL 1001 `381` or `261` → **Credit Note**; any other code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SpecifiedSupplyChainTradeTransaction/ApplicableSupplyChainTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non-empty → **Purchase Invoice**; empty/missing → **Cost Invoice** |

### Tax Breakdown (Tier-classified)

`ApplicableTradeTax` blocks are distributed across three rate-based tiers (not positional indexes): standard-rate fields (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capture rate ≥ 19; reduced-rate fields (`*_2`) capture 0 < rate < 19; zero-rate fields (`*_3`) capture rate = 0. See [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) for the full field list. (ZUGFeRD 1.0 uses the legacy CII vocabulary in its TRANSFORMATION XSLT, but the tier-selection rules above are identical to 2.x.)

### Document References

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Purchase order number |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note reference |

### Supplier (Seller) Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |

## Line Item Mapping

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Buyer's item number |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
