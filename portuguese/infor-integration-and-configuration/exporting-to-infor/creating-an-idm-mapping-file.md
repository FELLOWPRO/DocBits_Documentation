# Criando um Arquivo de Mapeamento IDM

## Campos Obrigatórios para o Arquivo de Mapeamento IDM

Ao criar um arquivo de mapeamento IDM, os seguintes campos são obrigatórios:

* **Definição do Tipo de Documento**
  * Certifique-se de que o código do tipo de documento em DocBits corresponda ao nome usado na URL das configurações de campo, semelhante ao Arquivo de Mapeamento BOD.
  * Verifique se o nome do tipo de documento em IDM está alinhado com a configuração do seu sistema. Por exemplo, no M3, pode ser **M3\_SupplierInvoice**, enquanto no LN, será diferente com base na sua configuração.
    * Um guia sobre como navegar no IDM pode ser encontrado no Gerenciador de Documentos em IDM nesta página.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

* **Valores Estáticos**
  *   Primeiro, defina todos os valores estáticos em uma única linha usando a chave **Static\_Values**:

      ```properties
      Static_Values=FileNameSeparator,ACLString
      ```
  *   Em seguida, atribua valores a cada variável estática usando o prefixo **SV\_**:

      ```properties
      SV_FileNameSeparator=_
      SV_ACLString=Public
      ```
* **Definição do Campo ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nome Pesquisável em IDM**
  * O **Nome PDF Pesquisável** será o nome do documento em IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID
```

## Mapeamento de Campos

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

*   Comece listando todos os campos de índice utilizados, especificando o ID e o tipo do campo.

    ```properties
    Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
    ```
*   Cada campo mapeado segue o formato:

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Confirme que **IndexFieldFromDocBits = IDMAttributeID**, garantindo que o mapeamento de campos em DocBits esteja alinhado com os atributos em IDM (Tipo de Documento → Atributos). Um guia sobre como navegar no IDM pode ser encontrado no Gerenciador de Documentos em IDM nesta página.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FzT9MMKlFCSBJtRW1pf4s%2Fimage.png?alt=media\&token=ea2f6ae2-f9f2-48d3-98e3-ed06dcda69f1)

### Exportação de arquivo XML e EDI

Para exportar o arquivo XML/EDI original juntamente com o PDF gerado, você precisa modificar o arquivo de Mapeamento IDM, na configuração de exportação. Primeiro, atualize a seção **Static\_Values** adicionando o prefixo e a extensão do arquivo. Depois disso, defina o mapeamento real para garantir a configuração de exportação correta.

Se uma exportação para faturas para IDM já estiver configurada, o PDF gerado já deve estar incluído na exportação. Se você não precisar do arquivo XML, pode pular a próxima parte. No entanto, se você precisar do arquivo XML, siga os passos abaixo.

#### Atualizando os Valores Estáticos:

Encontre o campo **Static\_Values** e adicione o seguinte:

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Em seguida, adicione as seguintes entradas abaixo de **SV\_ACLString**:

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Depois disso, adicione o mapeamento real, certificando-se de que o tipo de documento de exportação corresponda ao tipo de fornecedor IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mapeamento XML

Adicione o seguinte mapeamento na parte inferior do arquivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Nota: Certifique-se de que **export\_doc\_type** esteja definido como o tipo de fatura IDM. Neste exemplo, está definido para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mapeamento EDI

Adicione o seguinte mapeamento na parte inferior do arquivo:

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Nota: Certifique-se de que **export\_doc\_type** esteja definido como o tipo de fatura IDM. Neste exemplo, está definido para **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Gerenciador de Documentos no Infor

Vá para o Gerenciador de Documentos e selecione o nome do tipo de documento atual que você está tentando exportar, por exemplo, Fatura do Fornecedor.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Clique no ícone acima e depois clique em Administração → Tipo de Documento e, em seguida, encontre o tipo de documento que você precisa na lista.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Como mostrado abaixo, você verá o nome do tipo de documento como está no INFOR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Certifique-se de que é assim que o nome é mostrado no Arquivo de Mapeamento IDM.

### Carregar Arquivo para DocBits

Uma vez que o arquivo esteja preparado, faça o upload para sua configuração de exportação no DocBits. Isso está disponível em Configurações → Exportar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)
