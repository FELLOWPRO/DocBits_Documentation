# Funciones de Tabla

Funciones para leer, escribir y manipular tablas y filas de tablas.

**Fuente:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Lee el valor de una columna de una fila de tabla.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `row` | `dict` | Un objeto de fila de `table["rows"]` |
| `column_name` | `str` | Nombre de la columna (sin distincion de mayusculas/minusculas) |
| `default_value` | `any` | Valor de retorno si la columna esta vacia/no existe |
| `is_clean` | `bool` | Si es `True`: MAYUSCULAS con espacios eliminados |

**Ejemplo — Iterar filas de tabla:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
La comparacion del nombre de columna **no distingue entre mayusculas y minusculas**: `"DESCRIPTION"` tambien coincide con `"description"` o `"Description"`.
{% endhint %}

---

## set\_column\_value()

Establece el valor de una columna en una fila de tabla.

```python
set_column_value(row, column_name, value)
```

**Retorna:** `True` si el valor cambio, `False` si es identico

**Efectos secundarios:**
- Establece `extraction_method = "SCRIPT"`
- Crea automaticamente la columna si no existe

**Ejemplo — Calcular totales de linea:**

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

Establece un valor de fecha en una celda de tabla con formato y aritmetica de fechas.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Requerido para `date_format_pattern` |
| `row` | `dict` | Fila de la tabla |
| `column_name` | `str` | Nombre de la columna |
| `value` | `str` | Fecha ISO `"2026-03-25"` |
| `add_days` | `int` | Dias a agregar |
| `skip_weekend` | `bool` | Omitir fines de semana |
| `exclude_final_days` | `str/list` | Dias a excluir |

**Ejemplo — Calcular fechas de entrega por fila:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Establece un valor de monto en una celda de tabla con formato regional.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Ejemplo — Calcular y formatear totales de linea:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` se convierte automaticamente a `str()` antes de ser establecido.
{% endhint %}

---

## add\_table\_column()

Agrega una nueva columna a todas las filas de una tabla.

```python
add_table_column(table, col_name, default_value=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `table` | `dict` | El objeto de tabla (no `tables_dict`!) |
| `col_name` | `str` | Nombre de la nueva columna |
| `default_value` | `any` | Valor inicial para todas las filas |

**Efectos secundarios:**
- `is_extra_column = True` (marcada como no original)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Ejemplo — Agregar columna de codigo fiscal:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Ahora establecer valores por fila
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Proteccion contra duplicados:** Si la columna ya existe (verificacion sin distincion de mayusculas/minusculas), **no** se agregara de nuevo.
{% endhint %}

---

## remove\_rows\_from\_table()

Elimina un numero especifico de filas de una tabla.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `table_name` | `str` | Nombre de la tabla |
| `count` | `int` | Numero de filas a eliminar |
| `start` | `int` | Indice de inicio (basado en 0) |

**Lanza:** `ValueError` si `start` o `count` estan fuera de rango

**Ejemplo — Eliminar filas de encabezado o ultima fila:**

```python
# Eliminar las primeras 2 filas (ej., filas de encabezado)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Eliminar ultima fila
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Mantiene solo una fila especifica y elimina todas las demas.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `line_number` | `int` | Numero de fila (basado en 1!) |

{% hint style="warning" %}
`line_number=1` mantiene la primera fila. No confundir con indices basados en 0.
{% endhint %}

**Ejemplo:**

```python
# Mantener solo la 3ra fila
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Elimina todas las tablas del documento (con respaldo).

```python
delete_tables(document_data)
```

**Efectos secundarios:**
- Guarda las tablas bajo `last_deleted_table`
- Elimina `po_items`, `po_multi_matched`, `po_match_status`

**Ejemplo:**

```python
# Eliminar tablas (ej., para facturas de costos sin partidas)
delete_tables(document_data)
```

---

## restore\_tables()

Restaura las tablas previamente eliminadas con `delete_tables()`.

```python
restore_tables(document_data)
```

**Ejemplo:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Patron Eliminar + Restaurar:** Util cuando desea eliminar temporalmente tablas y restaurarlas bajo ciertas condiciones.
{% endhint %}

---

## Patrones Comunes

### Calcular suma de columna

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

### Filtrar filas vacias

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Eliminar de atras hacia adelante
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Calcular columna a partir de otras columnas

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
