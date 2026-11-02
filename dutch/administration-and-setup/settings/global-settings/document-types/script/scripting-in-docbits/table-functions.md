# Tabelfuncties

Functies voor het lezen, schrijven en manipuleren van tabellen en tabelrijen.

**Source:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Leest de waarde van een kolom uit een tabelrij.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `row` | `dict` | Een rij-object uit `table["rows"]` |
| `column_name` | `str` | Kolomnaam (hoofdletterongevoelig) |
| `default_value` | `any` | Retourwaarde als kolom leeg/ontbrekend is |
| `is_clean` | `bool` | Indien `True`: HOOFDLETTERS met spaties verwijderd |

**Voorbeeld — Tabelrijen doorlopen:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Kolomnaamvergelijking is **hoofdletterongevoelig**: `"DESCRIPTION"` komt ook overeen met `"description"` of `"Description"`.
{% endhint %}

---

## set\_column\_value()

Stelt de waarde van een kolom in een tabelrij in.

```python
set_column_value(row, column_name, value)
```

**Retourneert:** `True` als de waarde is gewijzigd, `False` als deze identiek is

**Neveneffecten:**
- Stelt `extraction_method = "SCRIPT"` in
- Maakt de kolom automatisch aan als deze niet bestaat

**Voorbeeld — Regeltotalen berekenen:**

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

Stelt een datumwaarde in een tabelcel in met opmaak en datumberekeningen.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Vereist voor `date_format_pattern` |
| `row` | `dict` | Tabelrij |
| `column_name` | `str` | Kolomnaam |
| `value` | `str` | ISO-datum `"2026-03-25"` |
| `add_days` | `int` | Dagen om toe te voegen |
| `skip_weekend` | `bool` | Weekenden overslaan |
| `exclude_final_days` | `str/list` | Dagen om uit te sluiten |

**Voorbeeld — Leverdata per rij berekenen:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Stelt een bedragwaarde in een tabelcel in met lokale opmaak.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Voorbeeld — Regeltotalen berekenen en opmaken:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` wordt automatisch geconverteerd naar `str()` voordat het wordt ingesteld.
{% endhint %}

---

## add\_table\_column()

Voegt een nieuwe kolom toe aan alle rijen van een tabel.

```python
add_table_column(table, col_name, default_value=None)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `table` | `dict` | Het tabelobject (niet `tables_dict`!) |
| `col_name` | `str` | Naam van de nieuwe kolom |
| `default_value` | `any` | Beginwaarde voor alle rijen |

**Neveneffecten:**
- `is_extra_column = True` (gemarkeerd als niet-origineel)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Voorbeeld — Belastingcodekolom toevoegen:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Nu waarden per rij instellen
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Duplicaatbeveiliging:** Als de kolom al bestaat (hoofdletterongevoelige controle), wordt deze **niet** opnieuw toegevoegd.
{% endhint %}

---

## remove\_rows\_from\_table()

Verwijdert een specifiek aantal rijen uit een tabel.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `table_name` | `str` | Naam van de tabel |
| `count` | `int` | Aantal te verwijderen rijen |
| `start` | `int` | Startindex (0-gebaseerd) |

**Gooit:** `ValueError` als `start` of `count` buiten bereik is

**Voorbeeld — Koptekstrijen of laatste rij verwijderen:**

```python
# Eerste 2 rijen verwijderen (bijv. koptekstrijen)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Laatste rij verwijderen
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Behoudt slechts een specifieke rij en verwijdert alle andere.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parameters:**

| Naam | Type | Beschrijving |
| ---- | ---- | ----------- |
| `line_number` | `int` | Rijnummer (1-gebaseerd!) |

{% hint style="warning" %}
`line_number=1` behoudt de eerste rij. Verwar dit niet met 0-gebaseerde indices.
{% endhint %}

**Voorbeeld:**

```python
# Alleen de 3e rij behouden
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Verwijdert alle tabellen uit het document (met back-up).

```python
delete_tables(document_data)
```

**Neveneffecten:**
- Slaat tabellen op onder `last_deleted_table`
- Verwijdert `po_items`, `po_multi_matched`, `po_match_status`

**Voorbeeld:**

```python
# Tabellen verwijderen (bijv. voor kostenfacturen zonder regelitems)
delete_tables(document_data)
```

---

## restore\_tables()

Herstelt tabellen die eerder zijn verwijderd met `delete_tables()`.

```python
restore_tables(document_data)
```

**Voorbeeld:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Verwijderen + Herstellen patroon:** Nuttig wanneer u tabellen tijdelijk wilt verwijderen en ze onder bepaalde voorwaarden wilt herstellen.
{% endhint %}

---

## Veelvoorkomende Patronen

### Kolomsom berekenen

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

### Lege rijen filteren

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Van achteren naar voren verwijderen
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Kolom berekenen uit andere kolommen

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
