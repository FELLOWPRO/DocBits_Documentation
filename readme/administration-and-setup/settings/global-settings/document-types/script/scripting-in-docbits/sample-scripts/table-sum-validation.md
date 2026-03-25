# Walidacja Sumy Tabeli

## Co robi ten skrypt?

Waliduje, czy suma wszystkich kwot pozycji w tabeli faktury odpowiada kwocie netto dokumentu. Jeśli rozbieżność przekracza 0,01, obliczona suma zastępuje wyodrębnioną kwotę netto — zapewniając spójność między pozycjami a polami nagłówka.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Oblicz sumę wszystkich kwot pozycji
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Porównaj z wyodrębnioną kwotą netto
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Suma pozycji różni się od nagłówka — zaktualizuj kwotę netto
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Wariant: Oznaczenie jako nieprawidłowe zamiast nadpisywania

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
                f"Suma pozycji ({round(total, 2)}) różni się od kwoty netto ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Kwoty się zgadzają")
    except ValueError:
        pass
```

## Wyjaśnienie krok po kroku

1. **Pobierz tabelę faktury** z `tables_dict`
2. **Zsumuj wszystkie wartości LINE_TOTAL** we wierszach tabeli
3. **Porównaj** obliczoną sumę z wyodrębnioną kwotą netto
4. **Zaktualizuj lub oznacz** — albo zastąp kwotę netto, albo oznacz ją jako nieprawidłową

## Użyte funkcje

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Odczyt wartości kolumn z wierszy
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt kwoty netto
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Ustawienie poprawionej kwoty
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Oznaczenie pola jako nieprawidłowe
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Oznaczenie pola jako prawidłowe
