---
description: Soporte de documentos electrónicos CHILE DTE en DocBits
---

# 🇨🇱 CHILE DTE

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Chile |
| **Tipos de documento** | Factura, Nota de crédito, Nota de débito, Guía de despacho |
| **Formato** | XML |
| **Estándar** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) es el estándar chileno de documentos tributarios electrónicos regulado por el Servicio de Impuestos Internos (SII). Todos los documentos DTE comparten el namespace `http://www.sii.cl/SiiDte`. DocBits detecta automáticamente el código de tipo DTE (`TipoDTE`) y lo dirige a las reglas de extracción correspondientes:

| Código de tipo | Tipo de documento |
|-----------|--------------|
| 33 | Factura Electrónica |
| 34 | Factura No Afecta o Exenta |
| 52 | Guía de Despacho |
| 56 | Nota de Débito |
| 61 | Nota de Crédito |

## Estado del soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="chile-dte-preview.png" alt="Vista previa de factura Chile DTE en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una CHILE DTE FACTURA (tipo 33)</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `Folio` | Número de folio del documento |
| `invoice_date` | `FchEmis` | Fecha de emisión ISO 8601 |
| `due_date` | `FchVenc` | Fecha de vencimiento |
| `currency` | Fijo: `CLP` | Siempre peso chileno |
| `total_amount` | `MntTotal` | Monto total incl. IVA |
| `net_amount` | `MntNeto` | Monto neto imponible |
| `tax_amount` | `IVA` | Monto del IVA (tasa estándar 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nombre de la empresa emisora |
| `supplier_id` | `RUTEmisor` | RUT del emisor (ej. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Dirección del emisor |
| `supplier_city` | `CiudadOrigen` | Ciudad del emisor |
| `supplier_country` | Fijo: `CL` | Siempre Chile |
| `buyer_name` | `RznSocRecep` | Nombre de la empresa receptora |
| `buyer_id` | `RUTRecep` | RUT del receptor |
| `buyer_address` | `DirRecep` | Dirección del receptor |
| `buyer_city` | `CiudadRecep` | Ciudad del receptor |
| `buyer_country` | Fijo: `CL` | Siempre Chile |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `Detalle`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `NroLinDet` | Número de línea |
| `DESCRIPTION` | `NmbItem` | Nombre del ítem |
| `QUANTITY` | `QtyItem` | Cantidad |
| `UNIT` | `UnmdItem` | Unidad de medida |
| `UNIT_PRICE` | `PrcItem` | Precio unitario excl. IVA |
| `VAT_RATE` | `TasaIVA` (del encabezado) | Tasa de IVA en % (típicamente 19%) |
| `VAT` | Calculado | IVA por línea |
| `NET_AMOUNT` | `MontoItem` | Total de línea |

## Reglas de clasificación

DocBits detecta documentos Chile DTE coincidiendo el namespace XML y `TipoDTE`:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

El elemento envolvente es `<EnvioDTE>` y cada DTE está envuelto en `<DTE><Documento>`.

## Véase también

- [Estándares de e-factura actualmente soportados](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos soportados](./)
