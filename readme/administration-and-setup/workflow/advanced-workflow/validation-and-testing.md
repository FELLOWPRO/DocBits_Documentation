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

## Validate

Haz clic en el control **Validate** (el icono de círculo con marca de verificación, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validación revisa el grafo en busca de problemas (nodos sin conectar, configuración faltante y conexiones no válidas) y los señala para que puedas corregirlos antes de que el flujo de trabajo se ejecute con documentos reales.

## Test

Haz clic en el control **Test** (el icono de reproducción, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para ejecutar el flujo actual con una muestra y observar cómo se comporta, sin afectar a los documentos en producción. Esta es la forma más rápida de comprobar un cambio que acabas de hacer en el lienzo.

## Cuándo usar cada uno

- **Validate / Test en el editor** (esta página) — retroalimentación instantánea mientras diseñas el flujo.
- **[Test Manager](../test-manager.md)** — guarda el escenario para poder volver a ejecutarlo más tarde (y junto con todos tus demás escenarios) y detectar regresiones tras cambios futuros.

## Próximos pasos

- Repasa los tipos de nodos y conexiones en [Nodos](nodes.md).
- Consulta todos los controles de la barra de herramientas y el lienzo en [Barra de herramientas y lienzo](toolbar-and-canvas.md).
