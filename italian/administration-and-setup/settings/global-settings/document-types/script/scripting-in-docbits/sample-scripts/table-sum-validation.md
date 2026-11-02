# Validazione Somma Tabella

## Cosa fa questo script?

Valida che la somma di tutti i totali di riga nella tabella fattura corrisponda all'importo netto del documento. Se c'e una discrepanza maggiore di 0,01, la somma calcolata sostituisce l'importo netto estratto — garantendo la coerenza tra le voci e i campi dell'intestazione.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calcolare la somma di tutti i totali di riga
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Confrontare con l'importo netto estratto
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # La somma delle righe differisce dall'intestazione — aggiornare l'importo netto
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variazione: Contrassegnare come non valido invece di sovrascrivere

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
                f"La somma dei totali riga ({round(total, 2)}) differisce dall'importo netto ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Gli importi corrispondono")
    except ValueError:
        pass
```

## Spiegazione Passo dopo Passo

1. **Ottenere la tabella fattura** da `tables_dict`
2. **Sommare tutti i valori LINE_TOTAL** attraverso le righe della tabella
3. **Confrontare** la somma calcolata con l'importo netto estratto
4. **Aggiornare o segnalare** — sostituire l'importo netto o contrassegnarlo come non valido

## Funzioni Utilizzate

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Leggere i valori delle colonne dalle righe
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere l'importo netto
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Impostare l'importo corretto
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Contrassegnare il campo come non valido
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Contrassegnare il campo come valido
