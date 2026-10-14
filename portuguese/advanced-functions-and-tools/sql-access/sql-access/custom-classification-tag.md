# Tag de classificação personalizada

## Tabela `public.custom_classification_tag`

### Colunas

* `id`: inteiro
* `org_id`: ID da organização
* `name`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação técnica da tabela `public.custom_classification_tag`

### Introdução

A tabela `public.custom_classification_tag` foi projetada para gerenciar tags de classificação personalizadas dentro de uma organização. Ela registra informações essenciais sobre cada tag, incluindo sua associação com uma organização, os detalhes de criação e modificação e o status do seu ciclo de vida.

### Descrição das colunas

#### id

* **Significado**: um identificador único para cada tag de classificação.
* **Função**: chave primária.
* **Conteúdo típico**: um valor inteiro que identifica cada registro da tabela de forma única.

#### org\_id

* **Significado**: o identificador da organização à qual a tag de classificação pertence.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma cadeia de caracteres, provavelmente um UUID, que representa o ID único da organização.

#### name

* **Significado**: o nome ou rótulo da tag de classificação.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que indica o nome ou a descrição da tag. Pode ser uma string vazia se o nome não for informado.

#### created\_by

* **Significado**: o identificador do usuário que criou a tag de classificação.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um inteiro que representa o ID do usuário criador.

#### created\_on

* **Significado**: o timestamp que indica quando a tag de classificação foi criada.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp com fuso horário, que registra a data e a hora exatas da criação.

#### last\_modified\_on

* **Significado**: o timestamp da última modificação feita na tag de classificação.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp com fuso horário, que pode ser `None` se não houve modificações desde a criação.

#### is\_deleted

* **Significado**: um indicador que informa se a tag de classificação foi marcada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: um valor booleano (`True` ou `False`), em que `False` significa que a tag está ativa e `True` indica que ela foi excluída ou desativada.
