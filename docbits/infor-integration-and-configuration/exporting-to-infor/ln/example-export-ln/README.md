# Example Export LN

## General Overview

The export to Infor LN involves transferring invoice-related data from Docbits into Infor LN in a structured manner. The data is organized into headers, tax lines, receipt lines, and cost lines. Each section includes static fields that remain constant across transactions and dynamic fields that vary based on the invoice or transaction details.

## Field Mappings

### Header Fields

| Field in Infor LN         | Mapped Field in Docbits | Description                                   |
| ------------------------- | ----------------------- | --------------------------------------------- |
| SF\_FinancialCompany      | 0200                    | Financial company                             |
| SF\_RateDeterminer        | docd                    | Rate determiner                               |
| SF\_ExternalRateFactor    | 1                       | External rate factor                          |
| SupplierCode              | supplier\_id            | Supplier identifier                           |
| PurchaseType              | purchase\_type          | Type of purchase                              |
| InvoiceType               | invoice\_sub\_type      | Subtype of the invoice                        |
| InvoiceNumberSupplier     | invoice\_id             | Supplier's invoice number                     |
| InvoiceDate               | invoice\_date           | Date of the invoice                           |
| InvoiceCurrency           | currency                | Currency used in the invoice                  |
| TaxCountry                | tax\_country\_1         | Tax country                                   |
| DocumentIDExternalPackage | correlation\_id         | External package ID                           |
| IDMReference              | idm\_reference          | IDM reference                                 |
| RateDate                  | invoice\_date           | Rate determination date                       |
| Reference                 | reference               | Reference number                              |
| InvoiceAmount             | total\_amount           | Total invoice amount                          |
| TaxBaseAmount             | total\_net\_amount      | Total net amount (before tax)                 |
| InvoiceDocumentType       | invoice\_type           | Type of document (e.g., invoice, credit note) |

### Tax Line Fields

| Field in Infor LN | Mapped Field in Docbits | Description         |
| ----------------- | ----------------------- | ------------------- |
| LineNumber        | TF\_line\_number        | Line number         |
| TaxSequenceNumber | TF\_line\_number        | Tax sequence number |
| TaxCode           | TF\_tax\_code           | Tax code            |
| TaxBaseAmount     | TF\_net\_amount         | Taxable base amount |
| TaxAmount         | TF\_tax\_amount         | Tax amount          |
| TaxCountry        | TF\_tax\_country        | Country for tax     |

### Receipt Line Fields

| Field in Infor LN | Mapped Field in Docbits | Description             |
| ----------------- | ----------------------- | ----------------------- |
| PackingSlip       | TF\_packing\_slip       | Packing slip number     |
| Order             | TF\_purchase\_order     | Purchase order number   |
| OrderPosition     | TF\_line\_number        | Order line number       |
| Receipt           | TF\_delivery\_number    | Delivery/receipt number |
| ReceiptLine       | TF\_delivery\_line      | Delivery/receipt line   |
| InvoicedAmount    | TF\_amount              | Invoiced amount         |
| InvoicedQuantity  | TF\_quantity            | Invoiced quantity       |

### Cost Line Fields

| Field in Infor LN | Mapped Field in Docbits | Description                |
| ----------------- | ----------------------- | -------------------------- |
| LineNumber        | auto                    | Auto-generated line number |
| LedgerAccount     | TF\_ledger\_account     | Ledger account             |
| DebitCredit       | invoice\_type           | Debit or credit indicator  |
| Amount            | TF\_amount              | Amount in the transaction  |
| Dimension1-12     | TF\_dimension\_X        | Cost dimensions            |
| Quantity1         | TF\_quantity            | Quantity 1                 |
| Quantity2         | TF\_quantity2           | Quantity 2                 |

## Static Fields

In addition to the dynamic mappings, there are several static fields used for each type of line, which are predefined as follows:

* **Header Static Fields**:
  * Financial Company: 0200
  * Rate Determiner: docd
  * External Rate Factor: 1
* **Receipt Line Static Fields**:
  * Order Type: purchase
  * Logistic Company: 200
  * Order Sequence: 1
* **Cost Line Static Fields**:
  * Target Company: 200

### Full Example&#x20;

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
