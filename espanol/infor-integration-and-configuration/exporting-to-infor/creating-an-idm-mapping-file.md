# Creando un Archivo de Mapeo IDM

## Campos Requeridos para el Archivo de Mapeo IDM

Al crear un archivo de mapeo IDM, se requieren los siguientes campos:

* **Definición del Tipo de Documento**
  * Asegúrese de que el código del tipo de documento en DocBits coincida con el nombre utilizado en la URL de la configuración del campo, similar al Archivo de Mapeo BOD.
  * Verifique que el nombre del tipo de documento en IDM esté alineado con la configuración de su sistema. Por ejemplo, en M3, puede ser **M3\_SupplierInvoice**, mientras que en LN, será diferente según su configuración.
    * Una guía sobre cómo navegar en IDM se puede encontrar en el Administrador de Documentos en IDM en esta página.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

* **Valores Estáticos**
  *   Primero, defina todos los valores estáticos en una sola línea utilizando la clave **Static\_Values**:

      ```properties
      Static_Values=FileNameSeparator,ACLString
      ```
  *   Luego, asigne valores a cada variable estática utilizando el prefijo **SV\_**:

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

* **Definición del Campo ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nombre Buscable en IDM**
  * El **Nombre PDF Buscable** será el nombre del documento en IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID
```

## Mapeo de Campos

*   Comience enumerando todos los campos de índice utilizados, especificando el ID y el tipo de campo.

    ```properties
    Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
    ```
*   Cada campo mapeado sigue el formato:

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Confirme que **IndexFieldFromDocBits = IDMAttributeID**, asegurándose de que el mapeo de campos en DocBits esté alineado con los atributos en IDM (Tipo de Documento → Atributos). Una guía sobre cómo navegar en IDM se puede encontrar en el Administrador de Documentos en IDM en esta página.

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

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FzT9MMKlFCSBJtRW1pf4s%2Fimage.png?alt=media\&token=ea2f6ae2-f9f2-48d3-98e3-ed06dcda69f1)

### Exportación de archivos XML y EDI

Para exportar el archivo XML/EDI original junto con el PDF generado, necesitas modificar el archivo de Mapeo IDM, en la configuración de exportación. Primero, actualiza la sección **Static\_Values** agregando el prefijo y la extensión del archivo. Después de eso, define el mapeo real para asegurar la correcta configuración de exportación.

Si ya está configurada una exportación para facturas a IDM, el PDF generado ya debería estar incluido en la exportación. Si no necesitas el archivo XML, puedes omitir la siguiente parte. Sin embargo, si necesitas el archivo XML, sigue los pasos a continuación.

#### Actualizando los Valores Estáticos:

Encuentra el campo **Static\_Values** y agrega lo siguiente:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Luego, agrega las siguientes entradas debajo de **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Después de eso, agrega el mapeo real, asegurándote de que el tipo de documento de exportación corresponda al tipo de proveedor IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mapeo XML

Agrega el siguiente mapeo al final del archivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Nota: Asegúrate de que **export\_doc\_type** esté configurado al tipo de factura IDM. En este ejemplo, está configurado para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mapeo EDI

Agrega el siguiente mapeo al final del archivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Nota: Asegúrate de que **export\_doc\_type** esté configurado al tipo de factura IDM. En este ejemplo, está configurado para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Gestor de Documentos en Infor

Ve al Gestor de Documentos y selecciona el nombre del tipo de documento actual que estás tratando de exportar, por ejemplo, Factura de Proveedor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Haz clic en el ícono de arriba y luego haz clic en Administración → Tipo de Documento y luego encuentra el tipo de documento que necesitas en la lista.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Como se muestra a continuación, verás el nombre del tipo de documento tal como está en INFOR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Asegúrate de que este sea el nombre que se muestra en el Archivo de Mapeo IDM.

### Subir Archivo a DocBits

Una vez que el archivo esté preparado, súbelo a tu configuración de exportación en DocBits. Esto está disponible en Configuración → Exportar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
