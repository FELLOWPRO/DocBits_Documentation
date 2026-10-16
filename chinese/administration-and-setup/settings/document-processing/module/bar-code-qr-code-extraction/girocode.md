# GiroCode（EPC069-12）

## 概述

**GiroCode** 是欧洲支付委员会在规范 **EPC069-12** 中定义的 SEPA 支付二维码。它是德国和奥地利银行（Sparkasse、VR-Banken、Deutsche Bank、Commerzbank、PSA Austria）发票上的事实标准，也在荷兰、比利时和芬兰发行。DocBits 可解码两个版本（**v001** 和 **v002**），并在文档 API 响应中返回完整的 SEPA 支付载荷。

### 功能概览

GiroCode 包含发起 SEPA 信用转账所需的全部信息：收款方 BIC 和 IBAN、收款方名称、金额、用途，以及结构化债权人参考信息或非结构化汇款文本。DocBits 会对载荷进行标准化，因此**小数分隔符使用 `.` 或 `,` 的金额**——这是德国二维码生成器常见的规范偏差——都能被正确接受。

#### 主要优势

* **广泛覆盖德国和奥地利**：所有主要零售银行都会在客户发票上打印 GiroCode。
* **支持两个版本**：v001（BIC 必填）和 v002（EEA 付款可不填 BIC）。
* **兼容不同小数分隔符**：`227.01` 和 `227,01` 均可接受。

***

### 检测

- 魔数前缀：`BCD\n001`（v001）或 `BCD\n002`（v002）
- 按 EPC069-12 规范排列、以换行符分隔的结构化载荷
- **v002**：当 IBAN 属于单一欧元支付区时，BIC 为可选项

### 提取字段

所有字段均使用 `girocode_` 前缀：

| 字段 | 描述 |
|-------|-------------|
| `girocode_bic` | 收款方 BIC（v001 中必填；EEA 付款的 v002 中可选） |
| `girocode_creditor_name` | 收款方名称 |
| `girocode_iban` | 收款方 IBAN |
| `girocode_amount` | 金额（小数）——接受 `.` 和 `,` 两种分隔符 |
| `girocode_currency` | 货币（通常为 `EUR`） |
| `girocode_purpose` | SEPA 用途代码 |
| `girocode_structured_reference` | 结构化债权人参考信息（ISO 11649 RF-reference） |
| `girocode_unstructured_remittance` | 自由文本汇款信息 |
| `girocode_version` | `001` 或 `002` |

### API 响应示例

真实示例（Dr. Meindl u. Partner 发票）：

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### 如何启用

GiroCode 解析由通用的 **Bar-Code / QR Code Extraction** 模块开关控制，无需针对特定标准进行配置。

1. **前往设置**：
   * 在仪表板中，进入 **Settings**。
   * 选择 **Document Processing**，然后选择 **Module**。
2. **启用功能**：
   * 向下滚动，找到 **Bar-Code / QR Code Extraction** 选项。
   * 切换滑块以启用该功能。

如需查看支付二维码标准的完整列表，请参阅[概览](./README.md)页面。
