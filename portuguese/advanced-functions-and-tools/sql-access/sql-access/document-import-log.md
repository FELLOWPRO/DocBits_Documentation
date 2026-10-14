# Log de importação de documentos

## Colunas

* `id`: inteiro
* `org_id`: ID da organização
* `sub_org_id`: interno
* `original_filename`: interno
* `filename`: interno
* `imported_on`: interno
* `source_type`: interno
* `source`: interno
* `success`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `import_id`: texto
* `extra_data`: texto
* `doc_id`: interno
* `email_connection_id`: inteiro
* `subject`: interno
* `body`: texto
* `sender`: interno
* `error_resp`: interno
* `source_received_on`: timestamp com fuso horário

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.document_import_log`

## Introdução

A tabela `public.document_import_log` foi projetada para registrar os detalhes das importações de documentos no sistema. Ela captura informações sobre cada documento, incluindo sua origem, o status da importação e os metadados relacionados. Esta tabela é essencial para acompanhar as atividades de importação de documentos e diagnosticar problemas que possam surgir durante o processo de importação.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada entrada do log de importação.
- **Função**: chave primária
- **Conteúdo típico**: valores inteiros sequenciais que identificam cada registro de forma única.

### org_id
- **Significado**: o identificador da organização associada à importação.
- **Função**: chave estrangeira
- **Conteúdo típico**: UUID ou string identificadora única semelhante que representa a organização.

### sub_org_id
- **Significado**: o identificador de uma suborganização ou departamento dentro da organização principal.
- **Função**: chave estrangeira
- **Conteúdo típico**: UUID ou string identificadora única semelhante; pode ser `None` se não for aplicável.

### original_filename
- **Significado**: o nome original do arquivo do documento no momento do upload.
- **Função**: campo descritivo
- **Conteúdo típico**: string que representa o nome do arquivo, por exemplo, `anton_invoice-1.pdf`.

### filename
- **Significado**: o nome do arquivo do documento depois de processado ou armazenado no sistema.
- **Função**: campo descritivo
- **Conteúdo típico**: string que representa o nome do arquivo, frequentemente idêntico a `original_filename`.

### imported_on
- **Significado**: a data e a hora em que o documento foi importado.
- **Função**: campo descritivo
- **Conteúdo típico**: timestamp no formato ISO 8601.

### source_type
- **Significado**: o tipo de origem a partir da qual o documento foi importado.
- **Função**: campo descritivo
- **Conteúdo típico**: string, por exemplo, `EMAIL`, que indica o tipo de origem.

### source
- **Significado**: informações detalhadas sobre a origem da importação.
- **Função**: campo descritivo
- **Conteúdo típico**: string que detalha a origem, por exemplo, `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Significado**: indica se a importação foi bem-sucedida.
- **Função**: campo de status
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### created_by
- **Significado**: o identificador do usuário que iniciou a importação.
- **Função**: chave estrangeira
- **Conteúdo típico**: inteiro que representa o ID do usuário.

### created_on
- **Significado**: a data e a hora em que a entrada do log de importação foi criada.
- **Função**: campo técnico
- **Conteúdo típico**: timestamp com fuso horário.

### last_modified_on
- **Significado**: a data e a hora da última modificação da entrada do log de importação.
- **Função**: campo técnico
- **Conteúdo típico**: timestamp com fuso horário; pode ser `None` se não foi modificado.

### is_deleted
- **Significado**: indica se a entrada do log de importação foi marcada como excluída.
- **Função**: campo de status
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### import_id
- **Significado**: um identificador único do processo de importação.
- **Função**: campo técnico
- **Conteúdo típico**: string ou texto que representa um ID de processo único.

### extra_data
- **Significado**: metadados adicionais relacionados à importação.
- **Função**: campo descritivo
- **Conteúdo típico**: string JSON com dados extras, como data, remetente, assunto e contagem.

### doc_id
- **Significado**: o identificador do documento.
- **Função**: chave estrangeira
- **Conteúdo típico**: UUID ou string identificadora única semelhante; pode ser `None`.

### email_connection_id
- **Significado**: o identificador da conexão de e-mail usada na importação.
- **Função**: chave estrangeira
- **Conteúdo típico**: inteiro que representa o ID da conexão de e-mail; pode ser `None`.

### subject
- **Significado**: a linha de assunto do e-mail do qual o documento foi importado.
- **Função**: campo descritivo
- **Conteúdo típico**: string que representa o assunto do e-mail.

### body
- **Significado**: o conteúdo do corpo do e-mail do qual o documento foi importado.
- **Função**: campo descritivo
- **Conteúdo típico**: texto com o conteúdo do corpo do e-mail; pode ser `None`.

### sender
- **Significado**: o endereço de e-mail do remetente do documento.
- **Função**: campo descritivo
- **Conteúdo típico**: string com o endereço de e-mail do remetente.

### error_resp
- **Significado**: resposta de erro ou mensagem de erro, caso a importação tenha falhado.
- **Função**: campo de status
- **Conteúdo típico**: string com os detalhes do erro; pode ser `None`.

### source_received_on
- **Significado**: a data e a hora em que o documento foi recebido da origem.
- **Função**: campo descritivo
- **Conteúdo típico**: timestamp com fuso horário.

Esta documentação oferece uma visão geral detalhada da tabela `public.document_import_log` e de suas colunas, que são essenciais para entender e gerenciar as importações de documentos no sistema.
```
