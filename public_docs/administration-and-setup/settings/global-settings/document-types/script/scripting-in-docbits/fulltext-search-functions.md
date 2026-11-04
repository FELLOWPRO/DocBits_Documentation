# Fulltext & Vector Search Functions

{% hint style="info" %}
**Available from version 11.48.0**

These functions require the **OPENSEARCH\_ENABLED** license/preference to be activated for your organization. Without it, all functions throw a `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Functions for searching document archives, finding similar documents, and querying ERP master data. These search across **all documents** of the organization — unlike `get_document_content()` which only reads the current document's text.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Source:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Searches the full OCR text of **all documents** in the organization. Finds text in `pages.pageText`, `tfidfCustomPageText` and `ai_text` fields via the fulltextsearch microservice.

```python
fulltext_search(query, **kwargs)
```

**Parameters:**

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | required | Search term (searched in OCR text of all documents) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (exact phrase), `"fuzzy"` (typo-tolerant, up to 2 char difference), `"prefix"` (starts with) |
| `doc_type` | `str` | `None` | Filter by document type (comma-separated, e.g. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filter by document status (comma-separated, e.g. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filter by vendor name |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Max results (capped at 50) |

**Returns:** `list[dict]` — Each dict contains:

| Field | Description |
| ----- | ----------- |
| `doc_id` | Document UUID |
| `name` | Filename (e.g. `"INV-2026-001.pdf"`) |
| `doc_type` | Document type (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Vendor name |
| `status` | Document status |
| `total_amount` | Total amount |
| `ocr_content` | Matched text excerpt from the document |
| `highlights` | Dict with highlighted matches per field |

**Example — Search for exact phrase:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Example — Fuzzy search (OCR typo tolerant):**

```python
# Finds "REVERSE CHARGE" even with OCR errors like "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Example — Prefix search:**

```python
# Finds all documents containing words starting with "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Empty query:** Passing an empty string returns `[]` immediately without making an HTTP call.
{% endhint %}

{% hint style="info" %}
**Error handling:** If the fulltextsearch service is unreachable, the function returns `[]` and logs a warning. It does **not** throw an exception.
{% endhint %}

---

## vector\_search()

Finds semantically similar documents using vector embeddings (k-NN search with 384-dimensional vectors). Useful for finding documents with similar content regardless of exact wording.

```python
vector_search(doc_id, **kwargs)
```

**Parameters:**

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | required | Source document UUID (the document to find similar matches for) |
| `k` | `int` | `5` | Number of similar documents to return (capped at 50) |

**Returns:** `list[dict]` — Each dict contains:

| Field | Description |
| ----- | ----------- |
| `doc_id` | Similar document UUID |
| `name` | Filename |
| `doc_type` | Document type |
| `similarity_score` | Raw similarity score (0-1) |
| `similarity_percent` | Similarity as percentage (0-100) |

**Example — Find similar documents:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**How it works:** Each document is converted to a 384-dimensional vector when indexed. The vector search finds the nearest neighbors in this vector space, which correspond to semantically similar documents.
{% endhint %}

---

## fulltext\_search\_erp()

Searches ERP master data (vendors, purchase orders, customers, materials) indexed in OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Parameters:**

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | required | Search term |
| `entity_types` | `str` | `None` | Filter by entity type (comma-separated: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filter by vendor number |
| `vendor_name` | `str` | `None` | Filter by vendor name |
| `company_code` | `str` | `None` | Filter by company code |
| `size` | `int` | `10` | Max results (capped at 50) |

**Returns:** `list[dict]` — Entity-type-specific fields (vendor records have `vendor_number`, `vendor_name`, etc.)

**Example — Validate vendor in ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Example — Search purchase orders:**

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

Returns autocomplete suggestions for search terms. Groups results by category (vendors, filenames, invoice numbers).

```python
fulltext_suggestions(query, **kwargs)
```

**Parameters:**

| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | required | Prefix / search term |
| `limit` | `int` | `10` | Max suggestions per category (capped at 20) |

**Returns:** `dict` with grouped suggestions:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Example — Get vendor suggestions:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Empty query:** Passing an empty string returns `{}` immediately.
{% endhint %}

---

## Quick Reference

| Function | Purpose | Returns |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | Search OCR text across all documents | `list[dict]` |
| `vector_search(doc_id, ...)` | Find semantically similar documents | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Search ERP master data | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Autocomplete suggestions | `dict` |

---

## Common Patterns

### License Check

All four functions automatically check the `OPENSEARCH_ENABLED` preference. If not enabled:

```python
# This will raise RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

To handle this gracefully in scripts:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch not enabled for this org — skip search
    results = []
```

### Combining with Field Functions

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
