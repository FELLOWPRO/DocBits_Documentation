---
description: "Elegir Field is, Docfield is o Compare two Fields"
---

# P1: Elegir Field is, Docfield is o Compare two Fields

Tres tarjetas de condición se parecen en el diseñador, y su diferencia decide qué puede detectar realmente una regla. Esta página le ayuda a elegir la correcta y después le da tres ejercicios cortos que muestran qué devuelve cada tarjeta. Al final sabrá distinguir «vacío» de «cero», «falso» de «ausente» y una condición no cumplida de un error.

Haga los ejercicios en Advanced Test, en su propia organización de pruebas y con un documento sintético. Aquí no se toca ningún documento de cliente.

## ¿Qué tarjeta necesita?

| Si quiere comprobar... | Use | Tarjeta y versión |
| --- | --- | --- |
| si un campo contiene algún valor | **Field is** | `condition_docfield_status` v2 |
| un campo frente a un valor que usted introduce | **Docfield is** | `condition_docfield_operator_value` v2 |
| dos campos del mismo documento entre sí | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Las tres son condiciones: devuelven un resultado y no cambian nada en el documento. Una comprobación de estado vacío no demuestra que un campo exista en el layout ni que su contenido sea válido para el negocio. Las páginas de cada tarjeta detallan todos los ajustes: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) y [Compare two Fields](../and/document-field/compare-two-fields.md).

## Ejercicio 1: averiguar qué significa «vacío»

**Objetivo:** saber qué valores trata Field is versión 2 como vacíos.

1. Añada **Field is** versión 2 a una regla de su organización de pruebas y seleccione un campo de texto de su layout.
2. Ponga el estado del campo en `field_empty` (Empty or missing).
3. Ejecute ocho casos de Advanced Test con datos de documento completos: campo ausente, `null`, texto vacío `""`, solo espacios `" "`, booleano `false`, número `0`, texto `"0"` y texto `"false"`.

**Listo cuando:** los cinco primeros casos devuelvan `field_empty=success` y los tres últimos `field_empty=failed_condition`. Estos ocho casos se probaron en Dev con datos de documento completos.

El número `0`, el texto `"0"` y el texto `"false"` son valores, no ausencias. Si su decisión de negocio es verdadero o falso, use una condición de casilla explícita en lugar de comprobar si el campo está vacío.

## Ejercicio 2: comparar un campo con un valor

**Objetivo:** ver cómo el operador y el tipo de campo cambian la respuesta.

1. Elija un campo numérico como `total_amount`, el operador `gt` y el valor `1000`.
2. Pruebe `1000`, `1000.01`, un campo ausente y un valor no válido.

**Listo cuando:** `1000` devuelva `failed_condition`, porque `gt` significa estrictamente mayor, `1000.01` devuelva `success` y una entrada ausente o no válida devuelva `error`.

## Ejercicio 3: comparar dos campos

**Objetivo:** saber cuándo se comparan dos valores y cuándo la tarjeta no puede compararlos en absoluto.

1. Defina el campo izquierdo, el operador y el campo derecho. Use dos campos con tipos compatibles.
2. Pruebe valores iguales, valores distintos y una entrada ausente.

**Listo cuando:** los valores iguales cumplan `eq`, los valores distintos devuelvan `failed_condition` y una entrada ausente devuelva `error` en lugar de una desigualdad demostrada.

## Qué significan los tres resultados

| Resultado | Qué le dice |
| --- | --- |
| `success` | La tarjeta comparó los valores y la condición se cumplió. |
| `failed_condition` | La tarjeta comparó los valores y la condición no se cumplió. `0` y `"0"` acaban aquí en una comprobación de estado vacío. |
| `error` | La tarjeta no pudo comparar, por ejemplo porque falta un valor o no es válido. Un error no es la misma respuesta que «distinto». |

## El tipo forma parte de la comparación

Un valor `"1000.01"` en un campo AMOUNT no es lo mismo que los mismos caracteres en un campo de texto. El paquete de formación v2 usa AMOUNT y puntos decimales en JSON. Revise juntos la clave técnica del campo, el layout y el tipo. Una etiqueta traducida no es una clave técnica, y un símbolo de moneda no es un valor numérico.

## Tarjetas y parámetros de ejemplo

Estos valores describen parámetros de tarjetas individuales, no un workflow completo importable. Sustituya YOUR\_\* por sus propias selecciones de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe las versiones disponibles y los permisos en su propia organización.

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
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Pruebas y límites

Algunos resultados de tarjeta y de nodo se comprobaron con datos sintéticos en Advanced Test. Las respuestas están en el paquete de formación. Las acciones de documento son simuladas; estas pruebas no demuestran una ejecución de documento guardada ni una entrega externa.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
