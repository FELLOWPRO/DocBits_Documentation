# Peppol BIS Billing 3.0

### Descripción general

Esta sección describe el plan de implementación para importar y mapear datos de archivos XML utilizando el esquema Peppol BIS Billing 3.0. Peppol BIS Billing 3.0 se desarrolló para estandarizar los procesos de facturación electrónica y garantizar el cumplimiento de los estándares europeos.

### Objetivos

* Garantizar el cumplimiento total de las especificaciones de Peppol BIS Billing 3.0.
* Integración perfecta de los datos de facturación electrónica en nuestro sistema de cuentas por pagar utilizando DocBits.
* Mejorar la calidad de los datos y la eficiencia del procesamiento.

### Alcance

El alcance de este proyecto es mapear elementos clave del esquema Peppol BIS Billing 3.0 a nuestras estructuras de datos internas. En particular, el mapeo cubrirá las siguientes áreas:

* Detalles del vendedor y del comprador
* Detalles de la factura
* Líneas de factura
* Instrucciones de pago
* Información fiscal y legal

### Elementos clave y mapeo

**Información del vendedor:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Dirección electrónica del vendedor
  * cbc:Name: Nombre comercial del vendedor
  * cbc:CompanyID: Número de registro legal del vendedor
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Detalles de la dirección del vendedor

**Información del comprador:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Dirección electrónica del comprador
  * cbc:Name: Nombre comercial del comprador
  * cbc:CompanyID: Número de registro legal del comprador
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Detalles de la dirección del comprador

**Detalles de la factura:**

* cbc:ID: Número de factura
* cbc:IssueDate: Fecha de emisión de la factura
* cbc:DueDate: Fecha de vencimiento de la factura
* cbc:InvoiceTypeCode: Tipo de factura

**Líneas de factura:**

* cac:InvoiceLine
  * cbc:ID: Número de línea de factura
  * cbc:InvoicedQuantity: Cantidad facturada
  * cbc:LineExtensionAmount: Importe de extensión de línea
  * cbc:Description: Descripción de la posición de facturación
  * cac:Item
    * cbc:Name: Nombre del artículo
    * cbc:SellerItemIdentification/cbc:ID: Número de artículo del vendedor
  * cac:Price
    * cbc:PriceAmount: Precio por unidad
    * cbc:BaseQuantity: Cantidad base para el precio

**Instrucciones de pago:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Código para identificar el método de pago
  * cbc:PaymentID: Identificador de pago

**Información fiscal:**

* cac:TaxTotal
  * cbc:TaxAmount: Importe total de impuestos
  * cac:TaxSubtotal: Detalles para cada importe de impuesto provisional

### Vista previa en PDF para factura electrónica

Se genera un documento PDF de acuerdo con un diseño estándar con los campos importados para proporcionar al usuario una vista previa para fines de referencia. Es posible realizar una mayor personalización del diseño de la vista previa en PDF, pero requiere un esfuerzo adicional.
