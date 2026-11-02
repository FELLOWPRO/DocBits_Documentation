---
description: Finland Finvoice (1.3, 2.0, 2.01, 3.0) electronic document support in DocBits
---

# 🇫🇮 Finland Finvoice

| Property | Value |
|----------|-------|
| **Country / Region** | Finland |
| **Document Types** | Invoice (Lasku), Credit Note (Hyvityslasku) |
| **Format** | XML |
| **Standard** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Locale** | `fi_FI` |

Finvoice is the Finnish banking sector's e-invoicing standard, developed and maintained by Finance Finland (Finanssiala ry). It is used for both B2B and B2G invoicing and is transmitted via the Finnish banking infrastructure. The root element is `<Finvoice>` with a versioned namespace URL. DocBits detects the version via the `xmlns` attribute:

| Version | Namespace URL |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

The Finnish Business ID (Y-tunnus) format is `1234567-8` (7 digits + check digit), used as the party identifier. The VAT number has the prefix `FI` followed by 8 digits (e.g. `FI12345678`). Dates are encoded in `CCYYMMDD` format.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="finland-finvoice-preview.png" alt="Finland Finvoice 3.0 invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Finland Finvoice 3.0 invoice (Lasku)</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Invoice number |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Date in `CCYYMMDD` format, converted to ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Payment due date (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Invoice, CRE01=Credit Note |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Currency code (typically `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Net amount excl. VAT |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Total VAT amount |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Total amount incl. VAT |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | VAT rate in % (standard 25.5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Seller company name |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Finnish Business ID (Y-tunnus, e.g. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | VAT number (e.g. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Seller street address |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Seller city |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Seller postal code |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | ISO country code (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Buyer company name |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Finnish Business ID (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Buyer street address |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Buyer city |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Buyer postal code |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | ISO country code (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | Payee IBAN (EPI payment details) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | BIC/SWIFT code |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Free-text payment terms |

### Line Item Table (`INVOICE_TABLE`)

Row path: `InvoiceRow`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Article / product code |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Article name / description |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Delivered quantity |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Unit code (e.g. `KPL` = piece) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Unit price excl. VAT |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | VAT rate in % per line |
| `VAT` | `InvoiceRow/RowVatAmount` | VAT amount per line |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Line total excl. VAT |

## Classification Rules

DocBits detects Finvoice documents by matching the `xmlns` attribute on the root `<Finvoice>` element:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` contains `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` contains `http://www.finvoice.fi/schema/finvoice20` (not 2.01) |
| FINVOICE 2.01 | `xmlns` contains `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` contains `http://www.finvoice.fi/schema/finvoice30` |

Classification uses the **first-match-wins** principle with more specific patterns (2.01) evaluated before the generic 2.0.

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Finland TEAPPSXML](./finland-teappsxml.md)
- [Supported Electronic Documents](./)
