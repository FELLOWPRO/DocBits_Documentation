# Notas de versión de DocBits — 12–25 de agosto de 2026

_Lo que cambia en la actualización de producción de DocBits del 25 de agosto de
2026, que abarca todo lo ocurrido desde la versión del 12 de agosto. Cada
servicio indica la versión que se despliega y, a continuación, las novedades o
correcciones en lenguaje sencillo. Los servicios que no aparecen en la lista no
tuvieron cambios visibles para el cliente._

---

## Aspectos destacados

- **Aislamiento más estricto entre organizaciones.** Una revisión de seguridad
  cerró varios puntos donde los datos de una organización podían leerse o
  escribirse desde otra: los scripts de documentos, las listas de usuarios de
  suborganizaciones, las pertenencias a grupos y el token de procesamiento que
  un documento lleva a lo largo del pipeline se comprueban ahora contra la
  organización del solicitante. Las aprobaciones también aplican correctamente
  el principio de cuatro ojos: el segundo aprobador debe ser una persona
  distinta del primero.
- **Los documentos dejan de quedarse atascados.** Se corrigieron cuatro causas
  distintas de documentos colgados para siempre: exportaciones que permanecían
  en "Exportando" tras ser denegadas, reinicios que se congelaban cuando
  fallaba un paso de procesamiento, divisiones por código de barras que nunca
  informaban de vuelta y la pantalla de contabilidad colgada en "Preparando…".
  En cada caso, el documento ahora termina o muestra un error real sobre el que
  se puede actuar.
- **Las notas de crédito se reconocen como notas de crédito.** Las notas de
  crédito XRechnung 3.0, 3.0.1 y 3.0.2 en sintaxis CII, las notas de crédito
  CII puras y los documentos ZUGFeRD 2.4 / Factur-X 1.08 se clasifican ahora
  correctamente, con el total leído del campo adecuado. Los documentos
  escaneados que mencionan tanto "factura" como "nota de crédito" se resuelven
  según qué palabra clave está más cerca del tipo de documento, y los importes
  vuelven a ser positivos al reclasificar una nota de crédito de nuevo como
  factura.
- **La coincidencia de PO hace cálculos fiables.** Las tolerancias se comparan
  como decimales exactos en lugar de valores de coma flotante, se basan en el
  valor de la orden de compra, y las facturas que hacen referencia a varias
  órdenes de compra se comparan contra todas ellas. Las columnas que nunca se
  mapearon ya no distorsionan la comprobación del importe de línea y, cuando
  faltan columnas obligatorias, el error las nombra.
- **Las ejecuciones de flujos de trabajo conservan su trabajo.** Un flujo de
  trabajo que escribe el valor de un campo lo escribe ahora en el documento de
  forma que una exportación posterior no pueda revertirlo silenciosamente. Los
  disparadores reintentados ya no descartan lo que la ejecución ya había
  hecho, y dos disparadores que actúan sobre el mismo documento se ponen en
  cola en lugar de robarse el bloqueo mutuamente.
- **Los correos de restablecimiento de contraseña se envían de nuevo.** Nunca
  salían del servidor, sin aviso alguno. El formulario de restablecimiento
  también muestra una respuesta real tras el envío, y la respuesta ya no
  revela si existe una cuenta.

---

## Web App — `10.55.0`

### Inicio de sesión y cuentas

- El restablecimiento de contraseña vuelve a funcionar de principio a fin: el
  correo llega, el formulario confirma el envío y la respuesta es la misma
  tanto si la dirección tiene cuenta como si no.
- Si su organización exige la inscripción en la autenticación de dos factores,
  la pantalla de inicio de sesión ahora lo indica en lugar de fallar sin
  mensaje.
- Los administradores ya no pueden activar la obligatoriedad de MFA para toda
  la organización antes de que la inscripción desde el inicio de sesión esté
  disponible, lo que antes podía dejar a usuarios sin acceso.

### Pantalla de validación

- El control deslizante de zoom llega ahora hasta el 150 % (antes se detenía
  en el 80 %), y hacer zoom en una tabla funciona más allá del ancho del
  contenedor en lugar de no hacer nada.
- Los campos de importe vacíos cuentan como 0 en lugar de lanzar un mensaje de
  error, y un doble clic en la imagen del documento se ignora cuando no hay
  ningún campo seleccionado.
- El banner que se muestra cuando otra sesión tiene el bloqueo del documento
  no tenía texto; ahora se explica. Etiquetar una tabla ya no dispara una
  falsa advertencia de "el documento fue modificado externamente" por su
  propio cambio.
- En la tabla de IA, un remapeo de columna que desmapearía otra columna pide
  confirmación primero, y los valores que no son números se marcan en las
  columnas AMOUNT y NUMBER.
- La pestaña "Tabla extraída" vuelve a enlazar con el entrenamiento manual de
  tablas cuando está vacía.
- Los números de artículo en la tabla de líneas de Compare se muestran como
  identificadores, no redondeados como importes.
- Los campos de aprobador resuelven los ids de usuario y de grupo a nombres,
  de modo que nunca muestran un id en bruto ni quedan vacíos. Las fechas
  límite de las tareas se convierten a través de una única ruta consciente de
  UTC, por lo que todos los usuarios ven la misma fecha.
- Los documentos devueltos a validación muestran un indicador de carga en
  lugar de una pantalla muerta mientras se preparan.

### Contabilidad

- Las líneas divididas conservan su signo % tras pulsar Enter, y el 0 % se
  acepta como valor.
- En el filtro de cuentas, Enter confirma la primera cuenta coincidente en
  lugar de no hacer nada.
- Los caracteres de flexdimension se mapean por id de dimensión, de modo que
  las dimensiones aterrizan en la columna correcta aunque el orden difiera.
- Una preparación contable fallida se recupera con un mensaje de error en
  lugar de quedarse colgada en "Preparando…" para siempre, y reabrir un
  documento ya no sirve datos obsoletos del anterior.

### Coincidencia de PO

- Abrir PO Matching sin tener mapeadas todas las columnas obligatorias vuelve
  a ser posible; cuando falta algo necesario, el mensaje nombra las columnas
  exactas.
- Las columnas que no están mapeadas a nada se ocultan al abrir la pantalla,
  tras preguntarle una vez, y ya no fluyen al cálculo del importe de línea.
- La cantidad coincidente se actualiza tras guardar, y la ventana emergente de
  columnas faltantes le dirige a Validación de Campos, donde puede
  corregirlo.

### Dashboard y búsqueda

- Las columnas basadas en desplegables (tipo de factura, estado y similares)
  muestran su etiqueta en el idioma de su interfaz en lugar del valor
  almacenado en bruto.
- La búsqueda de texto libre acepta paréntesis como texto normal; antes
  rechazaba la consulta. El operador de filtro "distinto de" permanece
  seleccionado, y editar un filtro a mano ya no corrompe el nombre del campo.
- Seleccionar una suborganización en la búsqueda rápida inserta su nombre, no
  su uuid, y el autocompletado de suborganizaciones ya no muestra duplicados.
- El dashboard puede recuperar ahora hasta 10.000 documentos por ventana de
  búsqueda, de modo que los conjuntos de resultados grandes se paginan
  correctamente.
- El panel de documentos duplicados muestra las mismas columnas resueltas que
  la lista principal, y los valores de filtro de proveedor con varias palabras
  sobreviven al pulsar Enter.

### Tareas

- El correo de asignación se envía cuando se asigna una tarea, una sola vez.
  Editar una tarea o marcarla como hecha ya no lo reenvía, y la fecha de
  "asignado el" sigue siendo la fecha de la asignación. Los correos de tareas
  también se muestran correctamente en Outlook.

### Workflow Builder

- La búsqueda, el orden y la paginación de la lista de flujos de trabajo se
  mantienen coherentes mientras filtra.
- El interruptor "ejecutar flujo de trabajo al cambiar" del constructor de
  layouts ahora condiciona realmente la ejecución, y activarlo exige elegir un
  flujo de trabajo.

### Configuración y administración

- El enlace de descarga de WatchDog y el comando de configuración apuntan al
  entorno en el que se encuentra, no siempre a producción.
- Árboles de decisión: el campo de documento seleccionado permanece resaltado
  cuando el selector se vuelve a abrir, las etiquetas truncadas reciben un
  tooltip y se muestran nombres de usuario (no ids en bruto) al añadir una
  línea.
- La casilla de System Admin es editable al editar un usuario.
- Analytics: los Core Web Vitals se muestran a partir de los datos de medición
  reales, y la vista del servicio de registros funciona.
- "Use Default Template" en el gestor de layouts copia el layout
  predeterminado como corresponde.
- Las etiquetas de campos personalizados ya no sobrescriben las traducciones
  incluidas de los campos estándar.
- Cotizaciones del portal de proveedores: el envío de una cotización con un
  valor REF1 fuera de la lista permitida se bloquea.
- MediOrder recibe detección de documentos duplicados en su pantalla de
  validación.

## API Service — `12.82.3`

### Seguridad y aislamiento de organizaciones

- El cambio de organización activa se valida contra su pertenencia real y
  falla de forma segura, y se cerró un endpoint interno de pruebas del que
  podía abusarse para cruzar organizaciones.
- Los scripts de documentos ya no pueden leerse ni sobrescribirse entre
  organizaciones, ni mediante la llamada de aplicar al documento ni mediante
  un id de versión ajeno al guardar.
- Las listas de usuarios de suborganizaciones y las listas de miembros de
  grupos solo devuelven personas de la organización del solicitante, y añadir
  varios usuarios a un grupo a la vez ya no descarta todos menos el primero.
- Una credencial de la organización equivocada se rechaza antes de que pueda
  convertirse en el token de procesamiento de un documento, y las consultas de
  búsqueda de texto completo se ejecutan como el usuario que llama y no como
  una identidad de servicio.
- Se aplica la aprobación a cuatro ojos: el segundo aprobador debe ser
  distinto de la persona que aprobó primero.
- La lista del PO Dashboard en vivo se limita a las suborganizaciones del
  usuario.

### Pipeline de documentos

- Los documentos denegados para exportación ya no se quedan en "Exportando"
  para siempre, y los errores de exportación siempre llevan un mensaje en
  lugar de uno vacío.
- Cuando un paso de procesamiento falla de forma abrupta, el documento pasa a
  un estado de error en lugar de quedarse atascado en "reinicio en curso" sin
  salida posible.
- Una división por código de barras que falla o agota el tiempo marca el
  documento como Error en lugar de mostrar "En ejecución" indefinidamente, y
  una división que no produce documentos hijos conserva el padre y lo marca en
  lugar de eliminarlo todo.
- Un reintento fallido ya no puede sobrescribir un documento que entretanto
  terminó de procesarse.
- Los documentos reiniciados sin interacción del usuario y los hijos de una
  división se ejecutan ahora con un token de organización duradero, de modo
  que el procesamiento de larga duración no muere con una sesión caducada.
- Una respuesta vacía de plantillas de layout ya no se almacena en caché
  durante seis horas, lo que antes hacía desaparecer los layouts hasta que la
  caché expiraba.

### Extracción y documentos electrónicos

- Los importes escritos con el signo menos al final ("100,00-") se interpretan
  como negativos en lugar de descartarse.
- Los documentos suizos se detectan como suizos (CHF, números de IVA CHE, IBAN
  CH) en lugar de asumir por defecto las convenciones alemanas, y las fechas
  escritas con guiones tipográficos se interpretan correctamente.
- Las notas de crédito XRechnung 3.0, 3.0.1 y 3.0.2 en sintaxis CII se
  clasifican como notas de crédito con el total leído del campo de total
  general; lo mismo ocurre con las notas de crédito CII puras. Una versión
  declarada de ZUGFeRD 2.4 / Factur-X 1.08 prevalece sobre el identificador de
  perfil genérico, y los tipos XRechnung sin sintaxis declarada se resuelven a
  su equivalente UBL o CII en lugar de fallar.
- Los campos desplegables (lista de valores) como Tax Country y Tax Code
  conservan su valor a través de la transformación de campos; antes se
  vaciaban.
- Extracción de tablas: un fallo en una columna de solo números se queda en
  esa columna en lugar de tumbar toda la tabla, la extracción de tablas con IA
  recibe un tiempo límite que sobrevive a ejecuciones de varios lotes, y se
  corrigieron dos fallos con formas de tabla inusuales (filas sin posiciones
  de página, número de columnas irregular).
- Los patrones de las reglas de origen coinciden sin distinguir mayúsculas de
  minúsculas.

### Exportación

- Una comprobación de impuestos que falla durante la vista previa de la
  exportación devuelve un error legible en lugar de un error de servidor, en
  ambos endpoints de vista previa.
- La exportación SFTP puede enviar el documento original junto con el
  convertido.
- Cuando existen configuraciones de exportación en varios niveles, la más
  específica gana de forma consistente.
- Las exportaciones BOD pueden llevar atributos de tipo de columna mediante
  mapeo.

### Importación y datos maestros

- El registro de importación de correo está completo: los correos entrantes
  rechazados y fallidos siempre reciben una fila de registro con un motivo
  preciso. Se acabaron los descartes silenciosos.
- Las importaciones BOD de órdenes de compra mantienen las sublíneas unidas a
  la línea correcta; un indicador arrastrado las unía antes a la equivocada.
- Importar un CSV con varios proveedores nuevos funciona (sus ids generados ya
  no colisionan), los alias de condiciones de descuento por pronto pago se
  importan y respetan el ajuste "en caso de conflicto", y la opción IGNORE en
  caso de conflicto se aplica más allá de los proveedores.
- La sugerencia de proveedor (TF-IDF) conserva su id de proveedor cuando se
  actualiza una preferencia, de modo que las sugerencias dejan de apuntar a la
  nada.

### Otras correcciones

- Las filas del dashboard resuelven las etiquetas de los desplegables en el
  idioma del usuario, sin bloquear la petición.
- Tras editar campos, el estado de coincidencia de PO se actualiza en lugar de
  mostrar el estado previo a la edición.
- Los documentos de Purchase Order Change reciben cinco campos con paridad con
  Purchase Order y un layout de validación de campos predeterminado.
- Las respuestas de error de 152 endpoints devuelven mensajes legibles en
  lugar de objetos de excepción en bruto, y la página de analítica de
  registros ya no responde con 502 para organizaciones sin índice de
  registros.

## Auth Service — `1.77.9`

- Los correos de restablecimiento de contraseña nunca se enviaban, sin aviso
  alguno; corregido, junto con el problema de seguridad de hilos subyacente.
- Un refresh token reutilizado se rechaza: la comprobación autoritativa en la
  base de datos se ejecuta ahora en todos los casos, en lugar de omitirse con
  un acierto de caché.
- Autenticación de dos factores: se puede registrar una aplicación de
  autenticación junto a los códigos por correo electrónico, y eliminar la
  última clave de acceso o regenerar los códigos de respaldo requiere antes un
  segundo factor reciente.
- Un id de suborganización válido ya no se rechaza con "Organization not
  found", y una clave de API creada en una suborganización resuelve su usuario
  técnico desde esa suborganización.
- Editar una organización valida el id de partner y ya no restablece el tipo
  de organización como efecto secundario.
- Los "tokens restantes" de la vista de suscripción se anclan al año de
  contrato, no al año natural.

## Auth Bridge Service — `0.5.7`

- La replicación de cuentas entre las regiones de la UE y EE. UU. se recupera
  por sí sola. Un flujo de replicación caído se vuelve a enganchar en el
  sitio, la replicación sigue fluyendo mientras se ejecuta una reconciliación,
  y la memoria de la reconciliación está acotada, de modo que el servicio deja
  de reiniciarse en bucle con tablas grandes.

## Barcode Service — `1.18.7`

- La lectura de códigos de barras se ejecuta con un límite de tiempo e informa
  de un timeout en lugar de colgarse, lo que antes dejaba el documento
  atascado en procesamiento.

## Docflow Service — `2.9.8`

- Los valores de campo escritos por una tarjeta de flujo de trabajo se
  guardan en el documento en sus dos representaciones almacenadas, de modo que
  una exportación posterior ya no los revierte.
- Un disparador reintentado conserva el trabajo que la ejecución ya había
  hecho, los disparadores que compiten por el mismo documento se ponen en cola
  en lugar de robarse el bloqueo, y un reintento escalado se coloca primero en
  la cola.
- Tarjetas de comparación de órdenes de compra: las tolerancias se comparan
  como decimales exactos y se basan en el valor de la orden de compra, las
  direcciones de comparación invertidas están disponibles como opciones, un
  asignado de grupo se informa como grupo en lugar de fallar en una
  comparación de id de usuario, los ids de asignación se comparan
  correctamente como UUIDs, las líneas con valores numéricos vacíos se omiten,
  y una comparación de "recibido" sin ningún dato de recepción informa de
  datos faltantes en lugar de fingir una coincidencia.
- La tarjeta Apply Decision Table se ha retirado.

## Email Service — `1.41.0`

- Las importaciones de Gmail recogen cada adjunto exactamente una vez; los
  duplicados por recogidas solapadas han desaparecido.
- El cursor de lectura de la importación solo avanza después de confirmarse
  una importación, de modo que un fallo a mitad de importación ya no puede
  saltarse correos.
- Cuando una configuración de importación se desactiva porque existe otra
  similar, esa desactivación es visible y se notifica, en lugar de ser
  silenciosa.

## Extraction Service — `1.54.5`

- Si un documento es una nota de crédito o una factura se resuelve según qué
  palabra clave está más cerca de la mención del tipo de documento, en lugar
  de ganar la primera coincidencia.
- Cuando varias interpretaciones de impuestos están dentro de la tolerancia,
  se prefiere la conciliación exacta sobre una aproximada.
- Tras un re-OCR forzado se restauran el tipo de documento y la configuración
  regional, de modo que la extracción y el entrenamiento de tablas vuelven a
  funcionar en documentos re-OCR.
- Los documentos sin tipo de documento ya no bloquean la búsqueda de reglas de
  tabla.

## FTP Service — `1.32.8`

- El escaneo de carpetas hace una sola operación de listado por carpeta con
  una profundidad acotada, de modo que las importaciones desde directorios FTP
  grandes son mucho más rápidas y dejan de agotar el tiempo de espera.

## Fulltext Service — `1.42.3`

- Los documentos cuyo payload de búsqueda almacenado no tenía campos extraídos
  se reindexan desde la base de datos, de modo que vuelven a aparecer en la
  búsqueda del dashboard.
- La ventana de búsqueda del dashboard admite hasta 10.000 documentos.
- Las búsquedas por facetas ya no fallan cuando la búsqueda semántica está
  activa.

## OCR Service — `1.10.7`

- El presupuesto de tiempo de OCR se dimensiona según el coste real por
  página, de modo que los documentos largos terminan en lugar de chocar con el
  límite del pipeline.

## PO Match Service — `1.59.8`

- Las líneas de tabla con cantidad cero se omiten en las comprobaciones de
  discrepancias en lugar de producir falsas discrepancias.
- Cuando faltan columnas obligatorias de coincidencia de PO, el resultado las
  nombra.
