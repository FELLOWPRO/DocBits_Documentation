# XRechnung 3.0.2 CII 字段映射

## 概览

本文档介绍 XRechnung 3.0.2 CII（跨行业发票）格式的完整字段映射流程。

## 1. CII XML 结构

XRechnung CII 使用 UN/CEFACT 跨行业发票格式，并包含以下命名空间：

| 前缀 | 命名空间 | 用途 |
| :--- | :--- | :--- |
| `rsm` | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` | 根容器 |
| `ram` | `urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100` | 业务实体 |
| `qdt` | `urn:un:unece:uncefact:data:standard:QualifiedDataType:100` | 限定数据类型 |
| `udt` | `urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100` | 非限定数据类型 |

**分类 URN**：`urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0.2`

## 2. CII XML → DocBits 字段提取

### 标头字段

| CII XML 路径 | DocBits 字段 | 数据类型 |
| :--- | :--- | :--- |
| `ExchangedDocument/ID` | `invoice_id` | 字符串 |
| `ExchangedDocument/TypeCode` | `invoice_type` | 字符串 |
| `ExchangedDocument/IssueDateTime/DateTimeString` | `invoice_date` | 日期（YYYYMMDD） |
| `ApplicableHeaderTradeAgreement/BuyerReference` | `buyer_reference` | 字符串 |
| `BuyerOrderReferencedDocument/IssuerAssignedID` | `purchase_order` | 字符串 |
| `ActualDeliverySupplyChainEvent/.../DateTimeString` | `ship_date` | 日期 |
| `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString` | `due_date` | 日期 |
| `ApplicableHeaderTradeSettlement/InvoiceCurrencyCode` | `currency` | 字符串 |

### 文档类型分类

在 `invoice_type` 接收数值 `TypeCode` 之前，TRANSFORMATION XSLT 会将其替换为易读标签：

| UNCL 1001 代码 | 含义 | DocBits `invoice_type` |
| :--- | :--- | :--- |
| `381` / `261` | 贷项通知单 / 自开贷项通知单 | **贷项通知单** |
| 任何其他代码（`380`、`383`、`384`、`386`、`389`、`325`、…） | 发票 / 借项 / 形式发票 / 等 | **发票** |

### 供应商字段

| CII XML 路径 | DocBits 字段 |
| :--- | :--- |
| `SellerTradeParty/ID` | `supplier_id` |
| `SellerTradeParty/Name` | `supplier_name` |
| `SellerTradeParty/PostalTradeAddress/LineOne` | `supplier_address` |
| `SellerTradeParty/PostalTradeAddress/CityName` | `supplier_city` |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `supplier_postal_code` |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `supplier_country` |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `supplier_vat` |
| `PayeePartyCreditorFinancialAccount/IBANID` | `iban` |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `bic` |

### 客户字段

| CII XML 路径 | DocBits 字段 |
| :--- | :--- |
| `BuyerTradeParty/ID` | `customer_id` |
| `BuyerTradeParty/Name` | `customer_name` |
| `BuyerTradeParty/PostalTradeAddress/LineOne` | `customer_address` |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `customer_vat` |

### 金额字段

| CII XML 路径 | DocBits 字段 |
| :--- | :--- |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxBasisTotalAmount` | `net_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxTotalAmount` | `tax_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/GrandTotalAmount` | `total_amount` |
| `ApplicableTradeTax/RateApplicablePercent` | `tax_rate` |
| `ApplicableTradeTax/BasisAmount` | `taxable_amount` |

### 行项目字段

| CII XML 路径 | DocBits 表格列 |
| :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_NUMBER` |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` |
| `SpecifiedTradeProduct/SellerAssignedID` | `SELLER_ITEM_ID` |
| `SpecifiedTradeProduct/BuyerAssignedID` | `BUYER_ITEM_ID` |
| `SpecifiedLineTradeDelivery/BilledQuantity` | `QUANTITY` |
| `BilledQuantity/@unitCode` | `UNIT` |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` |
| `SpecifiedTradeSettlementLineMonetarySummation/LineTotalAmount` | `TOTAL_AMOUNT` |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT_RATE` |
| `ApplicableTradeTax/CategoryCode` | `VAT_CATEGORY` |

## 3. DocBits → Infor BOD 导出（SyncSupplierInvoice）

### 标头映射

| DocBits 字段 | BOD XML 路径 |
| :--- | :--- |
| `INVOICE_NUMBER` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentID/ID` |
| `INVOICE_DATE` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentDateTime` |
| `VENDOR_ID` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/PartyIDs/ID` |
| `VENDOR_NAME` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/Name` |
| `TOTAL_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/TotalAmount` |
| `NET_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/ExtendedBaseAmount` |
| `TAX_AMOUNT` |（根据 ExtendedAmount - ExtendedBaseAmount 计算） |
| `CURRENCY` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/CurrencyExchangeRate/SourceCurrencyCode` |
| `PAYMENT_TERMS` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/PaymentTerm/Term/Description` |
| `PURCHASE_ORDER` | `UserArea/Property/NameValue[@name='PONumber']` |

### 行项目映射

| DocBits 列 | BOD XML 路径 |
| :--- | :--- |
| `POSITION` | `SupplierInvoiceDetail/LineNumber` |
| `ITEM_NUMBER` | `SupplierInvoiceDetail/Item/ItemID/ID` |
| `DESCRIPTION` | `SupplierInvoiceDetail/Item/Description` |
| `QUANTITY` | `SupplierInvoiceDetail/InvoicedQuantity` |
| `UNIT` | `SupplierInvoiceDetail/InvoicedQuantity/@unitCode` |
| `UNIT_PRICE` | `SupplierInvoiceDetail/UnitPrice/Amount` |
| `TOTAL_AMOUNT` | `SupplierInvoiceDetail/ExtendedAmount` |
