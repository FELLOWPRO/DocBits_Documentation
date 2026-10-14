# Erstellen einer IDM-Mapping-Datei

## Erforderliche Felder für die IDM-Mapping-Datei

Beim Erstellen einer IDM-Mapping-Datei sind die folgenden Felder erforderlich:

* **Dokumenttypdefinition**
  * Stellen Sie sicher, dass der Dokumenttypcode in DocBits mit dem Namen übereinstimmt, der in der URL der Feldeinstellungen verwendet wird, ähnlich wie in der BOD-Mapping-Datei.
  * Überprüfen Sie, ob der Dokumenttypname in IDM mit Ihrer Systemkonfiguration übereinstimmt. Zum Beispiel kann es in M3 **M3\_SupplierInvoice** sein, während es in LN je nach Ihrer Einrichtung anders sein wird.
    * Eine Anleitung, wie man in IDM navigiert, finden Sie im Dokumentenmanager in IDM auf dieser Seite.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

* **Statische Werte**
  *   Definieren Sie zunächst alle statischen Werte in einer einzigen Zeile mit dem Schlüssel **Static\_Values**:

      <pre class="language-properties"><code class="lang-properties"><strong>Static_Values=FileNameSeparator,ACLString
      </strong></code></pre>
  *   Weisen Sie dann jedem statischen Variablen Werte mit dem Präfix **SV\_** zu:

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

* **ACL-Felddefinition**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Suchbarer Name in IDM**
  * Der **Suchbare PDF-Name** wird der Dokumentname in IDM sein.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID
```

## Feldzuordnung

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

*   Beginnen Sie damit, alle verwendeten Indexfelder aufzulisten und die Feld-ID und den Typ anzugeben.

    ```properties
    Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
    ```
*   Jedes zugeordnete Feld folgt dem Format:

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Bestätigen Sie, dass **IndexFieldFromDocBits = IDMAttributeID**, um sicherzustellen, dass die Feldzuordnung in DocBits mit den Attributen in IDM (Dokumenttyp → Attribute) übereinstimmt. Eine Anleitung, wie man in IDM navigiert, finden Sie im Dokumentenmanager in IDM auf dieser Seite.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FzT9MMKlFCSBJtRW1pf4s%2Fimage.png?alt=media\&token=ea2f6ae2-f9f2-48d3-98e3-ed06dcda69f1)

### XML- und EDI-Dateiexport

Um die originale XML/EDI-Datei zusammen mit der generierten PDF zu exportieren, müssen Sie die IDM-Mapping-Datei in der Exportkonfiguration ändern. Aktualisieren Sie zunächst den Abschnitt **Static\_Values**, indem Sie das Dateipräfix und die Erweiterung hinzufügen. Danach definieren Sie das tatsächliche Mapping, um die korrekte Exportkonfiguration sicherzustellen.

Wenn bereits ein Export für Rechnungen an IDM eingerichtet ist, sollte die generierte PDF bereits im Export enthalten sein. Wenn Sie die XML-Datei nicht benötigen, können Sie den nächsten Teil überspringen. Wenn Sie jedoch die XML-Datei benötigen, folgen Sie den folgenden Schritten.

#### Aktualisieren der statischen Werte:

Suchen Sie das Feld **Static\_Values** und fügen Sie Folgendes hinzu:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Fügen Sie dann die folgenden Einträge unter **SV\_ACLString** hinzu:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Fügen Sie danach das tatsächliche Mapping hinzu und stellen Sie sicher, dass der Export-Dokumenttyp dem IDM-Dokumenttype entspricht.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### XML-Mapping

Fügen Sie das folgende Mapping am Ende der Datei hinzu:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Hinweis: Stellen Sie sicher, dass **export\_doc\_type** auf den IDM-Rechnungstyp eingestellt ist. In diesem Beispiel ist es auf **M3** eingestellt.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### EDI-Mapping

Fügen Sie das folgende Mapping am Ende der Datei hinzu:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Hinweis: Stellen Sie sicher, dass **export\_doc\_type** auf den IDM-Rechnungstyp eingestellt ist. In diesem Beispiel ist es auf **M3** eingestellt.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Dokumentenmanager in Infor

Gehen Sie zum Dokumentenmanager und wählen Sie den Namen des aktuellen Dokumenttyps aus, den Sie exportieren möchten, z. B. Lieferantenrechnung.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Klicken Sie auf das obige Symbol und dann auf Verwaltung → Dokumenttyp und suchen Sie den Dokumenttyp, den Sie in der Liste benötigen.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Wie unten gezeigt, sehen Sie dann den Dokumenttypnamen, wie er in INFOR ist.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Stellen Sie sicher, dass dies so im IDM-Mapping-Datei angezeigt wird.

### Datei in DocBits hochladen

Sobald die Datei vorbereitet ist, laden Sie sie in Ihre Exportkonfiguration in DocBits hoch. Dies ist unter Einstellungen → Export verfügbar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
