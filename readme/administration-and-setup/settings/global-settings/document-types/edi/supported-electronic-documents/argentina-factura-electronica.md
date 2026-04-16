---
description: Suporte a documentos eletrônicos ARGENTINA FACTURA ELECTRONICA no DocBits
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Propriedade | Valor |
|-------------|-------|
| **País / Região** | Argentina |
| **Tipos de documento** | Fatura |
| **Formato** | XML |
| **Padrão** | Argentina Factura Electrónica (tipos de comprobante AFIP além da Factura A) |
| **Idioma** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA abrange o conjunto mais amplo de documentos eletrônicos AFIP argentinos além da Factura A (tipo 001). Isso inclui Factura B (tipo 006), Factura C (tipo 011), Nota de Crédito (tipo 003) e outras variantes.

## Status de suporte

| Componente | Status |
|------------|--------|
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="argentina-factura-electronica-preview.png" alt="Visualização Argentina Factura Electronica no DocBits"><figcaption><p>Visualização padrão do DocBits para um documento ARGENTINA FACTURA ELECTRONICA</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elementos XML de origem | Observações |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Múltiplos fallbacks XPath |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, fallback: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `<items>/<item>`, `<Items>/<Item>` ou `<Detalle>/<Linea>`

| Coluna | Fonte | Observações |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` ou `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Regra de classificação

Documentos com valores `<tipoComprobante>` diferentes de `001` são roteados para este padrão.

## Relacionados

- [ARGENTINA AFIP](argentina-afip.md)
- [Documentos eletrônicos suportados](./)
