# LN 导出示例

## 总体概述

导出到 Infor LN 的过程，是将与发票相关的数据从 Docbits 以结构化方式传输到 Infor LN。数据分为抬头、税额行、收货行和成本行。每个部分都包含静态字段和动态字段：静态字段在各笔交易中保持不变，动态字段则根据发票或交易详情变化。

## 字段映射

### 抬头字段

| Infor LN 中的字段 | Docbits 中的映射字段 | 描述 |
| ----------------- | ------------------- | ---- |
| SF\_FinancialCompany | 0200 | 财务公司 |
| SF\_RateDeterminer | docd | 汇率确定方式 |
| SF\_ExternalRateFactor | 1 | 外部汇率因子 |
| SupplierCode | supplier\_id | 供应商标识符 |
| PurchaseType | purchase\_type | 采购类型 |
| InvoiceType | invoice\_sub\_type | 发票子类型 |
| InvoiceNumberSupplier | invoice\_id | 供应商发票号 |
| InvoiceDate | invoice\_date | 发票日期 |
| InvoiceCurrency | currency | 发票所用币种 |
| TaxCountry | tax\_country\_1 | 税务国家 |
| DocumentIDExternalPackage | correlation\_id | 外部包 ID |
| IDMReference | idm\_reference | IDM 参考信息 |
| RateDate | invoice\_date | 汇率确定日期 |
| Reference | reference | 参考编号 |
| InvoiceAmount | total\_amount | 发票总金额 |
| TaxBaseAmount | total\_net\_amount | 总净额（税前） |
| InvoiceDocumentType | invoice\_type | 文档类型（例如发票、贷项通知单） |

### 税额行字段

| Infor LN 中的字段 | Docbits 中的映射字段 | 描述 |
| ----------------- | ------------------- | ---- |
| LineNumber | TF\_line\_number | 行号 |
| TaxSequenceNumber | TF\_line\_number | 税额序号 |
| TaxCode | TF\_tax\_code | 税码 |
| TaxBaseAmount | TF\_net\_amount | 应税基数金额 |
| TaxAmount | TF\_tax\_amount | 税额 |
| TaxCountry | TF\_tax\_country | 税务所属国家 |

### 收货行字段

| Infor LN 中的字段 | Docbits 中的映射字段 | 描述 |
| ----------------- | ------------------- | ---- |
| PackingSlip | TF\_packing\_slip | 装箱单编号 |
| Order | TF\_purchase\_order | 采购订单编号 |
| OrderPosition | TF\_line\_number | 订单行号 |
| Receipt | TF\_delivery\_number | 交货/收货编号 |
| ReceiptLine | TF\_delivery\_line | 交货/收货行 |
| InvoicedAmount | TF\_amount | 开票金额 |
| InvoicedQuantity | TF\_quantity | 开票数量 |

### 成本行字段

| Infor LN 中的字段 | Docbits 中的映射字段 | 描述 |
| ----------------- | ------------------- | ---- |
| LineNumber | auto | 自动生成的行号 |
| LedgerAccount | TF\_ledger\_account | 总账科目 |
| DebitCredit | invoice\_type | 借方或贷方标识 |
| Amount | TF\_amount | 交易金额 |
| Dimension1-12 | TF\_dimension\_X | 成本维度 |
| Quantity1 | TF\_quantity | 数量 1 |
| Quantity2 | TF\_quantity2 | 数量 2 |

## 静态字段

除了动态映射外，各类行还使用若干预定义的静态字段：

* **抬头静态字段**：
  * 财务公司：0200
  * 汇率确定方式：docd
  * 外部汇率因子：1
* **收货行静态字段**：
  * 订单类型：purchase
  * 物流公司：200
  * 订单序号：1
* **成本行静态字段**：
  * 目标公司：200

### 完整示例&#x20;

````yaml
```properties
###########################
# Header
###########################

## Header Static Fields
StaticFields=FinancialCompany,RateDeterminer,ExternalRateFactor
SF_FinancialCompany=0200
SF_RateDeterminer=docd
SF_ExternalRateFactor=1

## Header Fields
HeaderFields=SupplierCode,PurchaseType,InvoiceType,InvoiceNumberSupplier,InvoiceDate,InvoiceAmount,InvoiceCurrency,RateDeterminer,RateDate,TaxCountry,TransactionEntryDate,Reference,IDMReference,DocumentIDExternalPackage,TaxBaseAmount,InvoiceDocumentType
HF_SupplierCode=supplier_id
HF_PurchaseType=purchase_type
HF_InvoiceType=invoice_sub_type
HF_InvoiceDate=invoice_date
HF_InvoiceNumberSupplier=invoice_id
HF_InvoiceCurrency=currency
HF_TaxCountry=tax_country_1
#HF_TransactionEntryDate=transaction_entry_date
HF_DocumentIDExternalPackage=correlation_id
HF_IDMReference=idm_reference
HF_RateDate=invoice_date
HF_Reference=reference
HF_InvoiceAmount=total_amount
HF_TaxBaseAmount=total_net_amount
HF_InvoiceDocumentType=invoice_type


###########################
# Tax Line
###########################

## Tax Line Fields
InvoiceTaxFields=LineNumber,TaxSequenceNumber,TaxCode,TaxBaseAmount,TaxAmount,TaxCountry
ITF_LineNumber=TF_line_number
ITF_TaxSequenceNumber=TF_line_number
ITF_TaxCode=TF_tax_code
ITF_TaxBaseAmount=TF_net_amount
ITF_TaxAmount=TF_tax_amount
ITF_TaxCountry=TF_tax_country


###########################
# Receipt Line
###########################

InvoiceReceipt=invoice_table

## Receipt Line Static Fields
InvoiceReceiptStaticFields=OrderType,LogisticCompany
IR_SF_OrderType=purchase
IR_SF_LogisticCompany=200
IR_SF_OrderSequence=1

## Receipt Line Fields
InvoiceReceiptFields=PackingSlip,Order,OrderPosition,Receipt,ReceiptLine,InvoicedAmount,InvoicedQuantity
IRF_PackingSlip=TF_packing_slip
IRF_Order=TF_purchase_order
IRF_OrderPosition=TF_line_number
IRF_OrderSequence=TF_line_sequence
IRF_Receipt=TF_delivery_number
IRF_ReceiptLine=TF_delivery_line
IRF_InvoicedAmount=TF_amount
IRF_InvoicedQuantity=TF_quantity


###########################
# Cost Line
###########################

InvoiceCost=cost_lines

## Cost Line Static Fields
InvoiceCostStaticFields=TargetCompany
IC_SF_TargetCompany=200

## Cost Line Fields
InvoiceCostFields=LineNumber,LedgerAccount,DebitCredit,Amount,Dimension1,Dimension2,Dimension3,Dimension4,Dimension5,Dimension6,Dimension7,Dimension8,Dimension9,Dimension10,Dimension11,Dimension12
ICF_LineNumber=auto
ICF_LedgerAccount=TF_ledger_account
ICF_DebitCredit=invoice_type
ICF_Amount=TF_amount
ICF_Dimension1=TF_dimension_1
ICF_Dimension2=TF_dimension_2
ICF_Dimension3=TF_dimension_3
ICF_Dimension4=TF_dimension_4
ICF_Dimension5=TF_dimension_5
ICF_Dimension6=TF_dimension_6
ICF_Dimension7=TF_dimension_7
ICF_Dimension8=TF_dimension_8
ICF_Dimension9=TF_dimension_9
ICF_Dimension10=TF_dimension_10
ICF_Dimension11=TF_dimension_11
ICF_Dimension12=TF_dimension_12
ICF_Quantity1=TF_quantity
ICF_Quantity2=TF_quantity2
```
````
