---
description: "DocBits 对 FACTUR-X 1.09 - ZUGFeRD 2.5 电子文档的支持"
---

# 🇫🇷 FACTUR-X 1.09 - ZUGFeRD 2.5

| 属性 | 值 |
|----------|-------|
| **国家 / 地区** | 法国 / 德国 |
| **文档类型** | 发票、贷项通知单 |
| **格式** | CII（嵌入式 PDF/A-3） |
| **标准** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **基于** | EN 16931 |

Factur-X 1.09 是法国发布版本，与 ZUGFeRD 2.5 等效（FeRD/FNFE-MPE 于 2026 年 6 月联合发布）。其 CII XML 使用 UN/CEFACT D22B 基础版本，并向后兼容 D16B，因此 Factur-X 1.08 / ZUGFeRD 2.4 的完整提取和转换约定继续适用。EXTENDED 配置文件新增了付款方式和 BIC 字段、第三方收款人（保理商）字段，以及减免/附加费用税务豁免原因字段。

支持全部五种配置文件：MINIMUM、BASIC WL、BASIC、EN 16931 (COMFORT) 和 EXTENDED。

## 支持状态

| 组件 | 状态 |
|-----------|--------|
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 相关内容

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [ZUGFeRD 配置](../zugferd/configuration.md)
- [ZUGFeRD 字段映射](../zugferd/README.md)
- [支持的电子文档](./)
