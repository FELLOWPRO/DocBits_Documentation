---
description: "P1: Definir la referencia de tolerancias y comparación PO"
---

# P1: Definir la referencia de tolerancias y comparación PO

La tolerancia porcentual depende del **lado de referencia**. En la tarjeta PO v5 revisada, `document_po` compara documento contra pedido; el pedido es la base porcentual. `po_document` invierte comparación y base. Las seis direcciones permitidas también incluyen el valor recibido. Defina dirección, operador y Any/All explícitamente.

Ejemplo: pedido 100, documento 102.02, igualdad con 2 %. Con referencia al pedido, el intervalo es 98–102: fuera. Con referencia al documento, es 99.9796–104.0604: el pedido 100 está dentro. Documento 102 coincide con el límite superior inclusivo de la primera dirección. Una tolerancia absoluta de 2 utiliza la unidad del valor comparado.

La tarjeta normaliza precios por unidad de precio y usa datos de pedido o recepción según la dirección. Compruebe asociación, cantidades y unidades. Any requiere una comparación coincidente; All todas las comparaciones realizadas. **Ninguna línea comparable** produce error de datos en v5, no un All satisfecho automáticamente. Registre por separado las filas sin asociar.

En workflows existentes, revise versión, dirección y operador guardados: las migraciones modificaron ajustes. Las etiquetas antiguas no bastan para aceptar. Registre valores, referencia, límite, exceso mínimo, precisión, pedido ausente y línea sin asociar. Este cálculo no sustituye la aceptación con sus datos maestros PO.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

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
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | error de datos |
| PO-05 | unmatched_rows>0 | compruebe cobertura por separado |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
