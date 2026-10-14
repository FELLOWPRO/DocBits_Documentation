# Tipo de documento da organização

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `document_type_id`: interno
* `document_type_key`: interno
* `document_locale`: interno
* `classification_method`: interno
* `is_active`: booleano
* `extraction_type`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `sub_org_id`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.organisation_document_type`

## Introdução

A tabela `public.organisation_document_type` foi projetada para gerenciar e armazenar informações sobre os diversos tipos de documentos associados às organizações. Isso inclui detalhes como a chave do tipo de documento, o idioma/região (locale), os métodos de classificação e o status do tipo de documento (ativo, excluído etc.). Ela parece servir como um mapeamento entre as organizações e os tipos de documentos que elas utilizam ou gerenciam, junto com metadados sobre esses documentos.

## Descrição das colunas

### id
- **Significado**: identificador único de cada registro da tabela.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica de forma única uma entrada de tipo de documento.
- **Observação**: essencial para distinguir cada registro.

### org_id
- **Significado**: identificador da organização relacionada ao tipo de documento.
- **Função**: chave estrangeira, provavelmente referenciando uma tabela de organizações.
- **Conteúdo típico**: uma string UUID.
- **Observação**: conecta o tipo de documento a uma organização específica.

### document_type_id
- **Significado**: identificador do tipo de documento.
- **Função**: chave estrangeira, possivelmente vinculada a uma tabela de referência de tipos de documentos.
- **Conteúdo típico**: uma string UUID.
- **Observação**: permite o mapeamento para tipos de documentos específicos.

### document_type_key
- **Significado**: uma chave ou código que representa o tipo de documento.
- **Função**: campo descritivo para a classificação do tipo de documento.
- **Conteúdo típico**: uma string que funciona como identificador ou rótulo do tipo de documento.
- **Observação**: usada para identificar o tipo de documento em uma forma legível por pessoas.

### document_locale
- **Significado**: configuração de idioma/região (locale) do tipo de documento.
- **Função**: campo descritivo para a especificação do locale.
- **Conteúdo típico**: uma string, frequentemente 'auto', que indica a determinação automática do locale.
- **Observação**: útil para fins de internacionalização e localização.

### classification_method
- **Significado**: método usado para classificar o tipo de documento.
- **Função**: campo descritivo que indica como o documento é classificado.
- **Conteúdo típico**: uma string, frequentemente 'auto', que sugere a classificação automática.
- **Observação**: importante para entender o processo de classificação.

### is_active
- **Significado**: status que indica se o tipo de documento está ativo.
- **Função**: campo booleano de status.
- **Conteúdo típico**: `True` ou `False`.
- **Observação**: determina se o tipo de documento está em uso no momento.

### extraction_type
- **Significado**: tipo de método de extração usado para o documento.
- **Função**: campo descritivo do processo de extração.
- **Conteúdo típico**: strings como 'FIX_COORDINATES', 'FLEX_COORDINATES' ou `None`.
- **Observação**: dá uma ideia de como os dados são extraídos dos documentos.

### created_by
- **Significado**: identificador do usuário que criou o registro.
- **Função**: campo técnico para fins de auditoria.
- **Conteúdo típico**: um número inteiro que representa o ID de um usuário.
- **Observação**: útil para o rastreamento de alterações e a responsabilização.

### created_on
- **Significado**: timestamp de quando o registro foi criado.
- **Função**: campo técnico para fins de auditoria.
- **Conteúdo típico**: um timestamp com fuso horário.
- **Observação**: importante para acompanhar a data e a hora de criação do registro.

### last_modified_on
- **Significado**: timestamp da última modificação do registro.
- **Função**: campo técnico para fins de auditoria.
- **Conteúdo típico**: um timestamp com fuso horário.
- **Observação**: útil para acompanhar as atualizações e as alterações do registro.

### is_deleted
- **Significado**: status que indica se o registro foi marcado como excluído.
- **Função**: campo booleano de status.
- **Conteúdo típico**: `True` ou `False`.
- **Observação**: auxilia na implementação da funcionalidade de exclusão lógica.

### sub_org_id
- **Significado**: identificador de uma suborganização relacionada ao tipo de documento.
- **Função**: possível chave estrangeira, que adiciona uma estrutura organizacional hierárquica.
- **Conteúdo típico**: uma string UUID ou `None`.
- **Observação**: fornece contexto adicional para a estrutura da organização.

```
