# Export nach M3 Mapping (API)

### Abschnitte

Die M3-Exportzuordnungsdatei ist in 5 Abschnitte unterteilt, wobei jeder Abschnitt weiter in 2 Abschnitte unterteilt ist

* Kopfzeile
* Statische Kopfzeilenfelder
* Kopfzeilenfelder
* Steuerzeilen
* Statische Steuerzeilenfelder
* Steuerzeilenfelder
* Belegzeilen
* Statische Belegzeilenfelder
* Belegzeilenfelder
* Auftragskostenzeilen (Zusätzliche Beträge)
* Statische Auftragskostenfelder
* Auftragskostenfelder
* Kostenzeilen
* Statische Kostenzeilenfelder
* Kostenzeilenfelder

### Hinzufügen und Entfernen von Feldern

Hinzufügen eines neuen Feldes:

* Zuerst muss der **M3-API-Feldname** zur Feldliste des entsprechenden Abschnitts hinzugefügt werden (z. B. StaticFields, HeaderFields, InvoiceTaxFields)
* Definieren Sie den statischen Wert oder den Dokumentfeldnamen für das API-Feld mit dem entsprechenden Präfix für den Abschnitt
* Beispiel 1: Um einen statischen Wert von **AAA** für das M3-API-Feld **DIVI** zu definieren, fügen wir zuerst DIVI zur **StaticFields**-Eigenschaft hinzu. Dann fügen wir eine Zeile **SF\_DIVI = AAA** hinzu, da SF\_ das Präfix für statische Felder ist
* Beispiel 2: Um das Kopffeld **IVDT (Rechnungsdatum)** auf das Feld invoice\_date von DocBits abzubilden, fügen wir zuerst IVDT zur **HeaderFields**-Eigenschaft hinzu. Dann fügen wir eine Zeile HF\_IVDT = invoice\_date hinzu, da HF\_ das Präfix für Kopffelder ist

Entfernen eines Feldes:

* Entfernen Sie einfach das Feld aus der Feldliste des Abschnitts und entfernen Sie die Zeile, die den Wert für das Feld definiert.

#### **Verfügbare M3-API-Felder:**

* Verfügbare M3-Felder können über das Öffnen des entsprechenden Bildschirms in M3 überprüft werden.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* Ebenso können Sie Feldnamen für Zeilen erhalten

### Kopfzeile:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Feldliste-Eigenschaft: StaticFields

Abschnittsfeldpräfix: SF\_

Verfügbare Felder: Sie können jedes M3-API-Feld mit einem beliebigen statischen Wert zuordnen

#### **Kopfzeilenfelder**

Feldliste-Eigenschaft: HeaderFields

Abschnittsfeldpräfix: HF\_

Verfügbare Felder: Sie können jedes DocBits-Feld einem beliebigen M3-API-Feld zuordnen

### Steuerzeile:

#### Statische Steuerzeilenfelder:

Feldliste-Eigenschaft: InvoiceTaxStaticFields

Abschnittsfeldpräfix: IT\_SF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: Sie können jeden Wert eingeben, da es sich um statische Felder handelt

#### Steuerzeilenfelder:

Feldliste-Eigenschaft: InvoiceTaxFields

M3-Feldpräfix: ITF\_

DocBits-Tabellenfeldpräfix: TF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Belegzeile:

#### Statische Belegzeilenfelder:

Feldliste-Eigenschaft: InvoiceReceiptStaticFields

Abschnittsfeldpräfix: IR\_SF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: Sie können jeden Wert eingeben, da es sich um statische Felder handelt

#### Belegzeilenfelder:

Feldliste-Eigenschaft: InvoiceReceiptFields

M3-Feldpräfix: IRF\_

DocBits-Tabellenfeldpräfix: TF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Auftragskostenzeile:

#### Statische Auftragskostenfelder:

Feldliste-Eigenschaft: OrderChargeStaticFields

Abschnittsfeldpräfix: OC\_SF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: Sie können jeden Wert eingeben, da es sich um statische Felder handelt

#### Auftragskostenfelder:

Feldliste-Eigenschaft: OrderChargeFields

M3-Feldpräfix: OCF\_

DocBits-Tabellenfeldpräfix: TF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Kostenzeile:

#### Statische Kostenzeilenfelder:

Feldliste-Eigenschaft: InvoiceCostStaticFields

Abschnittsfeldpräfix: IC\_SF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: Sie können jeden Wert eingeben, da es sich um statische Felder handelt

#### Kostenzeilenfelder:

Feldliste-Eigenschaft: InvoiceCostFields

M3-Feldpräfix: ICF\_

DocBits-Tabellenfeldpräfix: TF\_

Verfügbare M3-Felder: Bitte überprüfen Sie M3-API oder UI

Verfügbare DocBits-Felder: ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Neues Update
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
### Für US-Kunden aktualisieren wir dieses Mapping auf V3.
````
```
# Änderungen von Version 2 zu Version 3: 
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
-## Steuerzeilen-Statikfelder
- Rechnungssteuerstatikfelder=RDTP,DIVI,VTCD
- IT_SF_RDTP=3
- IT_SF_DIVI=PJA
+ ## Steuerzeilen-Statikfelder
+ Rechnungssteuerstatikfelder=RDTP,DIVI,VTCD,CONO
+ IT_SF_RDTP=3
+ IT_SF_DIVI=AAA
+ IT_SF_CONO=780
-## Steuerzeilenfelder
- Rechnungssteuerfelder=VTCD,VTA1,VTP1,CLAM
- ITF_VTCD=TF_tax_code
- ITF_VTA1=TF_tax_amount
- ITF_VTP1=TF_tax_rate
- ITF_CLAM=TF_gross_amount
+ ## Steuerzeilenfelder
+ Rechnungssteuerfelder=VTCD,VTA1,VTP1,CLAM
+ ITF_VTCD=TF_tax_code
+ ITF_VTA1=TF_tax_amount
+ ITF_VTP1=TF_tax_rate
+ ITF_CLAM=TF_gross_amount
- Rechnungsbelegstatikfelder=RDTP,DIVI,SERS,RELP,VTCD
+ Rechnungsbelegstatikfelder=RDTP,DIVI,SERS,RELP,VTCD,CONO
- IR_SF_DIVI=PJA
- IR_SF_SERS=0
+ IR_SF_DIVI=RFP
- IR_SF_VTCD=52
+ #IR_SF_VTCD=52
+ IR_SF_CONO=001
- Rechnungsbelegfelder=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
+ Rechnungsbelegfelder=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
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
- Bestellungsstatikfelder=RDTP,DIVI
+ Bestellungsstatikfelder=RDTP,DIVI,CONO
- OC_SF_DIVI=PJA
+ OC_SF_DIVI=RFP
+ OC_SF_CONO=001
- Rechnungskostenstatikfelder=RDTP,DIVI
+ Rechnungskostenstatikfelder=RDTP,DIVI,CONO
- IC_SF_DIVI=PJA
+ IC_SF_DIVI=RFP
+ IC_SF_CONO=001
# ITF_VTA1=TF_steuerbetrag
# ITF_VTP1=TF_steuerquote
# ITF_CLAM=TF_bruttobetrag

###########################
# Belegzeile
###########################

InvoiceReceipt=rechnungstabelle

## Statische Felder der Belegzeile
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Felder der Belegzeile
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
IRF_IVQA = TF_menge
IRF_PUUN = TF_einheit
IRF_PUNO = TF_bestellnummer
IRF_PNLI = TF_zeilennummer
IRF_ITNO = TF_artikelnummer
IRF_POPN = TF_artikelnummer
IRF_SUDO = TF_lieferschein
IRF_NEPR = TF_netto_einzelpreis
IRF_GRPR = TF_brutto_einzelpreis
IRF_PPUN = TF_einheitscode_preis
IRF_NLAM = TF_netto_betrag
IRF_GLAM = TF_gesamtbetrag
IRF_TCHG = TF_kosten
IRF_CDC1 = TF_rabatt

###########################
# Auftragskostenzeile
###########################

OrderCharge=auftragskosten

## Statische Felder der Auftragskosten
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=RFP
OC_SF_CONO=001

## Felder der Auftragskosten
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_betrag
OCF_CHGT=TF_gutschein_text
OCF_CEID=TF_hauptbuchkonto

###########################
# Kostenzeile
###########################

InvoiceCost=kostenzeilen

## Statische Felder der Kostenzeile
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=RFP
IC_SF_CONO=001

## Felder der Kostenzeile
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_betrag
ICF_VTXT=TF_gutschein_text
ICF_AIT1=TF_hauptbuchkonto
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=TF_dimension_4
ICF_AIT5=TF_dimension_5
ICF_AIT6=TF_dimension_6
ICF_AIT7=TF_dimension_7
ICF_AO01=TF_buchungsobjekt_1
ICF_AO02=TF_buchungsobjekt_2
ICF_AO03=TF_buchungsobjekt_3
ICF_AO04=TF_buchungsobjekt_4
ICF_AO05=TF_buchungsobjekt_5
ICF_AO06=TF_buchungsobjekt_6
ICF_AO07=TF_buchungsobjekt_7
```
````

