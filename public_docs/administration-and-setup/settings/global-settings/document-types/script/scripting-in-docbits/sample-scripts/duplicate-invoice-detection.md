# 重复发票检测

{% hint style="info" %}
**自版本 11.48.0 起提供** — 需要 `OPENSEARCH_ENABLED` 许可证。
{% endhint %}

## 此脚本的作用

在文档档案中搜索同一供应商开具的、发票编号相同的现有发票。如果发现可能的重复项，则将发票编号字段标记为无效，并显示一条警告，其中包含重复文档的名称和状态。

## 触发器

文档类型 **INVOICE** 的 `AFTER_FORMATTING`

## 完整脚本

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Search for documents with the same invoice number from the same vendor
    existing = fulltext_search(
        inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Exclude the current document from results
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## 分步说明

1. **读取发票编号和供应商**，从当前文档中获取
2. **搜索档案**，使用 `fulltext_search()` 按供应商名称和相关状态筛选
3. **排除当前文档**，避免与自身匹配
4. **标记为无效**，如果发现重复项，则显示现有文档的文件名和状态

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — 搜索所有文档中的 OCR 文本
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — 显示验证错误
