# Coluna da tabela de documentos

## Colunas

* `id`: interno
* `document_table_id`: interno
* `table_name`: interno
* `org_id`: ID da organização
* `column_name`: interno
* `column_type`: interno
* `title`: interno
* `translation_key`: interno
* `sort_order`: inteiro
* `clean_field`: booleano
* `alphanumeric_field`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.document_table_column`

## Introdução

A tabela `public.document_table_column` parece ter sido projetada para armazenar metadados sobre as colunas de diversas tabelas relacionadas a documentos, como tabelas de faturas ou de notas de entrega. Esses metadados incluem informações sobre o nome, o tipo e as propriedades de cada coluna, bem como identificadores organizacionais e técnicos. A tabela oferece suporte à geração e ao gerenciamento dinâmicos de esquemas de documentos no sistema.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada entrada de coluna da tabela.
- **Função**: chave primária.
- **Observação**: normalmente uma string UUID que identifica uma linha desta tabela de forma única.

### document_table_id
- **Significado**: refere-se à tabela que contém o documento do qual esta coluna faz parte.
- **Função**: chave estrangeira.
- **Observação**: provavelmente um UUID que faz referência a outra tabela em que as tabelas de documentos são definidas.

### table_name
- **Significado**: o nome da tabela de documentos à qual esta coluna pertence.
- **Função**: campo descritivo.
- **Conteúdo típico**: nomes como `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Observação**: facilita entender a qual estrutura de documento a coluna pertence.

### org_id
- **Significado**: identificador da organização que é proprietária da tabela de documentos ou a gerencia.
- **Função**: chave estrangeira.
- **Observação**: normalmente um UUID que faz referência a uma entidade de organização.

### column_name
- **Significado**: o nome técnico da coluna dentro da sua tabela de documentos.
- **Função**: campo descritivo.
- **Conteúdo típico**: nomes como `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Observação**: representa o nome real do campo na tabela de documentos.

### column_type
- **Significado**: descreve o tipo de dado da coluna.
- **Função**: campo descritivo.
- **Conteúdo típico**: `STRING`, `DATE`.
- **Observação**: indica o tipo de dado armazenado na coluna.

### title
- **Significado**: um título ou rótulo legível da coluna.
- **Função**: campo descritivo.
- **Conteúdo típico**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Observação**: usado para exibir os nomes das colunas de forma amigável ao usuário.

### translation_key
- **Significado**: chave usada para a internacionalização e a localização do título da coluna.
- **Função**: campo técnico.
- **Observação**: atualmente vazio nos dados de exemplo, o que sugere um uso opcional.

### sort_order
- **Significado**: define a ordem das colunas quando exibidas.
- **Função**: campo descritivo.
- **Conteúdo típico**: inteiros como `16`, `5`.
- **Observação**: determina a sequência das colunas na visualização da tabela de documentos.

### clean_field
- **Significado**: indica se a coluna contém dados higienizados.
- **Função**: indicador booleano.
- **Conteúdo típico**: `True` ou `False`.
- **Observação**: usado para o status de validação ou limpeza dos dados.

### alphanumeric_field
- **Significado**: especifica se a coluna deve ser tratada como um campo alfanumérico.
- **Função**: indicador booleano.
- **Conteúdo típico**: `True` ou `False`.
- **Observação**: útil para validação de entrada ou para fins de formatação.

### created_by
- **Significado**: identificador do usuário que criou esta entrada de coluna.
- **Função**: chave estrangeira.
- **Conteúdo típico**: valores inteiros como `1`, `8`.
- **Observação**: faz referência a um usuário ou a uma entidade do sistema responsável pela criação.

### created_on
- **Significado**: timestamp de quando a entrada de coluna foi criada.
- **Função**: campo técnico.
- **Conteúdo típico**: valores de data e hora em UTC.
- **Observação**: útil para auditoria e para o acompanhamento de alterações.

### last_modified_on
- **Significado**: timestamp da última modificação feita na entrada de coluna.
- **Função**: campo técnico.
- **Observação**: atualmente `None` nos dados de exemplo, o que indica que não houve modificação após a criação.

### is_deleted
- **Significado**: indica se a entrada de coluna foi excluída logicamente.
- **Função**: indicador booleano.
- **Conteúdo típico**: `True` ou `False`.
- **Observação**: ajuda a gerenciar exclusões lógicas sem remover os dados fisicamente.

```
