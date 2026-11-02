# Gatilho de status do documento

## Tabela `public.document_status_trigger`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `trigger_doc_type`: interno
* `trigger_doc_status`: interno
* `trigger_url`: interno
* `is_active`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação técnica da tabela `public.document_status_trigger`

### Introdução

A tabela `public.document_status_trigger` foi projetada para gerenciar e acompanhar o status de documentos dentro de uma organização. Esta tabela parece tratar de gatilhos relacionados ao processamento de documentos, provavelmente em um sistema de fluxo de trabalho. Ela registra informações sobre os tipos de documento e suas mudanças de status, podendo disparar ações ou fluxos de trabalho por meio de URLs especificadas.

### Descrição das colunas

#### id

* **Significado**: esta coluna armazena um identificador único para cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID, por exemplo, `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Significado**: representa o identificador único de uma organização.
* **Função**: chave estrangeira, vinculada a uma entidade de organização.
* **Conteúdo típico**: uma string UUID, por exemplo, `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Significado**: especifica o tipo de documento associado ao gatilho.
* **Função**: campo descritivo que indica o tipo de documento.
* **Conteúdo típico**: nomes de tipos de documento, como `INVOICE`.

#### trigger\_doc\_status

* **Significado**: indica o status específico do documento que ativa o gatilho.
* **Função**: campo descritivo que detalha o status do documento.
* **Conteúdo típico**: descrições de status, como `approved_pending_second_approval`.

#### trigger\_url

* **Significado**: URL que é acionada quando o status do documento atende a determinadas condições.
* **Função**: campo técnico para automação de fluxo de trabalho.
* **Conteúdo típico**: URLs, por exemplo, `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Significado**: indica se o gatilho está ativo no momento.
* **Função**: campo técnico para gerenciar os estados do gatilho.
* **Conteúdo típico**: valores booleanos, `True` ou `False`.

#### created\_by

* **Significado**: identifica o usuário que criou o registro.
* **Função**: chave estrangeira para uma entidade de usuário.
* **Conteúdo típico**: IDs de usuário inteiros, por exemplo, `1`.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo técnico para auditoria e acompanhamento de alterações.
* **Conteúdo típico**: timestamps com fuso horário, por exemplo, `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Significado**: timestamp da última modificação do registro.
* **Função**: campo técnico para auditoria e acompanhamento de alterações.
* **Conteúdo típico**: timestamps com fuso horário; pode ser `None` se não foi modificado.

#### is\_deleted

* **Significado**: indica se o registro é considerado excluído ou inativo.
* **Função**: campo técnico para exclusão lógica.
* **Conteúdo típico**: valores booleanos, `True` ou `False`.

Esta tabela oferece uma abordagem estruturada para gerenciar os status de documentos e os gatilhos associados no sistema de fluxo de trabalho de uma organização, garantindo que ações possam ser executadas automaticamente à medida que os documentos avançam pelos diversos estados.
