---
description: Suporte a documentos eletrônicos ARGENTINA AFIP no DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Propriedade          | Valor                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| **País / Região**    | Argentina                                                                  |
| **Tipos de documento** | Invoice                                                                  |
| **Formato**          | XML                                                                        |
| **Padrão**           | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Localidade**       | `es_AR`                                                                    |

O padrão ARGENTINA AFIP é o formato de fatura eletrônica da autoridade tributária federal argentina (AFIP). Os documentos são identificados por `<tipoComprobante>`, por exemplo, o tipo `001` = Factura A. Cada fatura inclui um número CAE (Código de Autorización Electrónica) e um código de barras para a validação da AFIP.

## Status de suporte

| Componente          | Status      |
| ------------------- | ----------- |
| Preview             | ✅ Suportado |
| Extração de campos  | ✅ Suportado |
| Transformação       | ✅ Suportado |

## Preview padrão

<figure><img src="../../../../../../.gitbook/assets/argentina-afip-preview.png" alt="Preview de fatura ARGENTINA AFIP no DocBits"><figcaption><p>Preview padrão do DocBits para uma fatura Factura A da ARGENTINA AFIP</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo do DocBits       | Elemento XML de origem                               | Observações                                        |
| ---------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| `invoice_id`           | `<puntoVenta>` + `<numeroComprobante>`               | Formatado como `PPPP-NNNNNNNN`                     |
| `invoice_date`         | `<cabecera>/<fechaEmision>`                          |                                                    |
| `due_date`             | `<cabecera>/<fechaVencimiento>`                      |                                                    |
| `currency`             | Fixo: `ARS`                                          | Sempre peso argentino                              |
| `total_amount`         | `<totales>/<total>`                                  |                                                    |
| `net_amount`           | `<totales>/<netoGravado>` ou `<subtotal>`            |                                                    |
| `tax_amount`           | `<totales>/<totalIVA>`                               |                                                    |
| `supplier_name`        | `<emisor>/<razonSocial>`                             |                                                    |
| `supplier_id`          | `<emisor>/<CUIT>` ou `<cabecera>/<CUIT>`             | CUIT = identificação fiscal argentina              |
| `supplier_address`     | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` |                                                    |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>`       |                                                    |
| `supplier_city`        | `<emisor>/<domicilioComercial>/<localidad>`          |                                                    |
| `supplier_country`     | Fixo: `AR`                                           |                                                    |
| `buyer_name`           | `<receptor>/<razonSocial>`                           |                                                    |
| `buyer_id`             | `<receptor>/<CUIT>`                                  |                                                    |
| `buyer_address`        | `<receptor>/<domicilio>/<calle>` + `<numero>`        |                                                    |
| `buyer_postal_code`    | `<receptor>/<domicilio>/<codigoPostal>`              |                                                    |
| `buyer_city`           | `<receptor>/<domicilio>/<localidad>`                 |                                                    |
| `buyer_country`        | Fixo: `AR`                                           |                                                    |
| `iban`                 | `<PAYMENT/IBAN>`                                     | Geralmente vazio, pois documentos da AFIP raramente contêm dados bancários |
| `bic`                  | `<PAYMENT/BIC>`                                      | Geralmente vazio                                   |
| `payment_terms`        | `<PAYMENT_TERMS>`                                    | Geralmente vazio                                   |
| `purchase_order`       | `<PURCHASE_ORDER>`                                   | Geralmente vazio                                   |

### Tabela de itens de linha (`INVOICE_TABLE`)

Caminho da linha: `<items>/<item>`

| Coluna        | Atributo / Elemento de origem | Observações                                  |
| ------------- | -------------------------- | --------------------------------------- |
| `POSITION`    | atributo `@numero`         | Número de sequência do item             |
| `DESCRIPTION` | `<descripcion>`            |                                         |
| `QUANTITY`    | `<cantidad>`               |                                         |
| `UNIT`        | `<unidadMedida>`           | Código de unidade da AFIP (por exemplo, `7` = unidade) |
| `UNIT_PRICE`  | `<precioUnitario>`         |                                         |
| `VAT_RATE`    | `<alicuotaIVA>`            | por exemplo, `21.00` para o IVA padrão argentino |
| `VAT`         | `<importeIVA>`             |                                         |
| `NET_AMOUNT`  | `<subtotal>`               | Total da linha antes dos impostos       |

## Regra de classificação

O DocBits detecta documentos ARGENTINA AFIP por meio do seguinte padrão regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

O tipo `001` corresponde à **Factura A** (fatura para compradores registrados no IVA). Os demais tipos de comprobante são tratados pelo padrão ARGENTINA FACTURA ELECTRONICA.

## Relacionados

* [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
* [Documentos eletrônicos compatíveis](./)
