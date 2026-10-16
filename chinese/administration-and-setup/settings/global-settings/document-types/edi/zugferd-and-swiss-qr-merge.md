# ZUGFeRD + Swiss QR 代码字段映射

## 概述

处理同时包含 ZUGFeRD XML 数据和 Swiss QR 代码的 PDF 发票时，DocBits 会从这两个来源提取数据并智能合并。

## 工作原理

1. **ZUGFeRD XML 提取** - DocBits 首先从嵌入的 ZUGFeRD XML 中提取字段
2. **Swiss QR 代码检测** - 条码服务检测并解析 Swiss QR 代码
3. **智能合并** - 使用 Swiss QR 数据填充空字段（保留已有值的字段）
4. **审计跟踪** - 完整的 QR 代码数据会存储在 `qr_code_data` 中，以供验证

## 字段映射表

### Swiss QR 代码 → DocBits 字段映射

| Swiss QR 字段 | DocBits 字段 | 说明 |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | 债权人的 IBAN（例如 CH9300762011...） |
| 金额 | `total_amount` | 付款金额（例如 1234.56） |
| 币种 | `currency` | 币种代码（CHF 或 EUR） |
| 参考编号 | `payment_reference` / `esr_reference` | QR 参考编号或 ESR 编号 |
| Creditor.Name | `supplier_name` | 供应商公司名称 |
| Creditor.AddressLine1 | `supplier_address` | 街道地址 |
| Creditor.PostalCode | `supplier_plz` | 邮政编码 |
| Creditor.City | `supplier_city` | 城市名称 |
| Creditor.Country | `supplier_country` | 国家/地区代码（CH） |
| Debtor.Name | `company_name` | 收款公司名称 |
| Debtor.AddressLine1 | `company_street` | 收款方街道地址 |
| Debtor.PostalCode | `company_plz` | 收款方邮政编码 |
| Debtor.City | `company_city` | 收款方城市 |

## 示例：样例发票处理

### 输入文档

*   **PDF**：包含嵌入式 ZUGFeRD 1.0 XML 和 Swiss QR 代码条码的发票

### 提取的 Swiss QR 代码数据

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### 字段提取结果

| 字段 | 值 | 来源 | 方法 |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## 提取方法

| 方法代码 | 说明 |
| :--- | :--- |
| **ED** | 电子文档（ZUGFeRD/XRechnung/PEPPOL XML） |
| **SWISS_QR** | Swiss QR 代码条码提取 |
| **OCR** | 光学字符识别 |
| **ML** | 机器学习提取 |

## 合并优先级

1. **ZUGFeRD XML** 优先级最高（结构化且可靠的数据）
2. **Swiss QR 代码** 用于填充空字段（付款数据准确性有保障）
3. **OCR/ML** 用于提取电子数据源中不存在的字段

## 支持的 Swiss QR 代码版本

* Swiss QR 账单格式（ISO 20022）
* QR-IBAN 格式（以 30、31 开头）
* 标准 IBAN 格式
* 支持或不支持结构化参考编号（QRR、SCOR）

## 版本要求

此功能需要 **api version 10.95.6** 和 **barcode version 1.0.5** 或更高版本。

### 组件版本（环境）

| 组件 | 版本 | 说明 |
| :--- | :--- | :--- |
| `api` | 10.95.6 | 支持 ZUGFeRD 1.0 提取的核心 API |
| `barcode` | 1.0.5 | Swiss QR 代码检测与解析 |
| `Auth` | 1.48.8 | 身份验证服务 |
