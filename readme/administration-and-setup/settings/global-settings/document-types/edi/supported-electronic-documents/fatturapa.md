---
description: "DocBits 对 FATTURAPA 电子文档的支持"
---

# 🇮🇹 FATTURAPA

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [意大利](countries/italy.md). 格式系列名称并不认证所有 FatturaPA 发布版本，也不证明能够通过 SDI 传输。请检查原始架构和接收方要求。
{% endhint %}

| 属性                 | 值                                      |
| -------------------- | ---------------------------------------- |
| **国家 / 地区**      | 意大利                                  |
| **文档类型**         | 发票、贷项通知单、简化发票              |
| **格式**             | XML (FatturaPA 1.2.x)                    |
| **标准**             | FatturaPA (SDI)                          |

FatturaPA 是由意大利税务局（Agenzia delle Entrate）规定的意大利电子发票标准。自 2019 年 1 月起，意大利企业之间的所有发票都必须通过 Sistema di Interscambio (SDI) 传输。DocBits 可处理 FatturaPA XML 文档，并提取所有抬头和行项目字段。

## 支持状态

| 组件         | 状态        |
| ---------------- | ----------- |
| 预览         | ✅ 支持      |
| 字段提取     | ✅ 支持      |
| 转换         | ✅ 支持      |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/fatturapa-preview.png" alt="DocBits 中的 FatturaPA 发票预览"><figcaption><p>DocBits 中意大利 FatturaPA 发票的默认预览</p></figcaption></figure>

## 相关内容

* [支持的电子文档](./)
