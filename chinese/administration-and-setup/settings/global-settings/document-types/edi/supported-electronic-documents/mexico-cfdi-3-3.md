---
description: "DocBits 对墨西哥 CFDI 3.3 电子文档的支持"
---

# 🇲🇽 墨西哥 CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [墨西哥](countries/mexico.md). 请检查命名空间、版本和 TipoDeComprobante。不能仅凭负金额识别贷项通知单；成功解析不代表已获 SAT 核准。
{% endhint %}

| 属性                 | 值                                               |
| -------------------- | -------------------------------------------------- |
| **国家 / 地区**      | 墨西哥                                             |
| **文档类型**         | 发票、贷项通知单、付款收据                          |
| **格式**             | XML                                                |
| **标准**             | CFDI 3.3（Comprobante Fiscal Digital por Internet） |

CFDI 3.3 是墨西哥数字税务收据标准的上一代版本，由 SAT（Servicio de Administración Tributaria）发布。虽然它已被 CFDI 4.0 取代，但许多历史发票仍使用此版本。它包含 UUID（folio fiscal）、RFC 标识符以及 IEPS/IVA 税额计算。

## 支持状态

| 组件               | 状态         |
| ---------------- | ----------- |
| 预览               | ✅ 支持       |
| 字段提取            | ✅ 支持       |
| 转换               | ✅ 支持       |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="DocBits 中的墨西哥 CFDI 3.3 发票预览"><figcaption><p>DocBits 中墨西哥 CFDI 3.3 发票的默认预览</p></figcaption></figure>

## 相关内容

* [支持的电子文档](./)
