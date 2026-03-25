# Funkcije tabele

Funkcije za citanje, pisanje i manipulaciju tabelama i redovima tabele.

**Izvor:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Cita vrednost kolone iz reda tabele.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `row` | `dict` | Objekat reda iz `table["rows"]` |
| `column_name` | `str` | Naziv kolone (bez razlikovanja velikih i malih slova) |
| `default_value` | `any` | Povratna vrednost ako kolona ne postoji/je prazna |
| `is_clean` | `bool` | Ako je `True`: VELIKA SLOVA sa uklonjenim razmacima |

**Primer -- Iteracija kroz redove tabele:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Poredjenje naziva kolona je **bez razlikovanja velikih i malih slova**: `"DESCRIPTION"` takodje odgovara `"description"` ili `"Description"`.
{% endhint %}

---

## set\_column\_value()

Postavlja vrednost kolone u redu tabele.

```python
set_column_value(row, column_name, value)
```

**Vraca:** `True` ako je vrednost promenjena, `False` ako je identicna

**Sporedni efekti:**
- Postavlja `extraction_method = "SCRIPT"`
- Automatski kreira kolonu ako ne postoji

**Primer -- Izracunavanje ukupnih iznosa po stavkama:**

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

Postavlja vrednost datuma u celiji tabele sa formatiranjem i aritmetikom datuma.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Potreban za `date_format_pattern` |
| `row` | `dict` | Red tabele |
| `column_name` | `str` | Naziv kolone |
| `value` | `str` | ISO datum `"2026-03-25"` |
| `add_days` | `int` | Dani za dodavanje |
| `skip_weekend` | `bool` | Preskoci vikende |
| `exclude_final_days` | `str/list` | Dani za iskljucivanje |

**Primer -- Izracunavanje datuma isporuke po redu:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Postavlja vrednost iznosa u celiji tabele sa formatiranjem prema lokalitetu.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Primer -- Izracunavanje i formatiranje ukupnih iznosa po stavkama:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` se automatski konvertuje u `str()` pre postavljanja.
{% endhint %}

---

## add\_table\_column()

Dodaje novu kolonu u sve redove tabele.

```python
add_table_column(table, col_name, default_value=None)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `table` | `dict` | Objekat tabele (ne `tables_dict`!) |
| `col_name` | `str` | Naziv nove kolone |
| `default_value` | `any` | Pocetna vrednost za sve redove |

**Sporedni efekti:**
- `is_extra_column = True` (oznacena kao neoriginalna)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Primer -- Dodavanje kolone poreskog koda:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Sada postavite vrednosti po redu
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Zastita od duplikata:** Ako kolona vec postoji (provera bez razlikovanja velikih i malih slova), nece biti ponovo dodata.
{% endhint %}

---

## remove\_rows\_from\_table()

Uklanja odredjeni broj redova iz tabele.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `table_name` | `str` | Naziv tabele |
| `count` | `int` | Broj redova za uklanjanje |
| `start` | `int` | Pocetni indeks (pocinje od 0) |

**Baca:** `ValueError` ako su `start` ili `count` van opsega

**Primer -- Uklanjanje redova zaglavlja ili poslednjeg reda:**

```python
# Uklanjanje prva 2 reda (npr. redovi zaglavlja)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Uklanjanje poslednjeg reda
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Zadrzava samo jedan odredjeni red i uklanja sve ostale.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parametri:**

| Naziv | Tip | Opis |
| ---- | ---- | ----------- |
| `line_number` | `int` | Broj reda (pocinje od 1!) |

{% hint style="warning" %}
`line_number=1` zadrzava prvi red. Nemojte mesati sa indeksima koji pocinu od 0.
{% endhint %}

**Primer:**

```python
# Zadrzi samo 3. red
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Brise sve tabele iz dokumenta (sa rezervnom kopijom).

```python
delete_tables(document_data)
```

**Sporedni efekti:**
- Cuva tabele pod `last_deleted_table`
- Uklanja `po_items`, `po_multi_matched`, `po_match_status`

**Primer:**

```python
# Brisanje tabela (npr. za troskovne fakture bez stavki)
delete_tables(document_data)
```

---

## restore\_tables()

Vraca tabele prethodno obrisane sa `delete_tables()`.

```python
restore_tables(document_data)
```

**Primer:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Obrazac brisanje + vracanje:** Korisno kada zelite privremeno da uklonite tabele i vratite ih pod odredjenim uslovima.
{% endhint %}

---

## Uobicajeni obrasci

### Izracunavanje zbira kolone

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

### Filtriranje praznih redova

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Uklanjanje od kraja ka pocetku
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Izracunavanje kolone iz drugih kolona

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
