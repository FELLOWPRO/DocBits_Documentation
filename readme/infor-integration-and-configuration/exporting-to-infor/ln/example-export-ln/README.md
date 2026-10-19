# Esempio di esportazione LN

## Panoramica generale

L'esportazione verso Infor LN consiste nel trasferire in modo strutturato i dati relativi alle fatture da Docbits a Infor LN. I dati sono organizzati in intestazioni, righe fiscali, righe di ricezione e righe di costo. Ogni sezione comprende campi statici, che rimangono costanti tra le transazioni, e campi dinamici, che variano in base ai dettagli della fattura o della transazione.

## Mappature dei campi

### Campi di intestazione

| Campo in Infor LN         | Campo mappato in Docbits | Descrizione                                              |
| ------------------------- | ------------------------ | -------------------------------------------------------- |
| SF\_FinancialCompany      | 0200                     | Società finanziaria                                      |
| SF\_RateDeterminer        | docd                     | Determinante del tasso                                   |
| SF\_ExternalRateFactor    | 1                        | Fattore di tasso esterno                                 |
| SupplierCode              | supplier\_id             | Identificativo del fornitore                             |
| PurchaseType              | purchase\_type           | Tipo di acquisto                                         |
| InvoiceType               | invoice\_sub\_type       | Sottotipo della fattura                                  |
| InvoiceNumberSupplier     | invoice\_id              | Numero di fattura del fornitore                          |
| InvoiceDate               | invoice\_date            | Data della fattura                                       |
| InvoiceCurrency           | currency                 | Valuta utilizzata nella fattura                          |
| TaxCountry                | tax\_country\_1          | Paese fiscale                                            |
| DocumentIDExternalPackage | correlation\_id          | ID del pacchetto esterno                                 |
| IDMReference              | idm\_reference           | Riferimento IDM                                          |
| RateDate                  | invoice\_date            | Data di determinazione del tasso                         |
| Reference                 | reference                | Numero di riferimento                                    |
| InvoiceAmount             | total\_amount            | Importo totale della fattura                             |
| TaxBaseAmount             | total\_net\_amount       | Importo netto totale (prima delle imposte)    |
| InvoiceDocumentType       | invoice\_type            | Tipo di documento (ad es. fattura, nota di credito)      |

### Campi della riga fiscale

| Campo in Infor LN | Campo mappato in Docbits | Descrizione                |
| ----------------- | ------------------------ | -------------------------- |
| LineNumber        | TF\_line\_number         | Numero di riga             |
| TaxSequenceNumber | TF\_line\_number         | Numero di sequenza fiscale |
| TaxCode           | TF\_tax\_code            | Codice fiscale             |
| TaxBaseAmount     | TF\_net\_amount          | Imponibile                 |
| TaxAmount         | TF\_tax\_amount          | Importo dell'imposta       |
| TaxCountry        | TF\_tax\_country         | Paese ai fini fiscali      |

### Campi della riga di ricezione

| Campo in Infor LN | Campo mappato in Docbits | Descrizione                    |
| ----------------- | ------------------------ | ------------------------------ |
| PackingSlip       | TF\_packing\_slip        | Numero della bolla di consegna |
| Order             | TF\_purchase\_order      | Numero dell'ordine di acquisto |
| OrderPosition     | TF\_line\_number         | Numero di riga dell'ordine     |
| Receipt           | TF\_delivery\_number     | Numero di consegna/ricezione   |
| ReceiptLine       | TF\_delivery\_line       | Riga di consegna/ricezione     |
| InvoicedAmount    | TF\_amount               | Importo fatturato              |
| InvoicedQuantity  | TF\_quantity             | Quantità fatturata             |

### Campi della riga di costo

| Campo in Infor LN | Campo mappato in Docbits | Descrizione                         |
| ----------------- | ------------------------ | ----------------------------------- |
| LineNumber        | auto                     | Numero di riga generato automaticamente |
| LedgerAccount     | TF\_ledger\_account      | Conto di contabilità generale       |
| DebitCredit       | invoice\_type            | Indicatore di addebito o accredito  |
| Amount            | TF\_amount               | Importo della transazione           |
| Dimension1-12     | TF\_dimension\_X         | Dimensioni di costo                 |
| Quantity1         | TF\_quantity             | Quantità 1                          |
| Quantity2         | TF\_quantity2            | Quantità 2                          |

## Campi statici

Oltre alle mappature dinamiche, per ogni tipo di riga vengono utilizzati diversi campi statici, predefiniti come segue:

* **Campi statici dell'intestazione**:
  * Financial Company: 0200
  * Rate Determiner: docd
  * External Rate Factor: 1
* **Campi statici della riga di ricezione**:
  * Order Type: purchase
  * Logistic Company: 200
  * Order Sequence: 1
* **Campi statici della riga di costo**:
  * Target Company: 200

### Esempio completo&#x20;

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
