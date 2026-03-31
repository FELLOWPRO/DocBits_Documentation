# Notas de versión

## **Lanzamiento Spring Spark 13 de mayo de 2026**

Disponibilidad en Sandbox: 27–29 de abril de 2026

### Mejoras de DocBits:

*   **Advanced Workflow Designer:**\
    DocBits presenta un Advanced Workflow Designer completamente nuevo — un constructor de automatización visual basado en nodos que pone la orquestación completa de flujos de trabajo al alcance de su mano. Usando un lienzo intuitivo de arrastrar y soltar, los administradores pueden conectar tarjetas de flujo de trabajo de DocBits en pipelines de procesamiento complejos y de múltiples pasos. Cada nodo en el lienzo representa una acción o punto de decisión, y las conexiones entre nodos definen el flujo de documentos a través del pipeline. El diseñador admite pasos de espera para introducir retrasos temporizados, rutas paralelas donde todas o algunas ramas deben completarse antes de continuar, y la capacidad de encadenar cualquier combinación de tarjetas integradas o creadas por socios. Los flujos de trabajo pueden guardarse como plantillas reutilizables, importarse y exportarse entre entornos, y probarse directamente desde el diseñador antes de ponerse en producción. El editor cuenta con un lienzo con ajuste a cuadrícula y navegación con mini-mapa para flujos de trabajo grandes, atajos de teclado para copiar y pegar, validación en tiempo real con resaltado de errores durante la construcción, y protección contra edición concurrente para evitar la sobrescritura de cambios por otros usuarios. Los registros de ejecución detallados proporcionan monitoreo por nodo, permitiendo a los administradores rastrear exactamente cómo se ejecutó cada paso en un flujo de trabajo y dónde ocurrieron los problemas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_advanced_workflow_designer.png)

*   **Mejoras del Workflow Designer:**\
    El diseñador de flujos de trabajo existente se ha mejorado con lógica de ramificación if/else, permitiendo flujos de trabajo basados en decisiones más sofisticados. Se han añadido varias nuevas tarjetas de condición, ampliando aún más el rango de lógica de automatización disponible. Un nuevo Workflow Test Manager permite a los administradores crear y ejecutar pruebas automatizadas para flujos de trabajo individual o colectivamente, asegurando que los cambios se comporten como se espera antes de la implementación. La sección de Workflow ahora también incluye un panel de KPIs con métricas clave sobre el rendimiento de ejecución de flujos de trabajo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_workflow_branching.png)

*   **DocNet AI Agents:**\
    DocBits ahora incluye DocNet AI Agents — agentes inteligentes y autónomos que se ejecutan en segundo plano para manejar tareas de procesamiento de documentos como la coincidencia de órdenes de compra y la validación de facturas. Los agentes operan de forma independiente, trabajando en las tareas asignadas y escalando a los usuarios solo cuando se necesita juicio humano. Cuando un agente encuentra una excepción o requiere confirmación, crea una solicitud de aprobación que aparece directamente en la bandeja de entrada del usuario, asegurando que nada se pierda sin requerir supervisión constante. Los agentes pueden coordinarse entre sí, delegando subtareas y organizando el trabajo en misiones y proyectos para procesos complejos de múltiples pasos. Un panel de agentes dedicado proporciona visibilidad completa de la actividad de los agentes, métricas de rendimiento y registros de auditoría, para que los administradores puedan monitorear qué están haciendo los agentes y con qué eficiencia trabajan. Las notificaciones en tiempo real mantienen informados a los usuarios cuando los agentes completan tareas o marcan elementos para revisión.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_docnet_ai_agents.png)

*   **Partner Card SDK:**\
    Un nuevo Partner Card SDK permite a desarrolladores externos y socios crear tarjetas de flujo de trabajo personalizadas para DocBits. Los socios pueden cargar paquetes de tarjetas para validación y revisión, importar tarjetas desde repositorios de GitHub y gestionar envíos a través de una página dedicada de configuración del Card SDK. Un sistema de revisión impulsado por IA evalúa automáticamente las tarjetas enviadas en cuanto a calidad y cumplimiento. El SDK incluye descargas basadas en ejemplos con diálogos de selección de tarjetas, validación de comportamiento en un entorno sandbox y documentación completa para comenzar. El Card SDK está protegido por verificaciones de licencia y ahora es visible para todos los usuarios, no solo para administradores.

*   **Full-Text Search / DocSearch:**\
    Se ha añadido una nueva capacidad de búsqueda de texto completo a DocBits, impulsada por búsqueda vectorial basada en IA. Los usuarios pueden buscar en todos los documentos indexados con filtrado de proveedores en tiempo real y una función "Find Similar" para localizar documentos que se asemejen a uno seleccionado. Una página de configuración dedicada permite a los administradores configurar la indexación de datos de IA, las preferencias de almacenamiento vectorial y monitorear el progreso de indexación en tiempo real. El acceso a DocSearch se gestiona a través de planes de suscripción.

*   **Expansión de formatos de E-Invoice:**\
    DocBits ha expandido significativamente su soporte de formatos de factura electrónica con más de 80 nuevos tipos globales de e-invoice y más de 40 nuevos formatos. Los formatos recién soportados incluyen Taiwan EGUI, Thailand E-Tax, India GST Credit Note, SPS Commerce RSX 7.7.4, XRechnung 3.0.2, ZUGFeRD 2.2 y 2.3.2, variantes Factur-X, Uruguay CFE, Ecuador SRI Retención, SVEFAKTURA 1.0, EHF 3.0, OIOUBL, Finvoice y Asia-Pacific PINT Credit Notes, entre otros. DocBits ahora logra una cobertura del 100% en clasificación y extracción para todos los formatos de documentos electrónicos soportados.

*   **Login Analytics:**\
    Un nuevo panel de Login Analytics da a los administradores visibilidad completa de la actividad de inicio de sesión en toda la organización. El panel incluye gráficos comparativos que muestran tendencias de inicio de sesión a lo largo del tiempo, vistas de agregación diaria y semanal, y geolocalización basada en GeoLite2 para ver de dónde provienen los inicios de sesión. Esto proporciona una forma rápida de detectar patrones de inicio de sesión inusuales y monitorear la seguridad de las cuentas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_login_analytics.png)

*   **Analytics Dashboard:**\
    Se ha introducido un módulo completo de análisis de procesamiento de documentos con múltiples vistas de panel incluyendo Executive Overview, API Metrics, Quality Metrics y Processing Performance. Document Flow Analytics ofrece métricas a nivel de organización sobre tiempos de procesamiento de documentos y transiciones de estado. Un sistema completo de Activity Log y Event Log permite a los administradores explorar, buscar, filtrar y exportar datos de eventos con visualizaciones de gráficos y resaltado de sintaxis JSON. Una función de Audit Trail proporciona seguimiento detallado del historial de cambios con detalles emergentes para cada modificación.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_analytics_dashboard.png)

*   **Mejoras en el control de acceso:**\
    El control de acceso se ha aplicado en toda la aplicación, cubriendo la pantalla de validación de campos, tablas extraídas por IA y múltiples otras vistas. Los administradores ahora tienen la opción de desactivar el control de acceso globalmente cuando sea necesario. El diseño del control de acceso ha sido renovado para una experiencia más consistente e intuitiva en todas las pantallas.

*   **Mejoras del Layout Builder:**\
    El Layout Builder ahora admite campos ocultos y de solo lectura con indicadores visuales, facilitando a los administradores comprender qué campos son visibles y editables para los usuarios. Un divisor redimensionable entre paneles mejora la flexibilidad del espacio de trabajo, y las configuraciones de longitud de campo proporcionan un control más preciso sobre los campos de entrada de datos.

*   **Historial de exportación en acciones del Dashboard:**\
    Los usuarios ahora pueden acceder al historial de exportación de un documento directamente desde el menú de acciones del panel, haciendo más rápido revisar intentos de exportación anteriores sin salir de la vista principal.

*   **Mejoras de exportación:**\
    Las configuraciones de exportación ahora admiten ordenamiento de ejecución, permitiendo a los administradores definir la secuencia en que se procesan múltiples métodos de exportación. Un nuevo botón de re-exportación en las pantallas de error permite a los usuarios reintentar desde el paso fallido en lugar de reiniciar todo el proceso. DocBits ahora también admite el objetivo de exportación API GLS840MI, con una interfaz actualizada para gestionar múltiples configuraciones de exportación activas por tipo de documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_export_improvements.png)

*   **Script Versioning & AI Chat:**\
    Los scripts de documentos ahora admiten historial de versiones completo, permitiendo a los administradores rastrear cambios, comparar versiones y restaurar versiones anteriores de scripts. Los scripts predeterminados están protegidos contra ediciones accidentales, y los nombres de scripts pueden editarse en línea con navegación breadcrumb. Los campos ahora pueden establecerse como de solo lectura programáticamente a través de la nueva función set\_is\_readonly. Un nuevo asistente de chat impulsado por IA ayuda con el desarrollo de scripts, proporcionando respuestas de streaming en tiempo real.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_script_versioning.png)

*   **API Key Management:**\
    Una nueva página de API Key Management en la configuración de integración permite a los administradores crear, ver y gestionar múltiples claves API con caché respaldado por Redis para rendimiento.

*   **Idea Board:**\
    Una nueva función Idea Board permite a los usuarios enviar, discutir y votar sobre ideas de funciones y sugerencias. El tablero incluye un editor de texto enriquecido con soporte de carga de imágenes, comentarios y funcionalidad de votación.

*   **Estadísticas de proveedores:**\
    Nuevas vistas de estadísticas de proveedores proporcionan información sobre métricas de procesamiento de documentos relacionadas con proveedores.

*   **Expansión de idiomas:**\
    DocBits ahora admite 22 idiomas, expandido desde la selección anterior. El selector de idiomas se ha actualizado con un diseño de cuadrícula de 4 columnas, y los usuarios ahora pueden establecer su idioma preferido directamente en su configuración de usuario.

*   **Rediseño del plan de suscripción:**\
    El selector de plan de suscripción se ha rediseñado con una visualización mejorada de información de tokens y una nueva fila de uso de DocNet en la tabla de suscripción.

*   **Dual Monitor Mode:**\
    El Dual Monitor Mode se ha movido a una configuración global de usuario, haciéndolo accesible y persistente entre sesiones para usuarios que trabajan con múltiples pantallas.

*   **Búsqueda difusa para caracteres alemanes:**\
    La funcionalidad de búsqueda ahora admite correctamente los caracteres especiales alemanes (diéresis), asegurando que las búsquedas de palabras como "Rechnungsnummer" también coincidan con representaciones alternativas de caracteres.

*   **Mejoras en notificaciones por correo electrónico:**\
    La sustitución de parámetros en plantillas de correo electrónico se ha mejorado con mejor validación de destinatarios y manejo de preferencias de usuario.

*   **Seguimiento del uso de créditos:**\
    Las organizaciones ahora pueden ver y rastrear su uso de créditos de IA a lo largo del tiempo con opciones de filtrado, proporcionando mejor visibilidad de los patrones de consumo.

### Mejoras generales:

*   El área de Settings se ha rediseñado con una barra lateral plegable, subcategorías organizadas y navegación basada en anclas para un acceso más rápido. Un panel de ayuda contextual proporciona orientación en línea, y las insignias de seguimiento de estado muestran la completitud de la configuración de un vistazo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_settings_redesign.png)

* Los documentos con códigos de barras ahora se dividen de manera más confiable, con mejor manejo de casos extremos y recuperación de errores.
* La coincidencia de PO ahora detecta y convierte automáticamente los precios unitarios al dividir líneas coincidentes, reduciendo las correcciones manuales.
* Los documentos ya no se quedan atascados durante la extracción — un nuevo sistema de seguimiento de estado asegura que cada documento avance a través del pipeline.
* Cuando ocurren errores de extracción, DocBits ahora proporciona mensajes de error más claros con detalles paso a paso para ayudar a solucionar el problema más rápido.
* El rendimiento general de la aplicación se ha mejorado con tiempos de respuesta más rápidos en todas las pantallas.
* Las reglas de Auto Accounting ahora admiten filtrado basado en números para condiciones de coincidencia más precisas.

### Correcciones de errores:

* Se corrigió un problema donde el nombre personalizado del panel no estaba alineado con el icono del panel.
* Se corrigió un problema donde el panel mostraba columnas que no estaban incluidas en la configuración de columnas visibles.
* Se corrigió un problema donde el nombre de la pestaña seleccionada no se mostraba en el panel.
* Se corrigió un problema donde la ventana emergente "Nueva versión disponible" aparecía en cada cambio de suborganización.
* Se corrigió un problema donde la configuración de documentos por página no se preservaba después de actualizar la página.
* Se corrigió un problema donde el conteo de documentos del panel no se actualizaba correctamente.
* Se corrigió un problema donde los usuarios recibían incorrectamente el mensaje de error "El panel ya existe".
* Se corrigió un problema donde la ventana emergente de confirmación de eliminación masiva no se mostraba.
* Se corrigieron múltiples problemas con la visualización y el comportamiento de guardado de paneles compartidos.
* Se corrigió un problema donde las tablas de documentos no se mostraban en la pantalla de validación.
* Se corrigió un problema donde se mostraba un mensaje de error incorrecto para archivos PDF no válidos.
* Se corrigió un problema donde el redimensionador de columnas aparecía detrás de los botones de acción de fila.
* Se corrigió un problema donde se extraían valores incorrectos para monto neto, monto de impuesto y tasa de impuesto.
* Se corrigió un problema donde las configuraciones de exportación no podían crearse sin especificar un tipo de documento cuando estaba marcado como opcional.
* Se corrigió un problema donde ocurría un error de configuración duplicada al agregar nuevas configuraciones de exportación.
* Se corrigió un problema donde ocurrían errores al crear múltiples configuraciones de exportación.
* Se corrigió un problema donde el título de configuración se borraba después de seleccionar Watchdog como tipo de exportación.
* Se corrigió un error interno del servidor al crear configuraciones de exportación de Infor.
* Se corrigió un problema que impedía el reinicio múltiple de documentos exportados.
* Se corrigió un problema donde algunas páginas de configuración no se podían encontrar.
* Se corrigió un problema donde el enlace de descarga de Watchdog devolvía un error.
* Se corrigió un problema donde el botón de crear List of Values no desencadenaba ninguna acción.
* Se corrigió un problema donde las descripciones de grupo no se mostraban.
* Se corrigió un problema donde el estado de validación de contraseña persistía después de cancelar la edición de un usuario.
* Se corrigió un problema donde los documentos en estado "Pending Watcher Export" no eran clicables.
* Se corrigió un problema donde se podían crear configuraciones de búsqueda duplicadas.
* Se corrigió un problema donde la ordenación de usuarios no funcionaba correctamente.
* Se corrigió un problema de visualización donde todo el texto de la aplicación aparecía en azul.
* Se corrigió un problema donde la visualización del formato de idioma era inconsistente.
* Se corrigió un problema donde la configuración de idioma aparecía vacía cuando no se seleccionaba ninguna preferencia.
* Se corrigió un problema donde se ignoraba el uso de mayúsculas/minúsculas del nombre de la empresa.
* Se corrigió un problema donde la búsqueda no funcionaba para grupos y permisos.
* Se corrigió un problema donde la acción de eliminar usuario no eliminaba correctamente al usuario.
* Se corrigió un problema donde los iconos de flujo de documentos no eran visibles.
* Se corrigió un error interno del servidor al guardar plantillas de correo electrónico.
* Se corrigió un problema donde se insertaban variables duplicadas en los asuntos de plantillas de correo electrónico.
* Se corrigió un error al guardar los detalles de la cuenta de correo electrónico entrante.
* Se corrigió un problema donde los documentos se quedaban atascados en estado "nuevo" después de la carga.
* Se corrigió un problema donde las columnas de tabla no estaban disponibles después de desactivarlas y reactivarlas.
* Se corrigió un problema donde la creación de árboles de decisión fallaba para tipos de documentos personalizados.
* Se corrigió un problema donde la extracción de tablas no devolvía resultados.
* Se corrigió un problema donde el tipo de documento CREDIT\_NOTE no se reconocía correctamente.
* Se corrigió un problema donde usuarios sin derechos de administrador podían ver todas las tareas creadas.
* Se corrigió un problema donde la ventana emergente de suborganización no se cerraba después de cargar archivos con arrastrar y soltar.
* Se corrigió un problema donde los filtros de período de tiempo no se aplicaban correctamente.
* Se corrigió un problema con la conversión de fecha y hora al formato estadounidense.
* Se corrigió un problema donde los flujos de trabajo se activaban en el orden incorrecto — la ejecución de flujos de trabajo ahora utiliza bloqueo de documentos y prioridades de cola adecuados.

## **Release HotFix 2 31 de marzo de 2026**

### Mejoras de DocBits:

* **Procesamiento híbrido de PDF — Extracción XML controlada por el usuario:**\
  Cuando un PDF contiene datos XML incrustados, los usuarios ahora pueden elegir si DocBits debe usar el XML incrustado para la extracción o procesar el documento como un PDF estándar. Esto otorga a las organizaciones control total sobre cómo se manejan los documentos híbridos, asegurando que se aplique el método de extracción más adecuado para su flujo de trabajo.

* **AP Assignment Code en la pantalla de Approval:**\
  La página de AP Manager Approval ahora incluye un campo de AP Assignment Code, integrado con Infor M3 CRS620. Esto permite a los aprobadores revisar y confirmar los códigos de asignación directamente durante el proceso de aprobación sin cambiar a sistemas externos.

* **Coincidencia del total de PO con el total del documento:**\
  DocBits ahora admite la comparación del total de la orden de compra con el total del documento, proporcionando una capa de validación adicional durante el PO Matching para detectar discrepancias más temprano en el proceso.

* **Actualización de número de artículo del proveedor y VPE:**\
  DocBits ahora admite la actualización de los campos de número de artículo del proveedor y VPE (Verpackungseinheit / unidad de embalaje) durante el procesamiento de documentos, con los valores sincronizados de vuelta a M3 en la exportación.

* **Clasificación mejorada del layout de documentos:**\
  El ID de layout del documento (tfidf_id) ahora se genera basándose únicamente en el texto del encabezado, excluyendo el texto del pie de página. Esto mejora la precisión de la clasificación al evitar que el contenido del pie de página influya en la detección del tipo de documento.

* **Botón Export & Next:**\
  Se ha añadido un nuevo botón "Export & Next", que permite a los usuarios exportar el documento actual y pasar inmediatamente al siguiente en la cola, agilizando el flujo de trabajo de revisión y exportación.

* **Proceso de aprobación para facturas de costos:**\
  El proceso de aprobación para facturas de costos se ha mejorado con una lógica de enrutamiento y validación optimizada.

### Corrección de errores:

* Se corrigió un problema en el que la exportación Infor SFTP fallaba con un error debido a un comando de biblioteca incorrecto.
* Se corrigió un problema en el que las casillas de verificación booleanas no podían mostrarse en la pantalla de aprobación.
* Se corrigió un problema en el que se enviaban mensajes UNMU aunque no hubiera discrepancias en la unidad de compra.
* Se corrigió un problema en el que el impuesto sobre las ventas se clasificaba incorrectamente como cargo en la pantalla de PO Matching, lo que resultaba en un importe pendiente negativo.
* Se corrigió un problema en el que la exportación fallaba cuando la unidad de compra no estaba establecida en la confirmación de pedido pero estaba presente en la orden de compra.
* Se corrigió un problema en el que faltaba el cuerpo del correo electrónico en varios documentos.
* Se corrigió un problema en el que el número de artículo del proveedor no era visible en la pantalla de aprobación y las actualizaciones no se enviaban a M3.
* Se corrigió un problema en el que la exportación de proveedores a Infor devolvía un error.
* Se corrigió un problema en el que PO Matching producía errores durante el procesamiento.
* Se corrigió un problema en el que la función `findAll` no funcionaba correctamente en los scripts de documentos.
* Se corrigió un problema en el que la columna "Updated By" de Watchdog mostraba incorrectamente el usuario Fellow Admin en lugar del usuario real.
* Se corrigió un problema en el que BOD-Mapping no podía configurarse en la interfaz de Watchdog.
* Se corrigió un problema en el que los cargos se mostraban incorrectamente como importes pendientes en lugar de mostrarse como cargos.
* Se corrigió un problema en el que el emparejamiento automático no funcionaba para facturas multilínea a pesar de tener una configuración de emparejamiento establecida.
* Se corrigió un problema en el que un guion ("-") en el número de artículo se consideraba durante el PO Matching para la orden de compra pero se ignoraba en la factura, causando una discrepancia falsa.
* Se corrigió un problema en el que tanto archivos PDF como XML se cargaban en la carpeta de exportación incluso cuando el interruptor "Export PDF" estaba desactivado.
* Se corrigió un problema en el que un estado faltante en la tarjeta de workflow impedía que los documentos progresaran a través del flujo de trabajo.
* Se corrigió un problema en el que la calidad del documento se degradaba significativamente después de la importación.
* Se corrigió un problema en el que la pantalla de PO Match generaba un error ("Cannot read properties of null").
* Se corrigió un problema en el que la lista de valores predeterminada no podía editarse.
* Se corrigió un problema en el que el workflow no podía leer el estado del campo correctamente, causando un enrutamiento incorrecto.
* Se corrigió un problema en el que las importaciones de correo electrónico entrante fallaban con un error.
* Se corrigió un problema en el que las líneas faltantes no llegaban correctamente a M3 durante la exportación.
* Se corrigió un problema en el que las facturas codificadas y aprobadas ocasionalmente no se actualizaban al estado "aprobado" en M3 a través de la API APS110.
* Se corrigió un problema con la configuración de Multi Banking que no funcionaba correctamente.
* Se corrigieron múltiples problemas con la visualización y el comportamiento de guardado de dashboards compartidos.
* Se corrigió un problema en el que el campo de número de artículo del proveedor estaba limitado a 30 caracteres, impidiendo el almacenamiento de valores más largos.
* Se corrigió un problema en el que los valores de precio unitario y precio unitario por unidad causaban un error durante la exportación.

### Cambios de configuración:

* Se actualizaron las plantillas de correo electrónico para eliminar el botón "Go to Task".
* Se ajustaron los scripts y la configuración de campos obligatorios en los elementos de costos.

## **Release HotFix 1 16 de marzo de 2026**

### Mejoras de DocBits:

* **Historial de documentos en la exportación SFTP:**\
  DocBits ahora permite incluir el historial completo del documento como parte del payload XML exportado al exportar a SFTP. Esta función es configurable a través de Export Settings y proporciona a los sistemas posteriores un registro de auditoría completo de cada cambio de estado y acción realizada sobre un documento dentro de DocBits — incluyendo quién realizó el cambio, cuándo ocurrió y cuáles eran los estados anterior y actual. Esto es particularmente valioso para el cumplimiento normativo, la trazabilidad y el análisis operativo.
* **Actualización de cargos en confirmación de pedido para Infor On Premise:**\
  Los clientes de Infor On Premise ahora pueden procesar confirmaciones de pedido que incluyen cargos directamente en DocBits. Los cargos se actualizan completamente a través de la exportación, haciendo que el proceso de confirmación de pedido de extremo a extremo sea fluido y eliminando la necesidad de ajustes manuales posteriores.
*   **Aplicar Layout predeterminado a todos los Origins:**\
    Se ha introducido un nuevo botón **Apply Default Layout to Origins** en la pantalla de configuración de layout. Los administradores ahora pueden enviar el layout predeterminado a todos los origins dentro de una organización en una sola acción, eliminando el laborioso proceso manual de copiar y pegar JSON de layout en cada origin individualmente. Esto es especialmente útil durante la incorporación de nuevos clientes donde múltiples origins necesitan ser configurados de manera consistente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Selección de tipo de documento para importación FTP:**\
    Las configuraciones de importación FTP ahora admiten la asignación de tipo de documento por carpeta. Al configurar una importación FTP, los usuarios pueden especificar qué tipo de documento — como Factura o Confirmación de Pedido — debe aplicarse a todos los documentos importados desde esa carpeta. Los documentos se clasifican automáticamente en la importación, eliminando la necesidad de asignación manual del tipo de documento después de la ingesta. Esto admite organizaciones que gestionan múltiples tipos de documentos en diferentes suborganizaciones y carpetas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Exportación a GLS840 para Infor On Premise:**\
  DocBits ahora admite la exportación de documentos al programa GLS840 para clientes de Infor On Premise, ampliando la gama de destinos de exportación admitidos para entornos on-premise.
*   **Mejoras de UI para Watchdog y configuración de exportación:**\
    Las pantallas de configuración de Watchdog y configuración de exportación se han actualizado con una interfaz de usuario mejorada, ofreciendo un diseño más limpio y una experiencia más intuitiva para los administradores que gestionan estas configuraciones.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Corrección de errores:

* Se corrigió un problema en el que los usuarios con derechos de visualización válidos no podían ver documentos — la lógica de permisos se ha refactorizado con una verificación de nivel de acceso que reemplaza el enfoque anterior de filtrado basado en grupos.
* Se mejoró el manejo de excepciones en múltiples áreas de la aplicación para mayor estabilidad.
* Se resolvió un problema en el que las columnas de tipo booleano no se manejaban correctamente durante la extracción de campos.
* Se corrigió un problema de autenticación asíncrona en el endpoint de carga de archivos.
* Se resolvieron problemas de visualización de la UI para la tabla de PO en la pantalla de validación.
* Se actualizó la plantilla de scripts para incluir comentarios de seguimiento de cambios para mejor auditabilidad.
* Se corrigió un problema con los campos desplegables que no se comportaban correctamente en la pantalla de validación.
* Se corrigió un problema en el que el campo de suborganización no se rellenaba previamente al actualizar las asignaciones de documentos desde el dashboard.

## **Lanzamiento Winter Summit 10 de diciembre de 2025**

### Mejoras de DocBits:

*   **Personalización mejorada de reglas de coincidencia de OC:**\
    DocBits ahora proporciona un control más granular y personalizable sobre las reglas de coincidencia de órdenes de compra. Los administradores pueden configurar con precisión qué columnas deben evaluarse durante el proceso de coincidencia para cada tipo de documento, asegurando que solo se consideren los campos más relevantes. Además, se pueden definir tolerancias a nivel de columna, lo que permite una mayor flexibilidad al manejar discrepancias menores. Cada regla también puede configurarse para aplicarse a la coincidencia manual, la coincidencia automática o ambas, brindando a los equipos la capacidad de adaptar el flujo de trabajo de coincidencia a sus requisitos operativos exactos. Estas mejoras mejoran significativamente la adaptabilidad y precisión del proceso de coincidencia de órdenes de compra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Soporte para múltiples cuentas financieras de proveedores:**\
    DocBits ahora admite la gestión de múltiples cuentas financieras para proveedores a través del RemitToPartyMaster BOD proporcionado por Infor. Esta mejora permite a las organizaciones mantener varios registros de cuentas de remisión para un solo proveedor, mejorando la flexibilidad y precisión en el procesamiento de pagos. Se ha introducido una nueva configuración para habilitar o deshabilitar esta capacidad, permitiendo a los administradores activar la función según sus necesidades operativas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Agregar acceso de usuario a resultados de extracción OCR:**\
    El botón **Vista OCR** en la pantalla de validación de campos ahora está disponible para todos los usuarios que tienen acceso de validación, en lugar de estar limitado a los administradores. Con esta actualización, cualquier usuario autorizado puede revisar los resultados de extracción OCR directamente, facilitando la validación de la precisión de los datos y monitoreando el rendimiento general del OCR. Esta mejora promueve una mayor transparencia y mejora la eficiencia del flujo de trabajo de validación.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Representación dinámica de columnas en pantallas de aprobación:**\
  Vistas de aprobación mejoradas para mostrar dinámicamente solo las columnas configuradas para comparación en las preferencias de base de datos de cada organización. Anteriormente, algunas columnas específicas de la organización aparecían vacías cuando no estaban configuradas para comparación, causando confusión. Ahora, las vistas de aprobación solo muestran campos que se están comparando activamente. Esto proporciona pantallas de aprobación más claras y específicas de la organización sin columnas vacías o irrelevantes.
* **Campo de tipo de pedido agregado a la búsqueda de datos maestros**:\
  La lista de encabezados de órdenes de compra ahora incluye una columna "Tipo de pedido" en la búsqueda de datos maestros, proporcionando capacidades adicionales de categorización.
* **Mejoras del panel de control de filtros personalizados:**\
  La funcionalidad de compartir panel de control se ha mejorado para proporcionar mayor flexibilidad a los usuarios compartidos. Las personas que tienen paneles compartidos con ellos ahora pueden ajustar y editar los filtros del panel, permitiéndoles adaptar la información mostrada a sus necesidades específicas. Esta mejora admite una experiencia de visualización más personalizada e interactiva, asegurando que los usuarios puedan refinar fácilmente los conocimientos de datos más relevantes para sus tareas.
* **Prefijos personalizables para columnas de pantalla de aprobación:**\
  Se ha introducido una nueva opción configurable para mostrar prefijos antes de las columnas de documentos en las pantallas de aprobación. Esta función se puede gestionar directamente dentro del constructor de diseño, otorgando a los administradores control total sobre si se muestran los prefijos y a qué tipos de documentos se aplican. Al habilitar esta opción, los usuarios obtienen un contexto más claro y una mejor legibilidad al revisar documentos durante el proceso de aprobación.

### Mejoras generales

* Se mejoró el registro de errores para tablas mal entrenadas en la extracción de tablas.
* Se agregó un límite de compartición para paneles de hasta 10 usuarios o 5 grupos, junto con un mensaje de error claro cuando se alcanza el límite.
* Se mejoró el manejo de errores para paneles personalizados cuando un usuario intenta crear un panel con un nombre que ya existe.

### Correcciones de Errores:

* Se corrigió un problema donde los correos electrónicos parecían enviarse exitosamente desde la sección Detalles del Proveedor pero no se entregaban a los destinatarios.
* Se corrigió un problema donde los campos desplegables agregados a las pantallas de aprobación/rechazo no se mostraban.
* Se corrigió un problema donde todos los documentos exportados estaban marcados como actualizados por última vez por el usuario incorrecto.
* Se corrigió un problema donde los documentos mostraban el estado "Flujo de trabajo en progreso" pero no se ejecutaban flujos de trabajo y el registro permanecía vacío.
* Se corrigió un problema donde usuarios no relacionados eran asignados a documentos en el momento de la exportación sin realizar ningún trabajo en ellos.
* Se corrigió un problema donde usuarios con permisos correctos no podían rechazar documentos asignados y recibían errores.
* Se corrigió un problema donde los iconos de flujo de documentos no se mostraban para algunas organizaciones.
* Se corrigió un problema donde aparecía una ventana emergente al cargar documentos con arrastrar y soltar en el panel.
* Se corrigió un problema donde las banderas E-TEXT se mostraban como habilitadas en la interfaz de usuario aunque la respuesta de la API mostraba todos los valores como falsos.
* Se corrigió un problema donde ocurría un error al cargar documentos que contenían páginas en blanco.
* Se resolvió un problema donde los hipervínculos de tareas en las notificaciones por correo electrónico no redirigían a los usuarios a la pantalla de aprobación correcta.
* Se resolvió un problema donde la selección de la sub-organización cruzada causaba que la Búsqueda de Datos Maestros no mostrara proveedores. Los usuarios ahora pueden ver correctamente los datos de proveedores entre organizaciones.

## Release Autumn Summit 22 de Octubre de 2025

### Mejoras en DocBits:

*   #### Mejoras en el Diseño de Plantillas de Correo Electrónico:

    El editor de plantillas de correo electrónico ha sido rediseñado para proporcionar una estructura más clara y una experiencia más fluida. Ahora es más intuitivo seleccionar campos de documentos, y los adjuntos se pueden incluir directamente dentro de las plantillas. Estas mejoras hacen que sea más rápido y fácil crear correos electrónicos profesionales y personalizados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Mejoras en el Panel de Control:

    El panel de control se ha ampliado para mejorar la navegación y personalización. Con nuevas pestañas, los usuarios pueden cambiar más rápidamente entre diferentes tipos de documentos, reduciendo el tiempo dedicado a buscar la vista correcta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Paneles de Filtro Personalizados:

    Además, los paneles de control ahora se pueden personalizar y filtrar según las preferencias individuales. Estos paneles personalizados también se pueden compartir con colegas, lo que facilita la creación de vistas de informes consistentes para todo el equipo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Registros de Notificaciones por Correo Electrónico:

    Una nueva función de registro está disponible para todas las notificaciones por correo electrónico. Los usuarios ahora pueden revisar un historial de notificaciones enviadas, lo que facilita verificar las entregas y solucionar problemas si los correos electrónicos no se reciben.
*   #### Soporte para Facturas Electrónicas: e-SLOG 1.6 y 2.0:

    Se ha introducido soporte para formatos adicionales de facturas electrónicas. El sistema ahora puede procesar y generar las versiones e-SLOG 1.6 y 2.0, ampliando la compatibilidad con socios y requisitos regulatorios.
*   #### Mejoras en la Detección de Duplicados:

    La detección de duplicados se ha mejorado con dos opciones de configuración potentes. El **Intervalo de Detección de Duplicados** le permite definir un rango de tiempo para verificar duplicados de manera más precisa, mientras que la configuración **No Permitir Exportar Duplicados** evita automáticamente la exportación de documentos detectados como duplicados. Juntas, estas mejoras brindan más control y garantizan una mayor precisión de los datos.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Mejoras en Árboles de Decisión:

    Los árboles de decisión son ahora más versátiles, con la capacidad de devolver valores de campos de documentos. Esto permite una lógica de automatización más avanzada, lo que permite a los flujos de trabajo tomar decisiones basadas en datos reales de documentos.
*   #### Nuevas Tarjetas de Flujo de Trabajo:

    Dos nuevas tarjetas de flujo de trabajo amplían las capacidades de automatización. La primera le permite verificar si un documento pertenece a una suborganización específica, lo que facilita el manejo de configuraciones multi-entidad. La segunda introduce una verificación de tolerancia de fecha de entrega, que compara las fechas de entrega con la fecha actual en días laborables para ayudar a gestionar y hacer cumplir los requisitos de entrega de manera más efectiva.
*   #### Mejoras en la Exportación CSV:

    La función de exportación CSV se ha mejorado significativamente. En lugar de exportar solo los documentos mostrados en la página actual, el sistema ahora exporta todos los documentos en un conjunto de datos. Cada exportación crea una entrada de registro, y el CSV resultante se envía automáticamente por correo electrónico, lo que proporciona un proceso de exportación más completo y confiable.
*   #### Marco de Tiempo para Eliminación de Órdenes de Compra:

    Una nueva opción de configuración permite a los administradores definir un marco de tiempo para la eliminación de órdenes de compra. Esta mejora añade flexibilidad y control sobre las políticas de retención de datos, asegurando que las órdenes de compra solo se eliminen cuando sea apropiado.

### Correcciones de Errores

* Se corrigió un problema donde se incluían datos antiguos al exportar documentos.
* Se corrigió el filtro para Errores de Exportación, que anteriormente mostraba también otros estados.
* Se resolvió una discrepancia de validación de tabla donde "Precio Unitario" provocaba errores pero "Precio Unitario Por" no, a pesar de que los valores eran correctos.
* Se corrigió un problema donde agregar una nueva columna al panel de control fallaba.
* Se corrigió un problema donde las tareas no eran visibles en la columna de tareas del panel de control.
* Se corrigió el comportamiento de ordenación aleatoria para que las listas sigan ahora un orden consistente.
* Se resolvió un problema donde no se podía detener el cambio de tamaño de columna.
* Se corrigió un error que impedía la coincidencia manual de líneas en la pantalla de Coincidencia de Órdenes de Compra.
* Se corrigió un problema donde la opción de adjuntar correo electrónico se restablecía después de guardar.
* Se corrigió un problema donde la contabilidad automática mostraba inicialmente IDs de base de datos al abrirse por primera vez.
* Se corrigió el comportamiento de campo difuso para que los valores ya no se sobrescriban incorrectamente.
* Se corrigió un problema donde los campos en la cuenta automática desaparecían después de eliminar el contenido.
* Se corrigió un error donde el usuario no podía cambiar el nombre de "Nombre" y "Apellido" en el cuadro de configuración.
* Se resolvió un problema donde los documentos podían quedar atascados en "flujo de trabajo en progreso."
* Se corrigió un problema de color de icono de menú donde los colores de organización seleccionados no se aplicaban correctamente.
* Se corrigió un problema donde a veces los códigos QR no eran reconocidos.
* Se corrigió un problema donde las cuentas no se podían eliminar con retroceso para ingresar una diferente.
* Se resolvió una confusión de idioma después de iniciar sesión tras la actualización de producción.

## Lanzamiento Spring Bloom – 23 de abril de 2025

### Mejoras en DocBits:

* **Opción de Filtro para el Registro de Importación de Correos Electrónicos:** Los usuarios ahora tienen la capacidad de filtrar los registros de importación y ordenar la tabla para una visión más clara y eficiente. Esta mejora agiliza el proceso de identificación y gestión de entradas de correo electrónico, mejorando la resolución de problemas y la gestión general de registros.
* **Soporte Multilingüe para la Lista de Valores:** Hemos ampliado las capacidades multilingües en la función de Lista de Valores. Los administradores ahora pueden definir etiquetas en múltiples idiomas, asegurando que la etiqueta correcta se muestre automáticamente según la configuración del idioma del sistema del usuario. Esta mejora promueve una mayor accesibilidad y localización, facilitando que los usuarios de todo el mundo interactúen con la plataforma en su idioma nativo.
* **Mejoras en los Detalles del Usuario en Configuración:** La interfaz de configuración ahora muestra información completa del usuario. Los administradores pueden ver fácilmente las afiliaciones a grupos, detalles de suborganizaciones y datos clave adicionales, lo que permite una mejor gestión de los roles de usuario y una comprensión más clara de las estructuras del equipo.
* **Información de Contabilidad Automática en la Pantalla de Aprobación:** La pantalla de aprobación ahora presenta detalles de contabilidad automática junto con la información de la factura. Esta mejora proporciona una visión más profunda de los datos de transacción, facilitando procesos de revisión más fluidos y una toma de decisiones más informada respecto a las facturas.
* **Contador de Tareas para Documentos en la Vista del Tablero:** Los documentos en el tablero ahora pueden indicar las tareas abiertas asociadas con ellos y mostrar el número total de tareas pendientes. Esta función proporciona a los usuarios una visión rápida de las acciones pendientes, mejorando la gestión de tareas y la eficiencia del flujo de trabajo.
* **Selección de Modelo de IA Basado en Proveedores:** Los usuarios ahora pueden seleccionar el modelo de IA utilizado para la extracción de datos por proveedor. Esta mejora permite una optimización ajustada, asegurando una mejor precisión en la extracción para diferentes proveedores y mejorando los resultados generales del procesamiento de datos.
* **Registros de Flujo de Trabajo Mejorados para Tarjetas de Árbol de Decisión:** Los registros ahora muestran la salida del árbol de decisión, facilitando el seguimiento y la comprensión de cómo se tomaron las decisiones dentro de los flujos de trabajo.
*   **Introducción de un Nuevo Sistema de Pruebas Automáticas para Mejorar la Funcionalidad y Estabilidad del Sistema:**

    Nos complace anunciar la implementación de un nuevo sistema de pruebas automatizadas diseñado para mejorar la funcionalidad y fiabilidad general de nuestra plataforma. Esta nueva configuración realizará verificaciones consistentes y exhaustivas en nuestro sistema para identificar cualquier problema antes de que afecte su experiencia. Al automatizar estas pruebas, podemos garantizar respuestas más rápidas a problemas potenciales y mantener los más altos estándares de calidad para nuestro sistema.

    ​

### Corrección de Errores

* Se resolvió un problema donde las tareas no aparecían en la pantalla de validación/aprobación.
* Se corrigió la posición del botón Siguiente/Anterior para que permanezca estático.
* Se solucionaron problemas de desplazamiento en las vistas de script y árbol de decisiones, asegurando que los botones de acción permanezcan estacionarios durante el desplazamiento.
* Se eliminó el campo de país de origen de las facturas electrónicas.
* Se corrigió un problema con el contador de tareas que mostraba un número inexacto de tareas.
* Se añadieron traducciones faltantes.
* Se corrigieron campos personalizados para mostrar nombres descriptivos en lugar de IDs.
* Se actualizó la lista de accesos directos para la pantalla de coincidencia de PO.
* Se resolvió un problema donde los documentos se descargaban con un nombre de archivo incorrecto.
* Se corrigieron inconsistencias de ordenamiento en la tabla de líneas de factura dentro de la coincidencia de PO.
* Se solucionó un problema que afectaba la funcionalidad de creación de tareas.
* Se corrigió un problema en la coincidencia de PO donde el ordenamiento de la tabla de facturas se restablecía al coincidir una línea.
* Se resolvieron problemas de contabilidad automática asegurando que las referencias de reserva se dividieran correctamente cuando se divide un monto.
* Se actualizó la información del host de ClickHouse.
* Se resolvió un problema donde los documentos duplicados no eran reconocidos como duplicados.
* Se corrigieron problemas de exportación causados por referencias de reserva que eran demasiado largas.
* Se resolvió un problema donde las casillas de verificación de solo lectura no eran de solo lectura.

​

## Lanzamiento de Hot Fix Winter Frost 10 de abril de 2025

### Mejoras en DocBits:

* **Función de Script `set_column_date_value` Mejorada:** La función `set_column_date_value` ahora incluye soporte para la opción `skip_weekend`, permitiendo que los valores de fecha omitan automáticamente los fines de semana al aplicarse.
* **Mejora en el Soporte de Carga de Archivos:** Los archivos PNG y JPEG ahora se pueden cargar directamente y se convierten automáticamente en formato PDF para un manejo de documentos más eficiente.
* **Actualizaciones de Funcionalidad de Watchdog:**
  * Ahora soporta exportación a **Enaio** para una mejor integración del sistema.
  * Capacidades de análisis mejoradas para extraer información de las estructuras XML de `Sync.ContentDocument`, lo que permite un procesamiento de datos más eficiente.

### Correcciones de Errores

* Se solucionó un problema en una función de script.
* Se resolvió un problema donde las órdenes de compra tenían un estado incorrecto después de ser actualizadas.

## Lanzamiento Hot Fix Winter Frost 11 de marzo de 2025

### Mejoras en DocBits:

* **Extracción de Datos Mejorada:** Se añadió una opción para extraer el **Purchase Order** o **Item Number** de una línea arriba o abajo.
* **Acceso Ampliado a Suborganizaciones Cruzadas:** Los usuarios no administradores ahora también pueden acceder a la función de **Cross Sub-Organizations**.

### **Corrección de Errores:**

* Se corrigió un problema donde los usuarios no podían ser añadidos a un grupo.
* Se corrigió un problema con fallos en la importación de correos electrónicos.
* Se resolvió un problema con la capacitación en el campo en documentos con más de una página
* Se corrigió un problema donde los scripts no funcionaban correctamente.
* Se resolvió un problema donde los datos del documento no se mostraban correctamente
* Se corrigió un problema con la configuración de actualización automática de la orden de compra
* Se solucionó un problema donde los tokens de suscripción se mostraban incorrectamente
* Se resolvió un problema donde la pantalla de tareas mostraba una versión de documento desactualizada
* Se corrigió un problema que causaba que los documentos no cambiaran su estado
* Se solucionó un problema donde los usuarios podían ser añadidos a una suborganización dos veces.
* Se solucionó un problema donde cambiar la suborganización de un documento causaba restablecer el usuario o grupo asignado.
