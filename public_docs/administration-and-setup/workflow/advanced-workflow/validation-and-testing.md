# Validación y pruebas

## Vídeo: Variables, pruebas y activación

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/es.vtt) · 1:58

<details>
<summary>Transcripción</summary>

**Elija el tipo de variable**

Abra Variables con las llaves. Elija texto, número, sí o no, o documento. Busque nombres. Document guarda una referencia mediante una acción específica; este formulario no admite valores de documento.

**Variables de la organización**

Elija nombre único, tipo y valor inicial. Crear, editar o eliminar se guarda inmediatamente para la organización. Otros workflows comparten estos valores. Guardar o descartar el lienzo no deshace cambios de variables.

**Valide primero la estructura**

Pulse Validar. Revise errores y advertencias sobre el lienzo. Pulse un mensaje para enfocar su nodo. Compruebe acciones, entradas, salidas, ciclos y uniones. Una estructura válida no garantiza datos correctos.

**Elija el contexto de prueba**

Reproducir en la barra abre la selección del documento. Elija documento, datos personalizados o prueba sin documento para tarjetas independientes. Start ejecuta directamente. Las pruebas incluyen cambios sin guardar y simulan acciones destructivas.

**Preparar y revisar escenarios de prueba**

Prepara pruebas separadas por encima, por debajo y exactamente en mil, además de datos ausentes. Después, revisa mensajes y duraciones: verde indica éxito, naranja falso, rojo error y gris omitido. Repite las correcciones. Usa el gestor de pruebas para escenarios repetibles.

**Guarde antes de activar**

El guardado automático conserva un borrador local aproximadamente cada treinta segundos tras cambios. Guarde explícitamente en el servidor. Active después del primer guardado. Compruebe el estado en la lista antes de esperar ejecución automática.

</details>

[Ver los cinco capítulos](../advanced-workflow-videos.md)

Mientras construyes un flujo de trabajo Avanzado, dos controles de la barra de herramientas te permiten comprobarlo sin salir del editor. Son para *comprobaciones rápidas durante la construcción*; para pruebas guardadas y repetibles, usa el [Test Manager](../test-manager.md).

## Validar

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.mp4" %}

**Vídeo:** Validar un Workflow · 0:47 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**Validar comprueba la construcción** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.mp4#t=0.25)

Antes de guardar, haga clic en Validar el flujo de trabajo en la barra de herramientas. Comprueba cómo está construido el flujo: si una tarjeta Cuando lo inicia, si cada tarjeta está conectada y si los caminos tienen sentido. Los problemas aparecen sobre el lienzo.

**Un clic en el mensaje lleva a la tarjeta** · [0:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.mp4#t=15.85)

Haga clic en un mensaje para ir a la tarjeta de la que trata. Aquí la tarjeta de asignación no está conectada, así que nunca se ejecutaría. Conéctela.

**Sin mensajes: el flujo es válido** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.mp4#t=26.35)

Valide de nuevo. Cuando no queda nada, el flujo es válido y puede guardarlo.

**Primero validar, luego probar** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-validate/v1/es.mp4#t=32.25)

Guardar hace las mismas comprobaciones, pero guarda el flujo aunque queden problemas, así que valide primero. Validar no comprueba sus datos ni los ajustes dentro de las tarjetas. Para ver qué hace un flujo con un documento real, pruébelo.

</details>

Haz clic en el control **Validate** (el icono de círculo con marca de verificación, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validación revisa el grafo en busca de problemas (nodos sin conectar, configuración faltante y conexiones no válidas) y los señala para que puedas corregirlos antes de que el flujo de trabajo se ejecute con documentos reales.

## Test

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4" %}

**Vídeo:** Probar un Workflow · 1:31 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.vtt)

<details>

<summary>Transcripción</summary>

**Probar antes de activar** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=0.25)

Pruebe un flujo antes de activarlo. Una prueba ejecuta lo que hay en el lienzo ahora, también los cambios sin guardar. Acciones como asignar o exportar solo se simulan, así que el documento queda como está.

**Probar todo el flujo** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=12.45)

Aquí hay un flujo que aún no está guardado. Para probar todo el flujo, haga clic en Flujo de trabajo de prueba en la barra de herramientas.

**Elegir un documento de prueba** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=20.183)

Elija el documento para la prueba. Los flujos que no necesitan documento también se pueden probar sin él. Busque el documento por su nombre, selecciónelo y haga clic en Prueba.

**Leer el resultado en el lienzo** · [0:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=31.85)

La prueba sigue el camino del documento. Esta factura no está pendiente de aprobación, así que la tarjeta Y termina con una condición fallida y el camino naranja sigue hasta la tarjeta de asignación. Los caminos no tomados aparecen en gris, y el banner de arriba muestra el resultado y cuánto duró la prueba.

**Detalles de cada tarjeta** · [0:48](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=48.55)

Haga clic en Detalles para ver cada tarjeta con su resultado y su mensaje. Repetir la prueba la ejecuta de nuevo después de un cambio.

**Probar una sola tarjeta** · [0:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=56.983)

Para probar una sola tarjeta, pase el ratón por encima y haga clic en el botón de reproducir. También puede hacer clic derecho en la tarjeta y elegir Prueba desde este nodo. La prueba empieza en esta tarjeta, con la misma elección de documento.

**La insignia muestra los detalles** · [1:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=70.083)

Solo se ejecutan esta tarjeta y las siguientes. Pase el ratón por la insignia para ver el resultado de la tarjeta. Cambie la tarjeta y pruebe de nuevo hasta que haga lo que espera.

**Qué significan los colores** · [1:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-testing/v2/es.mp4#t=80.283)

En resumen: verde significa éxito, naranja una condición fallida y rojo un error. Las tarjetas que no se ejecutaron aparecen atenuadas con una insignia gris.

</details>

Haz clic en el control **Test** (el icono de reproducción, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para ejecutar el flujo actual con una muestra y observar cómo se comporta, sin afectar a los documentos en producción. Esta es la forma más rápida de comprobar un cambio que acabas de hacer en el lienzo.

## Cuándo usar cada uno

- **Validate / Test en el editor** (esta página) — retroalimentación instantánea mientras diseñas el flujo.
- **[Test Manager](../test-manager.md)** — guarda el escenario para poder volver a ejecutarlo más tarde (y junto con todos tus demás escenarios) y detectar regresiones tras cambios futuros.

## Próximos pasos

- Repasa los tipos de nodos y conexiones en [Nodos](nodes.md).
- Consulta todos los controles de la barra de herramientas y el lienzo en [Barra de herramientas y lienzo](toolbar-and-canvas.md).
