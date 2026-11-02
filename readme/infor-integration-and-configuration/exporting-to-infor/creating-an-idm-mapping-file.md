# Creación de un archivo de mapeo IDM

## Campos del archivo de mapeo IDM

Al crear un archivo de mapeo IDM, se requieren los siguientes campos:

* **Definición del tipo de documento**
  * Asegúrese de que el código del tipo de documento en DocBits coincida con el nombre utilizado en la URL de la configuración de campos, igual que en el archivo de mapeo BOD.
  * Verifique que el nombre del tipo de documento en IDM se corresponda con la configuración de su sistema. Por ejemplo, en M3 puede ser **M3_SupplierInvoice**, mientras que en LN será distinto según su configuración.
    * Encontrará una guía sobre cómo navegar en IDM en Document Manager en IDM, en esta misma página.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Valores estáticos**

    * Primero, defina todos los valores estáticos en una sola línea con la clave **Static_Values**:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Después, asigne valores a cada variable estática con el prefijo **SV_**:

    ```properties
    SV_FileNameSeparator=_ 
    SV_ACLString=Public
    ```

```properties
#Define mappings for the static values
#Example: Static_Values=<StaticVariableName>
Static_Values=FileNameSeparator,ACLString
#Example: SF_<StaticVariableName> = StaticValue
SV_FileNameSeparator=_
SV_ACLString=Public
```

* **Campos estáticos**
  * Los campos estáticos sirven para establecer valores concretos e inmutables en todos los documentos. Estos valores se mantienen iguales en todos los documentos.
  *   Comience enumerando todos los campos **Static** utilizados, indicando el **IDMAttributeId** y el tipo.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Después, asigne valores estáticos a cada campo con el prefijo `SF_`:

      ```properties
      SF_BOD_AccountingEntityID=921_VVB
      SF_M3_Company=921
      SF_M3_Division=VVB
      ```

```properties
#Define mappings for the static fields
#Example: Static_Fields=<IDMAttributeId>:<type>
Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
#Example: SF_<IDMAttributeId> = StaticValue
#SF_MDS_EntityType=InforERPEnterpriseFinancialsReceivedInvoice
SF_BOD_AccountingEntityID=921_VVB
SF_M3_Company=921
SF_M3_Division=VVB
```

* **Campos de índice**
  *   Comience enumerando todos los campos de índice utilizados, indicando el **IDMAttributeId** y el tipo.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Cada campo mapeado sigue el formato:

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Confirme que **IndexFieldFromDocBits = IDMAttributeID**, de modo que el mapeo de campos en DocBits se corresponda con los atributos en IDM (Document Type → Attributes).\        Encontrará una guía sobre cómo navegar en IDM en Document Manager en IDM, en esta misma página.

```properties
#Define index fields
#Example: Index_Fields=<IndexFieldIdFromIDM>:<type>
Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
#Example: IF_<DocBitsFieldID> = <IDMAttributeId>
IF_INVOICE_ID=BOD_SupplierInvoiceID
IF_CORRELATION_ID=BOD_AlternateDocumentID_1
IF_INVOICE_DATE=M3_InvoiceDate
IF_COMPANY=M3_Company
IF_DIVISION=M3_Division
IF_DIVISION_NO=BOD_AccountingEntityID
IF_SUPPLIER_ID=BOD_RemitToPartyID
IF_SUPPLIER_NAME=BOD_SupplierPartyID
```

* **Definición del campo ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nombre con capacidad de búsqueda en IDM**
  * El **Searchable PDF Name** será el nombre del documento en IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="Ejemplo de archivo de mapeo IDM"><figcaption></figcaption></figure>

## Exportación de archivos XML y EDI

Para exportar el archivo XML/EDI original junto con el PDF generado, debe modificar el archivo de mapeo IDM en la configuración de exportación. Primero, actualice la sección **Static_Values** añadiendo el prefijo y la extensión del archivo. Después, defina el mapeo real para garantizar la configuración de exportación correcta.

Si ya hay una exportación de facturas a IDM configurada, el PDF generado ya debería estar incluido en la exportación. Si no necesita el archivo XML, puede omitir la siguiente parte. Sin embargo, si sí lo necesita, siga los pasos que se indican a continuación.

### Actualización de los valores estáticos:

Busque el campo **Static_Values** y añada lo siguiente:a

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Después, añada las siguientes entradas debajo de **SV_ACLString**:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Ejemplo de configuración de valores estáticos"><figcaption></figcaption></figure>

### Mapeo XML

Añada el siguiente mapeo al final del archivo:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Nota: asegúrese de que **export_doc_type** esté configurado con el tipo de factura de IDM. En este ejemplo está configurado para **M3**.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="Ejemplo de mapeo XML"><figcaption></figcaption></figure>

### Mapeo EDI

Añada el siguiente mapeo al final del archivo:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Nota: asegúrese de que **export_doc_type** esté configurado con el tipo de factura de IDM. En este ejemplo está configurado para **M3**.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="Ejemplo de mapeo EDI"><figcaption></figcaption></figure>

### Document Manager en Infor

Vaya a Document Manager y seleccione el nombre del tipo de documento que está intentando exportar, por ejemplo, Supplier Invoice.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Haga clic en el icono anterior y, después, en Administration → Document Type, y busque en la lista el tipo de documento que necesita

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Como se muestra a continuación, verá el nombre del tipo de documento tal como figura en INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Asegúrese de que el nombre aparezca exactamente así en el archivo de mapeo IDM

## Cargar el archivo en DocBits

Una vez preparado el archivo, cárguelo en su configuración de exportación en DocBits. Está disponible en Settings → Export.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
