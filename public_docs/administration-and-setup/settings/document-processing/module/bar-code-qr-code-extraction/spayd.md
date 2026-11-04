# SPAYD / 简易付款描述符（捷克）

## 概述

**SPAYD**（简易付款描述符），也称为 **SPD**，是由捷克银行协会定义的标准付款二维码。它印在几乎所有捷克企业发票上，在斯洛伐克部分地区也有使用。DocBits 可解码 SPAYD 载荷并返回完整的付款指令，包括捷克特有的符号（可变符号、特定符号和固定符号），这些内容会包含在文档 API 响应中。

### 功能概述

SPAYD 载荷是由星号分隔的键值对列表。值采用百分号编码，因此 UTF-8 收款人姓名和消息能够得到保留。DocBits 支持常见的 `ACC` 变体（IBAN 加可选 BIC，以加号分隔）和 `ALT-ACC`（以逗号分隔的备用 IBAN），并会将任何未知的供应商专用键保存在专用的 `spayd_raw_pairs` 字段中，确保下游使用方不会丢失数据。

#### 主要优势

* **全面覆盖捷克付款信息**：IBAN/BIC 以及 VS/SS/KS 符号会提取到对应的命名字段中。
* **安全支持 Unicode**：采用百分号编码的 UTF-8 收款人姓名和消息能够完整往返。
* **向前兼容**：未知键会保存在 `spayd_raw_pairs` 中。

***

### 检测

- 标识前缀：`SPD*1.0*`
- 载荷是由 `*` 分隔的 `KEY:value` 键值对列表，例如 `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- 值采用 **百分号编码**（RFC 3986）
- `ACC` 可包含 `IBAN+BIC`（以加号分隔）；`ALT-ACC` 包含以逗号分隔的备用 IBAN

### 提取的字段

所有字段均使用 `spayd_` 前缀：

| 字段 | 说明 |
|-------|-------------|
| `spayd_iban` | 主要 IBAN（来自 `ACC`） |
| `spayd_bic` | BIC（来自 `ACC`，如存在） |
| `spayd_alt_ibans` | 备用 IBAN 列表（来自 `ALT-ACC`） |
| `spayd_amount` | 金额（十进制数，来自 `AM`） |
| `spayd_currency` | 货币（来自 `CC`，通常为 `CZK`） |
| `spayd_variable_symbol` | 可变符号（`VS`）——发票编号 / 参考编号 |
| `spayd_specific_symbol` | 特定符号（`SS`） |
| `spayd_constant_symbol` | 固定符号（`KS`） |
| `spayd_recipient_name` | 收款人 / 受益人姓名（来自 `RN`） |
| `spayd_due_date` | 到期日（来自 `DT`，格式为 `YYYYMMDD`） |
| `spayd_message` | 自由文本消息（来自 `MSG`） |
| `spayd_raw_pairs` | 任何未知或供应商专用的 `KEY:value` 键值对，按原样保留 |

### API 响应示例

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### 如何启用

SPAYD 解析由通用的 **条形码 / 二维码提取** 模块开关控制，无需进行标准专用配置。

1. **前往设置**：
   * 在仪表板中，前往 **Settings**。
   * 选择 **Document Processing**，然后选择 **Module**。
2. **启用功能**：
   * 向下滚动，找到 **Bar-Code / QR Code Extraction** 选项。
   * 切换滑块以启用该功能。

如需查看付款二维码标准的完整列表，请参阅[概述](./README.md)页面。
