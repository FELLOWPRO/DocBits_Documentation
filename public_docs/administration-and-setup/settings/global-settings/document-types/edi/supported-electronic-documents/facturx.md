---
description: DocBits 中对 FACTURX 电子文档的支持
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [法国](countries/france.md). XML 标记 1p0 和 Factur-X XMP Version 1.0 无法确定发布版本。版本未知时，请保留通用名称。
{% endhint %}

| 属性                 | 值                     |
| -------------------- | ---------------------- |
| **国家 / 地区**      | 法国 / 德国             |
| **文档类型**         | 发票、贷项通知单         |
| **格式**             | CII（嵌入 PDF/A-3）     |
| **标准**             | Factur-X               |
| **基于**             | EN 16931               |

协调统一的 CII Guideline ID 可以标识格式系列和业务规范，但多个发布版本可能使用相同的 1p0 标记。Factur-X XMP Version 1.0 是架构标记，并非 1.08 或 1.09 这样的发布版本。ZUGFeRD XMP 可以声明其版本。如果缺少权威元数据，请保留通用格式系列的识别结果，并向发送方确认原始文件。

## 支持状态

| 组件             | 状态         |
| ---------------- | ----------- |
| 预览             | ✅ 支持       |
| 字段提取         | ✅ 支持       |
| 转换             | ✅ 支持       |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="DocBits 中的 Factur-X 发票预览"><figcaption><p>法国 Factur-X 发票的 DocBits 默认预览</p></figcaption></figure>

## 相关内容

* [ZUGFeRD 配置](../zugferd/)
* [ZUGFeRD 字段映射](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [支持的电子文档](./)
