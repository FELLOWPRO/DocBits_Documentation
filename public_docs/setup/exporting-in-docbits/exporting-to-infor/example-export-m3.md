
General Overview
The export to Infor M3 involves transferring invoice-related data from Docbits into Infor M3 in a structured manner. The data is organized into headers, tax lines, receipt lines, and cost lines. Each section includes static fields that remain constant across transactions and dynamic fields that vary based on the invoice or transaction details.

Field Mappings
Header Fields


Tax Line Fields


Receipt Line Fields

Cost Line Fields

Full Example
```properties
###########################
# Header
###########################

## Header Static Fields
StaticFields=IBTP,BSCD,IMCD,APCD,CRTP,cono,TXAP,TXIN,PVLD,PYME,BKID
#SF_DIVI=A10
SF_IBTP=20
SF_cono=010
#SF_BSCD=DE
SF_IMCD=0
#SF_APCD=MHIDALGO
SF_CRTP=1
#SF_GEOC=999999999
# Tax applicable
SF_TXAP=1
# Tax included
#SF_TXIN=1
# Partial validation
SF_PYME=SCT
SF_BKID=BANK0

## Header Fields
HeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,PUNO,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC,TECD,DIVI
HF_SUNO=supplier_id
HF_IVDT=invoice_date
HF_SINO=invoice_id
HF_SPYN=supplier_id
HF_CUCD=currency
HF_CUAM=total_amount
#HF_VTAM=total_tax_amount
HF_ACDT=accounting_date
#HF_SERS=invoice_sub_type
HF_FTCO=supplier_country_code
HF_PUNO=purchase_order
#HF_TXAP=tax_country_1
HF_CORI=correlation_id
HF_PAIN=sqr_field_esr_reference
HF_TCHG=additional_amount
HF_CDC1=negative_amount
HF_APCD=authorised_user
HF_TEPY=payment_terms
#HF_PYME=payment_method
#HF_BKID=bank_id
HF_GEOC=geo_code
HF_TECD=discount_term
HF_DIVI=company_id

###########################
# Tax Line
###########################

# ## Tax Line Static Fields
InvoiceTaxStaticFields=RDTP,VTCD,cono,TAXT
IT_SF_RDTP=3
#IT_SF_DIVI=A10
IT_SF_cono=010
# Tax Type
#IT_SF_TAXT=2

# ## Tax Line Fields
# InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
InvoiceTaxFields=TTXA,TAXC,GEOC,VTA1,DIVI
# ITF_VTCD=TF_tax_code
ITF_VTA1=TF_tax_amount
# ITF_VTP1=TF_tax_rate
# ITF_CLAM=TF_gross_amount
ITF_DIVI=company_id

ITF_TTXA = TF_amount
ITF_TAXC = TF_tax_code
ITF_GEOC = TF_geo_code


###########################
# Order Header Extra Charges
###########################

OrderHeaderExtraCharges=order_xtra_header_charges

## Order Header Extra Charge Static Fields
OrderExtraChargeStaticFields=RDTP,,cono,CDSE,CEID
OEC_SF_RDTP=2
#OEC_SF_DIVI=A10
OEC_SF_cono=010
OEC_SF_CEID=INVPD
OEC_SF_CDSE=99

## Order Header Extra Charge Fields
OrderExtraChargeFields=NLAM,DIVI
OECF_NLAM=TF_amoun
OECF_DIVI=company_id


###########################
# Receipt Line
###########################

InvoiceReceipt=invoice_table

## Receipt Line Static Fields
InvoiceReceiptStaticFields=RDTP,SERS,RELP,VTCD,cono
IR_SF_RDTP=1
#IR_SF_DIVI=A10
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_cono=010

## Receipt Line Fields
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1,REPN,PNLS,DIVI,IVCW,PUCD
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
IRF_DIVI = company_id
IRF_IVCW = TF_catch_weight
IRF_PUCD = TF_unit_price_per

###########################
# Order Line Charges
###########################

OrderLineCharge=order_charges
## Order Charge Static Fields
OrderLineChargeStaticFields=RDTP,cono
OLC_SF_RDTP=5
#OLC_SF_DIVI=A10
OLC_SF_cono=010

## Order Charge Fields
OrderLineChargeFields=NLAM,CHGT,CEID,PUNO,PNLI,GRPR,ITNO,IVQA,SUDO,CDSE,REPN,PNLS,DIVI
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
OLCF_DIVI=company_id


###########################
# Order Charge Line
###########################

OrderCharge=order_charges

## Order Charge Static Fields
OrderChargeStaticFields=RDTP,cono
OC_SF_RDTP=2
#OC_SF_DIVI=A10
OC_SF_cono=010

## Order Charge Fields
OrderChargeFields=NLAM,CHGT,CEID,CDSE,DIVI
OCF_NLAM=TF_amount
## Amier said to change the costing_element to ledger_account when we have additional costs. Error Message: Costing element must be entered
# OCF_CEID=TF_costing_element
OCF_CEID=TF_ledger_account
OCF_CDSE=TF_charge_sequence
OCF_DIVI=company_id


###########################
# Cost Line
###########################

InvoiceCost=cost_lines

## Cost Line Static Fields
InvoiceCostStaticFields=RDTP,cono
IC_SF_RDTP=8
#IC_SF_DIVI=A10
IC_SF_cono=010

## Cost Line Fields
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2,DIVI
ICF_NLAM=TF_amount
ICF_VTXT=TF_voucher_text
ICF_AIT1=TF_ledger_account
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=supplier_id
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
ICF_DIVI=company_id

###########################
# Debit Note Header
###########################

## Header Static Fields
DNStaticFields=IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,cono
#DN_SF_DIVI=A10
DN_SF_IBTP=20
DN_SF_cono=010
#DN_SF_BSCD=DE
DN_SF_IMCD=0
#DN_SF_TEPY=N00
#DN_SF_PYME=CSH
#DN_SF_APCD=MHIDALGO
DN_SF_CRTP=1
#DN_SF_BKID=DJ1

## Header Fields
DNHeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC,DIVI
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
DN_HF_APCD=authorised_user
DN_HF_TEPY=payment_terms
DN_HF_PYME=payment_method
DN_HF_BKID=bank_id
DN_HF_GEOC=geo_code
DN_HF_DIVI=company_id


###########################
# Debit Note Cost Line
###########################

DebiteNoteInvoiceCost=debite_note_cost_lines

## Cost Line Static Fields
DebitNoteCostStaticFields=RDTP,cono,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTXT
DNC_SF_RDTP=8
#DNC_SF_DIVI=A10
DNC_SF_cono=010
DNC_SF_AIT1=20216
DNC_SF_AIT3=100
DNC_SF_AIT6=INVDN
DNC_SF_AIT7=PP20230
DNC_SF_VTXT=Additional Charges Difference

## Cost Line Fields
DebitNoteInvoiceCostFields=NLAM,AIT5,DIVI
DNCF_NLAM=TF_amount
DNCF_AIT5=purchase_order
DNCF_DIVI=company_id

###########################
# Debit Note Receipt Line
###########################

DebitNoteReceipt=invoice_table

## Debit Note Receipt Line Static Fields
DebitNoteReceiptStaticFields=RDTP,SERS,RELP,VTCD,cono
DNR_SF_RDTP=1
#DNR_SF_DIVI=A10
DNR_SF_RELP=1
#DNR_SF_VTCD=52
DNR_SF_cono=010

## Debit Note Receipt Line Fields
DebitNoteReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1,DIVI
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
DNRF_DIVI = company_id


###########################
# Credit Note Header
###########################

## Header Static Fields
CNStaticFields=IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,cono
#CN_SF_DIVI=A10
CN_SF_IBTP=20
CN_SF_cono=010
#CN_SF_BSCD=DE
CN_SF_IMCD=0
#CN_SF_TEPY=N00
#CN_SF_PYME=CSH
#CN_SF_APCD=MHIDALGO
CN_SF_CRTP=1
#CN_SF_BKID=DJ1

## Header Fields
CNHeaderFields=SUNO,IVDT,SINO,SPYN,CUCD,CUAM,VTAM,ACDT,SERS,FTCO,BSCD,TXAP,CORI,PAIN,TCHG,CDC1,APCD,TEPY,PYME,BKID,GEOC,DIVI
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
CN_HF_APCD=authorised_user
CN_HF_TEPY=payment_terms
CN_HF_PYME=payment_method
CN_HF_BKID=bank_id
CN_HF_GEOC=geo_code
CN_HF_DIVI=company_id

###########################
# Credit Note Cost Line
###########################

CreditNoteInvoiceCost=credit_note_cost_lines

## Cost Line Static Fields
CreditNoteCostStaticFields=RDTP,cono,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTXT
CNC_SF_RDTP=8
#CNC_SF_DIVI=A10
CNC_SF_cono=010
CNC_SF_AIT1=20216
CNC_SF_AIT3=100
CNC_SF_AIT6=INVDN
CNC_SF_AIT7=PP20230
CNC_SF_VTXT=Additional Charges Difference

## Cost Line Fields
CreditNoteInvoiceCostFields=NLAM,AIT5,DIVI
CNCF_NLAM=TF_amount
CNCF_AIT5=purchase_order
CNCF_DIVI=company_id

###########################
# Credit Note Receipt Line
###########################

CreditNoteReceipt=invoice_table

## Credit Note Receipt Line Static Fields
CreditNoteReceiptStaticFields=RDTP,SERS,RELP,VTCD,cono
CNR_SF_RDTP=1
#CNR_SF_DIVI=A10
CNR_SF_RELP=1
#CNR_SF_VTCD=52
CNR_SF_cono=010

## Credit Note Receipt Line Fields
CeeditNoteReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1,DIVI
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
CNRF_DIVI = company_id
```