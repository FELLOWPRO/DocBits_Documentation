# Exportation TOML

**Comment la XRechnung est mappée dans DocBits**

**1. Configuration de l'en-tête (export_configuration.header)**

La section d'en-tête de la XRechnung est mappée aux champs de DocBits comme suit :

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

    •    **SUNO** : ID fournisseur, mappé à [supplier_id] de la XRechnung.

    •    **IVDT** : Date de facture, mappée à [invoice_date].

    •    **SINO** : Numéro de facture, mappé à [invoice_id].

    •    D'autres champs tels que le **montant total**, la **devise** et les **conditions de paiement** sont mappés de manière similaire des champs XRechnung aux champs DocBits.

**2. Lignes de taxe (export_configuration.tax_lines)**

Les informations relatives aux taxes sont mappées à l'aide de la configuration suivante :

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

    •    **GEOC** : Code géo, mappé au [geo_code] correspondant de la XRechnung.

    •    **TAXC** : Code taxe, mappé à [tax_code].

**3. Frais d'en-tête de commande (export_configuration.order_header_charges)**

Cette section gère tous les frais supplémentaires qui doivent être ajoutés au niveau de l'en-tête de la XRechnung.

[export_configuration.order_header_charges]
name = "order_header_charges"

 [export_configuration.order_header_charges.fields]
  RDTP = "2"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  CEID = "[[costing_element]]"
  CDSE = "[[charge_sequence]]"

    •    **NLAM** : Montant pour les frais de commande.

    •    **CEID** : Élément de coût, qui peut être mappé à partir d'éléments XRechnung spécifiques.

**4. Lignes de réception (export_configuration.receipt_lines)**

Les lignes de réception, qui représentent les postes dans la XRechnung, sont gérées comme suit :

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

    •    **IVQA** : Quantité, mappée à partir de [quantity] dans les postes de la XRechnung.

    •    **ITNO** : Numéro d'article, mappé à [item_number].

**5. Lignes de coût (export_configuration.cost_lines)**

Les lignes de coût, qui gèrent les coûts supplémentaires dans la XRechnung, sont mappées à l'aide des éléments suivants :

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
