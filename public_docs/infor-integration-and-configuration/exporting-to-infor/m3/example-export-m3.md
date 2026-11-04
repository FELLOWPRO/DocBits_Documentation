# Ejemplo de exportación a M3



## Descripción general

La exportación a Infor M3 consiste en transferir los datos relacionados con facturas de Docbits a Infor M3 de forma estructurada. Los datos se organizan en cabeceras, líneas de impuestos, líneas de recepción y líneas de costes. Cada sección incluye campos estáticos, que permanecen constantes en todas las transacciones, y campos dinámicos, que varían según los detalles de la factura o de la transacción.



## Asignación de campos

### Campos de cabecera

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | -------------------------- | ---------------------------- |
| HF\_SUNO          | supplier\_id               | Identificador del proveedor |
| HF\_IVDT          | invoice\_date              | Fecha de la factura |
| HF\_SINO          | invoice\_id                | Identificador de la factura |
| HF\_SPYN          | supplier\_id               | Identificador del proveedor |
| HF\_CUCD          | currency                   | Moneda utilizada en la factura |
| HF\_CUAM          | total\_amount              | Importe total |
| HF\_VTAM          | total\_tax\_amount         | Importe total del impuesto |
| HF\_ACDT          | accounting\_date           | Fecha contable |
| HF\_SERS          | invoice\_sub\_type         | Subtipo de factura |
| HF\_FTCO          | supplier\_country\_code    | Código de país del proveedor |
| HF\_PUNO          | purchase\_order            | Orden de compra |
| HF\_TXAP          | tax\_country\_1            | País del impuesto |
| HF\_CORI          | correlation\_id            | Identificador de correlación |
| HF\_PAIN          | sqr\_field\_esr\_reference | Referencia del campo |
| HF\_TCHG          | additional\_amount         | Importe adicional |
| HF\_CDC1          | negative\_amount           | Importe negativo |
| HF\_APCD          | authorised\_user           | Usuario autorizado |
| HF\_TEPY          | payment\_terms             | Condiciones de pago |
| HF\_PYME          | payment\_method            | Forma de pago |
| HF\_BKID          | bank\_id                   | Identificador del banco |
| HF\_GEOC          | geo\_code                  | Código geográfico |
| HF\_TECD          | discount\_term             | Condición de descuento |
| HF\_TXAP          | tax\_applicable            | Impuesto aplicable |
| HF\_TXIN          | tax\_included              | Impuesto incluido |



## Campos de línea de impuestos

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | ------------------- |
| ITF\_VTCD         | TF\_tax\_code           | Código de impuesto |
| ITF\_VTA1         | TF\_tax\_amount         | Importe del impuesto |
| ITF\_VTP1         | TF\_tax\_rate           | Tipo impositivo |
| ITF\_CLAM         | TF\_gross\_amount       | Importe bruto |
| ITF\_DIVI         | company\_id             | Identificador de la empresa |
| ITF\_TTXA         | TF\_amount              | Importe |
| ITF\_TAXC         | TF\_tax\_code           | Código de impuesto |
| ITF\_GEOC         | TF\_geo\_code           | Código geográfico |

## Campos de cargos adicionales de la cabecera del pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ---------------------- | ----------------------- | ----------- |
| OrderExtraChargeFields | NLAM                    | NLAM |
| OECF\_NLAM             | TF\_amount              | Importe |

## Campos de línea de recepción

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | --------------------- |
| IRF\_IVQA         | TF\_quantity            | Cantidad facturada |
| IRF\_PUUN         | TF\_unit                | Número de unidad |
| IRF\_PUNO         | TF\_purchase\_order     | Número de orden de compra |
| IRF\_PNLI         | TF\_line\_number        | Número de línea del pedido |
| IRF\_ITNO         | TF\_item\_number        | Número de artículo |
| IRF\_POPN         | TF\_item\_number        | Número de artículo |
| IRF\_SUDO         | TF\_packing\_slip       | Albarán |
| IRF\_NEPR         | TF\_net\_unit\_price    | Precio unitario neto |
| IRF\_GRPR         | TF\_gross\_unit\_price  | Precio unitario bruto |
| IRF\_PPUN         | TF\_unit\_code\_price   | Código de unidad de precio |
| IRF\_NLAM         | TF\_net\_amount         | Importe neto |
| IRF\_GLAM         | TF\_gross\_amount       | Importe bruto |
| IRF\_TCHG         | TF\_charges             | Cargos |
| IRF\_CDC1         | TF\_discount            | Descuento |
| IRF\_PNLS         | TF\_sub\_line\_number   | Número de sublínea |
| IRF\_REPN         | TF\_receipt\_number     | Número de recepción |
| IRF\_DIVI         | company\_id             | Identificador de la empresa |
| IRF\_IVCW         | TF\_catch\_weight       | Peso variable |
| IRF\_PUCD         | TF\_unit\_price\_per    | Precio unitario por |

## Campos de cargos de línea de pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | --------------- |
| OLCF\_GRPR        | TF\_unit\_price         | Precio unitario |
| OLCF\_CHGT        | TF\_voucher\_text       | Texto del comprobante |
| OLCF\_CEID        | TF\_costing\_element    | Elemento de costes |
| OLCF\_PUNO        | TF\_purchase\_order     | Orden de compra |
| OLCF\_PNLI        | TF\_line\_number        | Número de línea |
| OLCF\_ITNO        | TF\_item\_number        | Número de artículo |
| OLCF\_CDSE        | TF\_charge\_sequence    | Secuencia de cargo |
| OLCF\_PNLS        | TF\_sub\_line\_number   | Número de sublínea |
| OLCF\_REPN        | TF\_receipt\_number     | Número de recepción |
| OLCF\_IVQA        | TF\_quantity            | Cantidad |
| OLCF\_SUDO        | TF\_packing\_slip       | Albarán |

## Campos de línea de cargo del pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | --------------- |
| OCF\_NLAM         | TF\_amount              | Importe |
| OCF\_CEID         | TF\_costing\_element    | Elemento de costes |
| OCF\_CDSE         | TF\_charge\_sequence    | Secuencia de cargo |

### Campos de línea de costes

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ------------------------- | ------------------------- |
| ICF\_NLAM         | TF\_amount                | Importe en la transacción |
| ICF\_VTXT         | TF\_voucher\_text         | Texto del comprobante |
| ICF\_AIT1         | TF\_ledger\_account       | Cuenta contable |
| ICF\_AIT2         | TF\_dimension\_2          | Dimensión 2 |
| ICF\_AIT3         | TF\_dimension\_3          | Dimensión 3 |
| ICF\_AIT4         | supplier\_id              | Identificador del proveedor |
| ICF\_AIT5         | TF\_dimension\_5          | Dimensión 5 |
| ICF\_AIT6         | TF\_dimension\_6          | Dimensión 6 |
| ICF\_AIT7         | TF\_dimension\_7          | Dimensión 7 |
| ICF\_AO01         | TF\_accounting\_object\_1 | Objeto contable 1 |
| ICF\_AO02         | TF\_accounting\_object\_2 | Objeto contable 2 |
| ICF\_AO03         | TF\_accounting\_object\_3 | Objeto contable 3 |
| ICF\_AO04         | TF\_accounting\_object\_4 | Objeto contable 4 |
| ICF\_AO05         | TF\_accounting\_object\_5 | Objeto contable 5 |
| ICF\_AO06         | TF\_accounting\_object\_6 | Objeto contable 6 |
| ICF\_AO07         | TF\_accounting\_object\_7 | Objeto contable 7 |

## Campos de cabecera de nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | -------------------------- | ----------------------- |
| DN\_HF\_SUNO      | supplier\_id               | Identificador del proveedor |
| DN\_HF\_IVDT      | invoice\_date              | Fecha de la factura |
| DN\_HF\_SINO      | invoice\_id                | Identificador de la factura |
| DN\_HF\_SPYN      | supplier\_id               | Identificador del proveedor |
| DN\_HF\_CUCD      | currency                   | Moneda |
| DN\_HF\_CUAM      | total\_net\_amount\_us     | Importe neto total (us) |
| DN\_HF\_VTAM      | total\_tax\_amount         | Importe total del impuesto |
| DN\_HF\_ACDT      | invoice\_date              | Fecha de la factura |
| DN\_HF\_SERS      | invoice\_sub\_type         | Subtipo de factura |
| DN\_HF\_FTCO      | supplier\_country\_code    | Código de país del proveedor |
| DN\_HF\_TXAP      | tax\_country\_1            | País del impuesto |
| DN\_HF\_CORI      | correlation\_id            | Identificador de correlación |
| DN\_HF\_PAIN      | sqr\_field\_esr\_reference | Referencia ESR del campo Sqr |
| DN\_HF\_TCHG      | additional\_amount         | Importe adicional |
| DN\_HF\_CDC1      | negative\_amount           | Importe negativo |
| DN\_HF\_APCD      | buyer\_id                  | Identificador del comprador |
| DN\_HF\_TEPY      | payment\_terms             | Condiciones de pago |
| DN\_HF\_PYME      | payment\_method            | Forma de pago |
| DN\_HF\_BKID      | bank\_id                   | Identificador del banco |
| DN\_HF\_GEOC      | geo\_code                  | Código geográfico |

## Campos de línea de costes de nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="252">Campo en Infor M3</th><th>Campo asignado en Docbits</th><th>Descripción</th></tr></thead><tbody><tr><td>DebitNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM,AIT5</td></tr><tr><td>DNCF_NLAM</td><td>TF_amount</td><td>Importe</td></tr><tr><td>DNCF_AIT5</td><td>purchase_order</td><td>Orden de compra</td></tr></tbody></table>

## Campos de línea de recepción de nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | ---------------- |
| DNRF\_IVQA        | TF\_quantity            | Cantidad |
| DNRF\_PUUN        | TF\_unit                | Unidad |
| DNRF\_PUNO        | TF\_purchase\_order     | Orden de compra |
| DNRF\_PNLI        | TF\_line\_number        | Número de línea |
| DNRF\_ITNO        | TF\_item\_number        | Número de artículo |
| DNRF\_POPN        | TF\_item\_number        | Número de artículo |
| DNRF\_SUDO        | TF\_packing\_slip       | Albarán |
| DNRF\_NEPR        | TF\_net\_unit\_price    | Precio unitario neto |
| DNRF\_GRPR        | TF\_gross\_unit\_price  | Precio unitario bruto |
| DNRF\_PPUN        | TF\_unit\_code\_price   | Código de unidad de precio |
| DNRF\_NLAM        | TF\_net\_amount         | Importe neto |
| DNRF\_GLAM        | TF\_gross\_amount       | Importe bruto |
| DNRF\_TCHG        | TF\_charges             | Cargos |
| DNRF\_CDC1        | TF\_discount            | Descuento |

## Cabecera de nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | -------------------------- | ----------------------- |
| CN\_HF\_SUNO      | supplier\_id               | Identificador del proveedor |
| CN\_HF\_IVDT      | invoice\_date              | Fecha de la factura |
| CN\_HF\_SINO      | invoice\_id                | Identificador de la factura |
| CN\_HF\_SPYN      | supplier\_id               | Identificador del proveedor |
| CN\_HF\_CUCD      | currency                   | Moneda |
| CN\_HF\_CUAM      | total\_net\_amount\_us     | Importe neto total (us) |
| CN\_HF\_VTAM      | total\_tax\_amount         | Importe total del impuesto |
| CN\_HF\_ACDT      | invoice\_date              | Fecha de la factura |
| CN\_HF\_SERS      | invoice\_sub\_type         | Subtipo de factura |
| CN\_HF\_FTCO      | supplier\_country\_code    | Código de país del proveedor |
| CN\_HF\_TXAP      | tax\_country\_1            | País del impuesto |
| CN\_HF\_CORI      | correlation\_id            | Identificador de correlación |
| CN\_HF\_PAIN      | sqr\_field\_esr\_reference | Referencia ESR del campo Sqr |
| CN\_HF\_TCHG      | additional\_amount         | Importe adicional |
| CN\_HF\_CDC1      | negative\_amount           | Importe negativo |
| CN\_HF\_APCD      | buyer\_id                  | Identificador del comprador |
| CN\_HF\_TEPY      | payment\_terms             | Condiciones de pago |
| CN\_HF\_PYME      | payment\_method            | Forma de pago |
| CN\_HF\_BKID      | bank\_id                   | Identificador del banco |
| CN\_HF\_GEOC      | geo\_code                  | Código geográfico |

## Campos de línea de costes de nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="257">Campo en Infor M3</th><th>Campo asignado en Docbits</th><th>Descripción</th></tr></thead><tbody><tr><td>CreditNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM, AIT5</td></tr><tr><td>CNCF_NLAM</td><td>TF_amount</td><td>Importe</td></tr><tr><td>CNCF_AIT5</td><td>purchase_order</td><td>Orden de compra</td></tr></tbody></table>

## Campos de línea de recepción de nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo en Infor M3 | Campo asignado en Docbits | Descripción |
| ----------------- | ----------------------- | ---------------- |
| CNRF\_IVQA        | TF\_quantity            | Cantidad |
| CNRF\_PUUN        | TF\_unit                | Unidad |
| CNRF\_PUNO        | TF\_purchase\_order     | Orden de compra |
| CNRF\_PNLI        | TF\_line\_number        | Número de línea |
| CNRF\_ITNO        | TF\_item\_number        | Número de artículo |
| CNRF\_POPN        | TF\_item\_number        | Número de artículo |
| CNRF\_SUDO        | TF\_packing\_slip       | Albarán |
| CNRF\_NEPR        | TF\_net\_unit\_price    | Precio unitario neto |
| CNRF\_GRPR        | TF\_gross\_unit\_price  | Precio unitario bruto |
| CNRF\_PPUN        | TF\_unit\_code\_price   | Código de unidad de precio |
| CNRF\_NLAM        | TF\_net\_amount         | Importe neto |
| CNRF\_GLAM        | TF\_gross\_amount       | Importe bruto |
| CNRF\_TCHG        | TF\_charges             | Cargos |
| CNRF\_CDC1        | TF\_discount            | Descuento |

## Campos estáticos

Además de las asignaciones dinámicas, se utilizan varios campos estáticos para cada tipo de línea, que están predefinidos de la siguiente manera:

* **Campos estáticos de cabecera**:
  * StaticFields=DIVI,IBTP,BSCD,IMCD,APCD,CRTP,CONO,PVLD
  * SF\_DIVI=RFP
  * SF\_IBTP=20
  * SF\_CONO=001
  * SF\_BSCD=DE
  * SF\_IMCD=0
  * SF\_APCD=MHIDALGO
  * SF\_CRTP=1
  * SF\_PVLD=1
* **Campos estáticos de línea de impuestos:**
  * InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO,TAXT
  * IT\_SF\_RDTP=3
  * IT\_SF\_DIVI=RFP
  * IT\_SF\_CONO=001
  * IT\_SF\_TAXT=2
* **Campos estáticos de cargos adicionales de la cabecera del pedido:**
  * OrderExtraChargeStaticFields=RDTP,DIVI,CONO,CDSE,CEID
  * OEC\_SF\_RDTP=2
  * OEC\_SF\_DIVI=RFP
  * OEC\_SF\_CONO=001
  * OEC\_SF\_CEID=INVPD
  * OEC\_SF\_CDSE=99
* **Campos estáticos de línea de recepción**:
  * InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * IR\_SF\_RDTP=1
  * IR\_SF\_DIVI=RFP
  * IR\_SF\_RELP=1
  * IR\_SF\_VTCD=52
  * IR\_SF\_CONO=001
* **Campos estáticos de cargos de línea de pedido:**
  * OrderLineChargeStaticFields=RDTP,DIVI,CONO
  * OLC\_SF\_RDTP=5
  * OLC\_SF\_DIVI=RFP
  * OLC\_SF\_CONO=001
* **Campos estáticos de línea de cargo del pedido:**
  * OrderChargeStaticFields=RDTP,DIVI,CONO
  * OC\_SF\_RDTP=2
  * OC\_SF\_DIVI=RFP
  * OC\_SF\_CONO=001
* **Campos estáticos de línea de costes**:
  * InvoiceCostStaticFields=RDTP,DIVI,CONO
  * IC\_SF\_RDTP=8
  * IC\_SF\_DIVI=RFP
  * IC\_SF\_CONO=001
* **Campos estáticos de cabecera de nota de débito:**
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
* **Campos estáticos de línea de costes de nota de débito:**
  * DebitNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * DNC\_SF\_RDTP=8
  * DNC\_SF\_DIVI=RFP
  * DNC\_SF\_CONO=001
  * DNC\_SF\_AIT1=20216
  * DNC\_SF\_AIT3=100
  * DNC\_SF\_AIT6=INVDN
  * DNC\_SF\_AIT7=PP20230
* **Campos estáticos de línea de recepción de nota de débito**
  * DebitNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * DNR\_SF\_RDTP=1
  * DNR\_SF\_DIVI=RFP
  * DNR\_SF\_RELP=1
  * DNR\_SF\_VTCD=52
  * DNR\_SF\_CONO=001
* **Campos estáticos de cabecera de nota de crédito:**
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
* **Campos estáticos de línea de costes de nota de crédito:**
  * CreditNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * CNC\_SF\_RDTP=8
  * CNC\_SF\_DIVI=RFP
  * CNC\_SF\_CONO=001
  * CNC\_SF\_AIT1=20216
  * CNC\_SF\_AIT3=100
  * CNC\_SF\_AIT6=INVDN
  * CNC\_SF\_AIT7=PP20230
* **Campos estáticos de línea de recepción de nota de crédito:**
  * CreditNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * CNR\_SF\_RDTP=1
  * CNR\_SF\_DIVI=RFP
  * CNR\_SF\_RELP=1
  * CNR\_SF\_VTCD=52
  * CNR\_SF\_CONO=001





## Ejemplo completo

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
