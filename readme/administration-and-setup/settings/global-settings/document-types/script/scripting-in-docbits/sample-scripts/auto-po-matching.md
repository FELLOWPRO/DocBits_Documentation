# Automatisches PO-Matching

## Was macht dieses Skript?

Löst automatisch das PO-Matching (Bestellabgleich) aus, wenn eine Bestellnummer auf der Rechnung vorhanden ist. Der po-match-service Microservice vergleicht Rechnungspositionen mit der Bestellung und füllt die Abgleichergebnisse.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# PO-Nummer aus dem Dokument lesen
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # PO-Nummer bereinigen: Präfix und Leerzeichen entfernen
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Bereinigte PO-Nummer aktualisieren
    set_field_value(document_data, "purchase_order", po_nr)

    # Automatisches PO-Matching auslösen
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Schritt-für-Schritt-Erklärung

1. **PO-Nummer lesen** von der Rechnung
2. **Bereinigen** der PO-Nummer durch Entfernen gängiger Präfixe wie "PO-" oder "PO "
3. **Aktualisieren** der bereinigten PO-Nummer zurück ins Dokument
4. **PO-Matching auslösen**, das den po-match-service aufruft, um Rechnungspositionen mit Bestellpositionen zu vergleichen

## Was passiert nach dem Matching?

Die `document_data` werden aktualisiert mit:
- `po_items` — Zugeordnete Bestellpositionen
- `po_match_status` — Abgleichergebnis (`"matched"`, `"partially_matched"` usw.)
- `po_multi_matched` — Ob mehrere Bestellungen zugeordnet wurden

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwert lesen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Bereinigte PO-Nummer schreiben
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — PO-Matching auslösen
