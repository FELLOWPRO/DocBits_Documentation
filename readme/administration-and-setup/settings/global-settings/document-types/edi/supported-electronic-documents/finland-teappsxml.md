---
description: Compatibilidad con documentos electrónicos TEAPPSXML de Finlandia en DocBits
---

# 🇫🇮 Finlandia TEAPPSXML

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Finlandia |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | XML |
| **Estándar** | TEAPPSXML 3.0 (Tieto / Sector bancario finlandés) |
| **Configuración regional** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) es un estándar de factura electrónica finlandés utilizado principalmente en el sector bancario y financiero. El elemento raíz es `<TEAPPSXML>` con el espacio de nombres `urn:TEAPPSXML:3.0`. DocBits detecta los documentos TEAPPSXML por la presencia de `xmlns="urn:TEAPPSXML:"` en el elemento raíz.

El formato TEAPPSXML utiliza nombres de elementos en mayúsculas y una estructura plana con secciones separadas `<SENDER>`, `<RECEIVER>`, `<INVOICE>` y `<PAYMENTINFO>`. El formato del ID empresarial finlandés (Y-tunnus) es `1234567-8`, y los números de IVA utilizan el prefijo `FI` (ej. `FI12345678`).

## Estado de compatibilidad

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="finland-teappsxml-preview.png" alt="Vista previa de factura TEAPPSXML de Finlandia en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura TEAPPSXML de Finlandia</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Número de factura |
| `invoice_date` | `INVOICE/INVOICEDATE` | Fecha de emisión (AAAA-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Fecha de vencimiento del pago (AAAA-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Tipo de mensaje (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Código de divisa (típicamente `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Número de referencia de pago |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Referencia de pago finlandesa (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Importe neto sin IVA |
| `tax_amount` | `INVOICE/TOTALVAT` | Importe total de IVA |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Importe total con IVA |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Método de pago (ej. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Nombre de la empresa remitente |
| `supplier_id` | `SENDER/ID` | ID empresarial finlandés (Y-tunnus, ej. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Número de IVA (ej. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Dirección del remitente |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Ciudad del remitente |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Código postal del remitente |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | Código de país ISO (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Código BIC del banco del remitente |
| `buyer_name` | `INVOICE/BUYER/NAME` | Nombre de la empresa compradora |
| `buyer_id` | `INVOICE/BUYER/ID` | ID empresarial finlandés del comprador |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Dirección del comprador |
| `buyer_city` | `INVOICE/BUYER/CITY` | Ciudad del comprador |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Código postal del comprador |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | Código de país ISO (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN del beneficiario |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Código BIC del beneficiario |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `INVOICE/LINES/LINE`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `LINENUMBER` | Número de secuencia de línea |
| `DESCRIPTION` | `ARTICLENAME` | Nombre / descripción del artículo |
| `QUANTITY` | `QUANTITY` | Cantidad facturada |
| `UNIT` | `UNIT` | Unidad de medida (ej. `KPL` = pieza) |
| `UNIT_PRICE` | `UNITPRICE` | Precio unitario sin IVA |
| `VAT_RATE` | `VATRATE` | Tipo de IVA en % (estándar 25,5%) |
| `VAT` | Calculado | Importe de IVA por línea |
| `NET_AMOUNT` | `LINEAMOUNT` | Total de línea sin IVA |

## Regla de clasificación

DocBits detecta los documentos TEAPPSXML haciendo coincidir el atributo `xmlns` en el elemento raíz `<TEAPPSXML>`:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| TEAPPSXML | `xmlns` contiene `urn:TEAPPSXML:` |

## Relacionados

- [Estándares de facturación electrónica actualmente compatibles](../../currently-supported-e-invoice-standards/)
- [Finlandia Finvoice](./finland-finvoice.md)
- [Documentos electrónicos compatibles](./)
