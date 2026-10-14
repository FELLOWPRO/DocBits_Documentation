# Funções

A documentação das funções de scripting foi reorganizada em categorias focadas para facilitar a navegação.

## Categorias de Funções

### [Funções de Campo](field-functions.md)

Ler, escrever e controlar campos de documentos — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()`, e mais.

### [Funções de Tabela](table-functions.md)

Ler, escrever e manipular tabelas e linhas de tabelas — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()`, e mais.

### [Funções de Lógica de Negócio](business-logic-functions.md)

Lookups, correspondência de OC, tarefas, gestão de utilizadores/grupos e alterações de estado — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()`, e mais.

### [Funções Utilitárias](utility-functions.md)

Built-ins do Python, operações com strings, matemática, regex, data/hora e estruturas de dados — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()`, e mais.

### [Funções de Pesquisa Fulltext e Vetorial](fulltext-search-functions.md)

Pesquisar arquivos de documentos, encontrar documentos semelhantes e consultar dados mestre do ERP — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Disponível a partir da versão 11.48.0**, requer licença `OPENSEARCH_ENABLED`.

## Referência Rápida

| Categoria | Funções Principais |
| -------- | ------------- |
| **Campos** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tabelas** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Lógica de Negócio** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Pesquisa** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Utilitárias** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
