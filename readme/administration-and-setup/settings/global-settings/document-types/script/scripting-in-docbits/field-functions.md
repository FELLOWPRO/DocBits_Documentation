# 字段函数

用于读取、写入和控制文档字段的函数。

**来源：** `module/script/helper/document_script_functions.py`

---

## get\_field\_value() <a id="get_field_value"></a>

读取文档中某个字段的值。

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `document_data` 上下文对象 |
| `field_name` | `str` | 字段名称（例如 `"invoice_id"`） |
| `default_value` | `any` | 字段为空或缺失时的返回值（默认值：`None`） |
| `is_clean` | `bool` | 如果为 `True`：将值转换为大写并移除空格 |

**返回值：** 字段值（字符串），或 `default_value`

**示例 — 读取发票编号并设置备用值：**

```python
# Read field with default value
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# With is_clean=True: "INV 001" becomes "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**执行结果：** 返回字段值。当 `is_clean=True` 时，值会通过 `value.upper().replace(" ", "").strip()` 转换，适用于比较。

---

## set\_field\_value() <a id="set_field_value"></a>

设置字段的值。如果字段不存在，会自动创建该字段。

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `document_data` 上下文对象 |
| `field_name` | `str` | 字段名称 |
| `value` | `any` | 新值 |
| `remove_link` | `bool` | 如果为 `True`：移除 coords、confidence、rule 等属性 |

**返回值：** 如果值已更改则返回 `True`，如果值相同则返回 `False`

**副作用：**
- 设置 `highlight_field = True`（在界面中显示视觉提示）
- 设置 `extraction_method = "SCRIPT"`
- 设置 `formatted_value = value`

**示例 — 条件赋值：**

```python
# Set invoice ID
set_field_value(document_data, "invoice_id", "INV-2026-001")

# With remove_link: removes OCR link (coords, confidence etc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**执行结果：** 字段值会更新，并标记为由脚本修改。如果字段不存在，会自动创建该字段，并设置 `extraction_method: "SCRIPT"`，然后将其添加到 `fields` 和 `fields_dict` 中。

---

## set\_date\_value() <a id="set_date_value"></a>

设置日期值，并自动格式化，还可选择执行日期运算。

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `value` | `str` | ISO 日期：`"2026-03-25"`。如果为空：使用今天的日期 |
| `add_days` | `int` | 要增加的天数（例如，付款期限为 `30` 天） |
| `skip_weekend` | `bool` | 增加天数时跳过周末 |
| `exclude_final_days` | `str/list` | 要额外排除的日期（例如，`"MONDAY,FRIDAY"`） |

**示例 — 计算付款到期日（30 天，不含周末）：**

```python
# Due date: 30 days after invoice date, skip weekends
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Set delivery date to today
set_date_value(document_data, "delivery_date", None)  # None = today

# 14 days, excluding Saturday and Monday
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**执行结果：** 计算日期时会增加相应天数（可选择跳过周末或指定日期），并根据文档的 `date_format_pattern` 自动格式化（例如，德国使用 `%d.%m.%Y`）。

**`exclude_final_days` 的日期代码：**
`MONDAY`、`TUESDAY`、`WEDNESDAY`、`THURSDAY`、`FRIDAY`、`SATURDAY`、`SUNDAY`

---

## set\_amount\_value() <a id="set_amount_value"></a>

设置金额值，并自动按区域格式进行格式化。

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `value` | `str/number` | 英文格式的金额（例如，`"1234.56"`） |

**示例 — 设置净额：**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value becomes e.g., "1.234,56" for de_DE locale
```

**执行结果：** 金额会根据 `document_json` 中的 `amount_format_locale` 格式化（例如，`de_DE`、`en_US`）。

---

## create\_new\_field()

创建新的字段字典（不会将其添加到文档中）。

```python
create_new_field(field_name, value="")
```

**返回值：** 包含 `name`、`value`、`formatted_value`、`extraction_method: "SCRIPT"` 的字典

**示例：**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**更简单的替代方案：** 使用 `set_field_value()` 代替——如果字段不存在，它会自动创建字段。只有在需要手动操作字段字典时，才需要使用 `create_new_field()`。
{% endhint %}

---

## delete\_field()

从文档中移除字段。

```python
delete_field(document_data, field_name)
```

**返回值：** 删除后包含 `(doc_json, fields_dict)` 的元组

**示例：**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid() <a id="set_field_as_invalid"></a>

将字段标记为无效，并附上错误消息。

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `message` | `str` | 错误消息（显示在界面中） |
| `code` | `str` | 错误代码（默认值：`INVALID_VALUE`） |

**副作用：**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**示例 — IBAN 验证：**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**执行结果：** 在验证界面中，字段会以红色高亮显示，并向用户展示错误消息。

---

## set\_field\_as\_valid() <a id="set_field_as_valid"></a>

移除字段的无效状态。

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**示例：**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**执行结果：** 移除 `invalidated_by_script`、`validation_message`、`validation_code`，并设置 `is_valid = True`。

---

## set\_field\_attribute()

设置字段的任意属性。

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**示例：**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

下方列出了完整的[支持的属性](#supported-attributes)。

---

## set\_is\_required() <a id="set_is_required"></a>

将字段设为必填，或取消必填要求。

```python
set_is_required(document_data, field_name, value)
```

**示例 — 采购发票必须填写采购订单编号：**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

将字段设为只读或可编辑。

```python
set_is_readonly(document_data, field_name, value)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = 只读，`False` = 可编辑，`None` = 移除属性 |

**示例：**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden() <a id="set_is_hidden"></a>

在界面中隐藏或显示字段。

```python
set_is_hidden(document_data, field_name, value)
```

**示例 — 仅在相关时显示子组织字段：**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

强制对字段进行手动验证。

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = 强制验证，`False` = 移除 |
| `reset_validation` | `bool` | 如果为 `True`：将 `is_validated` 重置为 `False` |

**当 `value=True` 时的副作用：**
- `force_validation = True`
- 如果尚未验证，则设置 `is_valid = False`
- `validation_code = "FORCED_VALIDATION"`

**示例 — 强制验证高额金额：**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## 支持的属性 <a id="supported-attributes"></a>

### 核心字段属性

| 属性 | 类型 | 描述 |
| --------- | ---- | ----------- |
| `value` | any | 原始字段值 |
| `formatted_value` | string | 格式化后用于显示的值 |
| `content` | string | 原始提取内容 |
| `is_required` | bool | 字段是否为必填项 |
| `is_valid` | bool | 验证状态 |
| `is_validated` | bool | 用户是否已验证字段 |
| `is_readonly` | bool | 字段是否为只读 |
| `is_hidden` | bool | 字段是否在界面中隐藏 |
| `force_validation` | bool | 强制用户验证此字段 |
| `highlight_field` | bool | 在界面中高亮显示字段 |
| `extraction_method` | string | 值的提取方式（例如，`"SCRIPT"`） |

### 验证属性

| 属性 | 类型 | 描述 |
| --------- | ---- | ----------- |
| `validation_message` | string | 向用户显示的错误消息 |
| `validation_code` | string | 错误代码（例如，`"FORCED_VALIDATION"`、`"INVALID_VALUE"`） |
| `invalidated_by_script` | bool | 标记字段由脚本设为无效 |

### 提取/OCR 属性

| 属性 | 类型 | 描述 |
| --------- | ---- | ----------- |
| `coords` | object | 文档上的边界框坐标 |
| `confidence` | float | OCR/提取置信度分数 |
| `score` | float | 匹配/验证分数 |
| `score_description` | string | 分数说明 |
| `page` | int | 找到字段的页码 |
| `rule` | string | 应用的提取规则 |
