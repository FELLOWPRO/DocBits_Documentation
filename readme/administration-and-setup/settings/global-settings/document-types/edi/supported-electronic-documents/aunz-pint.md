---
description: DocBits 中对 AUNZ PINT 电子文档的支持
---

# 🇦🇺 AUNZ PINT

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [澳大利亚](countries/australia.md). 活动的格式系列名称没有固定的 PINT 发布版本号。请检查自定义标识和业务规范标识；网络送达需要单独的集成。
{% endhint %}

| 属性                   | 值                                                               |
| ---------------------- | ---------------------------------------------------------------- |
| **国家 / 地区**        | 澳大利亚 / 新西兰                                                |
| **文档类型**           | 发票、贷项通知单                                                 |
| **格式**               | UBL 2.1 XML                                                      |
| **标准**               | PINT A-NZ（澳大利亚—新西兰 Peppol 国际模型）                     |
| **区域设置**           | `en_AU`                                                          |

AUNZ PINT 是 Peppol 国际（PINT）发票模型在澳大利亚和新西兰的实现。它定义了一种基于 UBL 2.1 的发票格式，适用于 A-NZ 的监管要求，包括 ABN/NZBN 标识、GST 处理，以及符合 A-NZ Peppol 管理机构规范。DocBits 在 `PINT A-NZ` 电子文档类型下支持标准发票和贷项通知单文档类型，也支持自开票变体。

## 支持状态

| 组件     | 状态     |
| -------- | -------- |
| 预览     | ✅ 支持   |
| 字段提取 | ✅ 支持   |
| 转换     | ✅ 支持   |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/aunz-pint-preview.png" alt="DocBits 中的 AUNZ PINT 发票预览"><figcaption><p>AUNZ PINT 发票的默认 DocBits 预览</p></figcaption></figure>

## 字段映射 <a id="field-mapping"></a>

### 表头字段

| DocBits 字段         | 源 XPath（UBL 2.1）                                                                    | 说明                           |
| -------------------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| `invoice_id`         | `cbc:ID`                                                                               | 发票编号                       |
| `invoice_date`       | `cbc:IssueDate`                                                                        | ISO 8601 日期                  |
| `due_date`           | `cbc:DueDate`                                                                          | 付款到期日                     |
| `currency`           | `cbc:DocumentCurrencyCode`                                                             | 通常为 `AUD` 或 `NZD`          |
| `total_amount`       | `cbc:PayableAmount`（位于 `cac:LegalMonetaryTotal` 中）                                | 含 GST 的总额                  |
| `net_amount`         | `cbc:TaxExclusiveAmount`（位于 `cac:LegalMonetaryTotal` 中）                           | 不含 GST 的小计                |
| `tax_amount`         | `cbc:TaxAmount`（位于 `cac:TaxTotal` 中）                                              | GST 金额                       |
| `purchase_order`     | `cbc:BuyerReference`                                                                   | 买方采购订单参考号             |
| `payment_terms`      | `cbc:Note`（位于 `cac:PaymentTerms` 中）                                               | 自由文本付款条款               |
| `supplier_name`      | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name`                         | 供应商公司名称                 |
| `supplier_id`        | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID`                                 | ABN（schemeID 0151）           |
| `supplier_tax_id`    | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID`               | ABN 或 GST 编号                |
| `supplier_street`    | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName`               | 供应商街道                     |
| `supplier_city`      | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName`                  | 供应商城市                     |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone`              | 供应商邮政编码                 |
| `supplier_country`   | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO 国家代码（`AU` 或 `NZ`） |
| `buyer_name`         | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name`                         | 买方公司名称                   |
| `buyer_id`           | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID`                                 | ABN/NZBN（schemeID 0151）      |
| `buyer_street`       | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName`                | 买方街道                       |
| `buyer_city`         | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName`                  | 买方城市                       |
| `buyer_postal_code`  | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone`                | 买方邮政编码                   |
| `buyer_country`      | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO 国家代码                |
| `iban`               | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID`                                    | 付款账户 ID                    |

### 行项目表（`INVOICE_TABLE`）

行路径：`cac:InvoiceLine`

| 列            | 源 XPath（UBL 2.1）                           | 说明                                            |
| ------------- | --------------------------------------------- | ----------------------------------------------- |
| `POSITION`    | `cbc:ID`                                      | 行号                                            |
| `DESCRIPTION` | `cac:Item/cbc:Description`                    | 产品 / 服务说明                                 |
| `QUANTITY`    | `cbc:InvoicedQuantity`                        | 数量（单位代码位于 `@unitCode` 中）             |
| `UNIT`        | `cbc:InvoicedQuantity/@unitCode`              | 单位代码（例如 `C62` = 一件 / 个，`EA` = 每个） |
| `UNIT_PRICE`  | `cac:Price/cbc:PriceAmount`                   | 不含 GST 的单价                                 |
| `VAT_RATE`    | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST 税率（%）                                |
| `VAT`         | _(根据税额计算)_                               | 每行 GST 金额                                   |
| `NET_AMOUNT`  | `cbc:LineExtensionAmount`                     | 不含 GST 的行总额                               |

## 分类规则

DocBits 通过匹配 `CustomizationID` 元素来检测 PINT A-NZ 文档：

| 模式                                      | 规则类型         | 电子文档类型                   |
| ----------------------------------------- | ---------------- | ------------------------------ |
| `urn:peppol.org:pint:billing-1@aunz`      | STRING\_CONTAINS | PINT A-NZ（发票）              |
| `urn:peppol.org:pint:selfbilling-1@aunz`  | STRING\_CONTAINS | PINT A-NZ（自开票发票）        |

这两种模式都会归类到 `PINT A-NZ` 电子文档类型下。标准发票的根元素为 `<Invoice>`，贷项通知单的根元素为 `<CreditNote>`。

### A-NZ 特定功能

* **ABN/NZBN 标识符**：使用 `schemeID="0151"` 表示澳大利亚商业编号和新西兰商业编号
* **GST 税**：使用 `S`（标准税率）税务类别和 GST 税务方案
* **CustomizationID**：必须包含 `@aunz` 后缀，才能归类为 PINT A-NZ（而非全球 PINT）

## 相关内容

* [AUNZ PINT 自开票](aunz-pint-self-billing.md)
* [PINT A-NZ](pint-a-nz.md)
* [支持的电子文档](./)
