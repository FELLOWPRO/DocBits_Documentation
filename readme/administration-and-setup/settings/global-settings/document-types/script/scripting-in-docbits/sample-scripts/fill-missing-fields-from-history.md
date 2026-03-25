# Fehlende Felder aus Dokumenthistorie füllen

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert `OPENSEARCH_ENABLED` Lizenz.
{% endhint %}

## Was macht dieses Skript?

Wenn ein Dokument eine Bestellnummer hat, aber der Lieferantenname fehlt, durchsucht dieses Skript das Dokumentarchiv nach anderen Rechnungen mit derselben Bestellnummer und übernimmt den Lieferantennamen.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
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

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
