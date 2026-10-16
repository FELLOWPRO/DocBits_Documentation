---
description: "DocBits 对巴西 CT-E 电子文档的支持"
---

# 🇧🇷 巴西 CT-E

| 属性                 | 值                                                        |
| -------------------- | --------------------------------------------------------- |
| **国家 / 地区**      | 巴西                                                     |
| **文档类型**         | 运输发票（Conhecimento de Transporte Eletrônico）        |
| **格式**             | XML                                                       |
| **标准**             | CT-e 3.0（电子货运 / 运输提单）                           |
| **区域设置**         | `pt_BR`                                                   |

CT-e（Conhecimento de Transporte Eletrônico，`<mod>57</mod>`）是由物流和货运公司签发的巴西电子运输文档。该文档记录运输服务、货物价值、始发和目的地市镇（`cMunIni` / `cMunFim`）以及运费（`vTPrest`）。与 NF-e 不同，CT-e 使用 `cteProc` 作为根元素，并引用关联的 NF-e 文档。

## 支持状态

| 组件         | 状态       |
| ------------ | ---------- |
| 预览         | ✅ 支持     |
| 字段提取     | ✅ 支持     |
| 转换         | ✅ 支持     |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/brazil-cte-preview.png" alt="DocBits 中的巴西 CT-e 预览"><figcaption><p>巴西 CT-E 文档的 DocBits 默认预览</p></figcaption></figure>

## 字段映射

### 表头字段

| DocBits 字段  | 源 XPath                                                | 备注                         |
| ------------- | ------------------------------------------------------- | ---------------------------- |
| `invoice_id`  | `//*[local-name()='ide']/*[local-name()='nCT']`        | CT-e 编号                    |
| `invoice_date`| `//*[local-name()='ide']/*[local-name()='dhEmi']`      | 带 BRT 时区偏移的 ISO 8601   |
| `currency`    | 固定值：`BRL`                                           | 始终为巴西雷亚尔              |
| `total_amount`| `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | 运费服务总额                 |
| `net_amount`  | `//*[local-name()='vPrest']/*[local-name()='vRec']`    | 应收金额                     |
| `tax_amount`  | `//*[local-name()='ICMS']//*[local-name()='vICMS']`    | 运输服务的 ICMS              |
| `supplier_name`| `//*[local-name()='emit']/*[local-name()='xNome']`     | 承运方（transportadora）名称 |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']`      | 承运方 CNPJ                 |
| `buyer_name`  | `//*[local-name()='dest']/*[local-name()='xNome']`     | 收货方（destinatário）名称   |
| `buyer_id`    | `//*[local-name()='dest']/*[local-name()='CNPJ']`      | 收货方 CNPJ                 |

> CT-e 不包含行项目表；运输服务作为单笔文档级费用记录。

## 分类规则

DocBits 通过 XML 命名空间中的以下值检测巴西 CT-E 文档（根元素为 `<cteProc>`）：

```
http://www.portalfiscal.inf.br/cte
```

## 相关内容

* [巴西 NF-E](brazil-nfe.md)
* [巴西 NFC-E](brazil-nfce.md)
* [巴西 NFS-E](brazil-nfse.md)
* [支持的电子文档](./)
