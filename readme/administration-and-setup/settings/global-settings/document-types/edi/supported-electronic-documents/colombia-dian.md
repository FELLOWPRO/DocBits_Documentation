---
description: >-
  DocBits 对哥伦比亚 DIAN 电子文档的支持（Factura Electrónica、Documento Soporte）
---

# 🇨🇴 哥伦比亚 DIAN

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [哥伦比亚](countries/colombia.md). 在所检查的状态中，贷项通知单分类条目没有专用提取组件包。请确认实际生效的映射，不要根据发票条目推断支持情况。
{% endhint %}

| 属性                   | 值                                                                            |
| ---------------------- | ----------------------------------------------------------------------------- |
| **国家 / 地区**       | 哥伦比亚                                                                       |
| **文档类型**           | 发票（Factura Electrónica）、贷项通知单（Nota de Crédito）、Documento Soporte |
| **格式**               | XML（UBL 2.1）                                                                 |
| **标准**               | DIAN 2.1（Dirección de Impuestos y Aduanas Nacionales）                        |
| **区域设置**           | `es_CO`                                                                        |

哥伦比亚电子发票标准由 **DIAN**（Dirección de Impuestos y Aduanas Nacionales）监管。该标准基于 UBL 2.1，并包含 DIAN 专用扩展（`sts:DianExtensions`）。DocBits 通过 DIAN 命名空间识别哥伦比亚 DIAN 文档，并根据 `CustomizationID` 进行路由：

| CustomizationID | 文档类型                                            |
| --------------- | --------------------------------------------------- |
| 10              | Factura Electrónica de Venta (FACTURA ELECTRONICA)  |
| 20              | Nota de Crédito（贷项通知单）                       |
| 91              | Nota de Crédito por devolución                      |
| 92              | Nota de Débito                                      |
| DS              | Documento Soporte（DOCUMENTO SOPORTE）              |

DIAN 标识符（**NIT** — Número de Identificación Tributaria）在 UBL `CompanyID` 元素中使用 `schemeID="31"`。

## 支持状态

| 组件       | 状态       |
| ---------- | ---------- |
| 预览       | ✅ 支持     |
| 字段提取   | ✅ 支持     |
| 转换       | ✅ 支持     |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/colombia-dian-preview.png" alt="DocBits 中的哥伦比亚 DIAN Factura Electrónica 预览"><figcaption><p>COLOMBIA FACTURA ELECTRONICA（CustomizationID 10）的 DocBits 默认预览</p></figcaption></figure>

## 字段映射

### 页眉字段

| DocBits 字段   | 源 XML 元素                                        | 说明                                  |
| -------------- | -------------------------------------------------- | ------------------------------------- |
| `invoice_id`   | `cbc:ID`                                           | 带前缀的发票号码（例如 `SETP990000001`） |
| `invoice_date` | `cbc:IssueDate`                                    | 开具日期（ISO 8601）                  |
| `due_date`     | `cbc:DueDate`                                      | 付款到期日                            |
| `currency`     | `cbc:DocumentCurrencyCode`                         | 始终为 `COP`（哥伦比亚比索）           |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount`         | 应付总额，含 IVA                       |
| `net_amount`   | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount`    | 净额，不含 IVA                         |
| `tax_amount`   | `cac:TaxTotal/cbc:TaxAmount`                       | IVA 总额（标准税率为 19%）             |
| `supplier_name`| `cac:AccountingSupplierParty//cbc:RegistrationName`| 供应商法定名称                         |
| `supplier_id`  | `cac:AccountingSupplierParty//cbc:CompanyID`       | 供应商 NIT（schemeID=31）              |
| `buyer_name`   | `cac:AccountingCustomerParty//cbc:RegistrationName`| 买方法定名称                           |
| `buyer_id`     | `cac:AccountingCustomerParty//cbc:CompanyID`      | 买方 NIT（schemeID=31）                |

### 行项目表（`INVOICE_TABLE`）

行路径：`cac:InvoiceLine`（或 `cac:CreditNoteLine`）

| 列            | 源 XML 元素                  | 说明                         |
| ------------- | ---------------------------- | ---------------------------- |
| `POSITION`    | `cbc:ID`                     | 行号                         |
| `DESCRIPTION` | `cac:Item/cbc:Description`   | 产品或服务描述               |
| `QUANTITY`    | `cbc:InvoicedQuantity`       | 含单位代码属性的数量         |
| `UNIT_PRICE`  | `cac:Price/cbc:PriceAmount`  | 单价，不含 IVA               |
| `NET_AMOUNT`  | `cbc:LineExtensionAmount`    | 行总额，不含 IVA             |

## 分类规则

DocBits 根据 DIAN 命名空间字符串识别哥伦比亚 DIAN 文档：

| 电子文档类型                 | 匹配模式                                                                                 |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE   | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

发票的根元素为 `<Invoice>`（UBL 2.1），贷项通知单的根元素为 `<CreditNote>`。所有文档都包含一个 `<sts:DianExtensions>` 块，其中包含 DIAN 授权数据（`InvoiceAuthorization`、`CUFE`/`CUDE` UUID、二维码）。

## 相关内容

* [当前支持的电子发票标准](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/currently-supported-e-invoice-standards/README.md)
* [支持的电子文档](./)
