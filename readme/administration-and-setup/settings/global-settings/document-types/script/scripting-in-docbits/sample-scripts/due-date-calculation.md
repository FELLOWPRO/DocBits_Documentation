# Obliczanie Terminu Płatności

## Co robi ten skrypt?

Oblicza termin płatności na podstawie daty faktury, dodając konfigurowalną liczbę dni (np. 30). Weekendy są automatycznie pomijane, więc termin płatności zawsze wypada w dniu roboczym.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj datę faktury
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Oblicz termin płatności: 30 dni po dacie faktury, pomijanie weekendów
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Ustaw również datę księgowania = data faktury
    set_date_value(document_data, "accounting_date", inv_date)
```

## Warianty

### 14 dni, z wykluczeniem poniedziałków

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 dni, bez pomijania weekendów

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Ustaw datę dostawy na dzisiaj

```python
set_date_value(document_data, "delivery_date", None)  # None = dzisiaj
```

## Wyjaśnienie krok po kroku

1. **Odczytaj datę faktury** z dokumentu
2. **Oblicz termin płatności** za pomocą `set_date_value()` z `add_days=30` i `skip_weekend=True`
3. **Formatowanie daty** jest automatyczne — używa `date_format_pattern` dokumentu (np. `%d.%m.%Y`)
4. **Pomijanie weekendów** zapewnia, że termin płatności wypada od poniedziałku do piątku

## Kody dni dla `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt daty faktury
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Obliczanie i ustawianie terminu płatności
