---
description: Soporte de documentos electrónicos AUNZ PINT en DocBits
---

# 🇦🇺 AUNZ PINT

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Australia / Nueva Zelanda |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | UBL 2.1 XML |
| **Estándar** | PINT A-NZ (Modelo Peppol Internacional para Australia-Nueva Zelanda) |
| **Configuración regional** | `en_AU` |

AUNZ PINT es la implementación australiana/neozelandesa del modelo de facturación Peppol International (PINT). Define un formato de factura basado en UBL 2.1 adaptado a los requisitos regulatorios de A-NZ, incluyendo la identificación ABN/NZBN, el manejo del GST y el cumplimiento de las especificaciones de la A-NZ Peppol Authority. DocBits admite tanto los tipos de documento estándar Factura como Nota de crédito bajo el tipo de documento electrónico `PINT A-NZ`, así como la variante de autofacturación.

## Estado de soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="aunz-pint-preview.png" alt="Vista previa de factura AUNZ PINT en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura AUNZ PINT</p></figcaption></figure>

## Asignación de campos

### Campos de encabezado

| Campo DocBits | XPath de origen (UBL 2.1) | Notas |
|---|---|---|
| `invoice_id` | `cbc:ID` | Número de factura |
| `invoice_date` | `cbc:IssueDate` | Fecha ISO 8601 |
| `due_date` | `cbc:DueDate` | Fecha de vencimiento |
| `currency` | `cbc:DocumentCurrencyCode` | Típicamente `AUD` o `NZD` |
| `total_amount` | `cbc:PayableAmount` (en `cac:LegalMonetaryTotal`) | Total incl. GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (en `cac:LegalMonetaryTotal`) | Subtotal excl. GST |
| `tax_amount` | `cbc:TaxAmount` (en `cac:TaxTotal`) | Monto del GST |
| `purchase_order` | `cbc:BuyerReference` | Referencia de OC del comprador |
| `payment_terms` | `cbc:Note` (en `cac:PaymentTerms`) | Condiciones de pago en texto libre |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nombre del proveedor |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN o número GST |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Calle del proveedor |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Ciudad del proveedor |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Código postal del proveedor |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Código de país ISO (`AU` o `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nombre del comprador |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Calle del comprador |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Ciudad del comprador |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Código postal del comprador |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Código de país ISO |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | ID de cuenta de pago |

### Tabla de líneas de artículo (`INVOICE_TABLE`)

Ruta de filas: `cac:InvoiceLine`

| Columna | XPath de origen (UBL 2.1) | Notas |
|---|---|---|
| `POSITION` | `cbc:ID` | Número de línea |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descripción de producto/servicio |
| `QUANTITY` | `cbc:InvoicedQuantity` | Cantidad (código de unidad en `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Código de unidad (ej. `C62` = uno/pieza, `EA` = cada uno) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Precio unitario excl. GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | Tasa de GST en % |
| `VAT` | *(calculado a partir del monto de impuestos)* | Monto de GST por línea |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de línea excl. GST |

## Reglas de clasificación

DocBits detecta documentos PINT A-NZ coincidiendo con el elemento `CustomizationID`:

| Patrón | Tipo de regla | Tipo de documento electrónico |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Factura) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Factura de autofacturación) |

Ambos patrones se clasifican bajo el tipo de documento electrónico `PINT A-NZ`. El elemento raíz es `<Invoice>` para facturas estándar y `<CreditNote>` para notas de crédito.

### Características específicas de A-NZ

- **Identificadores ABN/NZBN**: Utiliza `schemeID="0151"` para Australian Business Numbers y New Zealand Business Numbers
- **Impuesto GST**: Utiliza la categoría impositiva `S` (tasa estándar) con el esquema de impuestos GST
- **CustomizationID**: Debe contener el sufijo `@aunz` para clasificarse como PINT A-NZ (vs. PINT global)

## Relacionado

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Documentos electrónicos soportados](./)