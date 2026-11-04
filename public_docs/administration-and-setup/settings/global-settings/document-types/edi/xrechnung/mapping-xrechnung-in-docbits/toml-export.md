# Exportação TOML

**Como o XRechnung é mapeado no DocBits**

**1. Configuração do Cabeçalho (export_configuration.header)**

A seção do cabeçalho no XRechnung é mapeada para os campos no DocBits da seguinte forma:

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

    •    **SUNO**: ID do fornecedor, mapeado de [supplier_id] do XRechnung.

    •    **IVDT**: Data da Fatura, mapeada de [invoice_date].

    •    **SINO**: Número da Fatura, mapeado de [invoice_id].

    •    Outros campos como **valor total**, **moeda** e **termos de pagamento** são mapeados de forma semelhante dos campos do XRechnung para os campos do DocBits.

**2. Linhas de Imposto (export_configuration.tax_lines)**

As informações relacionadas a impostos são mapeadas usando a seguinte configuração:

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

    •    **GEOC**: Código Geográfico, mapeado para o [geo_code] correspondente do XRechnung.

    •    **TAXC**: Código de Imposto, mapeado para [tax_code].

**3. Encargos do Cabeçalho do Pedido (export_configuration.order_header_charges)**

Esta seção lida com quaisquer encargos adicionais que precisem ser adicionados no nível do cabeçalho do XRechnung.

[export_configuration.order_header_charges]
name = "order_header_charges"

  [export_configuration.order_header_charges.fields]
  RDTP = "2"
  DIVI = "RFP"
  CONO = "001"
  NLAM = "[[amount]]"
  CEID = "[[costing_element]]"
  CDSE = "[[charge_sequence]]"

    •    **NLAM**: Valor para o encargo do pedido.

    •    **CEID**: Elemento de Custo, que pode ser mapeado a partir de elementos específicos do XRechnung.

**4. Linhas de Recebimento (export_configuration.receipt_lines)**

As linhas de recebimento, que representam itens de linha no XRechnung, são tratadas da seguinte forma:

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

    •    **IVQA**: Quantidade, mapeada de [quantity] nos itens de linha do XRechnung.

    •    **ITNO**: Número do Item, mapeado para [item_number].

**5. Linhas de Custo (export_configuration.cost_lines)**

As linhas de custo, que lidam com custos adicionais no XRechnung, são mapeadas usando o seguinte:

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
