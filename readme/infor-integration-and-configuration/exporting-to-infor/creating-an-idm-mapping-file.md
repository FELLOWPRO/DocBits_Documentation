# Een IDM-mappingbestand maken

## Velden voor het IDM-mappingbestand

Bij het maken van een IDM-mappingbestand zijn de volgende velden vereist:

* **Definitie van documenttype**
  * Zorg ervoor dat de documenttypecode in DocBits overeenkomt met de naam die in de URL van de veldinstellingen wordt gebruikt, vergelijkbaar met het BOD-mappingbestand.
  * Controleer of de naam van het documenttype in IDM overeenkomt met uw systeemconfiguratie. In M3 kan dit bijvoorbeeld **M3_SupplierInvoice** zijn, terwijl het in LN afhankelijk van uw setup anders is.
    * Een handleiding voor het navigeren in IDM vindt u onder Document Manager in IDM op deze pagina.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Static Values**

    * Definieer eerst alle statische waarden op één regel met de sleutel **Static_Values**:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Wijs vervolgens aan elke statische variabele een waarde toe met het voorvoegsel **SV_**:

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
  * Statische velden worden gebruikt om voor alle documenten specifieke, onveranderlijke waarden in te stellen. Deze waarden blijven voor alle documenten gelijk.
  *   Begin met het opsommen van alle gebruikte **Static**-velden, met vermelding van de **IDMAttributeId** en het type.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Wijs vervolgens aan elk veld statische waarden toe met het voorvoegsel `SF_`:

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
  *   Begin met het opsommen van alle gebruikte indexvelden, met vermelding van de **IDMAttributeId** en het type.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Elk gemapt veld heeft de volgende notatie:

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Bevestig dat **IndexFieldFromDocBits = IDMAttributeID**, zodat de veldmapping in DocBits overeenkomt met de attributen in IDM (Document Type → Attributes).\        Een handleiding voor het navigeren in IDM vindt u onder Document Manager in IDM op deze pagina.

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

* **Doorzoekbare naam in IDM**
  * De **Searchable PDF Name** is de documentnaam in IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="Voorbeeld van een IDM-mappingbestand"><figcaption></figcaption></figure>

## Export van XML- en EDI-bestanden

Om het originele XML/EDI-bestand samen met de gegenereerde PDF te exporteren, moet u het IDM-mappingbestand in de exportconfiguratie aanpassen. Werk eerst het gedeelte **Static_Values** bij door het bestandsvoorvoegsel en de extensie toe te voegen. Definieer daarna de eigenlijke mapping, zodat de exportconfiguratie klopt.

Als er al een export van facturen naar IDM is ingesteld, zit de gegenereerde PDF al in de export. Als u het XML-bestand niet nodig hebt, kunt u het volgende gedeelte overslaan. Hebt u het XML-bestand wel nodig, volg dan de onderstaande stappen.

### De Static Values bijwerken:

Zoek het veld **Static_Values** en voeg het volgende toe:

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Voeg vervolgens de volgende regels toe onder **SV_ACLString**:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Voorbeeld van de configuratie van Static Values"><figcaption></figcaption></figure>

### XML-mapping

Voeg de volgende mapping onderaan het bestand toe:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Opmerking: Zorg ervoor dat **export_doc_type** is ingesteld op het IDM-factuurtype. In dit voorbeeld is het ingesteld voor **M3**.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="Voorbeeld van een XML-mapping"><figcaption></figcaption></figure>

### EDI-mapping

Voeg de volgende mapping onderaan het bestand toe:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Opmerking: Zorg ervoor dat **export_doc_type** is ingesteld op het IDM-factuurtype. In dit voorbeeld is het ingesteld voor **M3**.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="Voorbeeld van een EDI-mapping"><figcaption></figcaption></figure>

### Documentbeheer in Infor

Ga naar Document Manager en selecteer de naam van het documenttype dat u wilt exporteren, bijvoorbeeld Supplier Invoice.

![Documentlijst in Infor Document Manager met het documenttype Rental_Invoice en de details van aanmaak en wijziging](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Klik op het bovenstaande pictogram en klik vervolgens op Administration → Document Type. Zoek daarna het gewenste documenttype in de lijst.

![Infor Control Center Document Type-pagina met documenttypen zoals Bank Statement CAMT053 en Customer invoice](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Zoals hieronder getoond ziet u dan de naam van het documenttype zoals deze in INFOR staat.

![Infor Document Manager MONGOOSE Reports-pagina met het tabblad Attributes en een documenttypenlijst inclusief Purchase Order](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Zorg ervoor dat de naam in het IDM-mappingbestand precies zo is opgenomen.

## Bestand uploaden naar DocBits

Zodra het bestand gereed is, uploadt u het naar uw exportconfiguratie in DocBits. Deze is beschikbaar onder Settings → Export.

![DocBits Export Settings-pagina met een factuuritem dat de INVOKE-webhook-exportmethode gebruikt en IDM Mapping File geselecteerd](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
