# 上下文变量

每个脚本都会在其执行上下文中自动获得以下变量。无需导入这些变量，它们可以直接使用。

---

## 主要变量

### `document_data`（别名：`doc`）

包含所有文档数据的根对象：

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
`doc` 是一个别名：`doc` 和 `document_data` 指向同一个对象。两者可以互换使用。
{% endhint %}

### `document_json`

直接访问 `document_data["document_json"]`。其中包含：

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

### `fields` 和 `fields_dict`

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
**使用 `set_field_value` 自动创建：** 如果使用 `set_field_value()` 时字段不存在，系统会**自动创建该字段**，并将其添加到 `fields` 和 `fields_dict` 中。
{% endhint %}

### `tables` 和 `tables_dict`

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

### `user_id`、`org_id`、`user`

```python
user_id    # Integer — ID of the current user
org_id     # String (UUID) — Organization of the document
user       # UserAuthentication object — for API calls like is_supplier_valid()
```

{% hint style="warning" %}
**`user` 并非始终完整可用：** 在 Celery 工作进程上下文（自动处理）中，`user` 的属性有限。在 UI 上下文（`ON_FIELD_CHANGE`、`ON_SAVE`）中，它是完整的用户对象。
{% endhint %}

---

## 常见访问方式

### 读取和写入字段

```python
# Recommended: via helper functions
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternative: directly via fields_dict
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### 遍历表格

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### 在文档中进行全文搜索

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### 子组织路由

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```
