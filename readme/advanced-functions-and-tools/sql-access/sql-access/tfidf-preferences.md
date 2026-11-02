# Preferências TF-IDF

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `tfidf_id`: interno
* `pref_key`: interno
* `pref_value`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_by`: interno
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_by`: interno
* `deleted_on`: timestamp com fuso horário
* `supplier_id`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.tfidf_preferences`

## Introdução

A tabela `public.tfidf_preferences` parece ter sido projetada para armazenar preferências relacionadas a configurações ou modelos TF-IDF (Term Frequency-Inverse Document Frequency). Essa tabela contém informações sobre preferências específicas definidas por organizações, incluindo as chaves de preferência e seus valores correspondentes, além de metadados sobre as atividades de criação, modificação e exclusão.

## Descrição das colunas

### id
- **Significado**: um identificador único de cada registro da tabela.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que representa o ID único de uma entrada de preferência.

### org_id
- **Significado**: identificador da organização associada à preferência.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que vincula a preferência a uma organização específica.

### tfidf_id
- **Significado**: identificador da configuração ou do modelo TF-IDF específico.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa a configuração TF-IDF vinculada.

### pref_key
- **Significado**: a chave ou o nome da configuração de preferência.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que representa o nome da preferência, como 'USE_ETEXT_IF_AVAILABLE' ou 'AI_MODEL'.

### pref_value
- **Significado**: o valor associado à chave de preferência.
- **Função**: campo descritivo.
- **Conteúdo típico**: um valor em string ou texto que corresponde à chave de preferência, por exemplo 'true', 'false' ou 'Full'.

### created_by
- **Significado**: identificador do usuário que criou a entrada de preferência.
- **Função**: campo descritivo.
- **Conteúdo típico**: um número inteiro que representa o ID do usuário criador.

### created_on
- **Significado**: timestamp de quando a entrada de preferência foi criada.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que indica a data e a hora de criação.

### last_modified_by
- **Significado**: identificador do usuário que modificou a entrada de preferência pela última vez.
- **Função**: campo descritivo.
- **Conteúdo típico**: um UUID que representa o ID do usuário que modificou a entrada por último, se aplicável.

### last_modified_on
- **Significado**: timestamp da última modificação da entrada de preferência.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que mostra a data e a hora da última modificação.

### is_deleted
- **Significado**: indicador que informa se a entrada de preferência foi marcada como excluída.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor booleano; `True` se a entrada foi excluída e `False` caso contrário.

### deleted_by
- **Significado**: identificador do usuário que marcou a entrada de preferência como excluída.
- **Função**: campo descritivo.
- **Conteúdo típico**: um UUID que representa o ID do usuário que excluiu a entrada, se aplicável.

### deleted_on
- **Significado**: timestamp de quando a entrada de preferência foi marcada como excluída.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que indica quando a entrada foi excluída.

### supplier_id
- **Significado**: identificador do fornecedor associado à preferência.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa o fornecedor vinculado à preferência.

Esta documentação oferece uma visão geral detalhada da finalidade e da estrutura da tabela `public.tfidf_preferences`, ajudando os desenvolvedores a entender como interagir com esses dados e utilizá-los de forma eficaz.
```
