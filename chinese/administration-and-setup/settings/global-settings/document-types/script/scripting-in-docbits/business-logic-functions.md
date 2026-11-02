# 业务逻辑函数

用于查找、采购订单匹配、任务、用户/组管理和状态更改的函数。

**来源：** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records() <a id="get_lookup_records"></a>

从查找表中查询主数据（供应商、物料、总账科目等）。

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `org_id` | `str` | 组织 UUID |
| `sub_org_id` | `str/None` | 子组织 UUID（或 `None`） |
| `lookup_name` | `str` | 查找表名称（例如 `"supplier"`、`"item"`、`"gl_account"`） |
| `filters` | `list` | 筛选条件（参见下方格式） |
| `skip` | `int` | 分页偏移量（默认值：0） |
| `limit` | `int` | 最大结果数（默认值：100） |
| `match_all` | `bool` | `True` = AND，`False` = OR（默认值：`True`） |
| `sort_order` | `list` | 排序（可选） |

### 筛选格式

支持三种格式：

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

### 排序

```python
# Format 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Tuple/List
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**示例 — 按供应商 ID 查找供应商：**

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

**示例 — 使用多个筛选条件搜索总账科目：**

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
内部使用支持模糊匹配的 `search_operator="SMART"`。
{% endhint %}

---

## is\_supplier\_valid()

检查查找数据中是否存在某个供应商。

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | `user` 上下文对象 |
| `filter_data_json` | `dict` | 格式为 `{"match_all": True, "filters": [...]}` 的筛选条件 |
| `sub_org_id` | `str/None` | 子组织 |

**返回值：** 如果至少匹配 1 条记录，则返回 `True`；否则返回 `False`

**示例 — 验证供应商：**

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

## auto\_po\_match\_for\_purchase\_orders() <a id="auto_po_match_for_purchase_orders"></a>

通过 po-match-service 微服务触发自动采购订单匹配。

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | 必须是真实的用户对象 |
| `document_data` | `dict` | 文档上下文 |
| `po_numbers` | `str/list` | 采购订单编号（逗号分隔的字符串或列表） |

**返回值：** 更新后的 `document_data`，包含 `po_items`、`po_match_status`、`po_multi_matched`

**示例 — 自动匹配采购订单：**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**重复保护：** 已验证的采购订单编号会存储在 `already_verified_po_numbers` 中，不会再次进行匹配。
{% endhint %}

---

## get\_next\_sequence\_number()

从数据库获取并原子递增序列号。

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `org_id` | `str` | 组织 UUID |
| `sequence_name` | `str` | 必须包含 `"sequence"`（例如 `"invoice_sequence"`） |
| `default_value` | `int` | 新建序列时的起始值 |

**返回值：** `int` — 下一个编号；如果名称无效，则返回 `None`

**示例 — 生成内部文档编号：**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**命名规则：** `sequence_name` 必须以 "sequence" 开头或结尾，或者包含 "SEQUENCE\_"。否则函数会返回 `None`。
{% endhint %}

---

## create\_document\_task() <a id="create_document_task"></a>

为当前文档创建任务。

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | 用户上下文 |
| `title` | `str` | 任务标题 |
| `description` | `str` | 描述 |
| `priority` | `str/int` | 优先级 |
| `assigned_to_user_id` | `str/None` | 指定用户 |
| `assigned_to_group_id` | `str/None` | 指定组 |
| `send_email` | `bool` | 发送电子邮件通知 |

**示例 — 为金额较高的发票创建任务：**

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

为文档指定子组织。

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**副作用：**
- 在 `document_json` 中设置 `sub_org_id`
- 直接保存到数据库（如果存在 `doc_id`）

**示例 — 根据供应商进行路由：**

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

## update\_document\_status\_with\_doc\_id() <a id="update_document_status_with_doc_id"></a>

更改文档状态。

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `doc_id` | `str` | 文档 UUID |
| `status` | `str` | 新状态（例如 `"error"`、`"ready_for_validation"`） |
| `message` | `str/None` | 状态消息 |
| `doc_classification_class` | `str/None` | 用于 `CLASSIFIED` 状态：新的文档类型 |

**示例 — 将文档设为错误状态：**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**注意：** 状态更改会触发下游操作（DocFlow 工作流、状态更改钩子）。仅在必要时使用。
{% endhint %}

---

## get\_document\_content() <a id="get_document_content"></a>

返回文档的完整 OCR 文本。

```python
get_document_content(document_data)
```

**返回值：** `str` — 所有页面的拼接文本

**示例 — 在全文中搜索关键词：**

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
结果会缓存 60 秒（TTL 缓存，最多 128 个条目）。
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

按 ID 或电子邮件查找用户。

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**返回值：** `UsersCache` 对象，包含 `.email`、`.first_name`、`.last_name`、`.user_id` 等属性

**示例 — 将任务分配给指定用户：**

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

## get\_group\_by\_id() / get\_group\_by\_name() <a id="get_group_by_id--get_group_by_name"></a>

按 ID 或名称查找用户组。

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**返回值：** `GroupCache` 对象

**示例 — 查找用于分配任务的组：**

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

支持类型转换的智能值比较。

```python
compare_values(value1, value2)
```

**比较逻辑：**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. 数字字符串 → 数值比较（`"1.0" == "1.00"` → `True`）
4. 字符串 → 忽略大小写和空格（`"ABC " == " abc"` → `True`）
5. 布尔值与字符串 → 字符串比较（`True == "true"` → `True`）
6. 兜底使用十进制比较

**示例 — 验证金额是否匹配：**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

检索值列表（LOV）条目。

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**参数：**

| 名称 | 类型 | 描述 |
| ---- | ---- | ----------- |
| `org_id` | `str` | 组织 UUID |
| `key` | `str` | LOV 键 |
| `return_type` | `str` | `"list_of_objects"` 或 `"list_of_values"` |
| `sub_org_id` | `str/None` | 可选的子组织筛选条件 |
| `language_code` | `str` | 语言代码（例如 `"en"`、`"de"`） |

**返回值：** LOV 值，以对象列表或扁平列表的形式返回。

**示例 — 获取已配置的税码：**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
