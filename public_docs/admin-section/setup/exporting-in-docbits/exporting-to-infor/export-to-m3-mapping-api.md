# Exportar a M3 Mapping (API)

### Secciones

El archivo de mapeo de exportación de M3 está dividido en 5 secciones y cada sección está dividida en 2 subsecciones

* Encabezado
* Campos Estáticos de Encabezado
* Campos de Encabezado
* Líneas de Impuestos
* Campos Estáticos de Línea de Impuestos
* Campos de Línea de Impuestos
* Líneas de Recibo
* Campos Estáticos de Línea de Recibo
* Campos de Línea de Recibo
* Líneas de Cargos de Orden (Montos Adicionales)
* Campos Estáticos de Cargos de Orden
* Campos de Cargos de Orden
* Líneas de Costo
* Campos Estáticos de Línea de Costo
* Campos de Línea de Costo

### Agregar y Eliminar Campos

Agregar Nuevo Campo:

* Primero necesitamos agregar el **nombre del campo de la API de M3** a la lista de campos de la sección relevante (por ejemplo, StaticFields, HeaderFields, InvoiceTaxFields)
* Definir el valor estático o el nombre del campo del documento para el campo de la API con el prefijo apropiado para la sección
* Ejemplo 1: Para definir un valor estático de **AAA** para el campo de la API de M3 **DIVI.** Primero agregamos DIVI a la propiedad **StaticFields**. Luego agregamos una línea **SF\_DIVI = AAA** ya que SF\_ es el prefijo para campos estáticos
* Ejemplo 2: Para mapear el campo de encabezado **IVDT (datos de factura)** al campo invoice\_date de DocBits. Primero agregamos IVDT a la propiedad **HeaderFields**. Luego agregamos una línea HF\_IVDT = invoice\_date ya que HF\_ es el prefijo para campos de encabezado

Eliminar Campo:

* Simplemente elimine el campo de la lista de campos de la sección y elimine la línea que define el valor para el campo.

#### **Campos de API de M3 Disponibles:**

* Los campos de M3 disponibles se pueden verificar abriendo la pantalla adecuada en M3.

<figure><img src="../../../../.gitbook/assets/aef99180-f060-497c-bd98-02d44fdd9274.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/266ad772-af8f-4aed-9cb7-c44aa8977cee.png" alt=""><figcaption></figcaption></figure>

* De manera similar, puede obtener los nombres de los campos para las líneas

### Encabezado:

<figure><img src="../../../../.gitbook/assets/4599dd21-9d05-4a0c-8b41-1e343c063871.png" alt=""><figcaption></figcaption></figure>

Propiedad de Lista de Campos: StaticFields

Prefijo de Campos de Sección: SF\_

Campos Disponibles: Puede mapear cualquier campo de la API de M3 con cualquier valor estático

#### **Campos de Encabezado**

Propiedad de Lista de Campos: HeaderFields

Prefijo de Campos de Sección: HF\_

Campos Disponibles: Puede mapear cualquier campo de DocBits a cualquier campo de la API de M3

### Línea de Impuestos:

#### Campos Estáticos de Línea de Impuestos:

Propiedad de Lista de Campos: InvoiceTaxStaticFields

Prefijo de Campos de Sección: IT\_SF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: Puede poner cualquier valor ya que son campos estáticos

#### Campos de Línea de Impuestos:

Propiedad de Lista de Campos: InvoiceTaxFields

Prefijo de Campos de M3: ITF\_

Prefijo de Campo de Tabla de DocBits: TF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: line\_number, tax\_amount, tax\_rate, net\_amount, gross\_amount, tax\_code\_full, tax\_code, tax\_country

### Línea de Recibo:

#### Campos Estáticos de Línea de Recibo:

Propiedad de Lista de Campos: InvoiceReceiptStaticFields

Prefijo de Campos de Sección: IR\_SF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: Puede poner cualquier valor ya que son campos estáticos

#### Campos de Línea de Recibo:

Propiedad de Lista de Campos: InvoiceReceiptFields

Prefijo de Campos de M3: IRF\_

Prefijo de Campo de Tabla de DocBits: TF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: packing\_slip, purchase\_order, line\_number, line\_sequence, delivery\_number, delivery\_line, amount, quantity, total\_net\_amount

### Línea de Cargos de Orden:

#### Campos Estáticos de Cargos de Orden:

Propiedad de Lista de Campos: OrderChargeStaticFields

Prefijo de Campos de Sección: OC\_SF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: Puede poner cualquier valor ya que son campos estáticos

#### Campos de Cargos de Orden:

Propiedad de Lista de Campos: OrderChargeFields

Prefijo de Campos de M3: OCF\_

Prefijo de Campo de Tabla de DocBits: TF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: ledger\_account, dimension\_2-7, amount, quantity, quantity2, position

### Línea de Costo:

#### Campos Estáticos de Línea de Costo:

Propiedad de Lista de Campos: InvoiceCostStaticFields

Prefijo de Campos de Sección: IC\_SF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: Puede poner cualquier valor ya que son campos estáticos

#### Campos de Línea de Costo:

Propiedad de Lista de Campos: InvoiceCostFields

Prefijo de Campos de M3: ICF\_

Prefijo de Campo de Tabla de DocBits: TF\_

Campos de M3 Disponibles: Por favor, verifique la API o la interfaz de usuario de M3

Campos de DocBits Disponibles: ledger\_account, dimension\_1-12, amount, quantity, quantity2, position

Nueva actualización
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
### Para clientes de EE. UU. actualizamos este mapeo a V3
````
```
# Cambios de la Versión 2 a la Versión 3: 
- StaticFields=DIVI,IBTP,BSCD,IMCD,TEPY,PYME,APCD,CRTP,GEOC,BKID
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
- ## Campos Estáticos de Línea de Impuestos
- InvoiceTaxStaticFields=RDTP,DIVI,VTCD
- IT_SF_RDTP=3
- IT_SF_DIVI=PJA
+ ## Campos Estáticos de Línea de Impuestos
+ InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO
+ IT_SF_RDTP=3
+ IT_SF_DIVI=AAA
+ IT_SF_CONO=780
- ## Campos de Línea de Impuestos
- InvoiceTaxFields=VTCD,VTA1,VTP1,CLAM
- ITF_VTCD=TF_tax_code
+ ## Campos de Línea de Impuestos
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
```markdown
# ITF_VTA1=TF_monto_impuesto
# ITF_VTP1=TF_tasa_impuesto
# ITF_CLAM=TF_monto_bruto

###########################
# Línea de Recibo
###########################

InvoiceReceipt=tabla_factura

## Campos Estáticos de la Línea de Recibo
InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
IR_SF_RDTP=1
IR_SF_DIVI=RFP
IR_SF_RELP=1
#IR_SF_VTCD=52
IR_SF_CONO=001

## Campos de la Línea de Recibo
InvoiceReceiptFields=IVQA,PUUN,PUNO,PNLI,ITNO,POPN,SUDO,NEPR,GRPR,PPUN,NLAM,GLAM,TCHG,CDC1
IRF_IVQA = TF_cantidad
IRF_PUUN = TF_unidad
IRF_PUNO = TF_orden_compra
IRF_PNLI = TF_numero_linea
IRF_ITNO = TF_numero_articulo
IRF_POPN = TF_numero_articulo
IRF_SUDO = TF_guia_embalaje
IRF_NEPR = TF_precio_neto_unidad
IRF_GRPR = TF_precio_bruto_unidad
IRF_PPUN = TF_precio_codigo_unidad
IRF_NLAM = TF_monto_neto
IRF_GLAM = TF_monto_total
IRF_TCHG = TF_cargos
IRF_CDC1 = TF_descuento

###########################
# Línea de Cargo de Orden
###########################

OrderCharge=cargos_orden

## Campos Estáticos de Cargo de Orden
OrderChargeStaticFields=RDTP,DIVI,CONO
OC_SF_RDTP=2
OC_SF_DIVI=RFP
OC_SF_CONO=001

## Campos de Cargo de Orden
OrderChargeFields=NLAM,CHGT,CEID
OCF_NLAM=TF_monto
OCF_CHGT=TF_texto_voucher
OCF_CEID=TF_cuenta_mayor


###########################
# Línea de Costo
###########################

InvoiceCost=líneas_costo

## Campos Estáticos de la Línea de Costo
InvoiceCostStaticFields=RDTP,DIVI,CONO
IC_SF_RDTP=8
IC_SF_DIVI=RFP
IC_SF_CONO=001

## Campos de la Línea de Costo
InvoiceCostFields=NLAM,VTXT,AO01,AO02,AO03,AO04,AO05,AO06,AO07,VTCD,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7,VTP1,VTP2
ICF_NLAM=TF_monto
ICF_VTXT=TF_texto_voucher
ICF_AIT1=TF_cuenta_mayor
ICF_AIT2=TF_dimension_2
ICF_AIT3=TF_dimension_3
ICF_AIT4=TF_dimension_4
ICF_AIT5=TF_dimension_5
ICF_AIT6=TF_dimension_6
ICF_AIT7=TF_dimension_7
ICF_AO01=TF_objeto_contable_1
ICF_AO02=TF_objeto_contable_2
ICF_AO03=TF_objeto_contable_3
ICF_AO04=TF_objeto_contable_4
ICF_AO05=TF_objeto_contable_5
ICF_AO06=TF_objeto_contable_6
ICF_AO07=TF_objeto_contable_7
```
```
````

