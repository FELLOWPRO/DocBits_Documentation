# Variáveis de Contexto

Cada script recebe automaticamente as seguintes variáveis no seu contexto de execução. Estas **não** precisam ser importadas — estão simplesmente disponíveis.

---

## Variáveis Principais

### `document_data` (alias: `doc`)

O objeto raiz que contém todos os dados do documento:

```python
document_data = {
    "document_json": { ... },   # O documento em si
    "fields": [ ... ],          # Array de todos os campos
    "fields_dict": { ... },     # Campos indexados por nome
    "tables": [ ... ],          # Array de todas as tabelas
    "tables_dict": { ... },     # Tabelas indexadas por nome
}
```

{% hint style="info" %}
`doc` é um alias — `doc` e `document_data` apontam para o mesmo objeto. Ambos podem ser usados de forma intercambiável.
{% endhint %}

### `document_json`

Acesso direto a `document_data["document_json"]`. Contém:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Para formatação de datas
    "amount_format_locale": "de_DE",         # Para formatação de valores
    "fields": [ ... ],                        # Array de campos
    "tables": [ ... ],                        # Array de tabelas
    "po_items": [ ... ],                      # Resultados da correspondência de OC
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` e `fields_dict`

```python
# fields = Array de todos os campos
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Valor bruto do OCR
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
        "coords": { ... },                    # Caixa delimitadora no documento
        "page": 1,
    },
    ...
]

# fields_dict = Indexado por nome
fields_dict = {
    "invoice_id": { ... },      # Mesmos objetos que em fields[]
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
**Criação automática com `set_field_value`:** Se um campo não existir ao usar `set_field_value()`, ele é **automaticamente criado** e adicionado tanto a `fields` como a `fields_dict`.
{% endhint %}

### `tables` e `tables_dict`

```python
# tables = Array de todas as tabelas
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
            ...  # Mais linhas
        ],
    },
]

# tables_dict = Indexado por nome da tabela
tables_dict = {
    "INVOICE_TABLE": { ... },   # Mesmos objetos que em tables[]
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — ID do utilizador atual
org_id     # String (UUID) — Organização do documento
user       # Objeto UserAuthentication — para chamadas API como is_supplier_valid()
```

{% hint style="warning" %}
**`user` nem sempre está totalmente disponível:** No contexto do worker Celery (processamento automático), `user` tem propriedades limitadas. No contexto da UI (`ON_FIELD_CHANGE`, `ON_SAVE`) é o objeto de utilizador completo.
{% endhint %}

---

## Padrões Comuns de Acesso

### Ler e escrever campos

```python
# Recomendado: via funções auxiliares
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternativa: diretamente via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Iterar tabelas

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Pesquisa de texto completo no documento

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Encaminhamento de sub-organização

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
