---
description: "P1: Calcular columnas y comprobar dependencias regex"
---

# P1: Calcular columnas y comprobar dependencias regex

**Calculate Columns** calcula entre dos columnas de una fila y escribe el resultado. **Calculate in / CALC_COLUMNS_REGEX** añade una condición regex en una tercera columna. Aquí la regex decide si calcular; no extrae ni reemplaza texto. La explicación anterior de sustituciones no describe esta tarjeta.

Ejemplo: `QTY=2`, `PRICE=10`, operación `*`, resultado `TOTAL=20.0`. Para la variante regex use `TYPE` y patrón `^A$`. Una fila A se calcula. En una fila B no coincidente, el código revisado escribe resultado vacío; un TOTAL existente no se conserva automáticamente.

La función aritmética redondea resultados numéricos a cuatro decimales. Un operando vacío puede convertirse en 0; dos textos vacíos devuelven vacío. `+` puede concatenar textos no numéricos. En la función revisada, `10/0` produce error. Valide números y celdas obligatorias antes del cálculo y configure una ruta de error.

Conserve una tabla completa antes/después: dos filas coincidentes, una no coincidente, entrada vacía, texto inválido y división por cero. Para cálculos dependientes A→B, conecte las tarjetas explícitamente y compruebe el valor actualizado que lee B. Compare cada fila y las columnas ajenas existentes, además del estado documental.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `calc_columns` · v2

Identidad: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identidad: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
