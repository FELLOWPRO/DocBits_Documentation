# Voorbeeld van M3-export



## Algemeen overzicht

Bij de export naar Infor M3 worden factuurgegevens gestructureerd vanuit DocBits overgedragen. De gegevens zijn verdeeld in kopgegevens, belastingregels, ontvangstregels en kostenregels. Elke sectie bevat statische velden die voor transacties gelijk blijven en dynamische velden die afhangen van de factuur of transactie.



## Veldmappings

### Kopvelden

| Veld in Infor M3 | Gekoppeld veld in DocBits    | Beschrijving                  |
| ----------------- | -------------------------- | ---------------------------- |
| HF\_SUNO          | supplier\_id               | Leveranciersidentificatie          |
| HF\_IVDT          | invoice\_date              | Factuurdatum                 |
| HF\_SINO          | invoice\_id                | Factuuridentificatie           |
| HF\_SPYN          | supplier\_id               | Leveranciersidentificatie          |
| HF\_CUCD          | currency                   | Valuta van de factuur |
| HF\_CUAM          | total\_amount              | Totaalbedrag                 |
| HF\_VTAM          | total\_tax\_amount         | Totaal belastingbedrag             |
| HF\_ACDT          | accounting\_date           | Boekingsdatum              |
| HF\_SERS          | invoice\_sub\_type         | Factuursubtype             |
| HF\_FTCO          | supplier\_country\_code    | Landcode van de leverancier        |
| HF\_PUNO          | purchase\_order            | Inkooporder               |
| HF\_TXAP          | tax\_country\_1            | Belastingland                  |
| HF\_CORI          | correlation\_id            | Correlatie-identificatie       |
| HF\_PAIN          | sqr\_field\_esr\_reference | Veldreferentie              |
| HF\_TCHG          | additional\_amount         | Aanvullend bedrag            |
| HF\_CDC1          | negative\_amount           | Negatief bedrag              |
| HF\_APCD          | authorised\_user           | Bevoegde gebruiker              |
| HF\_TEPY          | payment\_terms             | Betalingsvoorwaarden                |
| HF\_PYME          | payment\_method            | Betaalmethode               |
| HF\_BKID          | bank\_id                   | Bankidentificatie              |
| HF\_GEOC          | geo\_code                  | Geografische code                     |
| HF\_TECD          | discount\_term             | Kortingsvoorwaarde                |
| HF\_TXAP          | tax\_applicable            | Belasting van toepassing               |
| HF\_TXIN          | tax\_included              | Inclusief belasting                 |



## Belastingregelvelden

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving         |
| ----------------- | ----------------------- | ------------------- |
| ITF\_VTCD         | TF\_tax\_code           | Belastingcode            |
| ITF\_VTA1         | TF\_tax\_amount         | Belastingbedrag          |
| ITF\_VTP1         | TF\_tax\_rate           | Belastingtarief            |
| ITF\_CLAM         | TF\_gross\_amount       | Brutobedrag        |
| ITF\_DIVI         | company\_id             | Bedrijfsidentificatie |
| ITF\_TTXA         | TF\_amount              | Bedrag              |
| ITF\_TAXC         | TF\_tax\_code           | Belastingcode            |
| ITF\_GEOC         | TF\_geo\_code           | Geografische code            |

## Velden voor extra kosten op orderkopniveau <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3      | Gekoppeld veld in DocBits | Beschrijving |
| ---------------------- | ----------------------- | ----------- |
| OrderExtraChargeFields | NLAM                    | NLAM        |
| OECF\_NLAM             | TF\_amount              | Bedrag      |

## Ontvangstregelvelden

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving           |
| ----------------- | ----------------------- | --------------------- |
| IRF\_IVQA         | TF\_quantity            | Gefactureerde hoeveelheid     |
| IRF\_PUUN         | TF\_unit                | Eenheidsnummer           |
| IRF\_PUNO         | TF\_purchase\_order     | Inkoopordernummer |
| IRF\_PNLI         | TF\_line\_number        | Orderregelnummer     |
| IRF\_ITNO         | TF\_item\_number        | Artikelnummer           |
| IRF\_POPN         | TF\_item\_number        | Artikelnummer           |
| IRF\_SUDO         | TF\_packing\_slip       | Pakbon          |
| IRF\_NEPR         | TF\_net\_unit\_price    | Netto-eenheidsprijs        |
| IRF\_GRPR         | TF\_gross\_unit\_price  | Bruto-eenheidsprijs      |
| IRF\_PPUN         | TF\_unit\_code\_price   | Prijseenheidscode       |
| IRF\_NLAM         | TF\_net\_amount         | Nettobedrag            |
| IRF\_GLAM         | TF\_gross\_amount       | Brutobedrag          |
| IRF\_TCHG         | TF\_charges             | Kosten               |
| IRF\_CDC1         | TF\_discount            | Korting              |
| IRF\_PNLS         | TF\_sub\_line\_number   | Subregelnummer       |
| IRF\_REPN         | TF\_receipt\_number     | Ontvangstnummer        |
| IRF\_DIVI         | company\_id             | Bedrijfsidentificatie   |
| IRF\_IVCW         | TF\_catch\_weight       | Variabel gewicht          |
| IRF\_PUCD         | TF\_unit\_price\_per    | Eenheidsprijs per        |

## Velden voor kosten op orderregelniveau <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving     |
| ----------------- | ----------------------- | --------------- |
| OLCF\_GRPR        | TF\_unit\_price         | Eenheidsprijs      |
| OLCF\_CHGT        | TF\_voucher\_text       | Boekingstekst    |
| OLCF\_CEID        | TF\_costing\_element    | Kostenelement |
| OLCF\_PUNO        | TF\_purchase\_order     | Inkooporder  |
| OLCF\_PNLI        | TF\_line\_number        | Regelnummer     |
| OLCF\_ITNO        | TF\_item\_number        | Artikelnummer     |
| OLCF\_CDSE        | TF\_charge\_sequence    | Kostenvolgnummer |
| OLCF\_PNLS        | TF\_sub\_line\_number   | Subregelnummer |
| OLCF\_REPN        | TF\_receipt\_number     | Ontvangstnummer  |
| OLCF\_IVQA        | TF\_quantity            | Hoeveelheid        |
| OLCF\_SUDO        | TF\_packing\_slip       | Pakbon    |

## Orderkostenregelvelden <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving     |
| ----------------- | ----------------------- | --------------- |
| OCF\_NLAM         | TF\_amount              | Bedrag          |
| OCF\_CEID         | TF\_costing\_element    | Kostenelement |
| OCF\_CDSE         | TF\_charge\_sequence    | Kostenvolgnummer |

### Kostenregelvelden

| Veld in Infor M3 | Gekoppeld veld in DocBits   | Beschrijving               |
| ----------------- | ------------------------- | ------------------------- |
| ICF\_NLAM         | TF\_amount                | Bedrag in de transactie |
| ICF\_VTXT         | TF\_voucher\_text         | Boekingstekst              |
| ICF\_AIT1         | TF\_ledger\_account       | Grootboekrekening            |
| ICF\_AIT2         | TF\_dimension\_2          | Dimensie 2               |
| ICF\_AIT3         | TF\_dimension\_3          | Dimensie 3               |
| ICF\_AIT4         | supplier\_id              | Leveranciersidentificatie       |
| ICF\_AIT5         | TF\_dimension\_5          | Dimensie 5               |
| ICF\_AIT6         | TF\_dimension\_6          | Dimensie 6               |
| ICF\_AIT7         | TF\_dimension\_7          | Dimensie 7               |
| ICF\_AO01         | TF\_accounting\_object\_1 | Boekingsobject 1       |
| ICF\_AO02         | TF\_accounting\_object\_2 | Boekingsobject 2       |
| ICF\_AO03         | TF\_accounting\_object\_3 | Boekingsobject 3       |
| ICF\_AO04         | TF\_accounting\_object\_4 | Boekingsobject 4       |
| ICF\_AO05         | TF\_accounting\_object\_5 | Boekingsobject 5       |
| ICF\_AO06         | TF\_accounting\_object\_6 | Boekingsobject 6       |
| ICF\_AO07         | TF\_accounting\_object\_7 | Boekingsobject 7       |

## Kopvelden voor debetnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits    | Beschrijving             |
| ----------------- | -------------------------- | ----------------------- |
| DN\_HF\_SUNO      | supplier\_id               | Leveranciersidentificatie     |
| DN\_HF\_IVDT      | invoice\_date              | Factuurdatum            |
| DN\_HF\_SINO      | invoice\_id                | Factuuridentificatie     |
| DN\_HF\_SPYN      | supplier\_id               | Leveranciersidentificatie     |
| DN\_HF\_CUCD      | currency                   | Valuta                |
| DN\_HF\_CUAM      | total\_net\_amount\_us     | Totaal nettobedrag VS     |
| DN\_HF\_VTAM      | total\_tax\_amount         | Totaal belastingbedrag        |
| DN\_HF\_ACDT      | invoice\_date              | Invoice\_date           |
| DN\_HF\_SERS      | invoice\_sub\_type         | Factuursubtype        |
| DN\_HF\_FTCO      | supplier\_country\_code    | Landcode van de leverancier   |
| DN\_HF\_TXAP      | tax\_country\_1            | Belastingland             |
| DN\_HF\_CORI      | correlation\_id            | Correlatie-identificatie |
| DN\_HF\_PAIN      | sqr\_field\_esr\_reference | SQR-veld ESR-referentie |
| DN\_HF\_TCHG      | additional\_amount         | Aanvullend bedrag       |
| DN\_HF\_CDC1      | negative\_amount           | Negatief bedrag         |
| DN\_HF\_APCD      | buyer\_id                  | Kopersidentificatie       |
| DN\_HF\_TEPY      | payment\_terms             | Betalingsvoorwaarden           |
| DN\_HF\_PYME      | payment\_method            | Betaalmethode          |
| DN\_HF\_BKID      | bank\_id                   | Bankidentificatie         |
| DN\_HF\_GEOC      | geo\_code                  | Geografische code                |

## Kostenregelvelden voor debetnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="252">Veld in Infor M3</th><th>Gekoppeld veld in DocBits</th><th>Beschrijving</th></tr></thead><tbody><tr><td>DebitNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM,AIT5</td></tr><tr><td>DNCF_NLAM</td><td>TF_amount</td><td>Bedrag</td></tr><tr><td>DNCF_AIT5</td><td>purchase_order</td><td>Inkooporder</td></tr></tbody></table>

## Ontvangstregelvelden voor debetnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving      |
| ----------------- | ----------------------- | ---------------- |
| DNRF\_IVQA        | TF\_quantity            | Hoeveelheid         |
| DNRF\_PUUN        | TF\_unit                | Eenheid             |
| DNRF\_PUNO        | TF\_purchase\_order     | Inkooporder   |
| DNRF\_PNLI        | TF\_line\_number        | Regelnummer      |
| DNRF\_ITNO        | TF\_item\_number        | Artikelnummer      |
| DNRF\_POPN        | TF\_item\_number        | Artikelnummer      |
| DNRF\_SUDO        | TF\_packing\_slip       | Pakbon     |
| DNRF\_NEPR        | TF\_net\_unit\_price    | Netto-eenheidsprijs   |
| DNRF\_GRPR        | TF\_gross\_unit\_price  | Bruto-eenheidsprijs |
| DNRF\_PPUN        | TF\_unit\_code\_price   | Prijseenheidscode  |
| DNRF\_NLAM        | TF\_net\_amount         | Nettobedrag       |
| DNRF\_GLAM        | TF\_gross\_amount       | Brutobedrag     |
| DNRF\_TCHG        | TF\_charges             | Kosten          |
| DNRF\_CDC1        | TF\_discount            | Korting         |

## Kop voor creditnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits    | Beschrijving             |
| ----------------- | -------------------------- | ----------------------- |
| CN\_HF\_SUNO      | supplier\_id               | Leveranciersidentificatie    |
| CN\_HF\_IVDT      | invoice\_date              | Factuurdatum            |
| CN\_HF\_SINO      | invoice\_id                | Factuuridentificatie      |
| CN\_HF\_SPYN      | supplier\_id               | Leveranciersidentificatie     |
| CN\_HF\_CUCD      | currency                   | Valuta                |
| CN\_HF\_CUAM      | total\_net\_amount\_us     | Totaal nettobedrag VS     |
| CN\_HF\_VTAM      | total\_tax\_amount         | Totaal belastingbedrag        |
| CN\_HF\_ACDT      | invoice\_date              | Factuurdatum            |
| CN\_HF\_SERS      | invoice\_sub\_type         | Factuursubtype        |
| CN\_HF\_FTCO      | supplier\_country\_code    | Landcode van de leverancier   |
| CN\_HF\_TXAP      | tax\_country\_1            | Belastingland             |
| CN\_HF\_CORI      | correlation\_id            | Correlatie-identificatie  |
| CN\_HF\_PAIN      | sqr\_field\_esr\_reference | SQR-veld ESR-referentie |
| CN\_HF\_TCHG      | additional\_amount         | Aanvullend bedrag       |
| CN\_HF\_CDC1      | negative\_amount           | Negatief bedrag         |
| CN\_HF\_APCD      | buyer\_id                  | Kopersidentificatie        |
| CN\_HF\_TEPY      | payment\_terms             | Betalingsvoorwaarden           |
| CN\_HF\_PYME      | payment\_method            | Betaalmethode          |
| CN\_HF\_BKID      | bank\_id                   | Bankidentificatie         |
| CN\_HF\_GEOC      | geo\_code                  | Geografische code                |

## Kostenregelvelden voor creditnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="257">Veld in Infor M3</th><th>Gekoppeld veld in DocBits</th><th>Beschrijving</th></tr></thead><tbody><tr><td>CreditNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM, AIT5</td></tr><tr><td>CNCF_NLAM</td><td>TF_amount</td><td>Bedrag</td></tr><tr><td>CNCF_AIT5</td><td>purchase_order</td><td>Inkooporder</td></tr></tbody></table>

## Ontvangstregelvelden voor creditnota’s <a href="#tax-line-fields" id="tax-line-fields"></a>

| Veld in Infor M3 | Gekoppeld veld in DocBits | Beschrijving      |
| ----------------- | ----------------------- | ---------------- |
| CNRF\_IVQA        | TF\_quantity            | Hoeveelheid         |
| CNRF\_PUUN        | TF\_unit                | Eenheid             |
| CNRF\_PUNO        | TF\_purchase\_order     | Inkooporder   |
| CNRF\_PNLI        | TF\_line\_number        | Regelnummer      |
| CNRF\_ITNO        | TF\_item\_number        | Artikelnummer      |
| CNRF\_POPN        | TF\_item\_number        | Artikelnummer      |
| CNRF\_SUDO        | TF\_packing\_slip       | Pakbon     |
| CNRF\_NEPR        | TF\_net\_unit\_price    | Netto-eenheidsprijs   |
| CNRF\_GRPR        | TF\_gross\_unit\_price  | Bruto-eenheidsprijs |
| CNRF\_PPUN        | TF\_unit\_code\_price   | Prijseenheidscode  |
| CNRF\_NLAM        | TF\_net\_amount         | Nettobedrag       |
| CNRF\_GLAM        | TF\_gross\_amount       | Brutobedrag     |
| CNRF\_TCHG        | TF\_charges             | Kosten          |
| CNRF\_CDC1        | TF\_discount            | Korting         |

## Statische velden

Naast de dynamische mappings zijn er per regeltype vooraf gedefinieerde statische velden:

* **Statische kopvelden**:
  * StaticFields=DIVI,IBTP,BSCD,IMCD,APCD,CRTP,CONO,PVLD
  * SF\_DIVI=RFP
  * SF\_IBTP=20
  * SF\_CONO=001
  * SF\_BSCD=DE
  * SF\_IMCD=0
  * SF\_APCD=MHIDALGO
  * SF\_CRTP=1
  * SF\_PVLD=1
* **Statische belastingregelvelden:**
  * InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO,TAXT
  * IT\_SF\_RDTP=3
  * IT\_SF\_DIVI=RFP
  * IT\_SF\_CONO=001
  * IT\_SF\_TAXT=2
* **Statische velden voor extra kosten op orderkopniveau:**
  * OrderExtraChargeStaticFields=RDTP,DIVI,CONO,CDSE,CEID
  * OEC\_SF\_RDTP=2
  * OEC\_SF\_DIVI=RFP
  * OEC\_SF\_CONO=001
  * OEC\_SF\_CEID=INVPD
  * OEC\_SF\_CDSE=99
* **Statische ontvangstregelvelden**:
  * InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * IR\_SF\_RDTP=1
  * IR\_SF\_DIVI=RFP
  * IR\_SF\_RELP=1
  * IR\_SF\_VTCD=52
  * IR\_SF\_CONO=001
* **Statische velden voor kosten op orderregelniveau:**
  * OrderLineChargeStaticFields=RDTP,DIVI,CONO
  * OLC\_SF\_RDTP=5
  * OLC\_SF\_DIVI=RFP
  * OLC\_SF\_CONO=001
* **Statische orderkostenregelvelden:**
  * OrderChargeStaticFields=RDTP,DIVI,CONO
  * OC\_SF\_RDTP=2
  * OC\_SF\_DIVI=RFP
  * OC\_SF\_CONO=001
* **Statische kostenregelvelden**:
  * InvoiceCostStaticFields=RDTP,DIVI,CONO
  * IC\_SF\_RDTP=8
  * IC\_SF\_DIVI=RFP
  * IC\_SF\_CONO=001
* **Statische kopvelden voor debetnota's:**
  * DNStaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO
  * DN\_SF\_DIVI=RFP
  * DN\_SF\_IBTP=20
  * DN\_SF\_CONO=001
  * DN\_SF\_BSCD=DE
  * DN\_SF\_IMCD=0
  * DN\_SF\_TEPY=N00
  * DN\_SF\_PYME=CSH
  * DN\_SF\_APCD=MHIDALGO
  * DN\_SF\_CRTP=1
  * DN\_SF\_BKID=DJ1
* **Statische kostenregelvelden voor debetnota's:**
  * DebitNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * DNC\_SF\_RDTP=8
  * DNC\_SF\_DIVI=RFP
  * DNC\_SF\_CONO=001
  * DNC\_SF\_AIT1=20216
  * DNC\_SF\_AIT3=100
  * DNC\_SF\_AIT6=INVDN
  * DNC\_SF\_AIT7=PP20230
* **Statische ontvangstregelvelden voor debetnota's**
  * DebitNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * DNR\_SF\_RDTP=1
  * DNR\_SF\_DIVI=RFP
  * DNR\_SF\_RELP=1
  * DNR\_SF\_VTCD=52
  * DNR\_SF\_CONO=001
* **Statische kopvelden voor creditnota's:**
  * CNStaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO
  * CN\_SF\_DIVI=RFP
  * CN\_SF\_IBTP=20
  * CN\_SF\_CONO=001
  * CN\_SF\_BSCD=DE
  * CN\_SF\_IMCD=0
  * CN\_SF\_TEPY=N00
  * CN\_SF\_PYME=CSH
  * CN\_SF\_APCD=MHIDALGO
  * CN\_SF\_CRTP=1
  * CN\_SF\_BKID=DJ1
* **Statische kostenregelvelden voor creditnota's:**
  * CreditNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * CNC\_SF\_RDTP=8
  * CNC\_SF\_DIVI=RFP
  * CNC\_SF\_CONO=001
  * CNC\_SF\_AIT1=20216
  * CNC\_SF\_AIT3=100
  * CNC\_SF\_AIT6=INVDN
  * CNC\_SF\_AIT7=PP20230
* **Statische ontvangstregelvelden voor creditnota's:**
  * CreditNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * CNR\_SF\_RDTP=1
  * CNR\_SF\_DIVI=RFP
  * CNR\_SF\_RELP=1
  * CNR\_SF\_VTCD=52
  * CNR\_SF\_CONO=001





## Volledig voorbeeld

```
###########################
# Header
###########################

## Header Static Fields
StaticFields=DIVI,IBTP,BSCD,IMCD,APCD,CRTP,CONO,PVLD
SF_DIVI=RFP
SF_IBTP=20
SF_CONO=001
#SF_BSCD=DE
SF_IMCD=0
#SF_APCD=MHIDALGO
SF_CRTP=1
# Partial validation
#SF_PVLD=1

## Header Fields
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC,TECD,TXAP,TXIN
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_amount
#HF_VTAM=total_tax_amount
#HF_ACDT=invoice_date
#HF_SERS=invoice_sub_type
HF_FTCO=supplier_country_code
HF_PUNO=purchase_order
#HF_TXAP=tax_country_1
HF_CORI=correlation_id
HF_PAIN=sqr_field_esr_reference
HF_TCHG=additional_amount
HF_CDC1=negative_amount
HF_APCD=buyer_id
HF_TEPY=payment_terms
HF_PYME=payment_method
HF_BKID=bank_id
HF_GEOC=geo_code
HF_TECD=discount_term
# Tax applicable
HF_TXAP=tax_applicable
# Tax included
HF_TXIN=tax_included

###########################
# Tax Line
###########################

# ## Tax Line Static Fields
InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO,TAXT
IT_SF_RDTP=3
IT_SF_DIVI=RFP
IT_SF_CONO=001
# Tax Type
IT_SF_TAXT=2

# ## Tax Line Fields
# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
InvoiceTaxFields=TTXA,TAXC,GEOC
# ITF_VTCD=TF_tax_code
# ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount

ITF_TTXA = TF_amount
ITF_TAXC = TF_tax_code
ITF_GEOC = TF_geo_code


###########################
# Order Header Extra Charges
###########################

OrderHeaderExtraCharges=order_xtra_header_charges

## Order Header Extra Charge Static Fields
OrderExtraChargeStaticFields=RDTP,DIVI,CONO,CDSE,CEID
OEC_SF_RDTP=2
OEC_SF_DIVI=RFP
OEC_SF_CONO=001
OEC_SF_CEID=INVPD
OEC_SF_CDSE=99

## Order Header Extra Charge Fields
OrderExtraChargeFields=NLAM
OECF_NLAM=TF_amount


###########################
# Receipt Line
###########################

InvoiceReceipt=invoice_table

## Receipt Line Static Fields
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Receipt Line Fields
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1,REPN,PNLS
IRF_IVQA = TF_quantity
IRF_PUUN = TF_unit
IRF_PUNO = TF_purchase_order
IRF_PNLI = TF_line_number
IRF_ITNO = TF_item_number
IRF_POPN = TF_item_number
IRF_SUDO = TF_packing_slip
#IRF_NEPR = TF_net_unit_price
IRF_GRPR = TF_gross_unit_price
IRF_PPUN = TF_unit_code_price
#IRF_NLAM = TF_net_amount
#IRF_GLAM = TF_gross_amount
IRF_TCHG = TF_charges
IRF_CDC1 = TF_discount
IRF_PNLS = TF_sub_line_number
IRF_REPN = TF_receipt_number


###########################
# Order Line Charges
###########################

OrderLineCharge=order_charges
## Order Charge Static Fields
OrderLineChargeStaticFields=RDTP,DIVI,CONO
OLC_SF_RDTP=5
OLC_SF_DIVI=RFP
OLC_SF_CONO=001

## Order Charge Fields
OrderLineChargeFields=NLAM,CHGT,CEID,PUNO,PNLI,GRPR,ITNO,IVQA,SUDO,CDSE,REPN,PNLS
OLCF_GRPR=TF_unit_price
OLCF_CHGT=TF_voucher_text
OLCF_CEID=TF_costing_element
OLCF_PUNO=TF_purchase_order
OLCF_PNLI=TF_line_number
OLCF_ITNO=TF_item_number
OLCF_CDSE=TF_charge_sequence
OLCF_PNLS = TF_sub_line_number
OLCF_REPN = TF_receipt_number
OLCF_IVQA=TF_quantity
OLCF_SUDO=TF_packing_slip


###########################
# Order Charge Line
###########################

OrderCharge=order_charges

## Order Charge Static Fields
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=RFP
OC_SF_CONO=001

## Order Charge Fields
OrderChargeFields=NLAM,CHGT,CEID,CDSE
OCF_NLAM=TF_amount
OCF_CEID=TF_costing_element
OCF_CDSE=TF_charge_sequence


###########################
# Cost Line
###########################

InvoiceCost=cost_lines

## Cost Line Static Fields
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=RFP
IC_SF_CONO=001

## Cost Line Fields
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_amount
ICF_VTXT=TF_voucher_text
ICF_AIT1=TF_ledger_account
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=TF_dimension_4
ICF_AIT5=TF_dimension_5
ICF_AIT6=TF_dimension_6
ICF_AIT7=TF_dimension_7
ICF_AO01=TF_accounting_object_1
ICF_AO02=TF_accounting_object_2
ICF_AO03=TF_accounting_object_3
ICF_AO04=TF_accounting_object_4
ICF_AO05=TF_accounting_object_5
ICF_AO06=TF_accounting_object_6
ICF_AO07=TF_accounting_object_7


###########################
# Debit Note Header
###########################

## Header Static Fields
DNStaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO
DN_SF_DIVI=RFP
DN_SF_IBTP=20
DN_SF_CONO=001
#DN_SF_BSCD=DE
DN_SF_IMCD=0
#DN_SF_TEPY=N00
#DN_SF_PYME=CSH
#DN_SF_APCD=MHIDALGO
DN_SF_CRTP=1
#DN_SF_BKID=DJ1

## Header Fields
DNHeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC
DN_HF_SUNO=supplier_id
DN_HF_IVDT=invoice_date
DN_HF_SINO=invoice_id
DN_HF_SPYN=supplier_id
DN_HF_CUCD=currency
DN_HF_CUAM=total_net_amount_us
#DN_HF_VTAM=total_tax_amount
#DN_HF_ACDT=invoice_date
#DN_HF_SERS=invoice_sub_type
DN_HF_FTCO=supplier_country_code
DN_HF_TXAP=tax_country_1
DN_HF_CORI=correlation_id
DN_HF_PAIN=sqr_field_esr_reference
DN_HF_TCHG=additional_amount
DN_HF_CDC1=negative_amount
DN_HF_APCD=buyer_id
DN_HF_TEPY=payment_terms
DN_HF_PYME=payment_method
DN_HF_BKID=bank_id
DN_HF_GEOC=geo_code


###########################
# Debit Note Cost Line
###########################

DebiteNoteInvoiceCost=debite_note_cost_lines

## Cost Line Static Fields
DebitNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
DNC_SF_RDTP=8
DNC_SF_DIVI=RFP
DNC_SF_CONO=001
DNC_SF_AIT1=20216
DNC_SF_AIT3=100
DNC_SF_AIT6=INVDN
DNC_SF_AIT7=PP20230

## Cost Line Fields
DebitNoteInvoiceCostFields=NLAM,AIT5
DNCF_NLAM=TF_amount
DNCF_AIT5=purchase_order

###########################
# Debit Note Receipt Line
###########################

DebitNoteReceipt=invoice_table

## Debit Note Receipt Line Static Fields
DebitNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
DNR_SF_RDTP=1
DNR_SF_DIVI=RFP
DNR_SF_RELP=1
#DNR_SF_VTCD=52
DNR_SF_CONO=001

## Debit Note Receipt Line Fields
DebitNoteReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
DNRF_IVQA = TF_quantity
DNRF_PUUN = TF_unit
DNRF_PUNO = TF_purchase_order
DNRF_PNLI = TF_line_number
DNRF_ITNO = TF_item_number
DNRF_POPN = TF_item_number
DNRF_SUDO = TF_packing_slip
#DNRF_NEPR = TF_net_unit_price
DNRF_GRPR = TF_gross_unit_price
DNRF_PPUN = TF_unit_code_price
#DNRF_NLAM = TF_net_amount
#DNRF_GLAM = TF_gross_amount
DNRF_TCHG = TF_charges
DNRF_CDC1 = TF_discount


###########################
# Credit Note Header
###########################

## Header Static Fields
CNStaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO
CN_SF_DIVI=RFP
CN_SF_IBTP=20
CN_SF_CONO=001
#CN_SF_BSCD=DE
CN_SF_IMCD=0
#CN_SF_TEPY=N00
#CN_SF_PYME=CSH
#CN_SF_APCD=MHIDALGO
CN_SF_CRTP=1
#CN_SF_BKID=DJ1

## Header Fields
CNHeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC
CN_HF_SUNO=supplier_id
CN_HF_IVDT=invoice_date
CN_HF_SINO=invoice_id
CN_HF_SPYN=supplier_id
CN_HF_CUCD=currency
CN_HF_CUAM=total_net_amount_us
#CN_HF_VTAM=total_tax_amount
#CN_HF_ACDT=invoice_date
#CN_HF_SERS=invoice_sub_type
CN_HF_FTCO=supplier_country_code
CN_HF_TXAP=tax_country_1
CN_HF_CORI=correlation_id
CN_HF_PAIN=sqr_field_esr_reference
CN_HF_TCHG=additional_amount
CN_HF_CDC1=negative_amount
CN_HF_APCD=buyer_id
CN_HF_TEPY=payment_terms
CN_HF_PYME=payment_method
CN_HF_BKID=bank_id
CN_HF_GEOC=geo_code


###########################
# Credit Note Cost Line
###########################

CreditNoteInvoiceCost=credit_note_cost_lines

## Cost Line Static Fields
CreditNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
CNC_SF_RDTP=8
CNC_SF_DIVI=RFP
CNC_SF_CONO=001
CNC_SF_AIT1=20216
CNC_SF_AIT3=100
CNC_SF_AIT6=INVDN
CNC_SF_AIT7=PP20230

## Cost Line Fields
CreditNoteInvoiceCostFields=NLAM,AIT5
CNCF_NLAM=TF_amount
CNCF_AIT5=purchase_order

###########################
# Credit Note Receipt Line
###########################

CreditNoteReceipt=invoice_table

## Credit Note Receipt Line Static Fields
CreditNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
CNR_SF_RDTP=1
CNR_SF_DIVI=RFP
CNR_SF_RELP=1
#CNR_SF_VTCD=52
CNR_SF_CONO=001

## Credit Note Receipt Line Fields
CeeditNoteReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
CNRF_IVQA = TF_quantity
CNRF_PUUN = TF_unit
CNRF_PUNO = TF_purchase_order
CNRF_PNLI = TF_line_number
CNRF_ITNO = TF_item_number
CNRF_POPN = TF_item_number
CNRF_SUDO = TF_packing_slip
#CNRF_NEPR = TF_net_unit_price
CNRF_GRPR = TF_gross_unit_price
CNRF_PPUN = TF_unit_code_price
#CNRF_NLAM = TF_net_amount
#CNRF_GLAM = TF_gross_amount
CNRF_TCHG = TF_charges
CNRF_CDC1 = TF_discount
```
