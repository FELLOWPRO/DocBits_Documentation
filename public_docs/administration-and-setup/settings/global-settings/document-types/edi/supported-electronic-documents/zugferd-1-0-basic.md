---
description: DocBits 对 ZUGFERD 1.0 BASIC 电子文档的支持
---

# 🇩🇪 ZUGFERD 1.0 BASIC

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [德国](countries/germany.md). 语法、发布版本和业务规范是不同的选择。不要根据共用的 1p0 标记推断 Factur-X 发布版本。
{% endhint %}

| 属性                 | 值                         |
| -------------------- | -------------------------- |
| **国家 / 地区**      | 德国                       |
| **文档类型**         | 发票、贷项通知单            |
| **格式**             | CII（嵌入式 PDF/A-3）       |
| **标准**             | ZUGFeRD 1.0，Basic 配置文件 |
| **基于**             | ZUGFeRD 1.0 规范            |

ZUGFeRD 1.0 的 Basic 配置文件包含发票编号、日期、卖方/买方、行项目和税额汇总等必要发票字段。它提供了足够的结构化数据，可在大多数 ERP 系统中实现自动记账。

## 支持状态

| 组件             | 状态       |
| ---------------- | ---------- |
| 预览             | ✅ 支持     |
| 字段提取         | ✅ 支持     |
| 转换             | ✅ 支持     |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="DocBits 中的 ZUGFeRD 1.0 Basic 发票预览"><figcaption><p>DocBits 为德国 ZUGFeRD 1.0 Basic 发票提供的默认预览</p></figcaption></figure>

## 相关内容

* [ZUGFeRD 配置](../zugferd/)
* [ZUGFeRD 字段映射](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/edi/zugferd/versions/README.md)
* [受支持的电子文档](./)
