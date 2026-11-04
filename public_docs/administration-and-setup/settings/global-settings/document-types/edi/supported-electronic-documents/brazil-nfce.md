---
description: DocBits 对 BRAZIL NFC-E 电子文档的支持
---

# 🇧🇷 巴西 NFC-E

<!-- edocs-country-scope -->

{% hint style="info" %}
请参阅国家指南，了解版本限制、实际生效的配置和国家说明视频。 [巴西](countries/brazil.md). 它们属于不同的文档系列。已配置的 NFS-e 版本并不认证所有市级架构或所有国家服务发票版式。
{% endhint %}

| 属性                 | 值                                                     |
| -------------------- | ------------------------------------------------------- |
| **国家 / 地区**      | 巴西                                                  |
| **文档类型**         | 消费者发票（Nota Fiscal de Consumidor Eletrônica） |
| **格式**             | XML                                                     |
| **标准**             | NFC-e 4.0（零售 / 销售点消费者发票）     |
| **区域设置**         | `pt_BR`                                                 |

NFC-e（Nota Fiscal de Consumidor Eletrônica，`<mod>65</mod>`）是巴西面向最终消费者零售销售的电子发票。它与 NF-e XML 架构（`nfeProc` 命名空间）共用，但使用型号代码 65。NFC-e 文档通常使用买方的 CPF（个人税号），而不是 CNPJ；对于简单零售交易，每个行项目也不会包含 PIS/COFINS。

## 支持状态

| 组件             | 状态        |
| ---------------- | ----------- |
| 预览             | ✅ 支持 |
| 字段提取         | ✅ 支持 |
| 转换             | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="DocBits 中的巴西 NFC-e 预览"><figcaption><p>BRAZIL NFC-E 文档的 DocBits 默认预览</p></figcaption></figure>

## 字段映射

### 发票抬头字段

| DocBits 字段   | 来源 XPath                                               | 备注                    |
| --------------- | ---------------------------------------------------------- | ------------------------ |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Nota Fiscal 编号       |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | 带 BRT 时区偏移的 ISO 8601 |
| `currency`      | 固定值：`BRL`                                               | 始终为巴西雷亚尔    |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | NFC-e 总值        |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | 产品小计        |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | ICMS 税额合计           |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | 零售商名称            |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` or `CPF` | CNPJ 或 CPF              |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | 消费者姓名            |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CPF']` or `CNPJ` | CPF（个人）或 CNPJ |

### 行项目表（`INVOICE_TABLE`）

行路径：`//*[local-name()='det']`

| 列             | 相对 XPath                                                              | 备注                      |
| -------------- | --------------------------------------------------------------------------- | -------------------------- |
| `POSITION`     | `@nItem`                                                                    | 行项目序号       |
| `ITEM_CODE`    | `*[local-name()='prod']/*[local-name()='cProd']`                            | 产品代码               |
| `DESCRIPTION`  | `*[local-name()='prod']/*[local-name()='xProd']`                            | 产品描述        |
| `NCM_CODE`     | `*[local-name()='prod']/*[local-name()='NCM']`                              | NCM 海关分类 |
| `CFOP_CODE`    | `*[local-name()='prod']/*[local-name()='CFOP']`                             | 业务税务代码      |
| `UNIT`         | `*[local-name()='prod']/*[local-name()='uCom']`                             | 计量单位            |
| `QUANTITY`     | `*[local-name()='prod']/*[local-name()='qCom']`                             | 商业数量        |
| `UNIT_PRICE`   | `*[local-name()='prod']/*[local-name()='vUnCom']`                           | 单价                 |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']`                            | 行项目总额                 |
| `ICMS_AMOUNT`  | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | 每个行项目的 ICMS 税额          |
| `VAT_RATE`     | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS 税率（%）              |

## 分类规则

DocBits 通过在 `http://www.portalfiscal.inf.br/nfe` 命名空间 XML 中匹配 `<mod>65</mod>` 来检测 BRAZIL NFC-E 文档。

## 相关文档

* [巴西 NF-E](brazil-nfe.md)
* [巴西 CT-E](brazil-cte.md)
* [巴西 NFS-E](brazil-nfse.md)
* [支持的电子文档](./)
