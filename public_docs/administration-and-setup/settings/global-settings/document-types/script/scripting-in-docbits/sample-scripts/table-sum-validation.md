# Tabelsom Validatie

## Wat doet dit script?

Valideert dat de som van alle regeltotalen in de factuurtabel overeenkomt met het nettobedrag van het document. Als er een verschil groter dan 0,01 is, vervangt de berekende som het geextraheerde nettobedrag — dit garandeert consistentie tussen regelitems en koptekstvelden.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Som van alle regeltotalen berekenen
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Vergelijken met geëxtraheerd nettobedrag
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Regelsom verschilt van koptekst — nettobedrag bijwerken
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variatie: Als ongeldig markeren in plaats van overschrijven

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
                f"Regeltotaalsom ({round(total, 2)}) verschilt van nettobedrag ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Bedragen komen overeen")
    except ValueError:
        pass
```

## Stapsgewijze Uitleg

1. **Factuurtabel ophalen** uit `tables_dict`
2. **Alle LINE_TOTAL-waarden optellen** over de tabelrijen
3. **Vergelijken** van de berekende som met het geextraheerde nettobedrag
4. **Bijwerken of markeren** — het nettobedrag vervangen of als ongeldig markeren

## Gebruikte Functies

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Kolomwaarden uit rijen lezen
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Nettobedrag lezen
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Gecorrigeerd bedrag instellen
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Veld als ongeldig markeren
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Veld als geldig markeren
