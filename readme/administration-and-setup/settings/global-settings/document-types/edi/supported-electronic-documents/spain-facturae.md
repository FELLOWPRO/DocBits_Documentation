---
description: España Facturae (3.2, 3.2.1, 3.2.2) – Compatibilidad con documentos electrónicos en DocBits
---

# 🇪🇸 España Facturae

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | España |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | XML |
| **Estándar** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Configuración regional** | `es_ES` |

Facturae es el estándar español obligatorio de facturación electrónica, gestionado por la Agencia Estatal de Administración Tributaria (AEAT) y el Ministerio de Hacienda. Es obligatorio para facturas dirigidas a entidades del sector público español y ampliamente utilizado en transacciones B2B. El elemento raíz es `<fe:Facturae>` con una URL de espacio de nombres versionada. DocBits detecta la versión mediante el atributo `xsi:schemaLocation`, que hace referencia a una de las URL de esquema oficiales:

| Versión | URL del esquema |
|---------|----------------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Estado de compatibilidad

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="spain-facturae-preview.png" alt="Vista previa de factura España Facturae en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura España Facturae 3.2.2</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Número de factura |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Fecha de emisión (AAAA-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Fecha de vencimiento del pago |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Factura, NC=Nota de crédito |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Siempre `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Referencia de pedido / contrato del comprador |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Importe neto sin IVA |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Importe total de IVA |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Importe total con IVA |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Tipo de IVA en % (estándar 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Código del medio de pago |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Nombre del proveedor |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (p. ej. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF o CIF español |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Dirección del proveedor |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Ciudad del proveedor |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Código postal del proveedor |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | Código de país ISO (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Nombre del comprador |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF del comprador |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Dirección del comprador |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Ciudad del comprador |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Código postal del comprador |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | Código de país ISO (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN del beneficiario |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `Invoices/Invoice/Items/InvoiceLine`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `ItemDescription` | Secuencia / descripción usada como identificador |
| `DESCRIPTION` | `ItemDescription` | Descripción del artículo |
| `QUANTITY` | `Quantity` | Cantidad facturada |
| `UNIT` | `UnitOfMeasure` | Unidad de medida (p. ej. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Precio unitario sin IVA |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Tipo de IVA en % (normalmente 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Importe de IVA por línea |
| `NET_AMOUNT` | `TotalCost` | Total de línea sin IVA |

## Reglas de clasificación

DocBits detecta los documentos Facturae mediante la coincidencia del atributo `xsi:schemaLocation` en el elemento raíz `<fe:Facturae>`:

| Tipo de documento electrónico | Patrón |
|------------------------------|--------|
| FACTURAE 3.2 | `xsi:schemaLocation` contiene `Facturaev3_2.xml` (no 3_2_1 ni 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` contiene `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` contiene `Facturaev3_2_2.xml` |

El elemento raíz es `<fe:Facturae>` con espacio de nombres `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (específico de versión). La clasificación usa el principio **primer coincidente gana**, con los patrones más específicos (3.2.2, 3.2.1) evaluados antes del genérico 3.2.

## Relacionados

- [Estándares de e-factura actualmente compatibles](../../currently-supported-e-invoice-standards/)
- [Documentos electrónicos compatibles](./)
