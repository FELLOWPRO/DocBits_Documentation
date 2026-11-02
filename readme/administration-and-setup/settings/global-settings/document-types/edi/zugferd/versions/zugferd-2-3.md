# ZUGFeRD 2.3 Field Mapping

## Overview

ZUGFeRD 2.3 is the latest major version, incorporating improvements for better interoperability and compliance with modern e-invoicing requirements.

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

### Payment Information

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |

### Tax Breakdown (Tier-classified)

`ApplicableTradeTax` blocks are distributed across three rate-based tiers (not positional indexes): standard-rate fields (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capture rate ≥ 19; reduced-rate fields (`*_2`) capture 0 < rate < 19; zero-rate fields (`*_3`) capture rate = 0. See [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) for the full field list.

## Line Item Mapping

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Net unit price |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
