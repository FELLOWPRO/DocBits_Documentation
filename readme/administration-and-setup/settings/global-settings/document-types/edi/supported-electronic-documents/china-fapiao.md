---
description: >-
  DocBits 支持中国发票（FAPIAO、E-FAPIAO、增值税普通发票、增值税专用发票）电子文档
---

# 🇨🇳 中国发票

| 属性             | 值                                                               |
| ---------------- | ---------------------------------------------------------------- |
| **国家 / 地区**   | 中国                                                             |
| **文档类型**     | 增值税普通发票 (普通发票)、增值税专用发票 (专用发票)、E-Fapiao |
| **格式**         | XML                                                              |
| **标准**         | 发票（Fapiao），国家税务总局                                        |
| **区域设置**     | `zh_CN`                                                          |

发票（Fapiao）是由国家税务总局（STA / 国家税务总局）主管的中国税务发票标准。所有发票文档共用 `urn:china:tax:fapiao:1.0` 命名空间。DocBits 通过 `fapiao_type` 元素自动检测发票类型，并应用相应的提取规则：

| fapiao\_type 值 | 文档类型                                           |
| ------------------ | -------------------------------------------------- |
| 普通发票               | 增值税普通发票（FAPIAO / GENERAL VAT INVOICE） |
| 专用发票               | 增值税专用发票（SPECIAL VAT INVOICE）          |
| 电子发票               | 电子发票（E-FAPIAO）                                |

## 支持状态

| 组件             | 状态       |
| ---------------- | ---------- |
| 预览             | ✅ 支持 |
| 字段提取         | ✅ 支持 |
| 转换             | ✅ 支持 |

## 默认预览

<figure><img src="../../../../../../.gitbook/assets/china-fapiao-preview.png" alt="DocBits 中中国增值税普通发票预览"><figcaption><p>DocBits 中中国增值税普通发票（普通发票）的默认预览</p></figcaption></figure>

## 字段映射

### 抬头字段

| DocBits 字段      | 源 XML 元素                 | 说明                                     |
| ------------------ | --------------------------- | -------------------------------------- |
| `invoice_id`       | `fapiao_head/fapiao_number` | 发票号码 — 8 位数字（发票号码）        |
| `invoice_date`     | `fapiao_head/issue_date`    | 开具日期（ISO 8601）                  |
| `currency`         | 固定值：`CNY`                | 始终为人民币           |
| `total_amount`     | `total/total_with_tax`      | 含增值税的总金额（价税合计）          |
| `net_amount`       | `total/total_amount`        | 不含增值税的应税金额（金额）      |
| `tax_amount`       | `total/total_tax`           | 增值税总额（税额）                  |
| `supplier_name`    | `seller/name`               | 销售方公司名称（销售方名称）            |
| `supplier_id`      | `seller/taxpayer_id`        | 销售方纳税人识别号 — 18 个字符（纳税人识别号） |
| `supplier_address` | `seller/address`            | 销售方地址                         |
| `supplier_country` | 固定值：`CN`                 | 始终为中国                           |
| `iban`             | `seller/bank_account`       | 销售方银行账号             |
| `buyer_name`       | `buyer/name`                | 购买方公司名称（购买方名称）             |
| `buyer_id`         | `buyer/taxpayer_id`         | 购买方纳税人识别号（纳税人识别号）             |
| `buyer_address`    | `buyer/address`             | 购买方地址                          |
| `buyer_country`    | 固定值：`CN`                 | 始终为中国                           |

### 行项目表 (`INVOICE_TABLE`)

行路径：`items/item`

| 列            | 源 XML 元素 | 说明                                      |
| ------------- | ------------------ | ------------------------------------------ |
| `POSITION`    | `seq`              | 行序号                       |
| `DESCRIPTION` | `name` + `spec`    | 项目名称和规格（拼接） |
| `QUANTITY`    | `quantity`         | 数量                                   |
| `UNIT`        | `unit`             | 计量单位（例如：箱、台、项）             |
| `UNIT_PRICE`  | `unit_price`       | 不含增值税的单价                       |
| `VAT_RATE`    | `tax_rate`         | 增值税税率（%）（通常为 6%、9% 或 13%）   |
| `VAT`         | `tax_amount`       | 每行增值税额                        |
| `NET_AMOUNT`  | `amount`           | 不含增值税的行总额                       |

## 分类规则

DocBits 通过匹配 XML 命名空间和 `fapiao_type` 来检测中国发票：

| 电子文档类型               | 模式                                                           |
| ------------------------- | -------------------------------------------------------------- |
| 中国增值税普通发票 | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| 中国增值税专用发票 | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| 中国电子发票            | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

根元素为 `<fapiao>`，其命名空间为 `urn:china:tax:fapiao:1.0`。分类遵循**先匹配优先**原则，并按模式长度排序（最长优先）。

## 相关内容

* [当前支持的电子发票标准](https://github.com/Fellow-Consulting-AG/docbits/tree/main/readme/administration-and-setup/settings/global-settings/document-types/currently-supported-e-invoice-standards/README.md)
* [支持的电子文档](./)
