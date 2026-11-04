# E-mails recebidos

## Tabela `public.inbound_emails`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `is_active`: booleano
* `email_senders`: interno
* `email_receiver`: interno
* `token`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_by`: interno
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_by`: interno
* `deleted_on`: timestamp com fuso horário

### Análise e descrição

## Documentação técnica: tabela `public.inbound_emails`

### Introdução

A tabela `public.inbound_emails` foi projetada para armazenar e gerenciar informações sobre e-mails recebidos por uma organização. Essa tabela registra os detalhes do remetente e do destinatário, o status do e-mail e vários metadados relacionados à criação, modificação e exclusão de registros. Ela parece fazer parte de um sistema de gerenciamento de e-mails dentro de uma organização, possivelmente usado para o acompanhamento das comunicações recebidas por e-mail.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string única, provavelmente um UUID, como `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Significado**: identificador da organização associada ao e-mail recebido.
* **Função**: chave estrangeira, que se vincula a outra tabela com os detalhes da organização.
* **Conteúdo típico**: uma string única, provavelmente um UUID, como `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Significado**: indica se o registro de e-mail está ativo no momento.
* **Função**: indicador de status.
* **Conteúdo típico**: um valor booleano, `True` ou `False`.

#### email\_senders

* **Significado**: armazena informações sobre o(s) remetente(s) do e-mail.
* **Função**: campo de dados.
* **Conteúdo típico**: uma string semelhante a JSON com os detalhes dos remetentes, por exemplo `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Significado**: endereço de e-mail do destinatário principal.
* **Função**: campo de dados.
* **Conteúdo típico**: uma string com um endereço de e-mail. No exemplo, está vazia, o que sugere um uso opcional ou variável.

#### token

* **Significado**: um token associado ao e-mail, possivelmente para autenticação ou identificação.
* **Função**: campo de autenticação ou rastreamento.
* **Conteúdo típico**: uma string longa gerada aleatoriamente.

#### created\_by

* **Significado**: identificador do usuário que criou o registro.
* **Função**: chave estrangeira, que se vincula a uma tabela de usuários ou funcionários.
* **Conteúdo típico**: um número inteiro que representa o ID de um usuário, como `1`.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo de metadados.
* **Conteúdo típico**: um valor de data e hora com informações de fuso horário, por exemplo `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Significado**: identificador do usuário que modificou o registro pela última vez.
* **Função**: chave estrangeira, que se vincula a uma tabela de usuários ou funcionários.
* **Conteúdo típico**: pode ser um ID de usuário ou nulo se nenhuma modificação foi feita.

#### last\_modified\_on

* **Significado**: timestamp de quando o registro foi modificado pela última vez.
* **Função**: campo de metadados.
* **Conteúdo típico**: um valor de data e hora que indica o momento da última modificação, por exemplo `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Significado**: indica se o registro de e-mail foi marcado como excluído.
* **Função**: indicador de status.
* **Conteúdo típico**: um valor booleano, `True` ou `False`.

#### deleted\_by

* **Significado**: identificador do usuário que marcou o registro como excluído.
* **Função**: chave estrangeira, que se vincula a uma tabela de usuários ou funcionários.
* **Conteúdo típico**: pode ser um ID de usuário ou nulo se o registro não foi excluído.

#### deleted\_on

* **Significado**: timestamp de quando o registro foi marcado como excluído.
* **Função**: campo de metadados.
* **Conteúdo típico**: um valor de data e hora que indica o momento da exclusão, ou uma data padrão se não for aplicável, por exemplo `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
