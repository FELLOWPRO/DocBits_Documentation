# Obracun datuma dospeca

## Sta ova skripta radi?

Izracunava datum dospeca placanja na osnovu datuma fakture dodavanjem podesivog broja dana (npr. 30). Vikendi se automatski preskacu tako da datum dospeca uvek pada na radni dan.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje datuma fakture
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Izracunavanje datuma dospeca: 30 dana posle datuma fakture, preskoci vikende
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Takodje postavi datum knjizenja = datum fakture
    set_date_value(document_data, "accounting_date", inv_date)
```

## Varijacije

### 14 dana, iskljucujuci ponedeljke

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 dana, bez preskakanja vikenda

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Postavljanje datuma isporuke na danas

```python
set_date_value(document_data, "delivery_date", None)  # None = danas
```

## Objasnjenje korak po korak

1. **Citanje datuma fakture** iz dokumenta
2. **Izracunavanje datuma dospeca** koriscenjem `set_date_value()` sa `add_days=30` i `skip_weekend=True`
3. **Formatiranje datuma** je automatsko -- koristi `date_format_pattern` dokumenta (npr. `%d.%m.%Y`)
4. **Preskakanje vikenda** osigurava da datum dospeca pada na pon-pet

## Kodovi dana za `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje datuma fakture
- [set\_date\_value()](../field-functions.md#set\_date\_value) -- Izracunavanje i postavljanje datuma dospeca
