# Notas de versión

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
* Se corrigió un problema en el que las líneas de PO con un estado excluido (p. ej., "Closed") aún podían arrastrarse y emparejarse en la pantalla de PO Matching a pesar de estar excluidas por las reglas de emparejamiento.

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
