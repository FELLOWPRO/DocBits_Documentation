# Fälligkeitsberechnung

## Was macht dieses Skript?

Berechnet das Zahlungsfälligkeitsdatum basierend auf dem Rechnungsdatum, indem eine konfigurierbare Anzahl von Tagen addiert wird (z.B. 30). Wochenenden werden automatisch übersprungen, sodass das Fälligkeitsdatum immer auf einen Werktag fällt.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Rechnungsdatum lesen
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Fälligkeitsdatum berechnen: 30 Tage nach Rechnungsdatum, Wochenenden überspringen
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Auch Buchungsdatum = Rechnungsdatum setzen
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variationen

### 14 Tage, Montage ausschließen

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 Tage, ohne Wochenend-Überspringung

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Lieferdatum auf heute setzen

```python
set_date_value(document_data, "delivery_date", None)  # None = heute
```

## Schritt-für-Schritt-Erklärung

1. **Rechnungsdatum lesen** aus dem Dokument
2. **Fälligkeitsdatum berechnen** mit `set_date_value()` mit `add_days=30` und `skip_weekend=True`
3. **Datumsformatierung** erfolgt automatisch — verwendet das `date_format_pattern` des Dokuments (z.B. `%d.%m.%Y`)
4. **Wochenend-Überspringung** stellt sicher, dass das Fälligkeitsdatum auf Mo-Fr fällt

## Tagescodes für `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Rechnungsdatum lesen
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Fälligkeitsdatum berechnen und setzen
