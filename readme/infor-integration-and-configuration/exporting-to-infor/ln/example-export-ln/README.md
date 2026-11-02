# Exemple d'exportation LN

## Vue d'ensemble

L'exportation vers Infor LN consiste à transférer de manière structurée les données de facture de Docbits vers Infor LN. Les données sont organisées en en-têtes, lignes de taxe, lignes de réception et lignes de coûts. Chaque section comprend des champs statiques, qui restent constants d'une transaction à l'autre, et des champs dynamiques, qui varient selon les détails de la facture ou de la transaction.

## Mappages de champs

### Champs d'en-tête

| Champ dans Infor LN       | Champ mappé dans Docbits | Description                                           |
| ------------------------- | ------------------------ | ----------------------------------------------------- |
| SF\_FinancialCompany      | 0200                     | Société financière                                    |
| SF\_RateDeterminer        | docd                     | Déterminant du taux                                   |
| SF\_ExternalRateFactor    | 1                        | Facteur de taux externe                               |
| SupplierCode              | supplier\_id             | Identifiant du fournisseur                            |
| PurchaseType              | purchase\_type           | Type d'achat                                          |
| InvoiceType               | invoice\_sub\_type       | Sous-type de la facture                               |
| InvoiceNumberSupplier     | invoice\_id              | Numéro de facture du fournisseur                      |
| InvoiceDate               | invoice\_date            | Date de la facture                                    |
| InvoiceCurrency           | currency                 | Devise utilisée dans la facture                       |
| TaxCountry                | tax\_country\_1          | Pays fiscal                                           |
| DocumentIDExternalPackage | correlation\_id          | ID du paquet externe                                  |
| IDMReference              | idm\_reference           | Référence IDM                                         |
| RateDate                  | invoice\_date            | Date de détermination du taux                         |
| Reference                 | reference                | Numéro de référence                                   |
| InvoiceAmount             | total\_amount            | Montant total de la facture                           |
| TaxBaseAmount             | total\_net\_amount       | Montant net total (avant taxe)                        |
| InvoiceDocumentType       | invoice\_type            | Type de document (par ex. facture, avoir)             |

### Champs de ligne de taxe

| Champ dans Infor LN | Champ mappé dans Docbits | Description                |
| ------------------- | ------------------------ | -------------------------- |
| LineNumber          | TF\_line\_number         | Numéro de ligne            |
| TaxSequenceNumber   | TF\_line\_number         | Numéro de séquence de taxe |
| TaxCode             | TF\_tax\_code            | Code de taxe               |
| TaxBaseAmount       | TF\_net\_amount          | Base imposable             |
| TaxAmount           | TF\_tax\_amount          | Montant de la taxe         |
| TaxCountry          | TF\_tax\_country         | Pays fiscal                |

### Champs de ligne de réception

| Champ dans Infor LN | Champ mappé dans Docbits | Description                     |
| ------------------- | ------------------------ | ------------------------------- |
| PackingSlip         | TF\_packing\_slip        | Numéro du bordereau de livraison |
| Order               | TF\_purchase\_order      | Numéro du bon de commande       |
| OrderPosition       | TF\_line\_number         | Numéro de ligne de commande     |
| Receipt             | TF\_delivery\_number     | Numéro de livraison/réception   |
| ReceiptLine         | TF\_delivery\_line       | Ligne de livraison/réception    |
| InvoicedAmount      | TF\_amount               | Montant facturé                 |
| InvoicedQuantity    | TF\_quantity             | Quantité facturée               |

### Champs de ligne de coûts

| Champ dans Infor LN | Champ mappé dans Docbits | Description                          |
| ------------------- | ------------------------ | ------------------------------------ |
| LineNumber          | auto                     | Numéro de ligne généré automatiquement |
| LedgerAccount       | TF\_ledger\_account      | Compte comptable                     |
| DebitCredit         | invoice\_type            | Indicateur de débit ou de crédit     |
| Amount              | TF\_amount               | Montant de la transaction            |
| Dimension1-12       | TF\_dimension\_X         | Dimensions de coûts                  |
| Quantity1           | TF\_quantity             | Quantité 1                           |
| Quantity2           | TF\_quantity2            | Quantité 2                           |

## Champs statiques

En plus des mappages dynamiques, plusieurs champs statiques sont utilisés pour chaque type de ligne et sont prédéfinis comme suit :

* **Champs statiques de l'en-tête** :
  * Financial Company : 0200
  * Déterminateur de taux : docd
  * Facteur de taux externe : 1
* **Champs statiques de la ligne de réception** :
  * Type de commande : achat
  * Logistic Company : 200
  * Order Sequence : 1
* **Champs statiques de la ligne de coûts** :
  * Target Company : 200

### Exemple complet&#x20;

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
