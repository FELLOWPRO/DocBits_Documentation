# ZUGFeRD 2.3.2 映射

## 概述

ZUGFeRD 2.3.2 是 2.3 标准的维护版本，确保与最新的 CII 更新兼容。

## 页眉字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段    | Infor BOD 字段    | 类型   | 描述         |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | 发票编号     |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型和子类型（由 TRA 驱动）

默认的 TRANSFORMATION XSLT 会生成两个派生字段：

| DocBits 字段       | 来源                                                                                                       | 逻辑                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他任何代码 → **发票** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；为空或缺失 → **成本发票**       |

### 税额明细（按层级分类）

`ApplicableTradeTax` 块按税率分配到三个层级（而非按位置使用 `[1]`/`[2]`/`[3]`）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）捕获税率 ≥ 19 的数据；减税率字段（`*_2`）捕获 0 < 税率 < 19 的数据；零税率字段（`*_3`）捕获税率 = 0 的数据。完整字段列表请参阅[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。

| ZUGFeRD CII 路径                                    | DocBits 字段 | Infor BOD 字段 | 类型   | 描述                   |
| --------------------------------------------------- | ------------- | --------------- | ------ | ---------------------- |
| `ApplicableTradeTax/RateApplicablePercent`（层级 1） | `TAX_RATE`    | `TaxPercent`    | NUMBER | 标准税率增值税（≥ 19） |
| `ApplicableTradeTax/BasisAmount`（层级 1）           | `NET_AMOUNT`  | `TaxableAmount` | AMOUNT | 标准税率净额           |
| `ApplicableTradeTax/CalculatedAmount`（层级 1）      | `TAX_AMOUNT`  | `TaxAmount`     | AMOUNT | 标准税率税额           |

## 行项目映射

| ZUGFeRD CII 路径                         | DocBits 字段  | Infor BOD 字段    | 类型   | 描述         |
| ---------------------------------------- | -------------- | ------------------ | ------ | ------------ |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | 行编号       |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | 项目描述     |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | 计费数量     |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | 不含税单价   |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | 行项目总额   |
