---
description: "Definir la referencia de tolerancias y comparación PO"
---

# P1: Definir la referencia de tolerancias y comparación PO

Una tolerancia del 2 por ciento no es un importe fijo. Es el 2 por ciento del lado con el que compara, así que la misma línea de factura puede fallar en una dirección y pasar en la otra. Esta página lo muestra con un par de valores, le da tres ejercicios para reproducirlo y después enumera las seis direcciones de comparación y los parámetros de tarjeta que puede copiar en su propia prueba.

Haga los ejercicios en Advanced Test, en su propia organización de pruebas, con un documento sintético y un pedido asociado.

## El lado de referencia es la base

En la tarjeta PO versión 5 examinada, `document_po` compara el valor del documento con el valor del pedido, así que el pedido es la base de una tolerancia porcentual. `po_document` invierte tanto la comparación como la base. Las seis direcciones permitidas incluyen además el lado recibido. Defina dirección, operador y Any/All explícitamente en lugar de confiar en lo que aún guarda una tarjeta existente.

## Ejercicio 1: los mismos valores, dos direcciones

**Objetivo:** ver cómo de las mismas cifras salen dos resultados distintos.

1. Prepare un pedido asociado de `100` y un precio unitario en el documento de `102.02`.
2. Compare con el operador `eq` y una tolerancia de `2` por ciento, primero con `document_po`. Espere `false`: el 2 por ciento de 100 es 2, así que el intervalo cerrado va de 98 a 102, y 102.02 queda 0.02 por encima.
3. Repita el mismo caso con `po_document`. Espere `true`: el 2 por ciento de 102.02 es 2.0404, el intervalo va de 99.9796 a 104.0604, y el valor del pedido 100 cae dentro.

**Listo cuando:** ambos resultados y ambos intervalos estén anotados, y pueda decir de qué valor se calculó el porcentaje en cada dirección.

Una tolerancia absoluta de `2` se comporta de otra forma: usa la unidad del valor comparado y no se desplaza con la referencia.

## Ejercicio 2: encontrar la frontera exacta

**Objetivo:** saber si el borde del intervalo cuenta.

1. Mantenga `document_po`, `eq` y la tolerancia del 2 por ciento, y cambie el valor del documento a `102`.
2. Ejecute el caso y después repítalo con `102.01`.

**Listo cuando:** `102` devuelva `true` y `102.01` devuelva `false`. El límite es inclusivo: 102 cae exactamente en la frontera superior del intervalo 98 a 102.

## Ejercicio 3: Any, All y las líneas comparadas

**Objetivo:** saber qué hace la tarjeta con varias líneas y qué ocurre cuando no hay nada que comparar.

1. Cree un documento con dos líneas contra el mismo pedido asociado: una dentro de la tolerancia y otra fuera.
2. Ejecute la tarjeta con `match_any` y después con `match_all`.
3. Ejecute un documento que no tenga ninguna línea comparable.

**Listo cuando:** `match_any` pase con la única línea que coincide, `match_all` falle en cuanto falla una comparación, y el documento sin línea comparable devuelva un error de datos. En la versión 5 eso es un error y no un All satisfecho automáticamente.

## ¿Qué lado es la base?

| Opción guardada | Lado comparado | Lado de referencia (base porcentual) |
| --- | --- | --- |
| `po_document` | Pedido | Documento |
| `received_document` | Datos recibidos | Documento |
| `po_received` | Pedido | Datos recibidos |
| `document_po` | Documento | Pedido |
| `document_received` | Documento | Datos recibidos |
| `received_po` | Datos recibidos | Pedido |

## Compruebe antes de confiar en un workflow existente

La tarjeta normaliza los precios por unidad de precio y usa datos de pedido o de recepción según la dirección, así que revise primero la asociación, las cantidades y las unidades. Any necesita una comparación coincidente; All, todas las comparaciones realizadas. Las filas sin asociar se registran aparte.

En workflows existentes vuelva a leer la versión guardada, la dirección y el operador: las migraciones cambiaron ajustes de comparación, así que las etiquetas históricas no bastan como evidencia de aceptación. Anote los valores y la referencia, la frontera exacta, el exceso más pequeño, la precisión de redondeo, el pedido ausente y la línea sin asociar. Este cálculo no sustituye la aceptación con sus propios datos maestros de PO.

## Tarjetas y parámetros de ejemplo

Estos valores describen parámetros de tarjetas individuales, no un workflow completo importable. Sustituya YOUR\_\* por sus propias selecciones de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe las versiones disponibles y los permisos en su propia organización.

### `condition_docfield_operator_docfield_tolerances` · v2

Identidad: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identidad: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | error de datos |
| PO-05 | unmatched\_rows>0 | revisar cobertura por separado |

## Pruebas y límites

Los parámetros y el comportamiento se comprobaron contra el catálogo de Dev y la revisión de código examinada. Los casos de prueba de negocio son un procedimiento de aceptación. En este capítulo no se realizaron aprobaciones personales, cambios de datos reales ni entregas.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
