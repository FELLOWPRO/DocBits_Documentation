# 加密货币支付 URI（BIP21 / BIP321）

## 概述

加密货币支付 URI 是一种非正式但广泛采用的标准，用于在二维码中编码加密货币付款请求。DocBits 支持识别五种最常见区块链上的 **BIP21**（原始 Bitcoin 支付 URI）和 **BIP321**（2024 年现代化扩展）：**Bitcoin**、**Lightning Network**、**Zcash**、**Ethereum** 和 **Litecoin**。

### 功能概览

加密货币二维码载荷是一个 URI，包含方案（`bitcoin:`、`lightning:`、`zcash:`、`ethereum:`、`litecoin:`）、收款地址以及一组 URL 风格的参数。DocBits 会提取所有标准 BIP21 参数（`amount`、`label`、`message`）以及较新的 BIP321 扩展（`lightning=` 付款备用方式、`pj=` / `pjos=` payjoin 端点）。根据 BIP21 规范，如果消费者不支持以 `req-` 为前缀的参数，可以拒绝处理这些参数。因此，DocBits 会将它们单独保存在字段（`crypto_required_params`）中，以便客户端决定如何处理。

#### 主要优势

* **支持多条链**：一个提取器即可处理 Bitcoin、Lightning、Zcash、Ethereum 和 Litecoin。
* **支持 BIP21 和 BIP321**：可识别两个版本，并在输出中提供版本信息。
* **方案不区分大小写**：`BITCOIN:` 和 `bitcoin:` 会被视为相同内容。

***

### 检测

- 基于方案检测（不区分大小写）：`bitcoin:`、`lightning:`、`zcash:`、`ethereum:`、`litecoin:`
- 标准 URI 格式：`<scheme>:<address>?<param>=<value>&<param>=<value>`

### 支持的参数

**BIP21 核心参数：**
- `amount` — 以原生加密货币单位表示的请求金额
- `label` — 收款方的可读标签
- `message` — 自由文本消息

**BIP321 扩展：**
- `lightning=<BOLT11>` — Lightning 账单备用方式
- `pj=<endpoint>` / `pjos=<endpoint>` — payjoin 端点
- `req-*` — 必需参数（保存在 `crypto_required_params` 中）

### 提取字段

所有字段均使用 `crypto_` 前缀：

| 字段 | 描述 |
|-------|-------------|
| `crypto_scheme` | `bitcoin`、`lightning`、`zcash`、`ethereum` 或 `litecoin` |
| `crypto_address` | 收款地址 |
| `crypto_amount` | 请求金额（十进制数） |
| `crypto_currency` | 原生货币符号（例如 `BTC`、`ETH`、`LTC`、`ZEC`） |
| `crypto_label` | 收款方标签（如果已设置） |
| `crypto_message` | 自由文本消息（如果已设置） |
| `crypto_lightning_fallback` | BOLT11 Lightning 账单（来自 BIP321 的 `lightning=`） |
| `crypto_payjoin_endpoint` | Payjoin 端点（来自 `pj=` / `pjos=`） |
| `crypto_required_params` | 所有 `req-*` 参数，保留供客户端决定如何处理 |
| `crypto_uri_version` | `bip21` 或 `bip321` |

### API 响应示例

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### 如何启用

加密货币 URI 解析由通用的 **Bar-Code / QR Code Extraction** 模块开关控制，无需针对特定标准进行配置。

1. **前往设置**：
   * 在仪表板中，前往 **Settings**。
   * 选择 **Document Processing**，然后选择 **Module**。
2. **启用该功能**：
   * 向下滚动，找到 **Bar-Code / QR Code Extraction** 选项。
   * 切换滑块以启用该功能。

如需查看完整的付款二维码标准列表，请参阅[概览](./README.md)页面。
