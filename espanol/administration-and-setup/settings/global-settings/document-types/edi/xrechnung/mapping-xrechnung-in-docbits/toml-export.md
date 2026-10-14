# Exportación TOML

**Cómo se mapea XRechnung en DocBits**

**1. Configuración de encabezado (export_configuration.header)**

La sección de encabezado en XRechnung se mapea a los campos en DocBits de la siguiente manera:

[export_configuration.header]
name = "header"

 [export_configuration.header.fields]
  DIVI = "RFP"
  IBTP = "20"
  IMCD = "0"
  CRTP = "1"
  CONO = "001"
  SUNO = "[supplier_id]"
  IVDT = "[invoice_date]"
  SINO = "[invoice_id]"
  SPYN = "[supplier_id]"
  CUCD = "[currency]"
  CUAM = "[total_amount]"
  FTCO = "[supplier_country_code]"
  PUNO = "[purchase_order]"
  CORI = "[correlation_id]"
  PAIN = "[sqr_field_esr_reference]"
  TCHG = "[additional_amount]"
  CDC1 = "[negative_amount]"
  APCD = "[buyer_id]"
  TEPY = "[payment_terms]"
  PYME = "[payment_method]"
  BKID = "[bank_id]"
  GEOC = "1"
  TECD = "[discount_term]"
  TXAP = "[tax_applicable]"
  TXIN = "[tax_included]"

    •    **SUNO**: ID del proveedor, mapeado a [supplier_id] de XRechnung.

    •    **IVDT**: Fecha de factura, mapeada a [invoice_date].

    •    **SINO**: Número de factura, mapeado a [invoice_id].

    •    Otros campos como **importe total**, **moneda** y **condiciones de pago** se mapean de manera similar desde XRechnung a los campos de DocBits.

**2. Líneas de impuestos (export_configuration.tax_lines)**

La información relacionada con los impuestos se mapea utilizando la siguiente configuración:

[export_configuration.tax_lines]
name = "tax_lines"

  [export_configuration.tax_lines.fields]
  RDTP = "3"
  DIVI = "RFP"
  CONO = "001"
  TAXT = "2"
  GEOC = "[[geo_code]]"
  TTXA = "[[amount]]"
  TAXC = "[[tax_code]]"

    •    **GEOC**: Código geográfico, mapeado al [geo_code] correspondiente de XRechnung.

    •    **TAXC**: Código de impuesto, mapeado a [tax_code].

**3. Cargos de encabezado de pedido (export_configuration.order_header_charges)**

Esta sección maneja cualquier cargo adicional que deba agregarse al nivel de encabezado de XRechnung.

[export_configuration.order_header_charges]
name = "order_header_charges"

  [export_configuration.order_header_charges.fields]
  RDTP = "2"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  CEID = "[[costing_element]]"
  CDSE = "[[charge_sequence]]"

    •    **NLAM**: Importe para el cargo del pedido.

    •    **CEID**: Elemento de costo, que se puede mapear desde elementos específicos de XRechnung.

**4. Líneas de recibo (export_configuration.receipt_lines)**

Las líneas de recibo, que representan partidas en XRechnung, se manejan de la siguiente manera:

[export_configuration.receipt_lines]
name = "receipt_lines"

  [export_configuration.receipt_lines.fields]
  RDTP = "1"
  DIVI = "RFP"
  RELP = "1"
  CONO = "001"
  IVQA = "[[quantity]]"
  PUUN = "[[unit]]"
  PUNO = "[[purchase_order]]"
  PNLI = "[[line_number]]"
  ITNO = "[[item_number]]"
  POPN = "[[item_number]]"
  SUDO = "[[packing_slip]]"
  GRPR = "[[gross_unit_price]]"
  PPUN = "[[unit_code_price]]"
  TCHG = "[[charges]]"
  CDC1 = "[[discount]]"
  REPN = "[[receipt_number]]"
  PNLS = "[[sub_line_number]]"

    •    **IVQA**: Cantidad, mapeada desde [quantity] en las partidas de XRechnung.

    •    **ITNO**: Número de artículo, mapeado a [item_number].

**5. Líneas de costo (export_configuration.cost_lines)**

Las líneas de costo, que manejan costos adicionales en XRechnung, se mapean utilizando lo siguiente:

[export_configuration.cost_lines]
name = "cost_lines"

  [export_configuration.cost_lines.fields]
  RDTP = "8"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  VTXT = "[[voucher_text]]"
  AO01 = "[[accounting_object_1]]"
  AO02 = "[[accounting_object_2]]"
  AO03 = "[[accounting_object_3]]"
  AO04 = "[[accounting_object_4]]"
  AO05 = "[[accounting_object_5]]"
  AO06 = "[[accounting_object_6]]"
  AO07 = "[[accounting_object_7]]"
  AIT1 = "[[ledger_account]]"
  AIT2 = "[[dimension_2]]"
  AIT3 = "[[dimension_3]]"
  AIT4 = "[[dimension_4]]"
  AIT5 = "[[dimension_5]]"
  AIT6 = "[[dimension_6]]"
  AIT7 = "[[dimension_7]]"
