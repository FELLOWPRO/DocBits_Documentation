# Criando um Arquivo de Mapeamento IDM

## Campos do Arquivo de Mapeamento IDM

Ao criar um arquivo de mapeamento IDM, os seguintes campos são obrigatórios:

* **Definição do Tipo de Documento**
  * Certifique-se de que o código do tipo de documento no DocBits corresponda ao nome usado na URL das configurações de campo, de forma semelhante ao Arquivo de Mapeamento BOD.
  * Verifique se o nome do tipo de documento no IDM está de acordo com a configuração do seu sistema. Por exemplo, no M3 pode ser **M3_SupplierInvoice**, enquanto no LN será diferente, conforme a sua configuração.
    * Um guia sobre como navegar no IDM pode ser encontrado em Document Manager no IDM, nesta página.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Valores Estáticos**

    * Primeiro, defina todos os valores estáticos em uma única linha usando a chave **Static_Values**:

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Em seguida, atribua valores a cada variável estática usando o prefixo **SV_**:

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

* **Campos Estáticos**
  * Os campos estáticos são usados para definir valores específicos e imutáveis em todos os documentos. Esses valores permanecem os mesmos em todos os documentos.
  *   Comece listando todos os campos **Static** utilizados, especificando o **IDMAttributeId** e o tipo.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Em seguida, atribua valores estáticos a cada campo usando o prefixo `SF_`:

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

* **Campos de Índice**
  *   Comece listando todos os campos de índice utilizados, especificando o **IDMAttributeId** e o tipo.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Cada campo mapeado segue o formato:

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Confirme que **IndexFieldFromDocBits = IDMAttributeID**, garantindo que o mapeamento de campos no DocBits esteja alinhado com os atributos no IDM (Document Type → Attributes).\        Um guia sobre como navegar no IDM pode ser encontrado em Document Manager no IDM, nesta página.

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

* **Definição do Campo ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nome Pesquisável no IDM**
  * O **Searchable PDF Name** será o nome do documento no IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="Exemplo de arquivo de mapeamento IDM"><figcaption></figcaption></figure>

## Exportação de arquivos XML e EDI

Para exportar o arquivo XML/EDI original junto com o PDF gerado, você precisa modificar o arquivo de mapeamento IDM na configuração de exportação. Primeiro, atualize a seção **Static_Values** adicionando o prefixo e a extensão do arquivo. Depois disso, defina o mapeamento propriamente dito para garantir a configuração de exportação correta.

Se uma exportação de faturas para o IDM já estiver configurada, o PDF gerado já deve estar incluído na exportação. Se você não precisar do arquivo XML, pode pular a próxima parte. Se precisar do arquivo XML, siga os passos abaixo.

### Atualizando os Valores Estáticos:

Localize o campo **Static_Values** e adicione o seguinte:

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Em seguida, adicione as entradas a seguir abaixo de **SV_ACLString**:

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Exemplo de configuração de valores estáticos"><figcaption></figcaption></figure>

### Mapeamento XML

Adicione o seguinte mapeamento no final do arquivo:

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Observação: certifique-se de que **export_doc_type** esteja definido como o tipo de fatura do IDM. Neste exemplo, ele está definido para o **M3**.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="Exemplo de mapeamento XML"><figcaption></figcaption></figure>

### Mapeamento EDI

Adicione o seguinte mapeamento no final do arquivo:

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Observação: certifique-se de que **export_doc_type** esteja definido como o tipo de fatura do IDM. Neste exemplo, ele está definido para o **M3**.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="Exemplo de mapeamento EDI"><figcaption></figcaption></figure>

### Document Manager no Infor

Acesse o Document Manager e selecione o nome do tipo de documento que você está tentando exportar, por exemplo, Supplier Invoice.

![Lista de documentos do Infor Document Manager com o tipo de documento Rental_Invoice e os respetivos detalhes de criação e modificação](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Clique no ícone acima, depois em Administration → Document Type e localize na lista o tipo de documento de que você precisa

![Página Document Type do Infor Control Center listando tipos de documentos como Bank Statement CAMT053 e Customer invoice](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Conforme mostrado abaixo, você verá o nome do tipo de documento exatamente como ele está no INFOR

![Página MONGOOSE Reports do Infor Document Manager com o separador Attributes e uma lista de tipos de documentos incluindo Purchase Order](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Certifique-se de que o nome apareça exatamente assim no Arquivo de Mapeamento IDM

## Carregar o arquivo no DocBits

Quando o arquivo estiver pronto, carregue-o na sua configuração de exportação no DocBits. Ela está disponível em Settings → Export.

![Página de Export Settings do DocBits com uma entrada de fatura usando o método de exportação webhook INVOKE e IDM Mapping File selecionado](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
