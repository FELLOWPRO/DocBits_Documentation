# Field Functions

Functions for reading, writing, and controlling document fields.

**Source:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Reads the value of a field from the document.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | The `document_data` context object |
| `field_name` | `str` | Name of the field (e.g., `"invoice_id"`) |
| `default_value` | `any` | Return value if field is empty/missing (default: `None`) |
| `is_clean` | `bool` | If `True`: value is converted to UPPERCASE with spaces removed |

**Returns:** The field value as string, or `default_value`

**Example — Read invoice number with fallback:**

```python
# Read field with default value
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# With is_clean=True: "INV 001" becomes "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**What happens:** Returns the field value. When `is_clean=True`, the value is transformed via `value.upper().replace(" ", "").strip()` — useful for comparisons.

---

## set\_field\_value()

Sets the value of a field. Automatically creates the field if it does not exist.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | The `document_data` context object |
| `field_name` | `str` | Name of the field |
| `value` | `any` | New value |
| `remove_link` | `bool` | If `True`: removes coords, confidence, rule, etc. |

**Returns:** `True` if value changed, `False` if identical

**Side effects:**
- Sets `highlight_field = True` (visual indicator in UI)
- Sets `extraction_method = "SCRIPT"`
- Sets `formatted_value = value`

**Example — Conditional value assignment:**

```python
# Set invoice ID
set_field_value(document_data, "invoice_id", "INV-2026-001")

# With remove_link: removes OCR link (coords, confidence etc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**What happens:** The field value is updated and marked as script-modified. If the field does not exist, it is automatically created with `extraction_method: "SCRIPT"` and added to both `fields` and `fields_dict`.

---

## set\_date\_value()

Sets a date value with automatic formatting and optional date arithmetic.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `value` | `str` | ISO date: `"2026-03-25"`. If empty: today's date |
| `add_days` | `int` | Days to add (e.g., `30` for payment terms) |
| `skip_weekend` | `bool` | Skip weekends when adding days |
| `exclude_final_days` | `str/list` | Additional days to exclude (e.g., `"MONDAY,FRIDAY"`) |

**Example — Calculate payment due date (30 days, no weekends):**

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

**What happens:** The date is calculated by adding days (optionally skipping weekends/specific days) and automatically formatted according to the document's `date_format_pattern` (e.g., `%d.%m.%Y` for Germany).

**Day codes for `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Sets an amount value with automatic locale formatting.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `value` | `str/number` | Amount in English format (e.g., `"1234.56"`) |

**Example — Set net amount:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value becomes e.g., "1.234,56" for de_DE locale
```

**What happens:** The amount is formatted according to `amount_format_locale` from `document_json` (e.g., `de_DE`, `en_US`).

---

## create\_new\_field()

Creates a new field dictionary (without adding it to the document).

```python
create_new_field(field_name, value="")
```

**Returns:** Dict with `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Example:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Simpler alternative:** Use `set_field_value()` instead — it automatically creates the field if it does not exist. `create_new_field()` is only needed when you want to manually manipulate the field dict.
{% endhint %}

---

## delete\_field()

Removes a field from the document.

```python
delete_field(document_data, field_name)
```

**Returns:** Tuple `(doc_json, fields_dict)` after deletion

**Example:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Marks a field as invalid with an error message.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `message` | `str` | Error message (displayed in UI) |
| `code` | `str` | Error code (default: `INVALID_VALUE`) |

**Side effects:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Example — IBAN validation:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**What happens:** The field is highlighted red in the validation screen with the error message displayed to the user.

---

## set\_field\_as\_valid()

Removes the invalid status from a field.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Example:**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**What happens:** Removes `invalidated_by_script`, `validation_message`, `validation_code` and sets `is_valid = True`.

---

## set\_field\_attribute()

Sets an arbitrary attribute on a field.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Example:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

See the full list of [Supported Attributes](#supported-attributes) below.

---

## set\_is\_required()

Makes a field mandatory or removes the requirement.

```python
set_is_required(document_data, field_name, value)
```

**Example — PO number required for purchase invoices:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Makes a field read-only or editable.

```python
set_is_readonly(document_data, field_name, value)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = readonly, `False` = editable, `None` = remove attribute |

**Example:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Hides or shows a field in the UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Example — Show sub-org fields only when relevant:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Forces manual validation for a field.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = force validation, `False` = remove |
| `reset_validation` | `bool` | If `True`: resets `is_validated` back to `False` |

**Side effects when `value=True`:**
- `force_validation = True`
- `is_valid = False` (if not yet validated)
- `validation_code = "FORCED_VALIDATION"`

**Example — Force validation for high amounts:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Supported Attributes

### Core Field Attributes

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `value` | any | The raw field value |
| `formatted_value` | string | Display-formatted value |
| `content` | string | Original extracted content |
| `is_required` | bool | Whether field is mandatory |
| `is_valid` | bool | Validation status |
| `is_validated` | bool | Whether field has been validated by user |
| `is_readonly` | bool | Whether field is read-only |
| `is_hidden` | bool | Whether field is hidden in UI |
| `force_validation` | bool | Force user to validate this field |
| `highlight_field` | bool | Highlight field in UI |
| `extraction_method` | string | How value was extracted (e.g., `"SCRIPT"`) |

### Validation Attributes

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `validation_message` | string | Error message shown to user |
| `validation_code` | string | Error code (e.g., `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Marks field as invalidated by script |

### Extraction/OCR Attributes

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `coords` | object | Bounding box coordinates on document |
| `confidence` | float | OCR/extraction confidence score |
| `score` | float | Match/validation score |
| `score_description` | string | Description of the score |
| `page` | int | Page number where field was found |
| `rule` | string | Extraction rule that was applied |
