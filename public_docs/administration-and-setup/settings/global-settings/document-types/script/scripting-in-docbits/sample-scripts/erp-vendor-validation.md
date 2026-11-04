# ERP 供应商验证

{% hint style="info" %}
**从版本 11.48.0 起可用** — 需要 `OPENSEARCH_ENABLED` 许可证。
{% endhint %}

## 此脚本的作用

验证发票上的供应商是否存在于已编入 OpenSearch 索引的 ERP 主数据中。如果在 ERP 中找不到该供应商，则会将该字段标记为无效。此脚本通过搜索 ERP 索引而非查找表，补充现有的 `is_supplier_valid()` 函数。

## 触发条件

文档类型为 **INVOICE** 时触发 `AFTER_FORMATTING`

## 完整脚本

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## 变体：使用供应商编号进行验证

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Auto-fill vendor name from ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## 分步说明

1. **读取供应商名称**：从当前文档中读取
2. **搜索 ERP 主数据**：使用 `fulltext_search_erp()`，并按实体类型 `"vendor"` 筛选
3. **如果未找到**：将供应商名称字段标记为无效
4. **变体**：按供应商编号搜索，并使用 ERP 数据自动填充供应商名称

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — 搜索 ERP 主数据
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — 显示验证错误
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 写入字段值
