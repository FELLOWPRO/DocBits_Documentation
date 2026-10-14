# Een IDM Mappingbestand maken

## Vereiste Velden voor IDM Mapping Bestand

Bij het aanmaken van een IDM mapping bestand zijn de volgende velden vereist:

* **Documenttype Definitie**
  * Zorg ervoor dat de documenttypecode in DocBits overeenkomt met de naam die in de URL van de veldinstellingen wordt gebruikt, vergelijkbaar met het BOD Mapping Bestand.
  * Controleer of de documenttypename in IDM overeenkomt met uw systeemconfiguratie. Bijvoorbeeld, in M3 kan dit **M3\_SupplierInvoice** zijn, terwijl het in LN anders zal zijn, afhankelijk van uw setup.
    * Een gids over hoe te navigeren in IDM is te vinden in Document Manager in IDM op deze pagina.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

* **Statische Waarden**
  *   Definieer eerst alle statische waarden in één regel met de **Static\_Values** sleutel:

      ```properties
      Static_Values=FileNameSeparator,ACLString
      ```
  *   Wijs vervolgens waarden toe aan elke statische variabele met de **SV\_** prefix:

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

* **ACL Veld Definitie**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Doorzoekbare Naam in IDM**
  * De **Doorzoekbare PDF Naam** zal de documentnaam in IDM zijn.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID
```

## Veld Mapping

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

*   Begin met het opsommen van alle indexvelden die worden gebruikt, met vermelding van de veld-ID en het type.

    ```properties
    Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
    ```
*   Elk gemapt veld volgt het formaat:

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Bevestig dat **IndexFieldFromDocBits = IDMAttributeID**, zodat de veldmapping in DocBits overeenkomt met de attributen in IDM (Documenttype → Attributen). Een gids over hoe te navigeren in IDM is te vinden in Document Manager in IDM op deze pagina.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FzT9MMKlFCSBJtRW1pf4s%2Fimage.png?alt=media\&token=ea2f6ae2-f9f2-48d3-98e3-ed06dcda69f1)

### XML- en EDI-bestandsexport

Om het originele XML/EDI-bestand samen met de gegenereerde PDF te exporteren, moet je het IDM Mappingbestand aanpassen in de exportconfiguratie. Werk eerst de sectie **Static\_Values** bij door het bestandsvoorvoegsel en de extensie toe te voegen. Voeg daarna de daadwerkelijke mapping toe om de juiste exportconfiguratie te waarborgen.

Als er al een export voor facturen naar IDM is ingesteld, zou de gegenereerde PDF al in de export moeten zijn opgenomen. Als je het XML-bestand niet nodig hebt, kun je het volgende deel overslaan. Als je echter het XML-bestand wel nodig hebt, volg dan de onderstaande stappen.

#### De statische waarden bijwerken:

Zoek het veld **Static\_Values** en voeg het volgende toe:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Voeg vervolgens de volgende vermeldingen toe onder **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Voeg daarna de daadwerkelijke mapping toe, zorg ervoor dat het exportdocumenttype overeenkomt met het IDM-leverancierstype.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### XML-mapping

Voeg de volgende mapping onderaan het bestand toe:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Opmerking: Zorg ervoor dat **export\_doc\_type** is ingesteld op het IDM-factuurtype. In dit voorbeeld is het ingesteld voor **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### EDI-mapping

Voeg de volgende mapping onderaan het bestand toe:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Opmerking: Zorg ervoor dat **export\_doc\_type** is ingesteld op het IDM-factuurtype. In dit voorbeeld is het ingesteld voor **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Document Manager in Infor

Ga naar Document Manager en selecteer de naam van het huidige documenttype dat je probeert te exporteren, bijvoorbeeld Leveranciersfactuur.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Klik op het bovenstaande pictogram en klik vervolgens op Beheer → Documenttype en zoek het documenttype dat je nodig hebt in de lijst.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Zoals hieronder weergegeven, zie je dan de naam van het documenttype zoals deze in INFOR is.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Zorg ervoor dat dit is hoe de naam wordt weergegeven in het IDM Mappingbestand.

### Bestand uploaden naar DocBits

Zodra het bestand is voorbereid, upload je het naar je exportconfiguratie in DocBits. Dit is beschikbaar onder Instellingen → Exporteren.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
