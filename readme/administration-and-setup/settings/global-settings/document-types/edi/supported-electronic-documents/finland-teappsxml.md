---
description: Finland TEAPPSXML electronic document support in DocBits
---

# 🇫🇮 Finland TEAPPSXML

| Property | Value |
|----------|-------|
| **Country / Region** | Finland |
| **Document Types** | Invoice, Credit Note |
| **Format** | XML |
| **Standard** | TEAPPSXML 3.0 (Tieto / Finnish Banking) |
| **Locale** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) is a Finnish electronic invoice standard used primarily in the banking and financial sector. The root element is `<TEAPPSXML>` with the namespace `urn:TEAPPSXML:3.0`. DocBits detects TEAPPSXML documents by the presence of `xmlns="urn:TEAPPSXML:` in the root element.

The TEAPPSXML format uses upper-case element names and a flat structure with separate `<SENDER>`, `<RECEIVER>`, `<INVOICE>`, and `<PAYMENTINFO>` sections. The Finnish Business ID (Y-tunnus) format is `1234567-8`, and VAT numbers use the prefix `FI` (e.g. `FI12345678`).

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="finland-teappsxml-preview.png" alt="Finland TEAPPSXML invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Finland TEAPPSXML invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Invoice number |
| `invoice_date` | `INVOICE/INVOICEDATE` | Issue date (YYYY-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Payment due date (YYYY-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Message type (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Currency code (typically `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Payment reference number |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Finnish payment reference (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Net amount excl. VAT |
| `tax_amount` | `INVOICE/TOTALVAT` | Total VAT amount |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Total amount incl. VAT |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Payment method (e.g. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Sender company name |
| `supplier_id` | `SENDER/ID` | Finnish Business ID (Y-tunnus, e.g. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | VAT number (e.g. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Sender street address |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Sender city |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Sender postal code |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | ISO country code (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Sender bank BIC code |
| `buyer_name` | `INVOICE/BUYER/NAME` | Buyer company name |
| `buyer_id` | `INVOICE/BUYER/ID` | Buyer Finnish Business ID |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Buyer street address |
| `buyer_city` | `INVOICE/BUYER/CITY` | Buyer city |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Buyer postal code |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | ISO country code (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | Beneficiary IBAN |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Beneficiary BIC code |

### Line Item Table (`INVOICE_TABLE`)

Row path: `INVOICE/LINES/LINE`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | `LINENUMBER` | Line sequence number |
| `DESCRIPTION` | `ARTICLENAME` | Article name / description |
| `QUANTITY` | `QUANTITY` | Invoiced quantity |
| `UNIT` | `UNIT` | Unit of measure (e.g. `KPL` = piece) |
| `UNIT_PRICE` | `UNITPRICE` | Unit price excl. VAT |
| `VAT_RATE` | `VATRATE` | VAT rate in % (standard 25.5%) |
| `VAT` | Calculated | VAT amount per line |
| `NET_AMOUNT` | `LINEAMOUNT` | Line total excl. VAT |

## Classification Rule

DocBits detects TEAPPSXML documents by matching the `xmlns` attribute on the root `<TEAPPSXML>` element:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| TEAPPSXML | `xmlns` contains `urn:TEAPPSXML:` |

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Finland Finvoice](./finland-finvoice.md)
- [Supported Electronic Documents](./)
