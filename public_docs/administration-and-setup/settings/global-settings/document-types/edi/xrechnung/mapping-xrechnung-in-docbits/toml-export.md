# TOML-Export

**Wie XRechnung in DocBits zugeordnet wird**

**1. Kopfdatenkonfiguration (export_configuration.header)**

Der Kopfbereich in der XRechnung wird wie folgt Feldern in DocBits zugeordnet:

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

    •    **SUNO**: Lieferanten-ID, zugeordnet zu [supplier_id] aus XRechnung.

    •    **IVDT**: Rechnungsdatum, zugeordnet zu [invoice_date].

    •    **SINO**: Rechnungsnummer, zugeordnet zu [invoice_id].

    •    Andere Felder wie **Gesamtbetrag**, **Währung** und **Zahlungsbedingungen** werden ähnlich von der XRechnung zu DocBits-Feldern zugeordnet.

**2. Steuerzeilen (export_configuration.tax_lines)**

Steuerbezogene Informationen werden mit der folgenden Konfiguration zugeordnet:

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

    •    **GEOC**: Geocode, zugeordnet zum entsprechenden [geo_code] aus XRechnung.

    •    **TAXC**: Steuercode, zugeordnet zu [tax_code].

**3. Auftragskopfgebühren (export_configuration.order_header_charges)**

Dieser Abschnitt behandelt alle zusätzlichen Gebühren, die auf Kopfebene der XRechnung hinzugefügt werden müssen.

[export_configuration.order_header_charges]
name = "order_header_charges"

 [export_configuration.order_header_charges.fields]
 RDTP = "2"
 DIVI = "RFP"
 CONO = "001"
 NLAM = "[[amount]]"
 CEID = "[[costing_element]]"
 CDSE = "[[charge_sequence]]"

    •    **NLAM**: Betrag für die Auftragsgebühr.

    •    **CEID**: Kostenelement, das aus spezifischen XRechnung-Elementen zugeordnet werden kann.

**4. Empfangszeilen (export_configuration.receipt_lines)**

Empfangszeilen, die Einzelposten in der XRechnung darstellen, werden wie folgt behandelt:

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

    •    **IVQA**: Menge, zugeordnet von der [quantity] in den XRechnung-Einzelposten.

    •    **ITNO**: Artikelnummer, zugeordnet zu [item_number].

**5. Kostenzeilen (export_configuration.cost_lines)**

Kostenzeilen, die zusätzliche Kosten in der XRechnung behandeln, werden wie folgt zugeordnet:

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
