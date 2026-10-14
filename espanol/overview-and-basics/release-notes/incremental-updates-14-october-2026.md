# Notas de versión de DocBits — 14 de octubre de 2026

_Lo que cambia en el hotfix de producción de DocBits del 14 de octubre de 2026
(versión R1.0.15), que abarca todo lo ocurrido desde el [hotfix del 15 de septiembre](incremental-updates-15-september-2026.md).
Cada servicio indica la versión que se despliega y, a continuación, las
novedades o correcciones en lenguaje sencillo. Los servicios que no aparecen en
la lista no tuvieron cambios visibles para el cliente._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/es.mp4" %}

---

## Aspectos destacados

- **El asistente de configuración.** Una barra de chat en cada página de
  configuración responde preguntas sobre la configuración de su organización,
  en su idioma y a partir de la documentación de DocBits. Lee el estado actual
  de sus ajustes y los explica (permisos de grupo, canales de importación,
  interruptores de órdenes de compra, contabilidad). Cuando le pide activar o
  desactivar algo, muestra primero una vista previa, espera su confirmación y
  ofrece deshacer el cambio. "Abrir ajuste" lleva directamente al ajuste,
  incluso dentro de una sección plegada, y lo resalta. Los administradores de la
  organización activan o desactivan el asistente en Información de la empresa.
  Solo responde preguntas sobre DocBits y nunca cambia nada sin confirmación.
- **Nuevos niveles de IA.** Los niveles Fast y Full funcionan con modelos
  nuevos. Un nuevo nivel Auto elige Fast o Full para cada documento, y Nexus
  Flash se une a Nexus. Un modo de visión (híbrido o automático) decide cuándo
  se envía también la imagen de la página. Las preferencias de modelo de IA
  guardadas pasan solas a los nuevos niveles, y las pantallas muestran solo los
  nombres de los niveles. "Usar IA" es un desplegable (Estándar, Sí, No) con una
  vista previa de lo que solicitará la extracción estructurada.
- **Comprobación de campos de cabecera.** La pantalla de validación tiene un
  botón "Comprobación de campos de cabecera" junto a Guardar. Su informe lista
  cada campo de cabecera con el origen del valor (IA, regla, script o datos
  maestros), en una tabla compacta con filtro de origen, búsqueda y ordenación,
  y con las mismas etiquetas de campo que la pantalla de validación. La ventana
  de origen muestra la procedencia de cada valor en una sola franja.
- **Seguridad del inicio de sesión y de la organización.** Un desafío de MFA
  puede usarse una sola vez en cada vía de inicio de sesión, y para registrar un
  autenticador hace falta el código del correo electrónico. Las organizaciones
  poseen una lista de dominios de correo verificados; un inicio de sesión social
  (por ejemplo, Microsoft) se une a la organización que incluye el dominio y
  nunca crea por sí mismo una organización, un usuario ni una suscripción. Solo
  los administradores de la organización cambian las preferencias de la
  organización y escriben o aprueban reglas de coincidencia de órdenes de
  compra. Las respuestas en caché ya no pueden filtrarse entre organizaciones.
- **Coincidencia de órdenes de compra y cargos.** Los cargos que la orden de
  compra espera en cero tienen un mínimo absoluto, la tolerancia de cargos
  también se aplica a los cargos que la orden no presupuesta, y un campo puede
  listar varios elementos de costeo cuyos importes se reparten
  proporcionalmente a la orden de compra. Una columna de coincidencia puede
  llevar un indicador "permitir discrepancia". Las tarjetas de flujo de trabajo
  comparan los cargos por lista, y el límite de ejecución de flujos de trabajo
  sube de 30 a 50.
- **Menos cifras erróneas.** Los importes se muestran en el formato personal de
  cada usuario (incluidos Suiza y Eslovenia), los valores que solo son fecha
  conservan su día natural en cualquier zona horaria, la ecuación del total de
  EE. UU. tiene en cuenta los importes adicionales y las facturas con varios
  impuestos, y los documentos con importes de cabecera de 0,00 ya no caen en la
  pasada de candidatos equivocada.

---

## También corregido en esta versión

- El dashboard ya no se queda vacío cuando una condición de carrera fija el
  filtro de suborganización al ID de la organización y excluye así todos los
  documentos.
- Los valores de dimensión vuelven a poder seleccionarse para todos los
  usuarios.
- Se corrigió un error de carga notificado por un cliente.
- "Coincidencia sobre el total" funciona para los proveedores cuya factura tiene
  una sola línea, y para las configuraciones de proveedor que lo notificaron.
- Documentos electrónicos SPS: se ajustan los cargos del 810, se actualiza el
  layout de cargos del 855 y se corrige el logotipo del cliente en la vista
  previa del documento electrónico.

---

## Web App — `10.78.9.4`

**Asistente de configuración**
- Un panel de chat lateral derecho con interruptor está disponible en todas las
  páginas de configuración. La conversación se mantiene al cambiar de página,
  está limitada a 20 mensajes y muestra los cambios aplicados con la opción de
  deshacer.
- Le saluda con preguntas adecuadas a la página de configuración actual y
  muestra tarjetas de ajuste con un interruptor de activación. Esc cierra primero
  los menús, Detener interrumpe una respuesta en curso, y las capturas de
  pantalla de las respuestas se abren en un visor ampliado.
- Al aplicar un cambio se abre un cuadro de diálogo con vista previa,
  confirmación y deshacer.
- Todos los ajustes pueden buscarse desde la barra lateral, y el ajuste
  encontrado se resalta con otro color. "Abrir ajuste" se desplaza hasta el
  destino dentro de un acordeón plegado.
- Un interruptor del asistente para administradores de la organización está en
  Información de la empresa.
- El consejo de IA se atribuye a Nova, y solo aparecen nombres de niveles, nunca
  ID de modelos.

**Pantalla de validación y gestión de documentos**
- Nuevo botón "Comprobación de campos de cabecera" con informe, origen por campo
  y página de ayuda (véase Aspectos destacados). Las etiquetas de origen y los
  chips de estado se mantienen dentro de sus celdas.
- Desaparecen las insignias de texto "de datos maestros" junto a las etiquetas
  de campo; esa información está ahora en la ventana de origen.
- Se ejecuta en todas partes una única validación de campos compartida, lo que
  elimina el error genérico "Uno o más campos necesitan validación" tras Auto
  Accounting.
- Los tooltips de los botones de la ventana de campo (Eliminar, Borrar,
  Confirmar) indican qué hace cada uno antes de pulsarlo.
- Una fila optimista muestra ahora lo que se almacenó, no lo que se escribió.
  Una reasignación de columnas solo pide confirmación cuando una columna visible
  pierde su asignación.
- Las páginas que superan el límite de páginas de OCR son de solo lectura y
  están marcadas, también en el visor de Auto Accounting. El antiguo panel de
  restricción de páginas de importación se retira.
- Aparece una tabla de OC para cada número de orden de compra de un campo de
  cabecera con varias OC, y el Layout Builder rotula las pestañas de OC a partir
  de la clave de la tabla de OC y ya no informa de que el módulo está
  desactivado cuando la tabla de OC está activa.
- La tarjeta de propuesta muestra la tolerancia en lugar de `[object Object]`, y
  la pantalla de comparación de aprobación deja de redondear las columnas de
  comparación configuradas (números de artículo).

**Cuentas, configuración y errores**
- Cada aviso de error y cada error de inicio de sesión muestra el ID de traza de
  la petición fallida, para que el soporte pueda localizarla. Los errores del
  WebSocket del dashboard rechazan exactamente la petición que nombran.
- Información de la empresa lista los dominios de correo de la organización.
- Los administradores pueden reenviar el correo "Establezca su contraseña" desde
  la página de usuario.
- Los administradores globales fijan el inicio del contrato en la tabla de
  suscripción.
- Los administradores de la organización ven la pestaña Executive Dashboard y
  los botones de añadir y eliminar XSLT. Los miembros guardan layouts como
  preferencia propia.
- Una sesión sin organización recibe un error claro y el selector de
  organización en lugar de un dashboard vacío.
- Los importes siguen el formato numérico personal del usuario, y los valores
  que solo son fecha conservan su día en cualquier zona horaria.
- Los datos maestros envían los ID de suborganización solo cuando difieren del
  ID de la organización, y las cabeceras personalizadas de datos maestros se
  envían como cabeceras.
- La máscara de Tablas ya no recorta el desplegable "Usar IA", el texto de
  ayuda de IA ya no tapa la línea de entrenamiento, y la tabla de IA conserva su
  botón Aplicar directo, con una comprobación de cabecera solo con icono y un
  mensaje de licencia.
- Los iconos de extracción de tablas vuelven a mostrarse tras retirar la antigua
  fuente de iconos.

**Tablero de tareas**
- El tablero carga su primera página con menos peticiones duplicadas, Intro
  ejecuta la búsqueda de inmediato, las respuestas tardías se asocian a la
  búsqueda correcta, el pie muestra el recuento real de resultados en lugar de
  la capacidad de la página, y una eliminación iniciada en una organización se
  cancela antes de enviarse si cambia de organización.

---

## API Service — `12.83.293`

**Asistente de configuración y MCP**
- Punto de acceso de chat con salvaguardas: solo preguntas sobre DocBits,
  ningún cambio sin confirmación, las preguntas poco claras o sobre el propio
  asistente reciben ayuda en lugar de un rechazo, y las respuestas transmiten
  primero las tarjetas y después el texto.
- Bloques de solo lectura para cada área de configuración (permisos de grupo,
  canales de importación, coincidencia de OC, contabilidad, dominios de correo),
  un catálogo de enlaces directos con una herramienta de búsqueda de ajustes, y
  búsqueda en la documentación de DocBits con imágenes.
- Flujo de aplicación de la primera fase: vista previa, confirmación y deshacer
  para los ajustes compatibles, una única regla de ámbito para los tres, a
  prueba de doble confirmación y de caducidad.
- Las herramientas MCP nunca leen archivos del servidor en modo remoto, y las
  herramientas de fixtures y de laboratorio solo se ejecutan en dev.

**IA**
- Nuevos modelos detrás de los niveles Fast y Full, el nivel Auto, Nexus Flash
  y la preferencia del modo de visión. Las preferencias `AI_MODEL` guardadas
  pasan a los nuevos niveles.
- "Usar IA" documenta lo que solicita la extracción estructurada.

**Seguridad y aislamiento**
- Solo los administradores de la organización cambian las preferencias de la
  organización.
- La llamada `/accounting/rebuild` entrena solo la organización de quien llama,
  falla de forma segura si la consulta de la organización falla y responde 400
  ante un ID incorrecto.
- El renderizado de XSLT, XML y PDF deniega el acceso a archivos y a la red, no
  resuelve inclusiones externas, y los bytes de la factura se sanean antes de
  llegar al transformador. Las vistas previas de PDF renderizadas solo admiten
  hosts de imágenes de confianza.
- Las claves de caché incluyen la organización y el mismo identificador siempre
  da la misma clave, de modo que un ID de organización ajeno ya no puede leer
  datos en caché. Se eliminan los borrados de caché de todo el dashboard de la
  organización en cada cambio de documento.
- La lista de dominios de correo de la organización se transmite a Auth.

**Coincidencia de órdenes de compra y exportación**
- Un campo puede listar varios elementos de costeo cuyos importes se reparten
  proporcionalmente a la OC.
- Los sustitutos de aprobación se vinculan a la solicitud de aprobación activa,
  los guardados de aprobaciones recuperadas ya no bloquean, y un documento
  pendiente de aprobación se rechaza para la exportación.
- La anotación PDF/A conserva el catálogo y el XML incrustado, de modo que las
  facturas electrónicas mantienen su XML tras la anotación. Las facturas UBL con
  el CustomizationID EN 16931 simple se clasifican (red de facturas
  electrónicas).
- GRPR se redondea a los 6 decimales que acepta M3. Los factores de conversión
  de la unidad de medida base se añaden a la línea congelada.
- Se respetan los entrenamientos y las reglas de formato eliminados de forma
  lógica, y `update_document_fields` de MCP ya no confirma una escritura que
  perdió. `get_table_rules` responde con un fallo tipado, y una carga de
  traducciones vacía usa su valor de respaldo.
- Los importes eslovenos usan `sl_SI` y las preferencias guardadas se migran.
  Las etiquetas de clasificación personalizadas enviadas como ID UUID se
  resuelven. Los dashboards compartidos conservan `created_by` y la lista de
  usuarios compartidos al actualizarse.
- Los marcos de error del dashboard incluyen el `request_id` de la petición, y
  cada respuesta JSON fallida incluye un ID de traza.
- El sistema reinicia solo los workers en mal estado en lugar de toda la flota
  de la API y comprueba correctamente la lista de tareas registradas. Se vuelve
  a consumir la cola del monitor de bloqueos.

---

## Auth Service — `1.78.49`

- Un desafío de autenticación multifactor es de un solo uso en cada vía de
  inicio de sesión, no solo en el flujo MCP. Para registrarse hace falta el
  código del correo electrónico, no se emite ningún token de registro tras un
  inicio de sesión con contraseña compartida, y se avisa a los usuarios cuando
  se registra un factor.
- Las organizaciones poseen una lista de dominios de correo, cada uno asignable
  una sola vez. Un inicio de sesión social se une a la organización que incluye
  el dominio verificado, nunca inventa una organización, un usuario ni una
  suscripción, y rechaza sin nombrar a nadie mientras se avisa a los
  administradores. Se gestionan los dominios que devuelve Microsoft.
- Cada inicio de sesión rechazado incluye un ID de traza. Los administradores
  pueden reenviar el correo "Establezca su contraseña". El saldo del contrato
  lleva signo y el inicio del contrato queda auditado.

## Auth Bridge — `0.5.7`

- La replicación de cuentas entre la UE y EE. UU. mantiene alimentada su
  conexión durante la reconciliación, vuelve a enganchar por sí sola un slot de
  replicación caído, usa memoria acotada y trata un origen de replicación
  existente como éxito. El inicio de sesión entre regiones es más fiable.

## Docflow Service — `2.10.22`

- La tarjeta separada de precio unitario lee las definiciones de campo
  predeterminadas de la organización para los cargos y compara todos los
  elementos de costeo que lista un campo.
- El límite de ejecución de flujos de trabajo sube de 30 a 50, y las búsquedas
  en el registro de flujos de trabajo rechazan un ID que no sea un UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` informa de todas las columnas de tabla configuradas,
  incluidas las que están vacías.

## Extraction Service — `1.56.0.1`

- Niveles: nuevos modelos detrás de Fast y Full, Auto, Nexus Flash y un modo de
  visión. Las peticiones de visión al host de inferencia se mantienen por debajo
  de su límite de tamaño.
- La extracción de tablas con Nexus agrupa las páginas por lotes (dos por lote),
  ejecuta los lotes en paralelo con un tiempo de espera medido, reintenta los
  errores transitorios y divide un lote que superó el tiempo de espera. Los
  campos de cabecera se leen de todos los lotes.
- Totales de EE. UU.: los importes adicionales forman parte de la ecuación del
  total, el par 1 cuenta en la salvaguarda del par 2, los candidatos de baja
  puntuación se omiten cuando los impuestos no son cero, y "above" y "below"
  coinciden con etiquetas de varias palabras.
- Los campos identificadores reparan los caracteres que realmente aparecen, y
  los caracteres invisibles se tratan según lo que significan, de modo que una
  "O" ya no se convierte en un carácter extraño.

## Fulltext Service — `1.42.41`

- Nuevo índice para la documentación de DocBits, con puntos de acceso de
  ingesta y búsqueda, imágenes en las respuestas y un plazo para toda la
  búsqueda. Alimenta el asistente de configuración.

## PO Match Service — `1.59.48`

- Mínimo absoluto para los cargos que la orden de compra espera en cero, y
  tolerancia de cargos para los cargos que la orden no presupuesta.
- Una columna puede llevar un indicador "permitir discrepancia". Varios
  elementos de costeo por campo se reparten proporcionalmente.
- Solo los administradores de la organización escriben o aprueban reglas de
  coincidencia, y las condiciones de las reglas solo aceptan una gramática de
  expresiones de lista blanca.
- Los cambios de reglas pueden simularse frente a un conjunto de reglas de
  sustitución sin escribir, para las propuestas de cambio de Touchless. Las
  columnas adicionales de OC que se deben comparar se leen del atributo del tipo
  de documento, con una migración de la antigua preferencia.

---

_Sin cambios en esta versión: Auto Accounting, Barcode, E-Mail, FTP, Ideas, OCR,
Operator. FTP y Operator solo incluyen mantenimiento interno._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
