# Alerta de status do documento

## Tabela `public.document_status_alert`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type_id`: interno
* `doc_type_key`: interno
* `doc_status`: interno
* `email_address`: texto
* `send_to_assigned_user`: booleano
* `delay_delta`: inteiro
* `delay_delta_type`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `name`: interno
* `is_recursive`: booleano
* `is_active`: booleano
* `priority`: interno
* `email_template_id`: interno

### Análise e descrição

## Documentação da tabela: `public.document_status_alert`

### Introdução

A tabela `public.document_status_alert` parece ter sido projetada para gerenciar alertas relacionados aos status de documentos dentro de uma organização. Com base nos nomes das colunas, a tabela armazena informações sobre diversos tipos de documentos e seus status, incluindo detalhes sobre notificações e a temporização dos alertas. Esta tabela provavelmente é usada para disparar alertas com base em determinados status e condições de documentos, possivelmente para notificar usuários ou escalar processos.

### Descrição das colunas

#### `id`

* **Significado**: identificador único de cada registro de alerta.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que identifica cada linha da tabela de forma única.

#### `org_id`

* **Significado**: identificador da organização associada ao alerta.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que faz referência a um registro de organização.

#### `doc_type_id`

* **Significado**: identificador do tipo de documento.
* **Função**: chave estrangeira (presumida).
* **Conteúdo típico**: normalmente um UUID, embora os dados de exemplo mostrem `None`, o que indica que este campo pode ser opcional.

#### `doc_type_key`

* **Significado**: chave que representa o tipo de documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string como 'INVOICE' ou 'XML\_INVOICE'.

#### `doc_status`

* **Significado**: status atual do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: strings de status descritivas, como 'validated\_pending\_approval' ou 'error'.

#### `email_address`

* **Significado**: endereço de e-mail para o qual os alertas são enviados.
* **Função**: campo de notificação.
* **Conteúdo típico**: um endereço de e-mail; pode ser `None` se nenhum e-mail for especificado.

#### `send_to_assigned_user`

* **Significado**: indica se o alerta deve ser enviado ao usuário atribuído ao documento.
* **Função**: campo booleano.
* **Conteúdo típico**: `True` ou `False`.

#### `delay_delta`

* **Significado**: intervalo de tempo pelo qual o alerta é adiado.
* **Função**: campo de temporização.
* **Conteúdo típico**: inteiro que representa a duração do atraso.

#### `delay_delta_type`

* **Significado**: unidade de tempo de `delay_delta`.
* **Função**: campo de temporização.
* **Conteúdo típico**: normalmente 'minutes'.

#### `created_by`

* **Significado**: identificador do usuário que criou o registro de alerta.
* **Função**: chave estrangeira (presumida).
* **Conteúdo típico**: inteiro que representa um ID de usuário.

#### `created_on`

* **Significado**: timestamp de quando o registro de alerta foi criado.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora com informações de fuso horário.

#### `last_modified_on`

* **Significado**: timestamp da última modificação do registro de alerta.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora com informações de fuso horário; pode ser `None` se não foi modificado.

#### `is_deleted`

* **Significado**: indica se o registro de alerta está marcado como excluído.
* **Função**: campo booleano.
* **Conteúdo típico**: `True` ou `False`.

#### `name`

* **Significado**: nome ou rótulo do alerta.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o nome do alerta.

#### `is_recursive`

* **Significado**: indica se o alerta deve se repetir em intervalos definidos.
* **Função**: campo booleano.
* **Conteúdo típico**: `True` ou `False`.

#### `is_active`

* **Significado**: indica se o alerta está ativo no momento.
* **Função**: campo booleano.
* **Conteúdo típico**: `True` ou `False`.

#### `priority`

* **Significado**: nível de prioridade do alerta.
* **Função**: campo descritivo.
* **Conteúdo típico**: pode ser strings como 'High', 'Medium', 'Low'; os dados de exemplo mostram `None`.

#### `email_template_id`

* **Significado**: identificador do modelo de e-mail usado para o alerta.
* **Função**: chave estrangeira (presumida).
* **Conteúdo típico**: normalmente um UUID; os dados de exemplo mostram `None`, o que indica que este campo pode ser opcional.
