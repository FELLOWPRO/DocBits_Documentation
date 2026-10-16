# 表格函数

用于读取、写入和处理表格及表格行的函数。

**来源：** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value() <a id="get_column_value"></a>

读取表格行中某一列的值。

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `row` | `dict` | 来自 `table["rows"]` 的行对象 |
| `column_name` | `str` | 列名（不区分大小写） |
| `default_value` | `any` | 列为空或不存在时的返回值 |
| `is_clean` | `bool` | 如果为 `True`：转换为大写并移除空格 |

**示例 — 遍历表格行：**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
列名比较**不区分大小写**：`"DESCRIPTION"` 也会匹配 `"description"` 或 `"Description"`。
{% endhint %}

---

## set\_column\_value()

设置表格行中某一列的值。

```python
set_column_value(row, column_name, value)
```

**返回值：** 值发生变化时为 `True`，值相同时为 `False`

**副作用：**
- 设置 `extraction_method = "SCRIPT"`
- 如果列不存在，则自动创建该列

**示例 — 计算行总额：**

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

在表格单元格中设置日期值，并支持格式化和日期运算。

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `date_format_pattern` 所必需 |
| `row` | `dict` | 表格行 |
| `column_name` | `str` | 列名 |
| `value` | `str` | ISO 日期 `"2026-03-25"` |
| `add_days` | `int` | 要增加的天数 |
| `skip_weekend` | `bool` | 跳过周末 |
| `exclude_final_days` | `str/list` | 要排除的日期 |

**示例 — 计算每行的交付日期：**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

在表格单元格中设置金额值，并按区域设置格式化。

```python
set_column_amount_value(document_data, row, column_name, value)
```

**示例 — 计算并格式化行总额：**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
设置前会自动将 `value` 转换为 `str()`。
{% endhint %}

---

## add\_table\_column()

向表格的所有行添加新列。

```python
add_table_column(table, col_name, default_value=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `table` | `dict` | 表格对象（不是 `tables_dict`！） |
| `col_name` | `str` | 新列的名称 |
| `default_value` | `any` | 所有行的初始值 |

**副作用：**
- 设置 `is_extra_column = True`（标记为非原始列）
- 设置 `is_mapped = True`
- 设置 `extraction_method = "SCRIPT"`

**示例 — 添加税码列：**

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
**重复保护：** 如果该列已存在（检查时不区分大小写），则**不会**再次添加。
{% endhint %}

---

## remove\_rows\_from\_table()

从表格中移除指定数量的行。

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `table_name` | `str` | 表格名称 |
| `count` | `int` | 要移除的行数 |
| `start` | `int` | 起始索引（从 0 开始） |

**抛出异常：** 如果 `start` 或 `count` 超出范围，则抛出 `ValueError`

**示例 — 移除表头行或最后一行：**

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

仅保留指定的一行，并移除其他所有行。

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `line_number` | `int` | 行号（从 1 开始！） |

{% hint style="warning" %}
`line_number=1` 会保留第一行。请勿与从 0 开始的索引混淆。
{% endhint %}

**示例：**

```python
# Keep only the 3rd row
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables() <a id="delete_tables"></a>

删除文档中的所有表格（并备份）。

```python
delete_tables(document_data)
```

**副作用：**
- 将表格保存在 `last_deleted_table` 下
- 移除 `po_items`、`po_multi_matched`、`po_match_status`

**示例：**

```python
# Delete tables (e.g., for cost invoices without line items)
delete_tables(document_data)
```

---

## restore\_tables()

恢复先前通过 `delete_tables()` 删除的表格。

```python
restore_tables(document_data)
```

**示例：**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**删除 + 恢复模式：** 如果需要临时移除表格，并在满足特定条件时恢复，可以使用此模式。
{% endhint %}

---

## 常见模式

### 计算列总和

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

### 筛选空行

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

### 根据其他列计算列值

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
