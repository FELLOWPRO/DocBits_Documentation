---
description: PINT A-NZ electronic document support in DocBits
---

# 🇦🇺 PINT A-NZ

| Property             | Value                                                            |
| -------------------- | ---------------------------------------------------------------- |
| **Country / Region** | Australia / New Zealand                                          |
| **Document Types**   | Invoice, Credit Note                                             |
| **Format**           | UBL 2.1 XML                                                      |
| **Standard**         | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale**           | `en_AU`                                                          |

PINT A-NZ (Peppol International Model for Australia-New Zealand) is the localized Peppol invoice specification for the Australia/New Zealand region. It extends the global PINT model with A-NZ specific business rules, tax categories (GST), and identifier schemes (ABN, NZBN). This is the technical reference page with the complete field mapping.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/aunz-pint-preview.png" alt="PINT A-NZ invoice preview in DocBits"><figcaption><p>Default DocBits preview for a PINT A-NZ invoice</p></figcaption></figure>

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

## Classification Rule

DocBits detects PINT A-NZ documents by matching the `CustomizationID` element:

```
urn:peppol.org:pint:billing-1@aunz
```

For self-billing documents, the pattern is:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Both classify under the `PINT A-NZ` electronic document type.

## Related

* [AUNZ PINT](aunz-pint.md) — Overview and A-NZ specific features
* [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Self-billing variant
* [Supported Electronic Documents](./)
