# ZUGFeRD 1.0 映射

## 概述

ZUGFeRD 1.0 是该标准的初始版本。虽然版本较旧，但仍有许多文档使用此格式。DocBits 完全支持从 ZUGFeRD 1.0 XML 文件中提取数据。

## 表头字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段       | Infor BOD 字段    | 类型   | 描述         |
| --------------------------------- | ------------------- | ------------------ | ------ | ------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER`    | `DocumentID`       | STRING | 发票编号     |
| `ExchangedDocument/TypeCode`      | `INVOICE_TYPE_CODE` | `DocumentType`     | STRING | 发票类型代码 |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`      | `DocumentDateTime` | DATE   | 发票开具日期 |

### 文档类型和子类型（由 TRA 驱动）

除原始的 `INVOICE_TYPE_CODE` 外，默认的 TRANSFORMATION XSLT 还会输出两个派生字段。ZUGFeRD 1.0 使用旧版 CII 词汇，因此其 XPath 与 2.x 不同：

| DocBits 字段      | 来源（1.0 架构）                                                                                                      | 逻辑                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `CrossIndustryDocument/HeaderExchangedDocument/TypeCode`                                                                 | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票** |
| `INVOICE_SUB_TYPE` | `SpecifiedSupplyChainTradeTransaction/ApplicableSupplyChainTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | 非空 → **采购发票**；为空或缺失 → **费用发票**       |

### 税额明细（按层级分类）

`ApplicableTradeTax` 块会根据税率分配到三个层级（不按位置索引）：标准税率字段（`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`）对应税率 ≥ 19；减税率字段（`*_2`）对应 0 < 税率 < 19；零税率字段（`*_3`）对应税率 = 0。完整字段列表请参阅[ZUGFeRD 税额明细](./#tax-breakdown-tier-classified)。（ZUGFeRD 1.0 在其 TRANSFORMATION XSLT 中使用旧版 CII 词汇，但上述层级选择规则与 2.x 相同。）

### 文档引用

| ZUGFeRD CII 路径                      | DocBits 字段     | Infor BOD 字段   | 类型   | 描述           |
| ------------------------------------- | ----------------- | ----------------- | ------ | -------------- |
| `BuyerOrderReferencedDocument/ID`     | `PURCHASE_ORDER`  | `CustomerOrderID` | STRING | 采购订单编号   |
| `ContractReferencedDocument/ID`       | `CONTRACT_NUMBER` | `ContractID`      | STRING | 合同引用       |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE`   | `ShipmentID`      | STRING | 交货单引用     |

### 供应商（卖方）信息

| ZUGFeRD CII 路径                                   | DocBits 字段        | Infor BOD 字段       | 类型   | 描述       |
| -------------------------------------------------- | -------------------- | --------------------- | ------ | ---------- |
| `SellerTradeParty/ID`                              | `VENDOR_ID`          | `SupplierPartyID`     | STRING | 供应商 ID  |
| `SellerTradeParty/Name`                            | `VENDOR_NAME`        | `SupplierPartyName`   | STRING | 供应商名称 |
| `SellerTradeParty/PostalTradeAddress/Line1`        | `VENDOR_ADDRESS`     | `SupplierAddress1`    | STRING | 地址行 1   |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode`  | STRING | 邮政编码   |
| `SellerTradeParty/PostalTradeAddress/CityName`     | `VENDOR_CITY`        | `SupplierCity`        | STRING | 城市       |
| `SellerTradeParty/PostalTradeAddress/CountryID`    | `VENDOR_COUNTRY`     | `SupplierCountryCode` | STRING | 国家代码   |

## 行项目映射

| ZUGFeRD CII 路径                         | DocBits 字段  | Infor BOD 字段    | 类型   | 描述         |
| ---------------------------------------- | -------------- | ------------------ | ------ | ------------ |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | 行号         |
| `SpecifiedTradeProduct/BuyerAssignedID`  | `ITEM_NUMBER`  | `BuyerItemID`      | STRING | 买方物料编号 |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | 物料描述     |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | 开票数量     |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | 不含税单价   |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | 行项目总额   |
