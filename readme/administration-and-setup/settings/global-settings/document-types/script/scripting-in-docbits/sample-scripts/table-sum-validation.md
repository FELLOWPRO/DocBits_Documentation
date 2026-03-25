# Validacija zbira tabele

## Sta ova skripta radi?

Validira da zbir svih ukupnih iznosa stavki u tabeli fakture odgovara neto iznosu dokumenta. Ako postoji neslaganje vece od 0.01, izracunati zbir zamenjuje ekstraktovani neto iznos -- cime se osigurava konzistentnost izmedju stavki i polja zaglavlja.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Izracunavanje zbira svih ukupnih iznosa stavki
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Poredjenje sa ekstraktovanim neto iznosom
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Zbir stavki se razlikuje od zaglavlja -- azuriraj neto iznos
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Varijacija: Oznaci kao nevazece umesto prepisivanja

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
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## Objasnjenje korak po korak

1. **Preuzimanje tabele fakture** iz `tables_dict`
2. **Sabiranje svih LINE_TOTAL vrednosti** kroz redove tabele
3. **Poredjenje** izracunatog zbira sa ekstraktovanim neto iznosom
4. **Azuriranje ili oznacavanje** -- ili zamena neto iznosa ili oznacavanje kao nevazeceg

## Koriscene funkcije

- [get\_column\_value()](../table-functions.md#get\_column\_value) -- Citanje vrednosti kolona iz redova
- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje neto iznosa
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) -- Postavljanje ispravljenog iznosa
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) -- Oznacavanje polja kao nevazeceg
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) -- Oznacavanje polja kao vazeceg
