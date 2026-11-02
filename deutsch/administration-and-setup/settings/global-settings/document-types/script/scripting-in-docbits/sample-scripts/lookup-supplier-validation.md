# Lieferanten-Lookup-Validierung

## Was macht dieses Skript?

Validiert die Lieferantennummer der Rechnung gegen die Stammdaten in der Lookup-Tabelle. Wenn der Lieferant gefunden wird, werden Name und Zahlungsbedingungen automatisch ausgefüllt. Wenn nicht gefunden, wird das Feld als ungültig markiert, damit der Benutzer es korrigieren kann.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Lieferanten-ID aus dem Dokument lesen
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Lieferanten-Lookup-Tabelle abfragen
    records = get_lookup_records(
        org_id,                                    # Aktuelle Organisation
        document_json.get("sub_org_id"),           # Sub-Org (falls zutreffend)
        "supplier",                                # Name der Lookup-Tabelle
        [["VENDOR_ID", supplier_id]],              # Filter: exakte Übereinstimmung auf VENDOR_ID
        limit=1                                    # Nur den ersten Treffer benötigt
    )

    if records:
        # Lieferant gefunden — zugehörige Felder automatisch ausfüllen
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Lieferant nicht gefunden — als ungültig markieren
        set_field_as_invalid(document_data, "supplier_id",
                             f"Lieferant '{supplier_id}' nicht in Stammdaten gefunden")
```

## Schritt-für-Schritt-Erklärung

1. **Lieferanten-ID lesen** aus dem Dokument mit `get_field_value()`
2. **Lookup-Tabelle abfragen** mit `get_lookup_records()` unter Verwendung der Lieferanten-ID als Filter
3. **Bei Treffer**: Lieferantenname und Zahlungsbedingungen aus Stammdaten automatisch ausfüllen
4. **Bei keinem Treffer**: Lieferanten-ID-Feld mit einer aussagekräftigen Fehlermeldung als ungültig markieren

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwert lesen
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Stammdaten abfragen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Feldwert schreiben
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validierungsfehler anzeigen
