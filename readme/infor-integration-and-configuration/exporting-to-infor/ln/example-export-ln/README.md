# Ejemplo de exportación a Infor ERP / SAP

## Descripción general

La exportación a Infor ERP / SAP consiste en transferir de forma estructurada los datos relacionados con facturas desde Docbits a Infor ERP / SAP. Los datos se organizan en cabeceras, líneas de impuestos, líneas de recepción y líneas de costes. Cada sección incluye campos estáticos que permanecen constantes entre transacciones y campos dinámicos que varían según los detalles de la factura o de la transacción.

## Asignaciones de campos

### Campos de cabecera

| Campo en Infor LN         | Campo asignado en Docbits | Descripción                                   |
| ------------------------- | ----------------------- | --------------------------------------------- |
| SF\_FinancialCompany      | 0200                    | Empresa financiera                            |
| SF\_RateDeterminer        | docd                    | Determinante del tipo de cambio               |
| SF\_ExternalRateFactor    | 1                       | Factor de tipo de cambio externo              |
| SupplierCode              | supplier\_id            | Identificador del proveedor                   |
| PurchaseType              | purchase\_type          | Tipo de compra                                |
| InvoiceType               | invoice\_sub\_type      | Subtipo de la factura                         |
| InvoiceNumberSupplier     | invoice\_id             | Número de factura del proveedor               |
| InvoiceDate               | invoice\_date           | Fecha de la factura                           |
| InvoiceCurrency           | currency                | Moneda utilizada en la factura                |
| TaxCountry                | tax\_country\_1         | País fiscal                                   |
| DocumentIDExternalPackage | correlation\_id         | ID del paquete externo                        |
| IDMReference              | idm\_reference          | Referencia IDM                                |
| RateDate                  | invoice\_date           | Fecha de determinación del tipo de cambio     |
| Reference                 | reference               | Número de referencia                          |
| InvoiceAmount             | total\_amount           | Importe total de la factura                   |
| TaxBaseAmount             | total\_net\_amount      | Importe neto total (antes de impuestos)       |
| InvoiceDocumentType       | invoice\_type           | Tipo de documento (p. ej., factura, abono)    |

### Campos de línea de impuestos

| Campo en Infor LN | Campo asignado en Docbits | Descripción                  |
| ----------------- | ----------------------- | ---------------------------- |
| LineNumber        | TF\_line\_number        | Número de línea              |
| TaxSequenceNumber | TF\_line\_number        | Número de secuencia fiscal   |
| TaxCode           | TF\_tax\_code           | Código de impuesto           |
| TaxBaseAmount     | TF\_net\_amount         | Base imponible               |
| TaxAmount         | TF\_tax\_amount         | Importe del impuesto         |
| TaxCountry        | TF\_tax\_country        | País del impuesto            |

### Campos de línea de recepción

| Campo en Infor LN | Campo asignado en Docbits | Descripción                      |
| ----------------- | ----------------------- | -------------------------------- |
| PackingSlip       | TF\_packing\_slip       | Número del albarán               |
| Order             | TF\_purchase\_order     | Número de la orden de compra     |
| OrderPosition     | TF\_line\_number        | Número de línea del pedido       |
| Receipt           | TF\_delivery\_number    | Número de entrega/recepción      |
| ReceiptLine       | TF\_delivery\_line      | Línea de entrega/recepción       |
| InvoicedAmount    | TF\_amount              | Importe facturado                |
| InvoicedQuantity  | TF\_quantity            | Cantidad facturada               |

### Campos de línea de costes

| Campo en Infor LN | Campo asignado en Docbits | Descripción                         |
| ----------------- | ----------------------- | ----------------------------------- |
| LineNumber        | auto                    | Número de línea autogenerado        |
| LedgerAccount     | TF\_ledger\_account     | Cuenta contable                     |
| DebitCredit       | invoice\_type           | Indicador de débito o crédito       |
| Amount            | TF\_amount              | Importe de la transacción           |
| Dimension1-12     | TF\_dimension\_X        | Dimensiones de costes               |
| Quantity1         | TF\_quantity            | Cantidad 1                          |
| Quantity2         | TF\_quantity2           | Cantidad 2                          |

## Campos estáticos

Además de las asignaciones dinámicas, se utilizan varios campos estáticos para cada tipo de línea, que están predefinidos de la siguiente manera:

* **Campos estáticos de cabecera**:
  * Financial Company: 0200
  * Rate Determiner: docd
  * External Rate Factor: 1
* **Campos estáticos de línea de recepción**:
  * Order Type: purchase
  * Logistic Company: 200
  * Order Sequence: 1
* **Campos estáticos de línea de costes**:
  * Target Company: 200

### Ejemplo completo&#x20;

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
