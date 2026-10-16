# NOVA — Versión principal

**Instantánea de versión: 16 de octubre de 2026**

NOVA incluye todas las funciones que antes estaban disponibles como beta en VESTA como funciones regulares, junto con la validación guiada de documentos, más formas de mejorar la automatización, comprobaciones más claras de facturas electrónicas y un mejor control sobre las importaciones y el procesamiento de documentos. Estas notas describen las adiciones orientadas al cliente en las versiones de servicio que se enumeran a continuación, en comparación con el [último hotfix de VESTA publicado, R1.0.15 del 14 de octubre de 2026](incremental-updates-14-october-2026.md), incluidos hotfixes anteriores de VESTA.

La instantánea identifica las compilaciones cubiertas por estas notas. Para consultar la disponibilidad en su entorno de pruebas o de producción y el cambio entre canales, consulte el [ciclo de vida de las versiones de DocBits](../docbits-release-lifecycle-strategy.md). Las funciones que disponen de un interruptor de organización o de tipo de documento aún deben ser habilitadas por un administrador.

## Antiguas funciones beta de VESTA: incluidas en NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Todas las antiguas funciones beta de VESTA forman ahora parte del conjunto de funciones regulares de NOVA.** Para los clientes que no utilizaron la beta de VESTA, esto amplía las funciones disponibles para su equipo, incluidas **Gestionar diseños**, [**Reglas de validación personalizadas**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) y [**Reglas de transformación**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). La configuración de la organización, los interruptores de tipo de documento y los permisos de acceso siguen aplicándose.

Las mismas antiguas funciones beta se convertirán en funciones regulares de VESTA con el **siguiente hotfix de VESTA, previsto para el [11 de noviembre de 2026](vesta-hotfix-11-november-2026.md)**. Este anuncio cubre las antiguas funciones beta de VESTA; las secciones siguientes también describen adiciones y mejoras adicionales de NOVA.

## Qué añade NOVA para los clientes <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

La siguiente comparación cubre las antiguas funciones beta ahora disponibles, nuevas capacidades y extensiones de funciones existentes. La base de VESTA incluye funcionalidad que solo estaba disponible en beta; su inclusión en el conjunto de funciones regulares de NOVA es un cambio de versión orientado al cliente.

| Capacidad | Base de VESTA (incluida la beta) | Qué ganan los clientes con NOVA |
| --- | --- | --- |
| **Usar antiguas funciones beta** | Funciones disponibles a través de la beta de VESTA | **Funciones regulares de NOVA:** todas las antiguas funciones beta de VESTA están incluidas. Su introducción regular en VESTA está prevista para el hotfix del 11 de noviembre de 2026. |
| **Obtener ayuda al validar un documento** | Asistente de configuración y Comprobación de campos de cabecera | **Nuevo Asistente de validación:** identificar campos bloqueantes, saltar al valor relevante, revisar correcciones sugeridas y mantener el chat en una ventana separada. |
| **Mejorar la automatización a partir de correcciones cotidianas** | Panel de Touchless Intelligence, diagnóstico de proveedores y propuestas de cambios | **Nuevo proceso de revisión y medición:** enviar solicitudes de mejora, revisar propuestas de reglas aprendidas, ver evidencia de documentos afectados, clasificar oportunidades y medir resultados tras la activación. |
| **Comprender y resolver errores de facturas electrónicas** | Comprobaciones de documentos electrónicos, catálogo de reglas y visor de XML | **Validación de facturas electrónicas ampliada:** informes agrupados por nivel de validación, controles de políticas e historial de cambios, rechazo desde el informe e inspección de XML dentro de facturas PDF compatibles. |
| **Controlar importaciones FTP/SFTP** | Conexiones de importación y retención o archivado de archivos fuente | **Nueva configuración guiada y controles:** asistente de conexión, registros paso a paso, reintentos configurables y notificaciones de fallo, y eliminación de archivos fuente tras una importación exitosa. |
| **Trabajar con reglas y diseños** | Motores de reglas, registros de ejecución y transformaciones tras la búsqueda de datos maestros; los paneles de gestión requerían un enlace beta | **Acceso más amplio y mejores herramientas:** abrir paneles de gestión directamente, buscar y previsualizar diseños de destino, abrir el editor de diseño de un documento y registrar la ejecución de la selección de diseño. |
| **Actuar desde el Asistente de configuración** | Chat de configuración, previsualizar/confirmar/deshacer y alertas proactivas de estado de las importaciones | **Acciones adicionales:** gestionar conexiones fallidas, ver historial de desactivaciones, cambiar elementos de configuración seleccionados, crear una regla de validación inactiva desde un catálogo y ver explicaciones de página. |
| **Controlar el procesamiento de documentos** | Límites de páginas por organización y reinicio de documentos | **Nuevas opciones a nivel de documento:** reiniciar con un número de páginas elegido, ver páginas procesadas frente al total y elegir si se extraen campos ocultos. |
| **Conciliar entregas complejas** | Conciliación de pedidos de compra y vinculación manual de líneas | **Conciliación más flexible:** seleccionar líneas en cualquier dirección, conservar opcionalmente cada sublínea de documento conciliada y agrupar solicitudes de exportación por columnas de línea configuradas. |
| **Mantener el trabajo exportado y el completado como estados distintos** | Flujos de trabajo de exportación y Finished existentes | **Nuevos controles de estado:** utilice Exported para el procesamiento de seguimiento, opcionalmente bloquee documentos Finished y localice documentos retenidos por el límite de ejecución del flujo de trabajo. |

### Habilitar las funciones que requieren configuración

* **Asistente de validación:** un administrador de organización lo habilita en **Configuración → Información de la empresa → Asistentes**. Es independiente del Asistente de configuración y permanece desactivado hasta que se habilite.
* **Informes de revisión de mejoras y de consultoría:** requieren acceso de administrador de organización y de Analytics. Las propuestas aprendidas necesitan historial de correcciones; un resultado medido necesita datos suficientes y que el período de seguimiento esté completo.
* **Controles de reglas y diseños:** sus interruptores de habilitación por tipo de documento siguen aplicando. NOVA hace accesibles los paneles de gestión sin un enlace beta.
* **Comportamiento de procesamiento opcional:** configure la limpieza y los reintentos de FTP por conexión. La expansión de sublíneas de uno a muchos y el bloqueo de documento terminado son ajustes de activación voluntaria.

Para la disponibilidad en su entorno y el cambio de canal de publicación, consulte el [ciclo de vida de las versiones](../docbits-release-lifecycle-strategy.md).

## Ver los videos de funciones <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Utilice estos recorridos junto con las notas de la versión para comprender las funciones relacionadas y su configuración. Los videos disponibles en español se enlazan a continuación; los demás videos están claramente etiquetados como English.

| Tema | Video |
| --- | --- |
| Elegir la automatización adecuada — incluido dónde encajan las Reglas de conciliación de pedidos | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/en.mp4) |
| Reglas de transformación | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/en.mp4) |
| Reglas de validación personalizadas | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4) |
| Diseños y reglas de selección | [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4) |
| Touchless Intelligence | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/en.mp4) |
| Validación de facturas electrónicas | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/en.mp4) |
| Usuarios y acceso de administrador | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/en.mp4) |
| Suborganizaciones | [Video en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/es.mp4) · [Video en English](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/en.mp4) |

### AI Table: seis videos breves

Estos videos están en English. Vea la serie completa o elija el tema que necesite.

1. [Leer la tabla de AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Corregir una columna y enseñar a DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Tres problemas típicos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Líneas de descuento, impuesto y cantidad cero](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Lo que la IA ya lee correctamente](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [El asistente y quién puede cambiar qué](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Para capturas de pantalla e instrucciones detalladas, consulte la [guía de AI Table](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Asistente de validación: ayuda con el documento que tiene delante

* **Identificar qué bloquea el progreso.** Pregunte por qué un documento no puede continuar. El asistente identifica los campos afectados, explica el problema y ofrece un salto al campo o a la celda de tabla. Utiliza el documento actual y los derechos de acceso del usuario.
* **Revisar correcciones sugeridas en contexto.** Donde está soportado, los revisores pueden aplicar un valor de campo o tabla propuesto, utilizar un candidato de datos maestros, repetir una búsqueda o abrir la pantalla de conciliación correspondiente. Los cambios en el formulario siguen sujetos al proceso normal de revisión y guardado del documento. Los documentos de solo lectura y los usuarios sin permiso de edición no reciben acciones de edición.
* **Consultar sobre conciliación y contabilidad.** El asistente puede explicar el contexto de pedido de compra o contable cuando se abre en esas pantallas. Los cambios al formulario de validación se realizan en la pantalla de validación.
* **Comprender una mejora antes de usarla.** Las explicaciones conectan una regla o ajuste propuesto con los valores reales del documento. Pueden incluir un diagrama y una explicación narrada en el idioma del usuario cuando esté disponible. Las sugerencias se mantienen enfocadas en el documento actual.
* **Trabajar con el chat en una ventana independiente.** Abra la conversación en una ventana aparte mientras revisa el documento. Las acciones que modifican el formulario permanecen en la ventana del documento.
* **Ver más detalle detrás de los valores extraídos.** La vista de origen del valor añade detalles como OCR frente a la capa de texto del PDF, la coincidencia con reglas de extracción y la búsqueda que proporcionó un valor. La explicación de la tabla de IA añade consejos de configuración más accionables y recuentos más claros.

Un administrador de organización habilita el Asistente de validación de forma independiente al Asistente de configuración en **Configuración → Información de la empresa → Asistentes**.

## Convertir correcciones repetidas en mejoras de automatización

El panel existente de [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) incorpora un proceso de revisión y seguimiento:

* **Propuestas de reglas aprendidas.** Las correcciones manuales repetidas pueden sugerir una [regla de transformación](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Los administradores ven lo que escribiría, los ejemplos de apoyo y los documentos en los que reemplazaría un valor que el equipo había aceptado. Una propuesta se revisa antes de convertirse en una regla activa.
* **Solicitudes de mejora de los revisores.** Los usuarios pueden enviar una mejora desde el asistente de documentos para que un administrador la revise en Touchless Intelligence. La solicitud mantiene su explicación y su decisión juntas.
* **Medir lo que ocurrió tras la activación.** Para las reglas de transformación compatibles, DocBits compara las correcciones manuales antes y después de la activación y muestra la tasa de procesamiento sin intervención junto a ellas. La medición utiliza períodos de 14 días e identifica datos insuficientes en lugar de inventar una mejora. Cambiar una regla inicia una nueva medición para esa revisión.
* **Informe de consultoría.** Los administradores pueden generar una vista clasificada de oportunidades de mejora en extracción, datos maestros, conciliación de pedidos de compra, contabilidad, configuración y flujo de procesamiento. El impacto estimado se etiqueta como estimación hasta que se haya medido.
* **Consejos de conciliación específicos por proveedor.** Los problemas repetidos de conciliación de proveedores y artículos pueden informar propuestas de tolerancias o [reglas de conciliación de pedidos](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md). Los consejos distinguen un pedido de compra ausente de un problema de regla o tolerancia.
* **Resúmenes de seguimiento.** Un resumen semanal para administradores reúne las solicitudes de mejora abiertas, las principales oportunidades y las mediciones completadas cuando hay algo que informar. Se puede notificar a los solicitantes cuando un resultado medido esté disponible.

## Asistente de configuración: acciones adicionales y explicaciones de páginas

El [Asistente de configuración](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), incluidas las alertas proactivas de salud de correo electrónico/FTP, ya se incluyó en VESTA. NOVA añade acciones y contexto a esa experiencia existente:

* **Acciones de conexión desde un aviso de salud.** Abra la conexión afectada, revise la acción disponible y confírmela desde el asistente. Los avisos de salud también pueden descartarse. Las tarjetas básicas de advertencia por canal y su información de error/reintento ya existen en VESTA.
* **Historial de desactivación visible.** Donde se registre, una importación deshabilitada muestra cuándo se apagó y por quién.
* **Acciones revisadas adicionales.** Los administradores pueden previsualizar y confirmar cambios compatibles como activar tipos de documento, renombrar un grupo, cambiar el modo de búsqueda de un campo de búsqueda, eliminar un campo o crear una regla de validación personalizada inactiva desde el catálogo.
* **Gestionar conexiones de importación con fallos.** Las tarjetas compatibles pueden apagar o eliminar una conexión tras la confirmación. Las acciones reversibles ofrecen una opción de deshacer; la eliminación permanente se identifica como tal.
* **Explicaciones de páginas.** Ciertas páginas de configuración ofrecen vídeos con subtítulos y transcripciones, incluidos diseños, usuarios, suborganizaciones, reglas de transformación y validación de facturas electrónicas donde haya disponible una versión en el idioma.

## Reglas y diseños: acceso directo y mejores diagnósticos

* **Los controles de la antigua beta se convierten en funciones regulares.** Gestionar diseños, [Reglas de validación personalizadas](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) y [Reglas de transformación](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) son visibles en la configuración avanzada de tipos de documento de NOVA sin un enlace de beta. Sus interruptores de habilitación siguen bajo control del administrador. Estos controles se incluyen en el hotfix de VESTA previsto para el 11 de noviembre de 2026 junto con todas las demás funciones de la antigua beta de VESTA.
* **Diagnósticos de reglas más útiles.** Las reglas de selección de diseño incorporan una opción **Registrar ejecución**. La búsqueda de reglas acepta identificadores de reglas, y al abrir un editor se carga la regla guardada actual. El registro de ejecución de reglas existente sigue siendo el lugar para revisar lo que se ejecutó.
* **Elija y abra diseños con más contexto.** Busque diseños de destino, previsualice su contenido y ábralos directamente desde una regla de selección. Las reglas de selección de aprobación aceptan correctamente los tipos de diseño de aprobación compatibles. Los administradores también disponen de un acceso directo desde la validación de documentos al editor de diseños de ese tipo de documento.
* **Seleccione varios valores de condición.** Condiciones como **es uno de** admiten múltiples valores seleccionados.
* **Encuentre campos de detección de duplicados más rápido.** El selector de campos en la configuración de duplicados del tipo de documento es buscable.

Las transformaciones tras la búsqueda de datos maestros, el registro básico de ejecución de reglas, los editores de reglas más amplios y las correcciones de clonación de reglas estándar ya tienen implementaciones en la línea base de VESTA. NOVA mantiene esa funcionalidad y pone los antiguos controles de gestión beta a disposición como funciones regulares.

Para pasos de configuración, ejemplos y pruebas, consulte [Reglas de validación personalizadas](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) y [Reglas de transformación](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Para elegir qué diseño utiliza un documento, consulte [Reglas de selección de diseño](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## Validación de facturas electrónicas: hallazgos más claros y controles de política

* **Un informe organizado por nivel de validación.** Los hallazgos se agrupan en sintaxis, esquema, reglas de negocio, reglas de verificación cruzada y reglas específicas de país, con grupos adicionales para otras comprobaciones de estándares y de valores. Los mensajes y resúmenes utilizan el idioma del usuario cuando hay traducciones disponibles.
* **Comprobaciones más completas y resultados más claros.** El validador y el informe actualizados distinguen entre errores, advertencias y la severidad efectiva tras la configuración específica de la organización. La página se denomina **Validación de facturas electrónicas**.
* **Políticas por tipo de documento.** Los administradores pueden revisar si la validación de facturas electrónicas está habilitada y si los fallos bloquean el procesamiento. La vista de políticas identifica las anulaciones por subtipo, y los cambios de política se registran en un historial de cambios.
* **Inspeccione el XML dentro de una factura en PDF.** El visor de XML puede leer el XML incrustado en PDFs ZUGFeRD/Factur-X compatibles, abrir la posición referenciada por un hallazgo y volver al documento.
* **Rechace con un motivo registrado.** Un revisor autorizado puede rechazar un documento elegible desde el informe de validación. El informe prepara un motivo a partir de sus errores para que el revisor lo verifique antes de confirmar.
* **Correcciones adicionales de formato.** Las facturas CII de utilidad EDNA se reconocen, y las correcciones en el mapeo de IVA de XRechnung mejoran cómo los valores relevantes de la factura llegan a los campos de DocBits.

Consulte [Reglas de validación de documentos electrónicos](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## Importaciones por FTP/SFTP y correo electrónico

* **Configuración guiada de FTP/SFTP.** El asistente de conexión separa los detalles del servidor, las opciones de importación y la configuración. Las comprobaciones de conexión y los mensajes de error más claros ayudan a los administradores a identificar una conexión incorrecta o una carpeta de origen inexistente.
* **Registros de importación por paso.** Revise el progreso de un archivo a través de la importación FTP, incluida la carga y la acción configurada sobre el archivo de origen.
* **Comportamiento configurable de reintentos y notificaciones.** Defina el intervalo entre reintentos posteriores, cuánto tiempo seguir reintentando y los destinatarios de notificaciones. Cuando se agota la ventana de reintentos, la conexión puede deshabilitarse automáticamente y notificarse a los destinatarios; el asistente muestra el aviso de desactivación.
* **Eliminar tras una importación exitosa.** Además de retener o archivar los archivos de origen, los administradores pueden elegir eliminarlos del servidor FTP/SFTP tras una importación exitosa. El archivado y la eliminación son alternativas separadas.
* **Recuperación de importaciones más fiable.** Se evita que ejecuciones FTP superpuestas carguen el mismo archivo de origen dos veces. La edición de una conexión conserva su contraseña almacenada a menos que se reemplace. El manejo de correo electrónico no marca un mensaje para eliminación cuando la copia falló.
* **Soporte de correo firmado.** Los mensajes S/MIME con firma opaca que contienen facturas pueden desempaquetarse en lugar de omitirse.
* **Historial y estado de la configuración de correo electrónico.** La configuración de importación muestra quién guardó o activó por última vez una configuración. El interruptor de correo entrante refleja el estado activo almacenado, incluida una configuración recién guardada.

Consulte [Importación por FTP](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) y [Probar una conexión de importación FTP](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Procesamiento y extracción de documentos

* **Reiniciar con un número de páginas elegido.** El panel añade una acción de reinicio que permite a los revisores especificar cuántas páginas procesar para ese documento, dentro de su número real de páginas.
* **Ver el límite de procesamiento.** El panel puede mostrar las páginas procesadas frente al total de páginas de un documento limitado. La configuración **Páginas a procesar** de la organización se agrupa bajo Procesamiento de documentos en **Clasificar y extraer**.
* **Controlar la extracción de campos ocultos.** Los administradores pueden elegir si los campos ocultos participan en la extracción mediante la configuración **Extraer campos ocultos**.
* **Mayor rapidez en lotes grandes.** Los reinicios masivos de documentos, las importaciones de CSV de datos maestros, el procesamiento de PDF y la extracción de campos basada en reglas reciben mejoras de rendimiento.
* **Extracción con IA más resistente.** Los tiempos de espera se informan como tiempos de espera, y los fallos de modelos compatibles pueden recurrir a otro modelo disponible. Correcciones adicionales gestionan claves repetidas en la salida de IA, sinónimos de campos configurados y definiciones de tablas guardadas vacías.
* **Conservar el valor recién introducido.** Guardar una celda de tabla sin hacer clic primero en otro lugar conserva el valor escrito. Las fechas con nombres de mes confundidos por OCR se gestionan de forma más fiable.

## Conciliación, aprobación y exportación de pedidos

La [guía de Reglas de conciliación de pedidos](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) explica cómo activar la conciliación basada en reglas, configurar tipos de conciliación y tolerancias, establecer el orden de ejecución y gestionar versiones de reglas.

* **Conciliar en cualquier dirección.** Seleccione líneas de documento y conéctelas a líneas de pedido, o comience desde las líneas del pedido. Esto resulta útil cuando muchas líneas de albarán se relacionan con una sola línea de pedido.
* **Conservar el detalle de líneas de uno a muchos.** Una configuración de conciliación ahora puede retener una sublínea individual para cada línea de documento cuando varias líneas concuerdan con una línea de pedido. Esta opción está desactivada de forma predeterminada. La exportación genérica por API puede agrupar solicitudes por columnas de línea configuradas, admitiendo entregas o contenedores que necesitan registros de destino separados.
* **Configurar el respaldo de última línea.** Las organizaciones pueden controlar si la línea restante de documento y pedido puede conciliarse mediante el respaldo de línea única.
* **Conciliación y visualización más precisas.** Las correcciones preservan la base de precio correcta para conciliaciones con conversión de envases, heredan el estado de la línea de pedido en filas de programación y muestran cantidades recibidas desde líneas de recepción.
* **Evitar la aprobación prematura y el trabajo duplicado.** La aprobación final se bloquea mientras existan discrepancias de pedido relevantes sin aprobar. La ejecución repetida del flujo de trabajo no crea otra tarea abierta para el mismo grupo, y las comprobaciones de exportación duplicada se ejecutan antes de la aprobación.
* **Separar Exported de Finished.** Las acciones de exportación pueden seleccionar el estado tras una exportación exitosa. **Exported** tiene su propia insignia en el panel. Las organizaciones que activan el bloqueo de documento terminado impiden que los flujos de trabajo ordinarios o los reinicios vuelvan a abrir documentos terminados; las anulaciones autorizadas se registran.
* **Resolución de problemas de flujo de trabajo más clara.** Un filtro del panel encuentra documentos retenidos por el límite de ejecución del flujo de trabajo. Las ejecuciones del flujo de trabajo pueden inspeccionarse en una ventana emergente, y un cambio de estado rechazado indica el estado del documento.
* **Correcciones adicionales de exportación.** Se ajustan los reintentos de validación y aprobación de M3, y las configuraciones de exportación de proveedores condicionales se gestionan correctamente.

## Usabilidad y acceso cotidianos

* **Navegación más fiable.** Las direcciones de documentos actualizadas tienen redirecciones para enlaces antiguos. Los enlaces profundos de NOVA mantienen el canal previsto durante el inicio de sesión, y el progreso de carga muestra qué parte de la página se está preparando.
* **Preferencias de trabajo personales.** El orden de columnas de pedido se guarda por usuario, y la pantalla de aprobación recuerda el panel lateral abierto del usuario.
* **Vistas de tareas y paneles más fiables.** Las tareas sin asignatario pueden listarse, abrirse y asignarse. El tablero de tareas se recarga cuando la organización seleccionada está lista, los intervalos de fecha personalizados del panel se aplican correctamente y se evitan filas de documento duplicadas.
* **Etiquetas y registros mejorados.** Los administradores pueden editar claves de traducción de campos y columnas de tabla. Las columnas del registro de documentos pueden redimensionarse, las columnas personalizadas del panel gestionan identificadores de campos con mayúsculas y minúsculas, y las etiquetas y nombres de archivo largos se ajustan de forma más consistente.
* **Alcance de las notificaciones.** Las reglas de correo electrónico de estado de documento pueden limitarse a una suborganización.
* **Incorporación de proveedores.** Los enlaces mágicos de registro del Portal de proveedores siguen siendo válidos durante **21 días en lugar de 7 días**. Los administradores también pueden configurar el encabezado de error de carga para un campo de archivo en un diseño de proveedor.
* **Fiabilidad del inicio de sesión.** El inicio de sesión con SAML ya no reutiliza sesiones caducadas o revocadas. El inicio de sesión de gestión admite el paso de MFA requerido, y las membresías inactivas no pueden recibir una nueva invitación para establecer una contraseña.
* **Imágenes del Tablero de ideas.** Las imágenes cargadas se almacenan y se sirven por separado de la descripción de la idea, lo que mejora el manejo de imágenes.
* **Cambio controlado de canal.** La configuración de Canal de publicación puede establecerse en solo lectura cuando el cambio no está habilitado para el entorno. Consulte el anuncio de la versión para conocer la disponibilidad.

## Asistentes conectados y herramientas de integración

Para organizaciones y socios que utilizan la integración MCP de DocBits, NOVA añade herramientas para listar reglas de validación resueltas, probar una regla contra un documento sin guardar cambios y explicar la evidencia de ejecución de reglas almacenada. Los asistentes conectados también pueden listar solicitudes de mejora y enviar una aprobación autorizada por un administrador a través del mismo proceso de revisión que la aplicación web. Se aplican los permisos existentes de organización y documento.

## Capacidades ya presentes en VESTA

NOVA también incorpora la funcionalidad que se enumera a continuación. Donde el acceso estaba previamente limitado a la beta de VESTA, la disponibilidad regular forma parte de esta versión de NOVA y está prevista para el hotfix de VESTA del 11 de noviembre de 2026. La lista describe la funcionalidad anterior, junto con los cambios de disponibilidad y las mejoras explicadas anteriormente:

* El Asistente de configuración original, su búsqueda de documentación, el flujo básico de vista previa/confirmación/deshacer y las alertas proactivas de salud de importación por email/FTP.
* Los niveles de IA Fast, Full, Nexus y Auto y la configuración de modo de visión.
* La Verificación de campos de cabecera y el informe original de origen de valores.
* La primera versión de Touchless Intelligence, el diagnóstico de proveedores, el análisis masivo y el diagrama de decisión de órdenes de compra.
* Los motores subyacentes de reglas de validación, transformación y selección de diseño, las transformaciones tras la búsqueda de datos maestros y el registro básico de ejecución de reglas.
* Mejoras anteriores de búsqueda en el panel, MFA, dominios de email de organización verificados, tolerancia de cargos y el aumento del límite de ejecución de flujos de trabajo a 50.

Consulte el [hotfix de VESTA del 14 de octubre](incremental-updates-14-october-2026.md), el [hotfix del 15 de septiembre](incremental-updates-15-september-2026.md) y las [notas de versión anteriores](README.md#vesta-hotfix-releases) para conocer el historial de versiones de VESTA.

## Versiones de servicios de NOVA

Estas son las versiones y marcas de tiempo de despliegue en la **instantánea del 16 de octubre de 2026**. Las marcas de tiempo describen despliegues individuales de servicios, no una fecha de lanzamiento separada para cada funcionalidad.

| Servicio | Versión | Marca de tiempo de despliegue |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Los números de versión avanzan de forma independiente en los dos canales. Un número mayor no significa por sí mismo que un servicio tenga una nueva funcionalidad para el cliente. Los cambios revisados de Auto Accounting, Barcode, Docnet, Fulltext, OCR y Operator son cambios de mantenimiento o de fiabilidad de procesamiento; no introducen un flujo de trabajo de cliente separado en esta comparación. Las actualizaciones de Auth Bridge mejoran la fiabilidad de la sincronización de cuentas entre regiones.
