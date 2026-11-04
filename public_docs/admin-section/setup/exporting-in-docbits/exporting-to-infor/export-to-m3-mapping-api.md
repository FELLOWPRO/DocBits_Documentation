# Exportation vers M3 Mapping (API)

### Sections

Le fichier de mapping d'exportation M3 est divisé en 5 sections et chaque section est ensuite divisée en 2 sections

* En-tête
* Champs statiques d'en-tête
* Champs d'en-tête
* Lignes de taxe
* Champs statiques de ligne de taxe
* Champs de ligne de taxe
* Lignes de reçu
* Champs statiques de ligne de reçu
* Champs de ligne de reçu
* Lignes de frais de commande (Montants supplémentaires)
* Champs statiques de frais de commande
* Champs de frais de commande
* Lignes de coût
* Champs statiques de ligne de coût
* Champs de ligne de coût

### Ajout et suppression de champs

Ajout d'un nouveau champ :

* Tout d'abord, nous devons ajouter le **nom du champ de l'API M3** à la liste des champs de la section pertinente (par exemple, ChampsStatiques, ChampsEn-tête, Champs de taxe de facture)
* Définir la valeur statique ou le nom du champ de document pour le champ de l'API avec le préfixe approprié pour la section
* Exemple 1 : Pour définir une valeur statique de **AAA** pour le champ de l'API M3 **DIVI.** Tout d'abord, nous avons ajouté DIVI à la propriété **ChampsStatiques**. Ensuite, nous ajoutons une ligne **SF\_DIVI = AAA** car SF\_ est le préfixe pour les champs statiques
* Exemple 2 : Pour mapper le champ d'en-tête **IVDT (date de facture)** au champ invoice\_date de DocBits. Tout d'abord, nous ajoutons IVDT à la propriété **ChampsEn-tête**. Ensuite, nous ajoutons une ligne HF\_IVDT = invoice\_date car HF\_ est le préfixe pour les champs d'en-tête

Suppression d'un champ :

* Il suffit de supprimer le champ de la liste des champs de la section et de supprimer la ligne définissant la valeur pour le champ.

#### **Champs d'API M3 disponibles :**

* Les champs M3 disponibles peuvent être vérifiés en ouvrant l'écran approprié dans M3.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* De même, vous pouvez obtenir les noms de champs pour les lignes

### En-tête :

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Propriété de liste des champs : ChampsStatiques

Préfixe des champs de section : SF\_

Champs disponibles : Vous pouvez mapper n'importe quel champ d'API M3 avec n'importe quelle valeur statique

#### **Champs d'en-tête**

Propriété de liste des champs : ChampsEn-tête

Préfixe des champs de section : HF\_

Champs disponibles : Vous pouvez mapper n'importe quel champ de DocBits avec n'importe quel champ d'API M3

### Ligne de taxe :

#### Champs statiques de ligne de taxe :

Propriété de liste des champs : ChampsStatiquesTaxeFacture

Préfixe des champs de section : IT\_SF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : Vous pouvez mettre n'importe quelle valeur car ce sont des champs statiques

#### Champs de ligne de taxe :

Propriété de liste des champs : ChampsTaxeFacture

Préfixe des champs M3 : ITF\_

Préfixe du champ de table DocBits : TF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : numéro_de_ligne, montant_de_taxe, taux_de_taxe, montant_net, montant_brut, code_fiscal_complet, code_fiscal, pays_de_taxe

### Ligne de reçu :

#### Champs statiques de ligne de reçu :

Propriété de liste des champs : ChampsStatiquesReçuFacture

Préfixe des champs de section : IR\_SF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : Vous pouvez mettre n'importe quelle valeur car ce sont des champs statiques

#### Champs de ligne de reçu :

Propriété de liste des champs : ChampsReçuFacture

Préfixe des champs M3 : IRF\_

Préfixe du champ de table DocBits : TF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : bon_de_livraison, bon_de_commande, numéro_de_ligne, séquence_de_ligne, numéro_de_livraison, ligne_de_livraison, montant, quantité, montant_net_total

### Ligne de frais de commande :

#### Champs statiques de frais de commande :

Propriété de liste des champs : ChampsStatiquesFraisCommande

Préfixe des champs de section : OC\_SF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : Vous pouvez mettre n'importe quelle valeur car ce sont des champs statiques

#### Champs de frais de commande :

Propriété de liste des champs : ChampsFraisCommande

Préfixe des champs M3 : OCF\_

Préfixe du champ de table DocBits : TF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : compte_de_livre, dimension_2-7, montant, quantité, quantité2, position

### Ligne de coût :

#### Champs statiques de ligne de coût :

Propriété de liste des champs : ChampsStatiquesCoûtFacture

Préfixe des champs de section : IC\_SF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : Vous pouvez mettre n'importe quelle valeur car ce sont des champs statiques

#### Champs de ligne de coût :

Propriété de liste des champs : ChampsCoûtFacture

Préfixe des champs M3 : ICF\_

Préfixe du champ de table DocBits : TF\_

Champs M3 disponibles : Veuillez vérifier l'API M3 ou l'interface utilisateur

Champs DocBits disponibles : compte_de_livre, dimension_1-12, montant, quantité, quantité2, position

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
### Pour les clients américains, nous mettons à jour ce mappage en V3
````
```
# Changements de la version 2 à la version 3 : 
- StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,BKID
- SF_DIVI=PJA
+ StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,CONO,GEOC
+ SF_DIVI=RFP
+ SF_CONO=001
- SF_TEPY=J30
- SF_PYME=PTR
+# SF_TEPY=N00
+# SF_PYME=CSH
+# SF_APCD=MHIDALGO
- SF_BKID=001
+ SF_GEOC=999999999
+# SF_BKID=DJ1
- HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN
+ HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID
- HF_CUAM=total_net_amount
+ HF_CUAM=total_net_amount_us
- HF_ACDT=invoice_date
+# HF_ACDT=invoice_date
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
+# HF_GEOC=supplier_geoc
-## Champs statiques de ligne de taxe
- InvoiceTaxStaticFields=RDTP,DIVI,VTCD
- IT_SF_RDTP=3
- IT_SF_DIVI=PJA
+# ## Champs statiques de ligne de taxe
+# InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
+# IT_SF_RDTP=3
+# IT_SF_DIVI=AAA
+# IT_SF_CONO=780
-## Champs de ligne de taxe
- InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
- ITF_VTCD=TF_tax_code
# ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount

###########################
# Ligne de Reçu
###########################

InvoiceReceipt=table_facture

## Champs Statiques de la Ligne de Reçu
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Champs de la Ligne de Reçu
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
IRF_IVQA = TF_quantité
IRF_PUUN = TF_unité
IRF_PUNO = TF_commande_achat
IRF_PNLI = TF_numéro_ligne
IRF_ITNO = TF_numéro_article
IRF_POPN = TF_numéro_article
IRF_SUDO = TF_bon_livraison
IRF_NEPR = TF_prix_unitaire_net
IRF_GRPR = TF_prix_unitaire_brut
IRF_PPUN = TF_prix_code_unité
IRF_NLAM = TF_montant_net
IRF_GLAM = TF_montant_total
IRF_TCHG = TF_frais
IRF_CDC1 = TF_remise

###########################
# Ligne de Frais de Commande
###########################

OrderCharge=frais_commande

## Champs Statiques de la Ligne de Frais de Commande
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=RFP
OC_SF_CONO=001

## Champs de la Ligne de Frais de Commande
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_montant
OCF_CHGT=TF_texte_bon
OCF_CEID=TF_compte_général

###########################
# Ligne de Coût
###########################

InvoiceCost=lignes_coût

## Champs Statiques de la Ligne de Coût
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=RFP
IC_SF_CONO=001

## Champs de la Ligne de Coût
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_montant
ICF_VTXT=TF_texte_bon
ICF_AIT1=TF_compte_général
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=TF_dimension_4
ICF_AIT5=TF_dimension_5
ICF_AIT6=TF_dimension_6
ICF_AIT7=TF_dimension_7
ICF_AO01=TF_objet_comptable_1
ICF_AO02=TF_objet_comptable_2
ICF_AO03=TF_objet_comptable_3
ICF_AO04=TF_objet_comptable_4
ICF_AO05=TF_objet_comptable_5
ICF_AO06=TF_objet_comptable_6
ICF_AO07=TF_objet_comptable_7
```
````

