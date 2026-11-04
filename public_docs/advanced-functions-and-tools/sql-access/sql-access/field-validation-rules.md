# Regras de validação de campos

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `field_id`: interno
* `doc_type`: tipo de documento
* `is_sub_doc_type_field`: booleano
* `profile`: interno
* `field_name`: interno
* `field_length`: inteiro
* `field_label`: interno
* `is_required`: booleano
* `is_readonly`: booleano
* `is_hidden`: booleano
* `force_validation`: booleano
* `validation_pattern`: interno
* `confidence_threshold`: inteiro
* `match_score_threshold`: inteiro
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `additional_attributes`: texto

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.field_validation_rules`

## Introdução

A tabela `public.field_validation_rules` parece armazenar metadados e regras de validação para campos associados a vários tipos de documentos dentro de uma organização. Provavelmente é usada para garantir a integridade e a consistência dos dados em formulários ou documentos, especificando requisitos como a obrigatoriedade do campo, seu comprimento, sua visibilidade e quaisquer padrões de validação que devam ser aplicados.

## Descrição das colunas

### id
- **Significado**: identificador único de cada regra de validação de campo.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica um registro de forma única.

### org_id
- **Significado**: identificador da organização à qual a regra de validação se aplica.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que referencia uma organização específica.

### field_id
- **Significado**: identificador do campo específico ao qual a regra de validação está associada.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que referencia um campo específico.

### doc_type
- **Significado**: especifica o tipo de documento ao qual a regra de validação do campo está associada.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que indica o tipo de documento (por exemplo, `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Significado**: indica se o campo faz parte de um subtipo de documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### profile
- **Significado**: representa o perfil ou o contexto em que a validação do campo é aplicada.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string como `DEFAULT`.

### field_name
- **Significado**: o nome do campo para o qual a regra de validação é definida.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que representa o nome do campo (por exemplo, `Test`).

### field_length
- **Significado**: o comprimento máximo permitido para o conteúdo do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: um número inteiro que especifica o limite de caracteres.

### field_label
- **Significado**: o rótulo ou nome de exibição do campo na interface do usuário.
- **Função**: campo descritivo.
- **Conteúdo típico**: normalmente nulo nos dados de exemplo.

### is_required
- **Significado**: indica se o campo é obrigatório para o documento.
- **Função**: indicador de restrição.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### is_readonly
- **Significado**: especifica se o campo é editável ou somente leitura.
- **Função**: indicador de restrição.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### is_hidden
- **Significado**: indica se o campo deve ser ocultado da interface do usuário.
- **Função**: indicador de restrição.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### force_validation
- **Significado**: determina se a validação deve ser aplicada independentemente de outras condições.
- **Função**: indicador de restrição.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### validation_pattern
- **Significado**: um padrão (provavelmente uma expressão regular) com o qual o conteúdo do campo deve corresponder.
- **Função**: regra de validação.
- **Conteúdo típico**: normalmente nulo nos dados de exemplo.

### confidence_threshold
- **Significado**: o nível mínimo de confiança exigido para a validação do campo.
- **Função**: restrição de validação.
- **Conteúdo típico**: um valor inteiro que representa o limite de confiança.

### match_score_threshold
- **Significado**: a pontuação mínima de correspondência exigida para a validação do conteúdo do campo.
- **Função**: restrição de validação.
- **Conteúdo típico**: um valor inteiro que representa o limite da pontuação de correspondência.

### created_by
- **Significado**: identificador do usuário que criou esta regra de validação.
- **Função**: campo descritivo.
- **Conteúdo típico**: um número inteiro que representa o ID do usuário.

### created_on
- **Significado**: timestamp que indica quando a regra de validação foi criada.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário.

### last_modified_on
- **Significado**: timestamp que indica a última modificação da regra de validação.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário; pode ser nulo se nunca foi modificada.

### is_deleted
- **Significado**: indica se a regra de validação foi marcada como excluída.
- **Função**: indicador de exclusão lógica.
- **Conteúdo típico**: valor booleano (`True` ou `False`).

### additional_attributes
- **Significado**: armazena atributos extras ou metadados associados à regra de validação do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: texto, frequentemente nulo nos dados de exemplo.
```
