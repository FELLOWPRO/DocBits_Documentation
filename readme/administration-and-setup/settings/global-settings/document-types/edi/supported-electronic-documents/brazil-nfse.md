---
description: "DocBits 对 BRAZIL NFS-E 电子文档的支持"
---

# 🇧🇷 巴西 NFS-E

| 属性 | 值 |
| -------------------- | -------------------------------------------------------------------- |
| **国家 / 地区** | 巴西 |
| **文档类型** | 服务发票（Nota Fiscal de Serviços Eletrônica） |
| **格式** | XML |
| **标准** | NFS-e 2.04（ABRASF 市政服务发票国家标准） |
| **区域设置** | `pt_BR` |

NFS-e（Nota Fiscal de Serviços Eletrônica）是巴西的服务电子发票，由市级机构签发。DocBits 支持 ABRASF（Associação Brasileira das Secretarias de Finanças das Capitais）标准架构。NFS-e 文档使用的 XML 结构与 NF-e 不同：其主要税种是 ISS（Imposto Sobre Serviços），而不是 ICMS；供应商和买方分别称为 `PrestadorServico` / `TomadorServico`。`Discriminacao` 元素包含自由文本形式的服务描述。

## 支持状态

| 组件 | 状态 |
| ---------------- | ----------- |
| 预览 | ✅ 支持 |
| 字段提取 | ✅ 支持 |
| 转换 | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/brazil-nfse-preview.png" alt="DocBits 中的巴西 NFS-e 预览"><figcaption><p>BRAZIL NFS-E 文档的 DocBits 默认预览</p></figcaption></figure>

## 字段映射

### 抬头字段

| DocBits 字段 | 源 XPath | 备注 |
| --------------- | --------------------------------------------------------------------- | --------------------------- |
| `invoice_id` | `//*[local-name()='Numero']` | NFS-e 编号 |
| `invoice_date` | `//*[local-name()='DataEmissao']` | ISO 8601 签发日期 |
| `currency` | 固定值：`BRL` | 始终为巴西雷亚尔 |
| `total_amount` | `//*[local-name()='ValorServicos']` | 服务总金额 |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | 扣除款项后的净额 |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS（市政服务税） |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | 服务提供方名称 |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | 服务提供方 CNPJ |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | 服务接受方名称 |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | 服务接受方 CNPJ |

> NFS-e 在 `Discriminacao` 元素中描述单项服务，而不是行项目。不会提取 `INVOICE_TABLE`。

## 分类规则

DocBits 通过以下命名空间识别 BRAZIL NFS-E 文档：

```
http://www.abrasf.org.br/nfse.xsd
```

## 相关内容

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [支持的电子文档](./)
