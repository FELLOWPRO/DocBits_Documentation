# Instância de lote

## Tabela `public.batch_instance`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação da tabela: `public.batch_instance`

### Introdução

A tabela `public.batch_instance` foi projetada para armazenar informações sobre diversas instâncias de lote dentro de uma organização. Ela contém metadados importantes sobre cada instância, incluindo sua identificação única, a organização à qual pertence e os detalhes de criação e modificação. Esta tabela é essencial para acompanhar o ciclo de vida e o gerenciamento das instâncias de lote, provavelmente em um aplicativo de software que trabalha com processamento em lote.

### Colunas

#### `id`

* **Significado**: esta coluna armazena o identificador único de cada instância de lote.
* **Função**: chave primária (`id`).
* **Conteúdo típico**: uma string UUID que identifica cada instância de lote de forma única, por exemplo, `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Significado**: esta coluna armazena o identificador da organização associada à instância de lote.
* **Função**: chave estrangeira (`org_id`).
* **Conteúdo típico**: uma string UUID que representa a organização, por exemplo, `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Significado**: esta coluna indica o usuário ou a entidade do sistema que criou a instância de lote.
* **Função**: possivelmente uma chave estrangeira, que faz referência a uma tabela de usuários ou similar.
* **Conteúdo típico**: um inteiro que representa o ID do criador, por exemplo, `1`.

#### `created_on`

* **Significado**: esta coluna registra o timestamp de quando a instância de lote foi criada.
* **Função**: campo técnico para fins de auditoria e acompanhamento.
* **Conteúdo típico**: um timestamp com fuso horário, por exemplo, `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Significado**: esta coluna registra o timestamp da última modificação feita na instância de lote.
* **Função**: campo técnico para auditoria de alterações.
* **Conteúdo típico**: normalmente nulo ou um timestamp com fuso horário, caso tenham ocorrido modificações.

#### `is_deleted`

* **Significado**: esta coluna indica se a instância de lote está marcada como excluída.
* **Função**: campo técnico para exclusão lógica.
* **Conteúdo típico**: um valor booleano, normalmente `False` se a instância estiver ativa, por exemplo, `False`.

Esta documentação oferece uma visão geral completa da tabela `public.batch_instance`, detalhando a finalidade e a estrutura de cada coluna, o que é fundamental para desenvolvedores que trabalham com este modelo de dados.
