# 从文档历史记录填充缺失字段

{% hint style="info" %}
**从版本 11.48.0 起可用** — 需要 `OPENSEARCH_ENABLED` 许可证。
{% endhint %}

## 此脚本的作用

当文档包含采购订单编号但缺少供应商名称时，此脚本会在文档归档中搜索包含相同采购订单编号的其他发票，并从第一个匹配项中复制供应商名称。

## 触发条件

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Search archive for documents with this PO number
    history = fulltext_search(
        po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## 分步说明

1. **读取采购订单编号和供应商**：从当前文档中读取
2. **检查条件**：仅当存在采购订单编号但缺少供应商时继续
3. **搜索归档**：查找包含该采购订单编号的文档
4. **复制供应商名称**：从第一个已设置供应商名称的匹配项中复制

## 变体：填充多个字段

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Also fill other fields if available
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — 搜索所有文档中的 OCR 文本
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 写入字段值
