---
description: "Cinco capítulos en español sobre Advanced Workflows y sus registros, con subtítulos y transcripciones."
---

# Vídeos de Advanced Workflow

Los cinco capítulos tienen narración en español, un archivo de subtítulos y una transcripción. El primero muestra cómo crear el workflow de ejemplo paso a paso; los demás profundizan en cada tema.

Los tres primeros capítulos muestran el diseñador real de DocBits con borradores de demostración. La vista previa de búsqueda muestra el procesamiento real de documentos y los controles de registro con resultados vacíos. El capítulo de diagnóstico conserva los diagramas didácticos identificados como ilustraciones.

Cada vídeo incluye subtítulos WebVTT y una transcripción desplegable.

1. [Constructor y lienzo](#builder-and-canvas) · 4:42
2. [Nodos y rutas](#nodes-and-routes) · 2:00
3. [Variables, pruebas y activación](#variables-tests-and-activation) · 1:53
4. [Encontrar la ejecución relevante](#find-the-relevant-execution) · 1:56
5. [Seguir nodos y diagnosticar](#trace-nodes-and-diagnose) · 1:51

## Constructor y lienzo {#builder-and-canvas}

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

## Nodos y rutas {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/es.vtt) · 2:00

<details>
<summary>Transcripción</summary>

**La función de cada nodo**

Start inicia manualmente. When define un evento. Ninguno admite conexiones entrantes. And comprueba una condición. Then ejecuta una acción. Ambos constructores comparten el catálogo de tarjetas. Las notas explican el diseño sin ejecutarse.

**Tres resultados diferentes**

Arrastre una salida a la siguiente entrada. En el diseñador, azul indica éxito, naranja condición falsa y rojo error. And ofrece tres resultados; Then, éxito y error. La vista de ejecución representa el éxito en verde.

**Construya una alternativa**

Compruebe si una factura supera el umbral. Conecte azul con aprobación, naranja con procesamiento normal y rojo con gestión de errores. Una condición falsa puede continuar por su ruta conectada; no detiene todas las ramas.

**Unir con Wait ALL**

Wait ALL une ramas. Cada nodo de origen debe haber seguido una ruta conectada a la unión. Conecte ambas comprobaciones requeridas y la siguiente acción. Una ruta no seleccionada no aporta el resultado necesario.

**Alternativas con ANY y OR**

Wait ANY y OR unen ramas si al menos un origen siguió una ruta conectada. OR requiere dos nodos de origen distintos. Estas uniones no crean opciones exclusivas ni cancelan otras acciones. Pruebe el grafo completo.

**Mantenga el grafo ejecutable**

Los nodos de procesamiento deben ser accesibles desde una entrada. Evite ciclos y conexiones entrantes a Start o When. Incluya una acción Then y valide las rutas. Los nodos Delay importados requieren una duración positiva; Añadir no ofrece Delay.

</details>

## Variables, pruebas y activación {#variables-tests-and-activation}

Siga el workflow de facturas conectado en el diseñador real de DocBits. Abra Variables, compare los tipos y la referencia de documento, localice Validar, prepare pruebas con documentos o datos personalizados y vea Guardar y la activación. Las escenas de prueba muestran la configuración de datos de ejemplo; no muestran un resultado ejecutado.

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

## Encontrar la ejecución relevante {#find-the-relevant-execution}

{% hint style="info" %}
Vista previa para pruebas: pantallas reales de DocBits con acciones del documento, flujo del documento, tiempos de los pasos, registros vacíos y filtros de estado y fecha. El documento no tiene una ejecución guardada de Advanced Workflow. Esta vista previa aún no incluye filas de ejecución, paginación ni diagnóstico de nodos.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/es.vtt) · 1:50

<details>
<summary>Transcripción</summary>

**Empezar por el documento**

En el panel de documentos, abra el menú de acciones y elija Flujo del documento. El historial real muestra la importación y el OCR. Abra un paso para revisar los tiempos de espera y procesamiento. Estos pasos son distintos de los nodos de Advanced Workflow.

**Leer los contadores reales**

Aquí se muestran los registros de workflow del mismo documento. Azul indica el total, rojo los errores, amarillo las condiciones fallidas y verde los éxitos. Este documento de demostración no tiene ejecuciones registradas. Por eso, los cuatro contadores muestran cero.

**Revisar las columnas de ejecución**

Las columnas muestran nombre del workflow, fecha de creación, duración y resultado. Distinga ejecuciones repetidas por la marca de tiempo. Este documento no tiene una fila para abrir.

**Abrir los filtros de estado**

El icono de filtros abre el menú real. Ordene por nombre o fecha de creación, en sentido ascendente o descendente. Estado ofrece éxito, condición fallida y error.

**Elegir fechas y borrar filtros**

Elija el periodo con las fechas de inicio y fin o el calendario. El formato es año, mes y día. Aplicar solicita los resultados. Borrar filtros restablece la selección. Borre la búsqueda por separado.

**Vista previa: falta una ejecución guardada**

Esta vista previa permite comprobar el acceso al documento, sus detalles de procesamiento y los controles de registro. Falta una ejecución guardada de Advanced Workflow para mostrar filas reales, paginación, rutas y mensajes de nodos. Esos resultados no se simulan en este vídeo.

</details>

## Seguir nodos y diagnosticar {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/es.vtt) · 1:51

<details>
<summary>Transcripción</summary>

**Expanda una ejecución**

Expanda la fila del workflow. Una ejecución avanzada muestra el grafo a la izquierda y mensajes a la derecha; un workflow estándar muestra tarjetas en secuencia. Los datos describen aquella ejecución y pueden diferir del diseñador actual.

**Seleccione un nodo**

Desplace o amplíe el grafo y pulse un nodo. Card Logs muestra sus mensajes. Los controles Wait ALL y Wait ANY también pueden tener mensajes de nodo. Relacione el mensaje con el nodo seleccionado y la fecha de ejecución.

**Distinga los resultados**

Verde indica éxito; naranja, condición falsa; rojo, error; gris, omitido. Un nodo omitido no se ejecutó. Compruebe si se eligió otra rama o falta una entrada de unión antes de modificarlo.

**Siga la primera desviación**

Siga la ruta real desde la entrada. Para una condición de importe falsa, revise naranja; para un error, lea el mensaje y revise rojo. El gestor de errores puede funcionar y la ejecución conservar el error original.

**Revise las uniones**

En Wait ALL, compruebe cada origen y resultado conectado. En ANY u OR, busque un origen coincidente. Dos salidas del mismo nodo no representan aprobaciones independientes. Una condición naranja puede ser intencionada.

**Corrija y verifique**

Anote workflow, referencia del documento, fecha, nodo y mensaje exacto. Corrija datos o configuración y pruebe un escenario repetible. Guarde y compruebe la activación. Compare una ejecución nueva con la antigua; los registros anteriores conservan el comportamiento anterior.

</details>
