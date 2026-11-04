# Usuń wiersze z pustą ilością i kwotą

#### Część 1: Usuwanie wierszy z pustą ilością i kwotą

Ta sekcja skryptu przetwarza tabelę faktur w celu usunięcia wierszy, w których zarówno ilość, jak i całkowita kwota wynoszą zero lub nie zostały podane.

* **Sprawdź INVOICE\_TABLE:** Zaczyna od sprawdzenia, czy klucz `INVOICE_TABLE` istnieje w słowniku `tables_dict`.
* **Iteruj po wierszach:** Dla każdego wiersza w tabeli skrypt inicjuje flagi i zmienne w celu określenia, czy kolumny `TOTAL_AMOUNT` i `QUANTITY` istnieją oraz przechwycenia ich wartości.
* **Sprawdź nazwy kolumn:** Przechodząc przez każdą kolumnę w wierszu, szuka kolumn o nazwach `TOTAL_AMOUNT` i `QUANTITY`.
* Jeśli znajdzie `TOTAL_AMOUNT`, przechwytuje wartość. Jeśli ta wartość jest niezerowa, konwertuje ją na liczbę zmiennoprzecinkową.
* Podobnie dla `QUANTITY`, przechwytując i konwertując wartość, jeśli jest niezerowa.
* **Oznacz wiersz do usunięcia:** Po sprawdzeniu obu kolumn w wierszu, jeśli zarówno całkowita kwota, jak i ilość są faktycznie równe zero (zarówno przez bycie zerem, jak i nieistnienie), wiersz jest oznaczany do usunięcia poprzez ustawienie `row['is_deleted']` na `True`.

#### Część 2: Sprawdź łączną kwotę wierszy w porównaniu z łączną kwotą faktury

Ta sekcja oblicza łączną kwotę ze wszystkich wierszy faktury i porównuje ją z podaną łączną kwotą faktury w celu zweryfikowania ich zgodności.

* **Zainicjuj łączną kwotę wierszy:** Zaczyna od ustawienia zmiennej `lines_total` na 0.0 w celu akumulowania łącznej kwoty ze wszystkich wierszy.
* **Sumuj kwoty wierszy:** Iteruje po każdym wierszu w `INVOICE_TABLE`, wydobywając `TOTAL_AMOUNT` z każdego i dodając go do `lines_total`.
* **Pobierz i skonwertuj łączną kwotę faktury:** Pobiera łączną kwotę faktury, korzystając z funkcji pomocniczej `get_field_value` i konwertuje ją na liczbę zmiennoprzecinkową.
* **Porównaj kwoty:** Na koniec sprawdza, czy różnica bezwzględna między obliczoną łączną kwotą wierszy (`lines_total`) a podaną łączną kwotą faktury (`total_amount`) przekracza próg 0.05. Jeśli tak, oznacza pole łącznej kwoty faktury jako nieprawidłowe, korzystając z innej funkcji pomocniczej `set_field_as_invalid`, podając niezgodność.
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

1. Usuwanie wierszy danych, które nie przyczyniają się do całkowitej kwoty faktury z powodu braku ilości lub kwoty.
2. Sprawdzanie spójności między sumą poszczególnych kwot w wierszach a całkowitą kwotą faktury, zaznaczając różnice do podjęcia dalszych działań.

To automatyzacja pomaga utrzymać dokładne zapisy finansowe i może być kluczowa dla systemów takich jak ERP, które wymagają precyzyjnych danych do księgowości i raportowania finansowego.
