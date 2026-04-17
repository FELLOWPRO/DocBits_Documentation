---
description: Spain Facturae (3.2, 3.2.1, 3.2.2) electronic document support in DocBits
---

# 🇪🇸 Spain Facturae

| Property | Value |
|----------|-------|
| **Country / Region** | Spain |
| **Document Types** | Invoice (Factura), Credit Note |
| **Format** | XML |
| **Standard** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae is the Spanish mandatory e-invoice standard governed by the Agencia Estatal de Administración Tributaria (AEAT) and the Ministry of Finance. It is required for invoices to Spanish public-sector entities and widely used in B2B transactions. The root element is `<fe:Facturae>` with a versioned namespace URL. DocBits detects the version via the `xsi:schemaLocation` attribute, which references one of the official schema URLs:

| Version | Schema URL |
|---------|-----------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="spain-facturae-preview.png" alt="Spain Facturae invoice preview in DocBits"><figcaption><p>Default DocBits preview for a Spain Facturae 3.2.2 invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XML Element | Notes |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Invoice number |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Issue date (YYYY-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Payment due date |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Invoice, NC=Credit Note |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Always `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Buyer's order / contract reference |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Net amount excl. VAT |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Total VAT amount |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Total amount incl. VAT |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | VAT rate in % (standard 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Payment means code |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Seller company name |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (e.g. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | Spanish NIF or CIF tax ID |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Seller street address |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Seller city |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Seller postal code |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | ISO country code (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Buyer company name |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | Buyer NIF/CIF |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Buyer street address |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Buyer city |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Buyer postal code |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | ISO country code (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | Beneficiary IBAN |

### Line Item Table (`INVOICE_TABLE`)

Row path: `Invoices/Invoice/Items/InvoiceLine`

| Column | Source XML Element | Notes |
|---|---|---|
| `POSITION` | `ItemDescription` | Line sequence / description used as identifier |
| `DESCRIPTION` | `ItemDescription` | Item description |
| `QUANTITY` | `Quantity` | Invoiced quantity |
| `UNIT` | `UnitOfMeasure` | Unit of measure (e.g. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Unit price excl. VAT |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | VAT rate in % (typically 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | VAT amount per line |
| `NET_AMOUNT` | `TotalCost` | Line total excl. VAT |

## Classification Rules

DocBits detects Facturae documents by matching the `xsi:schemaLocation` attribute on the root `<fe:Facturae>` element:

| Electronic Document Type | Pattern |
|--------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` contains `Facturaev3_2.xml` (not 3_2_1 or 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` contains `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` contains `Facturaev3_2_2.xml` |

The root element is `<fe:Facturae>` with namespace `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (version-specific). Classification uses the **first-match-wins** principle, with more specific patterns (3.2.2, 3.2.1) matched before the generic 3.2.

## Related

- [Currently Supported E-Invoice Standards](../../currently-supported-e-invoice-standards/)
- [Supported Electronic Documents](./)
