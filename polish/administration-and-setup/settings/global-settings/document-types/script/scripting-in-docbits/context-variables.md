# Zmienne Kontekstowe

Kazdy skrypt automatycznie otrzymuje nastepujace zmienne w swoim kontekscie wykonania. Nie trzeba ich importowac — sa po prostu dostepne.

---

## Glowne zmienne

### `document_data` (alias: `doc`)

Glowny obiekt zawierajacy wszystkie dane dokumentu:

```python
document_data = {
    "document_json": { ... },   # Sam dokument
    "fields": [ ... ],          # Tablica wszystkich pol
    "fields_dict": { ... },     # Pola indeksowane po nazwie
    "tables": [ ... ],          # Tablica wszystkich tabel
    "tables_dict": { ... },     # Tabele indeksowane po nazwie
}
```

{% hint style="info" %}
`doc` jest aliasem — `doc` i `document_data` wskazuja na ten sam obiekt. Oba moga byc uzywane zamiennie.
{% endhint %}

### `document_json`

Bezposredni dostep do `document_data["document_json"]`. Zawiera:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Do formatowania dat
    "amount_format_locale": "de_DE",         # Do formatowania kwot
    "fields": [ ... ],                        # Tablica pol
    "tables": [ ... ],                        # Tablica tabel
    "po_items": [ ... ],                      # Wyniki dopasowania ZZ
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` i `fields_dict`

```python
# fields = Tablica wszystkich pol
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Surowa wartosc OCR
        "confidence": 0.95,
        "extraction_method": "AI",            # lub "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Ramka ograniczajaca w dokumencie
        "page": 1,
    },
    ...
]

# fields_dict = Indeksowane po nazwie
fields_dict = {
    "invoice_id": { ... },      # Te same obiekty co w fields[]
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
**Automatyczne tworzenie za pomoca `set_field_value`:** Jesli pole nie istnieje podczas uzywania `set_field_value()`, jest **automatycznie tworzone** i dodawane zarowno do `fields`, jak i `fields_dict`.
{% endhint %}

### `tables` i `tables_dict`

```python
# tables = Tablica wszystkich tabel
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
            ...  # Wiecej wierszy
        ],
    },
]

# tables_dict = Indeksowane po nazwie tabeli
tables_dict = {
    "INVOICE_TABLE": { ... },   # Te same obiekty co w tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID biezacego uzytkownika
org_id     # String (UUID) — Organizacja dokumentu
user       # Obiekt UserAuthentication — do wywolan API takich jak is_supplier_valid()
```

{% hint style="warning" %}
**`user` nie jest zawsze w pelni dostepny:** W kontekscie workera Celery (automatyczne przetwarzanie) `user` ma ograniczone wlasciwosci. W kontekscie UI (`ON_FIELD_CHANGE`, `ON_SAVE`) jest to pelny obiekt uzytkownika.
{% endhint %}

---

## Typowe wzorce dostepu

### Odczyt i zapis pol

```python
# Zalecane: przez funkcje pomocnicze
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternatywnie: bezposrednio przez fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iteracja po tabelach

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Wyszukiwanie pelnotekstowe w dokumencie

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Przekierowanie do podorganizacji

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
