# Variables de Contexte

Chaque script reçoit automatiquement les variables suivantes dans son contexte d'exécution. Elles n'ont **pas** besoin d'être importées — elles sont simplement disponibles.

---

## Variables principales

### `document_data` (alias : `doc`)

L'objet racine contenant toutes les données du document :

```python
document_data = {
    "document_json": { ... },   # Le document lui-même
    "fields": [ ... ],          # Tableau de tous les champs
    "fields_dict": { ... },     # Champs indexés par nom
    "tables": [ ... ],          # Tableau de toutes les tables
    "tables_dict": { ... },     # Tables indexées par nom
}
```

{% hint style="info" %}
`doc` est un alias — `doc` et `document_data` pointent vers le même objet. Les deux peuvent être utilisés de manière interchangeable.
{% endhint %}

### `document_json`

Accès direct à `document_data["document_json"]`. Contient :

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Pour le formatage des dates
    "amount_format_locale": "de_DE",         # Pour le formatage des montants
    "fields": [ ... ],                        # Tableau des champs
    "tables": [ ... ],                        # Tableau des tables
    "po_items": [ ... ],                      # Résultats de la correspondance BC
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` et `fields_dict`

```python
# fields = Tableau de tous les champs
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Valeur OCR brute
        "confidence": 0.95,
        "extraction_method": "AI",            # ou "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Boîte englobante dans le document
        "page": 1,
    },
    ...
]

# fields_dict = Indexé par nom
fields_dict = {
    "invoice_id": { ... },      # Mêmes objets que dans fields[]
    "invoice_date": { ... },
    "net_amount": { ... },
    "tax_amount": { ... },
    "total_amount": { ... },
    "supplier_name": { ... },
    "purchase_order": { ... },
    "currency": { ... },
    ...
}
```

{% hint style="danger" %}
**Création automatique avec `set_field_value` :** Si un champ n'existe pas lors de l'utilisation de `set_field_value()`, il est **automatiquement créé** et ajouté à la fois à `fields` et `fields_dict`.
{% endhint %}

### `tables` et `tables_dict`

```python
# tables = Tableau de toutes les tables
tables = [
    {
        "name": "INVOICE_TABLE",
        "rows": [
            {
                "columns": [
                    {
                        "name": "DESCRIPTION",
                        "value": "Widget A",
                        "formatted_value": "Widget A",
                        "content": "Widget A",
                        "is_validated": False,
                        "is_mapped": True,
                        "extraction_method": "AI",
                        "location": [ ... ],
                    },
                    {
                        "name": "QUANTITY",
                        "value": "10",
                        ...
                    },
                    {
                        "name": "UNIT_PRICE",
                        "value": "25.00",
                        ...
                    },
                    {
                        "name": "LINE_TOTAL",
                        "value": "250.00",
                        ...
                    },
                ],
            },
            ...  # Plus de lignes
        ],
    },
]

# tables_dict = Indexé par nom de table
tables_dict = {
    "INVOICE_TABLE": { ... },   # Mêmes objets que dans tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Entier — ID de l'utilisateur actuel
org_id     # Chaîne (UUID) — Organisation du document
user       # Objet UserAuthentication — pour les appels API comme is_supplier_valid()
```

{% hint style="warning" %}
**`user` n'est pas toujours entièrement disponible :** Dans le contexte du worker Celery (traitement automatique), `user` a des propriétés limitées. Dans le contexte UI (`ON_FIELD_CHANGE`, `ON_SAVE`), c'est l'objet utilisateur complet.
{% endhint %}

---

## Modèles d'accès courants

### Lire et écrire des champs

```python
# Recommandé : via les fonctions utilitaires
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternative : directement via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Itérer sur les tables

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Recherche plein texte dans le document

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Routage par sous-organisation

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
