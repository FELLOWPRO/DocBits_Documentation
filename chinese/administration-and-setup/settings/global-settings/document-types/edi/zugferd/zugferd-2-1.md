# ZUGFeRD 2.1 映射

## 概述

ZUGFeRD 2.1 与法国标准 Factur-X 1.0 完全相同。它完全符合 EN 16931，广泛用于德国与法国之间的跨境交易。

## 页眉字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段       | Infor BOD 字段    | 类型   | 描述       |
| --------------------------------- | ------------------- | ------------------ | ------ | ---------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER`    | `DocumentID`       | STRING | 发票编号   |
| `ExchangedDocument/TypeCode`      | `INVOICE_TYPE_CODE` | `DocumentType`     | STRING | 发票类型代码 |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`      | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型和子类型（由 TRA 驱动）

除原始 `INVOICE_TYPE_CODE` 外，默认 TRANSFORMATION XSLT 还会生成两个派生字段：

| DocBits 字段       | 来源                                                                                                     | 逻辑                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；空或缺失 → **费用发票**       |

### 税额明细（按层级分类）

`ApplicableTradeTax` 区块会按税率分配到三个层级（而非按位置索引）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）用于捕获税率 ≥ 19 的数据；低税率字段（`*_2`）用于捕获 0 < 税率 < 19 的数据；零税率字段（`*_3`）用于捕获税率 = 0 的数据。完整字段列表请参阅[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。

### 买方信息

| ZUGFeRD CII 路径                                  | DocBits 字段          | Infor BOD 字段       | 类型   | 描述     |
| ------------------------------------------------- | --------------------- | --------------------- | ------ | -------- |
| `BuyerTradeParty/ID`                              | `COMPANY_ID`          | `CustomerPartyID`     | STRING | 客户 ID  |
| `BuyerTradeParty/Name`                            | `COMPANY_NAME`        | `CustomerPartyName`   | STRING | 公司名称 |
| `BuyerTradeParty/PostalTradeAddress/Line1`        | `COMPANY_ADDRESS`     | `CustomerAddress1`    | STRING | 地址行 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode`  | STRING | 邮政编码 |
| `BuyerTradeParty/PostalTradeAddress/CityName`     | `COMPANY_CITY`        | `CustomerCity`        | STRING | 城市     |
| `BuyerTradeParty/PostalTradeAddress/CountryID`    | `COMPANY_COUNTRY`     | `CustomerCountryCode` | STRING | 国家代码 |

## 行项目映射

| ZUGFeRD CII 路径                         | DocBits 字段           | Infor BOD 字段    | 类型   | 描述           |
| ---------------------------------------- | ---------------------- | ------------------ | ------ | -------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`             | `LineNumber`       | STRING | 行号           |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID`     | STRING | 卖方物料编号   |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`          | `ItemDescription`  | STRING | 物料描述       |
| `BilledQuantity`                         | `QUANTITY`             | `InvoicedQuantity` | NUMBER | 计费数量       |
| `BilledQuantity/@unitCode`               | `UNIT`                 | `UnitCode`         | STRING | 计量单位       |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`           | `UnitPrice`        | AMOUNT | 不含税单价     |
| `LineTotalAmount`                        | `TOTAL_AMOUNT`         | `ExtendedAmount`   | AMOUNT | 行项目总额     |
