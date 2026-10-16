---
description: Compatibilidad con la factura electrónica GST de India en DocBits
---

# 🇮🇳 India GST E-Invoice

| Propiedad | Valor |
|----------|-------|
| **País / Región** | India |
| **Tipos de documento** | Factura (INV), Nota de crédito (CRN), Nota de débito (DBN) |
| **Formato** | XML (`<SignedInvoice>`) |
| **Estándar** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

La factura electrónica GST de India es el estándar obligatorio de facturación electrónica en el marco del régimen GST (Goods and Services Tax) de India, operado por el GSTN (GST Network). Las empresas que superan el umbral de facturación prescrito deben generar e-facturas a través del portal IRP (Invoice Registration Portal), que firma la factura y devuelve un **IRN** (Invoice Reference Number — un hash SHA-256 de 64 caracteres) y un código QR.

DocBits detecta los documentos GST E-Invoice por la presencia de `<SignedInvoice>` como elemento raíz. El formato incluye tres componentes fiscales GST:

| Componente fiscal | Descripción |
|--------------|-------------|
| IGST | GST integrado — aplicado en transacciones entre estados |
| CGST | GST central — aplicado en transacciones dentro del estado (componente central) |
| SGST | GST estatal — aplicado en transacciones dentro del estado (componente estatal) |

El identificador del contribuyente es el **GSTIN** (Goods and Services Tax Identification Number), un código alfanumérico de 15 caracteres con el formato `29AABCU9603R1ZM` (código de estado de 2 dígitos + PAN de 10 dígitos + número de entidad + dígito de control). Las fechas usan el formato `DD/MM/AAAA`.

## Estado de soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura electrónica GST de India</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Número de factura |
| `invoice_date` | `Invoice/DocDtls/Dt` | Fecha de emisión (`DD/MM/AAAA`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Factura, CRN=Nota de crédito, DBN=Nota de débito |
| `currency` | Fijo: `INR` | Siempre en rupia india |
| `net_amount` | `Invoice/ValDtls/AssVal` | Valor imponible / gravable |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Importe total del GST |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | Valor total de la factura incl. GST |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Importe del GST integrado |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Importe del GST central |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Importe del GST estatal |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Importe del cess (si aplica) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Nombre legal del vendedor |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | GSTIN del vendedor (15 caracteres, ej. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Nombre comercial del vendedor |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Dirección del vendedor línea 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Ciudad / ubicación del vendedor |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Código PIN del vendedor |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Código de estado del vendedor (2 dígitos) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Nombre legal del comprador |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | GSTIN del comprador |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Nombre comercial del comprador |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Dirección del comprador línea 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Ciudad / ubicación del comprador |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Código PIN del comprador |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Código de estado del comprador |
| `irn` | `Irn` | Número de referencia de factura (hash SHA-256 de 64 caracteres) |
| `ack_number` | `AckNo` | Número de acuse de recibo IRP |
| `ack_date` | `AckDt` | Fecha de acuse de recibo IRP |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `Invoice/ItemList/Item`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `SlNo` | Número de secuencia de línea |
| `DESCRIPTION` | `PrdDesc` | Descripción del producto / servicio |
| `QUANTITY` | `Qty` | Cantidad facturada |
| `UNIT` | `Unit` | Unidad de medida (ej. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Precio unitario |
| `VAT_RATE` | `GstRt` | Tasa GST en % (ej. 18%) |
| `VAT` | `IgstAmt` (o `CgstAmt` + `SgstAmt`) | Importe GST por línea |
| `NET_AMOUNT` | `AssAmt` | Importe imponible por línea |

## Regla de clasificación

DocBits detecta los documentos India GST E-Invoice comparando el elemento raíz:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| INDIA GST E-INVOICE | El elemento raíz contiene `<SignedInvoice` |

## Relacionados

- [Estándares de factura electrónica actualmente compatibles](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos compatibles](./)
