# Fonctions

La documentation des fonctions de scripting a été réorganisée en catégories ciblées pour faciliter la navigation.

## Catégories de Fonctions

### [Fonctions de Champ](field-functions.md)

Lire, écrire et contrôler les champs de documents — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` et plus.

### [Fonctions de Table](table-functions.md)

Lire, écrire et manipuler les tables et les lignes de tables — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` et plus.

### [Fonctions de Logique Métier](business-logic-functions.md)

Lookups, correspondance BC, tâches, gestion des utilisateurs/groupes et changements de statut — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` et plus.

### [Fonctions Utilitaires](utility-functions.md)

Built-ins Python, opérations sur les chaînes, mathématiques, regex, date/heure et structures de données — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` et plus.

### [Fonctions de Recherche Fulltext et Vectorielle](fulltext-search-functions.md)

Rechercher dans les archives de documents, trouver des documents similaires et interroger les données maîtres ERP — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Disponible à partir de la version 11.48.0**, nécessite la licence `OPENSEARCH_ENABLED`.

## Référence Rapide

| Catégorie | Fonctions Principales |
| --------- | --------------------- |
| **Champs** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tables** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Logique Métier** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Recherche** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Utilitaires** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
