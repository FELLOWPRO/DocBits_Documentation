# Beispielexport LN

## Allgemeiner Überblick

Beim Export nach Infor ERP / SAP werden rechnungsbezogene Daten strukturiert aus Docbits in Infor ERP / SAP übertragen. Die Daten sind in Kopfzeilen, Steuerzeilen, Wareneingangszeilen und Kostenzeilen gegliedert. Jeder Abschnitt enthält statische Felder, die über alle Transaktionen hinweg konstant bleiben, sowie dynamische Felder, die sich je nach Rechnung bzw. Transaktionsdetails unterscheiden.

## Feldzuordnungen

### Kopffelder

| Feld in Infor ERP / SAP | Zugeordnetes Feld in Docbits | Beschreibung                                         |
| ------------------------- | ----------------------- | ---------------------------------------------------- |
| SF\_FinancialCompany      | 0200                    | Finanzgesellschaft                                   |
| SF\_RateDeterminer        | docd                    | Kursbestimmer                                        |
| SF\_ExternalRateFactor    | 1                       | Externer Kursfaktor                                  |
| SupplierCode              | supplier\_id            | Lieferantenkennung                                   |
| PurchaseType              | purchase\_type          | Einkaufsart                                          |
| InvoiceType               | invoice\_sub\_type      | Untertyp der Rechnung                                |
| InvoiceNumberSupplier     | invoice\_id             | Rechnungsnummer des Lieferanten                      |
| InvoiceDate               | invoice\_date           | Datum der Rechnung                                   |
| InvoiceCurrency           | currency                | In der Rechnung verwendete Währung                   |
| TaxCountry                | tax\_country\_1         | Steuerland                                           |
| DocumentIDExternalPackage | correlation\_id         | ID des externen Pakets                               |
| IDMReference              | idm\_reference          | IDM-Referenz                                         |
| RateDate                  | invoice\_date           | Datum der Kursbestimmung                             |
| Reference                 | reference               | Referenznummer                                       |
| InvoiceAmount             | total\_amount           | Gesamtbetrag der Rechnung                            |
| TaxBaseAmount             | total\_net\_amount      | Nettogesamtbetrag (vor Steuern)                      |
| InvoiceDocumentType       | invoice\_type           | Dokumenttyp (z. B. Rechnung, Gutschrift)             |

### Steuerzeilenfelder

| Feld in Infor ERP / SAP | Zugeordnetes Feld in Docbits | Beschreibung          |
| ----------------- | ----------------------- | --------------------- |
| LineNumber        | TF\_line\_number        | Zeilennummer          |
| TaxSequenceNumber | TF\_line\_number        | Steuerfolgenummer     |
| TaxCode           | TF\_tax\_code           | Steuercode            |
| TaxBaseAmount     | TF\_net\_amount         | Steuerliche Bemessungsgrundlage |
| TaxAmount         | TF\_tax\_amount         | Steuerbetrag          |
| TaxCountry        | TF\_tax\_country        | Land für die Steuer   |

### Wareneingangszeilenfelder

| Feld in Infor ERP / SAP | Zugeordnetes Feld in Docbits | Beschreibung                  |
| ----------------- | ----------------------- | ----------------------------- |
| PackingSlip       | TF\_packing\_slip       | Lieferscheinnummer            |
| Order             | TF\_purchase\_order     | Bestellnummer                 |
| OrderPosition     | TF\_line\_number        | Bestellzeilennummer           |
| Receipt           | TF\_delivery\_number    | Liefer-/Wareneingangsnummer   |
| ReceiptLine       | TF\_delivery\_line      | Liefer-/Wareneingangszeile    |
| InvoicedAmount    | TF\_amount              | Fakturierter Betrag           |
| InvoicedQuantity  | TF\_quantity            | Fakturierte Menge             |

### Kostenzeilenfelder

| Feld in Infor ERP / SAP | Zugeordnetes Feld in Docbits | Beschreibung                      |
| ----------------- | ----------------------- | --------------------------------- |
| LineNumber        | auto                    | Automatisch generierte Zeilennummer |
| LedgerAccount     | TF\_ledger\_account     | Sachkonto                         |
| DebitCredit       | invoice\_type           | Soll-/Haben-Kennzeichen           |
| Amount            | TF\_amount              | Betrag der Transaktion            |
| Dimension1-12     | TF\_dimension\_X        | Kostendimensionen                 |
| Quantity1         | TF\_quantity            | Menge 1                           |
| Quantity2         | TF\_quantity2           | Menge 2                           |

## Statische Felder

Zusätzlich zu den dynamischen Zuordnungen gibt es für jeden Zeilentyp mehrere statische Felder, die wie folgt vordefiniert sind:

* **Statische Kopffelder**:
  * Financial Company: 0200
  * Rate Determiner: docd
  * External Rate Factor: 1
* **Statische Wareneingangszeilenfelder**:
  * Order Type: purchase
  * Logistic Company: 200
  * Order Sequence: 1
* **Statische Kostenzeilenfelder**:
  * Target Company: 200

### Vollständiges Beispiel&#x20;

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
