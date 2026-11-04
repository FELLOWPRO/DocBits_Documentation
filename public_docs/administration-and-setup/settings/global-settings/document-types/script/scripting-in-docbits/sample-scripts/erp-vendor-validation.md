# ERP-Lieferanten-Validierung

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert die Lizenz `OPENSEARCH_ENABLED`.
{% endhint %}

## Was macht dieses Skript?

Prüft, ob der Lieferant auf der Rechnung in den ERP-Stammdaten existiert, die in OpenSearch indiziert sind. Wird der Lieferant im ERP nicht gefunden, wird das Feld als ungültig markiert. Dies ergänzt die bestehende Funktion `is_supplier_valid()`, indem der ERP-Index statt der Lookup-Tabelle durchsucht wird.

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
            "Vendor not found in ERP master data"
        )
```

## Variante: Mit Lieferantennummer validieren

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Auto-fill vendor name from ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Schritt-für-Schritt-Erklärung

1. **Lieferantennamen lesen** aus dem aktuellen Dokument
2. **ERP-Stammdaten durchsuchen** mit `fulltext_search_erp()` und dem Filter auf den Entitätstyp `"vendor"`
3. **Wenn nicht gefunden**: Das Feld für den Lieferantennamen als ungültig markieren
4. **Variante**: Nach der Lieferantennummer suchen und den Lieferantennamen aus den ERP-Daten automatisch eintragen

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwert lesen
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — ERP-Stammdaten durchsuchen
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validierungsfehler anzeigen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Feldwert schreiben
