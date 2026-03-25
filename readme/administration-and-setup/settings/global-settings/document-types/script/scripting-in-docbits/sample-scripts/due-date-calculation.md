# Vervaldatumberekening

## Wat doet dit script?

Berekent de betalingsvervaldatum op basis van de factuurdatum door een configureerbaar aantal dagen op te tellen (bijv. 30). Weekenden worden automatisch overgeslagen zodat de vervaldatum altijd op een werkdag valt.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Factuurdatum lezen
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Vervaldatum berekenen: 30 dagen na factuurdatum, weekenden overslaan
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Ook boekingsdatum instellen = factuurdatum
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variaties

### 14 dagen, exclusief maandagen

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 dagen, zonder weekendoverslag

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Leverdatum instellen op vandaag

```python
set_date_value(document_data, "delivery_date", None)  # None = vandaag
```

## Stapsgewijze Uitleg

1. **Factuurdatum lezen** uit het document
2. **Vervaldatum berekenen** met `set_date_value()` met `add_days=30` en `skip_weekend=True`
3. **Datumopmaak** is automatisch — gebruikt het `date_format_pattern` van het document (bijv. `%d.%m.%Y`)
4. **Weekendoverslag** zorgt ervoor dat de vervaldatum op ma-vr valt

## Dagcodes voor `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Factuurdatum lezen
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Vervaldatum berekenen en instellen
