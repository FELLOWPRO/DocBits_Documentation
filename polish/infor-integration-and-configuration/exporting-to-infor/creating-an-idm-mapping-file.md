# Tworzenie pliku mapowania IDM

## Pola w pliku mapowania IDM

Podczas tworzenia pliku mapowania IDM wymagane są następujące pola:

* **Definicja typu dokumentu**
  * Upewnij się, że kod typu dokumentu w DocBits odpowiada nazwie użytej w URL ustawień pola, podobnie jak w pliku mapowania BOD.
  * Sprawdź, czy nazwa typu dokumentu w IDM jest zgodna z konfiguracją Twojego systemu. Na przykład w M3 może to być **M3_SupplierInvoice**, podczas gdy w LN będzie to inna nazwa, zależnie od Twojej konfiguracji.
    * Przewodnik po nawigacji w IDM można znaleźć w sekcji Document Manager w IDM na tej stronie.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Wartości statyczne (Static Values)**

    * Najpierw zdefiniuj wszystkie wartości statyczne w jednym wierszu, używając klucza **Static_Values**:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Następnie przypisz wartości do każdej zmiennej statycznej, używając prefiksu **SV_**:

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

* **Pola statyczne (Static Fields)**
  * Pola statyczne służą do ustawiania określonych, niezmiennych wartości we wszystkich dokumentach. Wartości te pozostają takie same w każdym dokumencie.
  *   Zacznij od wymienienia wszystkich używanych pól **Static**, podając **IDMAttributeId** i typ.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Następnie przypisz wartości statyczne do każdego pola, używając prefiksu `SF_`:

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

* **Pola indeksu (Index Fields)**
  *   Zacznij od wymienienia wszystkich używanych pól indeksu, podając **IDMAttributeId** i typ.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Każde zmapowane pole ma następujący format:

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Potwierdź, że **IndexFieldFromDocBits = IDMAttributeID**, aby mapowanie pól w DocBits odpowiadało atrybutom w IDM (Document Type → Attributes).\        Przewodnik po nawigacji w IDM można znaleźć w sekcji Document Manager w IDM na tej stronie.

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

* **Definicja pola ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nazwa wyszukiwalna w IDM**
  * **Searchable PDF Name** będzie nazwą dokumentu w IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="Przykład pliku mapowania IDM"><figcaption></figcaption></figure>

## Eksport plików XML i EDI

Aby wyeksportować oryginalny plik XML/EDI wraz z wygenerowanym plikiem PDF, musisz zmodyfikować plik mapowania IDM w konfiguracji eksportu. Najpierw zaktualizuj sekcję **Static_Values**, dodając prefiks i rozszerzenie pliku. Następnie zdefiniuj właściwe mapowanie, aby zapewnić poprawną konfigurację eksportu.

Jeśli eksport faktur do IDM jest już skonfigurowany, wygenerowany plik PDF powinien być już uwzględniony w eksporcie. Jeśli nie potrzebujesz pliku XML, możesz pominąć następną część. Jeśli jednak plik XML jest potrzebny, wykonaj poniższe kroki.

### Aktualizacja wartości statycznych:

Znajdź pole **Static_Values** i dodaj następujące:a

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Następnie dodaj poniższe wpisy pod **SV_ACLString**:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Przykład konfiguracji wartości statycznych"><figcaption></figcaption></figure>

### Mapowanie XML

Dodaj następujące mapowanie na końcu pliku:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Uwaga: upewnij się, że **export_doc_type** jest ustawiony na typ faktury w IDM. W tym przykładzie jest ustawiony dla **M3**.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="Przykład mapowania XML"><figcaption></figcaption></figure>

### Mapowanie EDI

Dodaj następujące mapowanie na końcu pliku:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Uwaga: upewnij się, że **export_doc_type** jest ustawiony na typ faktury w IDM. W tym przykładzie jest ustawiony dla **M3**.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="Przykład mapowania EDI"><figcaption></figcaption></figure>

### Document Manager w Infor

Przejdź do Document Manager i wybierz nazwę bieżącego typu dokumentu, który próbujesz wyeksportować, na przykład Supplier Invoice.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Kliknij powyższą ikonę, a następnie kliknij Administration → Document Type i znajdź na liście potrzebny typ dokumentu

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Jak pokazano poniżej, zobaczysz nazwę typu dokumentu dokładnie tak, jak występuje w INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Upewnij się, że nazwa w pliku mapowania IDM jest zapisana dokładnie w ten sposób

## Przesyłanie pliku do DocBits

Po przygotowaniu pliku prześlij go do swojej konfiguracji eksportu w DocBits. Jest ona dostępna w Settings → Export.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
