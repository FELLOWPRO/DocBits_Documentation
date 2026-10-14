# Correspondência de pedidos de compra do Ephesoft

## Tabela `public.ephesoft_po_matching`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_id`: interno
* `doc_type`: tipo de documento
* `ephesoft_doc_id`: interno
* `extracted_data`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação técnica da tabela `public.ephesoft_po_matching`

### Introdução

A tabela `public.ephesoft_po_matching` foi projetada para armazenar e gerenciar dados relacionados à correspondência de pedidos de compra com documentos, como faturas, processados pelo sistema Ephesoft. Essa tabela registra diversos detalhes sobre os documentos, seu processo de extração e o status da correspondência com pedidos de compra.

### Descrição das colunas

#### id

* **Significado**: um identificador único para cada registro da tabela, que provavelmente representa um documento ou uma transação específica processada.
* **Função**: chave primária.
* **Conteúdo típico**: identificador universalmente único (UUID) em formato string, por exemplo `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Significado**: identificador da organização associada ao documento ou à transação.
* **Função**: chave estrangeira, possivelmente vinculada a uma tabela de organizações.
* **Conteúdo típico**: UUID em formato string, por exemplo `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Significado**: identificador do documento processado pelo sistema.
* **Função**: chave estrangeira, vinculada a uma tabela de documentos ou similar.
* **Conteúdo típico**: UUID em formato string, por exemplo `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Significado**: tipo do documento processado, que indica a natureza do documento (por exemplo, INVOICE).
* **Função**: campo descritivo.
* **Conteúdo típico**: string que indica o tipo de documento, por exemplo `INVOICE`.

#### ephesoft\_doc\_id

* **Significado**: identificador usado pelo sistema Ephesoft para acompanhar o documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: string curta, possivelmente um identificador, por exemplo `DOC1`.

#### extracted\_data

* **Significado**: dados JSON com as informações extraídas do documento, incluindo campos, tabelas e metadados.
* **Função**: campo de armazenamento do conteúdo extraído do documento.
* **Conteúdo típico**: estrutura JSON com detalhes como tipo de documento, campos, tabelas e metadados.

#### created\_by

* **Significado**: identificador do usuário ou do sistema que criou o registro.
* **Função**: chave estrangeira, possivelmente vinculada a uma tabela de usuários.
* **Conteúdo típico**: número inteiro que representa o ID de um usuário, por exemplo `1`.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo técnico para o acompanhamento do registro.
* **Conteúdo típico**: timestamp com fuso horário, por exemplo `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Significado**: timestamp da última modificação do registro.
* **Função**: campo técnico para o acompanhamento do registro.
* **Conteúdo típico**: timestamp com fuso horário; pode ser nulo se não houve modificação desde a criação.

#### is\_deleted

* **Significado**: indicador que informa se o registro está marcado como excluído.
* **Função**: campo técnico para exclusão lógica.
* **Conteúdo típico**: booleano, `true` se o registro foi excluído e `false` caso contrário.
