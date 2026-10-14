# Archivo de Transformación y Mapeo

## 1. **Propósito**

Este archivo es responsable de extraer datos de un archivo XML Peppol BIS Billing 3.0, procesarlos y guardar la información relevante en un formato especificado. Está diseñado para permitir la extracción de campos clave para facilitar un procesamiento posterior o la integración en DocBits.

## 2. **Descripción general**

* **Archivo fuente**: La entrada es un archivo XML Peppol que sigue el estándar Peppol BIS Billing 3.0.
* **Proceso de extracción**: El archivo realiza una serie de pasos para leer, analizar y extraer elementos clave como detalles de la factura, información del proveedor, importes y fechas.
* **Salida**: Los datos extraídos se almacenan en un formato estructurado, en otro archivo XML.

## _**3.**_**&#x20;Descargar** **el Archivo de Transformación XML Peppol.**

* Ejemplo: _Este archivo contiene la lógica de transformación XML Peppol para extraer y guardar datos en otro archivo XML._
* Si tiene problemas con su archivo actual o se vuelve inutilizable, descargue esta versión de respaldo para restaurar la funcionalidad de transformación.

{% file src="../../../../../../.gitbook/assets/Transformation.xslt" %}

#### Aquí está el Mapeo:

<details>

<summary>Mapeo de Información de AccountingSupplierParty</summary>



* **Dirección Electrónica del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/EndpointID/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS>`
  * **Puede aparecer varias veces**: No.
* **ID del Esquema de la Dirección Electrónica del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/EndpointID/@schemeID`
  * **Mapeado a**: `<INVOICE><SUPPLIER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Puede aparecer varias veces**: No.
* **Identificación del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyIdentification/ID/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID>`
  * **Puede aparecer varias veces**: Se extraerá cada elemento `<PartyIdentification>` bajo `Supplier`.
* **ID del Esquema de Identificación del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapeado a**: `<INVOICE><SUPPLIER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Puede aparecer varias veces**: Cada elemento `<PartyIdentification>` tendrá su correspondiente ID de esquema.
* **Nombre del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/PartyName/Name/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><NAME>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Proveedor Línea 1**
  * **Fuente**:`//AccountingSupplierParty/Party/PostalAddress/StreetName/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><ADDRESS_LINE_1>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Proveedor Línea 2**
  * **Fuente**:`//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><ADDRESS_LINE_2>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Proveedor Línea 3**
  * **Fuente**:`//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapeado a**: `<InvoINVOICEice><SUPPLIER><ADDRESS_LINE_3>`
  * **Puede aparecer varias veces**: No.
* **ID de IVA del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><VAT_ID>`
  * **Puede aparecer varias veces**: No.
* **Esquema Fiscal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><TAX_SCHEME>`
  * **Puede aparecer varias veces**: No.
* **Nombre Legal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><LEGAL_NAME>`
  * **Puede aparecer varias veces**: No.
* **ID Legal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><LEGAL_ID>`
  * **Puede aparecer varias veces**: No.
* **ID del Esquema del ID Legal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapeado a**: `<INVOICE><SUPPLIER><LEGAL_ID_SCHEME_ID>`
  * **Puede aparecer varias veces**: No.
* **Forma Legal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><LEGAL_FORM>`
  * **Puede aparecer varias veces**: No.
* **Código Postal del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><POST_CODE>`
  * **Puede aparecer varias veces**: No.
* **Ciudad del Proveedor**
  * **Fuente**:`//AccountingSupplierParty/Party/PostalAddress/CityName/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><CITY>`
  * **Puede aparecer varias veces**: No.
* **Subentidad del País del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><COUNTRY_SUBENTITY>`
  * **Puede aparecer varias veces**: No.
* **Código de País del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><COUNTRY_CODE>`
  * **Puede aparecer varias veces**: No.
* **Nombre de Contacto del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/Contact/Name/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><CONTACT><NAME>`
  * **Puede aparecer varias veces**: No.
* **Teléfono de Contacto del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/Contact/Telephone/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><CONTACT><TELEPHONE>`
  * **Puede aparecer varias veces**: No.
* **Correo Electrónico de Contacto del Proveedor**
  * **Fuente**: `//AccountingSupplierParty/Party/Contact/ElectronicMail/text()`
  * **Mapeado a**: `<INVOICE><SUPPLIER><CONTACT><EMAIL>`
  * **Puede aparecer varias veces**: No.

</details>

<details>

<summary>Mapeo de Información de AccountingCustomerParty</summary>



* **Dirección Electrónica del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/EndpointID/text()`
  * **Mapeado a**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS>`
  * **Puede aparecer varias veces**: No.
* **ID del Esquema de la Dirección Electrónica del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/EndpointID/@schemeID`
  * **Mapeado a**: `<INVOICE><BUYER><ELECTRONIC_ADDRESS_SCHEME_ID>`
  * **Puede aparecer varias veces**: No.
* **Identificación del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/PartyIdentification/ID/text()`
  * **Mapeado a**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID>`
  * **Puede aparecer varias veces**: Se extraerá cada elemento `<PartyIdentification>` bajo `Buyer`.
* **ID del Esquema de Identificación del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyIdentification/ID/@schemeID`
  * **Mapeado a**: `<INVOICE><BUYER><PARTYIDENTIFICATION><ID_SCHEME_ID>`
  * **Puede aparecer varias veces**: Cada elemento `<PartyIdentification>` tendrá su correspondiente ID de esquema.
* **Nombre del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/PartyName/Name/text()`
  * **Mapeado a**: `<INVOICE><BUYER><NAME>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Comprador Línea 1**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/StreetName/text()`
  * **Mapeado a**: `<INVOICE><BUYER><ADDRESS_LINE_1>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Comprador Línea 2**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado a**: `<INVOICE><BUYER><ADDRESS_LINE_2>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Comprador Línea 3**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()`
  * **Mapeado a**: `<INVOICE><BUYER><ADDRESS_LINE_3>`
  * **Puede aparecer varias veces**: No.
* **ID de IVA del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()`
  * **Mapeado a**: `<INVOICE><BUYER><VAT_ID>`
  * **Puede aparecer varias veces**: No.
* **Esquema Fiscal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado a**: `<INVOICE><BUYER><TAX_SCHEME>`
  * **Puede aparecer varias veces**: No.
* **Nombre Legal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()`
  * **Mapeado a**: `<INVOICE><BUYER><LEGAL_NAME>`
  * **Puede aparecer varias veces**: No.
* **ID Legal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()`
  * **Mapeado a**: `<INVOICE><BUYER><LEGAL_ID>`
  * **Puede aparecer varias veces**: No.
* **ID del Esquema del ID Legal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID`
  * **Mapeado a**: `<INVOICE><BUYER><LEGAL_ID_SCHEME_ID>`
  * **Puede aparecer varias veces**: No.
* **Forma Legal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()`
  * **Mapeado a**: `<INVOICE><BUYER><LEGAL_FORM>`
  * **Puede aparecer varias veces**: No.
* **Código Postal del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()`
  * **Mapeado a**: `<INVOICE><BUYER><POST_CODE>`
  * **Puede aparecer varias veces**: No.
* **Ciudad del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/CityName/text()`
  * **Mapeado a**: `<INVOICE><BUYER><CITY>`
  * **Puede aparecer varias veces**: No.
* **Subentidad del País del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()`
  * **Mapeado a**: `<INVOICE><BUYER><COUNTRY_SUBENTITY>`
  * **Puede aparecer varias veces**: No.
* **Código de País del Comprador**
  * **Fuente**:`//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado a**: `<INVOICE><BUYER><COUNTRY_CODE>`
  * **Puede aparecer varias veces**: No.
* **Nombre de Contacto del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/Contact/Name/text()`
  * **Mapeado a**: `<INVOICE><BUYER><CONTACT><NAME>`
  * **Puede aparecer varias veces**: No.
* **Teléfono de Contacto del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/Contact/Telephone/text()`
  * **Mapeado a**: `<INVOICE><BUYER><CONTACT><TELEPHONE>`
  * **Puede aparecer varias veces**: No.
* **Correo Electrónico de Contacto del Comprador**
  * **Fuente**: `//AccountingCustomerParty/Party/Contact/ElectronicMail/text()`
  * **Mapeado a**: `<INVOICE><BUYER><CONTACT><EMAIL>`
  * **Puede aparecer varias veces**: No.

</details>

<details>

<summary>Mapeo de Información de PayeeParty</summary>



1. **Identificación del Beneficiario**
   * **Fuente**: `//PayeeParty/PartyIdentification/ID/text()`
   * **Mapeado a**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID>`
   * **Puede aparecer varias veces**: Se extraerá cada elemento `<PartyIdentification>` bajo `PayeeParty`.
2. **ID del Esquema de Identificación del Beneficiario**
   * **Fuente**: `//PayeeParty/PartyIdentification/ID/@schemeID`
   * **Mapeado a**: `<INVOICE><PAYEE><PARTYIDENTIFICATION><ID_SCHEME_ID>`
   * **Puede aparecer varias veces**: Cada elemento `<PartyIdentification>` tendrá su correspondiente ID de esquema.
3. **Nombre del Beneficiario**
   * **Fuente**: `//PayeeParty/PartyName/Name/text()`
   * **Mapeado a**: `<INVOICE><PAYEE><NAME>`
   * **Puede aparecer varias veces**: No.
4. **ID Legal del Beneficiario**
   * **Fuente**: `//PayeeParty/PartyLegalEntity/CompanyID/text()`
   * **Mapeado a**: `<INVOICE><PAYEE><LEGAL_ID>`
   * **Puede aparecer varias veces**: No.
5. **ID del Esquema del ID Legal del Beneficiario**
   * **Fuente**: `//PayeeParty/PartyLegalEntity/CompanyID/@schemeID`
   * **Mapeado a**: `<INVOICE><PAYEE><LEGAL_ID_SCHEME_ID>`
   * **Puede aparecer varias veces**: No.

</details>

<details>

<summary>Mapeo de Información de TaxRepresentativeParty</summary>



* **Nombre del Representante Fiscal**
  * **Fuente**: `//TaxRepresentativeParty/PartyName/Name/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><NAME>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Representante Fiscal Línea 1**
  * **Fuente**: `//TaxRepresentativeParty/PostalAddress/StreetName/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_1>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Representante Fiscal Línea 2**
  * **Fuente**:`//TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_2>`
  * **Puede aparecer varias veces**: No.
* **Dirección del Representante Fiscal Línea 3**
  * **Fuente**:`//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><ADDRESS_LINE_3>`
  * **Puede aparecer varias veces**: No.
* **ID de IVA del Representante Fiscal**
  * **Fuente**: `//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><VAT_ID>`
  * **Puede aparecer varias veces**: No.
* **Esquema Fiscal del Representante Fiscal**
  * **Fuente**:`//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><TAX_SCHEME>`
  * **Puede aparecer varias veces**: No.
* **Ciudad del Representante Fiscal**
  * **Fuente**: `//TaxRepresentativeParty/PostalAddress/CityName/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><CITY>`
  * **Puede aparecer varias veces**: No.
* **Código Postal del Representante Fiscal**
  * **Fuente**: `//TaxRepresentativeParty/PostalAddress/PostalZone/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><POST_CODE>`
  * **Puede aparecer varias veces**: No.
* **Subentidad del País del Representante Fiscal**
  * **Fuente**:`//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_SUBENTITY>`
  * **Puede aparecer varias veces**: No.
* **Código de País del Representante Fiscal**
  * **Fuente**:`//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()`
  * **Mapeado a**: `<INVOICE><TAX_REPRESENTATIVE_PARTY><COUNTRY_CODE>`
  * **Puede aparecer varias veces**: No.

</details>

<details>

<summary>Información General de la Factura</summary>



1. **Tipo de Factura**
   * **Fuente**: `"Invoice"`
   * **Mapeado a**: `<INVOICE><INVOICE_TYPE>`
   * **Puede aparecer varias veces**: No.
2. **Subtipo de Factura**
   * **Fuente**: `"Purchase Invoice"`
   * **Mapeado a**: `<INVOICE><INVOICE_SUB_TYPE>`
   * **Puede aparecer varias veces**: No.
3. **ID de Factura**
   * **Fuente**: `//ID/text()`
   * **Mapeado a**: `<INVOICE><INVOICE_ID>`
   * **Puede aparecer varias veces**: No.
4. **Código de Tipo de Factura**
   * **Fuente**: `//InvoiceTypeCode/text()`
   * **Mapeado a**: `<INVOICE><INVOICE_TYPE_CODE>`
   * **Puede aparecer varias veces**: No.
5. **Fecha de Factura**
   * **Fuente**: `normalize-space(//IssueDate/text())`
   * **Mapeado a**: `<INVOICE><INVOICE_DATE>`
   * **Puede aparecer varias veces**: No.
   * **Procesamiento**: Utiliza la plantilla `DateTimeString` para el formato.
6. **Fecha de Vencimiento**
   * **Fuente**: `normalize-space(//DueDate/text())`
   * **Mapeado a**: `<INVOICE><DUE_DATE>`
   * **Puede aparecer varias veces**: No.
   * **Procesamiento**: Utiliza la plantilla `DateTimeString` para el formato.
7. **Fecha de Punto Fiscal**
   * **Fuente**: `normalize-space(//TaxPointDate/text())`
   * **Mapeado a**: `<INVOICE><TAX_POINT_DATE>`
   * **Puede aparecer varias veces**: No.
   * **Procesamiento**: Utiliza la plantilla `DateTimeString` para el formato.
8. **Nota de Factura**
   * **Fuente**: `//Note/text()`
   * **Mapeado a**: `<INVOICE><INVOICE_NOTE>`
   * **Puede aparecer varias veces**: No.
9. **Código de Moneda del Documento**
   * **Fuente**: `//DocumentCurrencyCode/text()`
   * **Mapeado a**: `<INVOICE><DOCUMENT_CURRENCY_CODE>`
   * **Puede aparecer varias veces**: No.
10. **Código de Moneda Fiscal**
    * **Fuente**: `//TaxCurrencyCode/text()`
    * **Mapeado a**: `<INVOICE><TAX_CURRENCY_CODE>`
    * **Puede aparecer varias veces**: No.
11. **Costo Contable**
    * **Fuente**: `//AccountingCost/text()`
    * **Mapeado a**: `<INVOICE><ACCOUNTING_COST>`
    * **Puede aparecer varias veces**: No.
12. **Fecha de Inicio del Periodo de Facturación**
    * **Fuente**: `normalize-space(//InvoicePeriod/StartDate/text())`
    * **Mapeado a**: `<INVOICE><INVOCICE_PERIOD><START_DATE>`
    * **Puede aparecer varias veces**: No.
    * **Procesamiento**: Utiliza la plantilla `DateTimeString` para el formato.
13. **Fecha de Fin del Periodo de Facturación**
    * **Fuente**: `normalize-space(//InvoicePeriod/EndDate/text())`
    * **Mapeado a**: `<INVOICE><INVOCICE_PERIOD><END_DATE>`
    * **Puede aparecer several times**: No.
    * **Procesamiento**: Utiliza la plantilla `DateTimeString` para el formato.
14. **Código de Descripción del Periodo de Facturación**
    * **Fuente**: `//InvoicePeriod/DescriptionCode/text()`
    * **Mapeado a**: `<INVOICE><INVOCICE_PERIOD><DESCRIPTION_CODE>`
    * **Puede aparecer varias veces**: No.
15. **Referencia de Orden de Compra**
    * **Fuente**: `//OrderReference/ID/text()`
    * **Mapeado a**: `<INVOICE><PURCHASE_ORDER>`
    * **Puede aparecer varias veces**: No.
16. **Referencia de Orden de Venta**
    * **Fuente**: `//OrderReference/SalesOrderID/text()`
    * **Mapeado a**: `<INVOICE><SALES_ORDER>`
    * **Puede aparecer varias veces**: No.

</details>

<details>

<summary>Mapeo de Referencias de Documentos y Detalles Adicionales de Documentos</summary>

1. **Referencia del Comprador**
   * **Fuente**: `//BuyerReference/text()`
   * **Mapeado a**: `<INVOICE><BUYER_REFERENCE>`
   * **Puede aparecer varias veces**: No.

2)  **Referencia de Facturación**

    * **Fuente**: `//BillingReference`
    * **Mapeado a**: `<INVOICE><BILLING_REFERENCE>`
    * **Puede aparecer varias veces**: Sí. Cada elemento `<BillingReference>` en los datos de origen generará un elemento `<BILLING_REFERENCE>`.

    **Para cada Referencia de Facturación:**

    * **NÚMERO_DE_FACTURA_PRECEDENTE**
      * **Fuente**: `InvoiceDocumentReference/ID/text()`
      * **Mapeado a**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOCIE_NUMBER>`
      * **Puede aparecer varias veces**: No.
    * **FECHA_DE_EMISIÓN_DE_FACTURA_PRECEDENTE**
      * **Fuente**: `InvoiceDocumentReference/IssueDate/text()`
      * **Mapeado a**: `<INVOICE><BILLING_REFERENCE><PRECEDING_INVOICE_ISSUE_DATE>`
      * **Puede aparecer varias veces**: No.

3. **Referencia de Documento de Despacho**
   * **Fuente**: `//DespatchDocumentReference/ID/text()`
   * **Mapeado a**: `<INVOICE><DESPATCH_DOCUMENT_REFERENCE>`
   * **Puede aparecer varias veces**: No.

4) **Referencia de Documento de Recibo**
   * **Fuente**: `//ReceiptDocumentReference/ID/text()`
   * **Mapeado a**: `<INVOICE><RECEIPT_DOCUMENT_REFERENCE>`
   * **Puede aparecer varias veces**: No.

5. **Referencia de Documento del Originador**
   1. **Fuente**: `//OriginatorDocumentReference/ID/text()`
   2. **Mapeado a**: `<INVOICE><ORIGINATOR_DOCUMENT_REFERENCE>`
   3. **Puede aparecer varias veces**: No.

#### Referencia de Documento de Contrato

* **Fuente**: `//ContractDocumentReference/ID/text()`
* **Mapeado a**: `<INVOICE><CONTRACT_DOCUMENT_REFERENCE>`
* **Puede aparecer varias veces**: No.

#### Referencia de Proyecto

* **Fuente**: `//ProjectReference/ID/text()`
* **Mapeado a**: `<INVOICE><PROJECT_REFERENCE>`
* **Puede aparecer varias veces**: No.

#### Referencia de Documento Adicional

* **Fuente**: `//AdditionalDocumentReference`
* **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE>`
* **Puede aparecer varias veces**: Sí. Cada elemento `<AdditionalDocumentReference>` en los datos de origen generará un elemento `<ADDITIONAL_DOCUMENT_REFERENCE>`.

**Para cada Referencia de Documento Adicional:**

* **ID**
  * **Fuente**: `ID/text()`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ID>`
  * **Puede aparecer varias veces**: No.
* **SCHEME\_ID**
  * **Fuente**: `ID/@schemeID`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><SCHEME_ID>`
  * **Puede aparecer varias veces**: No.
* **CÓDIGO\_DE\_TIPO\_DE\_DOCUMENTO**
  * **Fuente**: `DocumentTypeCode/text()`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_TYPE_CODE>`
  * **Puede aparecer varias veces**: No.
* **DESCRIPCIÓN\_DEL\_DOCUMENTO**
  * **Fuente**: `DocumentDescription/text()`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><DOCUMENT_DESCRIPTION>`
  * **Puede aparecer varias veces**: No.

**Información de Adjuntos (para cada Referencia de Documento Adicional):**

* **EMBEDDED\_DOCUMENT\_BINARY\_OBJECT**
  * **Fuente**: `Attachment/EmbeddedDocumentBinaryObject/text()`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EMBEDDED_DOCUMENT_BINARY_OBJECT>`
  * **Puede aparecer varias veces**: No.
* **CÓDIGO\_MIME**
  * **Fuente**: `Attachment/EmbeddedDocumentBinaryObject/@mimeCode`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><MIME_CODE>`
  * **Puede aparecer varias veces**: No.
* **NOMBRE\_DE\_ARCHIVO**
  * **Fuente**: `Attachment/EmbeddedDocumentBinaryObject/@filename`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><FILENAME>`
  * **Puede aparecer varias veces**: No.
* **URL\_DE\_REFERENCIA\_EXTERNA**
  * **Fuente**: `Attachment/ExternalReference/URI/text()`
  * **Mapeado a**: `<INVOICE><ADDITIONAL_DOCUMENT_REFERENCE><ATTACHMENT><EXTERNAL_REFERENCE_URL>`
  * **Puede aparecer varias veces**: No.

</details>
