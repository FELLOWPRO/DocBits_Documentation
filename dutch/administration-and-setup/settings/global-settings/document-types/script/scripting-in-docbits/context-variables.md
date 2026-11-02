# Contextvariabelen

Elk script ontvangt automatisch de volgende variabelen in zijn uitvoeringscontext. Deze hoeven **niet** geimporteerd te worden -- ze zijn gewoon beschikbaar.

---

## Hoofdvariabelen

### `document_data` (alias: `doc`)

Het hoofdobject dat alle documentgegevens bevat:

```python
document_data = {
    "document_json": { ... },   # Het document zelf
    "fields": [ ... ],          # Array van alle velden
    "fields_dict": { ... },     # Velden geindexeerd op naam
    "tables": [ ... ],          # Array van alle tabellen
    "tables_dict": { ... },     # Tabellen geindexeerd op naam
}
```

{% hint style="info" %}
`doc` is een alias -- `doc` en `document_data` verwijzen naar hetzelfde object. Beide kunnen door elkaar worden gebruikt.
{% endhint %}

### `document_json`

Directe toegang tot `document_data["document_json"]`. Bevat:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Voor datumopmaak
    "amount_format_locale": "de_DE",         # Voor bedragopmaak
    "fields": [ ... ],                        # Velden-array
    "tables": [ ... ],                        # Tabellen-array
    "po_items": [ ... ],                      # PO-matchingresultaten
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` en `fields_dict`

```python
# fields = Array van alle velden
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Ruwe OCR-waarde
        "confidence": 0.95,
        "extraction_method": "AI",            # of "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Begrenzingskader in document
        "page": 1,
    },
    ...
]

# fields_dict = Geindexeerd op naam
fields_dict = {
    "invoice_id": { ... },      # Dezelfde objecten als in fields[]
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
**Automatisch aanmaken met `set_field_value`:** Als een veld niet bestaat bij gebruik van `set_field_value()`, wordt het **automatisch aangemaakt** en toegevoegd aan zowel `fields` als `fields_dict`.
{% endhint %}

### `tables` en `tables_dict`

```python
# tables = Array van alle tabellen
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
            ...  # Meer rijen
        ],
    },
]

# tables_dict = Geindexeerd op tabelnaam
tables_dict = {
    "INVOICE_TABLE": { ... },   # Dezelfde objecten als in tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID van de huidige gebruiker
org_id     # String (UUID) — Organisatie van het document
user       # UserAuthentication-object — voor API-aanroepen zoals is_supplier_valid()
```

{% hint style="warning" %}
**`user` is niet altijd volledig beschikbaar:** In Celery-workercontext (automatische verwerking) heeft `user` beperkte eigenschappen. In UI-context (`ON_FIELD_CHANGE`, `ON_SAVE`) is het het volledige gebruikersobject.
{% endhint %}

---

## Veelvoorkomende Toegangspatronen

### Velden lezen en schrijven

```python
# Aanbevolen: via helperfuncties
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternatief: direct via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Tabellen doorlopen

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Volledige tekst doorzoeken in document

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Sub-organisatie routering

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
