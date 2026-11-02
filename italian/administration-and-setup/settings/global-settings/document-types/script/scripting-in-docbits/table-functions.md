# Funzioni di Tabella

Funzioni per leggere, scrivere e manipolare tabelle e righe di tabella.

**Sorgente:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Legge il valore di una colonna da una riga di tabella.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `row` | `dict` | Un oggetto riga da `table["rows"]` |
| `column_name` | `str` | Nome della colonna (senza distinzione maiuscole/minuscole) |
| `default_value` | `any` | Valore restituito se la colonna e vuota/mancante |
| `is_clean` | `bool` | Se `True`: MAIUSCOLO con spazi rimossi |

**Esempio — Iterare le righe della tabella:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Il confronto del nome colonna e **senza distinzione maiuscole/minuscole**: `"DESCRIPTION"` corrisponde anche a `"description"` o `"Description"`.
{% endhint %}

---

## set\_column\_value()

Imposta il valore di una colonna in una riga di tabella.

```python
set_column_value(row, column_name, value)
```

**Restituisce:** `True` se il valore e cambiato, `False` se identico

**Effetti collaterali:**
- Imposta `extraction_method = "SCRIPT"`
- Crea automaticamente la colonna se non esiste

**Esempio — Calcolare i totali di riga:**

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

Imposta un valore data in una cella di tabella con formattazione e aritmetica delle date.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Necessario per `date_format_pattern` |
| `row` | `dict` | Riga della tabella |
| `column_name` | `str` | Nome della colonna |
| `value` | `str` | Data ISO `"2026-03-25"` |
| `add_days` | `int` | Giorni da aggiungere |
| `skip_weekend` | `bool` | Salta i fine settimana |
| `exclude_final_days` | `str/list` | Giorni da escludere |

**Esempio — Calcolare le date di consegna per ogni riga:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Imposta un valore importo in una cella di tabella con formattazione della localizzazione.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Esempio — Calcolare e formattare i totali di riga:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` viene automaticamente convertito in `str()` prima di essere impostato.
{% endhint %}

---

## add\_table\_column()

Aggiunge una nuova colonna a tutte le righe di una tabella.

```python
add_table_column(table, col_name, default_value=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `table` | `dict` | L'oggetto tabella (non `tables_dict`!) |
| `col_name` | `str` | Nome della nuova colonna |
| `default_value` | `any` | Valore iniziale per tutte le righe |

**Effetti collaterali:**
- `is_extra_column = True` (contrassegnata come non originale)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Esempio — Aggiungere colonna codice fiscale:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Ora impostare i valori per ogni riga
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Protezione dai duplicati:** Se la colonna esiste gia (controllo senza distinzione maiuscole/minuscole), **non** verra aggiunta di nuovo.
{% endhint %}

---

## remove\_rows\_from\_table()

Rimuove un numero specifico di righe da una tabella.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `table_name` | `str` | Nome della tabella |
| `count` | `int` | Numero di righe da rimuovere |
| `start` | `int` | Indice di partenza (basato su 0) |

**Solleva:** `ValueError` se `start` o `count` sono fuori intervallo

**Esempio — Rimuovere righe di intestazione o l'ultima riga:**

```python
# Rimuovere le prime 2 righe (es. righe di intestazione)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Rimuovere l'ultima riga
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Mantiene solo una riga specifica e rimuove tutte le altre.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `line_number` | `int` | Numero di riga (basato su 1!) |

{% hint style="warning" %}
`line_number=1` mantiene la prima riga. Non confondere con gli indici basati su 0.
{% endhint %}

**Esempio:**

```python
# Mantenere solo la 3a riga
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Elimina tutte le tabelle dal documento (con backup).

```python
delete_tables(document_data)
```

**Effetti collaterali:**
- Salva le tabelle sotto `last_deleted_table`
- Rimuove `po_items`, `po_multi_matched`, `po_match_status`

**Esempio:**

```python
# Eliminare le tabelle (es. per fatture di costo senza voci)
delete_tables(document_data)
```

---

## restore\_tables()

Ripristina le tabelle precedentemente eliminate con `delete_tables()`.

```python
restore_tables(document_data)
```

**Esempio:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Pattern Elimina + Ripristina:** Utile quando si desidera rimuovere temporaneamente le tabelle e ripristinarle in determinate condizioni.
{% endhint %}

---

## Pattern Comuni

### Calcolare la somma di una colonna

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

### Filtrare le righe vuote

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Rimuovere dal fondo verso l'inizio
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Calcolare una colonna da altre colonne

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
