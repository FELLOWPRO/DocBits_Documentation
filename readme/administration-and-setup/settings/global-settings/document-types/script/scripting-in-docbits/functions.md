# Functions

The scripting functions documentation has been reorganized into focused categories for easier navigation.

## Function Categories

### [Field Functions](field-functions.md)

Read, write, and control document fields — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()`, and more.

### [Table Functions](table-functions.md)

Read, write, and manipulate tables and table rows — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()`, and more.

### [Business Logic Functions](business-logic-functions.md)

Lookups, PO matching, tasks, user/group management, and status changes — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()`, and more.

### [Utility Functions](utility-functions.md)

Python built-ins, string operations, math, regex, date/time, and data structures — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()`, and more.

### [Fulltext & Vector Search Functions](fulltext-search-functions.md)

Search document archives, find similar documents, and query ERP master data — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Available from version 11.48.0**, requires `OPENSEARCH_ENABLED` license.

## Quick Reference

| Category | Key Functions |
| -------- | ------------- |
| **Fields** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tables** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Business Logic** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Search** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Utility** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
