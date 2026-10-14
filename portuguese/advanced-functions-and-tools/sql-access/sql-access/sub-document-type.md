# Subtipo de documento

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `name`: interno
* `title`: interno
* `translation_key`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

## Análise e descrição

```markdown
# Tabela `public.sub_document_type`

## Introdução

A tabela `sub_document_type` foi projetada para armazenar informações detalhadas sobre vários subtipos de documentos dentro de uma organização. Isso inclui identificadores únicos, associações organizacionais, nomes descritivos e metadados relacionados à criação e à modificação desses subtipos de documentos. A tabela também mantém o status de exclusão lógica dos registros.

## Descrição das colunas

### id
- **Significado**: esta coluna armazena o identificador único de cada subtipo de documento.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica de forma única um registro de subtipo de documento (por exemplo, `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Significado**: esta coluna indica a organização à qual o subtipo de documento pertence.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que referencia uma organização (por exemplo, `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Significado**: representa a chave do tipo de documento associada ao subtipo de documento.
- **Função**: chave estrangeira (implícita pela convenção de nomenclatura).
- **Conteúdo típico**: uma string de chave que se vincula a um tipo de documento mais amplo (por exemplo, `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Significado**: indica uma chave específica do subtipo de documento dentro de uma categoria de documento.
- **Função**: identificador único do subtipo de documento no escopo de um tipo de documento.
- **Conteúdo típico**: uma string de chave que identifica de forma única um subtipo de documento (por exemplo, `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Significado**: armazena um nome curto ou código do subtipo de documento.
- **Função**: descritiva.
- **Conteúdo típico**: um identificador ou código sucinto (por exemplo, `'TEST_SUB_TEST'`).

### title
- **Significado**: contém um título legível por pessoas para o subtipo de documento.
- **Função**: descritiva.
- **Conteúdo típico**: um título descritivo para interfaces de usuário ou relatórios (por exemplo, `'Test Sub Test'`).

### translation_key
- **Significado**: chave usada para internacionalização e localização, a fim de traduzir o nome do subtipo de documento.
- **Função**: técnica.
- **Conteúdo típico**: uma string usada em arquivos de tradução (por exemplo, `'test_sub_test'`).

### created_by
- **Significado**: identifica o usuário que criou a entrada do subtipo de documento.
- **Função**: técnica.
- **Conteúdo típico**: um número inteiro que representa o ID do usuário (por exemplo, `8`).

### created_on
- **Significado**: timestamp que indica quando o subtipo de documento foi criado.
- **Função**: técnica.
- **Conteúdo típico**: um timestamp com fuso horário (por exemplo, `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Significado**: timestamp que indica quando o subtipo de documento foi modificado pela última vez.
- **Função**: técnica.
- **Conteúdo típico**: um timestamp com fuso horário, possivelmente `None` se nunca foi modificado após a criação.

### is_deleted
- **Significado**: indicador booleano que informa se o subtipo de documento foi excluído logicamente.
- **Função**: técnica.
- **Conteúdo típico**: `True` ou `False`, que indica o status de exclusão (por exemplo, `False`).
```
