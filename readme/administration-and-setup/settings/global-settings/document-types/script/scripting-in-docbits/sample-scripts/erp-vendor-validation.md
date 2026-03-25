# ERP-Lieferanten-Validierung

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert `OPENSEARCH_ENABLED` Lizenz.
{% endhint %}

## Was macht dieses Skript?

Prüft, ob der Lieferant auf der Rechnung in den ERP-Stammdaten existiert, die in OpenSearch indiziert sind.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Lieferant nicht in ERP-Stammdaten gefunden"
        )
```

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
