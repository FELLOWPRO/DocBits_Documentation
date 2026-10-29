# Tareas y notificaciones

### Descripción general

La opción **Tareas y notificaciones** activa la gestión de tareas integrada de DocBits. Cuando está activada, los miembros del equipo pueden crear tareas, asignarse documentos entre sí (por ejemplo, para validación, corrección o aprobación) y recibir notificaciones al respecto.

Esta opción está **desactivada de forma predeterminada**. Cuando se activa, aparecen debajo cuatro opciones más:

* **Recuento de tareas del cuadro de mando**: muestra en el Panel qué documentos tienen tareas abiertas.
* **Permitir el filtro "Todos" para usuarios que no sean administradores**: permite que los usuarios que no son administradores vean todas las tareas.
* **Eliminación de tareas no administrativas**: determina qué tareas pueden eliminar los usuarios que no son administradores.
* **Finalización de tareas no administrativas**: determina qué tareas pueden cerrar los usuarios que no son administradores.

Estas opciones nunca restringen a los administradores de la organización.

### ¿Qué hace?

* **Activada**: Las funciones de Tareas y notificaciones quedan disponibles en DocBits. Los usuarios pueden asignar tareas, seguir su estado y recibir notificaciones cuando algo requiere su atención.
* **Desactivada**: La asignación de tareas y las notificaciones relacionadas quedan desactivadas. Al desactivarla también se desactiva **Recuento de tareas del cuadro de mando**.

### Recuento de tareas del cuadro de mando

**Recuento de tareas del cuadro de mando** controla si el Panel muestra qué documentos tienen tareas abiertas. No añade un contador, sino un icono de tarea en cada documento afectado.

* **Activada**: Un documento con tareas en estado **Abierto** o **En proceso** muestra un icono de tarea en la lista del Panel. Al pasar el cursor sobre el icono se ve cuántas tareas abiertas tiene el documento, por ejemplo "2 Tarea(s) abierta(s)". Las tareas hechas, rechazadas o eliminadas no se cuentan.
* **Desactivada**: El icono se oculta. Las tareas siguen funcionando con normalidad.

{% hint style="info" %}
**Recuento de tareas del cuadro de mando** depende de **Tareas y notificaciones**. Si desactiva Tareas y notificaciones, el icono de tareas del Panel también se desactiva.
{% endhint %}

### Permitir el filtro "Todos" para usuarios que no sean administradores.

El resumen de tareas tiene un filtro **Asignado a** con las opciones **Todo** y **Asignado a mí**. Los administradores siempre disponen de ambas opciones.

* **Activada**: Los usuarios que no son administradores también pueden elegir **Todo** y ver todas las tareas de la organización.
* **Desactivada** (predeterminado): Los usuarios que no son administradores solo disponen de **Asignado a mí**, por lo que el resumen les muestra las tareas que tienen asignadas.

### Eliminación de tareas no administrativas

Pese a su nombre, **Eliminación de tareas no administrativas** no se refiere a un tipo de tarea: determina qué tareas y notificaciones pueden eliminar los usuarios que no son administradores. Los administradores siempre pueden eliminar todas las tareas.

| Opción | Los usuarios que no son administradores pueden eliminar |
| --- | --- |
| **Ninguno** | Ninguna tarea. |
| **Solo tareas creadas** | Las tareas que han creado ellos. |
| **Tareas creadas y asignadas** | Las tareas que han creado ellos y las tareas asignadas a ellos o a uno de sus grupos. Se aplica mientras la opción no se haya cambiado nunca. |
| **Todas las tareas** | Todas las tareas. |

Los usuarios siempre pueden eliminar las tareas que han creado, salvo con **Ninguno**. Por eso, una tarea que no está asignada a nadie solo pueden eliminarla el usuario que la creó, los administradores o los usuarios cuando está seleccionada **Todas las tareas**. Una tarea sin creador registrado, por ejemplo una creada por el sistema, solo pueden eliminarla los usuarios a los que está asignada (con **Tareas creadas y asignadas**), los administradores o los usuarios cuando está seleccionada **Todas las tareas**.

{% hint style="warning" %}
Eliminar una tarea la quita de la lista de tareas sin que se tome ninguna decisión. Si las tareas solo deben cerrarse mediante una decisión, configure **Eliminación de tareas no administrativas** en **Ninguno** y **Finalización de tareas no administrativas** (ver más abajo) en **Solo para administradores**.
{% endhint %}

### Finalización de tareas no administrativas

**Finalización de tareas no administrativas** determina qué usuarios que no son administradores pueden cerrar una tarea, es decir, ponerla en **Hecho** o **Rechazado**. Los administradores siempre pueden cerrar tareas, sea cual sea la opción seleccionada aquí.

| Opción | Quién puede cerrar una tarea |
| --- | --- |
| **Comportamiento predeterminado** | La opción no añade ninguna restricción. Los usuarios pueden cerrar las tareas asignadas a ellos o a uno de sus grupos, como antes de que existiera la opción. Se aplica mientras la opción no se haya cambiado nunca. |
| **Administradores y usuarios asignados** | Los administradores y los usuarios a los que está asignada la tarea, directamente o a través de uno de sus grupos. Una tarea asignada a otra persona, o a nadie, no pueden cerrarla otros usuarios. DocBits también lo comprueba cuando una tarea se modifica a través de la API. |
| **Solo para administradores** | Solo los administradores. |

Con **Administradores y usuarios asignados** o **Solo para administradores**, un usuario que no puede cerrar una tarea:

* no ve el botón verde **Hecho** en la página de la tarea, y la lista de estados de esa página solo ofrece **Abierto** y **En proceso**;
* no puede hacer clic en el círculo de estado de la tarea en el panel de tareas del documento. Al pasar el cursor por encima se muestra "No está permitido marcar esta tarea como completada o rechazada.";
* no ve **Marcar como hecho** para esa tarea en la lista de tareas, y **Marcar como hecho** para una selección permanece oculto mientras haya una tarea de ese tipo seleccionada;
* no puede arrastrar la tarea a la columna **Hecho** o **Rechazado** del tablero de tareas. La tarjeta vuelve a su columna y se muestra el mismo mensaje.

La opción solo restringe el cierre. Los usuarios conservan todos los demás derechos que tenían antes: los usuarios a los que está asignada una tarea pueden seguir editándola, guardándola, moviéndola entre **Abierto** y **En proceso** y reabriéndola después de que se haya hecho. Los usuarios a los que una tarea no está asignada no podían cambiar su estado antes, y siguen sin poder hacerlo.

En los tipos de documento con **Historial de aprobaciones** activado, **Aprobar** sigue completando tareas abiertas del documento, sea cual sea la opción seleccionada aquí: las tareas asignadas al aprobador o a uno de sus grupos, y las tareas no asignadas a nadie. Si el aprobador es administrador, se completan todas las tareas abiertas del documento.

#### Tareas de documentos devueltos a validación

Como con **Administradores y usuarios asignados** o **Solo para administradores** los usuarios no pueden cerrar sus propias tareas, DocBits cierra por sí mismo las tareas abiertas de un documento cuando un documento pendiente de aprobación se devuelve a validación:

* **Restart workflow** en la pantalla de aprobación: se rechazan todas las tareas abiertas del documento.
* **Rechazar y corregir**: se rechazan todas las tareas abiertas del documento.
* **Aprobar y corregir**: se completan las tareas que completaría **Aprobar** (ver más arriba), solo en los tipos de documento con **Historial de aprobaciones** activado. Se rechazan todas las demás tareas abiertas.

Las tareas abiertas se cierran antes de que el documento vuelva a validación. Los flujos de trabajo que se ejecutan con el cambio de estado pueden crear después nuevas tareas para todo lo que aún requiera atención.

Con **Comportamiento predeterminado**, las tareas abiertas siguen abiertas cuando se devuelve un documento, como hasta ahora.

### Beneficios

* **Responsabilidades claras**: Los documentos pueden asignarse a la persona adecuada en lugar de depender del correo electrónico.
* **Nada se olvida**: Las notificaciones recuerdan a los usuarios los documentos que requieren su acción.
* **Trabajo pendiente de un vistazo**: Con **Recuento de tareas del cuadro de mando**, el Panel muestra qué documentos siguen teniendo tareas abiertas.
* **Las decisiones quedan documentadas**: Con las opciones de eliminación y finalización, las tareas solo salen de la cola mediante una decisión o un administrador.

### Cómo usarla

1. Vaya a **Ajustes**.
2. Seleccione **Procesamiento de documentos**.
3. Seleccione **Módulo**.
4. Abra la sección **Tipo de Documento**.
5. Active **Tareas y notificaciones**.
6. (Opcional) Active **Recuento de tareas del cuadro de mando** para mostrar el icono de tarea en el Panel.
7. (Opcional) Active **Permitir el filtro "Todos" para usuarios que no sean administradores** si todos los usuarios deben ver todas las tareas.
8. (Opcional) Elija en **Eliminación de tareas no administrativas** qué tareas pueden eliminar los usuarios.
9. (Opcional) Elija en **Finalización de tareas no administrativas** quién puede cerrar tareas.

Las opciones de eliminación y finalización se guardan en cuanto elige un valor.

### Cuándo usar esta función

* **Equipos que comparten el trabajo con documentos**: Actívela cuando varias personas validan o aprueban documentos y necesitan pasarse el trabajo entre sí.
* **Visibilidad de la carga de trabajo**: Active también **Recuento de tareas del cuadro de mando** cuando el equipo deba ver en el Panel qué documentos siguen teniendo tareas abiertas.
* **Tareas que solo deben cerrar los administradores o una decisión**: Ponga **Finalización de tareas no administrativas** en **Solo para administradores** o **Administradores y usuarios asignados**, y **Eliminación de tareas no administrativas** en **Ninguno**, cuando los usuarios no deban quitar tareas que en realidad no se han hecho.
* **Configuraciones de un solo usuario o totalmente automatizadas**: Puede dejarla desactivada si nadie necesita asignar documentos ni seguir tareas.
