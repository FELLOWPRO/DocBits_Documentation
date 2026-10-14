# Panel de Análisis

## Descripción general

El **Panel de Análisis** ofrece visibilidad completa del rendimiento del procesamiento de sus documentos. Realiza un seguimiento del tiempo que pasan los documentos en cada etapa de su recorrido — desde la importación hasta la exportación — y le ayuda a identificar cuellos de botella, comparar el rendimiento entre organizaciones, tipos de documentos y proveedores, y comparar sus resultados con el **Promedio Mundial de DocBits**.

Cada documento atraviesa distintas etapas:

**Nuevo** (importado) → **En ejecución** (procesando) → **Listo para la validación** (pendiente de revisión por el usuario) → **Pendiente de aprobación** (pendiente de aprobación) → **Exportar** (completado y exportado)

El tiempo transcurre en cada etapa — el Panel de Análisis le indica exactamente **cuánto** y **dónde** debe centrar sus mejoras.

### Dos tipos de cuellos de botella

El panel le ayuda a distinguir entre:

* **Cuellos de botella del sistema** — Cuánto tiempo está DocBits ocupado con el procesamiento automático (OCR y extracción de texto, clasificación de documentos, extracción de campos, validación automática). Optimizables mediante configuración y recursos del sistema.
* **Cuellos de botella del usuario** — Tiempo de espera para la validación y aprobación manual (tiempo de espera en cola, corrección manual de datos, revisión y validación, flujos de aprobación). Optimizables mediante el flujo de trabajo y la asignación de recursos.

## Cómo activarlo

El Panel de Análisis se controla mediante un ajuste del módulo. Una vez habilitado, aparece una entrada **Panel de Análisis** en la barra lateral izquierda.

1. Vaya a **Ajustes → Procesamiento de Documentos → Módulo → Panel y Análisis**.
2. Habilite la opción **Panel de Análisis**.

<mark style="color:red;">**Nota**</mark>: El Panel de Análisis requiere una **Suscripción al Panel de IA**.

<mark style="color:red;">**Nota**</mark>: El acceso al Panel de Análisis está limitado a usuarios con derechos de **administrador**.

## Tipos de flujo

Elija la perspectiva adecuada para su análisis. Cada tipo de flujo le ofrece una perspectiva diferente sobre los mismos datos.

| Tipo de flujo | Propósito | Pregunta clave |
| --- | --- | --- |
| **Estado** | Realizar el seguimiento del ciclo de vida del documento, desde la importación hasta la exportación | *"¿Cuál es el tiempo total de mis documentos, desde la importación hasta la exportación?"* |
| **Procesamiento** | Análisis técnico del rendimiento del módulo | *"¿Qué pasos de procesamiento son cuellos de botella?"* |
| **Interacción del usuario** | Puntos de contacto humanos y tiempos de espera | *"¿Cuánto tiempo esperan los documentos a los usuarios?"* |

Utilice el conmutador **Tipo de flujo** en la parte superior del panel para alternar entre perspectivas.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_flow_types.png)

### Flujo de Estado

Realiza el seguimiento del recorrido del documento desde **Nuevo** hasta **Exportado** — útil para el análisis del ciclo de vida de extremo a extremo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_status_flow.png)

### Flujo de Procesamiento

Analiza el rendimiento en todos los **módulos técnicos de procesamiento** (OCR, clasificación, extracción, validación) — útil para identificar cuellos de botella del lado del sistema.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_processing_flow.png)

### Flujo de Interacción del Usuario

Se centra en los **puntos de contacto humanos** — tiempo de espera en cola, validación manual, revisión y aprobación — útil para identificar cuellos de botella del flujo de trabajo y de personal.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_user_interaction_flow.png)

## Opciones de filtro

El panel admite un potente filtrado multidimensional. Todos los gráficos, tarjetas y tablas se actualizan en tiempo real en función de los filtros activos.

### Buscar

Localice cualquier documento al instante por **nombre** o **ID único**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_search.png)

### Pasos de flujo

Seleccione pasos específicos para centrar su análisis. Activar/desactivar pasos también recalcula las métricas de tiempo en los demás componentes del panel.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_flow_steps.png)

### Suborganización, Tipo de Documento, Proveedor, Grupo

Compare el rendimiento entre:

* **Suborganizaciones** — diferentes unidades de negocio o inquilinos
* **Tipos de Documento** — facturas, órdenes de compra, albaranes de entrega, etc.
* **Proveedores** — para identificar qué proveedores provocan los tiempos de procesamiento más largos
* **Grupos** — para comparar el rendimiento entre los grupos de usuarios asignados (disponible para los tipos de flujo **Estado** e **Interacción del usuario**)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_dimensions.png)

<mark style="color:red;">**Nota**</mark>: El filtro **Grupo** solo se aplica a los documentos que están **asignados directamente a un grupo**. Los documentos asignados a un usuario individual — incluso si ese usuario es miembro de un grupo — **no** se incluyen en los resultados del filtro de grupo.

### Solo documentos exportados

Activado de forma predeterminada — solo los documentos que han completado la exportación se tienen en cuenta en las métricas del panel.

<mark style="color:red;">**Nota**</mark>: Desactivar esta opción puede dar lugar a valores promedio inexactos, ya que también se incluyen en los cálculos los documentos que aún no se han completado.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_only_exported_toggle.png)

### Intervalo de tiempo

Analice cualquier período desde **7 días** hasta un **año completo**, o establezca un **intervalo personalizado** mediante el selector de fechas.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_time_range.png)

## Tarjetas de Pasos de flujo

Cada tarjeta representa un paso del flujo basado en el **Tipo de flujo** seleccionado. Las tarjetas se adaptan a su selección — mostrando las etapas del ciclo de vida para *Estado*, los módulos de procesamiento para *Procesamiento*, o los puntos de contacto del usuario para *Interacción del usuario*.

Cada tarjeta muestra:

* Tiempos **Mínimo, Promedio, Máximo** para el paso
* Una comparación entre **su Tiempo Promedio** y el **Promedio Mundial de DocBits** (cuando el conmutador de comparación está activado)
* Un círculo de selección para **incluir o excluir** el paso de los cálculos de tiempo agregado utilizados por el Gráfico de Tiempo Promedio, el Gráfico de Tendencia Temporal y la Tabla de Datos

Un conmutador **Seleccionar todo** en el encabezado le permite incluir o excluir cada paso a la vez.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_flow_steps_card.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_step_toggle.png)

### Comparar con el Promedio Mundial

El conmutador **Comparar con el Promedio Mundial** controla si el Promedio Mundial de DocBits se muestra en las tarjetas y en el gráfico. Cuando está activado, el tiempo promedio en cada tarjeta se codifica por color:

* **Verde** — su Tiempo Promedio está en o por debajo del Promedio Mundial
* **Naranja** — su Tiempo Promedio está hasta un **+25%** por encima del Promedio Mundial
* **Rojo** — su Tiempo Promedio está un **+25%** o más por encima del Promedio Mundial

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_global_average_comparison.png)

## Gráfico de Tiempo Promedio

El Gráfico de Tiempo Promedio visualiza cómo se distribuye el tiempo de procesamiento para los pasos de flujo seleccionados. Utilice el selector **Agrupar por** para comparar entre diferentes dimensiones:

* **Pasos de flujo** — ver qué pasos consumen más tiempo
* **Suborganización** — identificar variaciones entre unidades de negocio
* **Tipo de Documento** — comparar los tiempos de procesamiento entre tipos de documentos
* **Proveedor** — descubrir qué proveedores tienen los tiempos de procesamiento más largos
* **Grupo** — comparar entre los grupos de usuarios asignados (solo para los tipos de flujo Estado e Interacción del usuario)

Cuando **Comparar con el Promedio Mundial** está activado, el gráfico también muestra el Promedio Mundial de DocBits para realizar la comparación.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_average_time_chart.png)

## Documentos principales

La tarjeta **Documentos principales** enumera los documentos individuales que coinciden con el conjunto de filtros activos, clasificados por tiempo total empleado.

* Conmutador de **orden de clasificación** — alterna entre **descendente** (más lento primero) y **ascendente** (más rápido primero).
* Desplegable de **tamaño de página** y paginación — recorra el conjunto de resultados.
* **Ocultar / mostrar** un documento mediante el icono del ojo junto a él — los documentos ocultos se excluyen de todos los cálculos de tiempo del panel.
* **Ocultar / mostrar todos** los documentos del filtro mediante el icono del ojo del encabezado.
* **Haga clic en un documento** (nombre de archivo o barra de progreso) para copiar su ID de Documento al portapapeles.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_top_documents.png)

## Gráfico de Tendencia Temporal

Realice un seguimiento de las tendencias de rendimiento a lo largo del tiempo y detecte anomalías. El Gráfico de Tendencia Temporal muestra el **Tiempo Promedio** de los pasos de flujo seleccionados actualmente y se puede agrupar por:

* **Pasos de flujo** — una línea por cada paso seleccionado
* **Suborganización**
* **Tipo de Documento**
* **Proveedor**
* **Grupo** (disponible para los tipos de flujo **Estado** e **Interacción del usuario**)

Esto facilita la detección de un aumento repentino para un proveedor específico, o un incremento gradual para un tipo de documento específico, antes de que se convierta en un problema crítico.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_time_trend.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_time_trend_grouped.png)

## Tabla de Datos

La Tabla de Datos proporciona acceso completo a todos los datos de fila subyacentes del conjunto de filtros activos.

* **Arrastre columnas al panel de Columnas ocultas** (a la izquierda de la tabla) para eliminarlas de la vista. Las columnas ocultas se utilizan para la agregación — los tiempos **Mínimo / Máximo / Promedio** se recalculan dinámicamente en función de las columnas visibles. Arrastre un chip de vuelta a la tabla (o haga clic en el icono **+**) para restaurar la columna.
* **Clasifique** haciendo clic en los encabezados de columna y **reordene** las columnas arrastrándolas y soltándolas.
* **Descargar CSV** mediante el botón del encabezado de la tarjeta — solo se exportan las columnas visibles actualmente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table_hide_columns.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table_export.png)
