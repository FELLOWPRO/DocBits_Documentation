---
description: Soporte de documentos electrónicos ARGENTINA AFIP en DocBits
---

# 🇦🇷 ARGENTINA AFIP

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Argentina |
| **Tipos de documento** | Factura |
| **Formato** | XML |
| **Estándar** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Idioma** | `es_AR` |

El estándar ARGENTINA AFIP es el formato de factura electrónica de la autoridad tributaria federal argentina (AFIP). Los documentos se identifican mediante `<tipoComprobante>` — por ejemplo, tipo `001` = Factura A. Cada factura incluye un número CAE (Código de Autorización Electrónica) y un código de barras para la validación de AFIP.

## Estado de soporte

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="argentina-afip-preview.png" alt="Vista previa de factura ARGENTINA AFIP en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura ARGENTINA AFIP Factura A</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | Elemento XML de origen | Notas |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Formato: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Fijo: `ARS` | Siempre Peso Argentino |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` o `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` o `<cabecera>/<CUIT>` | CUIT = número de identificación fiscal argentino |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Fijo: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Fijo: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Generalmente vacío |
| `bic` | `<PAYMENT/BIC>` | Generalmente vacío |
| `payment_terms` | `<PAYMENT_TERMS>` | Generalmente vacío |
| `purchase_order` | `<PURCHASE_ORDER>` | Generalmente vacío |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `<items>/<item>`

| Columna | Atributo / Elemento de origen | Notas |
|---|---|---|
| `POSITION` | Atributo `@numero` | Número de posición |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | Código de unidad AFIP (p.ej. `7` = unidad) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | p.ej. `21.00` para el IVA estándar argentino |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Total de línea antes de impuestos |

## Regla de clasificación

DocBits detecta documentos ARGENTINA AFIP mediante el patrón regex:

```
<tipoComprobante>001\s*</tipoComprobante>
```

El tipo `001` corresponde a **Factura A**.

## Relacionados

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Documentos electrónicos compatibles](./)
