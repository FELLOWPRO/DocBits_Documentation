---
description: "在测试文档处理之前，先确定已配置的 eDocs 格式系列、语法、版本和业务规范。"
---

# eDocs 格式、版本和国家指南

从原始文档和对应的国家指南开始检查。仅凭国家名称无法确定文件格式。版本标识、XML 语法和业务规范描述的是不同的内容。

{% hint style="info" %}
这些表格记录了 2026 年 10 月 17 日对开发环境目录及相应处理代码的检查结果。它们说明有哪些规则和配置组件可用，并不代表对所有文件、法律要求或生产部署的认证。组织配置可以覆盖默认规则。
{% endhint %}

## 正确理解支持矩阵

- 格式系列：电子文档格式，例如 XRechnung、Factur-X、KSeF 或 CFDI。
- 语法：实际的数据载荷，例如 UBL XML、CII XML 或内嵌 XML 的 PDF。扫描 PDF、JSON 导出文件或二维码图片并不等同于 XML 数据载荷。
- 版本：文档声明的发布版本或架构版本。通用的格式系列名称不能证明所有版本均受支持。
- 业务规范：业务或数据要求的一个子集，例如 BASIC、EN16931、EXTENDED 或买方代开票。业务规范不是发布版本。
- 规则与组件：分类、Transformation、Preview 和 Extraction Paths 相互独立。已配置的业务规范不一定有独立的分类规则。
- 验证与传输：呈现文件或提取数据本身，不能验证所有法律规则、签名、税务核准或网络送达情况。

## 国家指南

| 国家 / 地区 | 格式系列和版本范围 | 目录检查结果 |
| --- | --- | --- |
| [奥地利](countries/austria.md) | ebInterface 4.3、5.0、6.0 和 6.1 各有独立条目。 | 已找到条目 |
| [丹麦](countries/denmark.md) | OIOUBL 2.1 是明确列出的丹麦条目。 | 已找到条目 |
| [芬兰](countries/finland.md) | Finvoice 1.3、2.0、2.01 和 3.0 各有独立条目。TEAPPSXML 属于另一个格式系列。 | 已找到条目 |
| [法国](countries/france.md) | Factur-X 既有通用条目，也有具体发布版本的条目，包括 1.0.05、1.08 和 1.09。VRBL FR CIUS 1.0 为独立条目。 | 已找到条目 |
| [德国](countries/germany.md) | XRechnung 从 1.0 到 3.0.2 共有十三个版本名称，每个版本均有 CII 和 UBL 条目。ZUGFeRD 包含早期业务规范，以及 2.5 的 CII 和 UBL 条目。 | 已找到条目 |
| [意大利](countries/italy.md) | FatturaPA 是已配置的意大利格式系列。 | 已找到条目 |
| [荷兰](countries/netherlands.md) | SI-UBL 2.0 有专用条目。 | 已找到条目 |
| [挪威](countries/norway.md) | 目录列出了 EHF Invoice 3.0，以及 EHF Order、Order Response 和 Despatch Advice。 | 已找到条目 |
| [波兰](countries/poland.md) | KSeF 有通用、FA2 和 FA3 条目。 | 已找到条目 |
| [斯洛文尼亚](countries/slovenia.md) | e-SLOG 1.6 和 2.0 各有独立条目。 | 已找到条目 |
| [西班牙](countries/spain.md) | Facturae 有通用、3.2、3.2.1 和 3.2.2 条目。 | 已找到条目 |
| [瑞典](countries/sweden.md) | Svefaktura 1.0 是明确列出的瑞典条目。 | 已找到条目 |
| [澳大利亚](countries/australia.md) | PINT A-NZ 有与新西兰共用的发票和贷项通知单规则条目。 | 已找到条目 |
| [新西兰](countries/new-zealand.md) | PINT A-NZ 有与澳大利亚共用的发票和贷项通知单规则条目。 | 已找到条目 |
| [印度](countries/india.md) | India GST E-Invoice 和 GST CreditNote 各有独立条目。 | 已找到条目 |
| [印度尼西亚](countries/indonesia.md) | Indonesia E-Faktur 是已配置的格式系列。 | 已找到条目 |
| [中国](countries/china.md) | 目录包含 Fapiao、E-Fapiao、General VAT Invoice 和 Special VAT Invoice。 | 已找到条目 |
| [日本](countries/japan.md) | JP PINT 和 JP PINT Self-Billing 是独立条目。 | 已找到条目 |
| [韩国](countries/korea.md) | Korea E-Tax Invoice 和 Korea NTS 是已配置的格式系列。 | 已找到条目 |
| [马来西亚](countries/malaysia.md) | MyInvois 有发票和贷项通知单规则条目。 | 已找到条目 |
| [菲律宾](countries/philippines.md) | Philippines EIS 是已配置的格式系列。 | 已找到条目 |
| [新加坡](countries/singapore.md) | InvoiceNow 有发票和贷项通知单条目；InvoiceNow SG 是另一个已配置的名称。 | 已找到条目 |
| [台湾](countries/taiwan.md) | Taiwan eGUI 是已配置的格式系列。 | 已找到条目 |
| [泰国](countries/thailand.md) | Thailand E-Tax Invoice 是已配置的格式系列。 | 已找到条目 |
| [越南](countries/vietnam.md) | Vietnam E-Invoice 是已配置的格式系列。 | 已找到条目 |
| [阿根廷](countries/argentina.md) | Argentina AFIP 和 Factura Electronica 是已配置的名称。 | 已找到条目 |
| [巴西](countries/brazil.md) | 巴西有 NF-e、NFC-e、CT-e、NFS-e 和 SPED NFS-e 条目。NFS-e 包含版本 1.00 和 2.00 至 2.04；SPED 包含 1.00.02 和 1.01。 | 已找到条目 |
| [智利](countries/chile.md) | Chile DTE 有发票、贷项通知单和发货单条目。 | 已找到条目 |
| [哥伦比亚](countries/colombia.md) | Colombia Factura Electronica 和 Documento Soporte 各有独立条目。 | 已找到条目 |
| [哥斯达黎加](countries/costa-rica.md) | 较早的文档提到了哥斯达黎加，但在所检查的开发环境目录中未找到匹配的分类或配置条目。 | 尚未确认 |
| [厄瓜多尔](countries/ecuador.md) | Ecuador SRI 有通用、1.0.0、1.1.0、2.0.0 和 2.1.0 条目。预扣税是独立的文档类型。 | 已找到条目 |
| [墨西哥](countries/mexico.md) | Mexico CFDI 3.3 和 4.0 各有独立条目。 | 已找到条目 |
| [巴拉圭](countries/paraguay.md) | Paraguay DTE、SIFEN 和 SIFEN 150 是已配置的名称。 | 已找到条目 |
| [秘鲁](countries/peru.md) | Peru CPE 有通用、UBL 2.0 和 UBL 2.1 条目。Factura Electronica 是另一个名称。 | 已找到条目 |
| [乌拉圭](countries/uruguay.md) | Uruguay CFE 有通用、24 和 25 条目。目录还列出了 E-Factura 和 E-Nota Credito。 | 已找到条目 |
| [哈萨克斯坦](countries/kazakhstan.md) | Kazakhstan ESF 是已配置的格式系列。 | 已找到条目 |
| [沙特阿拉伯](countries/saudi-arabia.md) | ZATCA Fatoorah、Reporting、Simplified 和 Tax Invoice 各有独立条目。 | 已找到条目 |
| [土耳其](countries/turkey.md) | Turkey E-Fatura 和 E-Arsiv 是独立配置的格式系列。 | 已找到条目 |
| [阿拉伯联合酋长国](countries/united-arab-emirates.md) | UAE VAT Invoice 是已配置的名称。 | 已找到条目 |
| [国际](countries/international.md) | 国际条目包括 Peppol BIS 3.0、UBL 2.1、纯 CII、EDI、INVOIC02、cXML、OCI、BOD 和 SPS Commerce RSX 7.7.4。 | 已找到条目 |

## Factur-X / ZUGFeRD：不要臆测发布版本

协调统一的 CII Guideline ID 可以标识格式系列和业务规范，但多个发布版本可能使用相同的 1p0 标记。Factur-X XMP Version 1.0 是架构标记，并非 1.08 或 1.09 这样的发布版本。ZUGFeRD XMP 可以声明其版本。如果缺少权威元数据，请保留通用格式系列的识别结果，并向发送方确认原始文件。

MINIMUM 和 BASIC WL 可能不包含后续处理所需的行项目信息。BASIC、EN16931/COMFORT 和 EXTENDED 涵盖的数据范围各不相同。数据更全面的业务规范可能包含提取映射未使用的字段。请用真实样例检查必需字段。

## 检查组织中的格式

1. 保留原始 XML 或内嵌 XML 的 PDF。查看命名空间、架构或自定义标识，以及声明的版本和业务规范。

2. 针对适用的业务文档，打开设置 → 文档类型 → E-Doc。搜索指南中所列的准确电子文档格式名称。

3. 检查实际生效的 Default 或 Custom 来源及其活动配置版本。查看 Transformation、Preview 和 Extraction Paths。保存草稿不会将其激活。

4. 针对所需的每一种语法、版本和业务文档，测试有代表性的原始文件。验证关键字段、金额、税额、发票或贷项通知单分类，以及 ERP 导出结果。

5. 单独确认验证策略和传输方式。保留自定义映射，并在重新启动现有文档之前检查审批和导出历史。

[验收检查](../credit-note-recognized-as-invoice.md)

[使用 Claude 或 Codex 配置 DocBits](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md)：连接、提示词、预览、版本化更改、验证与回退。
