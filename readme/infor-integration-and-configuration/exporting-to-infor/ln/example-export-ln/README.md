# Exemplo de Exportação para o LN

## Visão geral

A exportação para o Infor LN transfere de forma estruturada os dados relacionados a faturas do Docbits para o Infor LN. Os dados são organizados em cabeçalhos, linhas de imposto, linhas de recebimento e linhas de custo. Cada seção inclui campos estáticos, que permanecem constantes em todas as transações, e campos dinâmicos, que variam conforme os detalhes da fatura ou da transação.

## Mapeamento de campos

### Campos do cabeçalho

| Campo no Infor LN         | Campo mapeado no Docbits | Descrição                                           |
| ------------------------- | ------------------------ | --------------------------------------------------- |
| SF\_FinancialCompany      | 0200                     | Empresa financeira                                  |
| SF\_RateDeterminer        | docd                     | Determinador de taxa                                |
| SF\_ExternalRateFactor    | 1                        | Fator de taxa externo                               |
| SupplierCode              | supplier\_id             | Identificador do fornecedor                         |
| PurchaseType              | purchase\_type           | Tipo de compra                                      |
| InvoiceType               | invoice\_sub\_type       | Subtipo da fatura                                   |
| InvoiceNumberSupplier     | invoice\_id              | Número da fatura do fornecedor                      |
| InvoiceDate               | invoice\_date            | Data da fatura                                      |
| InvoiceCurrency           | currency                 | Moeda usada na fatura                               |
| TaxCountry                | tax\_country\_1          | País do imposto                                     |
| DocumentIDExternalPackage | correlation\_id          | ID do pacote externo                                |
| IDMReference              | idm\_reference           | Referência IDM                                      |
| RateDate                  | invoice\_date            | Data de determinação da taxa                        |
| Reference                 | reference                | Número de referência                                |
| InvoiceAmount             | total\_amount            | Valor total da fatura                               |
| TaxBaseAmount             | total\_net\_amount       | Valor líquido total (antes do imposto)              |
| InvoiceDocumentType       | invoice\_type            | Tipo de documento (por exemplo, fatura, nota de crédito) |

### Campos da linha de imposto

| Campo no Infor LN | Campo mapeado no Docbits | Descrição                   |
| ----------------- | ------------------------ | --------------------------- |
| LineNumber        | TF\_line\_number         | Número da linha             |
| TaxSequenceNumber | TF\_line\_number         | Número de sequência do imposto |
| TaxCode           | TF\_tax\_code            | Código do imposto           |
| TaxBaseAmount     | TF\_net\_amount          | Base de cálculo do imposto  |
| TaxAmount         | TF\_tax\_amount          | Valor do imposto            |
| TaxCountry        | TF\_tax\_country         | País do imposto             |

### Campos da linha de recebimento

| Campo no Infor LN | Campo mapeado no Docbits | Descrição                      |
| ----------------- | ------------------------ | ------------------------------ |
| PackingSlip       | TF\_packing\_slip        | Número da guia de remessa      |
| Order             | TF\_purchase\_order      | Número do pedido de compra     |
| OrderPosition     | TF\_line\_number         | Número da linha do pedido      |
| Receipt           | TF\_delivery\_number     | Número da entrega/recebimento  |
| ReceiptLine       | TF\_delivery\_line       | Linha da entrega/recebimento   |
| InvoicedAmount    | TF\_amount               | Valor faturado                 |
| InvoicedQuantity  | TF\_quantity             | Quantidade faturada            |

### Campos da linha de custo

| Campo no Infor LN | Campo mapeado no Docbits | Descrição                          |
| ----------------- | ------------------------ | ---------------------------------- |
| LineNumber        | auto                     | Número de linha gerado automaticamente |
| LedgerAccount     | TF\_ledger\_account      | Conta contábil                     |
| DebitCredit       | invoice\_type            | Indicador de débito ou crédito     |
| Amount            | TF\_amount               | Valor da transação                 |
| Dimension1-12     | TF\_dimension\_X         | Dimensões de custo                 |
| Quantity1         | TF\_quantity             | Quantidade 1                       |
| Quantity2         | TF\_quantity2            | Quantidade 2                       |

## Campos estáticos

Além dos mapeamentos dinâmicos, há vários campos estáticos usados em cada tipo de linha, predefinidos da seguinte forma:

* **Campos estáticos do cabeçalho**:
  * Financial Company: 0200
  * Rate Determiner: docd
  * External Rate Factor: 1
* **Campos estáticos da linha de recebimento**:
  * Order Type: purchase
  * Logistic Company: 200
  * Order Sequence: 1
* **Campos estáticos da linha de custo**:
  * Target Company: 200

### Exemplo completo&#x20;

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
