# 转换文件和映射

## 1. **用途**

此文件用于从 PEPPOL BIS Billing 3.0 XML 文件中提取数据、处理数据，并以指定格式保存相关信息。它旨在提取关键字段，以便在 DocBits 中进一步处理或集成。

## 2. **概述**

* **源文件**：输入是符合 PEPPOL BIS Billing 3.0 标准的 PEPPOL XML 文件。
* **提取流程**：文件执行一系列步骤来读取、解析并提取关键元素，例如发票详细信息、供应商信息、金额和日期。
* **输出**：提取的数据以结构化格式存储在另一个 XML 文件中。

## _**3.**_**&#x20;下载** **PEPPOL XML 转换文件。**

* 示例：_此文件包含 PEPPOL XML 转换逻辑，用于提取数据并将其保存到另一个 XML 文件中。_
* 如果当前文件出现问题或无法使用，请下载此备份版本以恢复转换功能。

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### 以下是映射：

<details>

<summary>AccountingSupplierParty 信息映射 </summary>



* **供应商电子地址**
  * **源**：`//AccountingSupplierParty/Party/EndpointID/text()`
  * **映射到**：`<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **可出现多次**：否。
* **供应商电子地址方案 ID**
  * **源**：`//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **映射到**：`<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **可出现多次**：否。
* **供应商标识**
  * **源**：`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **映射到**：`<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **可出现多次**：将提取 `Supplier` 下的每个 `<PartyIdentification>` 元素。
* **供应商标识方案 ID**
  * **源**：`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **映射到**：`<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **可出现多次**：每个 `<PartyIdentification>` 元素都有相应的方案 ID。
* **供应商名称**
  * **源**：`//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **映射到**：`<INVOICE><SUPPLIER><NAME>`
  * **可出现多次**：否。
* **供应商地址行 1**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **映射到**：`<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **可出现多次**：否。
* **供应商地址行 2**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **映射到**：`<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **可出现多次**：否。
* **供应商地址行 3**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **映射到**：`<INVOICE><SUPPLIER><ADDRESS_LINE_3>`
  * **可出现多次**：否。
* **供应商 VAT ID**
  * **源**：`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **映射到**：`<INVOICE><SUPPLIER><VAT_ID>`
  * **可出现多次**：否。
* **供应商税务方案**
  * **源**：`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **映射到**：`<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **可出现多次**：否。
* **供应商法定名称**
  * **源**：`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **映射到**：`<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **可出现多次**：否。
* **供应商法定 ID**
  * **源**：`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **映射到**：`<INVOICE><SUPPLIER><LEGAL_ID>`
  * **可出现多次**：否。
* **供应商法定 ID 方案 ID**
  * **源**：`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **映射到**：`<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **可出现多次**：否。
* **供应商法律形式**
  * **源**：`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **映射到**：`<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **可出现多次**：否。
* **供应商邮政编码**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **映射到**：`<INVOICE><SUPPLIER><POST_CODE>`
  * **可出现多次**：否。
* **供应商城市**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **映射到**：`<INVOICE><SUPPLIER><CITY>`
  * **可出现多次**：否。
* **供应商国家子区域**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **映射到**：`<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **可出现多次**：否。
* **供应商国家代码**
  * **源**：`//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **映射到**：`<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **可出现多次**：否。
* **供应商联系人姓名**
  * **源**：`//AccountingSupplierParty/Party/Contact/Name/text()`
  * **映射到**：`<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **可出现多次**：否。
* **供应商联系电话**
  * **源**：`//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **映射到**：`<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **可出现多次**：否。
* **供应商联系电子邮件**
  * **源**：`//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **映射到**：`<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **可出现多次**：否。

</details>

<details>

<summary>AccountingCustomerParty 信息映射</summary>



* **买方电子地址**
  * **源**：`//AccountingCustomerParty/Party/EndpointID/text()`
  * **映射到**：`<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **可出现多次**：否。
* **买方电子地址方案 ID**
  * **源**：`//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **映射到**：`<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **可出现多次**：否。
* **买方标识**
  * **源**：`//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **映射到**：`<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **可出现多次**：将提取 `Buyer` 下的每个 `<PartyIdentification>` 元素。
* **买方标识方案 ID**
  * **源**：`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **映射到**：`<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **可出现多次**：每个 `<PartyIdentification>` 元素都有相应的方案 ID。
* **买方名称**
  * **源**：`//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **映射到**：`<INVOICE><BUYER><NAME>`
  * **可出现多次**：否。
* **买方地址行 1**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **映射到**：`<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **可出现多次**：否。
* **买方地址行 2**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **映射到**：`<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **可出现多次**：否。
* **买方地址行 3**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **映射到**：`<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **可出现多次**：否。
* **买方 VAT ID**
  * **源**：`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **映射到**：`<INVOICE><BUYER><VAT_ID>`
  * **可出现多次**：否。
* **买方税务方案**
  * **源**：`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **映射到**：`<INVOICE><BUYER><TAX_SCHEME>`
  * **可出现多次**：否。
* **买方法定名称**
  * **源**：`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **映射到**：`<INVOICE><BUYER><LEGAL_NAME>`
  * **可出现多次**：否。
* **买方法定 ID**
  * **源**：`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **映射到**：`<INVOICE><BUYER><LEGAL_ID>`
  * **可出现多次**：否。
* **买方法定 ID 方案 ID**
  * **源**：`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **映射到**：`<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **可出现多次**：否。
* **买方法律形式**
  * **源**：`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **映射到**：`<INVOICE><BUYER><LEGAL_FORM>`
  * **可出现多次**：否。
* **买方邮政编码**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **映射到**：`<INVOICE><BUYER><POST_CODE>`
  * **可出现多次**：否。
* **买方城市**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **映射到**：`<INVOICE><BUYER><CITY>`
  * **可出现多次**：否。
* **买方国家子区域**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **映射到**：`<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **可出现多次**：否。
* **买方国家代码**
  * **源**：`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **映射到**：`<INVOICE><BUYER><COUNTRY_CODE>`
  * **可出现多次**：否。
* **买方联系人姓名**
  * **源**：`//AccountingCustomerParty/Party/Contact/Name/text()`
  * **映射到**：`<INVOICE><BUYER><CONTACT><NAME>`
  * **可出现多次**：否。
* **买方联系电话**
  * **源**：`//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **映射到**：`<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **可出现多次**：否。
* **买方联系电子邮件**
  * **源**：`//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **映射到**：`<INVOICE><BUYER><CONTACT><EMAIL>`
  * **可出现多次**：否。

</details>

<details>

<summary>PayeeParty 信息映射</summary>



1. **收款方标识**
   * **源**：`//PayeeParty/PartyIdentification/ID/text()`
   * **映射到**：`<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **可出现多次**：将提取 `PayeeParty` 下的每个 `<PartyIdentification>` 元素。
2. **收款方标识方案 ID**
   * **源**：`//PayeeParty/PartyIdentification/ID/@schemeID`
   * **映射到**：`<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **可出现多次**：每个 `<PartyIdentification>` 元素都有相应的方案 ID。
3. **收款方名称**
   * **源**：`//PayeeParty/PartyName/Name/text()`
   * **映射到**：`<INVOICE><PAYEE><NAME>`
   * **可出现多次**：否。
4. **收款方法定 ID**
   * **源**：`//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **映射到**：`<INVOICE><PAYEE><LEGAL_ID>`
   * **可出现多次**：否。
5. **收款方法定 ID 方案 ID**
   * **源**：`//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **映射到**：`<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **可出现多次**：否。

</details>

<details>

<summary>TaxRepresentativeParty 信息映射</summary>



* **税务代表方名称**
  * **源**：`//TaxRepresentativeParty/PartyName/Name/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **可出现多次**：否。
* **税务代表方地址行 1**
  * **源**：`//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **可出现多次**：否。
* **税务代表方地址行 2**
  * **源**：`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **可出现多次**：否。
* **税务代表方地址行 3**
  * **源**：`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **可出现多次**：否。
* **税务代表方 VAT ID**
  * **源**：`//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **可出现多次**：否。
* **税务代表方税务方案**
  * **源**：`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **可出现多次**：否。
* **税务代表方城市**
  * **源**：`//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **可出现多次**：否。
* **税务代表方邮政编码**
  * **源**：`//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **可出现多次**：否。
* **税务代表方国家子区域**
  * **源**：`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **可出现多次**：否。
* **税务代表方国家代码**
  * **源**：`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **映射到**：`<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **可出现多次**：否。

</details>

<details>

<summary>发票一般信息 </summary>



1. **发票类型**
   * **源**：`"Invoice"`
   * **映射到**：`<INVOICE><INVOICE_TYPE>`
   * **可出现多次**：否。
2. **发票子类型**
   * **源**：`"Purchase Invoice"`
   * **映射到**：`<INVOICE><INVOICE_SUB_TYPE>`
   * **可出现多次**：否。
3. **发票 ID**
   * **源**：`//ID/text()`
   * **映射到**：`<INVOICE><INVOICE_ID>`
   * **可出现多次**：否。
4. **发票类型代码**
   * **源**：`//InvoiceTypeCode/text()`
   * **映射到**：`<INVOICE><INVOICE_TYPE_CODE>`
   * **可出现多次**：否。
5. **发票日期**
   * **源**：`normalize-space(//IssueDate/text())`
   * **映射到**：`<INVOICE><INVOICE_DATE>`
   * **可出现多次**：否。
   * **处理**：使用 `DateTimeString` 模板进行格式化。
6. **到期日**
   * **源**：`normalize-space(//DueDate/text())`
   * **映射到**：`<INVOICE><DUE_DATE>`
   * **可出现多次**：否。
   * **处理**：使用 `DateTimeString` 模板进行格式化。
7. **税款日期**
   * **源**：`normalize-space(//TaxPointDate/text())`
   * **映射到**：`<INVOICE><TAX_POINT_DATE>`
   * **可出现多次**：否。
   * **处理**：使用 `DateTimeString` 模板进行格式化。
8. **发票备注**
   * **源**：`//Note/text()`
   * **映射到**：`<INVOICE><INVOICE_NOTE>`
   * **可出现多次**：否。
9. **单据币种代码**
   * **源**：`//DocumentCurrencyCode/text()`
   * **映射到**：`<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **可出现多次**：否。
10. **税务币种代码**
    * **源**：`//TaxCurrencyCode/text()`
    * **映射到**：`<INVOICE><TAX_CURRENCY_CODE>`
    * **可出现多次**：否。
11. **会计成本**
    * **源**：`//AccountingCost/text()`
    * **映射到**：`<INVOICE><ACCOUNTING_COST>`
    * **可出现多次**：否。
12. **发票期间开始日期**
    * **源**：`normalize-space(//InvoicePeriod/StartDate/text())`
    * **映射到**：`<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **可出现多次**：否。
    * **处理**：使用 `DateTimeString` 模板进行格式化。
13. **发票期间结束日期**
    * **源**：`normalize-space(//InvoicePeriod/EndDate/text())`
    * **映射到**：`<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **可出现多次**：否。
    * **处理**：使用 `DateTimeString` 模板进行格式化。
14. **发票期间描述代码**
    * **源**：`//InvoicePeriod/DescriptionCode/text()`
    * **映射到**：`<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **可出现多次**：否。
15. **采购订单引用**
    * **源**：`//OrderReference/ID/text()`
    * **映射到**：`<INVOICE><PURCHASE_ORDER>`
    * **可出现多次**：否。
16. **销售订单引用**
    * **源**：`//OrderReference/SalesOrderID/text()`
    * **映射到**：`<INVOICE><SALES_ORDER>`
    * **可出现多次**：否。

</details>

<details>

<summary>单据引用和其他单据详细信息映射</summary>

1. **买方引用**
   * **源**：`//BuyerReference/text()`
   * **映射到**：`<INVOICE><BUYER_REFERENCE>`
   * **可出现多次**：否。

2)  **账单引用**

    * **源**：`//BillingReference`
    * **映射到**：`<INVOICE><BILLING_REFERENCE>`
    * **可出现多次**：是。源数据中的每个 `<BillingReference>` 元素都会生成一个 `<BILLING_REFERENCE>` 元素。

    **针对每个账单引用：**

    * **前序发票编号**
      * **源**：`InvoiceDocumentReference/ID/text()`
      * **映射到**：`<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **可出现多次**：否。
    * **前序发票开具日期**
      * **源**：`InvoiceDocumentReference/IssueDate/text()`
      * **映射到**：`<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **可出现多次**：否。

3. **发货单据引用**
   * **源**：`//DespatchDocumentReference/ID/text()`
   * **映射到**：`<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **可出现多次**：否。

4) **收货单据引用**
   * **源**：`//ReceiptDocumentReference/ID/text()`
   * **映射到**：`<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **可出现多次**：否。

5. **发起方单据引用**
   1. **源**：`//OriginatorDocumentReference/ID/text()`
   2. **映射到**：`<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **可出现多次**：否。

#### 合同单据引用

* **源**：`//ContractDocumentReference/ID/text()`
* **映射到**：`<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **可出现多次**：否。

#### 项目引用

* **源**：`//ProjectReference/ID/text()`
* **映射到**：`<INVOICE><PROJECT_REFERENCE>`
* **可出现多次**：否。

#### 其他单据引用

* **源**：`//AdditionalDocumentReference`
* **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **可出现多次**：是。源数据中的每个 `<AdditionalDocumentReference>` 元素都会生成一个 `<ADDITIONAL_DOCUMENT_REFERENCE>` 元素。

**针对每个其他单据引用：**

* **ID**
  * **源**：`ID/text()`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **可出现多次**：否。
* **方案 ID**
  * **源**：`ID/@schemeID`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **可出现多次**：否。
* **单据类型代码**
  * **源**：`DocumentTypeCode/text()`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **可出现多次**：否。
* **单据描述**
  * **源**：`DocumentDescription/text()`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **可出现多次**：否。

**附件信息（适用于每个其他单据引用）：**

* **嵌入式单据二进制对象**
  * **源**：`Attachment/EmbeddedDocumentBinaryObject/text()`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **可出现多次**：否。
* **MIME 代码**
  * **源**：`Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **可出现多次**：否。
* **文件名**
  * **源**：`Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **可出现多次**：否。
* **外部引用 URL**
  * **源**：`Attachment/ExternalReference/URI/text()`
  * **映射到**：`<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **可出现多次**：否。

</details>
