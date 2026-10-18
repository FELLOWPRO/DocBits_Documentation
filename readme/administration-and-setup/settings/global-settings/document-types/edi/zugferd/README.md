# ZUGFeRD 概览

## 简介

ZUGFeRD（Zentraler User Guide des Forums elektronische Rechnung Deutschland）是一种德国电子发票标准，基于 UN/CEFACT 跨行业发票（CII）和 ISO 19005-3（PDF/A-3）。它将结构化发票数据与 PDF 文件结合起来。

DocBits 从 ZUGFeRD 文档中提取字段，并使用 OAGIS BOD 标准将其与 Infor ERP 系统（M3、LN）匹配。

## 支持的 ZUGFeRD 版本

DocBits 支持多个版本的 ZUGFeRD 标准：

* [ZUGFeRD 1.0](zugferd-1-0.md)
* [ZUGFeRD 2.0](zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](zugferd-2-1.md)
* [ZUGFeRD 2.2](zugferd-2-2.md)
* [ZUGFeRD 2.3](zugferd-2-3.md)
* [ZUGFeRD 2.3.2](zugferd-2-3-2.md)

## 完整的表头字段映射

### 发票标识

| ZUGFeRD CII 路径                  | DocBits 字段       | Infor BOD 字段    | 类型   | 描述         |
| --------------------------------- | ------------------- | ------------------ | ------ | ------------ |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER`    | `DocumentID`       | STRING | 发票编号     |
| `ExchangedDocument/TypeCode`      | `INVOICE_TYPE_CODE` | `DocumentType`     | STRING | 发票类型代码 |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`      | `DocumentDateTime` | DATE   | 发票开具日期 |
| `ExchangedDocument/IncludedNote`  | `INVOICE_NOTE`      | `Note`             | STRING | 发票备注     |

### 文档类型和子类型（由 TRA 驱动）

> **Factur-X** 也采用相同逻辑 — Factur-X 1.x 使用与 ZUGFeRD 2.x 相同的 CII 词汇，因此下方的动态区块也会为两者生成。

除原始的 `INVOICE_TYPE_CODE` 外，默认的 TRANSFORMATION XSLT 还会生成包含两个派生字段的规范 `<INVOICE>` 树：

| DocBits 字段      | 来源                                                                                                                                                    | 逻辑                                                                    |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `INVOICE_TYPE`     | `ExchangedDocument/TypeCode`（ZUGFeRD 1.0 中为 `HeaderExchangedDocument/TypeCode`）                                                                      | UNCL 1001 `381` 或 `261` → **贷项通知单**；其他代码 → **发票** |
| `INVOICE_SUB_TYPE` | 是否存在 `BuyerOrderReferencedDocument/IssuerAssignedID`（2.x 中位于 `ApplicableHeaderTradeAgreement` 下，1.0 中位于 `ApplicableSupplyChainTradeAgreement` 下） | 非空 → **采购发票**；为空或缺失 → **费用发票**       |

`INVOICE_SUB_TYPE` 用于区分与采购订单关联的发票和直接费用发票，以便进行 AP 路由。

### 文档引用

| ZUGFeRD CII 路径                      | DocBits 字段     | Infor BOD 字段   | 类型   | 描述           |
| ------------------------------------- | ----------------- | ----------------- | ------ | -------------- |
| `BuyerOrderReferencedDocument/ID`     | `PURCHASE_ORDER`  | `CustomerOrderID` | STRING | 采购订单编号   |
| `ContractReferencedDocument/ID`       | `CONTRACT_NUMBER` | `ContractID`      | STRING | 合同引用       |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE`   | `ShipmentID`      | STRING | 送货单引用     |

### 日期

| ZUGFeRD CII 路径                                    | DocBits 字段          | Infor BOD 字段      | 类型 | 描述             |
| --------------------------------------------------- | ---------------------- | -------------------- | ---- | ---------------- |
| `ExchangedDocument/IssueDateTime`                   | `INVOICE_DATE`         | `DocumentDateTime`   | DATE | 发票日期         |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE`        | `ActualShipDateTime` | DATE | 交货/发货日期    |
| `SpecifiedTradePaymentTerms/DueDateDateTime`        | `DUE_DATE`             | `PaymentDueDateTime` | DATE | 付款到期日       |
| `BillingSpecifiedPeriod/StartDateTime`              | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | 计费周期开始日期 |
| `BillingSpecifiedPeriod/EndDateTime`                | `BILLING_PERIOD_END`   | `BillingPeriodEnd`   | DATE | 计费周期结束日期 |

### 供应商（卖方）信息

| ZUGFeRD CII 路径                                                       | DocBits 字段        | Infor BOD 字段       | 类型   | 描述       |
| ---------------------------------------------------------------------- | -------------------- | --------------------- | ------ | ---------- |
| `SellerTradeParty/ID`                                                  | `VENDOR_ID`          | `SupplierPartyID`     | STRING | 供应商 ID  |
| `SellerTradeParty/GlobalID`                                            | `VENDOR_GLN`         | `SupplierPartyGLN`    | STRING | 全球位置码 |
| `SellerTradeParty/Name`                                                | `VENDOR_NAME`        | `SupplierPartyName`   | STRING | 供应商名称 |
| `SellerTradeParty/PostalTradeAddress/Line1`                            | `VENDOR_ADDRESS`     | `SupplierAddress1`    | STRING | 地址第 1 行 |
| `SellerTradeParty/PostalTradeAddress/Line2`                            | `VENDOR_ADDRESS_2`   | `SupplierAddress2`    | STRING | 地址第 2 行 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode`                     | `VENDOR_POSTAL_CODE` | `SupplierPostalCode`  | STRING | 邮政编码   |
| `SellerTradeParty/PostalTradeAddress/CityName`                         | `VENDOR_CITY`        | `SupplierCity`        | STRING | 城市       |
| `SellerTradeParty/PostalTradeAddress/CountryID`                        | `VENDOR_COUNTRY`     | `SupplierCountryCode` | STRING | 国家代码   |
| `SellerTradeParty/SpecifiedTaxRegistration/ID`                         | `VAT_NO_EXTRACTED`   | `SupplierTaxID`       | STRING | 增值税登记号 |
| `SellerTradeParty/DefinedTradeContact/EmailURIID`                      | `VENDOR_EMAIL`       | `SupplierEmail`       | STRING | 电子邮箱   |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE`       | `SupplierPhone`       | STRING | 电话       |

### 买方信息

| ZUGFeRD CII 路径                                  | DocBits 字段         | Infor BOD 字段       | 类型   | 描述       |
| ------------------------------------------------- | --------------------- | --------------------- | ------ | ---------- |
| `BuyerTradeParty/ID`                              | `COMPANY_ID`          | `CustomerPartyID`     | STRING | 客户 ID    |
| `BuyerTradeParty/GlobalID`                        | `COMPANY_GLN`         | `CustomerPartyGLN`    | STRING | 全球位置码 |
| `BuyerTradeParty/Name`                            | `COMPANY_NAME`        | `CustomerPartyName`   | STRING | 公司名称   |
| `BuyerTradeParty/PostalTradeAddress/Line1`        | `COMPANY_ADDRESS`     | `CustomerAddress1`    | STRING | 地址第 1 行 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode`  | STRING | 邮政编码   |
| `BuyerTradeParty/PostalTradeAddress/CityName`     | `COMPANY_CITY`        | `CustomerCity`        | STRING | 城市       |
| `BuyerTradeParty/PostalTradeAddress/CountryID`    | `COMPANY_COUNTRY`     | `CustomerCountryCode` | STRING | 国家代码   |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID`     | `COMPANY_VAT_ID`      | `CustomerTaxID`       | STRING | 增值税 ID  |

### 付款信息

| ZUGFeRD CII 路径                                   | DocBits 字段    | Infor BOD 字段 | 类型   | 描述       |
| -------------------------------------------------- | ---------------- | --------------- | ------ | ---------- |
| `PayeePartyCreditorFinancialAccount/IBANID`        | `IBAN_EXTRACTED` | `PayeeIBAN`     | STRING | IBAN       |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC`            | `PayeeBIC`      | STRING | BIC/SWIFT 代码 |
| `SpecifiedTradePaymentTerms/Description`           | `PAYMENT_TERMS`  | `PaymentTerms`  | STRING | 付款条款说明 |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode`    | `PAYMENT_METHOD` | `PaymentMethod` | STRING | 付款方式代码 |

### 货币和金额（表头级别）

| ZUGFeRD CII 路径       | DocBits 字段      | Infor BOD 字段        | 类型   | 描述       |
| ---------------------- | ------------------ | ---------------------- | ------ | ---------- |
| `InvoiceCurrencyCode`  | `CURRENCY`         | `CurrencyCode`         | STRING | 发票货币   |
| `TaxBasisTotalAmount`  | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount`  | AMOUNT | 净额合计   |
| `TaxTotalAmount`       | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount`       | AMOUNT | 税额合计   |
| `GrandTotalAmount`     | `TOTAL_AMOUNT`     | `GrandTotalAmount`     | AMOUNT | 总金额     |
| `DuePayableAmount`     | `AMOUNT_DUE`       | `DuePayableAmount`     | AMOUNT | 应付金额   |
| `TotalPrepaidAmount`   | `PREPAID_AMOUNT`   | `TotalPrepaidAmount`   | AMOUNT | 预付金额   |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT`  | `AllowanceTotalAmount` | AMOUNT | 折让总额   |
| `ChargeTotalAmount`    | `CHARGES`          | `ChargeTotalAmount`    | AMOUNT | 费用总额   |

### 税额明细（按档位分类） <a id="tax-breakdown-tier-classified"></a>

默认的 TRANSFORMATION XSLT 会根据税率，将 `ApplicableTradeTax` 区块分配到三个档位，而不是使用位置索引。每个区块都根据其 `RateApplicablePercent` 匹配到相应档位：

| 档位              | DocBits 字段                                 | 选择规则 |
| ----------------- | -------------------------------------------- | -------- |
| 档位 1（标准）    | `TAX_RATE`、`NET_AMOUNT`、`TAX_AMOUNT`       | 税率 ≥ 19 |
| 档位 2（优惠）    | `TAX_RATE_2`、`NET_AMOUNT_2`、`TAX_AMOUNT_2` | 0 < 税率 < 19 |
| 档位 3（零税率）  | `TAX_RATE_3`、`NET_AMOUNT_3`、`TAX_AMOUNT_3` | 税率 = 0 |

| ZUGFeRD CII 路径                                    | DocBits 字段  | Infor BOD 字段  | 类型   | 描述       |
| --------------------------------------------------- | -------------- | ---------------- | ------ | ---------- |
| `ApplicableTradeTax/RateApplicablePercent`（档位 1） | `TAX_RATE`     | `TaxPercent`     | NUMBER | 标准税率增值税百分比 |
| `ApplicableTradeTax/BasisAmount`（档位 1）           | `NET_AMOUNT`   | `TaxableAmount`  | AMOUNT | 标准税率净额 |
| `ApplicableTradeTax/CalculatedAmount`（档位 1）      | `TAX_AMOUNT`   | `TaxAmount`      | AMOUNT | 标准税率税额 |
| `ApplicableTradeTax/RateApplicablePercent`（档位 2） | `TAX_RATE_2`   | `TaxPercent2`    | NUMBER | 优惠税率增值税百分比 |
| `ApplicableTradeTax/BasisAmount`（档位 2）           | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | 优惠税率净额 |
| `ApplicableTradeTax/CalculatedAmount`（档位 2）      | `TAX_AMOUNT_2` | `TaxAmount2`     | AMOUNT | 优惠税率税额 |
| `ApplicableTradeTax/RateApplicablePercent`（档位 3） | `TAX_RATE_3`   | `TaxPercent3`    | NUMBER | 零税率增值税百分比 |
| `ApplicableTradeTax/BasisAmount`（档位 3）           | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | 零税率净额 |
| `ApplicableTradeTax/CalculatedAmount`（档位 3）      | `TAX_AMOUNT_3` | `TaxAmount3`     | AMOUNT | 零税率税额 |

## 完整的行项目（表格）字段映射

### 行项目标识

| ZUGFeRD CII 路径                         | DocBits 字段          | Infor BOD 字段   | 类型   | 描述          |
| ---------------------------------------- | ---------------------- | ----------------- | ------ | ------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`             | `LineNumber`      | STRING | 行号          |
| `SpecifiedTradeProduct/BuyerAssignedID`  | `ITEM_NUMBER`          | `BuyerItemID`     | STRING | 买方商品编号  |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID`    | STRING | 卖方商品编号  |
| `SpecifiedTradeProduct/GlobalID`         | `ITEM_CODE`            | `ItemCode`        | STRING | 全球 ID（GTIN/EAN） |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`          | `ItemDescription` | STRING | 商品说明      |

### 行项目引用

| ZUGFeRD CII 路径                          | DocBits 字段    | Infor BOD 字段           | 类型   | 描述             |
| ----------------------------------------- | ---------------- | ------------------------- | ------ | ---------------- |
| `BuyerOrderReferencedDocument/ID`         | `PURCHASE_ORDER` | `CustomerOrderID`         | STRING | 行项目级采购订单编号 |
| `BuyerOrderReferencedDocument/LineID`     | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | 采购订单行号     |
| `DespatchAdviceReferencedDocument/ID`     | `DELIVERY_NOTE`  | `ShipmentID`              | STRING | 送货单           |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE`  | `ShipmentLineNumber`      | STRING | 送货单行号       |

### 数量和单位

| ZUGFeRD CII 路径           | DocBits 字段      | Infor BOD 字段    | 类型   | 描述       |
| -------------------------- | ------------------ | ------------------ | ------ | ---------- |
| `BilledQuantity`           | `QUANTITY`         | `InvoicedQuantity` | NUMBER | 开票数量   |
| `BilledQuantity/@unitCode` | `UNIT`             | `UnitCode`         | STRING | 计量单位代码 |
| `PackageQuantity`          | `PACKAGE_QUANTITY` | `PackageQuantity`  | NUMBER | 包装件数   |

### 定价

| ZUGFeRD CII 路径                           | DocBits 字段             | Infor BOD 字段    | 类型   | 描述       |
| ------------------------------------------ | ------------------------- | ------------------ | ------ | ---------- |
| `NetPriceProductTradePrice/ChargeAmount`   | `UNIT_PRICE`              | `UnitPrice`        | AMOUNT | 净单价     |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE`             | `GrossUnitPrice`   | AMOUNT | 含税单价   |
| `NetPriceProductTradePrice/BasisQuantity`  | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | 价格基准数量 |

### 行项目金额

| ZUGFeRD CII 路径             | DocBits 字段  | Infor BOD 字段  | 类型   | 描述       |
| ---------------------------- | -------------- | ---------------- | ------ | ---------- |
| `LineTotalAmount`            | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | 行项目总额 |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT`   | `NetAmount`      | AMOUNT | 行项目净额 |

### 行项目税额

| ZUGFeRD CII 路径                           | DocBits 字段  | Infor BOD 字段   | 类型   | 描述       |
| ------------------------------------------ | -------------- | ----------------- | ------ | ---------- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT`          | `TaxPercent`      | NUMBER | 增值税税率 |
| `ApplicableTradeTax/TypeCode`              | `TAX_CODE`     | `TaxCode`         | STRING | 税类型代码 |
| `ApplicableTradeTax/CategoryCode`          | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | 税类别     |

### 折让和费用（行项目级别）

| ZUGFeRD CII 路径                                 | DocBits 字段      | Infor BOD 字段    | 类型   | 描述         |
| ------------------------------------------------ | ------------------ | ------------------ | ------ | ------------ |
| `AppliedTradeAllowanceCharge/ActualAmount`       | `DISCOUNT`         | `AllowanceAmount`  | AMOUNT | 折扣金额     |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | 折扣百分比   |
| `AppliedTradeAllowanceCharge/ActualAmount`       | `SURCHARGE`        | `ChargeAmount`     | AMOUNT | 附加费金额   |
| `AppliedTradeAllowanceCharge/Reason`             | `ALLOWANCE_REASON` | `AllowanceReason`  | STRING | 折让原因     |

### 其他行项目字段

| ZUGFeRD CII 路径                                              | DocBits 字段            | Infor BOD 字段         | 类型   | 描述         |
| ------------------------------------------------------------- | ------------------------ | ----------------------- | ------ | ------------ |
| `SpecifiedTradeProduct/OriginTradeCountry/ID`                 | `COUNTRY_OF_ORIGIN`      | `CountryOfOrigin`       | STRING | 原产国       |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | 商品特征     |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime`           | `DELIVERY_DATE`          | `ActualDeliveryDate`    | DATE   | 行项目交货日期 |

## 实际生效的规则与激活

如果电子贷项通知单显示为 Invoice，请按照[分类故障排查指南](../credit-note-recognized-as-invoice.md)进行检查。该指南涵盖实际生效的自定义或默认源代码、类型代码、Extraction Paths，以及安全激活步骤。

## 国家指南

请参阅国家指南，了解准确格式名称、语法、版本限制和已检查的配置状态。 [eDocs 格式、版本和国家指南](../supported-electronic-documents/README.md).
