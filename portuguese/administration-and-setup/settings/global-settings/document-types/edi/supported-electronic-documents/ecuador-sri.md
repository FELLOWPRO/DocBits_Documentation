---
description: >-
  Suporte a documentos eletrônicos Ecuador SRI (Factura Electrónica, SRI 1.0.0 –
  2.1.0) no DocBits
---

# 🇪🇨 ECUADOR SRI

| Propriedade | Valor |
| --- | --- |
| **País / Região** | Equador |
| **Tipos de documento** | Factura (fatura), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Formato** | XML |
| **Padrão** | SRI (Servicio de Rentas Internas) |
| **Idioma** | `es_EC` |

O padrão de fatura eletrônica Ecuador SRI é emitido sob a autoridade do Servicio de Rentas Internas (SRI), a autoridade tributária do Equador. Os documentos usam um formato XML proprietário com o elemento raiz `<factura id="comprobante" version="X.X.X">`. O DocBits detecta automaticamente a versão a partir do atributo `version` e o tipo de documento a partir de `codDoc`:

| Atributo version | Tipo de documento |
| --- | --- |
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

O número da fatura é uma composição de três campos: `estab-ptoEmi-secuencial` (por exemplo, `001-001-000000001`). A `claveAcceso` é uma chave de acesso de 49 dígitos emitida pelo SRI para a autenticação do documento. O Equador usa o **dólar americano (USD)** como moeda oficial.

## Status de suporte

| Componente | Status |
| --- | --- |
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/ecuador-sri-preview.png" alt="Visualização de Factura Ecuador SRI no DocBits"><figcaption><p>Visualização padrão do DocBits para uma Factura Electrónica Ecuador SRI (versão 2.1.0)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
| --- | --- | --- |
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Composição: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Formato de data `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Prazo de pagamento (por exemplo, `30 dias`) |
| `currency` | Fixo: `USD` | Sempre dólar americano (moeda oficial do Equador) |
| `invoice_type` | Fixo: `Factura` | Rótulo do tipo de documento |
| `net_amount` | `infoFactura/totalSinImpuestos` | Total líquido sem IVA |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Valor do IVA |
| `total_amount` | `infoFactura/importeTotal` | Valor total com IVA |
| `supplier_name` | `infoTributaria/razonSocial` | Nome da empresa emitente |
| `supplier_id` | `infoTributaria/ruc` | RUC — identificação do contribuinte com 13 dígitos |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (igual a supplier\_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Endereço da sede do emitente |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | Código da forma de pagamento do SRI |
| `buyer_name` | `infoFactura/razonSocialComprador` | Nome da empresa compradora |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC ou CI do comprador |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `detalles/detalle`

| Coluna | Elemento XML de origem | Observações |
| --- | --- | --- |
| `POSITION` | Índice sequencial | Número da linha, a partir de 1 |
| `DESCRIPTION` | `descripcion` | Descrição do item |
| `QUANTITY` | `cantidad` | Quantidade |
| `UNIT_PRICE` | `precioUnitario` | Preço unitário sem IVA |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Alíquota de IVA em % (por exemplo, 15%) |
| `VAT` | `impuestos/impuesto/valor` | Valor do IVA por linha |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Total da linha sem IVA |

## Regras de classificação

O DocBits detecta documentos Ecuador SRI por meio da correspondência com o elemento raiz e o atributo de versão:

| Tipo de documento eletrônico | Padrão |
| --- | --- |
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (qualquer versão) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

O elemento raiz é `<factura>` com `id="comprobante"`. O atributo `version` determina a versão específica do SRI. A classificação usa o princípio **first-match-wins** (a primeira correspondência prevalece), ordenado pelo comprimento do padrão (o mais longo/mais específico primeiro).

## Relacionado

* [Padrões de Fatura Eletrônica Atualmente Suportados](../../currently-supported-e-invoice-standards/)
* [Documentos Eletrônicos Suportados](./)
