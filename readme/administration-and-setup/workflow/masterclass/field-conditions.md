---
description: "P1: Elegir Field is, Docfield is o Compare two Fields"
---

# P1: Elegir Field is, Docfield is o Compare two Fields

Use **Field is** para comprobar el estado vacío, **Docfield is** para comparar con un valor configurado y **Compare two Fields** para dos valores del documento actual. La comprobación de vacío no demuestra que exista el campo en el diseño ni que sea válido para el negocio.

En Field is v2, campo ausente, `null`, texto vacío, solo espacios y booleano `false` significan vacío. El número `0`, el texto `"0"` y el texto `"false"` no están vacíos. Estos ocho casos se probaron en Dev con datos documentales completos. Use una condición de casilla explícita cuando la decisión sea verdadero/falso.

`"1000.01"` en un campo AMOUNT difiere de los mismos caracteres en un campo de texto. El paquete v2 usa AMOUNT y puntos decimales en JSON. Compruebe conjuntamente clave técnica, diseño y tipo. Una etiqueta traducida no es una clave técnica, ni un símbolo monetario un valor numérico.

Para Compare two Fields, defina campo izquierdo, operador y campo derecho. Compruebe tipos compatibles y ambas entradas; un valor ausente o no comparable es un error de datos, no una desigualdad demostrada. Repita casos positivo, negativo, entrada ausente y límite exacto. Registre valor, tipo y salida elegida.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `condition_docfield_status` · v2

Identidad: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identidad: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identidad: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Pruebas y límites

Se comprobaron resultados seleccionados de tarjetas y nodos con datos sintéticos en Advanced Test. Las respuestas están en el paquete. Las acciones documentales son simuladas; no prueban una ejecución persistida ni una entrega externa.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
