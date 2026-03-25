# Funkcije

Dokumentacija funkcija za skriptovanje je reorganizovana u fokusirane kategorije radi lakse navigacije.

## Kategorije funkcija

### [Funkcije polja](field-functions.md)

Citanje, pisanje i kontrola polja dokumenta -- `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` i ostalo.

### [Funkcije tabele](table-functions.md)

Citanje, pisanje i manipulacija tabelama i redovima tabele -- `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` i ostalo.

### [Funkcije poslovne logike](business-logic-functions.md)

Pretrazivanja, uparivanje narudzbenica, zadaci, upravljanje korisnicima/grupama i promene statusa -- `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` i ostalo.

### [Pomocne funkcije](utility-functions.md)

Python ugradjene funkcije, operacije sa stringovima, matematika, regex, datum/vreme i strukture podataka -- `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` i ostalo.

## Brza referenca

| Kategorija | Kljucne funkcije |
| -------- | ------------- |
| **Polja** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tabele** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Poslovna logika** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Pomocne** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
