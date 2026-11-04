# Duplikat-Rechnungserkennung

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert `OPENSEARCH_ENABLED` Lizenz.
{% endhint %}

## Was macht dieses Skript?

Durchsucht das Dokumentarchiv nach vorhandenen Rechnungen mit derselben Rechnungsnummer vom selben Lieferanten.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    existing = fulltext_search(
        inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Mögliches Duplikat: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
