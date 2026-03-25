# Tabellen-Funktionen

Funktionen zum Lesen, Schreiben und Manipulieren von Tabellen und Tabellenzeilen.

**Quelle:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Liest den Wert einer Spalte aus einer Tabellenzeile.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `row` | `dict` | Ein Zeilenobjekt aus `table["rows"]` |
| `column_name` | `str` | Spaltenname (Groß-/Kleinschreibung wird ignoriert) |
| `default_value` | `any` | Rückgabewert wenn Spalte leer/nicht vorhanden |
| `is_clean` | `bool` | Wenn `True`: GROSSBUCHSTABEN mit entfernten Leerzeichen |

**Beispiel — Tabellenzeilen iterieren:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Der Spaltenname-Vergleich ist **nicht Groß-/Kleinschreibung-sensitiv**: `"DESCRIPTION"` findet auch `"description"` oder `"Description"`.
{% endhint %}

---

## set\_column\_value()

Setzt den Wert einer Spalte in einer Tabellenzeile.

```python
set_column_value(row, column_name, value)
```

**Rückgabe:** `True` wenn Wert geändert, `False` wenn identisch

**Nebeneffekte:**
- Setzt `extraction_method = "SCRIPT"`
- Erstellt die Spalte automatisch, wenn sie nicht existiert

**Beispiel — Zeilenbeträge berechnen:**

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

Setzt einen Datumswert in einer Tabellenzelle mit Formatierung und Datumsarithmetik.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `document_data` | `dict` | Erforderlich für `date_format_pattern` |
| `row` | `dict` | Tabellenzeile |
| `column_name` | `str` | Spaltenname |
| `value` | `str` | ISO-Datum `"2026-03-25"` |
| `add_days` | `int` | Tage zum Addieren |
| `skip_weekend` | `bool` | Wochenenden überspringen |
| `exclude_final_days` | `str/list` | Auszuschließende Tage |

**Beispiel — Liefertermine pro Zeile berechnen:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Setzt einen Betragswert in einer Tabellenzelle mit Locale-Formatierung.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Beispiel — Zeilenbeträge berechnen und formatieren:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` wird vor dem Setzen automatisch in `str()` konvertiert.
{% endhint %}

---

## add\_table\_column()

Fügt eine neue Spalte zu allen Zeilen einer Tabelle hinzu.

```python
add_table_column(table, col_name, default_value=None)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `table` | `dict` | Das Tabellenobjekt (nicht `tables_dict`!) |
| `col_name` | `str` | Name der neuen Spalte |
| `default_value` | `any` | Anfangswert für alle Zeilen |

**Nebeneffekte:**
- `is_extra_column = True` (als nicht-original markiert)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Beispiel — Steuercode-Spalte hinzufügen:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Werte pro Zeile setzen
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Duplikatschutz:** Wenn die Spalte bereits existiert (Groß-/Kleinschreibung-unabhängige Prüfung), wird sie **nicht** erneut hinzugefügt.
{% endhint %}

---

## remove\_rows\_from\_table()

Entfernt eine bestimmte Anzahl von Zeilen aus einer Tabelle.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `table_name` | `str` | Name der Tabelle |
| `count` | `int` | Anzahl der zu entfernenden Zeilen |
| `start` | `int` | Startindex (0-basiert) |

**Wirft:** `ValueError` wenn `start` oder `count` außerhalb des Bereichs liegt

**Beispiel — Kopfzeilen oder letzte Zeile entfernen:**

```python
# Erste 2 Zeilen entfernen (z.B. Kopfzeilen)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Letzte Zeile entfernen
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Behält nur eine bestimmte Zeile und entfernt alle anderen.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parameter:**

| Name | Typ | Beschreibung |
| ---- | --- | ------------ |
| `line_number` | `int` | Zeilennummer (1-basiert!) |

{% hint style="warning" %}
`line_number=1` behält die erste Zeile. Nicht mit 0-basierten Indizes verwechseln.
{% endhint %}

**Beispiel:**

```python
# Nur die 3. Zeile behalten
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Löscht alle Tabellen aus dem Dokument (mit Backup).

```python
delete_tables(document_data)
```

**Nebeneffekte:**
- Speichert Tabellen unter `last_deleted_table`
- Entfernt `po_items`, `po_multi_matched`, `po_match_status`

**Beispiel:**

```python
# Tabellen löschen (z.B. für Kostenrechnungen ohne Positionen)
delete_tables(document_data)
```

---

## restore\_tables()

Stellt zuvor mit `delete_tables()` gelöschte Tabellen wieder her.

```python
restore_tables(document_data)
```

**Beispiel:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Löschen + Wiederherstellen-Muster:** Nützlich, wenn Tabellen temporär entfernt und unter bestimmten Bedingungen wiederhergestellt werden sollen.
{% endhint %}

---

## Häufige Muster

### Spaltensumme berechnen

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

### Leere Zeilen filtern

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Von hinten nach vorne entfernen
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Spalte aus anderen Spalten berechnen

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
