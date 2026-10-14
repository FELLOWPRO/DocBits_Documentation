# Context Variables

Every script automatically receives the following variables in its execution context. These do **not** need to be imported — they are simply available.

---

## Main Variables

### `document_data` (alias: `doc`)

The root object containing all document data:

```python
document_data = {
    "document_json": { ... },   # The document itself
    "fields": [ ... ],          # Array of all fields
    "fields_dict": { ... },     # Fields indexed by name
    "tables": [ ... ],          # Array of all tables
    "tables_dict": { ... },     # Tables indexed by name
}
```

{% hint style="info" %}
`doc` is an alias — `doc` and `document_data` point to the same object. Both can be used interchangeably.
{% endhint %}

### `document_json`

Direct access to `document_data["document_json"]`. Contains:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # For date formatting
    "amount_format_locale": "de_DE",         # For amount formatting
    "fields": [ ... ],                        # Field array
    "tables": [ ... ],                        # Table array
    "po_items": [ ... ],                      # PO matching results
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` and `fields_dict`

```python
# fields = Array of all fields
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Raw OCR value
        "confidence": 0.95,
        "extraction_method": "AI",            # or "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Bounding box in document
        "page": 1,
    },
    ...
]

# fields_dict = Indexed by name
fields_dict = {
    "invoice_id": { ... },      # Same objects as in fields[]
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
**Auto-create with `set_field_value`:** If a field does not exist when using `set_field_value()`, it is **automatically created** and added to both `fields` and `fields_dict`.
{% endhint %}

### `tables` and `tables_dict`

```python
# tables = Array of all tables
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
            ...  # More rows
        ],
    },
]

# tables_dict = Indexed by table name
tables_dict = {
    "INVOICE_TABLE": { ... },   # Same objects as in tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID of the current user
org_id     # String (UUID) — Organization of the document
user       # UserAuthentication object — for API calls like is_supplier_valid()
```

{% hint style="warning" %}
**`user` is not always fully available:** In Celery worker context (automatic processing), `user` has limited properties. In UI context (`ON_FIELD_CHANGE`, `ON_SAVE`) it is the full user object.
{% endhint %}

---

## Common Access Patterns

### Read and write fields

```python
# Recommended: via helper functions
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternative: directly via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iterate tables

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Fulltext search in document

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Sub-org routing

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
