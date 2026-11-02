---
description: AUNZ PINT electronic document support in DocBits
---

# 🇦🇺 AUNZ PINT

| Property             | Value                                                            |
| -------------------- | ---------------------------------------------------------------- |
| **Country / Region** | Australia / New Zealand                                          |
| **Document Types**   | Invoice, Credit Note                                             |
| **Format**           | UBL 2.1 XML                                                      |
| **Standard**         | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale**           | `en_AU`                                                          |

AUNZ PINT is the Australian/New Zealand implementation of the Peppol International (PINT) invoice model. It defines a UBL 2.1-based invoice format tailored to the A-NZ regulatory requirements including ABN/NZBN identification, GST handling, and compliance with the A-NZ Peppol Authority specifications. DocBits supports both the standard Invoice and Credit Note document types under the `PINT A-NZ` electronic document type, as well as the Self-Billing variant.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/aunz-pint-preview.png" alt="AUNZ PINT invoice preview in DocBits"><figcaption><p>Default DocBits preview for an AUNZ PINT invoice</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field          | Source XPath (UBL 2.1)                                                                       | Notes                           |
| ---------------------- | -------------------------------------------------------------------------------------------- | ------------------------------- |
| `invoice_id`           | `cbc:ID`                                                                                     | Invoice number                  |
| `invoice_date`         | `cbc:IssueDate`                                                                              | ISO 8601 date                   |
| `due_date`             | `cbc:DueDate`                                                                                | Payment due date                |
| `currency`             | `cbc:DocumentCurrencyCode`                                                                   | Typically `AUD` or `NZD`        |
| `total_amount`         | `cbc:PayableAmount` (in `cac:LegalMonetaryTotal`)                                            | Total incl. GST                 |
| `net_amount`           | `cbc:TaxExclusiveAmount` (in `cac:LegalMonetaryTotal`)                                       | Subtotal excl. GST              |
| `tax_amount`           | `cbc:TaxAmount` (in `cac:TaxTotal`)                                                          | GST amount                      |
| `purchase_order`       | `cbc:BuyerReference`                                                                         | Buyer's PO reference            |
| `payment_terms`        | `cbc:Note` (in `cac:PaymentTerms`)                                                           | Free-text payment terms         |
| `supplier_name`        | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name`                               | Supplier company name           |
| `supplier_id`          | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID`                                       | ABN (schemeID 0151)             |
| `supplier_tax_id`      | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID`                     | ABN or GST number               |
| `supplier_street`      | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName`                     | Supplier street                 |
| `supplier_city`        | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName`                       | Supplier city                   |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone`                     | Supplier postal code            |
| `supplier_country`     | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO country code (`AU` or `NZ`) |
| `buyer_name`           | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name`                               | Buyer company name              |
| `buyer_id`             | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID`                                       | ABN/NZBN (schemeID 0151)        |
| `buyer_street`         | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName`                     | Buyer street                    |
| `buyer_city`           | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName`                       | Buyer city                      |
| `buyer_postal_code`    | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone`                     | Buyer postal code               |
| `buyer_country`        | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO country code                |
| `iban`                 | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID`                                          | Payment account ID              |

### Line Item Table (`INVOICE_TABLE`)

Row path: `cac:InvoiceLine`

| Column        | Source XPath (UBL 2.1)                           | Notes                                           |
| ------------- | ------------------------------------------------ | ----------------------------------------------- |
| `POSITION`    | `cbc:ID`                                         | Line number                                     |
| `DESCRIPTION` | `cac:Item/cbc:Description`                       | Product/service description                     |
| `QUANTITY`    | `cbc:InvoicedQuantity`                           | Quantity (unit code in `@unitCode`)             |
| `UNIT`        | `cbc:InvoicedQuantity/@unitCode`                 | Unit code (e.g. `C62` = one/piece, `EA` = each) |
| `UNIT_PRICE`  | `cac:Price/cbc:PriceAmount`                      | Unit price excl. GST                            |
| `VAT_RATE`    | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST rate in %                                   |
| `VAT`         | _(calculated from tax amount)_                   | GST amount per line                             |
| `NET_AMOUNT`  | `cbc:LineExtensionAmount`                        | Line total excl. GST                            |

## Classification Rules

DocBits detects PINT A-NZ documents by matching the `CustomizationID` element:

| Pattern                                  | Rule Type        | Electronic Document Type         |
| ---------------------------------------- | ---------------- | -------------------------------- |
| `urn:peppol.org:pint:billing-1@aunz`     | STRING\_CONTAINS | PINT A-NZ (Invoice)              |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING\_CONTAINS | PINT A-NZ (Self-Billing Invoice) |

Both patterns classify under the `PINT A-NZ` electronic document type. The root element is `<Invoice>` for standard invoices and `<CreditNote>` for credit notes.

### A-NZ Specific Features

* **ABN/NZBN identifiers**: Uses `schemeID="0151"` for Australian Business Numbers and New Zealand Business Numbers
* **GST tax**: Uses the `S` (Standard rated) tax category with the GST tax scheme
* **CustomizationID**: Must contain `@aunz` suffix to be classified as PINT A-NZ (vs. global PINT)

## Related

* [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
* [PINT A-NZ](pint-a-nz.md)
* [Supported Electronic Documents](./)
