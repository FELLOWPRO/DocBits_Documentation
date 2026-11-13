---
description: "P1: Diferenciar asignación, tarea y aprobación secuencial"
---

# P1: Diferenciar asignación, tarea y aprobación secuencial

Una **asignación documental** determina la responsabilidad actual. Una **tarea** es un trabajo separado. Una **notificación** informa. Ninguna constituye ya una aprobación personal. Asignar a un grupo tampoco demuestra el consentimiento de todos sus miembros.

Las tarjetas secuenciales reúnen destinatarios y orden del proceso. El ejemplo usa revisor A con orden 10 y B con 20. La finalización revisada comienza por el menor valor. El paso a B depende de la decisión del usuario procesada en el circuito de aprobación; un nodo Wait no realiza por sí solo ese traspaso.

Evite la asignación directa en la misma ejecución si espera al primer destinatario secuencial: la finalización puede omitir esa primera asignación cuando el documento ya se asignó directamente. Configure `task_type`, prioridad, destinatario y `send_email` por separado. Mantenga el correo desactivado durante ejercicios.

La aceptación requiere A→aprobar→B→aprobar, rechazo por A, destinatario ausente y evento repetido. El rechazo debe impedir la exportación final; un destinatario no resuelto no debe aparecer como aprobación completada. Compruebe responsabilidad documental y tareas por separado. La simulación del diseñador no demuestra un traspaso real entre usuarios.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4" %}

**Vídeo:** Aprobación en dos pasos con tablas de decisión · 2:50 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**Dos pasos, dos tablas de decisión** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=0.25)

Una aprobación en dos pasos: primero los aprobadores que devuelve una tabla de decisión, luego un grupo final que siempre va al final. Dos tablas de decisión: una devuelve usuarios, la otra un grupo.

**Una cadena: tabla, asignación, tabla, asignación** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=12.283)

Coloque cada tarjeta de asignación justo después de su propia tabla de decisión, en una sola cadena: tabla, asignación, tabla, asignación. Ambas tablas guardan sus resultados.

**Cada asignación justo tras su tabla** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=25.583)

Un Workflow solo conserva el último resultado de una tabla de decisión. Cada tarjeta de asignación lo lee al ejecutarse, así que debe ejecutarse antes de que la siguiente tabla lo reemplace.

**Las prioridades fijan el orden** · [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=37.15)

El orden de las aprobaciones viene de las prioridades, no del orden de las tarjetas: el número más bajo recibe el documento primero. Dé al grupo final el número más alto.

**Prueba: aprobadores, luego el grupo** · [0:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=48.15)

La prueba muestra cada tarjeta con éxito. La primera tarjeta de asignación pone en cola a los dos aprobadores, la segunda al grupo final. Al final de la ejecución, una última asignación entrega el documento al primero de ellos.

**En paralelo: no funciona** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=76.216)

Esta disposición no funciona. Dos rutas en paralelo parecen iguales, pero el Workflow las ejecuta paso a paso: primero ambas tablas, luego ambas tarjetas de asignación.

**Se pierden los aprobadores - sin error** · [1:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=87.65)

La prueba ejecuta primero ambas tablas y luego ambas tarjetas de asignación. Las dos leen el resultado de la segunda tabla: el grupo entra dos veces en la cola y los aprobadores se pierden. Cada tarjeta sigue mostrando éxito, nada le avisa. Use la cadena.

**Un último aprobador fijo: prioridad 99** · [1:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=117.75)

En un Workflow Estándar, un aprobador fijo puede ir siempre al final: asigne los usuarios de la tabla y luego añada una tarjeta que asigne un usuario con prioridad alta, por ejemplo 99.

**Prioridades de la tabla más bajas** · [2:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=129.55)

Las prioridades de la tabla deben quedar por debajo de ese número. Si la tabla no encuentra a nadie, el Workflow se detiene en la tarjeta de la tabla y no se asigna a nadie. Un usuario que devuelven ambas se consulta dos veces.

**Comprobarlo en una prueba** · [2:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/es.mp4#t=142.083)

Un Workflow Estándar prueba una tarjeta cada vez, así que pruebe las mismas tarjetas en un Advanced Workflow. La primera tarjeta pone en cola a los aprobadores de la tabla, la segunda añade el usuario fijo. Sus prioridades lo dejan al final.

</details>

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `action_assign_doc_to_user_sequential` · v2

Identidad: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identidad: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Aprobar → B → Aprobar |
| ASSIGN-02 | A → Rechazar | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Ruta alternativa |
| ASSIGN-04 | RUN-1 → RUN-2 | compruebe duplicados |
| ASSIGN-05 | direct + sequential | compruebe primer destinatario |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
