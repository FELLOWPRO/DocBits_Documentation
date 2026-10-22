---
description: "P1: Seguir la tabla de decisión hasta la asignación"
---

# P1: Seguir la tabla de decisión hasta la asignación

Una tabla de decisión conecta campos de entrada con resultados tipificados. El ejemplo usa `cost_center=4711` y `total_amount`: revisor A hasta 1000 y B por encima. Cree dos reglas sin solapamiento y utilice usuarios válidos de su organización de prueba. El archivo del paquete describe la configuración; no garantiza una importación en el editor.

En **Decision Table has Returns** v3, active `store_data=wf_store_data`. La v2 lee en cambio la opción booleana de almacenamiento. La asignación siguiente necesita resultados guardados en la misma ejecución. Ejecutar la tabla correctamente no confirma un usuario válido.

Un resultado de usuario puede contener `output_type=user` y `value=101`; 101 es sintético y debe sustituirse por un usuario de prueba existente. Después elija **Assign document based on decision table** con `assignee_type=user`. La versión 2 revisada de esa acción selecciona el último resultado coincidente. Varias coincidencias no implican aprobación de todos los usuarios.

Pruebe una, ninguna y varias coincidencias, tipo incorrecto, usuario inválido y almacenamiento desactivado. Dirija ausencia de coincidencia y error de asignación a una alternativa explícita. Establezca orden y política de coincidencias; no convierta el orden accidental en regla de negocio. Acepte la asignación real en el documento.

La condición de tabla de decisión llama realmente al servicio para evaluar la tabla. El modo de prueba no garantiza ausencia de efectos secundarios; use datos propios de prueba y revise las acciones empleadas.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `condition_decision_tree_data` · v3

Identidad: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identidad: `699912a7-2369-47e0-9092-8d027e13752a`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | sin resultado / usuario inválido / tipo incorrecto | Ruta alternativa |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | sin resultado guardado para asignación |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
