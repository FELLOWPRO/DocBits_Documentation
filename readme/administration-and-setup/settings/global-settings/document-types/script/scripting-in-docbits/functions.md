# Funzioni

La documentazione delle funzioni di scripting e stata riorganizzata in categorie mirate per una navigazione piu semplice.

## Categorie di Funzioni

### [Funzioni di Campo](field-functions.md)

Leggere, scrivere e controllare i campi del documento — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` e altre.

### [Funzioni di Tabella](table-functions.md)

Leggere, scrivere e manipolare tabelle e righe di tabella — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` e altre.

### [Funzioni di Logica Aziendale](business-logic-functions.md)

Ricerche, abbinamento OA, attivita, gestione utenti/gruppi e cambiamenti di stato — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` e altre.

### [Funzioni di Utilita](utility-functions.md)

Funzioni built-in di Python, operazioni su stringhe, matematica, regex, data/ora e strutture dati — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` e altre.

## Riferimento Rapido

| Categoria | Funzioni Chiave |
| -------- | ------------- |
| **Campi** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tabelle** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Logica Aziendale** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Utilita** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
