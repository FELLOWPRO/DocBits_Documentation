---
description: Compatibilidad con documentos electrónicos DIAN de Colombia en DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Colombia DIAN

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Colombia |
| **Tipos de documento** | Factura (Factura Electrónica), Nota de Crédito (Nota de Crédito), Documento Soporte |
| **Formato** | XML (UBL 2.1) |
| **Estándar** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Configuración regional** | `es_CO` |

El estándar colombiano de facturación electrónica está regulado por la **DIAN** (Dirección de Impuestos y Aduanas Nacionales). Se basa en UBL 2.1 con extensiones específicas de DIAN (`sts:DianExtensions`). DocBits detecta los documentos Colombia DIAN a través del espacio de nombres DIAN y los enruta según el `CustomizationID`:

| CustomizationID | Tipo de documento |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Credit Note) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

El identificador DIAN (**NIT** — Número de Identificación Tributaria) utiliza `schemeID="31"` en el elemento UBL `CompanyID`.

## Estado de compatibilidad

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="colombia-dian-preview.png" alt="Vista previa de Colombia DIAN Factura Electrónica en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Asignación de campos

### Campos de cabecera

| Campo DocBits | Elemento XML origen | Notas |
|---|---|---|
| `invoice_id` | `cbc:ID` | Número de factura con prefijo (p. ej. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Fecha de emisión (ISO 8601) |
| `due_date` | `cbc:DueDate` | Fecha de vencimiento del pago |
| `currency` | `cbc:DocumentCurrencyCode` | Siempre `COP` (Peso colombiano) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Total a pagar incl. IVA |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Importe neto excl. IVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Importe total del IVA (tasa estándar 19 %) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Nombre legal del proveedor |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT del proveedor (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Nombre legal del comprador |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT del comprador (schemeID=31) |

### Tabla de líneas de pedido (`INVOICE_TABLE`)

Ruta de fila: `cac:InvoiceLine` (o `cac:CreditNoteLine`)

| Columna | Elemento XML origen | Notas |
|---|---|---|
| `POSITION` | `cbc:ID` | Número de línea |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descripción del producto o servicio |
| `QUANTITY` | `cbc:InvoicedQuantity` | Cantidad con atributo de código de unidad |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Precio unitario excl. IVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de línea excl. IVA |

## Reglas de clasificación

DocBits detecta los documentos Colombia DIAN mediante la cadena de espacio de nombres DIAN:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

El elemento raíz es `<Invoice>` (UBL 2.1) para facturas, `<CreditNote>` para notas de crédito. Todos los documentos incluyen un bloque `<sts:DianExtensions>` con datos de autorización DIAN (`InvoiceAuthorization`, UUID `CUFE`/`CUDE`, código QR).

## Relacionado

- [Estándares de factura electrónica compatibles actualmente](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos compatibles](./)
