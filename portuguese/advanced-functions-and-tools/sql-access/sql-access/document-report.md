# Relatório do documento

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_id`: interno
* `doc_type`: tipo de documento
* `sub_doc_type`: interno
* `time_spent`: interno
* `fields_total`: inteiro
* `fields_correct`: inteiro
* `checkbox_fields_total`: inteiro
* `checkbox_fields_correct`: inteiro
* `table_values_total`: inteiro
* `table_values_correct`: inteiro
* `detail_report`: texto
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `validated_by`: inteiro
* `sub_org_id`: interno

## Análise e descrição

```markdown
# Documentação da tabela Relatório do documento

## Introdução
A tabela `public.document_report` foi projetada para armazenar informações detalhadas sobre relatórios de processamento de documentos, especificamente relacionados à validação e à extração de campos de documentos como faturas. A tabela captura metadados sobre o documento, métricas de processamento e os resultados da validação, que podem ser usados para auditoria, acompanhamento e melhoria dos fluxos de trabalho de processamento de documentos.

## Descrição das colunas

### id
- **Significado**: identificador único de cada entrada de relatório de documento.
- **Função**: chave primária
- **Conteúdo típico**: um UUID que representa o relatório de documento único.

### org_id
- **Significado**: identificador da organização associada ao documento.
- **Função**: chave estrangeira
- **Conteúdo típico**: um UUID que faz referência a uma organização.

### doc_id
- **Significado**: identificador do documento específico a que o relatório se refere.
- **Função**: chave estrangeira
- **Conteúdo típico**: um UUID que representa o documento único.

### doc_type
- **Significado**: tipo do documento processado, como uma fatura.
- **Função**: campo descritivo
- **Conteúdo típico**: valores como `INVOICE`.

### sub_doc_type
- **Significado**: subtipo do documento, que oferece uma categorização mais detalhada.
- **Função**: campo descritivo
- **Conteúdo típico**: pode ser `null` ou subtipos específicos como "Cost Invoice".

### time_spent
- **Significado**: tempo gasto na validação do documento.
- **Função**: campo de métrica
- **Conteúdo típico**: normalmente '0', medindo o tempo em unidades predefinidas.

### fields_total
- **Significado**: número total de campos extraídos do documento.
- **Função**: campo de métrica
- **Conteúdo típico**: um inteiro que representa o total de campos, por exemplo, 13.

### fields_correct
- **Significado**: número de campos extraídos e validados corretamente.
- **Função**: campo de métrica
- **Conteúdo típico**: um inteiro que representa os campos processados corretamente, por exemplo, 12.

### checkbox_fields_total
- **Significado**: número total de campos de caixa de seleção processados.
- **Função**: campo de métrica
- **Conteúdo típico**: geralmente `0`, indicando os campos de caixa de seleção processados.

### checkbox_fields_correct
- **Significado**: número de campos de caixa de seleção validados corretamente.
- **Função**: campo de métrica
- **Conteúdo típico**: geralmente `0`, indicando os campos de caixa de seleção validados corretamente.

### table_values_total
- **Significado**: número total de valores de tabela extraídos do documento.
- **Função**: campo de métrica
- **Conteúdo típico**: geralmente `0`, indicando o total de valores de tabela processados.

### table_values_correct
- **Significado**: número de valores de tabela validados corretamente.
- **Função**: campo de métrica
- **Conteúdo típico**: geralmente `0`, indicando os valores de tabela validados corretamente.

### detail_report
- **Significado**: conteúdo JSON com o relatório detalhado dos campos do documento e de seu status de validação.
- **Função**: campo descritivo/técnico
- **Conteúdo típico**: string JSON com informações detalhadas dos campos.

### created_on
- **Significado**: timestamp de quando a entrada do relatório de documento foi criada.
- **Função**: campo técnico
- **Conteúdo típico**: timestamp em UTC, por exemplo, `2025-03-10 08:07:24+00`.

### last_modified_on
- **Significado**: timestamp da última modificação do relatório de documento.
- **Função**: campo técnico
- **Conteúdo típico**: timestamp em UTC, que indica o momento da última atualização.

### is_deleted
- **Significado**: indica se o relatório de documento foi marcado como excluído.
- **Função**: campo técnico
- **Conteúdo típico**: valor booleano; `False` se não foi excluído.

### validated_by
- **Significado**: identificador do usuário que validou o documento.
- **Função**: chave estrangeira
- **Conteúdo típico**: inteiro que representa o ID do validador, por exemplo, `1`.

### sub_org_id
- **Significado**: identificador de uma suborganização relacionada ao documento.
- **Função**: chave estrangeira
- **Conteúdo típico**: um UUID que faz referência a uma suborganização.
```
