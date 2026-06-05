---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Panel de Flujos de Trabajo

El Panel de Flujos de Trabajo es su centro principal para gestionar y monitorear todos los flujos de trabajo en DocBits. Acceda a él haciendo clic en el icono de **Flujos de Trabajo** en la barra lateral izquierda.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Panel de Flujos de Trabajo con totales de ejecuciones, tasas de éxito y fallo, el gráfico de ejecuciones y la actividad reciente"><figcaption><p>El Panel de Flujos de Trabajo: totales de ejecuciones, tasas de éxito/fallo y actividad reciente de cada flujo de trabajo.</p></figcaption></figure>

## Pestaña del Panel

La pestaña del Panel proporciona una vista general del rendimiento de los flujos de trabajo para un período de tiempo seleccionado.

### Filtros

- **Fecha de inicio / Fecha de fin** — Seleccione el rango de tiempo para las estadísticas
- **Nombre del Flujo de Trabajo** — Filtre por un flujo de trabajo específico o vea todos
- **Comparar** — Compare dos períodos de tiempo lado a lado
- **Limpiar** — Restablezca todos los filtros

### Tarjetas de Estadísticas

| Métrica | Descripción |
|---|---|
| **Flujos de trabajo ejecutados hoy** | Número total de ejecuciones de flujos de trabajo hoy |
| **Flujos de trabajo creados (período)** | Nuevos flujos de trabajo creados dentro del rango de fechas seleccionado |
| **Total de ejecuciones** | Ejecuciones acumuladas de flujos de trabajo durante el período |
| **Ejecuciones exitosas** | Número de ejecuciones que se completaron sin errores |
| **Tasa de éxito** | Porcentaje de ejecuciones exitosas vs. ejecuciones totales |
| **Tasa de fallo** | Porcentaje de ejecuciones fallidas vs. ejecuciones totales |

{% hint style="warning" %}
Una tasa de fallo alta (mostrada como **CRITICAL** en rojo) indica que los flujos de trabajo están encontrando errores. Investigue los flujos de trabajo fallidos utilizando los registros de ejecución en el [Constructor Avanzado de Flujos de Trabajo](advanced-workflow-builder/).
{% endhint %}

### Gráfico de Ejecuciones de Flujos de Trabajo

El gráfico muestra un desglose mensual de ejecuciones de flujos de trabajo **exitosas** (verde) y **fallidas** (rojo/rosa), ayudándole a identificar tendencias y picos de errores.

### Actividad Reciente

- **Últimas Pruebas de Flujos de Trabajo** — Muestra las ejecuciones de prueba recientes con estado de aprobado/fallido
- **Últimos Flujos de Trabajo** — Muestra los flujos de trabajo creados o modificados recientemente

## Pestaña de Lista de Flujos de Trabajo

La pestaña de Lista de Flujos de Trabajo muestra todos los flujos de trabajo con capacidades de búsqueda, ordenamiento y gestión.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Columnas

| Columna | Descripción |
|---|---|
| **Estado** | Icono de alternancia — haga clic para habilitar/deshabilitar un flujo de trabajo |
| **Nombre** | Nombre del flujo de trabajo (haga clic para abrir en el Constructor de Flujos de Trabajo) |
| **Tipo** | Insignia que muestra `Advanced` para flujos de trabajo visuales |
| **Cuándo...** | Resumen de la condición de activación |
| **Actualizado Por** | Usuario que modificó por última vez el flujo de trabajo |
| **Creado El** | Fecha y hora de creación |
| **Actualizado** | Fecha y hora de la última modificación |
| **Acciones** | Menú contextual (eliminar, duplicar, exportar) |

### Acciones

- **Buscar** — Filtre flujos de trabajo por nombre usando la barra de búsqueda
- **+ AGREGAR FLUJO DE TRABAJO** — Cree un nuevo flujo de trabajo (abre el [Constructor Avanzado de Flujos de Trabajo](advanced-workflow-builder/))
- **PLANTILLAS** — Explore y cargue plantillas de flujos de trabajo guardadas
- **IMPORTAR FLUJO DE TRABAJO** — Importe un flujo de trabajo desde un archivo JSON

## Pestaña de Lista del Gestor de Pruebas

La Lista del Gestor de Pruebas muestra todas las configuraciones y resultados de pruebas de flujos de trabajo. Úsela para configurar escenarios de prueba automatizados para sus flujos de trabajo.

El **Gestor de Pruebas** le permite guardar escenarios de prueba por flujo de trabajo y ejecutarlos juntos, de modo que pueda confirmar que sus flujos de trabajo siguen comportándose correctamente después de los cambios:

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Lista del Gestor de Pruebas de flujos de trabajo con escenarios de prueba y Run All Tests"><figcaption><p>La Test Manager List: cada escenario muestra un resultado de aprobado/fallido; use <strong>Run All Tests</strong> para volver a ejecutarlos todos.</p></figcaption></figure>

## Pestaña de Licencia

La pestaña de Licencia muestra el estado actual de su licencia de DocFlow y las funciones disponibles.

## Pestaña de Card SDK

La pestaña de Card SDK le permite crear y gestionar tarjetas de flujo de trabajo personalizadas (tarjetas de socios) que amplían las capacidades integradas de DocFlow.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### Subir ZIP

Suba una aplicación de socio como un archivo ZIP que contenga:
- `app.json` — Metadatos y configuración de la tarjeta
- `.docflowcompose/flow/` — Archivos de definición de la tarjeta

Tamaño máximo de archivo: **10 MB**. Haga clic en **Upload & Validate** para enviar la tarjeta para revisión.

### Importación desde GitHub

Importe tarjetas de socios directamente desde un repositorio de GitHub en lugar de subir un archivo ZIP.

### Envíos

Vea y gestione todas las tarjetas de socios enviadas:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Columna | Descripción |
|---|---|
| **Card Name** | Nombre de la aplicación y tarjeta del socio |
| **card_type_label** | Tipo de tarjeta (`Action_card` o `Condition_card`) |
| **Version** | Número de versión de la tarjeta |
| **Submitted** | Fecha de envío |
| **Estado** | Estado actual de revisión |
| **Acciones** | Acciones disponibles según el estado |

#### Estados de las Tarjetas

| Estado | Significado | Acciones disponibles |
|---|---|---|
| **Validated** | La tarjeta pasó la validación | Descargar, Aprobar, Rechazar |
| **Approved** | La tarjeta está activa y disponible en los flujos de trabajo | Descargar, Deshabilitar, Revocar |
| **Rejected** | La tarjeta no pasó la revisión | Eliminar |
| **Disabled** | La tarjeta fue desactivada | Eliminar |

### Descargar Plantilla SDK

Haga clic en **Download SDK Template** para obtener una plantilla inicial para crear sus propias tarjetas personalizadas. La plantilla incluye la estructura de archivos requerida y configuraciones de ejemplo.

{% hint style="info" %}
Las tarjetas de socios también se pueden gestionar programáticamente a través de las [herramientas MCP de DocFlow](../../../advanced-functions-and-tools/docflow-mcp/). Use las herramientas MCP de Card SDK para crear, validar, aprobar y probar tarjetas desde su IDE o scripts de automatización.
{% endhint %}
