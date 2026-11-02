# Compliance Text Search (Reverse Charge)

{% hint style="info" %}
**Available from version 11.48.0** — Requires `OPENSEARCH_ENABLED` license.
{% endhint %}

## What does this script do?

Searches for compliance-relevant text like "REVERSE CHARGE" in the document archive. If matching documents exist, the tax code is automatically set. Supports both exact phrase matching and fuzzy search (typo-tolerant for OCR errors).

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

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

## Variant: Fuzzy Search (OCR Error Tolerant)

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

## Step-by-Step Explanation

1. **Search the archive** for the exact phrase "REVERSE CHARGE" using `fulltext_search()`
2. **Filter by document type** to only search invoices
3. **If found**: Automatically set the tax code field to "RC"
4. **Fuzzy variant**: Use `search_type="fuzzy"` to catch OCR misreads (up to 2 character differences)

## Functions Used

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Search OCR text across all documents
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Write field value
