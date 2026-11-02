# Atributos de extração de documentos eletrônicos

## Tabela `public.electronic_document_extraction_attributes`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `electronic_document_type`: interno
* `attribute_name`: interno
* `attribute_type`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `last_modified_by`: interno
* `deleted_by`: interno

### Análise e descrição

## Documentação técnica de `public.electronic_document_extraction_attributes`

### Introdução

A tabela `public.electronic_document_extraction_attributes` parece gerenciar atributos relacionados à extração de documentos eletrônicos. Isso envolve o armazenamento de diversas características e metadados sobre os tipos de documentos eletrônicos, seus métodos de processamento e as organizações associadas. A tabela parece oferecer suporte a funcionalidades como identificação do tipo de documento, transformações, pré-visualizações e descrições de estrutura, essenciais para o tratamento eficaz de documentos eletrônicos.

### Descrição das colunas

#### id

* **Significado**: um identificador único para cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma sequência UUID que identifica de forma única cada entrada de atributo de extração de documento.
* **Observação**: serve como referência única para cada linha.

#### org\_id

* **Significado**: identificador da organização relacionada aos atributos do documento.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma sequência UUID que se vincula à organização associada.
* **Observação**: conecta os atributos de extração de documentos a uma organização específica.

#### doc\_type\_key

* **Significado**: uma chave que representa o tipo de documento.
* **Função**: identificador para categorizar documentos.
* **Conteúdo típico**: uma string que indica o tipo de documento, como 'INVOICE' ou 'ORDER\_CONFIRMATION'.
* **Observação**: usada para determinar a categoria do documento.

#### sub\_doc\_type\_key

* **Significado**: representa uma subcategoria do tipo de documento principal.
* **Função**: identificador para uma classificação mais detalhada.
* **Conteúdo típico**: nulo ou uma string de subtipo específica.
* **Observação**: útil para uma granularidade maior na classificação de documentos.

#### electronic\_document\_type

* **Significado**: o formato ou padrão do documento eletrônico.
* **Função**: campo descritivo do formato do documento.
* **Conteúdo típico**: strings como 'EDI' ou 'FACTURX'.
* **Observação**: indica o padrão ou formato do documento.

#### attribute\_name

* **Significado**: o nome do atributo relacionado ao processo de extração do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: strings como 'PREVIEW' ou 'TRANSFORMATION'.
* **Observação**: descreve o atributo específico relacionado ao tratamento do documento.

#### attribute\_type

* **Significado**: o tipo do atributo relacionado à extração do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: strings como 'XSLT' ou 'JSON'.
* **Observação**: especifica o formato de dados ou o método usado para o atributo.

#### created\_by

* **Significado**: ID do usuário que criou o registro.
* **Função**: chave estrangeira.
* **Conteúdo típico**: número inteiro que representa o ID de um usuário.
* **Observação**: registra quem criou o registro inicialmente.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora em UTC.
* **Observação**: indica o momento de criação do registro.

#### last\_modified\_on

* **Significado**: timestamp da última modificação do registro.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora em UTC, ou nulo se não foi modificado.
* **Observação**: registra a atualização mais recente do registro.

#### is\_deleted

* **Significado**: indica se o registro está marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano, `True` ou `False`.
* **Observação**: auxilia no tratamento de exclusão lógica.

#### deleted\_on

* **Significado**: timestamp de quando o registro foi marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora em UTC, ou uma data muito antiga padrão se não foi excluído.
* **Observação**: usado para registrar quando o registro foi excluído.

#### last\_modified\_by

* **Significado**: ID do usuário que modificou o registro pela última vez.
* **Função**: chave estrangeira.
* **Conteúdo típico**: string UUID, ou nulo se não foi modificado.
* **Observação**: identifica o usuário responsável pela última modificação.

#### deleted\_by

* **Significado**: ID do usuário que marcou o registro como excluído.
* **Função**: chave estrangeira.
* **Conteúdo típico**: string UUID, ou nulo se não foi excluído.
* **Observação**: registra quem executou a ação de exclusão.

Esta documentação oferece uma visão geral detalhada da estrutura da tabela e de suas colunas, facilitando a compreensão e o uso por desenvolvedores e administradores de banco de dados.
