# Tabellensummen-Validierung

## Was macht dieses Skript?

Validiert, dass die Summe aller Positionsbeträge in der Rechnungstabelle mit dem Nettobetrag des Dokuments übereinstimmt. Wenn eine Abweichung größer als 0,01 vorliegt, ersetzt die berechnete Summe den extrahierten Nettobetrag — um die Konsistenz zwischen Positionen und Kopffeldern sicherzustellen.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Summe aller Positionsbeträge berechnen
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Mit extrahiertem Nettobetrag vergleichen
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Positionssumme weicht vom Kopffeld ab — Nettobetrag aktualisieren
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variation: Als ungültig markieren statt überschreiben

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Positionssumme ({round(total, 2)}) weicht vom Nettobetrag ({net_amount}) ab")
        else:
            set_field_as_valid(document_data, "net_amount", "Beträge stimmen überein")
    except ValueError:
        pass
```

## Schritt-für-Schritt-Erklärung

1. **Rechnungstabelle abrufen** aus `tables_dict`
2. **Alle LINE_TOTAL-Werte summieren** über die Tabellenzeilen
3. **Vergleichen** der berechneten Summe mit dem extrahierten Nettobetrag
4. **Aktualisieren oder kennzeichnen** — entweder den Nettobetrag ersetzen oder als ungültig markieren

## Verwendete Funktionen

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Spaltenwerte aus Zeilen lesen
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Nettobetrag lesen
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Korrigierten Betrag setzen
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Feld als ungültig markieren
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Feld als gültig markieren
