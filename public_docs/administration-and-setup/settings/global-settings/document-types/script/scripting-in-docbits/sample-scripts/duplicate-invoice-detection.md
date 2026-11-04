# Duplicate Invoice Detection

{% hint style="info" %}
**Available from version 11.48.0** — Requires `OPENSEARCH_ENABLED` license.
{% endhint %}

## What does this script do?

Searches the document archive for existing invoices with the same invoice number from the same vendor. If a potential duplicate is found, the invoice number field is marked as invalid with a warning showing the duplicate document name and status.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

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

## Step-by-Step Explanation

1. **Read invoice number and vendor** from the current document
2. **Search the archive** with `fulltext_search()` filtering by vendor name and relevant statuses
3. **Exclude current document** from results to avoid self-matching
4. **Mark as invalid** if any duplicate is found, showing the filename and status of the existing document

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Search OCR text across all documents
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Show validation error
