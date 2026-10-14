# Variables de Contexto

Cada script recibe automaticamente las siguientes variables en su contexto de ejecucion. **No** necesitan ser importadas — simplemente estan disponibles.

---

## Variables Principales

### `document_data` (alias: `doc`)

El objeto raiz que contiene todos los datos del documento:

```python
document_data = {
    "document_json": { ... },   # El documento en si
    "fields": [ ... ],          # Array de todos los campos
    "fields_dict": { ... },     # Campos indexados por nombre
    "tables": [ ... ],          # Array de todas las tablas
    "tables_dict": { ... },     # Tablas indexadas por nombre
}
```

{% hint style="info" %}
`doc` es un alias — `doc` y `document_data` apuntan al mismo objeto. Ambos pueden usarse indistintamente.
{% endhint %}

### `document_json`

Acceso directo a `document_data["document_json"]`. Contiene:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Para formato de fechas
    "amount_format_locale": "de_DE",         # Para formato de montos
    "fields": [ ... ],                        # Array de campos
    "tables": [ ... ],                        # Array de tablas
    "po_items": [ ... ],                      # Resultados de coincidencia de OC
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` y `fields_dict`

```python
# fields = Array de todos los campos
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Valor OCR sin procesar
        "confidence": 0.95,
        "extraction_method": "AI",            # o "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Cuadro delimitador en el documento
        "page": 1,
    },
    ...
]

# fields_dict = Indexado por nombre
fields_dict = {
    "invoice_id": { ... },      # Mismos objetos que en fields[]
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
**Auto-creacion con `set_field_value`:** Si un campo no existe al usar `set_field_value()`, se **crea automaticamente** y se agrega tanto a `fields` como a `fields_dict`.
{% endhint %}

### `tables` y `tables_dict`

```python
# tables = Array de todas las tablas
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
            ...  # Mas filas
        ],
    },
]

# tables_dict = Indexado por nombre de tabla
tables_dict = {
    "INVOICE_TABLE": { ... },   # Mismos objetos que en tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID del usuario actual
org_id     # String (UUID) — Organizacion del documento
user       # Objeto UserAuthentication — para llamadas API como is_supplier_valid()
```

{% hint style="warning" %}
**`user` no siempre esta completamente disponible:** En el contexto de Celery worker (procesamiento automatico), `user` tiene propiedades limitadas. En el contexto de UI (`ON_FIELD_CHANGE`, `ON_SAVE`) es el objeto de usuario completo.
{% endhint %}

---

## Patrones de Acceso Comunes

### Leer y escribir campos

```python
# Recomendado: mediante funciones auxiliares
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternativa: directamente via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iterar tablas

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Busqueda de texto completo en el documento

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Enrutamiento por sub-organizacion

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
