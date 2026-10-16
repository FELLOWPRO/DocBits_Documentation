# ZUGFeRD 2.3 映射

## 概述

ZUGFeRD 2.3 是最新的主要版本，在互操作性方面有所改进，并更符合现代电子发票要求。

## 标题字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段    | Infor BOD 字段    | 类型   | 描述       |
| --------------------------------- | ---------------- | ------------------ | ------ | ---------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | 发票编号   |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型与子类型（由 TRA 驱动）

默认的 TRANSFORMATION XSLT 会生成两个派生字段：

| DocBits 字段      | 来源                                                                                                     | 逻辑                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；空或缺失 → **费用发票**       |

### 付款信息

| ZUGFeRD CII 路径                                   | DocBits 字段    | Infor BOD 字段 | 类型   | 描述         |
| -------------------------------------------------- | ---------------- | --------------- | ------ | ------------- |
| `PayeePartyCreditorFinancialAccount/IBANID`        | `IBAN_EXTRACTED` | `PayeeIBAN`     | STRING | IBAN           |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC`            | `PayeeBIC`      | STRING | BIC/SWIFT 代码 |

### 税额明细（按税率分类）

`ApplicableTradeTax` 块会按税率分配到三个等级（并非按位置索引）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）用于记录税率 ≥ 19 的项目；低税率字段（`*_2`）用于记录 0 < 税率 < 19 的项目；零税率字段（`*_3`）用于记录税率 = 0 的项目。完整字段列表请参见[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。

## 行项目映射

| ZUGFeRD CII 路径                         | DocBits 字段  | Infor BOD 字段    | 类型   | 描述         |
| ---------------------------------------- | -------------- | ------------------ | ------ | ------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | 行编号       |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | 行项目描述   |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | 开票数量     |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | 净单价       |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | 行项目总额   |
