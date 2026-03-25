# Compliance-Textsuche (Reverse Charge)

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert `OPENSEARCH_ENABLED` Lizenz.
{% endhint %}

## Was macht dieses Skript?

Sucht nach compliance-relevantem Text wie "REVERSE CHARGE" im Dokumentarchiv und setzt den Steuercode automatisch.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variante: Fuzzy-Suche (OCR-fehlertolerant)

```python
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Verwendete Funktionen

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
