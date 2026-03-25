# Funciones

La documentacion de funciones de scripting ha sido reorganizada en categorias enfocadas para facilitar la navegacion.

## Categorias de Funciones

### [Funciones de Campo](field-functions.md)

Leer, escribir y controlar campos del documento — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()`, y mas.

### [Funciones de Tabla](table-functions.md)

Leer, escribir y manipular tablas y filas de tablas — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()`, y mas.

### [Funciones de Logica de Negocio](business-logic-functions.md)

Lookups, coincidencia de OC, tareas, gestion de usuarios/grupos y cambios de estado — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()`, y mas.

### [Funciones de Utilidad](utility-functions.md)

Funciones integradas de Python, operaciones de cadenas, matematicas, regex, fecha/hora y estructuras de datos — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()`, y mas.

## Referencia Rapida

| Categoria | Funciones Clave |
| -------- | ------------- |
| **Campos** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tablas** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Logica de Negocio** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Utilidad** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
