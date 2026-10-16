---
description: "DocBits 对阿根廷电子发票（ARGENTINA FACTURA ELECTRONICA）的支持"
---

# 🇦🇷 阿根廷电子发票（ARGENTINA FACTURA ELECTRONICA）

| 属性 | 值 |
| -------------------- | ----------------------------------------------------------------------- |
| **国家 / 地区** | 阿根廷 |
| **文档类型** | 发票 |
| **格式** | XML |
| **标准** | 阿根廷电子发票（Argentina Factura Electrónica）（除 Factura A 之外的 AFIP 凭证类型） |
| **区域设置** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA 涵盖 Factura A（类型 001）之外更广泛的阿根廷 AFIP 电子文档类型，包括 Factura B（类型 006）、Factura C（类型 011）、Nota de Crédito（类型 003）等凭证类型。DocBits 会从 `<tipoComprobante>` 自动检测文档类型，并应用相应的提取规则。

## 支持状态

| 组件 | 状态 |
| ---------------- | ----------- |
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="DocBits 中的阿根廷电子发票预览"><figcaption><p>ARGENTINA FACTURA ELECTRONICA 文档的 DocBits 默认预览</p></figcaption></figure>

## 字段映射

### 抬头字段

| DocBits 字段 | 源 XML 元素 | 备注 |
| ---------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| `invoice_id` | `//NumeroFactura`、`//cbte_nro`、`//CbteNro`、`//InvoiceNumber` | 为不同架构提供多个 XPath 回退选项 |
| `invoice_date` | `//FechaEmision`、`//cbte_fch`、`//CbteFch`、`//IssueDate` | |
| `due_date` | `//fechaVencimiento`、`//fechaVtoPago` | |
| `currency` | `//Moneda`、`//mon_id`、`//MonId`，回退值：`ARS` | |
| `total_amount` | `//MontoTotal`、`//imp_total`、`//ImpTotal`、`//TotalAmount` | |
| `net_amount` | `//MontoNeto`、`//imp_neto`、`//ImpNeto`、`//NetAmount` | |
| `tax_amount` | `//MontoIVA`、`//imp_iva`、`//ImpIVA`、`//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`、`//razon_social`、`//RazonSocial`、`//SellerName` | |
| `supplier_id` | `//CUITProveedor`、`//cuit`、`//Cuit`、`//SellerID` | CUIT = 阿根廷税号 |
| `buyer_name` | `//NombreComprador`、`//nombre_cliente`、`//NombreCliente`、`//BuyerName` | |
| `buyer_id` | `//CUITComprador`、`//doc_nro`、`//DocNro`、`//BuyerID` | |
| `iban` | `//PAYMENT/IBAN` | 通常为空 |
| `bic` | `//PAYMENT/BIC` | 通常为空 |
| `payment_terms` | `//PAYMENT_TERMS` | 通常为空 |
| `purchase_order` | `//PURCHASE_ORDER` | 通常为空 |

### 行项目表（`INVOICE_TABLE`）

行路径：`<items>/<item>`、`<Items>/<Item>` 或 `<Detalle>/<Linea>`

| 列 | 源属性 / 元素 | 备注 |
| ------------- | --------------------------------------- | -------------------- |
| `POSITION` | `@numero`、`<numero>` 或 `position()` | 行项目序号 |
| `DESCRIPTION` | `<descripcion>`、`<Descripcion>` | |
| `QUANTITY` | `<cantidad>`、`<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`、`<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`、`<AlicuotaIVA>` | 例如 `21.00` |
| `VAT` | `<importeIVA>`、`<ImporteIVA>` | |
| `NET_AMOUNT` | `<subtotal>`、`<Subtotal>`、`<importe>` | 行项目总额 |

## 分类规则

DocBits 通过缺少 Factura A 标记来检测 ARGENTINA FACTURA ELECTRONICA 文档——`<tipoComprobante>` 值不为 `001`（例如 `003`、`006`、`011`）的文档会被路由到此标准。

## 相关文档

* [ARGENTINA AFIP](argentina-afip.md)
* [支持的电子文档](./)
