# Adicionando e Editando Campos

## Aqui estão os passos para adicionar um novo campo ou modificar campos existentes no DocBits, incluindo detalhes sobre como acessar opções de configuração avançadas:

#### Adicionar um novo campo

* Faça login e acesse a Gestão de Documentos:

![Menu de configurações com a navegação Global Settings e as entradas Company Information, Groups Users and Permissions, Integration e Document Types](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fx3R65rHE45OlNCmUWrws%252FBildschirmfoto%25202024-05-23%2520um%252013.35.39.png%3Falt%3Dmedia%26token%3D5955c7bc-60f1-462c-9a39-964a94a82a9e\&width=768\&dpr=4\&quality=100\&sign=d8b8226e\&sv=2)

![Ecrã de configurações de Invoice com os separadores Labels, Edit layout, Document Sub Types, Table columns, Model Training, Regex, Scripts e EDI](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FaYWPJkffG6wnCbqyZPXj%252FBildschirmfoto%25202024-05-23%2520um%252013.38.53.png%3Falt%3Dmedia%26token%3Dcaa0a6ab-ca23-4602-83f2-e96956c25c00\&width=768\&dpr=4\&quality=100\&sign=942dc499\&sv=2)

**Adicionar um novo campo:**

* Clique na opção "Criar Campo".

![Lista de campos de Invoice details com as linhas invoice_id e Invoice number e as colunas Required, Hidden, OCR e Match Score](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWT32A6D02SxrepzTsBb2%252FBildschirmfoto%25202024-05-23%2520um%252013.41.38.png%3Falt%3Dmedia%26token%3De12b24d3-6f21-421c-ba46-d597c5ded908\&width=768\&dpr=4\&quality=100\&sign=b9c92149\&sv=2)

**Configuração Básica:**

![Diálogo de detalhes do campo do documento com Name, Title, menu pendente Select field type, interruptor Enable charges element e botão Save](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FVZmZsa7k7aaxNRLBmF5B%252Fimage.png%3Falt%3Dmedia%26token%3Db86d33a6-aeec-4336-926d-ad3a742af004\&width=768\&dpr=4\&quality=100\&sign=565e929b\&sv=2)

* **Nome**
  * Escolha um nome significativo e descritivo.
  * O nome deve ser único.
  * **Nota:** **Uma vez criado, o nome não pode ser alterado.**
* **Título**
  * Este é o nome exibido do campo.
  * Ele define como o campo aparece na interface do usuário.
  * **Nota:** **O título pode ser alterado posteriormente, se necessário.**
*   **Selecionar Tipo de Campo**

    * Escolha o tipo de campo a partir de uma lista suspensa.
    * Os tipos de campo disponíveis incluem várias opções para atender a diferentes necessidades de entrada de dados.
    * **Nota:** **Uma vez criado, o Tipo não pode ser alterado.**

    ![Menu pendente do tipo de campo com as opções Amount, String, Date, Number, Boolean, Currency e Dropdown e o botão Save](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FGdj3E8rrETfMp5fcEV2v%252Fimage.png%3Falt%3Dmedia%26token%3D7c0e6903-2204-447e-9d9b-c645f5a39067\&width=768\&dpr=4\&quality=100\&sign=3dd6efa8\&sv=2)
* **Opcional: Habilitar Elemento de Cobrança**
  * Uma caixa de seleção rotulada **Habilitar Elemento de Cobrança** pode ser selecionada.
  * Se marcada, você deve selecionar um elemento de cobrança a partir de uma lista suspensa.
  * **Importante:** Elementos de cobrança devem ser configurados previamente.
    * [Configuração de Elementos de Cobrança](https://docs.docbits.com/infor-integration-and-configuration/importing-customer-master-data/m3/table-extraction-for-costing-element)

**Configuração Avançada:**

* Aqui você pode definir outras propriedades, como regras de validação, valores de correspondência, modo somente leitura, ocultação e configurações de OCR.

![Tabela de campos para invoice_date com as colunas Required, Read Only, Hidden, Force Validation, OCR e Match Score](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FMxWT88mJzJ9aXmDED7Q4%252Fimage.png%3Falt%3Dmedia%26token%3D08c8867f-b560-44b3-8c23-e58bc6a31edd\&width=768\&dpr=4\&quality=100\&sign=635dad12\&sv=2)

**Salvar:**

* Após ter feito todas as configurações necessárias, clique em "Salvar" ou em um botão semelhante para criar o novo campo.

![Configuração de campo concluída, pronta para ser guardada com o botão Save](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FN1fp3VvCI0z7Yfe9ab6Y%252Fimage.png%3Falt%3Dmedia%26token%3D6e465e61-7f18-4302-aa9d-1e7c7619d574\&width=768\&dpr=4\&quality=100\&sign=94a50871\&sv=2)

**Acessar edição de campo:**

* Navegue até a lista de campos existentes e encontre o campo que deseja editar.

![Lista de campos de Vendor details com as linhas supplier_id e supplier_name e os interruptores Required, Read Only, OCR e Match Score](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2PJ9r9cBuD1K9MILmfGg%252Fimage.png%3Falt%3Dmedia%26token%3D7228e55e-b499-4aa4-b93d-217461371e26\&width=768\&dpr=4\&quality=100\&sign=54b4ab44\&sv=2)

**Selecionar um campo:**

* Clique no campo apropriado para acessar as opções de edição.

![Secção Vendor details com o botão Create Field e o campo vendor_id pronto para seleção](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F5EYT3k6jASAJz4RDgf2k%252Fimage.png%3Falt%3Dmedia%26token%3D4133db05-50cc-45e4-9c47-2ab9039e91ae\&width=768\&dpr=4\&quality=100\&sign=eac7a82f\&sv=2)

**Alterar a configuração:**

* Altere as propriedades do campo conforme necessário. Isso pode incluir mudar o nome, o tipo de campo, adicionar ou remover regras de validação, definir valores de correspondência ou ajustar outras configurações avançadas.

**Nota:** Se você alterar o **Título** de um campo, deve excluir e re-adicionar o campo no construtor de layout para que as alterações tenham efeito.

![Tabela de campos de Vendor details com a linha Vendor ID e as opções Required, Read Only, Hidden, Force Validation, OCR e Match Score](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FChH8vw1tSklCKJQRZTwn%252Fimage.png%3Falt%3Dmedia%26token%3D01f468df-aca1-464f-9609-9a460cc36735\&width=768\&dpr=4\&quality=100\&sign=6b4bd2da\&sv=2)

**Salvar:**

* Clique em "Salvar" para salvar as alterações que você fez no campo.

![Configuração de campo editada com o botão Save para aplicar as alterações do campo](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOm9YrCnnYI3JWDj0RPjT%252Fimage.png%3Falt%3Dmedia%26token%3Dc4b0e2d7-8402-4acc-9cfb-11c360ca1aaf\&width=768\&dpr=4\&quality=100\&sign=9fbc3f36\&sv=2)

Ao fornecer passos para adicionar novos campos e editar campos existentes, bem como acesso a opções de configuração avançadas, você pode maximizar a flexibilidade e adaptabilidade do seu sistema de processamento de documentos. Isso permite que você estruture e processe seus dados exatamente como precisar.
