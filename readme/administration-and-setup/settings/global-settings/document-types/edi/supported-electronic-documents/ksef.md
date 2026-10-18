---
description: DocBits 中的 KSEF 电子文档支持
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [波兰](countries/poland.md). FA2 与 FA3 使用不同的结构。请确认原始架构并测试适当的映射；解析文件不会将发票提交到 KSeF。
{% endhint %}

| 属性                 | 值                                       |
| -------------------- | ---------------------------------------- |
| **国家 / 地区**      | 波兰                                     |
| **文档类型**         | 发票、贷项通知单、更正发票               |
| **格式**             | XML                                      |
| **标准**             | KSeF（Krajowy System e-Faktur）          |

KSeF 是由波兰财政部运营的波兰国家电子发票系统。该系统将成为所有在波兰注册增值税的企业的强制要求。DocBits 支持 KSeF FA2 和 FA3 架构版本的发票处理。

## 支持状态

| 组件             | 状态        |
| ---------------- | ----------- |
| 预览             | ✅ 支持      |
| 字段提取         | ✅ 支持      |
| 转换             | ✅ 支持      |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="DocBits 中的 KSeF 发票预览"><figcaption><p>DocBits 中波兰 KSeF 发票的默认预览</p></figcaption></figure>

## 相关内容

* [支持的电子文档](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
