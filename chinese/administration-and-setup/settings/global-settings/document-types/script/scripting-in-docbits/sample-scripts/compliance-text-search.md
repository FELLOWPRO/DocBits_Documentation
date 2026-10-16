# 合规文本搜索（反向征税）

{% hint style="info" %}
**自版本 11.48.0 起可用** — 需要 `OPENSEARCH_ENABLED` 许可证。
{% endhint %}

## 此脚本的作用

在文档归档中搜索“REVERSE CHARGE”等与合规相关的文本。如果存在匹配的文档，则会自动设置税码。支持精确短语匹配和模糊搜索（可容忍 OCR 错误导致的拼写偏差）。

## 触发条件

文档类型为 **INVOICE** 时触发 `AFTER_FORMATTING`

## 完整脚本

```python
# Search for "REVERSE CHARGE" in the organization's document archive
rc_docs = fulltext_search(
    "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## 变体：模糊搜索（可容忍 OCR 错误）

```python
# Fuzzy search tolerates OCR errors like "REVERS CHARG" or "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## 分步说明

1. 使用 `fulltext_search()` 搜索精确短语“REVERSE CHARGE”
2. **按文档类型筛选**，仅搜索发票
3. **如果找到匹配项**：自动将税码字段设为“RC”
4. **模糊搜索变体**：使用 `search_type="fuzzy"`，以捕获 OCR 误读（最多可容忍 2 个字符的差异）

## 使用的函数

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — 在所有文档中搜索 OCR 文本
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 写入字段值
