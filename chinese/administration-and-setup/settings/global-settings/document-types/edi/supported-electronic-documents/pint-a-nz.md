---
description: DocBits 对 PINT A-NZ 电子文档的支持
---

# 🇦🇺 PINT A-NZ

| 属性                 | 值                                                               |
| -------------------- | ---------------------------------------------------------------- |
| **国家 / 地区**      | 澳大利亚 / 新西兰                                                |
| **文档类型**         | 发票、贷项通知单                                                  |
| **格式**             | UBL 2.1 XML                                                      |
| **标准**             | PINT A-NZ（澳大利亚-新西兰 Peppol 国际模型）                      |
| **区域设置**         | `en_AU`                                                          |

PINT A-NZ（澳大利亚-新西兰 Peppol 国际模型）是针对澳大利亚和新西兰地区本地化的 Peppol 发票规范。它在全球 PINT 模型的基础上扩展了 A-NZ 特定业务规则、税务类别（GST）和标识符方案（ABN、NZBN）。本页是技术参考，提供完整的字段映射。

## 支持状态

| 组件             | 状态        |
| ---------------- | ----------- |
| 预览             | ✅ 支持      |
| 字段提取         | ✅ 支持      |
| 转换             | ✅ 支持      |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/aunz-pint-preview.png" alt="DocBits 中的 PINT A-NZ 发票预览"><figcaption><p>PINT A-NZ 发票的默认 DocBits 预览</p></figcaption></figure>

## 字段映射

### 页眉字段

| DocBits 字段          | 源 XPath（UBL 2.1）                                                                    | 备注                           |
| --------------------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| `invoice_id`           | `cbc:ID`                                                                               | 发票编号                       |
| `invoice_date`         | `cbc:IssueDate`                                                                        | ISO 8601 日期                  |
| `due_date`             | `cbc:DueDate`                                                                          | 付款到期日                     |
| `currency`             | `cbc:DocumentCurrencyCode`                                                             | 通常为 `AUD` 或 `NZD`          |
| `total_amount`         | `cbc:PayableAmount`（位于 `cac:LegalMonetaryTotal` 中）                                | 含 GST 的总额                  |
| `net_amount`           | `cbc:TaxExclusiveAmount`（位于 `cac:LegalMonetaryTotal` 中）                           | 不含 GST 的小计                |
| `tax_amount`           | `cbc:TaxAmount`（位于 `cac:TaxTotal` 中）                                              | GST 金额                       |
| `purchase_order`       | `cbc:BuyerReference`                                                                   | 买方的采购订单参考信息         |
| `payment_terms`        | `cbc:Note`（位于 `cac:PaymentTerms` 中）                                               | 自由文本付款条款               |
| `supplier_name`        | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name`                        | 供应商公司名称                 |
| `supplier_id`          | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID`                                | ABN（schemeID 0151）           |
| `supplier_tax_id`      | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID`              | ABN 或 GST 编号                |
| `supplier_street`      | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName`              | 供应商街道地址                 |
| `supplier_city`        | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName`                | 供应商城市                     |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone`              | 供应商邮政编码                 |
| `supplier_country`     | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO 国家代码（`AU` 或 `NZ`）   |
| `buyer_name`            | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name`                        | 买方公司名称                   |
| `buyer_id`              | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID`                                | ABN/NZBN（schemeID 0151）      |
| `buyer_street`          | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName`              | 买方街道地址                   |
| `buyer_city`            | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName`                | 买方城市                       |
| `buyer_postal_code`     | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone`              | 买方邮政编码                   |
| `buyer_country`         | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO 国家代码                   |
| `iban`                  | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID`                                   | 付款账户 ID                    |

### 行项目表（`INVOICE_TABLE`）

行路径：`cac:InvoiceLine`

| 列            | 源 XPath（UBL 2.1）                           | 备注                                               |
| ------------- | --------------------------------------------- | -------------------------------------------------- |
| `POSITION`    | `cbc:ID`                                      | 行号                                               |
| `DESCRIPTION` | `cac:Item/cbc:Description`                    | 产品/服务描述                                     |
| `QUANTITY`    | `cbc:InvoicedQuantity`                        | 数量（单位代码位于 `@unitCode` 中）                |
| `UNIT`        | `cbc:InvoicedQuantity/@unitCode`              | 单位代码（例如 `C62` = 一件/个，`EA` = 每件）       |
| `UNIT_PRICE`  | `cac:Price/cbc:PriceAmount`                   | 不含 GST 的单价                                    |
| `VAT_RATE`    | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST 税率（%）                                  |
| `VAT`         | _(根据税额计算)_                               | 每行的 GST 金额                                   |
| `NET_AMOUNT`  | `cbc:LineExtensionAmount`                     | 不含 GST 的行总额                                 |

## 分类规则

DocBits 通过匹配 `CustomizationID` 元素来检测 PINT A-NZ 文档：

```
urn:peppol.org:pint:billing-1@aunz
```

对于自开票文档，匹配模式为：

```
urn:peppol.org:pint:selfbilling-1@aunz
```

两者都会归类为 `PINT A-NZ` 电子文档类型。

## 相关内容

* [AUNZ PINT](aunz-pint.md) — 概览和 A-NZ 特定功能
* [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — 自开票变体
* [Supported Electronic Documents](./)
