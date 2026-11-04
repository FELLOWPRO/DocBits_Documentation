# Esportazione al M3 Mapping (API)

### Sezioni

Il file di mapping dell'esportazione M3 è diviso in 5 sezioni e ciascuna sezione è ulteriormente divisa in 2 sezioni

* Intestazione
* Campi Statici Intestazione
* Campi Intestazione
* Righe Fiscali
* Campi Statici Righe Fiscali
* Campi Righe Fiscali
* Righe Ricevuta
* Campi Statici Righe Ricevuta
* Campi Righe Ricevuta
* Righe di Costo dell'Ordine (Importi Aggiuntivi)
* Campi Statici Costo dell'Ordine
* Campi Costo dell'Ordine
* Righe di Costo
* Campi Statici Costo
* Campi Costo

### Aggiunta e Rimozione di Campi

Aggiungere un Nuovo Campo:

* Prima è necessario aggiungere il **nome del campo api M3** alla proprietà della lista dei campi della sezione rilevante (es. CampiStatici, CampiIntestazione, CampiFiscaliFattura)
* Definire il valore statico o il nome del campo del documento per il campo api con il prefisso appropriato per la sezione
* Esempio 1: Per definire un valore statico di **AAA** per il campo api M3 **DIVI.** Prima abbiamo aggiunto DIVI alla proprietà **CampiStatici**. Poi aggiungiamo una riga **SF\_DIVI = AAA** poiché SF\_ è il prefisso per i campi statici
* Esempio 2: Per mappare il campo intestazione **IVDT (data fattura)** al campo data_fattura di DocBits. Prima aggiungiamo IVDT alla proprietà **CampiIntestazione**. Poi aggiungiamo una riga HF\_IVDT = data_fattura poiché HF\_ è il prefisso per i campi intestazione

Rimuovere un Campo:

* Basta rimuovere il campo dalla proprietà della lista dei campi della sezione e rimuovere la riga che definisce il valore per il campo.

#### **Campi Api M3 Disponibili:**

* I campi M3 disponibili possono essere verificati aprendo lo schermo appropriato in M3.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* Allo stesso modo è possibile ottenere i nomi dei campi per le righe

### Intestazione:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Proprietà della Lista dei Campi: CampiStatici

Prefisso Campi Sezione: SF\_

Campi Disponibili: È possibile mappare qualsiasi campo api M3 con qualsiasi valore statico

#### **Campi Intestazione**

Proprietà della Lista dei Campi: CampiIntestazione

Prefisso Campi Sezione: HF\_

Campi Disponibili: È possibile mappare qualsiasi campo DocBits con qualsiasi campo api M3

### Righe Fiscali:

#### Campi Statici Righe Fiscali:

Proprietà della Lista dei Campi: CampiStaticiFiscaliFattura

Prefisso Campi Sezione: IT\_SF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: È possibile inserire qualsiasi valore poiché sono campi statici

#### Campi Righe Fiscali:

Proprietà della Lista dei Campi: CampiFiscaliFattura

Prefisso Campi M3: ITF\_

Prefisso Campo Tabella DocBits: TF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: numero_riga, importo_imposta, aliquota_imposta, importo_netto, importo lordo, codice_imposta_completo, codice_imposta, paese_imposta

### Righe Ricevuta:

#### Campi Statici Righe Ricevuta:

Proprietà della Lista dei Campi: CampiStaticiRicevutaFattura

Prefisso Campi Sezione: IR\_SF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: È possibile inserire qualsiasi valore poiché sono campi statici

#### Campi Righe Ricevuta:

Proprietà della Lista dei Campi: CampiRicevutaFattura

Prefisso Campi M3: IRF\_

Prefisso Campo Tabella DocBits: TF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: bolla_di_spedizione, ordine_di_acquisto, numero_riga, sequenza_riga, numero_consegna, linea_consegna, importo, quantità, importo_netto_totale

### Righe di Costo dell'Ordine:

#### Campi Statici Costo dell'Ordine:

Proprietà della Lista dei Campi: CampiStaticiCostoOrdine

Prefisso Campi Sezione: OC\_SF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: È possibile inserire qualsiasi valore poiché sono campi statici

#### Campi Costo dell'Ordine:

Proprietà della Lista dei Campi: CampiCostoOrdine

Prefisso Campi M3: OCF\_

Prefisso Campo Tabella DocBits: TF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: conto_contabile, dimensione_2-7, importo, quantità, quantità2, posizione

### Righe di Costo:

#### Campi Statici Costo:

Proprietà della Lista dei Campi: CampiStaticiCostoFattura

Prefisso Campi Sezione: IC\_SF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: È possibile inserire qualsiasi valore poiché sono campi statici

#### Campi Costo:

Proprietà della Lista dei Campi: CampiCostoFattura

Prefisso Campi M3: ICF\_

Prefisso Campo Tabella DocBits: TF\_

Campi M3 Disponibili: Si prega di verificare M3 API o UI

Campi DocBits Disponibili: conto_contabile, dimensione_1-12, importo, quantità, quantità2, posizione

Nuovo aggiornamento
```
###########################
# Header
###########################

## Header Static Fields
StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,CONO,BKID
SF_DIVI=AAA
SF_IBTP=20
SF_CONO=780
#SF_BSCD=DE
SF_IMCD=0
SF_TEPY=N00
SF_PYME=SCT
SF_APCD=FABCEO
SF_CRTP=1
SF_GEOC=60290522

## Header Fields
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,BKID
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_net_amount
#HF_VTAM=total_tax_amount
HF_ACDT=invoice_date
#HF_SERS=invoice_sub_type
HF_FTCO=supplier_country_code
HF_PUNO=purchase_order
HF_TXAP=tax_country_1
HF_CORI = correlation_id
HF_PAIN = sqr_field_esr_reference
HF_BKID = custom_field_1


###########################
# Tax Line
###########################

# ## Tax Line Static Fields
# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
# IT_SF_RDTP=3
# IT_SF_DIVI=AAA
# IT_SF_CONO=780

# ## Tax Line Fields
# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
# ITF_VTCD=TF_tax_code
# ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount

###########################
# Receipt Line
###########################

InvoiceReceipt=invoice_table

## Receipt Line Static Fields
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=AAA
IR_SF_SERS=0
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=780

## Receipt Line Fields
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
IRF_IVQA = TF_quantity
IRF_PUUN = TF_unit
IRF_PUNO = TF_purchase_order
IRF_PNLI = TF_line_number
IRF_ITNO = TF_item_number
IRF_POPN = TF_item_number
IRF_SUDO = TF_packing_slip
#IRF_NEPR = TF_net_unit_price
IRF_GRPR = TF_gross_unit_price
IRF_PPUN = TF_unit
#IRF_NLAM = TF_net_amount
IRF_GLAM = TF_total_amount

###########################
# Order Charge Line
###########################

OrderCharge=order_charges

## Order Charge Static Fields
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=AAA
OC_SF_CONO=780

## Order Charge Fields
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_amount
OCF_CHGT=TF_voucher_text
OCF_CEID=TF_ledger_account


###########################
# Cost Line
###########################

InvoiceCost=cost_lines

## Cost Line Static Fields
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=AAA
IC_SF_CONO=780

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
```
### Per i clienti statunitensi aggiorniamo questo mapping a V3
````
```
# Cambiamenti dalla Versione 2 alla Versione 3: 
-StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,BKID
- SF_DIVI=PJA
+ StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO,GEOC
+ SF_DIVI=RFP
+ SF_CONO=001
- SF_TEPY=J30
- SF_PYME=PTR
+ #SF_TEPY=N00
+ #SF_PYME=CSH
+ #SF_APCD=MHIDALGO
- SF_BKID=001
+ SF_GEOC=999999999
+ #SF_BKID=DJ1
- HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN
+ HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
- HF_CUAM=total_net_amount
+ HF_CUAM=total_net_amount_us
- HF_ACDT=invoice_date
+ #HF_ACDT=invoice_date
- HF_CORI = correlation_id
- HF_PAIN = sqr_field_esr_reference
-
+ HF_CORI=correlation_id
+ HF_PAIN=sqr_field_esr_reference
+ HF_TCHG=additional_amount
+ HF_CDC1=negative_amount
+ HF_APCD=buyer_id
+ HF_TEPY=payment_terms
+ HF_PYME=payment_method
+ HF_BKID=bank_id
+ #HF_GEOC=supplier_geoc
-## Campi Statici della Linea Fiscale
- InvoiceTaxStaticFields=RDTP,DIVI,VTCD
- IT_SF_RDTP=3
- IT_SF_DIVI=PJA
+ ## Campi Statici della Linea Fiscale
+ InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
+ IT_SF_RDTP=3
+ IT_SF_DIVI=AAA
+ IT_SF_CONO=780
-## Campi della Linea Fiscale
- InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
- ITF_VTCD=TF_tax_code
+ ## Campi della Linea Fiscale
+ InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
+ ITF_VTCD=TF_tax_code
- InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD
+ InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
- IR_SF_DIVI=PJA
- IR_SF_SERS=0
+ IR_SF_DIVI=RFP
- IR_SF_VTCD=52
+ #IR_SF_VTCD=52
+ IR_SF_CONO=001
- InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
+ InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
- #IRF_PUNO = TF_purchase_order
- #IRF_PNLI = TF_line_number
+ IRF_PUNO = TF_purchase_order
+ IRF_PNLI = TF_line_number
- #IRF_NEPR = TF_net_unit_price
+ IRF_NEPR = TF_net_unit_price
- IRF_PPUN = TF_unit
- #IRF_NLAM = TF_net_amount
+ IRF_PPUN = TF_unit_code_price
+ IRF_NLAM = TF_net_amount
+ IRF_TCHG = TF_charges
+ IRF_CDC1 = TF_discount
- OrderChargeStaticFields=RDTP,DIVI
+ OrderChargeStaticFields=RDTP,DIVI,CONO
- OC_SF_DIVI=PJA
+ OC_SF_DIVI=RFP
+ OC_SF_CONO=001
- InvoiceCostStaticFields=RDTP,DIVI
+ InvoiceCostStaticFields=RDTP,DIVI,CONO
- IC_SF_DIVI=PJA
+ IC_SF_DIVI=RFP
+ IC_SF_CONO=001

###########################
# Intestazione
###########################

## Campi Statici dell'Intestazione
StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO,GEOC
SF_DIVI=RFP
SF_IBTP=20
SF_CONO=001
#SF_BSCD=DE
SF_IMCD=0
#SF_TEPY=N00
#SF_PYME=CSH
#SF_APCD=MHIDALGO
SF_CRTP=1
SF_GEOC=999999999
#SF_BKID=DJ1

## Campi dell'Intestazione
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_net_amount_us
#HF_VTAM=total_tax_amount
#HF_ACDT=invoice_date
HF_SERS=invoice_sub_type
HF_FTCO=supplier_country_code
HF_PUNO=purchase_order
HF_TXAP=tax_country_1
HF_CORI=correlation_id
HF_PAIN=sqr_field_esr_reference
HF_TCHG=additional_amount
HF_CDC1=negative_amount
HF_APCD=buyer_id
HF_TEPY=payment_terms
HF_PYME=payment_method
HF_BKID=bank_id
#HF_GEOC=supplier_geoc

###########################
# Linea Fiscale
###########################

# ## Campi Statici della Linea Fiscale
# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
# IT_SF_RDTP=3
# IT_SF_DIVI=AAA
# IT_SF_CONO=780

# ## Campi della Linea Fiscale
# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
# ITF_VTCD=TF_tax_code
# ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount

###########################
# Riga Ricevuta
###########################

InvoiceReceipt=tabella_fattura

## Campi Statici Riga Ricevuta
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Campi Riga Ricevuta
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
IRF_IVQA = TF_quantità
IRF_PUUN = TF_unità
IRF_PUNO = TF_ordine_di_acquisto
IRF_PNLI = TF_numero_riga
IRF_ITNO = TF_numero_articolo
IRF_POPN = TF_numero_articolo
IRF_SUDO = TF_bolla_di_spedizione
IRF_NEPR = TF_prezzo_unitario_netto
IRF_GRPR = TF_prezzo_unitario lordo
IRF_PPUN = TF_prezzo_codice_unità
IRF_NLAM = TF_importo_netto
IRF_GLAM = TF_importo_totale
IRF_TCHG = TF_costi
IRF_CDC1 = TF_sconto

###########################
# Riga Costo Ordine
###########################

OrderCharge=spese_ordine

## Campi Statici Riga Costo Ordine
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=RFP
OC_SF_CONO=001

## Campi Riga Costo Ordine
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_importo
OCF_CHGT=TF_testo_buono
OCF_CEID=TF_conto_contabile

###########################
# Riga Costo
###########################

InvoiceCost=righe_costo

## Campi Statici Riga Costo
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=RFP
IC_SF_CONO=001

## Campi Riga Costo
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_importo
ICF_VTXT=TF_testo_buono
ICF_AIT1=TF_conto_contabile
ICF_AIT2=TF_dimensione_2
ICF_AIT3=TF_dimensione_3
ICF_AIT4=TF_dimensione_4
ICF_AIT5=TF_dimensione_5
ICF_AIT6=TF_dimensione_6
ICF_AIT7=TF_dimensione_7
ICF_AO01=TF_oggetto_contabile_1
ICF_AO02=TF_oggetto_contabile_2
ICF_AO03=TF_oggetto_contabile_3
ICF_AO04=TF_oggetto_contabile_4
ICF_AO05=TF_oggetto_contabile_5
ICF_AO06=TF_oggetto_contabile_6
ICF_AO07=TF_oggetto_contabile_7
```
````

