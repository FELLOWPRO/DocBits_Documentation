# Peppol BIS Billing 3.0

### 概述

本节介绍使用 Peppol BIS Billing 3.0 架构导入和映射 XML 文件数据的实施计划。Peppol BIS Billing 3.0 旨在统一电子账单流程，并确保符合欧洲标准。

### 目标&#x20;

* 确保完全符合 Peppol BIS Billing 3.0 规范。
* 使用 DocBits 将电子发票数据无缝集成到我们的应付账款系统中。
* 提高数据质量和处理效率。

### 范围&#x20;

本项目旨在将 Peppol BIS Billing 3.0 架构的关键元素映射到我们的内部数据结构。具体而言，映射将涵盖以下领域：

* 供应商和买方信息
* 发票信息&#x20;
* 发票行项目
* 付款说明
* 税务和法律信息

### 关键元素和映射

**供应商信息：**

* cac:AccountingSupplierParty
  * cbc:EndpointID：供应商的电子地址
  * cbc:Name：供应商的商号
  * cbc:CompanyID：供应商的法定注册号
  * cbc:StreetName、cbc:CityName、cbc:PostalZone：供应商的地址信息

**买方信息：**

* cac:AccountingCustomerParty
  * cbc:EndpointID：买方的电子地址
  * cbc:Name：买方的商号
  * cbc:CompanyID：买方的法定注册号
  * cbc:StreetName、cbc:CityName、cbc:PostalZone：买方的地址信息

**发票信息：**

* cbc:ID：发票编号
* cbc:IssueDate：发票开具日期
* cbc:DueDate：发票到期日
* cbc:InvoiceTypeCode：发票类型

**发票行项目：**

* cac:InvoiceLine
  * cbc:ID：发票行项目编号
  * cbc:InvoicedQuantity：开票数量
  * cbc:LineExtensionAmount：行项目金额
  * cbc:Description：账单项目说明
  * cac:Item
    * cbc:Name：项目名称
    * cbc:SellerItemIdentification/cbc:ID：供应商的项目编号
  * cac:Price
    * cbc:PriceAmount：单价
    * cbc:BaseQuantity：价格的基准数量

**付款说明：**

* cac:PaymentMeans
  * cbc:PaymentMeansCode：用于识别付款方式的代码
  * cbc:PaymentID：付款标识符

**税务信息：**

* cac:TaxTotal
  * cbc:TaxAmount：税额总计
  * cac:TaxSubtotal：各项税额小计的详细信息

### 电子发票 PDF 预览

系统会根据标准版式生成 PDF 文档，并填入已导入的字段，供用户预览参考。PDF 预览版式可以进一步自定义，但需要投入额外工作。
