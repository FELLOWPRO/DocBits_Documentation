---
description: "P1: Seguir la tabla de decisión hasta la asignación"
---

# P1: Seguir la tabla de decisión hasta la asignación

Una tabla de decisión conecta campos de entrada con resultados tipificados. El ejemplo usa `cost_center=4711` y `total_amount`: revisor A hasta 1000 y B por encima. Cree dos reglas sin solapamiento y utilice usuarios válidos de su organización de prueba. El archivo del paquete describe la configuración; no garantiza una importación en el editor.

En **Decision Table has Returns** v3, active `store_data=wf_store_data`. La v2 lee en cambio la opción booleana de almacenamiento. La asignación siguiente necesita resultados guardados en la misma ejecución. Ejecutar la tabla correctamente no confirma un usuario válido.

Un resultado de usuario puede contener `output_type=user` y `value=101`; 101 es sintético y debe sustituirse por un usuario de prueba existente. Después elija **Assign document based on decision table** con `assignee_type=user`. La versión 2 revisada de esa acción selecciona el último resultado coincidente. Varias coincidencias no implican aprobación de todos los usuarios.

Pruebe una, ninguna y varias coincidencias, tipo incorrecto, usuario inválido y almacenamiento desactivado. Dirija ausencia de coincidencia y error de asignación a una alternativa explícita. Establezca orden y política de coincidencias; no convierta el orden accidental en regla de negocio. Acepte la asignación real en el documento.

La condición de tabla de decisión llama realmente al servicio para evaluar la tabla. El modo de prueba no garantiza ausencia de efectos secundarios; use datos propios de prueba y revise las acciones empleadas.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4" %}

**Vídeo:** Tablas de decisión en tarjetas de asignación · 1:49 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.vtt)

<details>

<summary>Transcripción</summary>

**Tablas de decisión en dos pasos** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=0.25)

Las tablas de decisión deciden quién se ocupa de un documento. En un flujo trabajan en dos pasos. Una tarjeta Y ejecuta la tabla de decisión y guarda lo que devuelve. Las tarjetas Entonces usan esos resultados para asignar el documento o crear tareas.

**Éxito, condición fallida o error** · [0:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=15.183)

La tarjeta Y tiene éxito cuando la tabla devuelve al menos una coincidencia para el documento. Sin coincidencia termina como condición fallida y sigue el camino naranja. Sin tabla elegida, o si la tabla no puede ejecutarse, termina como error.

**Ejecutar la tabla y guardar los resultados** · [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=29.883)

Añada la tarjeta Y que comprueba si la tabla de decisión devuelve resultados y elija la tabla. Luego configúrela para que guarde los datos devueltos. Sin eso, las tarjetas siguientes no tienen con qué trabajar.

**El primer usuario recibe el documento** · [0:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=44.916)

En el camino del éxito, la tarjeta Entonces que asigna según el primer usuario devuelto da el documento al primer usuario de la tabla. Cada usuario devuelto, también el primero, recibe una tarea o una notificación. Dé a la tarea un título, una descripción y una prioridad, y elija si también se envía un correo. Los grupos devueltos se ignoran.

**Sin campos: todo de la tabla** · [1:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=70.55)

En cambio, la tarjeta que asigna el documento de forma secuencial a un usuario o grupo según la tabla de decisión no tiene ningún campo. Toma usuarios y grupos de la tabla, cada uno con la prioridad que devuelve la tabla, o una por defecto. Al final de la ejecución, la entrada con el número de prioridad más bajo recibe el documento, salvo que otra tarjeta ya lo haya asignado directamente.

**Qué tarjeta para cada caso** · [1:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/decision-tables/v2/es.mp4#t=90.85)

En resumen: para dar el documento a una persona e informar a todos los demás, use la tarjeta del primer usuario. Para que la tabla lo decida todo, también las prioridades, use la tarjeta secuencial sin campos. Para crear solo tareas, use la tarjeta de tareas para resultados de tablas de decisión.

</details>

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
