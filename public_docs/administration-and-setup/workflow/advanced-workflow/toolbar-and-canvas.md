# Barra de herramientas y lienzo

## Vídeo: Constructor y lienzo

Conoce a Javier y sigue su explicación en la interfaz real de DocBits en español. Revisa el panel de workflows, la lista y la licencia antes de abrir un borrador sin guardar en el diseñador. Paso a paso, nombra el workflow, configura la comprobación del importe y dos acciones, organiza las tarjetas y conecta ambas rutas. Después muestra cómo preparar pruebas con un documento o datos personalizados. La cuenta de demostración no tiene una suscripción de Advanced Workflow y bloquea la validación; el borrador permanece sin guardar e inactivo.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.vtt) · [Transcripción (texto)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.txt) · 3:04

| En este vídeo | Inicio |
| --- | --- |
| Conozca al administrador | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=0) |
| Comprobar el acceso | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=4) |
| Nombrar el workflow | [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=25) |
| Configurar el importe | [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=37) |
| Añadir la acción Approval | [0:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=59) |
| Añadir la acción Standard | [1:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=78) |
| Organizar las tarjetas | [1:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=97) |
| Conectar las rutas | [1:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=112) |
| Preparar las pruebas | [2:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=135) |
| Validar, guardar y activar | [2:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/es.mp4#t=158) |

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

Añado una segunda tarjeta con la misma acción. La acción establece un campo del documento. Uso la clave de demostración approval_route. Esta vez, el campo de demostración recibe el valor Standard. Las dos tarjetas están configuradas. Todavía necesitan conexiones para determinar qué acción se ejecuta.

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4" %}

**Vídeo:** Diseñador de Advanced Workflow: tarjetas y caminos · 2:08 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.vtt)

<details>

<summary>Transcripción</summary>

**Empezar un flujo nuevo** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=0.25)

Abra el Panel de flujo de trabajo y seleccione Nuevo flujo de trabajo.

**Elegir Flujo de trabajo avanzado** · [0:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=5.016)

Elija Flujo de trabajo avanzado. El diseñador se abre con un nodo de inicio, donde empieza cada flujo.

**Cuando, Y y Entonces** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=11.85)

Añada tarjetas con el menú Agregar o con un clic derecho en el lienzo. Las tres categorías de tarjetas son Cuando, Y y Entonces.

**Cuando: la condición de activación** · [0:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=23.916)

La tarjeta Cuando es la condición de activación. Decide cuándo empieza el flujo, por ejemplo para un tipo de documento concreto.

**Y: una condición más** · [0:37](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=37.35)

Las tarjetas Y añaden más condiciones. Comprueban el documento, por ejemplo su estado. El resultado es éxito o una condición fallida.

**Entonces: la tarjeta de acción** · [0:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=50.716)

Las tarjetas Entonces son las tarjetas de acción. Cambian el documento, por ejemplo rellenan un campo o aprueban el documento.

**Arrastrar para conectar** · [0:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=57.95)

Para conectar dos tarjetas, arrastre desde un punto a la derecha de una tarjeta hasta la entrada a la izquierda de la siguiente.

**Azul: éxito** · [1:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=65.516)

El azul es el camino del éxito. Todas las tarjetas lo tienen. El flujo lo toma cuando la tarjeta termina.

**Naranja: condición fallida** · [1:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=72.683)

El naranja es el camino de la condición fallida. Solo lo tienen las tarjetas Y. El flujo lo toma cuando la condición no se cumple.

**Rojo: error** · [1:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=81.45)

El rojo es el camino de error. Lo tienen las tarjetas Y y Entonces. El flujo lo toma cuando una tarjeta falla con un error.

**Si-si no con captura de errores** · [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=89.616)

Juntos, estos caminos forman un si-si no con captura de errores. El éxito ejecuta una acción, una condición fallida otra, y un error una alternativa, por ejemplo una tarea para una persona.

**Un camino por estado** · [1:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=101.416)

Para varios casos, enlace tarjetas de Estado del documento por sus caminos de condición fallida. Cada tarjeta comprueba un estado, así cada estado tiene su propio camino.

**El camino hacia una tarjeta y desde ella** · [1:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-designer/v2/es.mp4#t=111.85)

Haga clic en una tarjeta para resaltar su camino de ejecución: las tarjetas por las que pasa un documento para llegar a ella y las que pueden seguirla. Todo lo demás se atenúa. Aquí, a la tarea solo se llega desde la tarjeta Cuando, por el camino de error rojo de la tarjeta de estado.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4" %}

**Vídeo:** Descripciones y notas del Workflow · 1:00 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**Explique su flujo** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=0.25)

Un flujo con varias ramas es más fácil de mantener cuando se explica solo. El diseñador tiene dos herramientas para ello: una descripción de todo el flujo y notas en el lienzo.

**Describir todo el flujo** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=10.45)

Seleccione Editar descripción en la barra de herramientas y diga en una o dos frases para qué sirve el flujo. La descripción se guarda al guardar el flujo.

**Añadir una nota** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=19.15)

Para explicar un solo paso, haga clic derecho en el lienzo, abra el menú de añadir y elija Nota. La nota aparece donde hizo clic.

**Doble clic para escribir** · [0:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=28.316)

Haga doble clic en la nota para escribir en ella, hasta quinientos caracteres. Haga clic al lado cuando termine.

**Mover y cambiar el tamaño** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=34.683)

Arrastre la nota junto a las tarjetas que explica y tire de su esquina inferior derecha para agrandarla.

**Dar color a las notas** · [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=41.55)

Haga clic derecho en una nota para cambiar su color. Los colores ayudan a agrupar notas, por ejemplo azul para explicaciones y rojo para preguntas abiertas.

**Las notas nunca se ejecutan** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-notes/v1/es.mp4#t=51.683)

Las notas son solo para las personas. No están conectadas a ninguna tarjeta y nunca se ejecutan, así que no cambian lo que hace el flujo.

</details>

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
