# Erstellen einer IDM-Mapping-Datei

## Felder für die IDM-Mapping-Datei

Beim Erstellen einer IDM-Mapping-Datei sind die folgenden Felder erforderlich:

* **Document Type Definition**
  * Stellen Sie sicher, dass der Dokumenttyp-Code in DocBits mit dem in der URL der Feldeinstellungen verwendeten Namen übereinstimmt, ähnlich wie bei der BOD-Mapping-Datei.
  * Überprüfen Sie, ob der Dokumenttypname in IDM mit Ihrer Systemkonfiguration übereinstimmt. In M3 könnte er beispielsweise **M3_SupplierInvoice** lauten, während er in LN je nach Ihrer Einrichtung anders ausfällt.
    * Eine Anleitung zur Navigation in IDM finden Sie unter Document Manager in IDM auf dieser Seite.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Static Values**

    * Definieren Sie zunächst alle statischen Werte in einer einzigen Zeile mit dem Schlüssel **Static_Values**:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Weisen Sie anschließend jeder statischen Variablen mit dem Präfix **SV_** einen Wert zu:

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

* **Static Fields**
  * Statische Felder werden verwendet, um bestimmte, unveränderliche Werte für alle Dokumente festzulegen. Diese Werte bleiben über alle Dokumente hinweg konstant.
  *   Listen Sie zunächst alle verwendeten **Static**-Felder auf und geben Sie die **IDMAttributeId** und den Typ an.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Weisen Sie anschließend jedem Feld mit dem Präfix `SF_` statische Werte zu:

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

* **Index Fields**
  *   Listen Sie zunächst alle verwendeten Indexfelder auf und geben Sie die **IDMAttributeId** und den Typ an.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Jedes zugeordnete Feld folgt dem Format:

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Stellen Sie sicher, dass **IndexFieldFromDocBits = IDMAttributeID** gilt, um zu gewährleisten, dass die Feldzuordnung in DocBits mit den Attributen in IDM übereinstimmt (Document Type → Attributes).\        Eine Anleitung zur Navigation in IDM finden Sie unter Document Manager in IDM auf dieser Seite.

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

* **ACL Field Definition**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Searchable Name in IDM**
  * Der **Searchable PDF Name** wird der Dokumentname in IDM sein.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="IDM Mapping File Example"><figcaption></figcaption></figure>

## Export von XML- und EDI-Dateien

Um die ursprüngliche XML-/EDI-Datei zusammen mit dem generierten PDF zu exportieren, müssen Sie die IDM-Mapping-Datei in der Exportkonfiguration ändern. Aktualisieren Sie zunächst den Abschnitt **Static_Values**, indem Sie das Datei-Präfix und die Dateierweiterung hinzufügen. Definieren Sie anschließend das eigentliche Mapping, um die korrekte Exportkonfiguration sicherzustellen.

Wenn bereits ein Export von Rechnungen nach IDM eingerichtet ist, sollte das generierte PDF bereits im Export enthalten sein. Wenn Sie die XML-Datei nicht benötigen, können Sie den nächsten Teil überspringen. Falls Sie die XML-Datei jedoch benötigen, befolgen Sie die nachstehenden Schritte.

### Aktualisieren der Static Values:

Suchen Sie das Feld **Static_Values** und fügen Sie Folgendes hinzu:

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Fügen Sie anschließend die folgenden Einträge unterhalb von **SV_ACLString** hinzu:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Static Values Configuration Example"><figcaption></figcaption></figure>

### XML-Mapping

Fügen Sie das folgende Mapping am Ende der Datei hinzu:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Hinweis: Stellen Sie sicher, dass **export_doc_type** auf den IDM-Rechnungstyp gesetzt ist. In diesem Beispiel ist es für **M3** festgelegt.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="XML Mapping Example"><figcaption></figcaption></figure>

### EDI-Mapping

Fügen Sie das folgende Mapping am Ende der Datei hinzu:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Hinweis: Stellen Sie sicher, dass **export_doc_type** auf den IDM-Rechnungstyp gesetzt ist. In diesem Beispiel ist es für **M3** festgelegt.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="EDI Mapping Example"><figcaption></figcaption></figure>

### Document Manager in Infor

Gehen Sie zum Document Manager und wählen Sie den Namen des aktuellen Dokumenttyps aus, den Sie exportieren möchten, zum Beispiel Supplier Invoice.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Klicken Sie auf das oben gezeigte Symbol, klicken Sie anschließend auf Administration → Document Type und suchen Sie dann den benötigten Dokumenttyp in der Liste.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Wie unten dargestellt, sehen Sie anschließend den Namen des Dokumenttyps so, wie er in INFOR lautet.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Stellen Sie sicher, dass der Name in der IDM-Mapping-Datei genau so angezeigt wird.

## Datei in DocBits hochladen

Sobald die Datei vorbereitet ist, laden Sie sie in Ihre Exportkonfiguration in DocBits hoch. Diese ist unter Settings → Export verfügbar.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)