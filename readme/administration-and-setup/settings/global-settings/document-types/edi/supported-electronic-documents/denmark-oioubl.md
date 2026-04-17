---
description: Soporte de documentos electrónicos Denmark OIOUBL 2.1 en DocBits
---

# 🇩🇰 Denmark OIOUBL 2.1

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Denmark |
| **Tipos de documento** | Invoice (Faktura), Credit Note |
| **Formato** | XML (UBL 2.1) |
| **Estándar** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Configuración regional** | `da_DK` |

OIOUBL (Offentlig Information Online UBL) es el estándar danés de facturación electrónica basado en UBL 2.1. Es obligatorio para facturas dirigidas a entidades del sector público danés y se utiliza ampliamente en transacciones B2B. DocBits detecta documentos OIOUBL 2.1 por la presencia de `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. El identificador de perfil `urn:www.nesubl.eu:profiles:profile5:ver2.0` indica el perfil de factura NES (Northern European Subset).

## Estado de soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="denmark-oioubl-preview.png" alt="Denmark OIOUBL 2.1 invoice preview in DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura Denmark OIOUBL 2.1 (Faktura)</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `cbc:ID` | Número de factura |
| `invoice_date` | `cbc:IssueDate` | Fecha de emisión ISO 8601 |
| `due_date` | `cbc:DueDate` | Fecha de vencimiento del pago |
| `invoice_type` | `cbc:InvoiceTypeCode` | Código UNCL 1001 (380=Factura, 381=Nota de crédito) |
| `currency` | `cbc:DocumentCurrencyCode` | Siempre `DKK` (Corona danesa) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Número de referencia del pedido del comprador |
| `buyer_reference` | `cbc:BuyerReference` | Referencia interna del comprador / número de ubicación EAN |
| `note` | `cbc:Note` | Instrucciones de pago o notas en texto libre |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Importe neto sin IVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Importe total de IVA (tipo estándar del 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Importe total con IVA |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Tipo de IVA en % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nombre de la empresa proveedora |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | Número CVR (p. ej. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Número de IVA/CVR |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Dirección del proveedor |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Ciudad del proveedor |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Código postal del proveedor |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | Código de país ISO (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nombre de la empresa cliente |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | Número CVR |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Número de IVA/CVR |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Dirección del cliente |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Ciudad del cliente |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Código postal del cliente |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | Código de país ISO (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Cuenta bancaria / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | Código BIC/SWIFT |

### Tabla de líneas de artículo (`INVOICE_TABLE`)

Ruta de fila: `cac:InvoiceLine`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `cbc:ID` | Número de secuencia de línea |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Nombre / descripción del artículo |
| `QUANTITY` | `cbc:InvoicedQuantity` | Cantidad facturada |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Precio unitario sin IVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de línea sin IVA |

## Regla de clasificación

DocBits detecta documentos OIOUBL 2.1 comparando el elemento `CustomizationID`:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

El elemento raíz es `<Invoice>` (o `<CreditNote>`) en el espacio de nombres UBL 2.1 `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Relacionado

- [Estándares de e-factura actualmente soportados](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos soportados](./)
