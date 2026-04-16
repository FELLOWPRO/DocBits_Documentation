---
description: Soporte de documentos electrónicos CHILE DTE en DocBits
---

# 🇨🇱 CHILE DTE

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Chile |
| **Tipos de Documento** | Factura (Factura), Nota de Crédito, Nota de Débito, Guía de Despacho |
| **Formato** | XML |
| **Estándar** | DTE (Documento Tributario Electrónico), SII |
| **Configuración Regional** | `es_CL` |

DTE (Documento Tributario Electrónico) es el estándar chileno de documentos tributarios electrónicos regulado por el Servicio de Impuestos Internos (SII). Todos los documentos DTE comparten el espacio de nombres `http://www.sii.cl/SiiDte`. DocBits detecta automáticamente el código de tipo DTE (`TipoDTE`) y enruta a las reglas de extracción correspondientes:

| Código de Tipo | Tipo de Documento |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Estado de Soporte

| Componente | Estado |
|-----------|--------|
| Vista Previa | ✅ Soportado |
| Extracción de Campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista Previa Predeterminada

<figure><img src="chile-dte-preview.png" alt="Vista previa de Chile DTE Factura en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una CHILE DTE FACTURA (tipo 33)</p></figcaption></figure>

## Mapeo de Campos

### Campos de Encabezado

| Campo DocBits | Elemento XML Fuente | Notas |
|---|---|---|
| `invoice_id` | `Folio` | Número de folio del documento |
| `invoice_date` | `FchEmis` | Fecha de emisión ISO 8601 |
| `due_date` | `FchVenc` | Fecha de vencimiento del pago |
| `currency` | Fijo: `CLP` | Siempre Peso Chileno |
| `total_amount` | `MntTotal` | Monto total incl. IVA |
| `net_amount` | `MntNeto` | Monto neto imponible |
| `tax_amount` | `IVA` | Monto de IVA (tasa estándar 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nombre de la empresa emisora |
| `supplier_id` | `RUTEmisor` | RUT del emisor (p. ej. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Dirección del emisor |
| `supplier_city` | `CiudadOrigen` | Ciudad del emisor |
| `supplier_country` | Fijo: `CL` | Siempre Chile |
| `buyer_name` | `RznSocRecep` | Nombre de la empresa receptora |
| `buyer_id` | `RUTRecep` | RUT del receptor |
| `buyer_address` | `DirRecep` | Dirección del receptor |
| `buyer_city` | `CiudadRecep` | Ciudad del receptor |
| `buyer_country` | Fijo: `CL` | Siempre Chile |

### Tabla de Líneas de Detalle (`INVOICE_TABLE`)

Ruta de fila: `Detalle`

| Columna | Elemento XML Fuente | Notas |
|---|---|---|
| `POSITION` | `NroLinDet` | Número de secuencia de línea |
| `DESCRIPTION` | `NmbItem` | Nombre del artículo |
| `QUANTITY` | `QtyItem` | Cantidad |
| `UNIT` | `UnmdItem` | Unidad de medida |
| `UNIT_PRICE` | `PrcItem` | Precio unitario excl. IVA |
| `VAT_RATE` | `TasaIVA` (del encabezado) | Tasa de IVA en % (normalmente 19%) |
| `VAT` | Calculado | IVA por línea |
| `NET_AMOUNT` | `MontoItem` | Total de línea |

## Reglas de Clasificación

DocBits detecta documentos Chile DTE coincidiendo el espacio de nombres XML y `TipoDTE`:

| Tipo de Documento Electrónico | Patrón |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

El elemento envolvente es `<EnvioDTE>` y cada DTE está contenido en `<DTE><Documento>`.

## Relacionado

- [Estándares de Factura Electrónica Actualmente Soportados](../../currently-supported-e-invoice-standards/)
- [Documentos Electrónicos Soportados](./)
