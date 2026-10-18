# Barra de herramientas y lienzo

## Vídeo: Constructor y lienzo

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.mp4" %}

[Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.vtt) · 1:56

<details>
<summary>Transcripción</summary>

**Una factura con dos rutas**

Este es un flujo avanzado real en DocBits. Una comprobación del importe de la factura conduce a dos acciones. Las conexiones determinan qué acción se ejecuta. El ejemplo utiliza un borrador sin guardar y campos de demostración.

**Configurar la comprobación**

Abra Añadir, elija And y seleccione una condición de campo del documento. Indique el campo del importe, elija Mayor que e introduzca mil. Utilice la clave exacta del campo en la configuración del documento.

**Configurar las acciones**

Añada dos tarjetas Then. Ambas establecen el campo de demostración approval route. Una escribe Approval y la otra Standard. Estos valores identifican la ruta. Configure las acciones de su proceso para un flujo de producción.

**Conectar las salidas**

Conecte Start con la entrada de la condición. Conecte la salida azul de éxito con Approval y la salida naranja de condición falsa con Standard. La salida roja trata los errores de evaluación por separado. La posición de una tarjeta no crea una ruta.

**Preparar los casos de prueba**

Abra Probar en la barra de herramientas. Seleccione un documento de prueba o introduzca sus datos completos en JSON. Compruebe importes superiores, inferiores e iguales a mil, además de valores ausentes. Revise los resultados de los nodos después de ejecutar.

**Validar, guardar y activar**

Valide las conexiones y la configuración de las tarjetas. Guarde explícitamente en el servidor y compruebe la activación por separado. Los borradores automáticos del navegador no sustituyen a Guardar. La ejecución y los registros requieren el módulo y la suscripción adecuados.

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
