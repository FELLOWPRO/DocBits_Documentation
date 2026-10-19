# Credenciais de API

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `sub_org_id`: interno
* `title`: interno
* `credentials_type`: interno
* `credentials_json`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `last_modified_by`: interno
* `deleted_by`: interno

## Análise e descrição

```markdown
# Documentação da tabela: `public.api_credentials`

## Introdução

A tabela `public.api_credentials` foi projetada para armazenar e gerenciar informações de credenciais de API. Esta tabela é fundamental para que as organizações tratem com segurança seus dados de autenticação de API, garantindo que os diversos serviços possam interagir entre si usando as credenciais corretas. Ela inclui informações sobre o tipo de credencial, a organização à qual pertence e metadados sobre sua criação e modificação.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada entrada da tabela.
- **Função**: chave primária.
- **Conteúdo típico**: um identificador universalmente único (UUID) que representa um conjunto específico de credenciais de API.

### org_id
- **Significado**: identificador da organização proprietária das credenciais.
- **Função**: chave estrangeira.
- **Conteúdo típico**: um UUID que faz referência ao registro da organização em outra tabela.

### sub_org_id
- **Significado**: identificador de uma suborganização dentro da organização principal.
- **Função**: chave estrangeira (opcional).
- **Conteúdo típico**: pode conter um UUID que faz referência a uma suborganização, ou `None`.

### title
- **Significado**: um título descritivo para as credenciais de API.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string como "supplier_auth" que indica a finalidade ou o uso das credenciais.

### credentials_type
- **Significado**: especifica o tipo de credenciais armazenadas.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string como "ionapi" que indica o formato ou o protocolo usado pelas credenciais.

### credentials_json
- **Significado**: um objeto JSON com informações detalhadas das credenciais.
- **Função**: campo técnico.
- **Conteúdo típico**: string JSON com diversos pares chave-valor que detalham os parâmetros de autenticação.

### created_by
- **Significado**: ID do usuário que criou o registro das credenciais.
- **Função**: campo técnico.
- **Conteúdo típico**: um inteiro que representa o ID do usuário.

### created_on
- **Significado**: timestamp que indica quando as credenciais foram criadas.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor de data e hora com fuso horário, por exemplo, `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Significado**: timestamp que indica o momento da última modificação das credenciais.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor de data e hora com fuso horário, ou `None` se nunca foi modificado.

### is_deleted
- **Significado**: indicador que informa se as credenciais estão marcadas como excluídas.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor booleano, em que `False` indica credenciais ativas.

### deleted_on
- **Significado**: timestamp que indica quando as credenciais foram marcadas como excluídas.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor de data e hora com fuso horário, ou `None` se não foi excluído.

### last_modified_by
- **Significado**: identificador do usuário que modificou as credenciais pela última vez.
- **Função**: campo técnico.
- **Conteúdo típico**: uma cadeia de caracteres que representa o ID do usuário, ou `None`.

### deleted_by
- **Significado**: identificador do usuário que marcou as credenciais como excluídas.
- **Função**: campo técnico.
- **Conteúdo típico**: uma cadeia de caracteres que representa o ID do usuário, ou `None`.
```
