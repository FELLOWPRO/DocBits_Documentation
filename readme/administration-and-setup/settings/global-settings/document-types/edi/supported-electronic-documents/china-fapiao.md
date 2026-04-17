---
description: Soporte para documentos electrónicos CHINA FAPIAO en DocBits
---

# 🇨🇳 CHINA FAPIAO

| Propiedad | Valor |
|----------|-------|
| **País / Región** | China |
| **Tipos de documento** | Factura IVA general, Factura IVA especial, E-Fapiao |
| **Formato** | XML |
| **Norma** | Fapiao (发票), State Taxation Administration |
| **Locale** | `zh_CN` |
| **Namespace XML** | `urn:china:tax:fapiao:1.0` |

Fapiao (发票) es el sistema chino de facturación fiscal electrónica regulado por la State Taxation Administration (国家税务总局). Todos los documentos Fapiao comparten el namespace XML `urn:china:tax:fapiao:1.0`. DocBits detecta automáticamente el tipo de Fapiao y dirige hacia las reglas de extracción apropiadas:

| Tipo de Fapiao | Código | Descripción |
|-----------|------|-------------|
| 普通发票 | General VAT Invoice | Factura IVA general (普通发票) |
| 专用发票 | Special VAT Invoice | Factura IVA especial (专用发票) — deducible |

## Estado del soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="china-fapiao-preview.png" alt="Vista previa de factura China Fapiao en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una CHINA GENERAL VAT INVOICE (普通发票)</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `fapiao_number` | Número de factura (8 dígitos) |
| `invoice_code` | `fapiao_code` | Código de factura (10-12 dígitos) |
| `invoice_date` | `issue_date` | Fecha de emisión ISO 8601 |
| `fapiao_type` | `fapiao_type` | Tipo: 普通发票 o 专用发票 |
| `check_code` | `check_code` | Código de verificación (20 dígitos) |
| `machine_code` | `machine_code` | Número de máquina fiscal |
| `currency` | Fijo: `CNY` | Siempre yuan chino |
| `total_amount` | `total_with_tax` | Importe total con IVA (价税合计) |
| `net_amount` | `total_amount` | Importe neto (金额) |
| `tax_amount` | `total_tax` | Importe del IVA (税额) |
| `amount_in_words` | `amount_in_words` | Importe en caracteres chinos (大写) |
| `supplier_name` | `seller/name` | Nombre de la empresa emisora (销售方) |
| `supplier_id` | `seller/taxpayer_id` | Identificación fiscal del emisor (18 caracteres) |
| `supplier_address` | `seller/address` | Dirección del emisor |
| `supplier_telephone` | `seller/telephone` | Teléfono del emisor |
| `supplier_bank_name` | `seller/bank_name` | Banco del emisor |
| `supplier_bank_account` | `seller/bank_account` | Cuenta bancaria del emisor |
| `buyer_name` | `buyer/name` | Nombre de la empresa destinataria (购买方) |
| `buyer_id` | `buyer/taxpayer_id` | Identificación fiscal del destinatario |
| `buyer_address` | `buyer/address` | Dirección del destinatario |
| `buyer_telephone` | `buyer/telephone` | Teléfono del destinatario |
| `remarks` | `remarks` | Observaciones (备注) |
| `issuer` | `issuer` | Emisor (开票人) |
| `tax_authority` | `tax_authority` | Autoridad fiscal (税务机关) |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de la línea: `items/item`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `SEQ` | `seq` | Número de línea |
| `ITEM_NAME` | `name` | Descripción del artículo |
| `SPEC` | `spec` | Especificación / modelo |
| `UNIT` | `unit` | Unidad de medida |
| `QUANTITY` | `quantity` | Cantidad |
| `UNIT_PRICE` | `unit_price` | Precio unitario neto |
| `AMOUNT` | `amount` | Total de la línea neto |
| `TAX_RATE` | `tax_rate` | Tasa de IVA en % (13% o 9%) |
| `TAX_AMOUNT` | `tax_amount` | IVA por línea |

## Reglas de clasificación

DocBits detecta documentos China Fapiao comparando el namespace XML y el tipo de Fapiao:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0" version="1.0">` |
| CHINA SPECIAL VAT INVOICE | `<fapiao xmlns="urn:china:tax:fapiao:1.0"` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA FAPIAO | `<fapiao` (coincidencia genérica) |
| CHINA FAPIAO | `税务总局` (coincidencia de texto) |
| CHINA VAT INVOICE | `<VATInvoice` (formato heredado) |

La clasificación usa el principio **FIRST MATCH WINS** ordenado por longitud de patrón (el más largo primero). El elemento raíz es `<fapiao>` con el namespace `urn:china:tax:fapiao:1.0`.

## Véase también

- [Normas de e-facturación actualmente soportadas](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos soportados](./)
