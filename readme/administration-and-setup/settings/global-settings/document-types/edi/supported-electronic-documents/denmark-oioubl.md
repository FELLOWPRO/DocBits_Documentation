---
description: Denmark OIOUBL 2.1 electronic document support in DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Property | Value |
|----------|-------|
| **Country / Region** | Denmark |
| **Document Types** | Invoice (Faktura), Credit Note |
| **Format** | XML (UBL 2.1) |
| **Standard** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Locale** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) is the Danish e-invoicing standard based on UBL 2.1. It is mandatory for invoices to Danish public-sector entities and widely used in B2B transactions. DocBits detects OIOUBL 2.1 documents by the presence of `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. The profile identifier `urn:www.nesubl.eu:profiles:profile5:ver2.0` indicates the NES (Northern European Subset) invoice profile.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="denmark-oioubl-preview.png" alt="Denmark OIOUBL 2.1 invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Denmark OIOUBL 2.1 invoice (Faktura)</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `cbc:ID` | Invoice number |
| `invoice_date` | `cbc:IssueDate` | ISO 8601 issue date |
| `due_date` | `cbc:DueDate` | Payment due date |
| `invoice_type` | `cbc:InvoiceTypeCode` | UNCL 1001 code (380=Invoice, 381=Credit Note) |
| `currency` | `cbc:DocumentCurrencyCode` | Always `DKK` (Danish Krone) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Buyer's order reference number |
| `buyer_reference` | `cbc:BuyerReference` | Buyer's internal reference / EAN location number |
| `note` | `cbc:Note` | Free-text payment instructions or notes |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Net amount excl. VAT |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Total VAT amount (25% standard rate) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Total amount incl. VAT |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | VAT rate in % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Supplier company name |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR number (e.g. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | VAT/CVR number |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Supplier street address |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Supplier city |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Supplier postal code |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | ISO country code (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Customer company name |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR number |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | VAT/CVR number |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Customer street address |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Customer city |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Customer postal code |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | ISO country code (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Bank account / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | BIC/SWIFT code |

### Line Item Table (`INVOICE_TABLE`)

Row path: `cac:InvoiceLine`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | `cbc:ID` | Line sequence number |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Item name / description |
| `QUANTITY` | `cbc:InvoicedQuantity` | Invoiced quantity |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Unit price excl. VAT |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Line total excl. VAT |

## Classification Rule

DocBits detects OIOUBL 2.1 documents by matching the `CustomizationID` element:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

The root element is `<Invoice>` (or `<CreditNote>`) in the UBL 2.1 namespace `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Supported Electronic Documents](./)
