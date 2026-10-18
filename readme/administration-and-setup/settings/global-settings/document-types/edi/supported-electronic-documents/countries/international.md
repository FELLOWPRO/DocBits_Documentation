---
description: "国际条目包括 Peppol BIS 3.0、UBL 2.1、纯 CII、EDI、INVOIC02、cXML、OCI、BOD 和 SPS Commerce RSX 7.7.4。"
---

# 国际

在测试原始文件之前，使用本指南确定已配置的格式系列和版本范围。

[所有国家和支持范围](../README.md)

## 变体与版本限制

国际条目包括 Peppol BIS 3.0、UBL 2.1、纯 CII、EDI、INVOIC02、cXML、OCI、BOD 和 SPS Commerce RSX 7.7.4。

**语法:** UBL / CII / EDI / cXML

发票、订单、响应和发货映射相互独立。文件处理本身不提供 Peppol 接入点，也不提供与贸易伙伴的连接。

这些表格记录了 2026 年 10 月 17 日对开发环境目录及相应处理代码的检查结果。它们说明有哪些规则和配置组件可用，并不代表对所有文件、法律要求或生产部署的认证。组织配置可以覆盖默认规则。

## 已检查的规则和组件矩阵

| 准确格式名称 | 规则文档键 | 可用组件 |
| --- | --- | --- |
| `BOD` | `PURCHASE_ORDER` | C / — / — / — |
| `CXML ORDER CONFIRMATION` | `ORDER_CONFIRMATION` | C / T / P / E |
| `CXML PURCHASE ORDER` | `PURCHASE_ORDER` | C / T / P / E |
| `EDI` | `PURCHASE_ORDER` | C / T / P / E |
| `EDI` | `ORDER_CONFIRMATION` | C / T / P / E |
| `EDI` | `INVOICE` | C / T / P / E |
| `INVOIC02` | `INVOICE` | C / T / P / E |
| `OCI CATALOG ORDER` | `PURCHASE_ORDER` | C / T / P / E |
| `PEPPOL BIS 3.0` | `INVOICE` | C / T / P / E |
| `PEPPOL DESPATCH ADVICE 3.0` | `DELIVERY_NOTE` | C / T / P / E |
| `PEPPOL ORDER 3.0` | `PURCHASE_ORDER` | C / T / P / E |
| `PEPPOL ORDER RESPONSE 3.0` | `ORDER_CONFIRMATION` | C / T / P / E |
| `PURCHASE ORDER BOD` | `PURCHASE_ORDER` | C / T / P / E |
| `PURE CII D16B EU` | `INVOICE` | C / T / P / E |
| `PURE CII D16B EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D16B NON-EU` | `INVOICE` | C / T / P / E |
| `PURE CII D16B NON-EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D22B EU` | `INVOICE` | C / T / P / E |
| `PURE CII D22B EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D22B NON-EU` | `INVOICE` | C / T / P / E |
| `PURE CII D22B NON-EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D23B EU` | `INVOICE` | C / T / P / E |
| `PURE CII D23B EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D23B NON-EU` | `INVOICE` | C / T / P / E |
| `PURE CII D23B NON-EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D24B EU` | `INVOICE` | C / T / P / E |
| `PURE CII D24B EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII D24B NON-EU` | `INVOICE` | C / T / P / E |
| `PURE CII D24B NON-EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII V1 EU` | `INVOICE` | C / T / P / E |
| `PURE CII V1 EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `PURE CII V1 NON-EU` | `INVOICE` | C / T / P / E |
| `PURE CII V1 NON-EU CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `SPS COMMERCE RSX 7.7.4` | `PURCHASE_ORDER_ACKNOWLEDGMENT` | C / T / P / E |
| `SPS COMMERCE RSX 7.7.4` | `ADVANCE_SHIP_NOTICE` | C / T / P / E |
| `SPS COMMERCE RSX 7.7.4` | `PURCHASE_ORDER` | C / T / P / E |
| `SPS COMMERCE RSX 7.7.4` | `INVOICE` | C / T / P / E |
| `SPS COMMERCE RSX 7.7.4` | `PURCHASE_ORDER_CHANGE` | C / T / P / E |
| `UBL 2.1` | `INVOICE` | C / T / P / E |
| `UBL 2.1 CREDITNOTE` | `CREDIT_NOTE` | C / T / P / E |
| `UBL 2.1 DESPATCH ADVICE` | `DELIVERY_NOTE` | C / T / P / E |
| `UBL 2.1 ORDER` | `PURCHASE_ORDER` | C / T / P / E |
| `UBL 2.1 ORDER RESPONSE` | `ORDER_CONFIRMATION` | C / T / P / E |

C = 分类，T = Transformation，P = Preview，E = Extraction Paths。文档键用于查找规则或配置，不能保证最终保存的 invoice_type 值。转换可以通过 INVOICE 映射将文档分类为贷项通知单。

短横线表示状态检查未报告该准确格式与文档键组合的专用组件。这不排除使用共享或回退映射的可能性。在依赖此处理路径之前，请验证实际生效的映射选择逻辑，并测试有代表性的文件。

<!-- Country screenshot and narrated film pending; no unavailable media is linked. -->

## 验收检查

组件检查只能确认配置存在，并非针对所有版本的端到端处理测试。请测试准确的数据载荷，以及集成所需的发票或贷项通知单处理路径。

## 检查组织中的格式

1. 保留原始 XML 或内嵌 XML 的 PDF。查看命名空间、架构或自定义标识，以及声明的版本和业务规范。

2. 针对适用的业务文档，打开设置 → 文档类型 → E-Doc。搜索指南中所列的准确电子文档格式名称。

3. 检查实际生效的 Default 或 Custom 来源及其活动配置版本。查看 Transformation、Preview 和 Extraction Paths。保存草稿不会将其激活。

4. 针对所需的每一种语法、版本和业务文档，测试有代表性的原始文件。验证关键字段、金额、税额、发票或贷项通知单分类，以及 ERP 导出结果。

5. 单独确认验证策略和传输方式。保留自定义映射，并在重新启动现有文档之前检查审批和导出历史。

## 相关格式参考

- [INVOIC02](../invoic02.md)
- [🇪🇺 PEPPOL BIS 3.0](../peppol-bis-3-0.md)
- [SPS COMMERCE RSX 7.7.4](../sps-commerce-rsx-7-7-4.md)
- [UBL 2.1](../ubl-2-1.md)
