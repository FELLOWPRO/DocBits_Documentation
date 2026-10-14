# Transformation file and Mapping

## 1. **Purpose**

This file is responsible for extracting data from a PEPPOL BIS Billing 3.0 XML file, processing it, and saving the relevant information in a specified format. It is designed to enable the extraction of key fields to facilitate further processing or integration into DocBits.

## 2. **Overview**

* **Source File**: The input is a PEPPOL XML file that follows the PEPPOL BIS Billing 3.0 standard.
* **Extraction Process**: The file performs a series of steps to read, parse, and extract key elements such as invoice details, supplier information, amounts, and dates.
* **Output**: The extracted data is stored in a structured format, in another XML file.

## _**3.**_**&#x20;Download** **the PEPPOL XML Transformation File.**

* Example: _This file contains the PEPPOL XML transformation logic for extracting and saving data to another XML file._
* If you encounter issues with your current file or it becomes unusable, download this backup version to restore the transformation functionality.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Here is the Mapping:

<details>

<summary>AccountingSupplierParty Information Mapping </summary>



* **Supplier Electronic Address**
  * **Source**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Can Appear Multiple Times**: No.
* **Supplier Electronic Address Scheme ID**
  * **Source**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Mapped To**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Can Appear Multiple Times**: No.
* **Supplier Identification**
  * **Source**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Can Appear Multiple Times**: Each `<PartyIdentification>` element under `Supplier` will be extracted.
* **Supplier Identification Scheme ID**
  * **Source**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapped To**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Can Appear Multiple Times**: Each `<PartyIdentification>` element will have its corresponding scheme ID.
* **Supplier Name**
  * **Source**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><NAME>`
  * **Can Appear Multiple Times**: No.
* **Supplier Address Line 1**
  * **Source**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Can Appear Multiple Times**: No.
* **Supplier Address Line 2**
  * **Source**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Can Appear Multiple Times**: No.
* **Supplier Address Line 3**
  * **Source**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapped To**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Can Appear Multiple Times**: No.
* **Supplier VAT ID**
  * **Source**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Can Appear Multiple Times**: No.
* **Supplier Tax Scheme**
  * **Source**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Can Appear Multiple Times**: No.
* **Supplier Legal Name**
  * **Source**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Can Appear Multiple Times**: No.
* **Supplier Legal ID**
  * **Source**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Can Appear Multiple Times**: No.
* **Supplier Legal ID Scheme ID**
  * **Source**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapped To**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Can Appear Multiple Times**: No.
* **Supplier Legal Form**
  * **Source**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Can Appear Multiple Times**: No.
* **Supplier Post Code**
  * **Source**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Can Appear Multiple Times**: No.
* **Supplier City**
  * **Source**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><CITY>`
  * **Can Appear Multiple Times**: No.
* **Supplier Country Subentity**
  * **Source**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Can Appear Multiple Times**: No.
* **Supplier Country Code**
  * **Source**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Can Appear Multiple Times**: No.
* **Supplier Contact Name**
  * **Source**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Can Appear Multiple Times**: No.
* **Supplier Contact Telephone**
  * **Source**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Can Appear Multiple Times**: No.
* **Supplier Contact Email**
  * **Source**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Mapped To**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Can Appear Multiple Times**: No.

</details>

<details>

<summary>AccountingCustomerParty Information Mapping</summary>



* **Buyer Electronic Address**
  * **Source**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Mapped To**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Can Appear Multiple Times**: No.
* **Buyer Electronic Address Scheme ID**
  * **Source**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Mapped To**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Can Appear Multiple Times**: No.
* **Buyer Identification**
  * **Source**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Mapped To**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Can Appear Multiple Times**: Each `<PartyIdentification>` element under `Buyer` will be extracted.
* **Buyer Identification Scheme ID**
  * **Source**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapped To**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Can Appear Multiple Times**: Each `<PartyIdentification>` element will have its corresponding scheme ID.
* **Buyer Name**
  * **Source**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Mapped To**: `<INVOICE><BUYER><NAME>`
  * **Can Appear Multiple Times**: No.
* **Buyer Address Line 1**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Mapped To**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Can Appear Multiple Times**: No.
* **Buyer Address Line 2**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapped To**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Can Appear Multiple Times**: No.
* **Buyer Address Line 3**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapped To**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Can Appear Multiple Times**: No.
* **Buyer VAT ID**
  * **Source**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapped To**: `<INVOICE><BUYER><VAT_ID>`
  * **Can Appear Multiple Times**: No.
* **Buyer Tax Scheme**
  * **Source**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapped To**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Can Appear Multiple Times**: No.
* **Buyer Legal Name**
  * **Source**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapped To**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Can Appear Multiple Times**: No.
* **Buyer Legal ID**
  * **Source**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapped To**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Can Appear Multiple Times**: No.
* **Buyer Legal ID Scheme ID**
  * **Source**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapped To**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Can Appear Multiple Times**: No.
* **Buyer Legal Form**
  * **Source**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapped To**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Can Appear Multiple Times**: No.
* **Buyer Post Code**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Mapped To**: `<INVOICE><BUYER><POST_CODE>`
  * **Can Appear Multiple Times**: No.
* **Buyer City**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Mapped To**: `<INVOICE><BUYER><CITY>`
  * **Can Appear Multiple Times**: No.
* **Buyer Country Subentity**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapped To**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Can Appear Multiple Times**: No.
* **Buyer Country Code**
  * **Source**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapped To**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Can Appear Multiple Times**: No.
* **Buyer Contact Name**
  * **Source**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Mapped To**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Can Appear Multiple Times**: No.
* **Buyer Contact Telephone**
  * **Source**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Mapped To**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Can Appear Multiple Times**: No.
* **Buyer Contact Email**
  * **Source**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Mapped To**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Can Appear Multiple Times**: No.

</details>

<details>

<summary>PayeeParty Information Mapping</summary>



1. **Payee Identification**
   * **Source**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Mapped To**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Can Appear Multiple Times**: Each `<PartyIdentification>` element under `PayeeParty` will be extracted.
2. **Payee Identification Scheme ID**
   * **Source**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Mapped To**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Can Appear Multiple Times**: Each `<PartyIdentification>` element will have its corresponding scheme ID.
3. **Payee Name**
   * **Source**: `//PayeeParty/PartyName/Name/text()`
   * **Mapped To**: `<INVOICE><PAYEE><NAME>`
   * **Can Appear Multiple Times**: No.
4. **Payee Legal ID**
   * **Source**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Mapped To**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Can Appear Multiple Times**: No.
5. **Payee Legal ID Scheme ID**
   * **Source**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Mapped To**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Can Appear Multiple Times**: No.

</details>

<details>

<summary>TaxRepresentativeParty Information Mapping</summary>



* **Tax Representative Party Name**
  * **Source**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Address Line 1**
  * **Source**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Address Line 2**
  * **Source**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Address Line 3**
  * **Source**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative VAT ID**
  * **Source**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Tax Scheme**
  * **Source**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative City**
  * **Source**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Post Code**
  * **Source**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Country Subentity**
  * **Source**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Can Appear Multiple Times**: No.
* **Tax Representative Country Code**
  * **Source**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Mapped To**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Can Appear Multiple Times**: No.

</details>

<details>

<summary>General Invoice Information </summary>



1. **Invoice Type**
   * **Source**: `"Invoice"`
   * **Mapped To**: `<INVOICE><INVOICE_TYPE>`
   * **Can Appear Multiple Times**: No.
2. **Invoice Sub Type**
   * **Source**: `"Purchase Invoice"`
   * **Mapped To**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Can Appear Multiple Times**: No.
3. **Invoice ID**
   * **Source**: `//ID/text()`
   * **Mapped To**: `<INVOICE><INVOICE_ID>`
   * **Can Appear Multiple Times**: No.
4. **Invoice Type Code**
   * **Source**: `//InvoiceTypeCode/text()`
   * **Mapped To**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Can Appear Multiple Times**: No.
5. **Invoice Date**
   * **Source**: `normalize-space(//IssueDate/text())`
   * **Mapped To**: `<INVOICE><INVOICE_DATE>`
   * **Can Appear Multiple Times**: No.
   * **Processing**: Uses the `DateTimeString` template for formatting.
6. **Due Date**
   * **Source**: `normalize-space(//DueDate/text())`
   * **Mapped To**: `<INVOICE><DUE_DATE>`
   * **Can Appear Multiple Times**: No.
   * **Processing**: Uses the `DateTimeString` template for formatting.
7. **Tax Point Date**
   * **Source**: `normalize-space(//TaxPointDate/text())`
   * **Mapped To**: `<INVOICE><TAX_POINT_DATE>`
   * **Can Appear Multiple Times**: No.
   * **Processing**: Uses the `DateTimeString` template for formatting.
8. **Invoice Note**
   * **Source**: `//Note/text()`
   * **Mapped To**: `<INVOICE><INVOICE_NOTE>`
   * **Can Appear Multiple Times**: No.
9. **Document Currency Code**
   * **Source**: `//DocumentCurrencyCode/text()`
   * **Mapped To**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Can Appear Multiple Times**: No.
10. **Tax Currency Code**
    * **Source**: `//TaxCurrencyCode/text()`
    * **Mapped To**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Can Appear Multiple Times**: No.
11. **Accounting Cost**
    * **Source**: `//AccountingCost/text()`
    * **Mapped To**: `<INVOICE><ACCOUNTING_COST>`
    * **Can Appear Multiple Times**: No.
12. **Invoice Period Start Date**
    * **Source**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Mapped To**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Can Appear Multiple Times**: No.
    * **Processing**: Uses the `DateTimeString` template for formatting.
13. **Invoice Period End Date**
    * **Source**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Mapped To**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Can Appear Multiple Times**: No.
    * **Processing**: Uses the `DateTimeString` template for formatting.
14. **Invoice Period Description Code**
    * **Source**: `//InvoicePeriod/DescriptionCode/text()`
    * **Mapped To**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Can Appear Multiple Times**: No.
15. **Purchase Order Reference**
    * **Source**: `//OrderReference/ID/text()`
    * **Mapped To**: `<INVOICE><PURCHASE_ORDER>`
    * **Can Appear Multiple Times**: No.
16. **Sales Order Reference**
    * **Source**: `//OrderReference/SalesOrderID/text()`
    * **Mapped To**: `<INVOICE><SALES_ORDER>`
    * **Can Appear Multiple Times**: No.

</details>

<details>

<summary>Document References and Additional Document Details Mapping</summary>

1. **Buyer Reference**
   * **Source**: `//BuyerReference/text()`
   * **Mapped To**: `<INVOICE><BUYER_REFERENCE>`
   * **Can Appear Multiple Times**: No.

2)  **Billing Reference**

    * **Source**: `//BillingReference`
    * **Mapped To**: `<INVOICE><BILLING_REFERENCE>`
    * **Can Appear Multiple Times**: Yes. Each `<BillingReference>` element in the source data will generate a `<BILLING_REFERENCE>` element.

    **For each Billing Reference:**

    * **PRECEDING\_INVOICE\_NUMBER**
      * **Source**: `InvoiceDocumentReference/ID/text()`
      * **Mapped To**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Can Appear Multiple Times**: No.
    * **PRECEDING\_INVOICE\_ISSUE\_DATE**
      * **Source**: `InvoiceDocumentReference/IssueDate/text()`
      * **Mapped To**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Can Appear Multiple Times**: No.

3. **Despatch Document Reference**
   * **Source**: `//DespatchDocumentReference/ID/text()`
   * **Mapped To**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Can Appear Multiple Times**: No.

4) **Receipt Document Reference**
   * **Source**: `//ReceiptDocumentReference/ID/text()`
   * **Mapped To**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Can Appear Multiple Times**: No.

5. **Originator Document Reference**
   1. **Source**: `//OriginatorDocumentReference/ID/text()`
   2. **Mapped To**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Can Appear Multiple Times**: No.

#### Contract Document Reference

* **Source**: `//ContractDocumentReference/ID/text()`
* **Mapped To**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Can Appear Multiple Times**: No.

#### Project Reference

* **Source**: `//ProjectReference/ID/text()`
* **Mapped To**: `<INVOICE><PROJECT_REFERENCE>`
* **Can Appear Multiple Times**: No.

#### Additional Document Reference

* **Source**: `//AdditionalDocumentReference`
* **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Can Appear Multiple Times**: Yes. Each `<AdditionalDocumentReference>` element in the source data will generate an `<ADDITIONAL_DOCUMENT_REFERENCE>` element.

**For each Additional Document Reference:**

* **ID**
  * **Source**: `ID/text()`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Can Appear Multiple Times**: No.
* **SCHEME\_ID**
  * **Source**: `ID/@schemeID`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Can Appear Multiple Times**: No.
* **DOCUMENT\_TYPE\_CODE**
  * **Source**: `DocumentTypeCode/text()`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Can Appear Multiple Times**: No.
* **DOCUMENT\_DESCRIPTION**
  * **Source**: `DocumentDescription/text()`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Can Appear Multiple Times**: No.

**Attachment Information (for each Additional Document Reference):**

* **EMBEDDED\_DOCUMENT\_BINARY\_OBJECT**
  * **Source**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Can Appear Multiple Times**: No.
* **MIME\_CODE**
  * **Source**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Can Appear Multiple Times**: No.
* **FILENAME**
  * **Source**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Can Appear Multiple Times**: No.
* **EXTERNAL\_REFERENCE\_URL**
  * **Source**: `Attachment/ExternalReference/URI/text()`
  * **Mapped To**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Can Appear Multiple Times**: No.

</details>

