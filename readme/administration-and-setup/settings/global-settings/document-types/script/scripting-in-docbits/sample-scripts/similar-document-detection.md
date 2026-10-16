# 相似文档检测（向量搜索）

{% hint style="info" %}
**自版本 11.48.0 起可用** — 需要 `OPENSEARCH_ENABLED` 许可证。
{% endhint %}

## 此脚本的作用

使用基于向量的相似性搜索，查找与当前文档在语义上相似的文档。如果找到相似度超过 95% 的文档，则会将发票编号标记为可能存在欺诈或重复。

## 触发器

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## 分步说明

1. **获取当前文档 ID**：从 `document_json` 获取
2. **查找相似文档**：通过 `vector_search()` 返回最近的 5 个邻居
3. **检查相似度阈值**：如果任何文档的相似度超过 95%，则将其标记
4. **标记为无效**：附上相似文档的名称和相似度分数

## 向量搜索的工作原理

每个文档的 OCR 文本在建立索引时都会转换为 384 维向量嵌入。`vector_search()` 使用 k-NN（k-最近邻）在此向量空间中查找最近邻，返回内容在语义上相似的文档，即使具体用词不同也能找到。

**使用场景：**
- 欺诈检测（来自不同“供应商”的几乎相同的发票）
- 超越精确文本匹配的重复项检测
- 跨不同格式或语言查找相关文档

## 使用的函数

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — 查找语义相似的文档
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — 显示验证错误
