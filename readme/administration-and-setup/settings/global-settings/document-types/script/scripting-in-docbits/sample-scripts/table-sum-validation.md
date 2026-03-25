# Validacion de Suma de Tabla

## Que hace este script?

Valida que la suma de todos los totales de linea en la tabla de factura coincida con el monto neto del documento. Si hay una discrepancia mayor a 0.01, la suma calculada reemplaza el monto neto extraido — asegurando consistencia entre las partidas y los campos de encabezado.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calcular suma de todos los totales de linea
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Comparar con monto neto extraido
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # La suma de lineas difiere del encabezado — actualizar monto neto
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variacion: Marcar como invalido en lugar de sobrescribir

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
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## Explicacion Paso a Paso

1. **Obtener tabla de factura** de `tables_dict`
2. **Sumar todos los valores LINE_TOTAL** a traves de las filas de la tabla
3. **Comparar** la suma calculada con el monto neto extraido
4. **Actualizar o marcar** — ya sea reemplazar el monto neto o marcarlo como invalido

## Funciones Utilizadas

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Leer valores de columna de filas
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer monto neto
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Establecer monto corregido
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Marcar campo como invalido
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Marcar campo como valido
