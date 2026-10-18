---
description: DocBits 中对 KSEF FA2 电子文档的支持
---

# 🇵🇱 KSEF FA2

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [波兰](countries/poland.md). FA2 与 FA3 使用不同的结构。请确认原始架构并测试适当的映射；解析文件不会将发票提交到 KSeF。
{% endhint %}

| 属性                 | 值                         |
| -------------------- | --------------------------- |
| **国家 / 地区**      | 波兰                        |
| **文档类型**         | 发票、更正发票               |
| **格式**             | XML                         |
| **标准**             | KSeF FA(2)                  |

KSeF FA2 是波兰国家电子发票系统的第二版架构。它定义了结构化发票（faktury）的 XML 结构，包括卖方和买方数据、行项目、增值税税率和付款条款，以满足波兰税法的要求。

## 支持状态

| 组件               | 状态         |
| ------------------ | ------------ |
| 预览               | ✅ 支持      |
| 字段提取           | ✅ 支持      |
| 转换               | ✅ 支持      |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="DocBits 中 KSeF FA(2) 发票的预览"><figcaption><p>波兰 KSeF FA(2) 发票的默认 DocBits 预览</p></figcaption></figure>

## 相关

* [支持的电子文档](./)
