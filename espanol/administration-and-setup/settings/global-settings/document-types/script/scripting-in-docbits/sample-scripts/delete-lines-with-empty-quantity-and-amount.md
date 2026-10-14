# Eliminar lineas con cantidad y monto vacios

#### Parte 1: Eliminar Lineas con Cantidad y Monto Vacios

Esta seccion del script procesa una tabla de factura para eliminar cualquier linea donde tanto la cantidad como el monto total sean cero o no esten proporcionados.

* **Verificar INVOICE\_TABLE:** Comienza verificando si la clave `INVOICE_TABLE` existe en el diccionario `tables_dict`.
* **Iterar sobre Filas:** Para cada fila en la tabla, el script inicializa flags y variables para determinar si existen las columnas `TOTAL_AMOUNT` y `QUANTITY` y para capturar sus valores.
* **Verificar Nombres de Columnas:** Al iterar a traves de cada columna en una fila, busca columnas llamadas `TOTAL_AMOUNT` y `QUANTITY`.
  * Si se encuentra `TOTAL_AMOUNT`, captura el valor. Si este valor no es cero, lo convierte a numero de punto flotante.
  * De manera similar para `QUANTITY`, capturando y convirtiendo el valor si no es cero.
* **Marcar Fila para Eliminacion:** Despues de verificar ambas columnas en una fila, si tanto el monto total como la cantidad son efectivamente cero (ya sea por ser cero o por no existir), la fila se marca para eliminacion estableciendo `row['is_deleted']` en `True`.

#### Parte 2: Validar Total de Lineas contra Total de Factura

Esta seccion calcula el monto total de todas las lineas en una factura y lo compara con el total reportado de la factura para validar su consistencia.

* **Inicializar Total de Lineas:** Comienza estableciendo una variable `lines_total` en 0.0 para acumular el monto total de todas las lineas.
* **Sumar Montos de Lineas:** Itera sobre cada fila en la `INVOICE_TABLE`, extrayendo el `TOTAL_AMOUNT` de cada una y anadiendolo a `lines_total`.
* **Recuperar y Convertir Total de Factura:** Obtiene el monto total de la factura usando una funcion auxiliar `get_field_value` y lo convierte a numero de punto flotante.
* **Comparar Totales:** Finalmente, verifica si la diferencia absoluta entre el total calculado de lineas (`lines_total`) y el total reportado de la factura (`total_amount`) excede un umbral de 0.05. Si es asi, marca el campo de total de factura como invalido usando otra funcion auxiliar `set_field_as_invalid`, citando una discrepancia.

```python
##################################################
# Eliminar lineas con cantidad y monto vacios
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
# Fin: Eliminar lineas con cantidad y monto vacios
##################################################

##################################################
# Validar total de lineas contra total de factura
##################################################
lines_total = 0.0
# Obtener total de lineas
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

# Obtener total de factura
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparar total de lineas con total de factura
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Fin: Validar total de lineas contra total de factura
##################################################
```

#### Resumen

El script asegura efectivamente la integridad de los datos mediante:

1. Eliminar filas de datos que no contribuyen al total financiero de la factura debido a la falta de cantidades o montos.
2. Validar la consistencia entre la suma de los montos individuales de lineas y el total general de la factura, destacando discrepancias para acciones adicionales.

Esta automatizacion ayuda a mantener registros financieros precisos y puede ser crucial para sistemas como ERP que requieren datos precisos para contabilidad e informes financieros.
