# Configuração de lookup

## Tabela `public.lookup_configuration`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type`: tipo de documento
* `lookup_dataset_name`: interno
* `lookup_name`: interno
* `conflict_handle`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `match_all`: booleano
* `last_modified_by`: interno
* `deleted_by`: interno
* `context`: interno
* `context_detail`: interno

### Análise e descrição

## Documentação técnica da tabela `public.lookup_configuration`

### Introdução

A tabela `public.lookup_configuration` foi projetada para armazenar as configurações de diversas operações de consulta de dados (lookup) dentro de uma organização. Ela inclui informações sobre a organização, o tipo de documentos envolvidos e os conjuntos de dados e nomes específicos usados nas consultas. A tabela também registra a criação e a modificação dessas configurações, bem como seu status atual (ativa ou excluída).

### Descrição das colunas

#### id

* **Significado**: identificador único de cada entrada de configuração de lookup na tabela.
* **Função**: chave primária que identifica cada linha de forma única.
* **Conteúdo típico**: valores UUID, por exemplo `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Significado**: representa a organização associada à configuração de lookup.
* **Função**: chave estrangeira, que se vincula a uma organização em outra tabela.
* **Conteúdo típico**: valores UUID que indicam identificadores de organizações, por exemplo `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Significado**: especifica o tipo de documento ao qual a configuração de lookup se aplica.
* **Função**: campo descritivo que indica o contexto da configuração.
* **Conteúdo típico**: strings como `'MEDI_ORDER'`, `'INVOICE'` etc.

#### lookup\_dataset\_name

* **Significado**: o nome do conjunto de dados usado para realizar as consultas.
* **Função**: campo descritivo usado para identificar conjuntos de dados.
* **Conteúdo típico**: strings descritivas como `'customer_tini'` e `'supplier'`.

#### lookup\_name

* **Significado**: o nome específico ou alias usado na operação de lookup.
* **Função**: campo descritivo que indica o nome operacional.
* **Conteúdo típico**: strings como `'customer_tini'` e `'supplier (copy)'`.

#### conflict\_handle

* **Significado**: indica a estratégia para tratar conflitos durante as consultas.
* **Função**: campo descritivo da estratégia de resolução de conflitos.
* **Conteúdo típico**: valores como `'BEST_SCORE'` e `'RETURN_NONE'`.

#### created\_by

* **Significado**: o ID do usuário que criou a configuração de lookup.
* **Função**: campo técnico para registrar o criador da entrada.
* **Conteúdo típico**: valores inteiros que representam IDs de usuários, por exemplo `1`.

#### created\_on

* **Significado**: timestamp de quando a configuração de lookup foi criada.
* **Função**: campo técnico para registrar o momento da criação.
* **Conteúdo típico**: timestamps, por exemplo `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Significado**: timestamp da última modificação feita na configuração de lookup.
* **Função**: campo técnico para registrar o momento da última atualização.
* **Conteúdo típico**: timestamps, normalmente `None` se não houve modificação.

#### is\_deleted

* **Significado**: indica se a configuração de lookup foi marcada como excluída.
* **Função**: campo booleano para o acompanhamento do status.
* **Conteúdo típico**: valores booleanos, `False` para entradas ativas.

#### deleted\_on

* **Significado**: timestamp de quando a configuração de lookup foi marcada como excluída.
* **Função**: campo técnico para registrar o momento da exclusão.
* **Conteúdo típico**: frequentemente uma data de espaço reservado padrão, por exemplo `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Significado**: especifica se o lookup deve corresponder a todas as condições.
* **Função**: campo booleano de configuração.
* **Conteúdo típico**: valores booleanos, normalmente `False`.

#### last\_modified\_by

* **Significado**: o ID do usuário que modificou a configuração de lookup pela última vez.
* **Função**: campo técnico para registrar o usuário que atualizou a entrada por último.
* **Conteúdo típico**: UUID ou identificador do usuário que modificou, frequentemente `None`.

#### deleted\_by

* **Significado**: o ID do usuário que marcou a configuração de lookup como excluída.
* **Função**: campo técnico para registrar o usuário responsável pela exclusão.
* **Conteúdo típico**: UUID ou identificador, frequentemente `None`.

#### context

* **Significado**: o contexto em que o lookup é aplicado, como uma seção de um documento.
* **Função**: campo descritivo do contexto operacional.
* **Conteúdo típico**: strings como `'header'`.

#### context\_detail

* **Significado**: detalhes adicionais sobre o contexto do lookup.
* **Função**: campo descritivo para informações de contexto ampliadas.
* **Conteúdo típico**: frequentemente `None`, usado para uma descrição adicional do contexto.
