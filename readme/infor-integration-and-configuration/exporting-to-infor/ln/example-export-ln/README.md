# Przykładowy eksport LN

## Przegląd ogólny

Eksport do Infor LN polega na przesłaniu danych związanych z fakturą z Docbits do Infor LN w uporządkowany sposób. Dane są podzielone na nagłówki, linie podatkowe, linie przyjęć i linie kosztów. Każda sekcja zawiera pola statyczne, które pozostają stałe we wszystkich transakcjach, oraz pola dynamiczne, które różnią się w zależności od szczegółów faktury lub transakcji.

## Mapowanie pól

### Pola nagłówka

| Pole w Infor LN           | Zmapowane pole w Docbits | Opis                                                 |
| ------------------------- | ------------------------ | ---------------------------------------------------- |
| SF\_FinancialCompany      | 0200                     | Spółka finansowa                                     |
| SF\_RateDeterminer        | docd                     | Wyznacznik kursu                                     |
| SF\_ExternalRateFactor    | 1                        | Zewnętrzny współczynnik kursu                        |
| SupplierCode              | supplier\_id             | Identyfikator dostawcy                               |
| PurchaseType              | purchase\_type           | Rodzaj zakupu                                        |
| InvoiceType               | invoice\_sub\_type       | Podtyp faktury                                       |
| InvoiceNumberSupplier     | invoice\_id              | Numer faktury dostawcy                               |
| InvoiceDate               | invoice\_date            | Data faktury                                         |
| InvoiceCurrency           | currency                 | Waluta użyta na fakturze                             |
| TaxCountry                | tax\_country\_1          | Kraj podatkowy                                       |
| DocumentIDExternalPackage | correlation\_id          | Identyfikator pakietu zewnętrznego                   |
| IDMReference              | idm\_reference           | Odwołanie IDM                                        |
| RateDate                  | invoice\_date            | Data ustalenia kursu                                 |
| Reference                 | reference                | Numer referencyjny                                   |
| InvoiceAmount             | total\_amount            | Łączna kwota faktury                                 |
| TaxBaseAmount             | total\_net\_amount       | Łączna kwota netto (przed opodatkowaniem)            |
| InvoiceDocumentType       | invoice\_type            | Rodzaj dokumentu (np. faktura, nota kredytowa)       |

### Pola linii podatkowej

| Pole w Infor LN   | Zmapowane pole w Docbits | Opis                       |
| ----------------- | ------------------------ | -------------------------- |
| LineNumber        | TF\_line\_number         | Numer linii                |
| TaxSequenceNumber | TF\_line\_number         | Numer kolejny podatku      |
| TaxCode           | TF\_tax\_code            | Kod podatku                |
| TaxBaseAmount     | TF\_net\_amount          | Podstawa opodatkowania     |
| TaxAmount         | TF\_tax\_amount          | Kwota podatku              |
| TaxCountry        | TF\_tax\_country         | Kraj podatkowy             |

### Pola linii przyjęcia

| Pole w Infor LN   | Zmapowane pole w Docbits | Opis                            |
| ----------------- | ------------------------ | ------------------------------- |
| PackingSlip       | TF\_packing\_slip        | Numer listu przewozowego        |
| Order             | TF\_purchase\_order      | Numer zamówienia zakupu         |
| OrderPosition     | TF\_line\_number         | Numer linii zamówienia          |
| Receipt           | TF\_delivery\_number     | Numer dostawy/przyjęcia         |
| ReceiptLine       | TF\_delivery\_line       | Linia dostawy/przyjęcia         |
| InvoicedAmount    | TF\_amount               | Zafakturowana kwota             |
| InvoicedQuantity  | TF\_quantity             | Zafakturowana ilość             |

### Pola linii kosztów

| Pole w Infor LN | Zmapowane pole w Docbits | Opis                              |
| --------------- | ------------------------ | --------------------------------- |
| LineNumber      | auto                     | Automatycznie generowany numer linii |
| LedgerAccount   | TF\_ledger\_account      | Konto księgowe                    |
| DebitCredit     | invoice\_type            | Wskaźnik debetu lub kredytu       |
| Amount          | TF\_amount               | Kwota w transakcji                |
| Dimension1-12   | TF\_dimension\_X         | Wymiary kosztów                   |
| Quantity1       | TF\_quantity             | Ilość 1                           |
| Quantity2       | TF\_quantity2            | Ilość 2                           |

## Pola statyczne

Oprócz mapowań dynamicznych dla każdego typu linii używanych jest kilka pól statycznych, które są predefiniowane w następujący sposób:

* **Pola statyczne nagłówka**:
  * Spółka finansowa: 0200
  * Wyznacznik kursu: docd
  * Zewnętrzny współczynnik kursu: 1
* **Pola statyczne linii przyjęcia**:
  * Typ zamówienia: purchase
  * Spółka logistyczna: 200
  * Sekwencja zamówienia: 1
* **Pola statyczne linii kosztów**:
  * Spółka docelowa: 200

### Pełny przykład&#x20;

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
