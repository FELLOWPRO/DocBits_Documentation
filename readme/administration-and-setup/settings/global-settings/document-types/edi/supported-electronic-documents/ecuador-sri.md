---
description: Soporte de documentos electrónicos Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) en DocBits
---

# 🇪🇨 Ecuador SRI

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Ecuador |
| **Tipos de Documento** | Factura (Invoice), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Formato** | XML |
| **Estándar** | SRI (Servicio de Rentas Internas) |
| **Configuración regional** | `es_EC` |

El estándar de factura electrónica Ecuador SRI es emitido bajo la autoridad del Servicio de Rentas Internas (SRI), la autoridad tributaria de Ecuador. Los documentos utilizan un formato XML propietario con un elemento raíz `<factura id="comprobante" version="X.X.X">`. DocBits detecta automáticamente la versión a partir del atributo `version` y el tipo de documento a partir de `codDoc`:

| Atributo version | Tipo de Documento |
|------------------|-------------------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

El número de factura es un compuesto de tres campos: `estab-ptoEmi-secuencial` (p. ej. `001-001-000000001`). La `claveAcceso` es una clave de acceso de 49 dígitos emitida por el SRI para la autenticación de documentos. Ecuador utiliza el **Dólar Estadounidense (USD)** como moneda oficial.

## Estado de Soporte

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista Previa Predeterminada

<figure><img src="ecuador-sri-preview.png" alt="Vista previa de Ecuador SRI Factura en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una Factura Electrónica Ecuador SRI (versión 2.1.0)</p></figcaption></figure>

## Mapeo de Campos

### Campos de Cabecera

| Campo DocBits | Elemento XML Fuente | Notas |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Compuesto: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Formato de fecha `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Plazo de pago (p. ej. `30 dias`) |
| `currency` | Fijo: `USD` | Siempre Dólar Estadounidense (moneda oficial de Ecuador) |
| `invoice_type` | Fijo: `Factura` | Etiqueta del tipo de documento |
| `net_amount` | `infoFactura/totalSinImpuestos` | Total neto sin IVA |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | Monto del IVA |
| `total_amount` | `infoFactura/importeTotal` | Monto total con IVA |
| `supplier_name` | `infoTributaria/razonSocial` | Nombre de la empresa emisora |
| `supplier_id` | `infoTributaria/ruc` | RUC — identificación tributaria de 13 dígitos |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (igual que supplier_id) |
| `supplier_address` | `infoTributaria/dirMatriz` | Dirección de la sede del emisor |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | Código de forma de pago SRI |
| `buyer_name` | `infoFactura/razonSocialComprador` | Nombre de la empresa compradora |
| `buyer_id` | `infoFactura/identificacionComprador` | RUC o CI del comprador |

### Tabla de Líneas de Detalle (`INVOICE_TABLE`)

Ruta de fila: `detalles/detalle`

| Columna | Elemento XML Fuente | Notas |
|---|---|---|
| `POSITION` | Índice secuencial | Número de línea desde 1 |
| `DESCRIPTION` | `descripcion` | Descripción del artículo |
| `QUANTITY` | `cantidad` | Cantidad |
| `UNIT_PRICE` | `precioUnitario` | Precio unitario sin IVA |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | Tasa de IVA en % (p. ej. 15%) |
| `VAT` | `impuestos/impuesto/valor` | Monto del IVA por línea |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | Total de línea sin IVA |

## Reglas de Clasificación

DocBits detecta los documentos Ecuador SRI haciendo coincidir el elemento raíz y el atributo de versión:

| Tipo de Documento Electrónico | Patrón |
|-------------------------------|--------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (cualquier versión) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

El elemento raíz es `<factura>` con `id="comprobante"`. El atributo `version` determina la versión específica del SRI. La clasificación utiliza el principio **primera coincidencia gana**, ordenado por longitud del patrón (el más largo/específico primero).

## Relacionado

- [Estándares de Factura Electrónica Actualmente Compatibles](../../currently-supported-e-invoice-standards/)
- [Documentos Electrónicos Compatibles](./)
