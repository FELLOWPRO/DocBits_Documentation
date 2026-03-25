# Fonctions

La documentation des fonctions de scripting a été réorganisée en catégories ciblées pour faciliter la navigation.

## Catégories de fonctions

### [Fonctions de Champ](field-functions.md)

Lire, écrire et contrôler les champs de document — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()`, et plus encore.

### [Fonctions de Tableau](table-functions.md)

Lire, écrire et manipuler les tables et les lignes de table — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()`, et plus encore.

### [Fonctions de Logique Métier](business-logic-functions.md)

Recherches, correspondance BC, tâches, gestion des utilisateurs/groupes et changements de statut — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()`, et plus encore.

### [Fonctions Utilitaires](utility-functions.md)

Fonctions Python intégrées, opérations sur les chaînes, mathématiques, regex, date/heure et structures de données — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()`, et plus encore.

## Référence rapide

| Catégorie | Fonctions clés |
| -------- | ------------- |
| **Champs** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tables** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **Logique Métier** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Utilitaires** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
