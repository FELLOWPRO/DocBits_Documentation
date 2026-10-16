---
description: Soporte de documentos electrónicos PINT A-NZ en DocBits
---

# 🇦🇺 PINT A-NZ

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Australia / Nueva Zelanda |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | UBL 2.1 XML |
| **Estándar** | PINT A-NZ (Modelo Peppol Internacional para Australia-Nueva Zelanda) |
| **Configuración regional** | `en_AU` |

PINT A-NZ (Modelo Peppol Internacional para Australia-Nueva Zelanda) es la especificación de facturación Peppol localizada para la región de Australia/Nueva Zelanda. Extiende el modelo PINT global con reglas de negocio específicas de A-NZ, categorías impositivas (GST) y esquemas de identificación (ABN, NZBN). Esta es la página de referencia técnica con la asignación de campos completa.

## Estado de soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="aunz-pint-preview.png" alt="Vista previa de factura PINT A-NZ en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura PINT A-NZ</p></figcaption></figure>

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

## Regla de clasificación

DocBits detecta documentos PINT A-NZ coincidiendo con el elemento `CustomizationID`:

```
urn:peppol.org:pint:billing-1@aunz
```

Para documentos de autofacturación, el patrón es:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Ambos se clasifican bajo el tipo de documento electrónico `PINT A-NZ`.

## Relacionado

- [AUNZ PINT](aunz-pint.md) — Resumen y características específicas de A-NZ
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Variante de autofacturación
- [Documentos electrónicos soportados](./)