# Ähnliche Dokumente erkennen (Vektorsuche)

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert `OPENSEARCH_ENABLED` Lizenz.
{% endhint %}

## Was macht dieses Skript?

Verwendet vektorbasierte Ähnlichkeitssuche, um semantisch ähnliche Dokumente zu finden. Bei mehr als 95% Ähnlichkeit wird die Rechnungsnummer als potenziell doppelt markiert.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ ähnlich zu: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Verwendete Funktionen

- [vector\_search()](../fulltext-search-functions.md#vector\_search)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
