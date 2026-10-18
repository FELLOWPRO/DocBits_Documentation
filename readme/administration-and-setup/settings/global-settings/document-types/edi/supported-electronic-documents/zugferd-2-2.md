---
description: DocBits 对 ZUGFERD 2.2 电子文档的支持
---

# 🇩🇪 ZUGFERD 2.2

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [德国](countries/germany.md). 语法、发布版本和业务规范是不同的选择。不要根据共用的 1p0 标记推断 Factur-X 发布版本。
{% endhint %}

| 属性 | 值 |
| -------------------- | ---------------------- |
| **国家 / 地区** | 德国 |
| **文档类型** | 发票、贷项通知单 |
| **格式** | CII（嵌入式 PDF/A-3） |
| **标准** | ZUGFeRD 2.2 |
| **基于** | EN 16931 |

ZUGFeRD 2.2 于 2022 年发布，符合欧洲标准 EN 16931，等同于 Factur-X 1.0.06。它使用 CII D16B XML 语法，并支持五种符合性配置：Minimum、Basic WL、Basic、EN 16931（Comfort）和 Extended。

## 支持状态

| 组件 | 状态 |
| ---------------- | ----------- |
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="DocBits 中的 ZUGFeRD 2.2 发票预览"><figcaption><p>DocBits 中德国 ZUGFeRD 2.2 发票的默认预览</p></figcaption></figure>

## 相关内容

* [ZUGFeRD 配置](../zugferd/)
* [ZUGFeRD 字段映射](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [支持的电子文档](./)
