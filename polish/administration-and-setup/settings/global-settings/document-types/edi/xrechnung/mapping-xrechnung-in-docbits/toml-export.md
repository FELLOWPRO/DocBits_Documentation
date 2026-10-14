# Eksport TOML

**Jak XRechnung jest mapowany w DocBits**

**1. Konfiguracja nagłówka (export_configuration.header)**

Sekcja nagłówka w XRechnung jest mapowana na pola w DocBits w następujący sposób:

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

    •    **SUNO**: ID dostawcy, zmapowane z [supplier_id] z XRechnung.

    •    **IVDT**: Data faktury, zmapowana z [invoice_date].

    •    **SINO**: Numer faktury, zmapowany z [invoice_id].

    •    Inne pola, takie jak **całkowita kwota**, **waluta** i **warunki płatności**, są podobnie mapowane z pól XRechnung na pola DocBits.

**2. Linie podatkowe (export_configuration.tax_lines)**

Informacje podatkowe są mapowane przy użyciu następującej konfiguracji:

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

    •    **GEOC**: Kod geograficzny, zmapowany do odpowiedniego [geo_code] z XRechnung.

    •    **TAXC**: Kod podatkowy, zmapowany do [tax_code].

**3. Opłaty nagłówka zamówienia (export_configuration.order_header_charges)**

Ta sekcja obsługuje wszelkie dodatkowe opłaty, które należy dodać na poziomie nagłówka XRechnung.

[export_configuration.order_header_charges]
name = "order_header_charges"

  [export_configuration.order_header_charges.fields]
  RDTP = "2"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  CEID = "[[costing_element]]"
  CDSE = "[[charge_sequence]]"

    •    **NLAM**: Kwota opłaty za zamówienie.

    •    **CEID**: Element kosztowy, który można zmapować z określonych elementów XRechnung.

**4. Linie odbioru (export_configuration.receipt_lines)**

Linie odbioru, które reprezentują pozycje liniowe w XRechnung, są obsługiwane w następujący sposób:

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

    •    **IVQA**: Ilość, zmapowana z [quantity] w pozycjach liniowych XRechnung.

    •    **ITNO**: Numer przedmiotu, zmapowany do [item_number].

**5. Linie kosztowe (export_configuration.cost_lines)**

Linie kosztowe, które obsługują dodatkowe koszty w XRechnung, są mapowane przy użyciu następujących pól:

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
