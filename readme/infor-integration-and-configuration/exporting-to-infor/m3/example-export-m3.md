# Exemplo de Exportação para o M3



## Visão geral

A exportação para o Infor M3 transfere de forma estruturada os dados relacionados a faturas do Docbits para o Infor M3. Os dados são organizados em cabeçalhos, linhas de imposto, linhas de recebimento e linhas de custo. Cada seção inclui campos estáticos, que permanecem constantes em todas as transações, e campos dinâmicos, que variam conforme os detalhes da fatura ou da transação.



## Mapeamento de campos

### Campos do cabeçalho

| Campo no Infor M3 | Campo mapeado no Docbits   | Descrição                      |
| ----------------- | -------------------------- | ------------------------------ |
| HF\_SUNO          | supplier\_id               | Identificador do fornecedor    |
| HF\_IVDT          | invoice\_date              | Data da fatura                 |
| HF\_SINO          | invoice\_id                | Identificador da fatura        |
| HF\_SPYN          | supplier\_id               | Identificador do fornecedor    |
| HF\_CUCD          | currency                   | Moeda usada na fatura          |
| HF\_CUAM          | total\_amount              | Valor total                    |
| HF\_VTAM          | total\_tax\_amount         | Valor total do imposto         |
| HF\_ACDT          | accounting\_date           | Data de contabilização         |
| HF\_SERS          | invoice\_sub\_type         | Subtipo da fatura              |
| HF\_FTCO          | supplier\_country\_code    | Código do país do fornecedor   |
| HF\_PUNO          | purchase\_order            | Pedido de compra               |
| HF\_TXAP          | tax\_country\_1            | País do imposto                |
| HF\_CORI          | correlation\_id            | Identificador de correlação    |
| HF\_PAIN          | sqr\_field\_esr\_reference | Referência do campo            |
| HF\_TCHG          | additional\_amount         | Valor adicional                |
| HF\_CDC1          | negative\_amount           | Valor negativo                 |
| HF\_APCD          | authorised\_user           | Usuário autorizado             |
| HF\_TEPY          | payment\_terms             | Condições de pagamento         |
| HF\_PYME          | payment\_method            | Forma de pagamento             |
| HF\_BKID          | bank\_id                   | Identificador do banco         |
| HF\_GEOC          | geo\_code                  | Código geográfico              |
| HF\_TECD          | discount\_term             | Condição de desconto           |
| HF\_TXAP          | tax\_applicable            | Imposto aplicável              |
| HF\_TXIN          | tax\_included              | Imposto incluído               |



## Campos da linha de imposto

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição                  |
| ----------------- | ------------------------ | -------------------------- |
| ITF\_VTCD         | TF\_tax\_code            | Código do imposto          |
| ITF\_VTA1         | TF\_tax\_amount          | Valor do imposto           |
| ITF\_VTP1         | TF\_tax\_rate            | Alíquota do imposto        |
| ITF\_CLAM         | TF\_gross\_amount        | Valor bruto                |
| ITF\_DIVI         | company\_id              | Identificador da empresa   |
| ITF\_TTXA         | TF\_amount               | Valor                      |
| ITF\_TAXC         | TF\_tax\_code            | Código do imposto          |
| ITF\_GEOC         | TF\_geo\_code            | Código geográfico          |

## Campos de encargos adicionais do cabeçalho do pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3      | Campo mapeado no Docbits | Descrição |
| ---------------------- | ------------------------ | --------- |
| OrderExtraChargeFields | NLAM                     | NLAM      |
| OECF\_NLAM             | TF\_amount               | Valor     |

## Campos da linha de recebimento

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição                  |
| ----------------- | ------------------------ | -------------------------- |
| IRF\_IVQA         | TF\_quantity             | Quantidade faturada        |
| IRF\_PUUN         | TF\_unit                 | Número da unidade          |
| IRF\_PUNO         | TF\_purchase\_order      | Número do pedido de compra |
| IRF\_PNLI         | TF\_line\_number         | Número da linha do pedido  |
| IRF\_ITNO         | TF\_item\_number         | Número do item             |
| IRF\_POPN         | TF\_item\_number         | Número do item             |
| IRF\_SUDO         | TF\_packing\_slip        | Guia de remessa            |
| IRF\_NEPR         | TF\_net\_unit\_price     | Preço unitário líquido     |
| IRF\_GRPR         | TF\_gross\_unit\_price   | Preço unitário bruto       |
| IRF\_PPUN         | TF\_unit\_code\_price    | Código da unidade de preço |
| IRF\_NLAM         | TF\_net\_amount          | Valor líquido              |
| IRF\_GLAM         | TF\_gross\_amount        | Valor bruto                |
| IRF\_TCHG         | TF\_charges              | Encargos                   |
| IRF\_CDC1         | TF\_discount             | Desconto                   |
| IRF\_PNLS         | TF\_sub\_line\_number    | Número da sublinha         |
| IRF\_REPN         | TF\_receipt\_number      | Número do recebimento      |
| IRF\_DIVI         | company\_id              | Identificador da empresa   |
| IRF\_IVCW         | TF\_catch\_weight        | Peso variável (catch weight) |
| IRF\_PUCD         | TF\_unit\_price\_per     | Preço unitário por         |

## Campos de encargos da linha do pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição                  |
| ----------------- | ------------------------ | -------------------------- |
| OLCF\_GRPR        | TF\_unit\_price          | Preço unitário             |
| OLCF\_CHGT        | TF\_voucher\_text        | Texto do comprovante       |
| OLCF\_CEID        | TF\_costing\_element     | Elemento de custo          |
| OLCF\_PUNO        | TF\_purchase\_order      | Pedido de compra           |
| OLCF\_PNLI        | TF\_line\_number         | Número da linha            |
| OLCF\_ITNO        | TF\_item\_number         | Número do item             |
| OLCF\_CDSE        | TF\_charge\_sequence     | Sequência do encargo       |
| OLCF\_PNLS        | TF\_sub\_line\_number    | Número da sublinha         |
| OLCF\_REPN        | TF\_receipt\_number      | Número do recebimento      |
| OLCF\_IVQA        | TF\_quantity             | Quantidade                 |
| OLCF\_SUDO        | TF\_packing\_slip        | Guia de remessa            |

## Campos da linha de encargos do pedido <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição            |
| ----------------- | ------------------------ | -------------------- |
| OCF\_NLAM         | TF\_amount               | Valor                |
| OCF\_CEID         | TF\_costing\_element     | Elemento de custo    |
| OCF\_CDSE         | TF\_charge\_sequence     | Sequência do encargo |

### Campos da linha de custo

| Campo no Infor M3 | Campo mapeado no Docbits  | Descrição                   |
| ----------------- | ------------------------- | --------------------------- |
| ICF\_NLAM         | TF\_amount                | Valor da transação          |
| ICF\_VTXT         | TF\_voucher\_text         | Texto do comprovante        |
| ICF\_AIT1         | TF\_ledger\_account       | Conta contábil              |
| ICF\_AIT2         | TF\_dimension\_2          | Dimensão 2                  |
| ICF\_AIT3         | TF\_dimension\_3          | Dimensão 3                  |
| ICF\_AIT4         | supplier\_id              | Identificador do fornecedor |
| ICF\_AIT5         | TF\_dimension\_5          | Dimensão 5                  |
| ICF\_AIT6         | TF\_dimension\_6          | Dimensão 6                  |
| ICF\_AIT7         | TF\_dimension\_7          | Dimensão 7                  |
| ICF\_AO01         | TF\_accounting\_object\_1 | Objeto contábil 1           |
| ICF\_AO02         | TF\_accounting\_object\_2 | Objeto contábil 2           |
| ICF\_AO03         | TF\_accounting\_object\_3 | Objeto contábil 3           |
| ICF\_AO04         | TF\_accounting\_object\_4 | Objeto contábil 4           |
| ICF\_AO05         | TF\_accounting\_object\_5 | Objeto contábil 5           |
| ICF\_AO06         | TF\_accounting\_object\_6 | Objeto contábil 6           |
| ICF\_AO07         | TF\_accounting\_object\_7 | Objeto contábil 7           |

## Campos do cabeçalho da nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits   | Descrição                       |
| ----------------- | -------------------------- | ------------------------------- |
| DN\_HF\_SUNO      | supplier\_id               | Identificador do fornecedor     |
| DN\_HF\_IVDT      | invoice\_date              | Data da fatura                  |
| DN\_HF\_SINO      | invoice\_id                | Identificador da fatura         |
| DN\_HF\_SPYN      | supplier\_id               | Identificador do fornecedor     |
| DN\_HF\_CUCD      | currency                   | Moeda                           |
| DN\_HF\_CUAM      | total\_net\_amount\_us     | Valor líquido total (US)        |
| DN\_HF\_VTAM      | total\_tax\_amount         | Valor total do imposto          |
| DN\_HF\_ACDT      | invoice\_date              | Data da fatura                  |
| DN\_HF\_SERS      | invoice\_sub\_type         | Subtipo da fatura               |
| DN\_HF\_FTCO      | supplier\_country\_code    | Código do país do fornecedor    |
| DN\_HF\_TXAP      | tax\_country\_1            | País do imposto                 |
| DN\_HF\_CORI      | correlation\_id            | Identificador de correlação     |
| DN\_HF\_PAIN      | sqr\_field\_esr\_reference | Referência do campo SQR/ESR     |
| DN\_HF\_TCHG      | additional\_amount         | Valor adicional                 |
| DN\_HF\_CDC1      | negative\_amount           | Valor negativo                  |
| DN\_HF\_APCD      | buyer\_id                  | Identificador do comprador      |
| DN\_HF\_TEPY      | payment\_terms             | Condições de pagamento          |
| DN\_HF\_PYME      | payment\_method            | Forma de pagamento              |
| DN\_HF\_BKID      | bank\_id                   | Identificador do banco          |
| DN\_HF\_GEOC      | geo\_code                  | Código geográfico               |

## Campos da linha de custo da nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="252">Campo no Infor M3</th><th>Campo mapeado no Docbits</th><th>Descrição</th></tr></thead><tbody><tr><td>DebitNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM,AIT5</td></tr><tr><td>DNCF_NLAM</td><td>TF_amount</td><td>Valor</td></tr><tr><td>DNCF_AIT5</td><td>purchase_order</td><td>Pedido de compra</td></tr></tbody></table>

## Campos da linha de recebimento da nota de débito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição                  |
| ----------------- | ------------------------ | -------------------------- |
| DNRF\_IVQA        | TF\_quantity             | Quantidade                 |
| DNRF\_PUUN        | TF\_unit                 | Unidade                    |
| DNRF\_PUNO        | TF\_purchase\_order      | Pedido de compra           |
| DNRF\_PNLI        | TF\_line\_number         | Número da linha            |
| DNRF\_ITNO        | TF\_item\_number         | Número do item             |
| DNRF\_POPN        | TF\_item\_number         | Número do item             |
| DNRF\_SUDO        | TF\_packing\_slip        | Guia de remessa            |
| DNRF\_NEPR        | TF\_net\_unit\_price     | Preço unitário líquido     |
| DNRF\_GRPR        | TF\_gross\_unit\_price   | Preço unitário bruto       |
| DNRF\_PPUN        | TF\_unit\_code\_price    | Código da unidade de preço |
| DNRF\_NLAM        | TF\_net\_amount          | Valor líquido              |
| DNRF\_GLAM        | TF\_gross\_amount        | Valor bruto                |
| DNRF\_TCHG        | TF\_charges              | Encargos                   |
| DNRF\_CDC1        | TF\_discount             | Desconto                   |

## Cabeçalho da nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits   | Descrição                       |
| ----------------- | -------------------------- | ------------------------------- |
| CN\_HF\_SUNO      | supplier\_id               | Identificador do fornecedor     |
| CN\_HF\_IVDT      | invoice\_date              | Data da fatura                  |
| CN\_HF\_SINO      | invoice\_id                | Identificador da fatura         |
| CN\_HF\_SPYN      | supplier\_id               | Identificador do fornecedor     |
| CN\_HF\_CUCD      | currency                   | Moeda                           |
| CN\_HF\_CUAM      | total\_net\_amount\_us     | Valor líquido total (US)        |
| CN\_HF\_VTAM      | total\_tax\_amount         | Valor total do imposto          |
| CN\_HF\_ACDT      | invoice\_date              | Data da fatura                  |
| CN\_HF\_SERS      | invoice\_sub\_type         | Subtipo da fatura               |
| CN\_HF\_FTCO      | supplier\_country\_code    | Código do país do fornecedor    |
| CN\_HF\_TXAP      | tax\_country\_1            | País do imposto                 |
| CN\_HF\_CORI      | correlation\_id            | Identificador de correlação     |
| CN\_HF\_PAIN      | sqr\_field\_esr\_reference | Referência do campo SQR/ESR     |
| CN\_HF\_TCHG      | additional\_amount         | Valor adicional                 |
| CN\_HF\_CDC1      | negative\_amount           | Valor negativo                  |
| CN\_HF\_APCD      | buyer\_id                  | Identificador do comprador      |
| CN\_HF\_TEPY      | payment\_terms             | Condições de pagamento          |
| CN\_HF\_PYME      | payment\_method            | Forma de pagamento              |
| CN\_HF\_BKID      | bank\_id                   | Identificador do banco          |
| CN\_HF\_GEOC      | geo\_code                  | Código geográfico               |

## Campos da linha de custo da nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

<table><thead><tr><th width="257">Campo no Infor M3</th><th>Campo mapeado no Docbits</th><th>Descrição</th></tr></thead><tbody><tr><td>CreditNoteInvoiceCostFields</td><td>NLAM,AIT5</td><td>NLAM, AIT5</td></tr><tr><td>CNCF_NLAM</td><td>TF_amount</td><td>Valor</td></tr><tr><td>CNCF_AIT5</td><td>purchase_order</td><td>Pedido de compra</td></tr></tbody></table>

## Campos da linha de recebimento da nota de crédito <a href="#tax-line-fields" id="tax-line-fields"></a>

| Campo no Infor M3 | Campo mapeado no Docbits | Descrição                  |
| ----------------- | ------------------------ | -------------------------- |
| CNRF\_IVQA        | TF\_quantity             | Quantidade                 |
| CNRF\_PUUN        | TF\_unit                 | Unidade                    |
| CNRF\_PUNO        | TF\_purchase\_order      | Pedido de compra           |
| CNRF\_PNLI        | TF\_line\_number         | Número da linha            |
| CNRF\_ITNO        | TF\_item\_number         | Número do item             |
| CNRF\_POPN        | TF\_item\_number         | Número do item             |
| CNRF\_SUDO        | TF\_packing\_slip        | Guia de remessa            |
| CNRF\_NEPR        | TF\_net\_unit\_price     | Preço unitário líquido     |
| CNRF\_GRPR        | TF\_gross\_unit\_price   | Preço unitário bruto       |
| CNRF\_PPUN        | TF\_unit\_code\_price    | Código da unidade de preço |
| CNRF\_NLAM        | TF\_net\_amount          | Valor líquido              |
| CNRF\_GLAM        | TF\_gross\_amount        | Valor bruto                |
| CNRF\_TCHG        | TF\_charges              | Encargos                   |
| CNRF\_CDC1        | TF\_discount             | Desconto                   |

## Campos estáticos

Além dos mapeamentos dinâmicos, há vários campos estáticos usados em cada tipo de linha, predefinidos da seguinte forma:

* **Campos estáticos do cabeçalho**:
  * StaticFields=DIVI,IBTP,BSCD,IMCD,APCD,CRTP,CONO,PVLD
  * SF\_DIVI=RFP
  * SF\_IBTP=20
  * SF\_CONO=001
  * SF\_BSCD=DE
  * SF\_IMCD=0
  * SF\_APCD=MHIDALGO
  * SF\_CRTP=1
  * SF\_PVLD=1
* **Campos estáticos da linha de imposto:**
  * InvoiceTaxStaticFields=RDTP,DIVI,VTCD,CONO,TAXT
  * IT\_SF\_RDTP=3
  * IT\_SF\_DIVI=RFP
  * IT\_SF\_CONO=001
  * IT\_SF\_TAXT=2
* **Campos estáticos dos encargos adicionais do cabeçalho do pedido:**
  * OrderExtraChargeStaticFields=RDTP,DIVI,CONO,CDSE,CEID
  * OEC\_SF\_RDTP=2
  * OEC\_SF\_DIVI=RFP
  * OEC\_SF\_CONO=001
  * OEC\_SF\_CEID=INVPD
  * OEC\_SF\_CDSE=99
* **Campos estáticos da linha de recebimento**:
  * InvoiceReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * IR\_SF\_RDTP=1
  * IR\_SF\_DIVI=RFP
  * IR\_SF\_RELP=1
  * IR\_SF\_VTCD=52
  * IR\_SF\_CONO=001
* **Campos estáticos de encargos da linha do pedido:**
  * OrderLineChargeStaticFields=RDTP,DIVI,CONO
  * OLC\_SF\_RDTP=5
  * OLC\_SF\_DIVI=RFP
  * OLC\_SF\_CONO=001
* **Campos estáticos da linha de encargos do pedido:**
  * OrderChargeStaticFields=RDTP,DIVI,CONO
  * OC\_SF\_RDTP=2
  * OC\_SF\_DIVI=RFP
  * OC\_SF\_CONO=001
* **Campos estáticos da linha de custo**:
  * InvoiceCostStaticFields=RDTP,DIVI,CONO
  * IC\_SF\_RDTP=8
  * IC\_SF\_DIVI=RFP
  * IC\_SF\_CONO=001
* **Campos estáticos do cabeçalho da nota de débito:**
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
* **Campos estáticos da linha de custo da nota de débito:**
  * DebitNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * DNC\_SF\_RDTP=8
  * DNC\_SF\_DIVI=RFP
  * DNC\_SF\_CONO=001
  * DNC\_SF\_AIT1=20216
  * DNC\_SF\_AIT3=100
  * DNC\_SF\_AIT6=INVDN
  * DNC\_SF\_AIT7=PP20230
* **Campos estáticos da linha de recebimento da nota de débito**
  * DebitNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * DNR\_SF\_RDTP=1
  * DNR\_SF\_DIVI=RFP
  * DNR\_SF\_RELP=1
  * DNR\_SF\_VTCD=52
  * DNR\_SF\_CONO=001
* **Campos estáticos do cabeçalho da nota de crédito:**
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
* **Campos estáticos da linha de custo da nota de crédito:**
  * CreditNoteCostStaticFields=RDTP,DIVI,CONO,AIT1,AIT2,AIT3,AIT4,AIT5,AIT6,AIT7
  * CNC\_SF\_RDTP=8
  * CNC\_SF\_DIVI=RFP
  * CNC\_SF\_CONO=001
  * CNC\_SF\_AIT1=20216
  * CNC\_SF\_AIT3=100
  * CNC\_SF\_AIT6=INVDN
  * CNC\_SF\_AIT7=PP20230
* **Campos estáticos da linha de recebimento da nota de crédito:**
  * CreditNoteReceiptStaticFields=RDTP,DIVI,SERS,RELP,VTCD,CONO
  * CNR\_SF\_RDTP=1
  * CNR\_SF\_DIVI=RFP
  * CNR\_SF\_RELP=1
  * CNR\_SF\_VTCD=52
  * CNR\_SF\_CONO=001





## Exemplo completo

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
