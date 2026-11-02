# public.document\_log

## Tabela `public.document_log`

### Colunas

* `id`: inteiro
* `org_id`: ID da organização
* `doc_id`: interno
* `action_type`: interno
* `action_description`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `is_hidden`: booleano
* `previous_status`: interno
* `current_status`: interno

### Análise e descrição

## Documentação técnica: tabela `public.document_log`

### Introdução

A tabela `public.document_log` foi projetada para registrar o histórico e as mudanças de status dos documentos dentro de uma organização. Ela registra as ações executadas nos documentos, como atualizações de status, junto com detalhes sobre o usuário que executou a ação e timestamps que indicam quando essas ações ocorreram. Essa tabela é fundamental para auditar os fluxos de processamento de documentos e entender o ciclo de vida de cada documento.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada entrada de log.
* **Função**: chave primária. Esta coluna serve como identificador único de cada registro da tabela.
* **Conteúdo típico**: valores inteiros que são incrementados a cada nova entrada.

#### org\_id

* **Significado**: identificador da organização associada ao documento.
* **Função**: chave estrangeira. Vincula-se a uma entidade de organização, embora isso não esteja definido explicitamente neste contexto.
* **Conteúdo típico**: strings de caracteres, provavelmente UUIDs, que representam identificadores de organizações.

#### doc\_id

* **Significado**: identificador do documento associado à entrada de log.
* **Função**: chave estrangeira. Esta coluna referencia um documento específico dentro do sistema.
* **Conteúdo típico**: strings de caracteres, provavelmente UUIDs, que representam identificadores de documentos.

#### action\_type

* **Significado**: tipo da ação registrada.
* **Função**: campo descritivo. Indica a categoria da ação executada.
* **Conteúdo típico**: strings como `STATUS_CHANGE`, que indicam a natureza da ação.

#### action\_description

* **Significado**: descrição detalhada da ação executada.
* **Função**: campo descritivo. Fornece contexto ou detalhes sobre a ação.
* **Conteúdo típico**: descrições em texto, por exemplo "Data extraction started" e "Error occurred processing document".

#### created\_by

* **Significado**: identificador do usuário que criou a entrada de log.
* **Função**: chave estrangeira. Vincula-se a uma entidade de usuário e indica quem executou a ação.
* **Conteúdo típico**: valores inteiros que representam identificadores de usuários.

#### created\_on

* **Significado**: timestamp de quando a entrada de log foi criada.
* **Função**: campo técnico. Registra o momento exato em que uma ação foi registrada.
* **Conteúdo típico**: timestamps com informações de fuso horário, por exemplo `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Significado**: timestamp da última modificação da entrada de log.
* **Função**: campo técnico. Indica o momento da última atualização da entrada de log.
* **Conteúdo típico**: timestamps, possivelmente nulos se não houve modificação após a criação.

#### is\_deleted

* **Significado**: indicador que informa se a entrada de log está marcada como excluída.
* **Função**: campo técnico. Usado para a exclusão lógica de entradas.
* **Conteúdo típico**: valores booleanos, em que `False` indica entradas ativas e `True`, entradas excluídas.

#### is\_hidden

* **Significado**: indicador que informa se a entrada de log está oculta da exibição normal.
* **Função**: campo técnico. Usado para controlar a visibilidade das entradas de log.
* **Conteúdo típico**: valores booleanos, em que `False` indica entradas visíveis e `True`, entradas ocultas.

#### previous\_status

* **Significado**: status do documento antes da execução da ação.
* **Função**: campo descritivo. Fornece o estado do documento antes da ação registrada.
* **Conteúdo típico**: strings como `new`, `validating` e `running`, que representam estados de documentos.

#### current\_status

* **Significado**: status do documento após a execução da ação.
* **Função**: campo descritivo. Indica o estado atualizado do documento após a ação.
* **Conteúdo típico**: strings como `running`, `ready_for_validation` e `error`, que representam estados de documentos.

Esta documentação oferece uma visão geral da tabela `public.document_log`, detalhando a finalidade e a estrutura de cada coluna, o que é essencial para os desenvolvedores que gerenciam fluxos de documentos e mantêm trilhas de auditoria.
