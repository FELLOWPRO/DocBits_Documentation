# Fill Missing Fields from Document History

{% hint style="info" %}
**Available from version 11.48.0** — Requires `OPENSEARCH_ENABLED` license.
{% endhint %}

## What does this script do?

When a document has a PO number but is missing the supplier name, this script searches the document archive for other invoices containing the same PO number and copies the vendor name from the first match.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

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

## Step-by-Step Explanation

1. **Read PO number and supplier** from the current document
2. **Check condition**: Only proceed if PO exists but supplier is missing
3. **Search the archive** for documents containing the PO number
4. **Copy vendor name** from the first match that has a vendor name set

## Variant: Fill Multiple Fields

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

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Search OCR text across all documents
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Write field value
