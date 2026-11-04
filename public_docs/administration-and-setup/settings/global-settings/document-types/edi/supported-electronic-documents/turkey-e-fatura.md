---
description: "DocBits 对土耳其 E-FATURA 电子文档的支持"
---

# 🇹🇷 土耳其 E-FATURA

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [土耳其](countries/turkey.md). 请检查原始业务规范和文档结构。格式系列名称不能确定所有 UBL-TR 发布版本，也不能证明已通过税务平台送达。
{% endhint %}

| 属性 | 值 |
| -------------------- | --------------------------------------- |
| **国家 / 地区** | 土耳其 |
| **文档类型** | 发票、贷项通知单 |
| **格式** | UBL-TR 1.2 XML |
| **标准** | e-Fatura（GİB - 税务管理局） |

土耳其 e-Fatura 是 GİB（税务管理局）针对已注册纳税人之间 B2B 交易规定的主要电子发票标准。发票通过注册的集成商和 GİB 平台交换。该格式采用 UBL-TR，这是土耳其本地化版本的 UBL，并包含用于 TCKN/VKN 纳税人识别的土耳其专用字段。

## 支持状态

| 组件 | 状态 |
| ---------------- | ----------- |
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/turkey-e-fatura-preview.png" alt="DocBits 中的土耳其 E-Fatura 发票预览"><figcaption><p>DocBits 中土耳其 E-Fatura 发票的默认预览</p></figcaption></figure>

## 相关内容

* [支持的电子文档](./)
* [土耳其 E-ARSIV](turkey-e-arsiv.md)
