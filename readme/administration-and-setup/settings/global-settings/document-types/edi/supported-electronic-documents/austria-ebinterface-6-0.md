---
description: AUSTRIA EBINTERFACE 6.0 electronic document support in DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.0

| Property | Value |
|----------|-------|
| **Country / Region** | Austria |
| **Document Types** | Invoice, Credit Note |
| **Format** | XML |
| **Standard** | ebInterface 6.0 |
| **Locale** | `de_AT` |

ebInterface 6.0 introduced alignment with the European standard EN 16931 while maintaining backward compatibility with Austrian-specific requirements. It supports the structured representation of invoice data including line items, tax details, and payment information. The namespace is `http://www.ebinterface.at/schema/6p0/`.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="austria-ebinterface-preview.png" alt="Austria ebInterface 6.0 invoice preview in DocBits"><figcaption><p>Default DocBits preview for an AUSTRIA EBINTERFACE 6.0 invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Invoice number |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601 date |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Payment due date |
| `delivery_date` | `eb:Delivery/eb:Date` | Delivery date |
| `currency` | `@eb:InvoiceCurrency` | Root attribute, always `EUR` for AT |
| `total_amount` | `eb:TotalGrossAmount` | Gross total incl. VAT |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Net taxable base |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | VAT amount |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Purchase order reference |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Free-text payment terms |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Biller company name |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Austrian UID (e.g. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Biller street address |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Biller city |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Biller postal code |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO country code |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | Biller email address |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Biller IBAN |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Recipient company name |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | Recipient UID |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Recipient street |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Recipient city |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Recipient postal code |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO country code |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Payment IBAN |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Payment BIC/SWIFT |

### Line Item Table (`INVOICE_TABLE`)

Row path: `eb:Details/eb:ItemList/eb:ListLineItem`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | Sequential index | 1-based line number |
| `DESCRIPTION` | `eb:Description` | Product/service description |
| `QUANTITY` | `eb:Quantity` | Numeric quantity |
| `UNIT` | `eb:Quantity/@eb:Unit` | Unit code (e.g. `STK` = piece) |
| `UNIT_PRICE` | `eb:UnitPrice` | Unit price excl. VAT |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | VAT rate in % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | VAT amount per line |
| `NET_AMOUNT` | `eb:LineItemAmount` | Line total excl. VAT |

## Classification Rule

DocBits detects AUSTRIA EBINTERFACE 6.0 documents by the namespace string:

```
http://www.ebinterface.at/schema/6p0/
```

## Related

- [Supported Electronic Documents](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
