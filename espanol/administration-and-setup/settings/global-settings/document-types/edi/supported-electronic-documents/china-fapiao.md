---
description: Soporte para documentos electrónicos China Fapiao (FAPIAO, E-FAPIAO, Factura IVA General, Factura IVA Especial) en DocBits
---

# 🇨🇳 China Fapiao

| Propiedad | Valor |
|----------|-------|
| **País / Región** | China |
| **Tipos de documento** | Factura IVA General (普通发票), Factura IVA Especial (专用发票), E-Fapiao |
| **Formato** | XML |
| **Estándar** | Fapiao (发票), State Taxation Administration |
| **Configuración regional** | `zh_CN` |

Fapiao (发票) es el estándar chino de factura fiscal emitido bajo la autoridad de la Administración Estatal de Tributación (STA / 国家税务总局). Todos los documentos Fapiao comparten el espacio de nombres `urn:china:tax:fapiao:1.0`. DocBits detecta automáticamente el tipo de Fapiao mediante el elemento `fapiao_type` y lo dirige a las reglas de extracción correspondientes:

| Valor de fapiao_type | Tipo de documento |
|-------------------|--------------|
| 普通发票 | Factura IVA General (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Factura IVA Especial (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Estado del soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Supported |
| Extracción de campos | ✅ Supported |
| Transformación | ✅ Supported |

## Vista previa predeterminada

<figure><img src="china-fapiao-preview.png" alt="Vista previa de la Factura IVA General China Fapiao en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una Factura IVA General China Fapiao (普通发票)</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Número Fapiao — 8 dígitos (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Fecha de emisión (ISO 8601) |
| `currency` | Fijo: `CNY` | Siempre Yuan Renminbi chino |
| `total_amount` | `total/total_with_tax` | Importe total con IVA (价税合计) |
| `net_amount` | `total/total_amount` | Importe neto gravable sin IVA (金额) |
| `tax_amount` | `total/total_tax` | Importe total del IVA (税额) |
| `supplier_name` | `seller/name` | Nombre de la empresa vendedora (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | ID fiscal del vendedor — 18 caracteres (纳税人识别号) |
| `supplier_address` | `seller/address` | Dirección del vendedor |
| `supplier_country` | Fijo: `CN` | Siempre China |
| `iban` | `seller/bank_account` | Número de cuenta bancaria del vendedor |
| `buyer_name` | `buyer/name` | Nombre de la empresa compradora (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | ID fiscal del comprador (纳税人识别号) |
| `buyer_address` | `buyer/address` | Dirección del comprador |
| `buyer_country` | Fijo: `CN` | Siempre China |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `items/item`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `seq` | Número de secuencia de línea |
| `DESCRIPTION` | `name` + `spec` | Nombre del artículo y especificación (concatenados) |
| `QUANTITY` | `quantity` | Cantidad |
| `UNIT` | `unit` | Unidad de medida (p. ej. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | Precio unitario sin IVA |
| `VAT_RATE` | `tax_rate` | Tasa de IVA en % (normalmente 6%, 9% o 13%) |
| `VAT` | `tax_amount` | Importe del IVA por línea |
| `NET_AMOUNT` | `amount` | Total de la línea sin IVA |

## Reglas de clasificación

DocBits detecta documentos China Fapiao haciendo coincidir el espacio de nombres XML y el `fapiao_type`:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

El elemento raíz es `<fapiao>` con el espacio de nombres `urn:china:tax:fapiao:1.0`. La clasificación utiliza el principio **first-match-wins** ordenado por longitud de patrón (el más largo primero).

## Relacionado

- [Estándares de e-factura actualmente soportados](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos soportados](./)
