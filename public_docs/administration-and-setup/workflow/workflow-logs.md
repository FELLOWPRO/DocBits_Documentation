# Registros de flujos de trabajo

Para ver explicaciones narradas de la vista avanzada de registros, consulta [Encontrar la ejecución relevante](advanced-workflow-builder/videos.md#find-the-relevant-execution) y [Seguir nodos y diagnosticar](advanced-workflow-builder/videos.md#trace-nodes-and-diagnose). Ambos capítulos están disponibles en inglés y alemán, con archivos de subtítulos y transcripciones.

## **Resumen**

Los **Registros de flujos de trabajo** permiten a los usuarios analizar qué Workflows se ejecutaron para un documento, comprender los resultados de la ejecución y profundizar en los detalles a nivel de condición para la depuración o la validación.

## **Acceso a los registros de flujos de trabajo**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4" %}

**Vídeo:** Leer los registros de flujos de trabajo · 1:34 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.vtt)

<details>

<summary>Transcripción</summary>

**Abrir los registros de flujos de trabajo** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=0.25)

Cada documento conserva los registros de los Workflows que se ejecutaron sobre él. En el Dashboard del documento, abre las acciones de un documento y elige Workflow Logs.

**Ejecuciones y sus resultados** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=12.15)

Arriba ves cuántas ejecuciones hubo y cuántas terminaron con un error, una condición fallida o un éxito. Debajo se lista cada ejecución con su Workflow, su hora, su duración y su resultado.

**El recorrido de una ejecución** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=25.716)

Arrastra el divisor hacia la izquierda para dar más espacio a los registros. Luego haz clic en una ejecución para ver el recorrido que siguió. Cada tarjeta muestra su resultado: verde para el éxito, naranja para una condición fallida, rojo para un error. Aquí la tarjeta And terminó con una condición fallida, así que la tarjeta Then posterior no se ejecutó.

**Por qué una tarjeta terminó así** · [0:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=45.35)

Selecciona una tarjeta para leer su registro. Indica qué comparó la tarjeta y por qué terminó así. Aquí el documento está listo para la validación, pero la tarjeta espera una segunda aprobación pendiente.

**Un error y su motivo** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=58.283)

Una ejecución que termina con un error muestra en rojo la tarjeta que falló. Aquí la tarjeta And no pudo leer la dirección de entrega del documento. Los datos que faltan son siempre un error, así que la tarjeta Then posterior no se ejecutó.

**Buscar ejecuciones** · [1:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=73.216)

Con muchas ejecuciones, usa la búsqueda para encontrar un Workflow por su nombre y el botón de filtro para acotar la lista por estado o fecha.

**Nota sobre el límite de ejecución** · [1:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-logs/v1/en.mp4#t=83.116)

Arriba aparece una nota cuando un Workflow ha alcanzado su límite de ejecuciones en este documento. El vídeo sobre los límites de ejecución lo explica.

</details>

Para acceder a los registros de flujos de trabajo:

1. Navega hasta el **Dashboard**.
2. Haz clic en el **Actions menu** (icono de tres puntos) junto al documento deseado.
3. Selecciona **Workflow Logs** en el menú.
   * <mark style="color:red;">**Note**</mark>: La función Workflow debe estar habilitada para acceder a esta opción.
4.  Se abre un **side panel** que muestra un resumen de los Workflows ejecutados.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="Dashboard with the workflow logs side panel showing summary counters and a table of executed workflows with result icons" width="563"><figcaption></figcaption></figure></div>

## **Abrir un registro como página propia**

El side panel cubre la lista de documentos. Para un documento cuyo Workflow revises durante un rato, abre el mismo registro como página completa: selecciona el icono de ventana nueva en la cabecera del panel. La página tiene la dirección `/workflows/logs/<document id>`, así que puedes mantenerla abierta en una segunda ventana del navegador o enviar la dirección a un compañero que tenga acceso al documento.

La página muestra los mismos contadores de resumen, la misma tabla de Workflows ejecutados y la misma vista de detalle que el panel.

## **Cambiar a otro documento**

En la página completa, un campo de búsqueda encima de la lista encuentra un documento por su nombre o por su ID. Los resultados muestran la fecha de carga, el asignado y el estado de cada documento, para que puedas distinguir documentos con nombres similares. Al seleccionar un resultado se carga su registro de Workflow y se pone el documento en la dirección. La búsqueda cubre los documentos de tu organización que tus permisos te permiten ver; cuando no hay coincidencias, DocBits lo indica debajo del campo en lugar de mostrar una lista vacía.

## **Componentes del panel de Workflow Logs**

#### **1. Contadores de resumen del Workflow**

Ubicados en la parte superior del panel de registros:

* **Azul**: Número total de Workflows ejecutados.
* **Rojo**: Workflows que terminaron con **errores**.
* **Amarillo**: Workflows que **no se completaron** debido a discrepancias en las condiciones.
* **Verde**: Workflows **ejecutados** correctamente.

#### **2. Tabla de ejecución de Workflows**

Cada fila de la tabla representa una ejecución de Workflow e incluye:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (en segundos)
* **Result Icon**:
  * Marca de verificación verde: el Workflow se ejecutó correctamente.
  * Cruz roja: el Workflow se ejecutó con un error.
  * Guion naranja: la ejecución se detuvo porque no se cumplió una condición

Al hacer clic en la **flecha** a la izquierda de cada fila se expande la **vista de detalle del Workflow**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Expanded workflow log row showing When and And condition cards with green checks and a grayed card that was not met, plus card logs" width="563"><figcaption></figcaption></figure></div>

### **Vista de detalle del Workflow**

Al hacer clic en una fila de Workflow concreta se abre su **registro detallado de ejecución**, que muestra:

#### **Evaluación de condiciones**

* Bloque **When...**: condición inicial.
* Bloque(s) **And...**: condiciones adicionales.
* Bloque(s) **Then...**: acciones que se realizan cuando se cumplen todas las condiciones.

Cada línea de condición muestra:

* **Marca de verificación verde**: la condición se cumplió.
* **Guion naranja**: la condición no se cumplió.
* **Cruz roja**: la condición falló **debido a un error**

### **Nota importante sobre el comportamiento**

Si una condición de un Workflow **no se cumple**, el sistema **deja de evaluar las tarjetas de Workflow siguientes** dentro de ese Workflow. Este comportamiento evita un procesamiento innecesario\
Como indicador visual, la tarjeta que **no cumplió su condición** se muestra en **gris**, y todas las **tarjetas posteriores** del mismo Workflow también aparecerán en **gris**, lo que indica que **no se ejecutaron**.
