# ZUGFeRD 2.0 映射

## 概述

ZUGFeRD 2.0 旨在符合欧洲标准 EN 16931。它采用 UN/CEFACT CII D16B 结构。

## 页眉字段映射

### 发票标识

| ZUGFeRD CII 路径               | DocBits 字段        | Infor BOD 字段     | 类型   | 描述         |
| ------------------------------ | ------------------- | ------------------ | ------ | ------------ |
| `ExchangedDocument/ID`         | `INVOICE_NUMBER`    | `DocumentID`       | STRING | 发票编号     |
| `ExchangedDocument/TypeCode`   | `INVOICE_TYPE_CODE` | `DocumentType`     | STRING | 发票类型代码 |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型和子类型（由 TRA 驱动）

除了原始的 `INVOICE_TYPE_CODE`，默认的 TRANSFORMATION XSLT 还会生成两个派生字段：

| DocBits 字段       | 来源                                                                                                       | 逻辑                                                                       |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票**             |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；为空或缺失 → **费用发票**                             |

### 税额明细（按税率分级）

`ApplicableTradeTax` 区块会分配到三个基于税率的级别（而非位置索引）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）用于记录税率 ≥ 19 的数据；减税税率字段（`*_2`）用于记录 0 < 税率 < 19 的数据；零税率字段（`*_3`）用于记录税率 = 0 的数据。完整字段列表请参阅[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。

### 日期

| ZUGFeRD CII 路径                                   | DocBits 字段   | Infor BOD 字段      | 类型 | 描述         |
| -------------------------------------------------- | ------------- | ------------------- | ---- | ------------ |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | 交货/发货日期 |
| `SpecifiedTradePaymentTerms/DueDateDateTime`       | `DUE_DATE`    | `PaymentDueDateTime` | DATE | 付款到期日   |

### 供应商（卖方）信息

| ZUGFeRD CII 路径                                  | DocBits 字段         | Infor BOD 字段       | 类型   | 描述     |
| ------------------------------------------------- | -------------------- | -------------------- | ------ | -------- |
| `SellerTradeParty/ID`                            | `VENDOR_ID`          | `SupplierPartyID`    | STRING | 供应商 ID |
| `SellerTradeParty/Name`                          | `VENDOR_NAME`        | `SupplierPartyName`  | STRING | 供应商名称 |
| `SellerTradeParty/PostalTradeAddress/Line1`      | `VENDOR_ADDRESS`     | `SupplierAddress1`   | STRING | 地址行 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | 邮政编码 |
| `SellerTradeParty/PostalTradeAddress/CityName`   | `VENDOR_CITY`        | `SupplierCity`       | STRING | 城市     |
| `SellerTradeParty/PostalTradeAddress/CountryID`  | `VENDOR_COUNTRY`     | `SupplierCountryCode` | STRING | 国家代码 |

## 行项目映射

| ZUGFeRD CII 路径                        | DocBits 字段   | Infor BOD 字段     | 类型   | 描述         |
| --------------------------------------- | ------------- | ------------------ | ------ | ------------ |
| `AssociatedDocumentLineDocument/LineID` | `POSITION`    | `LineNumber`       | STRING | 行号         |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID`      | STRING | 买方物料编号 |
| `SpecifiedTradeProduct/Name`            | `DESCRIPTION` | `ItemDescription`  | STRING | 物料描述     |
| `BilledQuantity`                        | `QUANTITY`    | `InvoicedQuantity` | NUMBER | 开票数量     |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice`        | AMOUNT | 不含税单价   |
| `LineTotalAmount`                       | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | 行项目总额   |
