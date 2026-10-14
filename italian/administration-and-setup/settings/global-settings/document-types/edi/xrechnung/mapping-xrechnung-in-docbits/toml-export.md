# Esportazione TOML

**Come XRechnung viene mappata in DocBits**

**1. Configurazione dell'intestazione (export_configuration.header)**

La sezione dell'intestazione nella XRechnung viene mappata sui campi in DocBits come segue:

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

    •    **SUNO**: ID del fornitore, mappato su [supplier_id] dalla XRechnung.

    •    **IVDT**: Data fattura, mappata su [invoice_date].

    •    **SINO**: Numero fattura, mappato su [invoice_id].

    •    Altri campi come **importo totale**, **valuta** e **termini di pagamento** sono mappati in modo simile dai campi XRechnung ai campi DocBits.

**2. Righe fiscali (export_configuration.tax_lines)**

Le informazioni relative alle tasse vengono mappate utilizzando la seguente configurazione:

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

    •    **GEOC**: Codice geografico, mappato sul corrispondente [geo_code] dalla XRechnung.

    •    **TAXC**: Codice fiscale, mappato su [tax_code].

**3. Oneri di intestazione ordine (export_configuration.order_header_charges)**

Questa sezione gestisce eventuali costi aggiuntivi che devono essere aggiunti a livello di intestazione della XRechnung.

[export_configuration.order_header_charges]
name = "order_header_charges"

  [export_configuration.order_header_charges.fields]
  RDTP = "2"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  CEID = "[[costing_element]]"
  CDSE = "[[charge_sequence]]"

    •    **NLAM**: Importo per l'addebito dell'ordine.

    •    **CEID**: Elemento di costo, che può essere mappato da elementi XRechnung specifici.

**4. Righe di ricezione (export_configuration.receipt_lines)**

Le righe di ricezione, che rappresentano le voci nella XRechnung, vengono gestite come segue:

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

    •    **IVQA**: Quantità, mappata dalla [quantity] nelle voci XRechnung.

    •    **ITNO**: Numero articolo, mappato su [item_number].

**5. Righe di costo (export_configuration.cost_lines)**

Le righe di costo, che gestiscono i costi aggiuntivi nella XRechnung, vengono mappate utilizzando quanto segue:

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
