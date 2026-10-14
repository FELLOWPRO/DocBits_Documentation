# Fehlende Felder aus der Dokumenthistorie füllen

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert die Lizenz `OPENSEARCH_ENABLED`.
{% endhint %}

## Was macht dieses Skript?

Wenn ein Dokument eine Bestellnummer hat, aber der Lieferantenname fehlt, durchsucht dieses Skript das Dokumentarchiv nach anderen Rechnungen mit derselben Bestellnummer und übernimmt den Lieferantennamen aus dem ersten Treffer.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

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

## Schritt-für-Schritt-Erklärung

1. **Bestellnummer und Lieferant lesen** aus dem aktuellen Dokument
2. **Bedingung prüfen**: Nur fortfahren, wenn die Bestellnummer vorhanden, der Lieferant aber leer ist
3. **Das Archiv durchsuchen** nach Dokumenten, die die Bestellnummer enthalten
4. **Lieferantennamen übernehmen** aus dem ersten Treffer, bei dem ein Lieferantenname gesetzt ist

## Variante: Mehrere Felder füllen

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

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwert lesen
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — OCR-Text aller Dokumente durchsuchen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Feldwert schreiben
