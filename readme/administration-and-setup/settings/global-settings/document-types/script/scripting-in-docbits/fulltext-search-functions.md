# 全文搜索与向量搜索函数

{% hint style="info" %}
**自版本 11.48.0 起可用**

这些函数要求为您的组织启用 **OPENSEARCH\_ENABLED** 许可证/偏好设置。若未启用，所有函数都会抛出 `RuntimeError("Fulltext search license is missing")`。
{% endhint %}

用于搜索文档归档、查找相似文档以及查询 ERP 主数据的函数。这些函数会搜索组织中的**所有文档**，而 `get_document_content()` 只读取当前文档的文本。

{% hint style="success" %}
**安全性：**脚本沙箱会自动注入 `org_id`。您无需传入该参数，脚本始终只会访问您自己组织的数据。
{% endhint %}

**来源：** `module/script/helper/document_script_functions.py`

---

## fulltext\_search() <a id="fulltext_search"></a>

搜索组织中**所有文档**的完整 OCR 文本。通过全文搜索微服务在 `pages.pageText`、`tfidfCustomPageText` 和 `ai_text` 字段中查找文本。

```python
fulltext_search(query, **kwargs)
```

**参数：**

| 名称 | 类型 | 默认值 | 描述 |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | 必填 | 搜索词（在所有文档的 OCR 文本中搜索） |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"`（精确短语）、`"fuzzy"`（容错拼写，最多允许相差 2 个字符）、`"prefix"`（前缀匹配） |
| `doc_type` | `str` | `None` | 按文档类型筛选（逗号分隔，例如 `"INVOICE,CREDIT_NOTE"`） |
| `status` | `str` | `None` | 按文档状态筛选（逗号分隔，例如 `"ready_for_validation,exported"`） |
| `vendor_name` | `str` | `None` | 按供应商名称筛选 |
| `date_range` | `str` | `None` | `"last_30_days"`、`"last_90_days"`、`"last_180_days"`、`"last_365_days"` |
| `size` | `int` | `10` | 最大结果数（上限为 50） |

**返回值：**`list[dict]` — 每个字典包含：

| 字段 | 描述 |
| ----- | ----------- |
| `doc_id` | 文档 UUID |
| `name` | 文件名（例如 `"INV-2026-001.pdf"`） |
| `doc_type` | 文档类型（`"INVOICE"`、`"ORDER_CONFIRMATION"` 等） |
| `vendor_name` | 供应商名称 |
| `status` | 文档状态 |
| `total_amount` | 总金额 |
| `ocr_content` | 文档中匹配到的文本摘录 |
| `highlights` | 包含各字段高亮匹配项的字典 |

**示例 — 搜索精确短语：**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**示例 — 模糊搜索（可容忍 OCR 错误）：**

```python
# Finds "REVERSE CHARGE" even with OCR errors like "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**示例 — 前缀搜索：**

```python
# Finds all documents containing words starting with "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**空查询：**传入空字符串会立即返回 `[]`，不会发起 HTTP 调用。
{% endhint %}

{% hint style="info" %}
**错误处理：**如果全文搜索服务不可用，函数会返回 `[]` 并记录警告，不会抛出异常。
{% endhint %}

---

## vector\_search() <a id="vector_search"></a>

使用向量嵌入查找语义相似的文档（基于 384 维向量的 k-NN 搜索）。无论措辞是否完全相同，都可用于查找内容相似的文档。

```python
vector_search(doc_id, **kwargs)
```

**参数：**

| 名称 | 类型 | 默认值 | 描述 |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | 必填 | 源文档 UUID（要为其查找相似匹配项的文档） |
| `k` | `int` | `5` | 要返回的相似文档数量（上限为 50） |

**返回值：**`list[dict]` — 每个字典包含：

| 字段 | 描述 |
| ----- | ----------- |
| `doc_id` | 相似文档 UUID |
| `name` | 文件名 |
| `doc_type` | 文档类型 |
| `similarity_score` | 原始相似度分数（0-1） |
| `similarity_percent` | 相似度百分比（0-100） |

**示例 — 查找相似文档：**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**工作原理：**每份文档在建立索引时都会转换为一个 384 维向量。向量搜索会在该向量空间中查找最近邻，这些最近邻对应语义相似的文档。
{% endhint %}

---

## fulltext\_search\_erp() <a id="fulltext_search_erp"></a>

搜索已编入 OpenSearch 索引的 ERP 主数据（供应商、采购订单、客户、物料）。

```python
fulltext_search_erp(query, **kwargs)
```

**参数：**

| 名称 | 类型 | 默认值 | 描述 |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | 必填 | 搜索词 |
| `entity_types` | `str` | `None` | 按实体类型筛选（逗号分隔：`"vendor"`、`"purchase_order"`、`"customer"`、`"material"`） |
| `vendor_number` | `str` | `None` | 按供应商编号筛选 |
| `vendor_name` | `str` | `None` | 按供应商名称筛选 |
| `company_code` | `str` | `None` | 按公司代码筛选 |
| `size` | `int` | `10` | 最大结果数（上限为 50） |

**返回值：**`list[dict]` — 包含特定于实体类型的字段（供应商记录包含 `vendor_number`、`vendor_name` 等）。

**示例 — 在 ERP 中验证供应商：**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**示例 — 搜索采购订单：**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # PO found in ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

返回搜索词的自动补全建议。结果按类别分组（供应商、文件名、发票编号）。

```python
fulltext_suggestions(query, **kwargs)
```

**参数：**

| 名称 | 类型 | 默认值 | 描述 |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | 必填 | 前缀/搜索词 |
| `limit` | `int` | `10` | 每个类别的最大建议数（上限为 20） |

**返回值：**按类别分组建议的 `dict`：

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**示例 — 获取供应商建议：**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**空查询：**传入空字符串会立即返回 `{}`。
{% endhint %}

---

## 快速参考

| 函数 | 用途 | 返回值 |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | 搜索所有文档的 OCR 文本 | `list[dict]` |
| `vector_search(doc_id, ...)` | 查找语义相似的文档 | `list[dict]` |
| `fulltext_search_erp(query, ...)` | 搜索 ERP 主数据 | `list[dict]` |
| `fulltext_suggestions(query, ...)` | 自动补全建议 | `dict` |

---

## 常见模式

### 许可证检查

这四个函数都会自动检查 `OPENSEARCH_ENABLED` 偏好设置。如果未启用：

```python
# This will raise RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

在脚本中进行适当处理：

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch not enabled for this org — skip search
    results = []
```

### 与字段函数结合使用

```python
# Search → validate → set field
invoice_number = get_field_value(document_data, "invoice_id", "")
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
