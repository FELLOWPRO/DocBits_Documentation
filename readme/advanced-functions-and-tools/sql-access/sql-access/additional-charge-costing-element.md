# Elemento de custeio de encargo adicional

## Tabela `public.additional_charge_costing_element`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `costing_element`: interno
* `description`: interno
* `charge_type`: interno
* `distribution_method`: interno
* `distribution_type`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `sub_org_id`: interno
* `charge_count`: inteiro
* `charge_icon`: interno
* `charge_category`: interno
* `charge_sequence_number`: inteiro
* `charge_operator`: inteiro
* `last_modified_by`: interno
* `deleted_by`: interno

### Análise e descrição

## Documentação da tabela: `public.additional_charge_costing_element`

### Introdução

A tabela `public.additional_charge_costing_element` foi projetada para gerenciar e armazenar informações sobre diversos elementos de custeio de encargos adicionais dentro de uma organização. Isso inclui dados sobre o tipo de encargo, a forma como é distribuído e metadados administrativos, como detalhes de criação e modificação. Esta tabela provavelmente é usada para a gestão financeira e operacional de uma organização, com foco em custos adicionais que precisam ser acompanhados e analisados.

### Descrição das colunas

#### id

* **Significado**: esta coluna armazena um identificador único para cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma sequência alfanumérica única que identifica cada registro de elemento de custeio.

#### org\_id

* **Significado**: o identificador da organização à qual este elemento de custeio pertence.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um UUID que representa a organização.

#### costing\_element

* **Significado**: um identificador ou código do elemento de custeio.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma sequência alfanumérica que representa o elemento de custeio específico.

#### description

* **Significado**: uma descrição textual do elemento de custeio.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma breve explicação textual do elemento de custeio.

#### charge\_type

* **Significado**: o tipo de encargo associado a este elemento de custeio.
* **Função**: campo descritivo.
* **Conteúdo típico**: um código ou texto curto que indica o tipo de encargo.

#### distribution\_method

* **Significado**: método pelo qual o encargo é distribuído.
* **Função**: campo descritivo.
* **Conteúdo típico**: um código ou texto curto que indica o método de distribuição.

#### distribution\_type

* **Significado**: tipo de distribuição do encargo.
* **Função**: campo descritivo.
* **Conteúdo típico**: um código ou texto curto que indica o tipo de distribuição.

#### created\_by

* **Significado**: identificador do usuário que criou o registro.
* **Função**: campo administrativo.
* **Conteúdo típico**: um inteiro que representa o ID do usuário.

#### created\_on

* **Significado**: timestamp que indica quando o registro foi criado.
* **Função**: campo administrativo.
* **Conteúdo típico**: um timestamp com informações de fuso horário.

#### last\_modified\_on

* **Significado**: timestamp da última modificação feita no registro.
* **Função**: campo administrativo.
* **Conteúdo típico**: um timestamp com informações de fuso horário.

#### is\_deleted

* **Significado**: indica se o registro está marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano (`True` ou `False`).

#### deleted\_on

* **Significado**: timestamp de quando o registro foi marcado como excluído.
* **Função**: campo administrativo.
* **Conteúdo típico**: um timestamp com informações de fuso horário ou `None` se não foi excluído.

#### sub\_org\_id

* **Significado**: identificador de uma suborganização relacionada ao elemento de custeio.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um UUID que representa a suborganização.

#### charge\_count

* **Significado**: o número de encargos associados ao elemento de custeio.
* **Função**: campo descritivo.
* **Conteúdo típico**: um inteiro que representa a contagem de encargos.

#### charge\_icon

* **Significado**: ícone ou símbolo associado ao encargo.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o ícone, provavelmente um caminho ou identificador.

#### charge\_category

* **Significado**: a categoria à qual o encargo pertence.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa a categoria do encargo.

#### charge\_sequence\_number

* **Significado**: número de sequência para ordenar os encargos.
* **Função**: campo descritivo.
* **Conteúdo típico**: um inteiro usado para sequenciar os encargos.

#### charge\_operator

* **Significado**: identificador do operador responsável pelo encargo.
* **Função**: campo descritivo.
* **Conteúdo típico**: um inteiro que representa o ID do operador.

#### last\_modified\_by

* **Significado**: identificador do usuário que modificou o registro pela última vez.
* **Função**: campo administrativo.
* **Conteúdo típico**: uma string que representa o ID do usuário, possivelmente `None` se nunca foi modificado.

#### deleted\_by

* **Significado**: identificador do usuário que marcou o registro como excluído.
* **Função**: campo administrativo.
* **Conteúdo típico**: uma string que representa o ID do usuário, possivelmente `None` se não foi excluído.
