# Funkcje Tabel

Funkcje do odczytu, zapisu i manipulacji tabelami oraz wierszami tabel.

**Zrodlo:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Odczytuje wartosc kolumny z wiersza tabeli.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `row` | `dict` | Obiekt wiersza z `table["rows"]` |
| `column_name` | `str` | Nazwa kolumny (bez rozrozniania wielkosci liter) |
| `default_value` | `any` | Wartosc zwracana jesli kolumna jest pusta/nie istnieje |
| `is_clean` | `bool` | Jesli `True`: WIELKIE LITERY z usunietymi spacjami |

**Przyklad — Iteracja po wierszach tabeli:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Porownanie nazw kolumn jest **bez rozrozniania wielkosci liter**: `"DESCRIPTION"` dopasowuje takze `"description"` lub `"Description"`.
{% endhint %}

---

## set\_column\_value()

Ustawia wartosc kolumny w wierszu tabeli.

```python
set_column_value(row, column_name, value)
```

**Zwraca:** `True` jesli wartosc sie zmienila, `False` jesli identyczna

**Efekty uboczne:**
- Ustawia `extraction_method = "SCRIPT"`
- Automatycznie tworzy kolumne, jesli nie istnieje

**Przyklad — Obliczanie sum pozycji:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
        try:
            total = float(qty) * float(price)
            set_column_value(row, "LINE_TOTAL", str(total))
        except ValueError:
            pass
```

---

## set\_column\_date\_value()

Ustawia wartosc daty w komorce tabeli z formatowaniem i arytmetyka dat.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Wymagane dla `date_format_pattern` |
| `row` | `dict` | Wiersz tabeli |
| `column_name` | `str` | Nazwa kolumny |
| `value` | `str` | Data ISO `"2026-03-25"` |
| `add_days` | `int` | Dni do dodania |
| `skip_weekend` | `bool` | Pomijanie weekendow |
| `exclude_final_days` | `str/list` | Dni do wykluczenia |

**Przyklad — Obliczanie dat dostawy na wiersz:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Ustawia wartosc kwoty w komorce tabeli z formatowaniem regionalnym.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Przyklad — Obliczanie i formatowanie sum pozycji:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` jest automatycznie konwertowane na `str()` przed ustawieniem.
{% endhint %}

---

## add\_table\_column()

Dodaje nowa kolumne do wszystkich wierszy tabeli.

```python
add_table_column(table, col_name, default_value=None)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `table` | `dict` | Obiekt tabeli (nie `tables_dict`!) |
| `col_name` | `str` | Nazwa nowej kolumny |
| `default_value` | `any` | Wartosc poczatkowa dla wszystkich wierszy |

**Efekty uboczne:**
- `is_extra_column = True` (oznaczona jako nieoryginalna)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Przyklad — Dodanie kolumny kodu podatkowego:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Teraz ustaw wartosci per wiersz
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Ochrona przed duplikatami:** Jesli kolumna juz istnieje (sprawdzanie bez rozrozniania wielkosci liter), **nie** zostanie dodana ponownie.
{% endhint %}

---

## remove\_rows\_from\_table()

Usuwa okreslona liczbe wierszy z tabeli.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `table_name` | `str` | Nazwa tabeli |
| `count` | `int` | Liczba wierszy do usuniecia |
| `start` | `int` | Indeks poczatkowy (od 0) |

**Wyrzuca:** `ValueError` jesli `start` lub `count` jest poza zakresem

**Przyklad — Usuwanie wierszy naglowka lub ostatniego wiersza:**

```python
# Usun pierwsze 2 wiersze (np. wiersze naglowka)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Usun ostatni wiersz
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Zachowuje tylko jeden konkretny wiersz i usuwa wszystkie pozostale.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parametry:**

| Nazwa | Typ | Opis |
| ---- | ---- | ----------- |
| `line_number` | `int` | Numer wiersza (od 1!) |

{% hint style="warning" %}
`line_number=1` zachowuje pierwszy wiersz. Nie nalezy mylic z indeksami od 0.
{% endhint %}

**Przyklad:**

```python
# Zachowaj tylko 3. wiersz
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Usuwa wszystkie tabele z dokumentu (z kopia zapasowa).

```python
delete_tables(document_data)
```

**Efekty uboczne:**
- Zapisuje tabele pod `last_deleted_table`
- Usuwa `po_items`, `po_multi_matched`, `po_match_status`

**Przyklad:**

```python
# Usun tabele (np. dla faktur kosztowych bez pozycji)
delete_tables(document_data)
```

---

## restore\_tables()

Przywraca tabele wczesniej usuniete za pomoca `delete_tables()`.

```python
restore_tables(document_data)
```

**Przyklad:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Wzorzec Usun + Przywroc:** Przydatny, gdy chcesz tymczasowo usunac tabele i przywrocic je pod pewnymi warunkami.
{% endhint %}

---

## Typowe wzorce

### Obliczanie sumy kolumny

```python
table = tables_dict.get("INVOICE_TABLE")
total = 0
if table:
    for row in table["rows"]:
        val = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(val)
        except ValueError:
            pass
    set_field_value(document_data, "calculated_total", str(round(total, 2)))
```

### Filtrowanie pustych wierszy

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Usuwanie od tylu do przodu
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Obliczanie kolumny z innych kolumn

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_AMOUNT", "0")
    for row in table["rows"]:
        net = float(get_column_value(row, "NET_AMOUNT", "0"))
        tax_rate = float(get_column_value(row, "TAX_RATE", "0"))
        tax = net * tax_rate / 100
        set_column_amount_value(document_data, row, "TAX_AMOUNT", tax)
```
