---
description: "Cinco capítulos en español sobre Advanced Workflows y sus registros, con subtítulos y transcripciones."
---

# Vídeos de Advanced Workflow

Aprenda a crear, probar y diagnosticar un workflow avanzado. Los cinco capítulos tienen narración en español.

Los tres primeros capítulos muestran la interfaz real de DocBits. Los dos capítulos de registros utilizan gráficos explicativos identificados como ilustraciones. Las capturas muestran borradores de demostración sin guardar.

Cada vídeo incluye subtítulos WebVTT y una transcripción desplegable.

1. [Constructor y lienzo](#builder-and-canvas) · 1:56
2. [Nodos y rutas](#nodes-and-routes) · 2:00
3. [Variables, pruebas y activación](#variables-tests-and-activation) · 1:53
4. [Encontrar la ejecución relevante](#find-the-relevant-execution) · 1:56
5. [Seguir nodos y diagnosticar](#trace-nodes-and-diagnose) · 1:51

## Constructor y lienzo {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.vtt) · 1:56

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/es.mp4" %}

[Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/es.mp4) · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/es.vtt) · 1:56

<details>
<summary>Transcripción</summary>

**Abra los registros del documento**

En el panel de documentos, seleccione Workflow Logs en Acciones. El acceso a workflows debe estar habilitado. Estos registros pertenecen al documento seleccionado. Las pruebas del diseñador y los registros de eventos o actividad de la organización son independientes.

**Interprete los contadores**

Azul cuenta ejecuciones del resultado actual; rojo, errores; amarillo, condiciones falsas; verde, éxitos. Los contadores describen ejecuciones, no definiciones de workflow ni nodos. Los filtros pueden cambiar estas cifras.

**Elija la ejecución exacta**

Cada fila muestra nombre del workflow, fecha de creación, duración en segundos y resultado. Un workflow puede ejecutarse varias veces para el mismo documento. Compare las fechas. Una ejecución breve puede mostrar cero coma cero cero segundos por redondeo.

**Limite los resultados**

Use Buscar para encontrar un workflow. El icono de ajustes abre dirección y criterio de ordenación, estado y fechas inicial y final. Ordene por nombre o creación. Introduzca fechas como año, mes, día y pulse Aplicar.

**Revise filtros y páginas**

Use la paginación para resultados antiguos. Borrar filtros recarga la lista sin selecciones. Vacíe Buscar por separado. Si no hay resultados, revise documento, fechas y estado. Una lista vacía no demuestra un error de ejecución.

**Estados especiales**

Un aviso y un icono de bloqueo indican el límite de ejecuciones del documento. Investigue disparadores repetidos antes de cambiar límites. La descarga de vídeo de DocOperator aparece solo si existe una grabación; corresponde a esa ejecución.

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
