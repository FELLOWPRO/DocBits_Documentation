---
description: "DocBits 支持的奥地利 ebInterface 6.1 电子文档"
---

# 🇦🇹 奥地利 EBINTERFACE 6.1

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [奥地利](countries/austria.md). 请将 XML 命名空间与已配置的版本匹配。不同的命名空间可能需要另一套映射。
{% endhint %}

| 属性 | 值 |
| -------------------- | -------------------- |
| **国家 / 地区** | 奥地利 |
| **文档类型** | 发票、贷项通知单 |
| **格式** | XML |
| **标准** | ebInterface 6.1 |
| **区域设置** | `de_AT` |

ebInterface 6.1 是奥地利电子发票标准的最新版本。它包含更新后的验证规则、对贷项通知单的改进支持，以及与 Peppol 网络更强的兼容性，便于跨境开票。命名空间为 `http://www.ebinterface.at/schema/6p1/`。

## 支持状态

| 组件 | 状态 |
| ---------------- | ----------- |
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/austria-ebinterface-preview.png" alt="DocBits 中的奥地利 ebInterface 6.1 发票预览"><figcaption><p>DocBits 中奥地利 EBINTERFACE 6.1 发票的默认预览</p></figcaption></figure>

## 字段映射

### 抬头字段

| DocBits 字段 | 源 XML 元素 | 备注 |
| ---------------------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| `invoice_id` | `eb:InvoiceNumber` | 发票编号 |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601 日期 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | 付款到期日 |
| `delivery_date` | `eb:Delivery/eb:Date` | 交付日期 |
| `currency` | `@eb:InvoiceCurrency` | 根属性；对于 AT 始终为 `EUR` |
| `total_amount` | `eb:TotalGrossAmount` | 含 VAT 的总金额 |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | 应税净额 |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | VAT 金额 |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | 采购订单引用 |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | 自由文本付款条款 |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | 开票方公司名称 |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | 奥地利 UID（例如 ATU12345678） |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | 开票方街道地址 |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | 开票方城市 |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | 开票方邮政编码 |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO 国家代码 |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | 开票方电子邮箱地址 |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | 开票方 IBAN |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | 收票方公司名称 |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | 收票方 UID |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | 收票方街道地址 |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | 收票方城市 |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | 收票方邮政编码 |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO 国家代码 |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | 付款 IBAN |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | 付款 BIC/SWIFT |

### 行项目表（`INVOICE_TABLE`）

行路径：`eb:Details/eb:ItemList/eb:ListLineItem`

| 列 | 源 XML 元素 | 备注 |
| ------------- | ---------------------------------- | ------------------------------ |
| `POSITION` | 顺序索引 | 从 1 开始的行号 |
| `DESCRIPTION` | `eb:Description` | 产品/服务描述 |
| `QUANTITY` | `eb:Quantity` | 数量值 |
| `UNIT` | `eb:Quantity/@eb:Unit` | 单位代码（例如 `STK` = 件） |
| `UNIT_PRICE` | `eb:UnitPrice` | 不含 VAT 的单价 |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | VAT 税率（%） |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | 每个行项目的 VAT 金额 |
| `NET_AMOUNT` | `eb:LineItemAmount` | 不含 VAT 的行项目总额 |

## 分类规则

DocBits 根据命名空间字符串检测奥地利 EBINTERFACE 6.1 文档：

```
http://www.ebinterface.at/schema/6p1/
```

## 相关内容

* [支持的电子文档](./)
* [奥地利 ebInterface](austria-ebinterface.md)
* [奥地利 ebInterface 6.0](austria-ebinterface-6-0.md)
