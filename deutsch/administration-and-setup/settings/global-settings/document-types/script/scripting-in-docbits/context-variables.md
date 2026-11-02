# Kontextvariablen

Jedes Skript erhält automatisch die folgenden Variablen in seinem Ausführungskontext. Diese müssen **nicht** importiert werden — sie stehen einfach zur Verfügung.

---

## Hauptvariablen

### `document_data` (Alias: `doc`)

Das Stammobjekt, das alle Dokumentdaten enthält:

```python
document_data = {
    "document_json": { ... },   # Das Dokument selbst
    "fields": [ ... ],          # Array aller Felder
    "fields_dict": { ... },     # Felder indiziert nach Name
    "tables": [ ... ],          # Array aller Tabellen
    "tables_dict": { ... },     # Tabellen indiziert nach Name
}
```

{% hint style="info" %}
`doc` ist ein Alias — `doc` und `document_data` zeigen auf dasselbe Objekt. Beide können austauschbar verwendet werden.
{% endhint %}

### `document_json`

Direkter Zugriff auf `document_data["document_json"]`. Enthält:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Für Datumsformatierung
    "amount_format_locale": "de_DE",         # Für Betragsformatierung
    "fields": [ ... ],                        # Feld-Array
    "tables": [ ... ],                        # Tabellen-Array
    "po_items": [ ... ],                      # PO-Matching-Ergebnisse
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` und `fields_dict`

```python
# fields = Array aller Felder
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Roher OCR-Wert
        "confidence": 0.95,
        "extraction_method": "AI",            # oder "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Begrenzungsrahmen im Dokument
        "page": 1,
    },
    ...
]

# fields_dict = Nach Name indiziert
fields_dict = {
    "invoice_id": { ... },      # Dieselben Objekte wie in fields[]
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
**Automatische Erstellung mit `set_field_value`:** Wenn ein Feld bei Verwendung von `set_field_value()` nicht existiert, wird es **automatisch erstellt** und sowohl zu `fields` als auch zu `fields_dict` hinzugefügt.
{% endhint %}

### `tables` und `tables_dict`

```python
# tables = Array aller Tabellen
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
            ...  # Weitere Zeilen
        ],
    },
]

# tables_dict = Nach Tabellenname indiziert
tables_dict = {
    "INVOICE_TABLE": { ... },   # Dieselben Objekte wie in tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID des aktuellen Benutzers
org_id     # String (UUID) — Organisation des Dokuments
user       # UserAuthentication-Objekt — für API-Aufrufe wie is_supplier_valid()
```

{% hint style="warning" %}
**`user` ist nicht immer vollständig verfügbar:** Im Celery-Worker-Kontext (automatische Verarbeitung) hat `user` eingeschränkte Eigenschaften. Im UI-Kontext (`ON_FIELD_CHANGE`, `ON_SAVE`) ist es das vollständige Benutzerobjekt.
{% endhint %}

---

## Häufige Zugriffsmuster

### Felder lesen und schreiben

```python
# Empfohlen: über Hilfsfunktionen
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternative: direkt über fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Tabellen iterieren

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Volltextsuche im Dokument

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Sub-Org-Zuordnung

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
