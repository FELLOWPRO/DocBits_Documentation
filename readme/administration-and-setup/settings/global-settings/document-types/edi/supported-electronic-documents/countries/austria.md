---
description: "ebInterface 4.3、5.0、6.0 和 6.1 各有独立条目。"
---

# 奥地利

在测试原始文件之前，使用本指南确定已配置的格式系列和版本范围。

[所有国家和支持范围](../README.md)

## 变体与版本限制

ebInterface 4.3、5.0、6.0 和 6.1 各有独立条目。

**语法:** XML

请将 XML 命名空间与已配置的版本匹配。不同的命名空间可能需要另一套映射。

这些表格记录了 2026 年 10 月 17 日对开发环境目录及相应处理代码的检查结果。它们说明有哪些规则和配置组件可用，并不代表对所有文件、法律要求或生产部署的认证。组织配置可以覆盖默认规则。

## 已检查的规则和组件矩阵

| 准确格式名称 | 规则文档键 | 可用组件 |
| --- | --- | --- |
| `EBINTERFACE 4.3` | `INVOICE` | C / T / P / E |
| `EBINTERFACE 5.0` | `INVOICE` | C / T / P / E |
| `EBINTERFACE 6.0` | `INVOICE` | C / T / P / E |
| `EBINTERFACE 6.1` | `INVOICE` | C / T / P / E |

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

- [🇦🇹 奥地利 EBINTERFACE](../austria-ebinterface.md)
- [🇦🇹 AUSTRIA EBINTERFACE 6.0](../austria-ebinterface-6-0.md)
- [🇦🇹 奥地利 EBINTERFACE 6.1](../austria-ebinterface-6-1.md)
