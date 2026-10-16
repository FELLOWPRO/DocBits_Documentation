---
description: DocBits 中对 FACTURX 电子文档的支持
---

# 🇫🇷 FACTURX

| 属性                 | 值                     |
| -------------------- | ---------------------- |
| **国家 / 地区**      | 法国 / 德国             |
| **文档类型**         | 发票、贷项通知单         |
| **格式**             | CII（嵌入 PDF/A-3）     |
| **标准**             | Factur-X               |
| **基于**             | EN 16931               |

Factur-X 是法德混合发票标准的法国实现。它会在 PDF/A-3 文档中嵌入结构化的 CII XML 数据，使发票既可供人工阅读，也可由机器处理。DocBits 会自动检测嵌入 XML 中的 Factur-X 版本和配置文件。

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
