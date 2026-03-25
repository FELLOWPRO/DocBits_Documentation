# Kontekst varijable

Svaka skripta automatski prima sledece varijable u svom kontekstu izvrsavanja. One **ne** moraju da se importuju -- jednostavno su dostupne.

---

## Glavne varijable

### `document_data` (alias: `doc`)

Koreni objekat koji sadrzi sve podatke dokumenta:

```python
document_data = {
    "document_json": { ... },   # Sam dokument
    "fields": [ ... ],          # Niz svih polja
    "fields_dict": { ... },     # Polja indeksirana po nazivu
    "tables": [ ... ],          # Niz svih tabela
    "tables_dict": { ... },     # Tabele indeksirane po nazivu
}
```

{% hint style="info" %}
`doc` je alias -- `doc` i `document_data` pokazuju na isti objekat. Oba se mogu koristiti naizmenicno.
{% endhint %}

### `document_json`

Direktan pristup `document_data["document_json"]`. Sadrzi:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Za formatiranje datuma
    "amount_format_locale": "de_DE",         # Za formatiranje iznosa
    "fields": [ ... ],                        # Niz polja
    "tables": [ ... ],                        # Niz tabela
    "po_items": [ ... ],                      # Rezultati uparivanja narudzbenica
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` i `fields_dict`

```python
# fields = Niz svih polja
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Sirova OCR vrednost
        "confidence": 0.95,
        "extraction_method": "AI",            # ili "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Okvir u dokumentu
        "page": 1,
    },
    ...
]

# fields_dict = Indeksirano po nazivu
fields_dict = {
    "invoice_id": { ... },      # Isti objekti kao u fields[]
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
**Automatsko kreiranje sa `set_field_value`:** Ako polje ne postoji prilikom koriscenja `set_field_value()`, ono se **automatski kreira** i dodaje u `fields` i `fields_dict`.
{% endhint %}

### `tables` i `tables_dict`

```python
# tables = Niz svih tabela
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
            ...  # Vise redova
        ],
    },
]

# tables_dict = Indeksirano po nazivu tabele
tables_dict = {
    "INVOICE_TABLE": { ... },   # Isti objekti kao u tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer -- ID trenutnog korisnika
org_id     # String (UUID) -- Organizacija dokumenta
user       # UserAuthentication objekat -- za API pozive kao sto je is_supplier_valid()
```

{% hint style="warning" %}
**`user` nije uvek potpuno dostupan:** U kontekstu Celery radnika (automatska obrada), `user` ima ogranicena svojstva. U kontekstu korisnickog interfejsa (`ON_FIELD_CHANGE`, `ON_SAVE`) to je kompletni korisnicki objekat.
{% endhint %}

---

## Uobicajeni obrasci pristupa

### Citanje i pisanje polja

```python
# Preporuceno: putem pomocnih funkcija
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternativa: direktno putem fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iteracija kroz tabele

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Pretraga celokupnog teksta u dokumentu

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Rutiranje podorganizacije

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
