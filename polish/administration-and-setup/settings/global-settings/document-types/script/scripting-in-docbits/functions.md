# Funkcje

Dokumentacja funkcji skryptowych zostala podzielona na kategorie tematyczne dla latwiejszej nawigacji.

## Kategorie funkcji

### [Funkcje Pol](field-functions.md)

Odczyt, zapis i kontrola pol dokumentu — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` i wiele wiecej.

### [Funkcje Tabel](table-functions.md)

Odczyt, zapis i manipulacja tabelami oraz wierszami tabel — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` i wiele wiecej.

### [Funkcje Logiki Biznesowej](business-logic-functions.md)

Wyszukiwania, dopasowywanie ZZ, zadania, zarzadzanie uzytkownikami/grupami i zmiany statusow — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` i wiele wiecej.

### [Funkcje Pomocnicze](utility-functions.md)

Wbudowane funkcje Pythona, operacje na ciagach znakow, matematyka, wyrazenia regularne, data/czas i struktury danych — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` i wiele wiecej.


### [Funkcje Wyszukiwania Fulltext i Wektorowego](fulltext-search-functions.md)

Przeszukiwanie archiwow dokumentow, znajdowanie podobnych dokumentow i odpytywanie danych bazowych ERP — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Dostepne od wersji 11.48.0**, wymaga licencji `OPENSEARCH_ENABLED`.

## Szybka referencja

| Kategoria | Kluczowe funkcje |
| -------- | ------------- |
| **Pola** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tabele** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Logika biznesowa** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Wyszukiwanie** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Pomocnicze** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
