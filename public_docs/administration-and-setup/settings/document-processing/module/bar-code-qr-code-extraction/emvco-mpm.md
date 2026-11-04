# EMVCo MPM（商户展示二维码）

## 概述

**EMVCo MPM**（商户展示模式）是由 EMVCo 维护的全球二维码规范。EMVCo 也是芯片卡和非接触式支付标准的制定机构。十余种国家级即时支付方案共用同一种 TLV（标签-长度-值）封装，因此只需一个解析器，即可支持**巴西**的 **Pix**、**印度**的 **UPI**、**新加坡**的 **PayNow**、**泰国**的 **PromptPay**、**印度尼西亚**的 **QRIS**、**菲律宾**的 **QR Ph**、**越南**的 **VietQR**、**香港**的 **FPS**、**马来西亚**的 **DuitNow**、**新加坡**的 **NETS** 等多种方案。

### 功能概览

所有 EMVCo MPM 载荷都采用相同的封装：以 `000201`（载荷格式指示器 = 01）开头，以 `6304<CRC>` 结尾，其中 `<CRC>` 是 4 位十六进制 CRC16-CCITT-FALSE 校验和。内部的 TLV 编码标签 26–51 包含**商户账户信息**模板，并通过 **GUI 子标签**进行标识。DocBits 正是通过该 GUI 标签来检测二维码所属的国家级方案。系统会验证 CRC，并以布尔值形式提供验证结果，方便商户检测遭到篡改或损坏的二维码。

#### 主要优势

* **一个提取器，支持多种方案**：一个通用 TLV 解析器即可处理整个 EMVCo MPM 系列。
* **识别国家级方案**：输出中包含方案名称（例如 `pix`、`upi`、`paynow`），便于下游逻辑进行分支处理。
* **提供 CRC 有效性**：`emvmpm_crc16_valid` 用于标示遭到篡改或损坏的二维码。
* **货币标准化**：ISO 4217 数字货币代码会自动转换为 alpha-3 代码（支持 20 多种货币；未映射的数字代码会原样保留）。

***

### 检测

- 特征格式：以 `000201` 开头，并以 `6304<4-hex CRC16-CCITT-FALSE>` 结尾
- 通用 TLV（标签-长度-值）解码器会遍历所有标签
- 通过商户账户信息模板（标签 26–51）中的 **GUI 子标签**识别国家级方案

### 已识别的国家级方案

| GUI 子标签 | 方案 | 国家/地区 |
|-------------|--------|---------|
| `br.gov.bcb.pix` | **Pix** | 巴西 |
| `UPI` | **UPI** | 印度 |
| `SG.PAYNOW` | **PayNow / SGQR** | 新加坡 |
| `SG.COM.NETS` | **NETS** | 新加坡 |
| `HK.COM.HKICL.FPS` | **FPS** | 香港 |
| `ID.CO.QRIS.WWW` | **QRIS** | 印度尼西亚 |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | 菲律宾 |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | 泰国 |
| `A000000727` | **VietQR** | 越南 |

即使 GUI / AID 值无法识别，内容仍会被解析；提取器会回退到通用 EMVCo MPM 字段集。

### 提取的字段

所有字段均使用 `emvmpm_` 前缀：

| 字段 | 描述 |
|-------|-------------|
| `emvmpm_scheme` | 检测到的国家级方案（例如 `pix`、`upi`、`paynow`、`qris`、`promptpay`、`vietqr`、`fps`、`qrph`、`nets`），或 `generic` |
| `emvmpm_merchant_name` | 商户名称（标签 59） |
| `emvmpm_merchant_city` | 商户所在城市（标签 60） |
| `emvmpm_country_code` | ISO 3166 alpha-2 国家/地区代码（标签 58） |
| `emvmpm_amount` | 交易金额（十进制，标签 54） |
| `emvmpm_currency` | alpha-3 货币代码（由标签 53 的数字代码转换而来） |
| `emvmpm_additional_data` | 嵌套对象：账单编号、参考标签、终端标签、交易用途（标签 62 子标签） |
| `emvmpm_crc16_valid` | 布尔值：CRC16 校验和匹配时为 `true` |

### 示例 API 响应（Pix）

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### 如何启用

EMVCo MPM 解析由通用的**条形码 / 二维码提取**模块开关控制，无需进行特定标准的配置。

1. **前往设置**：
   * 从仪表板进入**设置**。
   * 选择**文档处理**，然后选择**模块**。
2. **启用功能**：
   * 向下滚动，找到**条形码 / 二维码提取**选项。
   * 切换滑块以启用该功能。

如需查看完整的支付二维码标准列表，请参阅[概述](./README.md)页面。
