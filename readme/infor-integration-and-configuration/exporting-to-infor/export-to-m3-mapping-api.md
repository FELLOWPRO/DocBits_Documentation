# Export vers le mappage M3 (API)

### Sections

Le fichier de mappage d'export M3 est divisé en 5 sections, chacune étant elle-même divisée en 2 sections

* En-tête (Header)
  * Champs statiques de l'en-tête
  * Champs de l'en-tête
* Lignes de taxe (Tax Lines)
  * Champs statiques des lignes de taxe
  * Champs des lignes de taxe
* Lignes de réception (Receipt Lines)
  * Champs statiques des lignes de réception
  * Champs des lignes de réception
* Lignes de frais de commande (Order Charge Lines, montants supplémentaires)
  * Champs statiques des frais de commande
  * Champs des frais de commande
* Lignes de coûts (Cost Lines)
  * Champs statiques des lignes de coûts
  * Champs des lignes de coûts

### Ajout et suppression de champs

Ajout d'un nouveau champ :

* Il faut d'abord ajouter le **nom du champ de l'API M3** à la propriété de liste de champs de la section concernée (p. ex. StaticFields, HeaderFields, InvoiceTaxFields)
* Définissez ensuite la valeur statique ou le nom du champ de document pour le champ de l'API, avec le préfixe approprié pour la section
  * Exemple 1 : pour définir une valeur statique **AAA** pour le champ d'API M3 **DIVI.** Nous avons d'abord ajouté DIVI à la propriété **StaticFields**. Puis nous ajoutons une ligne **SF\_DIVI = AAA**, car SF\_ est le préfixe des champs statiques
  * Exemple 2 : pour mapper le champ d'en-tête **IVDT (invoice data)** au champ invoice\_date de DocBits. Nous ajoutons d'abord IVDT à la propriété **HeaderFields**. Puis nous ajoutons une ligne HF\_IVDT = invoice\_date, car HF\_ est le préfixe des champs d'en-tête

Suppression d'un champ :

* Supprimez simplement le champ de la propriété de liste de champs de la section et supprimez la ligne qui définit la valeur du champ.

#### **Champs de l'API M3 disponibles :**

* Les champs M3 disponibles peuvent être consultés en ouvrant l'écran approprié dans M3.

<figure><img src="../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt="Panneau d'état de lot M3 avec le message indiquant que la facture fournisseur 202300373 existe déjà et les champs d'informations détaillées"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt="Boîte de dialogue Field Information de M3 pour le champ WEEORN de la table FAPIBH avec le nom de panneau APA4S50E0, le type String, une longueur maximale de 30 et un bouton Copy to clipboard"><figcaption></figcaption></figure>

* Vous pouvez obtenir de la même manière les noms des champs pour les lignes

### En-tête (Header) :

<figure><img src="../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt="Extrait de code du mappage M3 dans la section Header Static Fields avec StaticFields=DIVI,IBTP,BSCD et des valeurs statiques comme SF_DIVI=PJA et SF_IBTP=20"><figcaption></figcaption></figure>

Propriété de liste de champs : StaticFields

Préfixe des champs de la section : SF\_

Champs disponibles : vous pouvez mapper n'importe quel champ de l'API M3 avec n'importe quelle valeur statique

#### **Champs de l'en-tête**

Propriété de liste de champs : HeaderFields

Préfixe des champs de la section : HF\_

Champs disponibles : vous pouvez mapper n'importe quel champ DocBits à n'importe quel champ de l'API M3

### Ligne de taxe (Tax Line) :

#### Champs statiques de la ligne de taxe :

Propriété de liste de champs : InvoiceTaxStaticFields

Préfixe des champs de la section : IT\_SF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : vous pouvez saisir n'importe quelle valeur, car ce sont des champs statiques

#### Champs de la ligne de taxe :

Propriété de liste de champs : InvoiceTaxFields

Préfixe des champs M3 : ITF\_

Préfixe des champs de tableau DocBits : TF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Ligne de réception (Receipt Line) :

#### Champs statiques de la ligne de réception :

Propriété de liste de champs : InvoiceReceiptStaticFields

Préfixe des champs de la section : IR\_SF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : vous pouvez saisir n'importe quelle valeur, car ce sont des champs statiques

#### Champs de la ligne de réception :

Propriété de liste de champs : InvoiceReceiptFields

Préfixe des champs M3 : IRF\_

Préfixe des champs de tableau DocBits : TF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Ligne de frais de commande (Order Charge Line) :

#### Champs statiques des frais de commande :

Propriété de liste de champs : OrderChargeStaticFields

Préfixe des champs de la section : OC\_SF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : vous pouvez saisir n'importe quelle valeur, car ce sont des champs statiques

#### Champs des frais de commande :

Propriété de liste de champs : OrderChargeFields

Préfixe des champs M3 : OCF\_

Préfixe des champs de tableau DocBits : TF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Ligne de coûts (Cost Line) :

#### Champs statiques de la ligne de coûts :

Propriété de liste de champs : InvoiceCostStaticFields

Préfixe des champs de la section : IC\_SF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : vous pouvez saisir n'importe quelle valeur, car ce sont des champs statiques

#### Champs de la ligne de coûts :

Propriété de liste de champs : InvoiceCostFields

Préfixe des champs M3 : ICF\_

Préfixe des champs de tableau DocBits : TF\_

Champs M3 disponibles : veuillez consulter l'API ou l'interface M3

Champs DocBits disponibles : ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Nouvelle mise à jour

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

### Pour les clients US, nous mettons à jour ce mappage vers la V3

````
```
# Changes from Version 2 to Version 3:# -StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,BKID
# -SF_DIVI=PJA
# +StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO,GEOC
# +SF_DIVI=RFP
# +SF_CONO=001
# -SF_TEPY=J30
# -SF_PYME=PTR
# +#SF_TEPY=N00
# +#SF_PYME=CSH
# +#SF_APCD=MHIDALGO
# -SF_BKID=001
# +SF_GEOC=999999999
# +#SF_BKID=DJ1
# -HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN
# +HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
# -HF_CUAM=total_net_amount
# +HF_CUAM=total_net_amount_us
# -HF_ACDT=invoice_date
# +#HF_ACDT=invoice_date
# -HF_CORI = correlation_id
# -HF_PAIN = sqr_field_esr_reference
# -
# +HF_CORI=correlation_id
# +HF_PAIN=sqr_field_esr_reference
# +HF_TCHG=additional_amount
# +HF_CDC1=negative_amount
# +HF_APCD=buyer_id
# +HF_TEPY=payment_terms
# +HF_PYME=payment_method
# +HF_BKID=bank_id
# +#HF_GEOC=supplier_geoc
# -## Tax Line Static Fields
# -InvoiceTaxStaticFields=RDTP,DIVI,VTCD
# -IT_SF_RDTP=3
# -IT_SF_DIVI=PJA
# +# ## Tax Line Static Fields
# +# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
# +# IT_SF_RDTP=3
# +# IT_SF_DIVI=AAA
# +# IT_SF_CONO=780
# -## Tax Line Fields
# -InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
# -ITF_VTCD=TF_tax_code
# -ITF_VTA1=TF_tax_amount
# -ITF_VTP1=TF_tax_rate
# -ITF_CLAM=TF_gross_amount
# +# ## Tax Line Fields
# +# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
# +# ITF_VTCD=TF_tax_code
# +# ITF_VTA1=TF_tax_amount
# +# ITF_VTP1=TF_tax_rate
# +# ITF_CLAM=TF_gross_amount
# -InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD
# +InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
# -IR_SF_DIVI=PJA
# -IR_SF_SERS=0
# +IR_SF_DIVI=RFP
# -IR_SF_VTCD=52
# +#IR_SF_VTCD=52
# +IR_SF_CONO=001
# -InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM
# +InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
# -#IRF_PUNO = TF_purchase_order
# -#IRF_PNLI = TF_line_number
# +IRF_PUNO = TF_purchase_order
# +IRF_PNLI = TF_line_number
# -#IRF_NEPR = TF_net_unit_price
# +IRF_NEPR = TF_net_unit_price
# -IRF_PPUN = TF_unit
# -#IRF_NLAM = TF_net_amount
# +IRF_PPUN = TF_unit_code_price
# +IRF_NLAM = TF_net_amount
# +IRF_TCHG = TF_charges
# +IRF_CDC1 = TF_discount
# -OrderChargeStaticFields=RDTP,DIVI
# +OrderChargeStaticFields=RDTP,DIVI,CONO
# -OC_SF_DIVI=PJA
# +OC_SF_DIVI=RFP
# +OC_SF_CONO=001
# -InvoiceCostStaticFields=RDTP,DIVI
# +InvoiceCostStaticFields=RDTP,DIVI,CONO
# -IC_SF_DIVI=PJA
# +IC_SF_DIVI=RFP
# +IC_SF_CONO=001

###########################
# Header
###########################

## Header Static Fields
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

## Header Fields
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_net_amount_us
#HF_VTAM=total_tax_amount
#HF_ACDT=invoice_date
#HF_SERS=invoice_sub_type
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
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Receipt Line Fields
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
IRF_IVQA = TF_quantity
IRF_PUUN = TF_unit
IRF_PUNO = TF_purchase_order
IRF_PNLI = TF_line_number
IRF_ITNO = TF_item_number
IRF_POPN = TF_item_number
IRF_SUDO = TF_packing_slip
IRF_NEPR = TF_net_unit_price
IRF_GRPR = TF_gross_unit_price
IRF_PPUN = TF_unit_code_price
IRF_NLAM = TF_net_amount
IRF_GLAM = TF_total_amount
IRF_TCHG = TF_charges
IRF_CDC1 = TF_discount

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
```
````
