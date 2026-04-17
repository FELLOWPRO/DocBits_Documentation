---
description: Compatibilidad con documentos electrónicos Finvoice de Finlandia (1.3, 2.0, 2.01, 3.0) en DocBits
---

# 🇫🇮 Finlandia Finvoice

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Finlandia |
| **Tipos de documento** | Factura (Lasku), Nota de crédito (Hyvityslasku) |
| **Formato** | XML |
| **Estándar** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Configuración regional** | `fi_FI` |

Finvoice es el estándar de facturación electrónica del sector bancario finlandés, desarrollado y mantenido por Finance Finland (Finanssiala ry). Se utiliza tanto para la facturación B2B como B2G y se transmite a través de la infraestructura bancaria finlandesa. El elemento raíz es `<Finvoice>` con una URL de espacio de nombres versionada. DocBits detecta la versión mediante el atributo `xmlns`:

| Versión | URL del espacio de nombres |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

El formato del ID empresarial finlandés (Y-tunnus) es `1234567-8` (7 dígitos + dígito de control), utilizado como identificador de parte. El número de IVA tiene el prefijo `FI` seguido de 8 dígitos (ej. `FI12345678`). Las fechas se codifican en formato `CCYYMMDD`.

## Estado de compatibilidad

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="finland-finvoice-preview.png" alt="Vista previa de factura Finvoice 3.0 de Finlandia en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura Finvoice 3.0 de Finlandia (Lasku)</p></figcaption></figure>

## Mapeo de campos

### Campos de encabezado

| Campo DocBits | Elemento XML fuente | Notas |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Número de factura |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Fecha en formato `CCYYMMDD`, convertida a ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Fecha de vencimiento del pago (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Factura, CRE01=Nota de crédito |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Código de divisa (típicamente `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Importe neto sin IVA |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Importe total de IVA |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Importe total con IVA |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Tipo de IVA en % (estándar 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Nombre de la empresa proveedora |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | ID empresarial finlandés (Y-tunnus, ej. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Número de IVA (ej. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Dirección del proveedor |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Ciudad del proveedor |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Código postal del proveedor |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | Código de país ISO (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Nombre de la empresa compradora |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | ID empresarial finlandés (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Dirección del comprador |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Ciudad del comprador |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Código postal del comprador |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | Código de país ISO (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN del beneficiario (detalles de pago EPI) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | Código BIC/SWIFT |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Condiciones de pago en texto libre |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `InvoiceRow`

| Columna | Elemento XML fuente | Notas |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Código de artículo / producto |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Nombre / descripción del artículo |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Cantidad entregada |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Código de unidad (ej. `KPL` = pieza) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Precio unitario sin IVA |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Tipo de IVA en % por línea |
| `VAT` | `InvoiceRow/RowVatAmount` | Importe de IVA por línea |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Total de línea sin IVA |

## Reglas de clasificación

DocBits detecta los documentos Finvoice haciendo coincidir el atributo `xmlns` en el elemento raíz `<Finvoice>`:

| Tipo de documento electrónico | Patrón |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice20` (no 2.01) |
| FINVOICE 2.01 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` contiene `http://www.finvoice.fi/schema/finvoice30` |

La clasificación utiliza el principio de **primera coincidencia gana**, con patrones más específicos (2.01) evaluados antes que el genérico 2.0.

## Relacionados

- [Estándares de facturación electrónica actualmente compatibles](../../currently-supported-e-invoice-standards/)
- [Finlandia TEAPPSXML](./finland-teappsxml.md)
- [Documentos electrónicos compatibles](./)
