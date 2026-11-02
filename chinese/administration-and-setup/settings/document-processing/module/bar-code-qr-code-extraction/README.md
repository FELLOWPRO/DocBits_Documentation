# 条形码 / QR 码提取

## **概述**

此功能可自动提取文档中嵌入的**条形码和 QR 码**信息。这是一项全开或全关的设置——启用后会同时提取这两种代码。

{% hint style="info" %}
**相关内容：**如需在验证文档时手动读取条形码 / QR 码的值并将其分配给某个字段，请参阅 [条形码分配](../barcode-assignment.md)。
{% endhint %}

## 如何启用条形码 / QR 码提取

请按以下步骤启用条形码 / QR 码提取功能：

1. **前往设置**：
   * 在仪表板中，前往**设置**。
   * 选择**文档处理**，然后选择**模块**。
2. **启用此功能**：
   * 向下滚动，找到**条形码 / QR 码提取**选项。
   * 切换滑块以启用条形码 / QR 码提取。

## **支持的代码类型**

DocBits 支持提取以下代码类型：

* **QR-CODE**
* **EAN-2**、**EAN-5**、**EAN-8**、**EAN-13**
* **UPC-A**、**UPC-E**
* **ISBN-10**、**ISBN-13**
* **COMPOSITE**
* **I25**
* **DATABAR**、**DATABAR-EXP**
* **CODABAR**
* **CODE-39**、**CODE-93**、**CODE-128**
* **PDF-417**
* **SQ-CODE**

## 付款 QR 码标准

除了通用 QR 码解码之外，DocBits 还能识别 **七种不同的付款 QR 码标准**，并将其中的付款字段自动提取到文档 API 响应中。客户无需再手动解码这些 QR 字符串——每种标准都有自己的字段前缀（例如 `swissqr_*`、`girocode_*`），因此这些值可以直接用于匹配、验证和导出。

| # | 标准 | 区域 | 字段前缀 | 典型用途 |
|---|----------|--------|--------------|-------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | 瑞士 | `swissqr_*` | 自 2020 年起的所有瑞士发票 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE、AT、NL、BE、FI | `girocode_*` | SEPA 付款 |
| 3 | [SPAYD / SPD](spayd.md) | CZ，部分 SK | `spayd_*` | 捷克银行协会标准 |
| 4 | [PagoPA](pagopa.md) | IT（公共管理部门） | `pagopa_*` | 意大利 PA 发票上的强制标准 |
| 5 | [Crypto Payment URIs](crypto-uris.md) | 全球加密货币 | `crypto_*` | Bitcoin、Lightning、Ethereum、Zcash、Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR、IN、SG、TH、MY、ID、PH、VN、HK 等 | `emvmpm_*` | Pix、UPI、PayNow、PromptPay、QRIS、QR Ph、VietQR、FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | 沙特阿拉伯 | `zatca_*` | 沙特阿拉伯每张发票上的强制标准 |

**检测会自动进行。**系统会检查每个解码后的 QR 字符串是否包含其特有前缀（例如，Swiss QR Bill v2.0 的 `SPC\n0200`，PagoPA 的 `PAGOPA|002|`），并且只会将识别出的标准解析为结构化字段。

### **相关页面**

[条形码提取详情](bar-code-extractions.md)
