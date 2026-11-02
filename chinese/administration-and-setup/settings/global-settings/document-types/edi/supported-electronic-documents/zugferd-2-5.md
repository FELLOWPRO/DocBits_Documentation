---
description: DocBits 对 ZUGFERD 2.5 电子文档的支持
---

# 🇩🇪 ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [德国](countries/germany.md). 语法、发布版本和业务规范是不同的选择。不要根据共用的 1p0 标记推断 Factur-X 发布版本。
{% endhint %}

| 属性 | 值 |
|----------|-------|
| **国家 / 地区** | 德国 |
| **文档类型** | 发票、贷项通知单 |
| **格式** | CII（嵌入式 PDF/A-3）或 UBL XML |
| **标准** | ZUGFeRD 2.5 |
| **基于** | EN 16931 |

ZUGFeRD 2.5（FeRD/FNFE-MPE 于 2026 年 6 月联合发布）等同于 Factur-X 1.09。其 CII XML 使用 UN/CEFACT D22B 基础版本，并向后兼容 D16B，因此完整的 ZUGFeRD 2.4 提取和转换约定继续适用。EXTENDED 配置文件新增了付款方式和 BIC、第三方收款方（保理商）以及减免项/费用税务豁免原因等字段。

五种配置文件均受支持：MINIMUM、BASIC WL、BASIC、EN 16931 (COMFORT) 和 EXTENDED。DocBits 会分别对 CII 和 UBL 变体进行分类。

## 支持状态

| 组件 | 状态 |
|-----------|--------|
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 相关内容

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD 配置](../zugferd/configuration.md)
- [ZUGFeRD 字段映射](../zugferd/README.md)
- [支持的电子文档](./)
