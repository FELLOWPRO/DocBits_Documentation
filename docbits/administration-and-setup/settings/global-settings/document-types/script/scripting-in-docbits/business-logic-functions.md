# Business Logic Functions

Functions for lookups, PO matching, tasks, user/group management, and status changes.

**Source:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Queries master data from lookup tables (suppliers, items, GL accounts, etc.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organization UUID |
| `sub_org_id` | `str/None` | Sub-organization UUID (or `None`) |
| `lookup_name` | `str` | Name of the lookup (e.g., `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Filter conditions (see formats below) |
| `skip` | `int` | Offset for pagination (default: 0) |
| `limit` | `int` | Max results (default: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (default: `True`) |
| `sort_order` | `list` | Sorting (optional) |

### Filter Formats

Three formats are supported:

```python
# Format 1: Dict with field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2: Tuple/List with 2 elements (field, value) → operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3: Tuple/List with 3 elements (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sorting

```python
# Format 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Tuple/List
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Example — Lookup supplier by vendor ID:**

```python
# Find supplier by vendor ID
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Example — Search GL accounts with multiple filters:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Internally uses `search_operator="SMART"` which supports fuzzy matching.
{% endhint %}

---

## is\_supplier\_valid()

Checks if a supplier exists in the lookup data.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | The `user` context object |
| `filter_data_json` | `dict` | Filter in format `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sub-organization |

**Returns:** `True` if at least 1 match, otherwise `False`

**Example — Validate supplier:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Supplier not found in master data")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Triggers automatic PO matching via the po-match-service microservice.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Must be a real user object |
| `document_data` | `dict` | Document context |
| `po_numbers` | `str/list` | PO numbers (comma-separated or list) |

**Returns:** Updated `document_data` with `po_items`, `po_match_status`, `po_multi_matched`

**Example — Auto-match PO:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Duplicate protection:** Already verified PO numbers are stored in `already_verified_po_numbers` and will not be matched again.
{% endhint %}

---

## get\_next\_sequence\_number()

Gets and atomically increments a sequence number in the database.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organization UUID |
| `sequence_name` | `str` | Must contain `"sequence"` (e.g., `"invoice_sequence"`) |
| `default_value` | `int` | Start value when sequence is newly created |

**Returns:** `int` — the next number, or `None` if name is invalid

**Example — Generate internal document number:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Naming rule:** The `sequence_name` must start or end with "sequence", or contain "SEQUENCE\_". Otherwise the function returns `None`.
{% endhint %}

---

## create\_document\_task()

Creates a task for the current document.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | User context |
| `title` | `str` | Task title |
| `description` | `str` | Description |
| `priority` | `str/int` | Priority |
| `assigned_to_user_id` | `str/None` | Assigned user |
| `assigned_to_group_id` | `str/None` | Assigned group |
| `send_email` | `bool` | Send email notification |

**Example — Create task for high-amount invoices:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="High invoice amount - review required",
        description=f"Invoice amount: {amount} exceeds 50,000 threshold",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Assigns a sub-organization to a document.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Side effects:**
- Sets `sub_org_id` in `document_json`
- Saves directly to the database (if `doc_id` is present)

**Example — Route based on supplier:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Changes the status of a document.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `doc_id` | `str` | Document UUID |
| `status` | `str` | New status (e.g., `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Status message |
| `doc_classification_class` | `str/None` | For `CLASSIFIED` status: new document type |

**Example — Set document to error status:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**Caution:** Status changes trigger downstream actions (DocFlow workflows, status-change hooks). Only use when necessary.
{% endhint %}

---

## get\_document\_content()

Returns the full OCR text of the document.

```python
get_document_content(document_data)
```

**Returns:** `str` — Concatenated text of all pages

**Example — Search fulltext for keywords:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regex search in fulltext
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
The result is cached for 60 seconds (TTL cache with max 128 entries).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Looks up a user by ID or email.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Returns:** `UsersCache` object with attributes like `.email`, `.first_name`, `.last_name`, `.user_id`

**Example — Assign task to specific user:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Review required",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Looks up a user group by ID or name.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Returns:** `GroupCache` object

**Example — Find group for task assignment:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approval needed",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Intelligent value comparison with type conversion.

```python
compare_values(value1, value2)
```

**Comparison logic:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Strings that are numbers → numeric comparison (`"1.0" == "1.00"` → `True`)
4. Strings → case-insensitive, space-insensitive (`"ABC " == " abc"` → `True`)
5. Bool vs String → string comparison (`True == "true"` → `True`)
6. Decimal comparison as fallback

**Example — Verify amounts match:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

Retrieves List-of-Values (LOV) entries.

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organization UUID |
| `key` | `str` | LOV key |
| `return_type` | `str` | `"list_of_objects"` or `"list_of_values"` |
| `sub_org_id` | `str/None` | Optional sub-organization filter |
| `language_code` | `str` | Language code (e.g., `"en"`, `"de"`) |

**Returns:** LOV values as a list of objects or as a flat list.

**Example — Get configured tax codes:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
