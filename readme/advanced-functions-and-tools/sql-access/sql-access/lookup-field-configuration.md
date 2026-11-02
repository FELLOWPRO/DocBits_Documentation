# Configuração de campos de lookup

## Tabela `public.lookup_field_configuration`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `lookup_rec_id`: interno
* `field_id`: interno
* `lookup_field`: interno
* `is_searchable`: booleano
* `parent_field_id`: interno
* `auto_trigger`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `search_operator`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Análise e descrição

## Documentação da tabela `public.lookup_field_configuration`

### Introdução

A tabela `public.lookup_field_configuration` parece ser uma tabela de configuração usada para definir e gerenciar campos de lookup em uma aplicação. A tabela inclui metadados sobre cada campo, como seu identificador, a organização associada, a possibilidade de pesquisa e informações de auditoria. Essa tabela provavelmente faz parte de um sistema maior para gerenciar campos dinâmicos ou definidos pelo usuário, permitindo consultas e configurações complexas.

### Descrição das colunas

#### `id`

* **Significado**: o identificador único de cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que identifica de forma única cada entrada de configuração.

#### `org_id`

* **Significado**: o identificador da organização à qual esta configuração está associada.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que representa a organização.

#### `lookup_rec_id`

* **Significado**: um identificador do registro de lookup específico ao qual esta configuração se aplica.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que referencia um registro de lookup específico.

#### `field_id`

* **Significado**: o identificador do campo que está sendo configurado.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que referencia um campo específico.

#### `lookup_field`

* **Significado**: o nome ou rótulo do campo que está sendo configurado.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o nome do campo, como "address\_1" ou "taxratefree".

#### `is_searchable`

* **Significado**: indica se o campo pode ser incluído em operações de pesquisa.
* **Função**: indicador de configuração.
* **Conteúdo típico**: um valor booleano (`True` ou `False`).

#### `parent_field_id`

* **Significado**: identificador do campo pai, se aplicável.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID ou `None` se não existir campo pai.

#### `auto_trigger`

* **Significado**: especifica se a configuração do campo deve acionar determinadas ações automaticamente.
* **Função**: indicador de configuração.
* **Conteúdo típico**: um valor booleano (`True` ou `False`).

#### `created_by`

* **Significado**: o identificador do usuário que criou a entrada de configuração.
* **Função**: campo de auditoria.
* **Conteúdo típico**: um número inteiro que representa o ID do usuário.

#### `created_on`

* **Significado**: o timestamp de quando a entrada de configuração foi criada.
* **Função**: campo de auditoria.
* **Conteúdo típico**: um timestamp com informações de fuso horário.

#### `last_modified_on`

* **Significado**: o timestamp da modificação mais recente da entrada de configuração.
* **Função**: campo de auditoria.
* **Conteúdo típico**: um timestamp com informações de fuso horário, ou `None` se nunca foi modificada.

#### `is_deleted`

* **Significado**: indica se a entrada de configuração foi marcada como excluída.
* **Função**: indicador de exclusão lógica.
* **Conteúdo típico**: um valor booleano (`True` ou `False`).

#### `deleted_on`

* **Significado**: o timestamp de quando a entrada de configuração foi marcada como excluída.
* **Função**: campo de auditoria.
* **Conteúdo típico**: um timestamp com informações de fuso horário, ou `None` se não foi excluída.

#### `search_operator`

* **Significado**: define o operador de pesquisa usado para o campo.
* **Função**: campo de configuração.
* **Conteúdo típico**: uma string como "contains", que indica o tipo de operação de pesquisa.

#### `last_modified_by`

* **Significado**: identificador do usuário que modificou a entrada de configuração pela última vez.
* **Função**: campo de auditoria.
* **Conteúdo típico**: uma string UUID ou `None` se nunca foi modificada.

#### `deleted_by`

* **Significado**: identificador do usuário que marcou a entrada como excluída.
* **Função**: campo de auditoria.
* **Conteúdo típico**: uma string UUID ou `None` se não foi excluída.

Esta documentação oferece uma visão detalhada da estrutura e da finalidade de cada coluna da tabela `public.lookup_field_configuration`, proporcionando aos desenvolvedores uma compreensão abrangente de como os campos de lookup são configurados e gerenciados no sistema.
