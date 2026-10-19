# Modelo de e-mail

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `name`: interno
* `email_type`: interno
* `value`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `subject`: interno
* `last_modified_by`: interno
* `deleted_by`: interno
* `doc_type`: tipo de documento

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.email_template`

## Introdução

A tabela `public.email_template` foi projetada para armazenar modelos de e-mail usados no sistema. Esses modelos estão associados a diferentes organizações e provavelmente são usados para enviar comunicações padronizadas por e-mail. A tabela contém metadados sobre os modelos, incluindo detalhes de criação e modificação, e também registra se um modelo foi excluído.

## Descrição das colunas

### id
- **Significado**: identificador único de cada modelo de e-mail.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID, como `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Observação**: serve como identificador principal do registro do modelo.

### org_id
- **Significado**: identificador da organização associada ao modelo de e-mail.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID.
- **Observação**: vincula o modelo a uma organização específica.

### name
- **Significado**: o nome do modelo de e-mail.
- **Função**: campo descritivo.
- **Conteúdo típico**: texto descritivo como `Supplier Magic Link Email`.
- **Observação**: usado para identificar a finalidade do modelo.

### email_type
- **Significado**: tipo ou categoria do modelo de e-mail.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings como `supplier_invite`.
- **Observação**: indica o contexto ou o uso do modelo.

### value
- **Significado**: o conteúdo do modelo de e-mail, normalmente em formato HTML.
- **Função**: campo de conteúdo.
- **Conteúdo típico**: string HTML contendo o layout e o conteúdo do e-mail.
- **Observação**: é o modelo efetivamente usado nos e-mails.

### created_by
- **Significado**: identificador do usuário que criou o modelo.
- **Função**: campo de metadados.
- **Conteúdo típico**: um número inteiro que representa o ID de um usuário.
- **Observação**: registra quem criou o modelo.

### created_on
- **Significado**: timestamp de quando o modelo foi criado.
- **Função**: campo de metadados.
- **Conteúdo típico**: um timestamp como `2024-07-18 13:29:59 UTC`.
- **Observação**: registra a data e a hora de criação.

### last_modified_on
- **Significado**: timestamp da última modificação do modelo.
- **Função**: campo de metadados.
- **Conteúdo típico**: um timestamp.
- **Observação**: registra a atualização mais recente do modelo.

### is_deleted
- **Significado**: indica se o modelo está marcado como excluído.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano, `True` ou `False`.
- **Observação**: usado para a exclusão lógica do modelo.

### deleted_on
- **Significado**: timestamp de quando o modelo foi marcado como excluído.
- **Função**: campo de metadados.
- **Conteúdo típico**: um timestamp ou `None` se não foi excluído.
- **Observação**: registra quando o modelo foi excluído.

### subject
- **Significado**: a linha de assunto do modelo de e-mail.
- **Função**: campo de conteúdo.
- **Conteúdo típico**: texto como `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Observação**: usado como assunto do e-mail quando o modelo é enviado.

### last_modified_by
- **Significado**: identificador do usuário que modificou o modelo pela última vez.
- **Função**: campo de metadados.
- **Conteúdo típico**: um identificador de usuário.
- **Observação**: registra quem modificou o modelo por último.

### deleted_by
- **Significado**: identificador do usuário que marcou o modelo como excluído.
- **Função**: campo de metadados.
- **Conteúdo típico**: um identificador de usuário.
- **Observação**: registra quem excluiu o modelo.

### doc_type
- **Significado**: tipo ou formato do documento relacionado ao modelo.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings que indicam o tipo de documento.
- **Observação**: pode estar relacionado ao formato ou à categoria do conteúdo do e-mail.
```
