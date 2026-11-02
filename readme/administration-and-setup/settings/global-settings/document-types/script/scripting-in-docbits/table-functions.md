# Table Functions

Functions for reading, writing, and manipulating tables and table rows.

**Source:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Reads the value of a column from a table row.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `row` | `dict` | A row object from `table["rows"]` |
| `column_name` | `str` | Column name (case-insensitive) |
| `default_value` | `any` | Return value if column is empty/missing |
| `is_clean` | `bool` | If `True`: UPPERCASE with spaces removed |

**Example — Iterate table rows:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Column name comparison is **case-insensitive**: `"DESCRIPTION"` also matches `"description"` or `"Description"`.
{% endhint %}

---

## set\_column\_value()

Sets the value of a column in a table row.

```python
set_column_value(row, column_name, value)
```

**Returns:** `True` if value changed, `False` if identical

**Side effects:**
- Sets `extraction_method = "SCRIPT"`
- Automatically creates the column if it does not exist

**Example — Calculate line totals:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
        try:
            total = float(qty) * float(price)
            set_column_value(row, "LINE_TOTAL", str(total))
        except ValueError:
            pass
```

---

## set\_column\_date\_value()

Sets a date value in a table cell with formatting and date arithmetic.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Required for `date_format_pattern` |
| `row` | `dict` | Table row |
| `column_name` | `str` | Column name |
| `value` | `str` | ISO date `"2026-03-25"` |
| `add_days` | `int` | Days to add |
| `skip_weekend` | `bool` | Skip weekends |
| `exclude_final_days` | `str/list` | Days to exclude |

**Example — Calculate delivery dates per row:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Sets an amount value in a table cell with locale formatting.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Example — Calculate and format line totals:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` is automatically converted to `str()` before being set.
{% endhint %}

---

## add\_table\_column()

Adds a new column to all rows of a table.

```python
add_table_column(table, col_name, default_value=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `table` | `dict` | The table object (not `tables_dict`!) |
| `col_name` | `str` | Name of the new column |
| `default_value` | `any` | Initial value for all rows |

**Side effects:**
- `is_extra_column = True` (marked as non-original)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Example — Add tax code column:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Now set values per row
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Duplicate protection:** If the column already exists (case-insensitive check), it will **not** be added again.
{% endhint %}

---

## remove\_rows\_from\_table()

Removes a specific number of rows from a table.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `table_name` | `str` | Name of the table |
| `count` | `int` | Number of rows to remove |
| `start` | `int` | Start index (0-based) |

**Raises:** `ValueError` if `start` or `count` is out of range

**Example — Remove header rows or last row:**

```python
# Remove first 2 rows (e.g., header rows)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Remove last row
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Keeps only one specific row and removes all others.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `line_number` | `int` | Row number (1-based!) |

{% hint style="warning" %}
`line_number=1` keeps the first row. Do not confuse with 0-based indices.
{% endhint %}

**Example:**

```python
# Keep only the 3rd row
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Deletes all tables from the document (with backup).

```python
delete_tables(document_data)
```

**Side effects:**
- Saves tables under `last_deleted_table`
- Removes `po_items`, `po_multi_matched`, `po_match_status`

**Example:**

```python
# Delete tables (e.g., for cost invoices without line items)
delete_tables(document_data)
```

---

## restore\_tables()

Restores tables previously deleted with `delete_tables()`.

```python
restore_tables(document_data)
```

**Example:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Delete + Restore pattern:** Useful when you want to temporarily remove tables and restore them under certain conditions.
{% endhint %}

---

## Common Patterns

### Calculate column sum

```python
table = tables_dict.get("INVOICE_TABLE")
total = 0
if table:
    for row in table["rows"]:
        val = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(val)
        except ValueError:
            pass
    set_field_value(document_data, "calculated_total", str(round(total, 2)))
```

### Filter empty rows

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Remove from back to front
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Compute column from other columns

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_AMOUNT", "0")
    for row in table["rows"]:
        net = float(get_column_value(row, "NET_AMOUNT", "0"))
        tax_rate = float(get_column_value(row, "TAX_RATE", "0"))
        tax = net * tax_rate / 100
        set_column_amount_value(document_data, row, "TAX_AMOUNT", tax)
```
