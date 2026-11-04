# Eliminar líneas con cantidad y monto vacíos

#### Parte 1: Eliminar líneas con cantidad y monto vacíos

Esta sección del script procesa una tabla de facturas para eliminar cualquier línea donde tanto la cantidad como el monto total sean cero o no estén proporcionados.

* **Verificar INVOICE\_TABLE:** Comienza verificando si la clave `INVOICE_TABLE` existe en el diccionario `tables_dict`.
* **Iterar sobre filas:** Para cada fila en la tabla, el script inicializa indicadores y variables para determinar si las columnas `TOTAL_AMOUNT` y `QUANTITY` existen y para capturar sus valores.
* **Verificar nombres de columnas:** Mientras itera a través de cada columna en una fila, busca columnas con los nombres `TOTAL_AMOUNT` y `QUANTITY`.
* Si se encuentra `TOTAL_AMOUNT`, se captura el valor. Si este valor es distinto de cero, se convierte a un número decimal.
* De manera similar para `QUANTITY`, capturando y convirtiendo el valor si es distinto de cero.
* **Marcar fila para eliminación:** Después de verificar ambas columnas en una fila, si tanto el monto total como la cantidad son efectivamente cero (ya sea por ser cero o por no existir), la fila se marca para eliminación estableciendo `row['is_deleted']` en `True`.

#### Parte 2: Validar el total de líneas contra el total de la factura

Esta sección calcula el monto total de todas las líneas en una factura y lo compara con el total reportado en la factura para validar su consistencia.

* **Inicializar total de líneas:** Comienza estableciendo una variable `lines_total` en 0.0 para acumular el monto total de todas las líneas.
* **Sumar montos de líneas:** Itera sobre cada fila en la `INVOICE_TABLE`, extrayendo el `TOTAL_AMOUNT` de cada una y sumándolo a `lines_total`.
* **Recuperar y convertir el total de la factura:** Obtiene el monto total de la factura utilizando una función auxiliar `get_field_value` y lo convierte a un número decimal.
* **Comparar totales:** Finalmente, verifica si la diferencia absoluta entre el total de líneas calculado (`lines_total`) y el total de la factura reportado (`total_amount`) excede un umbral de 0.05. Si es así, marca el campo de total de la factura como inválido utilizando otra función auxiliar `set_field_as_invalid`, citando una discrepancia.
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
#### Resumen

El script garantiza de manera efectiva la integridad de los datos al:

1. Eliminar filas de datos que no contribuyen al total financiero de la factura debido a la falta de cantidades o montos.
2. Validar la consistencia entre la suma de los montos de las líneas individuales y el total general de la factura, resaltando discrepancias para tomar medidas adicionales.

Esta automatización ayuda a mantener registros financieros precisos y puede ser crucial para sistemas como ERP que requieren datos precisos para contabilidad e informes financieros.
