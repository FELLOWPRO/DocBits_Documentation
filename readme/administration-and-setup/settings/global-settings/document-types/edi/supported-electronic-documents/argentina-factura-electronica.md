---
description: Suporte a documentos eletrônicos ARGENTINA FACTURA ELECTRONICA no DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Argentina](countries/argentina.md). A entrada de classificação de notas de crédito não tem um conjunto de extração dedicado no estado examinado. Verifique o mapeamento efetivo e teste uma amostra real de nota de crédito.
{% endhint %}

| Propriedade          | Valor                                                                   |
| -------------------- | ----------------------------------------------------------------------- |
| **País / Região**    | Argentina                                                               |
| **Tipos de documento** | Invoice                                                               |
| **Formato**          | XML                                                                     |
| **Padrão**           | Argentina Factura Electrónica (tipos de comprobante da AFIP além da Factura A) |
| **Localidade**       | `es_AR`                                                                 |

O ARGENTINA FACTURA ELECTRONICA abrange o conjunto mais amplo de documentos eletrônicos da AFIP argentina além da Factura A (tipo 001). Isso inclui outros tipos de comprobante, como Factura B (tipo 006), Factura C (tipo 011), Nota de Crédito (tipo 003) e outras variantes. O DocBits detecta automaticamente o tipo de documento a partir de `<tipoComprobante>` e aplica a extração adequada.

## Status de suporte

| Componente          | Status      |
| ------------------- | ----------- |
| Preview             | ✅ Suportado |
| Extração de campos  | ✅ Suportado |
| Transformação       | ✅ Suportado |

## Preview padrão

<figure><img src="../../../../../../.gitbook/assets/argentina-factura-electronica-preview.png" alt="Preview de Argentina Factura Electronica no DocBits"><figcaption><p>Preview padrão do DocBits para um documento ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo do DocBits | Elementos XML de origem                                                   | Observações                                  |
| ---------------- | ------------------------------------------------------------------------- | -------------------------------------------- |
| `invoice_id`     | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber`           | Vários XPaths alternativos para esquemas variantes |
| `invoice_date`   | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate`                |                                              |
| `due_date`       | `//fechaVencimiento`, `//fechaVtoPago`                                    |                                              |
| `currency`       | `//Moneda`, `//mon_id`, `//MonId`, alternativa: `ARS`                     |                                              |
| `total_amount`   | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount`              |                                              |
| `net_amount`     | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount`                   |                                              |
| `tax_amount`     | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount`                      |                                              |
| `supplier_name`  | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName`    |                                              |
| `supplier_id`    | `//CUITProveedor`, `//cuit`, `//Cuit`, `//SellerID`                       | CUIT = identificação fiscal argentina        |
| `buyer_name`     | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` |                                              |
| `buyer_id`       | `//CUITComprador`, `//doc_nro`, `//DocNro`, `//BuyerID`                   |                                              |
| `iban`           | `//PAYMENT/IBAN`                                                          | Geralmente vazio                             |
| `bic`            | `//PAYMENT/BIC`                                                           | Geralmente vazio                             |
| `payment_terms`  | `//PAYMENT_TERMS`                                                         | Geralmente vazio                             |
| `purchase_order` | `//PURCHASE_ORDER`                                                        | Geralmente vazio                             |

### Tabela de itens de linha (`INVOICE_TABLE`)

Caminho da linha: `<items>/<item>`, `<Items>/<Item>` ou `<Detalle>/<Linea>`

| Coluna        | Atributo / Elemento de origem           | Observações                  |
| ------------- | --------------------------------------- | ---------------------------- |
| `POSITION`    | `@numero`, `<numero>` ou `position()`   | Número de sequência do item  |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>`        |                              |
| `QUANTITY`    | `<cantidad>`, `<Cantidad>`              |                              |
| `UNIT_PRICE`  | `<precioUnitario>`, `<PrecioUnitario>`  |                              |
| `VAT_RATE`    | `<alicuotaIVA>`, `<AlicuotaIVA>`        | por exemplo, `21.00`         |
| `VAT`         | `<importeIVA>`, `<ImporteIVA>`          |                              |
| `NET_AMOUNT`  | `<subtotal>`, `<Subtotal>`, `<importe>` | Total da linha               |

## Regra de classificação

O DocBits detecta documentos ARGENTINA FACTURA ELECTRONICA pela ausência do marcador da Factura A: documentos com valores de `<tipoComprobante>` diferentes de `001` (por exemplo, `003`, `006`, `011`) são direcionados a este padrão.

## Relacionados

* [ARGENTINA AFIP](argentina-afip.md)
* [Documentos eletrônicos compatíveis](./)
