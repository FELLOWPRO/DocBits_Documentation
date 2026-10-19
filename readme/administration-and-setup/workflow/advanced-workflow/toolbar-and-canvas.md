# Barra de herramientas y lienzo

## Vídeo: Constructor y lienzo

Conoce a Javier y sigue su explicación en la interfaz real de DocBits en español. Revisa el panel de workflows, la lista y la licencia antes de abrir un borrador sin guardar en el diseñador. Paso a paso, nombra el workflow, configura la comprobación del importe y dos acciones, organiza las tarjetas y conecta ambas rutas. Después muestra cómo preparar pruebas con un documento o datos personalizados. La cuenta de demostración no tiene una suscripción de Advanced Workflow y bloquea la validación; el borrador permanece sin guardar e inactivo.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.vtt) · [Transcripción (texto)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.txt) · 4:42

| En este vídeo | Inicio |
| --- | --- |
| Conozca al administrador | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=0) |
| Comprobar el acceso | [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=5) |
| Nombrar el workflow | [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=35) |
| Configurar el importe | [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=52) |
| Añadir la acción Approval | [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=85) |
| Añadir la acción Standard | [1:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=111) |
| Organizar las tarjetas | [2:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=138) |
| Conectar las rutas | [2:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=171) |
| Preparar las pruebas | [3:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=214) |
| Validar, guardar y activar | [4:09](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/review/advanced_workflows_canvas-admin/20261019-small-monitor-b/es.mp4#t=249) |

<details>
<summary>Transcripción</summary>

**Conozca al administrador**

Administro DocBits. Creamos un control de facturas.

**Comprobar el acceso**

Empiezo en el panel de workflows y abro la lista. Después compruebo la licencia. Workflow y Advanced Workflow necesitan acceso activo. Con ambos accesos habilitados, Nuevo workflow ofrece Advanced Workflow. Esta cuenta de documentación no tiene una licencia de workflow activa. Por eso continúo con una vista previa sin guardar en el diseñador.

**Nombrar el workflow**

Estoy en el diseñador real de DocBits. Primero doy un nombre claro al borrador. Comprobaremos el importe de una factura y usaremos dos acciones sencillas para mostrar las rutas posibles. Esta demostración queda sin guardar.

**Configurar el importe**

Abro el menú para añadir y elijo una tarjeta de condición. En Campo del documento selecciono la condición Docfield. Introduzco el campo total_amount. Después elijo la comparación mayor que. E introduzco mil. Utilice la clave de campo de su propio documento. Exactamente mil no cumple esta comparación.

**Añadir la acción Approval**

Ahora añado una tarjeta de acción de la categoría Campo del documento. La acción establece un campo del documento. Uso la clave de demostración approval_route. E introduzco el valor Approval. Esto identifica la ruta. Un proceso de aprobación real necesita sus propias acciones de negocio.

**Añadir la acción Standard**

Añado una segunda tarjeta con la misma acción. Esta vez, el campo de demostración recibe el valor Standard. Las dos tarjetas están configuradas. Todavía necesitan conexiones para determinar qué acción se ejecuta.

**Organizar las tarjetas**

Arrastro las tarjetas hasta conseguir una disposición legible. Las dos acciones van a la derecha. La condición queda en el centro y Start a la izquierda. Mover una tarjeta cambia su posición. No crea una conexión.

**Conectar las rutas**

Arrastro desde la salida de Start hasta la entrada de la condición. La ruta de éxito lleva a Approval mediante una conexión azul. La ruta naranja de condición no cumplida lleva a Standard. La salida roja de error es una salida distinta para errores de evaluación. Aquí queda sin conectar. En un workflow de producción, decida cómo gestionar esos errores.

**Preparar las pruebas**

El botón de prueba de la barra abre la selección de un documento de prueba. Puedo elegir un documento de demostración o preparar datos personalizados completos. Pruebe importes superiores, inferiores e iguales a mil. Compruebe también un importe ausente. Esta cuenta no tiene licencia Advanced Workflow. Muestro la preparación de la prueba, no un resultado ejecutado.

**Validar, guardar y activar**

La validación comprueba conexiones y ajustes de las tarjetas. En esta cuenta, la falta de licencia bloquea la validación. Con una cuenta habilitada, guardaría explícitamente en el servidor. Después comprobaría la activación por separado. El interruptor está deshabilitado antes del primer guardado. El indicador de borrador automático se refiere a una copia local del navegador. No significa que el workflow esté guardado ni activado.

</details>

[Ver los cinco capítulos](../advanced-workflow-videos.md)

La barra de herramientas del Advanced Workflow se extiende a lo largo de la parte inferior del lienzo y te ofrece todo lo que necesitas para construir, navegar y gestionar el flujo.

## Controles de la barra de herramientas

- **+ Add** — abre el menú de nodos para añadir un nodo (consulta [Nodos](nodes.md)).
- **Undo / Redo** — retrocede o avanza por tus cambios.
- **Zoom in / Zoom out** — cambia el nivel de zoom del lienzo.
- **Workflow name** — nombra el flujo de trabajo en línea.
- **Edit description** — añade una descripción para el flujo de trabajo.
- **Variables** — abre el panel de [Variables](variables.md).
- **Help** — abre el diálogo de ayuda y atajos de teclado.
- **Validate / Test** — comprueba y ejecuta el flujo (consulta [Validación y pruebas](validation-and-testing.md)).
- **Snap to grid** — activa o desactiva el ajuste de los nodos a la cuadrícula para diseños ordenados.
- **Mini-map** — activa o desactiva un pequeño mapa general para navegar por grafos grandes.
- **Save** — guarda el flujo de trabajo. Un indicador de **auto-save** muestra cuándo se guardó el flujo automáticamente por última vez.

## Atajos de teclado

Pulsa <kbd>?</kbd> en el lienzo para abrir el diálogo de ayuda y atajos en cualquier momento.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Diálogo de ayuda y atajos de teclado"><figcaption><p>El diálogo de ayuda y atajos de teclado — atajos, resaltado de la ruta de ejecución y colores de conexión.</p></figcaption></figure>

| Atajo | Acción |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Guardar flujo de trabajo |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Validar flujo de trabajo |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Probar flujo de trabajo |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Deshacer / Rehacer |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Copiar / Pegar / Duplicar nodos seleccionados |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Seleccionar todos los nodos |
| <kbd>Shift</kbd> + Arrastrar | Seleccionar nodos (arrastrar) |
| <kbd>Cmd/Ctrl</kbd> + Clic izquierdo | Añadir/quitar nodo de la selección |
| Clic derecho | Menú para añadir nodos |
| <kbd>Del</kbd> | Eliminar nodo seleccionado |
| <kbd>?</kbd> | Mostrar esta ayuda |

## Próximos pasos

- Construye el flujo con [Nodos](nodes.md) y [Variables](variables.md).
