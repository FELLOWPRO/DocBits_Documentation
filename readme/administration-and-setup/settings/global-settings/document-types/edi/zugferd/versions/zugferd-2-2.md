# ZUGFeRD 2.2 Field Mapping

## Overview

ZUGFeRD 2.2 continues the alignment with EN 16931 and incorporates further updates from the CII standard.

## Header Field Mapping

### Invoice Identification

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice issue date |

### Document Type & Sub-Type (TRA-driven)

The default TRANSFORMATION XSLT emits two derived fields:

| DocBits Field | Source | Logic |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` or `261` → **Credit Note**; any other code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Non-empty → **Purchase Invoice**; empty/missing → **Cost Invoice** |

### Tax Breakdown (Tier-classified)

`ApplicableTradeTax` blocks are distributed across three rate-based tiers (not positional indexes): standard-rate fields (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capture rate ≥ 19; reduced-rate fields (`*_2`) capture 0 < rate < 19; zero-rate fields (`*_3`) capture rate = 0. See [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) for the full field list.

### Currency & Amounts

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Total net amount |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Total tax amount |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |

## Line Item Mapping

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
