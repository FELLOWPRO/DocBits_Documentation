---
description: "P1: Diferenciar asignación, tarea y aprobación secuencial"
---

# P1: Diferenciar asignación, tarea y aprobación secuencial

Una **asignación documental** determina la responsabilidad actual. Una **tarea** es un trabajo separado. Una **notificación** informa. Ninguna constituye ya una aprobación personal. Asignar a un grupo tampoco demuestra el consentimiento de todos sus miembros.

Las tarjetas secuenciales reúnen destinatarios y orden del proceso. El ejemplo usa revisor A con orden 10 y B con 20. La finalización revisada comienza por el menor valor. El paso a B depende de la decisión del usuario procesada en el circuito de aprobación; un nodo Wait no realiza por sí solo ese traspaso.

Evite la asignación directa en la misma ejecución si espera al primer destinatario secuencial: la finalización puede omitir esa primera asignación cuando el documento ya se asignó directamente. Configure `task_type`, prioridad, destinatario y `send_email` por separado. Mantenga el correo desactivado durante ejercicios.

La aceptación requiere A→aprobar→B→aprobar, rechazo por A, destinatario ausente y evento repetido. El rechazo debe impedir la exportación final; un destinatario no resuelto no debe aparecer como aprobación completada. Compruebe responsabilidad documental y tareas por separado. La simulación del diseñador no demuestra un traspaso real entre usuarios.

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
