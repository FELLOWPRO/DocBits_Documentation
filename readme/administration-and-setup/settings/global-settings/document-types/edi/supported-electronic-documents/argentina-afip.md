---
description: Suporte a documentos eletrônicos ARGENTINA AFIP no DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Propriedade | Valor |
|-------------|-------|
| **País / Região** | Argentina |
| **Tipos de documento** | Fatura |
| **Formato** | XML |
| **Padrão** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Idioma** | `es_AR` |

O padrão ARGENTINA AFIP é o formato de fatura eletrônica da autoridade tributária federal argentina (AFIP). Os documentos são identificados pelo `<tipoComprobante>` — por exemplo, tipo `001` = Factura A. Cada fatura inclui um número CAE (Código de Autorización Electrónica) e um código de barras para validação da AFIP.

## Status de suporte

| Componente | Status |
|------------|--------|
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="argentina-afip-preview.png" alt="Visualização de fatura ARGENTINA AFIP no DocBits"><figcaption><p>Visualização padrão do DocBits para uma fatura ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Formato: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Fixo: `ARS` | Sempre Peso Argentino |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` ou `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` ou `<cabecera>/<CUIT>` | CUIT = número de identificação fiscal argentino |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Fixo: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Fixo: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Geralmente vazio |
| `bic` | `<PAYMENT/BIC>` | Geralmente vazio |
| `payment_terms` | `<PAYMENT_TERMS>` | Geralmente vazio |
| `purchase_order` | `<PURCHASE_ORDER>` | Geralmente vazio |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `<items>/<item>`

| Coluna | Atributo / Elemento de origem | Observações |
|---|---|---|
| `POSITION` | Atributo `@numero` | Número de posição |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | Código de unidade AFIP (ex. `7` = unidade) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | ex. `21.00` para o IVA padrão argentino |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Total da linha antes dos impostos |

## Regra de classificação

O DocBits detecta documentos ARGENTINA AFIP por meio do padrão regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

## Relacionados

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Documentos eletrônicos suportados](./)
