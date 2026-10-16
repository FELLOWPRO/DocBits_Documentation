# ZUGFeRD 2.2 映射

## 概述

ZUGFeRD 2.2 继续与 EN 16931 保持一致，并纳入了 CII 标准的更多更新。

## 标题字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段    | Infor BOD 字段    | 类型   | 描述        |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | 发票编号     |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型和子类型（由 TRA 驱动）

默认 TRANSFORMATION XSLT 会生成两个派生字段：

| DocBits 字段      | 来源                                                                                                     | 逻辑                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；为空或缺失 → **成本发票**       |

### 税额明细（按等级分类）

`ApplicableTradeTax` 区块会按税率分为三个等级（而非按位置索引）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）用于税率 ≥ 19；低税率字段（`*_2`）用于 0 < 税率 < 19；零税率字段（`*_3`）用于税率 = 0。完整字段列表请参阅[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。

### 货币和金额

| ZUGFeRD CII 路径      | DocBits 字段      | Infor BOD 字段       | 类型   | 描述      |
| --------------------- | ------------------ | --------------------- | ------ | ---------------- |
| `InvoiceCurrencyCode` | `CURRENCY`         | `CurrencyCode`        | STRING | 发票币种 |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | 不含税总额 |
| `TaxTotalAmount`      | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount`      | AMOUNT | 税额总计 |
| `GrandTotalAmount`    | `TOTAL_AMOUNT`     | `GrandTotalAmount`    | AMOUNT | 总金额      |

## 行项目映射

| ZUGFeRD CII 路径                         | DocBits 字段  | Infor BOD 字段    | 类型   | 描述      |
| ---------------------------------------- | -------------- | ------------------ | ------ | ---------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | 行号      |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | 项目描述 |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | 开票数量  |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | 不含税单价   |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | 行项目总额       |
