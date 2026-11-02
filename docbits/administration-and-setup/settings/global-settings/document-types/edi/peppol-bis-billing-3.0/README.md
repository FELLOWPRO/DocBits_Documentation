# Peppol BIS Billing 3.0

### Overview

This section describes the implementation plan for importing and mapping data from XML files using the Peppol BIS Billing 3.0 schema. Peppol BIS Billing 3.0 was developed to standardize e-billing processes and ensure compliance with European standards.

### Objectives&#x20;

* Ensure full compliance with Peppol BIS Billing 3.0 specifications.
* Seamless integration of e-invoice data into our accounts payable system using DocBits.
* Improve data quality and processing efficiency.

### Scope&#x20;

The scope of this project is to map key elements of the Peppol BIS Billing 3.0 schema to our internal data structures. In particular, the mapping will cover the following areas:

* Vendor and Buyer details
* Invoice details&#x20;
* Invoice lines
* Payment instructions
* Tax and legal information

### Key elements and mapping

**Vendor information:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Electronic address of the vendor
  * cbc:Name: Trade name of the vendor
  * cbc:CompanyID: Legal registration number of the vendor
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Address details of the vendor

**Buyer information:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Electronic address of the buyer
  * cbc:Name: Trade name of the buyer
  * cbc:CompanyID: Legal registration number of the buyer
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Address details of the buyer

**Invoice details:**

* cbc:ID: Invoice number
* cbc:IssueDate: Issue date of the invoice
* cbc:DueDate: Invoice due date
* cbc:InvoiceTypeCode: Invoice type

**Invoice lines:**

* cac:InvoiceLine
  * cbc:ID: Invoice line number
  * cbc:InvoicedQuantity: Invoiced quantity
  * cbc:LineExtensionAmount: Line extension amount
  * cbc:Description: Description of the billing position
  * cac:Item
    * cbc:Name: Item name
    * cbc:SellerItemIdentification/cbc:ID: Item number of the vendor
  * cac:Price
    * cbc:PriceAmount: Price per unit
    * cbc:BaseQuantity: Base quantity for the price

**Payment instructions:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Code to identify the payment method
  * cbc:PaymentID: Payment identifier

**Tax information:**

* cac:TaxTotal
  * cbc:TaxAmount: Total tax amount
  * cac:TaxSubtotal: Details for each interim tax amount

### PDF preview for e-invoice

A PDF document is generated according to a standard layout with the imported fields in order to provide the user with a preview for reference purposes. Further customization of the PDF preview layout is possible but requires additional effort.
