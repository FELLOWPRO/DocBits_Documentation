# Similar Document Detection (Vector Search)

{% hint style="info" %}
**Available from version 11.48.0** — Requires `OPENSEARCH_ENABLED` license.
{% endhint %}

## What does this script do?

Uses vector-based similarity search to find documents that are semantically similar to the current one. If a document with more than 95% similarity is found, the invoice number is flagged as potentially fraudulent or duplicate.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

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

## Step-by-Step Explanation

1. **Get current document ID** from `document_json`
2. **Find similar documents** with `vector_search()` returning the 5 nearest neighbors
3. **Check similarity threshold**: If any document exceeds 95% similarity, flag it
4. **Mark as invalid** with the similar document's name and similarity score

## How Vector Search Works

Each document's OCR text is converted to a 384-dimensional vector embedding when indexed. `vector_search()` finds the nearest neighbors in this vector space using k-NN (k-Nearest Neighbors), returning documents whose content is semantically similar — even if the exact words differ.

**Use cases:**
- Fraud detection (nearly identical invoices from different "vendors")
- Duplicate detection that goes beyond exact text matching
- Finding related documents across different formats or languages

## Functions Used

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Find semantically similar documents
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Show validation error
