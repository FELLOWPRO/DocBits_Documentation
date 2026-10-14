# Usuwanie Linii z Pustą Ilością i Kwotą

#### Część 1: Usuwanie Linii z Pustą Ilością i Kwotą

Ta sekcja skryptu przetwarza tabelę faktury w celu usunięcia wszystkich linii, gdzie zarówno ilość, jak i całkowita kwota są zerowe lub nie zostały podane.

* **Sprawdzenie INVOICE\_TABLE:** Rozpoczyna się od sprawdzenia, czy klucz `INVOICE_TABLE` istnieje w słowniku `tables_dict`.
* **Iteracja przez Linie:** Dla każdej linii w tabeli, skrypt inicjalizuje flagi i zmienne w celu określenia, czy kolumny `TOTAL_AMOUNT` i `QUANTITY` istnieją oraz do przechwycenia ich wartości.
* **Sprawdzenie Nazw Kolumn:** Podczas iteracji przez każdą kolumnę w linii, szuka kolumn o nazwach `TOTAL_AMOUNT` i `QUANTITY`.
  * Jeśli `TOTAL_AMOUNT` zostanie znaleziony, przechwytuje wartość. Jeśli ta wartość nie jest zerowa, konwertuje ją na liczbę zmiennoprzecinkową.
  * Podobnie dla `QUANTITY`, przechwytując i konwertując wartość, jeśli nie jest zerowa.
* **Oznaczenie Linii do Usunięcia:** Po sprawdzeniu obu kolumn w linii, jeśli zarówno całkowita kwota, jak i ilość są efektywnie zerowe (albo są zerami, albo nie istnieją), linia jest oznaczana do usunięcia przez ustawienie `row['is_deleted']` na `True`.

#### Część 2: Walidacja Sumy Linii względem Sumy Faktury

Ta sekcja oblicza całkowitą kwotę wszystkich linii na fakturze i porównuje ją z raportowaną sumą faktury w celu walidacji spójności.

* **Inicjalizacja Sumy Linii:** Rozpoczyna od ustawienia zmiennej `lines_total` na 0.0, aby akumulować całkowitą kwotę wszystkich linii.
* **Sumowanie Wartości Linii:** Iteruje przez każdą linię w `INVOICE_TABLE`, wyodrębniając `TOTAL_AMOUNT` z każdej i dodając do `lines_total`.
* **Pobranie i Konwersja Sumy Faktury:** Pobiera całkowitą wartość faktury używając funkcji pomocniczej `get_field_value` i konwertuje na liczbę zmiennoprzecinkową.
* **Porównanie Sum:** Na koniec sprawdza, czy bezwzględna różnica między obliczoną sumą linii (`lines_total`) a raportowaną sumą faktury (`total_amount`) przekracza próg 0,05. Jeśli tak, oznacza pole sumy faktury jako nieprawidłowe używając innej funkcji pomocniczej `set_field_as_invalid`, podając rozbieżność.

```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################
```

#### Podsumowanie

Skrypt skutecznie zapewnia integralność danych poprzez:

1. Usuwanie linii danych, które nie przyczyniają się do sumy finansowej faktury z powodu brakujących ilości lub kwot.
2. Walidację spójności między sumą wartości poszczególnych linii a całkowitą sumą faktury, podkreślając rozbieżności do dalszych działań.

Ta automatyzacja pomaga utrzymać dokładne zapisy finansowe i może być kluczowa dla systemów takich jak ERP, które wymagają precyzyjnych danych do księgowości i sprawozdawczości finansowej.
