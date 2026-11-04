# Dados extraídos do documento

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_id`: interno
* `field_name`: interno
* `field_value`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `field_type`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.document_extracted_data`

## Introdução

A tabela `public.document_extracted_data` foi projetada para armazenar dados extraídos de diversos documentos, provavelmente para fins de processamento e análise de documentos. Cada entrada da tabela corresponde a um campo específico extraído de um documento, como uma fatura, e inclui metadados sobre o processo de extração. A tabela facilita o acompanhamento e o gerenciamento dos dados dos documentos, associando-os a organizações e a documentos específicos.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada entrada de dados extraídos.
- **Função**: chave primária.
- **Conteúdo típico**: uma string no formato UUID que identifica de forma única o registro de dados extraídos.

### org_id
- **Significado**: identificador da organização associada aos dados do documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string no formato UUID que representa a organização.

### doc_id
- **Significado**: identificador do documento do qual os dados foram extraídos.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string no formato UUID que representa o documento.

### field_name
- **Significado**: o nome do campo extraído do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings como 'invoice_id', 'invoice_date' etc., que indicam o tipo de dado extraído.

### field_value
- **Significado**: o valor associado ao campo extraído.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings que representam diversos tipos de dados, como números de fatura, datas ou valores.

### created_by
- **Significado**: o identificador do usuário ou processo que criou a entrada de dados.
- **Função**: campo técnico.
- **Conteúdo típico**: inteiro que representa um ID de usuário ou de processo.

### created_on
- **Significado**: o timestamp de quando a entrada de dados foi criada.
- **Função**: campo técnico.
- **Conteúdo típico**: timestamp com dados de fuso horário que indica a data e a hora da criação.

### last_modified_on
- **Significado**: o timestamp da última modificação feita na entrada de dados.
- **Função**: campo técnico.
- **Conteúdo típico**: timestamp com dados de fuso horário que indica a data e a hora da última modificação (pode ser nulo se nunca foi modificado).

### is_deleted
- **Significado**: um indicador que informa se a entrada de dados foi marcada como excluída.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano, em que `False` indica entradas ativas e `True` indica entradas excluídas.

### field_type
- **Significado**: o tipo de dado armazenado na coluna `field_value`.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings como 'date', 'AMOUNT' ou nulo, se o tipo não for especificado.

Este modelo de dados estruturado permite o armazenamento e a recuperação eficientes de dados relacionados a documentos, oferecendo suporte a diversas aplicações, do processamento de faturas à gestão de conformidade.
```
