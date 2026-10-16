# 供应商查询验证

## 此脚本的作用是什么？

将发票中的供应商编号与查询表中的主数据进行验证。如果找到该供应商，系统会自动填入其名称和付款条款。如果未找到，则会将该字段标记为无效，以便用户更正。

## 触发条件

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
# Read supplier ID from the document
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Query the supplier lookup table
    records = get_lookup_records(
        org_id,                                    # Current organization
        document_json.get("sub_org_id"),           # Sub-org (if applicable)
        "supplier",                                # Lookup table name
        [["VENDOR_ID", supplier_id]],              # Filter: exact match on VENDOR_ID
        limit=1                                    # Only need the first match
    )

    if records:
        # Supplier found — auto-fill related fields
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Supplier not found — mark as invalid
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## 分步说明

1. **读取供应商 ID**：使用 `get_field_value()` 从文档中读取
2. **查询查询表**：使用 `get_lookup_records()` 并将供应商 ID 作为筛选条件
3. **找到匹配项时**：从主数据自动填入供应商名称和付款条款
4. **未找到匹配项时**：将供应商 ID 字段标记为无效，并显示描述性错误消息

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — 查询主数据
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 写入字段值
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — 显示验证错误
