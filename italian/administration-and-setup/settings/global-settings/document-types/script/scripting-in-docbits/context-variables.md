# Variabili di Contesto

Ogni script riceve automaticamente le seguenti variabili nel suo contesto di esecuzione. Queste **non** devono essere importate -- sono semplicemente disponibili.

---

## Variabili Principali

### `document_data` (alias: `doc`)

L'oggetto radice che contiene tutti i dati del documento:

```python
document_data = {
    "document_json": { ... },   # Il documento stesso
    "fields": [ ... ],          # Array di tutti i campi
    "fields_dict": { ... },     # Campi indicizzati per nome
    "tables": [ ... ],          # Array di tutte le tabelle
    "tables_dict": { ... },     # Tabelle indicizzate per nome
}
```

{% hint style="info" %}
`doc` e un alias -- `doc` e `document_data` puntano allo stesso oggetto. Entrambi possono essere usati indifferentemente.
{% endhint %}

### `document_json`

Accesso diretto a `document_data["document_json"]`. Contiene:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Per la formattazione delle date
    "amount_format_locale": "de_DE",         # Per la formattazione degli importi
    "fields": [ ... ],                        # Array dei campi
    "tables": [ ... ],                        # Array delle tabelle
    "po_items": [ ... ],                      # Risultati dell'abbinamento OA
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` e `fields_dict`

```python
# fields = Array di tutti i campi
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Valore OCR grezzo
        "confidence": 0.95,
        "extraction_method": "AI",            # oppure "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Riquadro di delimitazione nel documento
        "page": 1,
    },
    ...
]

# fields_dict = Indicizzato per nome
fields_dict = {
    "invoice_id": { ... },      # Stessi oggetti presenti in fields[]
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
**Creazione automatica con `set_field_value`:** Se un campo non esiste quando si utilizza `set_field_value()`, viene **creato automaticamente** e aggiunto sia a `fields` che a `fields_dict`.
{% endhint %}

### `tables` e `tables_dict`

```python
# tables = Array di tutte le tabelle
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
            ...  # Altre righe
        ],
    },
]

# tables_dict = Indicizzato per nome della tabella
tables_dict = {
    "INVOICE_TABLE": { ... },   # Stessi oggetti presenti in tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Intero — ID dell'utente corrente
org_id     # Stringa (UUID) — Organizzazione del documento
user       # Oggetto UserAuthentication — per chiamate API come is_supplier_valid()
```

{% hint style="warning" %}
**`user` non e sempre completamente disponibile:** Nel contesto del worker Celery (elaborazione automatica), `user` ha proprieta limitate. Nel contesto UI (`ON_FIELD_CHANGE`, `ON_SAVE`) e l'oggetto utente completo.
{% endhint %}

---

## Pattern di Accesso Comuni

### Leggere e scrivere campi

```python
# Consigliato: tramite funzioni helper
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternativa: direttamente tramite fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iterare le tabelle

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Ricerca nel testo completo del documento

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Instradamento sotto-organizzazione

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
