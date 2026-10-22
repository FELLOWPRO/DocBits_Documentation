# Voorbeeld van LN-export

## Algemeen overzicht

Bij de export naar Infor LN worden factuurgegevens gestructureerd vanuit DocBits overgedragen. De gegevens zijn verdeeld in kopgegevens, belastingregels, ontvangstregels en kostenregels. Elke sectie bevat statische velden die voor transacties gelijk blijven en dynamische velden die afhangen van de factuur of transactie.

## Veldmappings

### Kopvelden

| Veld in Infor LN         | Gekoppeld veld in DocBits | Beschrijving                                   |
| ------------------------- | ----------------------- | --------------------------------------------- |
| SF\_FinancialCompany      | 0200                    | Financieel bedrijf                             |
| SF\_RateDeterminer        | docd                    | Koersbepaler                               |
| SF\_ExternalRateFactor    | 1                       | Externe koersfactor                          |
| SupplierCode              | supplier\_id            | Leveranciersidentificatie                           |
| PurchaseType              | purchase\_type          | Inkooptype                              |
| InvoiceType               | invoice\_sub\_type      | Factuursubtype                        |
| InvoiceNumberSupplier     | invoice\_id             | Factuurnummer van de leverancier                     |
| InvoiceDate               | invoice\_date           | Factuurdatum                           |
| InvoiceCurrency           | currency                | Valuta van de factuur                  |
| TaxCountry                | tax\_country\_1         | Belastingland                                   |
| DocumentIDExternalPackage | correlation\_id         | Extern pakket-ID                           |
| IDMReference              | idm\_reference          | IDM-referentie                                 |
| RateDate                  | invoice\_date           | Koersbepalingsdatum                       |
| Reference                 | reference               | Referentienummer                              |
| InvoiceAmount             | total\_amount           | Totaal factuurbedrag                          |
| TaxBaseAmount             | total\_net\_amount      | Totaal nettobedrag vóór belasting                 |
| InvoiceDocumentType       | invoice\_type           | Documenttype, bijvoorbeeld factuur of creditnota |

### Belastingregelvelden

| Veld in Infor LN | Gekoppeld veld in DocBits | Beschrijving         |
| ----------------- | ----------------------- | ------------------- |
| LineNumber        | TF\_line\_number        | Regelnummer         |
| TaxSequenceNumber | TF\_line\_number        | Belastingvolgnummer |
| TaxCode           | TF\_tax\_code           | Belastingcode            |
| TaxBaseAmount     | TF\_net\_amount         | Belastbare grondslag |
| TaxAmount         | TF\_tax\_amount         | Belastingbedrag          |
| TaxCountry        | TF\_tax\_country        | Belastingland     |

### Ontvangstregelvelden

| Veld in Infor LN | Gekoppeld veld in DocBits | Beschrijving             |
| ----------------- | ----------------------- | ----------------------- |
| PackingSlip       | TF\_packing\_slip       | Pakbonnummer     |
| Order             | TF\_purchase\_order     | Inkoopordernummer   |
| OrderPosition     | TF\_line\_number        | Orderregelnummer       |
| Receipt           | TF\_delivery\_number    | Leverings-/ontvangstnummer |
| ReceiptLine       | TF\_delivery\_line      | Leverings-/ontvangstregel   |
| InvoicedAmount    | TF\_amount              | Gefactureerd bedrag         |
| InvoicedQuantity  | TF\_quantity            | Gefactureerde hoeveelheid       |

### Kostenregelvelden

| Veld in Infor LN | Gekoppeld veld in DocBits | Beschrijving                |
| ----------------- | ----------------------- | -------------------------- |
| LineNumber        | auto                    | Automatisch gegenereerd regelnummer |
| LedgerAccount     | TF\_ledger\_account     | Grootboekrekening             |
| DebitCredit       | invoice\_type           | Debet-/creditaanduiding  |
| Amount            | TF\_amount              | Bedrag in de transactie  |
| Dimension1-12     | TF\_dimension\_X        | Kostendimensies            |
| Quantity1         | TF\_quantity            | Hoeveelheid 1                 |
| Quantity2         | TF\_quantity2           | Hoeveelheid 2                 |

## Statische velden

Naast de dynamische mappings zijn er per regeltype vooraf gedefinieerde statische velden:

* **Statische kopvelden**:
  * Financieel bedrijf: 0200
  * Koersbepaler: docd
  * Externe koersfactor: 1
* **Statische ontvangstregelvelden**:
  * Ordertype: purchase
  * Logistiek bedrijf: 200
  * Ordervolgnummer: 1
* **Statische kostenregelvelden**:
  * Doelbedrijf: 200

### Volledig voorbeeld&#x20;

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
