# Status de ativação de script do documento

## Tabela `public.document_script_activation_status`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `sort_order`: inteiro
* `is_active`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `script_id`: interno

### Análise e descrição

## Documentação da tabela: `public.document_script_activation_status`

### Introdução

A tabela `public.document_script_activation_status` foi projetada para gerenciar o status de ativação dos scripts associados a documentos dentro de uma organização. Cada entrada da tabela corresponde a um script específico e ao seu status de ativação atual, o que potencialmente permite às organizações controlar e organizar a execução de scripts em relação aos seus documentos.

### Descrição das colunas

#### id

* **Significado**: esta coluna armazena um identificador único para cada entrada da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: identificador universalmente único (UUID), como `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Observação**: garante que cada registro possa ser identificado de forma única.

#### org\_id

* **Significado**: representa o identificador de uma organização.
* **Função**: chave estrangeira, provavelmente referenciando uma tabela de organizações.
* **Conteúdo típico**: UUID que identifica a organização, por exemplo, `23f3d697-7411-4c95-981d-faf089d266be`.
* **Observação**: vincula o status de ativação do script a uma organização específica.

#### sort\_order

* **Significado**: indica a ordem em que os scripts devem ser executados ou exibidos.
* **Função**: campo técnico.
* **Conteúdo típico**: valores inteiros que representam a sequência, como `0`.
* **Observação**: pode ser usado para priorizar ou organizar os scripts.

#### is\_active

* **Significado**: indica se um script está ativo no momento.
* **Função**: campo técnico.
* **Conteúdo típico**: valores booleanos, `True` ou `False`.
* **Observação**: determina se o script associado deve ser executado.

#### created\_by

* **Significado**: identificador do usuário que criou o registro.
* **Função**: chave estrangeira, provavelmente referenciando uma tabela de usuários.
* **Conteúdo típico**: valor inteiro que representa um ID de usuário, como `1`.
* **Observação**: registra o criador do registro para fins de auditoria.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora com fuso horário, por exemplo, `2023-11-20 10:44:14.685170+00:00`.
* **Observação**: fornece um timestamp de criação para fins de controle de registros.

#### last\_modified\_on

* **Significado**: timestamp da última modificação do registro.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora com fuso horário, ou `None` se nunca foi modificado.
* **Observação**: útil para acompanhar as alterações ao longo do tempo.

#### is\_deleted

* **Significado**: indica se o registro está marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: valores booleanos, `True` ou `False`.
* **Observação**: permite a exclusão lógica de registros sem remoção física do banco de dados.

#### script\_id

* **Significado**: identificador do script associado ao registro.
* **Função**: chave estrangeira, provavelmente referenciando uma tabela de scripts.
* **Conteúdo típico**: UUID que identifica o script, por exemplo, `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Observação**: vincula o status de ativação a um script específico.
