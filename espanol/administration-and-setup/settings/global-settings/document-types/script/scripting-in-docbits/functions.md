# Funciones

La documentación de funciones de scripting se ha reorganizado en categorías específicas para facilitar la navegación.

## Categorías de Funciones

### [Funciones de Campo](field-functions.md)

Leer, escribir y controlar campos de documentos — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` y más.

### [Funciones de Tabla](table-functions.md)

Leer, escribir y manipular tablas y filas de tablas — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` y más.

### [Funciones de Lógica de Negocio](business-logic-functions.md)

Lookups, coincidencia de OC, tareas, gestión de usuarios/grupos y cambios de estado — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` y más.

### [Funciones de Utilidad](utility-functions.md)

Built-ins de Python, operaciones de cadena, matemáticas, regex, fecha/hora y estructuras de datos — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` y más.

### [Funciones de Búsqueda Fulltext y Vectorial](fulltext-search-functions.md)

Buscar en archivos de documentos, encontrar documentos similares y consultar datos maestros de ERP — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Disponible desde la versión 11.48.0**, requiere licencia `OPENSEARCH_ENABLED`.

## Referencia Rápida

| Categoría | Funciones Principales |
| --------- | --------------------- |
| **Campos** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tablas** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Lógica de Negocio** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Búsqueda** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Utilidad** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
