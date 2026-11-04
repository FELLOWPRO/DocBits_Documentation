# Tabela de lookup

## Tabela `public.lookup_table`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `data_key`: interno
* `rec_id`: interno
* `prop_name`: interno
* `prop_value`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `prop_value_clean`: interno
* `version`: inteiro
* `deleted_on`: timestamp com fuso horário
* `sub_org_id`: interno

### Análise e descrição

## Documentação técnica de `public.lookup_table`

### Introdução

A `public.lookup_table` foi projetada para armazenar metadados sobre diversas propriedades associadas aos dados organizacionais. Ela provavelmente funciona como um armazenamento de chave-valor para diferentes atributos relacionados a clientes ou a outras entidades da organização. A tabela registra informações como nomes e valores de propriedades e o contexto (por exemplo, a organização e a suborganização a que pertencem), além de informações de auditoria, como os timestamps de criação e modificação.

### Descrição das colunas

#### `id`

* **Significado**: identificador único de cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que identifica de forma única cada entrada.

#### `org_id`

* **Significado**: identificador da organização à qual os dados pertencem.
* **Função**: chave estrangeira, provavelmente vinculada a uma tabela de organizações.
* **Conteúdo típico**: uma string UUID que representa a organização.

#### `data_key`

* **Significado**: uma chave que representa um conjunto de dados ou um contexto específico dentro da organização.
* **Função**: identificador contextual para agrupar propriedades relacionadas.
* **Conteúdo típico**: string alfanumérica que indica uma categoria, como `customer_amier`.

#### `rec_id`

* **Significado**: identificador de um registro específico dentro do conjunto de dados.
* **Função**: identificador contextual, possivelmente uma chave estrangeira para outra tabela.
* **Conteúdo típico**: string alfanumérica ou nulo para registros sem um identificador específico.

#### `prop_name`

* **Significado**: nome da propriedade ou do atributo.
* **Função**: campo descritivo que indica o que o valor da propriedade representa.
* **Conteúdo típico**: strings como 'Kundennummer', 'Versandanschrift', 'Kundenname' etc.

#### `prop_value`

* **Significado**: valor da propriedade descrita por `prop_name`.
* **Função**: campo descritivo que contém os dados ou o valor em si.
* **Conteúdo típico**: strings ou números que representam o valor da propriedade.

#### `created_by`

* **Significado**: identificador do usuário ou do sistema que criou o registro.
* **Função**: campo técnico para fins de auditoria.
* **Conteúdo típico**: número inteiro que representa o ID de um usuário.

#### `created_on`

* **Significado**: timestamp que indica quando o registro foi criado.
* **Função**: campo técnico para fins de auditoria.
* **Conteúdo típico**: data e hora com informações de fuso horário.

#### `last_modified_on`

* **Significado**: timestamp que indica a última vez em que o registro foi modificado.
* **Função**: campo técnico para fins de auditoria.
* **Conteúdo típico**: data e hora com informações de fuso horário, possivelmente nulo se não houve modificação.

#### `is_deleted`

* **Significado**: indicador que informa se o registro foi excluído.
* **Função**: campo técnico que indica a exclusão lógica.
* **Conteúdo típico**: valor booleano (`True` ou `False`).

#### `prop_value_clean`

* **Significado**: versão limpa ou processada de `prop_value`.
* **Função**: campo descritivo para armazenar um valor normalizado ou padronizado.
* **Conteúdo típico**: semelhante a `prop_value`, possivelmente nulo se não for aplicável.

#### `version`

* **Significado**: número de versão do registro.
* **Função**: campo técnico para o controle de versões.
* **Conteúdo típico**: número inteiro que representa a versão do registro.

#### `deleted_on`

* **Significado**: timestamp que indica quando o registro foi marcado como excluído.
* **Função**: campo técnico para fins de auditoria.
* **Conteúdo típico**: data e hora com informações de fuso horário, possivelmente nulo se não foi excluído.

#### `sub_org_id`

* **Significado**: identificador de uma suborganização dentro da organização principal.
* **Função**: chave estrangeira, potencialmente vinculada a uma tabela de suborganizações.
* **Conteúdo típico**: uma string UUID que representa a suborganização, possivelmente nulo se não for aplicável.
