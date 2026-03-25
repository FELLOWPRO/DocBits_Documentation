# Funktionen

Die Dokumentation der Skriptfunktionen wurde in fokussierte Kategorien unterteilt, um die Navigation zu erleichtern.

## Funktionskategorien

### [Feld-Funktionen](field-functions.md)

Felder lesen, schreiben und steuern — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` und mehr.

### [Tabellen-Funktionen](table-functions.md)

Tabellen und Tabellenzeilen lesen, schreiben und manipulieren — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` und mehr.

### [Geschäftslogik-Funktionen](business-logic-functions.md)

Lookups, PO-Matching, Aufgaben, Benutzer-/Gruppenverwaltung und Statusänderungen — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` und mehr.

### [Hilfsfunktionen](utility-functions.md)

Python-Built-ins, String-Operationen, Mathematik, Regex, Datum/Uhrzeit und Datenstrukturen — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` und mehr.

## Kurzreferenz

| Kategorie | Wichtige Funktionen |
| --------- | ------------------- |
| **Felder** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tabellen** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Geschäftslogik** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Hilfsfunktionen** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
