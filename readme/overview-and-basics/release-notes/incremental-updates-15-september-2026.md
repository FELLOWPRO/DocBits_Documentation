# Notas de versión de DocBits — 15 de septiembre de 2026

_Lo que cambia en el hotfix de producción de DocBits del 15 de septiembre de
2026 (versión R1.0.13), que abarca todo lo ocurrido desde la versión del 1 de
septiembre. Cada servicio indica la versión que se despliega y, a continuación,
las novedades o correcciones en lenguaje sencillo. Los servicios que no aparecen
en la lista no tuvieron cambios visibles para el cliente._

---

## Aspectos destacados

- **Un único conjunto de reglas para la búsqueda del dashboard.** `field=value`
  es ahora exactamente este valor en todos los motores de búsqueda,
  `field:value` significa contiene (con `value*` y `*value` para empieza por y
  termina en), y `field!=value` devuelve también los documentos que no tienen
  ningún valor. Una búsqueda sin chip es una búsqueda de subcadena en todos los
  campos, números de orden de compra, códigos de barras y números de requisición
  incluidos. El recuento de resultados, los mosaicos de estado y la paginación
  describen el mismo conjunto de documentos, y una búsqueda que alcanzó la
  ventana de resultados o se ejecutó sin el índice de texto completo lo indica
  en lugar de informar "completa". La conexión de búsqueda propia del dashboard
  (WebSocket) nunca llegaba antes al índice de texto completo; ahora sí.
- **Los proveedores se reconocen con más frecuencia.** Cuando un campo de
  búsqueda (número de identificación fiscal, IBAN, número de proveedor)
  coincide exactamente con un proveedor, se usa ese proveedor aunque un campo
  amplio como el nombre coincida con varios. Los documentos XRechnung CII y
  Facturae vuelven a incluir sus campos de proveedor. Cuando los datos maestros
  reemplazaron un valor extraído, la pantalla de validación lo indica y permite
  restaurar el original.
- **La coincidencia de órdenes de compra se explica por sí misma.** La pantalla
  indica por qué no hay coincidencia, el tooltip de discrepancia nombra la
  columna que falló, el historial de coincidencias lista las reglas de
  transformación que se ejecutaron, y los precios unitarios de la OC se derivan
  del importe neto. Las coincidencias manuales vuelven a funcionar para
  organizaciones sin regla de respaldo, las órdenes de compra eliminadas
  permanecen eliminadas, y una tarea de coincidencia terminada de forma forzada
  marca el documento como fallido en lugar de dejarlo aparcado en "Cola" para
  siempre.
- **Documentos atascados y errores falsos.** Las organizaciones que cargan
  documentos de forma continua veían sus documentos degradados a una prioridad
  de cola que nunca se atendía en horario laboral (866 documentos atascados en
  "nuevo" en un cliente). Un barrido de reintentos podía sobrescribir horas
  después un documento exportado correctamente con "error" y enviar el correo
  de error de exportación correspondiente. Esa vía está cerrada.
- **Touchless Intelligence.** La pestaña de Analytics que mide cuántos
  documentos pasan por DocBits sin intervención humana recibe su primera
  versión completa: clústeres de problemas con consejos de IA, análisis masivo,
  propuestas de cambio con vista previa, aplicación y deshacer, una página de
  proveedor con tendencia y ejemplos, un diagrama del flujo del pipeline por
  documento y un diagrama del conjunto de reglas de órdenes de compra que
  indica por qué un documento no pasó.
- **Más rápido donde los datos son grandes.** Los inicios de sesión en frío
  omiten la suma del libro de créditos que tardaba hasta 33 s, el desplegable
  de contabilidad funciona para organizaciones con más de 2.000 cuentas, la
  página de reglas de E-Documents pagina sus 1.600 reglas en el servidor en
  lugar de congelar el navegador, y Actualizar en el dashboard de órdenes de
  compra devuelve datos frescos en lugar de una lista en caché.
- **Seguridad.** Los source maps del frontend dejan de enviarse con cada
  despliegue, los filtros de búsqueda de datos maestros se vinculan como
  parámetros SQL en lugar de interpolarse, un token caducado se rechaza incluso
  con un acierto de caché, y la comprobación de organización del token de
  procesamiento se aplica con independencia de la capa que la precede.

---

## Web App — `10.66.3`

### Inicio de sesión y cuentas

- El inicio de sesión es más rápido. La comprobación de suscripción al iniciar
  sesión pedía el saldo completo de créditos, que sumaba millones de filas del
  libro de registro y a menudo superaba el tiempo de espera de 10 s del
  cliente. El inicio de sesión ahora solo pregunta si existe una suscripción;
  los saldos se siguen calculando en Configuración → Suscripción.
- Cambiar de región (UE ↔ EE. UU.) mantiene la sesión iniciada. La región de
  destino responde "invalid token" durante unos segundos hasta que la sesión se
  ha replicado, y dos rutas de código interpretaban eso como una sesión muerta.
- Se corrigió la superposición "Updating DocBits v10.59.3.1 → v10.59.3.1" que
  se recargaba sin fin en sandbox. Una recarga con la misma versión ya no
  muestra la superposición, el bucle está acotado por pestaña y un banner
  ofrece una recuperación manual si vuelve a ocurrir.
- Los administradores pueden conceder la pestaña Analytics Dashboard a roles
  concretos, y los cambios de rol se guardan de forma fiable.
- La casilla de System Admin puede marcarse en un usuario existente. Crear un
  administrador del sistema desde el frontend ahora tiene efecto; un trabajo de
  sincronización restablecía el indicador en cada ejecución.
- Configuración → Roles: la lista de miembros se renderiza en lugar de quedarse
  colgada tras un indicador de carga cuando el servidor responde con un error.
- Iniciar sesión en el servidor MCP de DocBits exige autenticación de dos
  factores y consentimiento de un solo uso.

### Dashboard y búsqueda

- Nuevas reglas de operadores, descritas también en la ventana emergente de
  ayuda de búsqueda: `=` es exactamente este valor (sin distinguir mayúsculas
  de minúsculas), `:` es contiene, `: value*` empieza por, `: *value` termina
  en, `!=` es todo lo que no sea exactamente este valor, incluidos los
  documentos sin valor. Las comillas solo agrupan un valor con espacios.
- Una frase entre comillas como `"Johnson and Johnson"` se busca como una sola
  frase. "and" y "or" dentro de comillas ya no se interpretan como conectores.
- Cuando una búsqueda simple no encuentra nada, el dashboard explica la regla y
  ofrece chips de un clic (`Invoice number : <term>`, `Purchase order : <term>`,
  `Supplier ID : <term>`).
- Una búsqueda con cero resultados reinicia el paginador y todos los recuentos
  de la página. Antes, la paginación conservaba el recuento de la búsqueda
  anterior.
- Los números de orden de compra, los números de pedido, los códigos de barras,
  los tipos de factura y los números de requisición se encuentran sin chip.

### Pantalla de validación

- Los valores que los datos maestros reemplazaron quedan marcados. Una insignia
  ámbar muestra el valor original y el actual, el conjunto de datos y cómo
  coincidió, y un botón restaura el valor extraído. Los valores confirmados por
  los datos maestros o completados desde la orden de compra reciben sus propias
  etiquetas. Antes, todos llevaban la insignia "Extracted using saved rules".
- El sello de aprobación se guarda incluso cuando la página ya lleva otra
  anotación. En ese caso, los documentos anotados descargados no incluían el
  sello.
- "Hide non mapped columns" conserva las columnas que entrenó a mano (por
  ejemplo, Item Number y Purchase Order).
- Guardar reglas de extracción funciona después de escribir un número de página
  y luego dibujar un recuadro para un campo. Esa secuencia hacía fallar el
  guardado.
- La extracción estructurada puede activarse por proveedor, en la ventana
  emergente tfidf de la pantalla de validación y como columna de solo lectura
  en Configuración → Clasificación y Extracción.
- Train Model se ejecuta en segundo plano. La pantalla muestra "entrenamiento
  iniciado", consulta el resultado periódicamente e informa del éxito o del
  fallo. Las organizaciones grandes recibían un error de gateway mientras el
  entrenamiento continuaba en el servidor.
- Modo oscuro: el cursor de tijeras en la pantalla de división y el conmutador
  de modo en la pantalla de Auto Accounting vuelven a ser legibles.

### Coincidencia de órdenes de compra

Los cambios anunciados en [Hotfixes 8 de septiembre de 2026](incremental-updates-8-september-2026.md)
llegan a producción con esta versión: la coincidencia se mantiene al guardar,
la coincidencia se ejecuta de nuevo cuando se corrige el número de OC, la
pantalla indica por qué no hay coincidencia y por qué una coincidencia no se
conservó, el historial de coincidencias muestra las reglas de transformación, y
el precio unitario de la OC se calcula a partir del importe neto. Además:

- El tooltip de discrepancia nombra la columna que no coincidió. Antes estaba
  vacío porque solo se registraban las columnas coincidentes, y la pantalla
  solo podía decir "Mismatched".
- El botón Auto Match también exporta el documento cuando "PO Auto Match and
  Export" está activado. Antes, la exportación solo ocurría cuando el documento
  se abría desde el dashboard mediante "PO Match".
- La ventana emergente de tolerancia de cantidad/precio unitario permanece
  abierta cuando el servidor rechaza el guardado, de modo que los valores
  introducidos no se pierden.
- El botón Actualizar del dashboard de órdenes de compra limpia la caché del
  servidor antes de recargar. Una orden de compra importada desde el ERP
  aparecía solo después de siete u ocho minutos.
- La página de reglas de coincidencia de OC dibuja el conjunto de reglas como
  un diagrama de flujo, y el historial de coincidencias se ha trasladado a la
  barra de herramientas de acciones.

### Contabilidad automática

- Las organizaciones con más de 2.000 cuentas buscan en la lista de cuentas en
  el servidor. El desplegable aparecía vacío en sandbox para esas
  organizaciones, y la carga de la página tardaba cinco segundos.
- Las cuentas a las que hace referencia un documento se resuelven por lotes: un
  documento de 100 líneas con dos divisiones por línea necesita 4 peticiones en
  lugar de 403.
- Los encabezados de las tablas de Auto Accounting y de OC siguen la etiqueta
  definida en el constructor de layouts en lugar de un texto fijo.

### Configuración

- Configuración → E-Documents → Reglas pagina, busca y ordena en el servidor el
  catálogo de 1.600 reglas. La pestaña renderizaba todas las reglas a la vez y
  congelaba el navegador. "Reset all" es una sola llamada en lugar de una por
  regla.
- La configuración avanzada del tipo de documento muestra el estado guardado de
  cada interruptor. Un `false` guardado, una tolerancia `0` o un selector vacío
  se reemplazaban por el valor predeterminado, y cambiar de tipo de documento
  dejaba atrás los valores del tipo anterior.
- Reglas de transformación: una acción "Set value" se guarda. El editor la
  enviaba bajo un nombre que el servidor rechaza.
- Lista de Valores: la barra lateral muestra una lista nueva y elimina una
  lista borrada sin recargar; las respuestas tardías de una lista anterior ya
  no sobrescriben la actual.
- El enlace de subtipos de documento se muestra en los tipos de documento
  estándar.
- El mapeo JPL de la exportación SMB se descarga como `.properties`, de modo
  que el archivo puede volver a cargarse. Se llamaba `.xml` y se rechazaba al
  volver a subirlo.

### Flujos de trabajo

- Renombrar un flujo de trabajo conserva los cambios en las tarjetas realizados
  en la misma sesión. Los flujos de trabajo nuevos se crean en una sola
  petición de guardado, y los cambios de nombre de plantillas se persisten.
- Un archivo de flujo de trabajo exportado contiene el sobre de exportación
  completo (versión, nombre, descripción). Los flujos de trabajo avanzados
  pueden importarse de nuevo; antes, el archivo perdía su versión, se leía como
  un flujo de trabajo estándar y se rechazaba.
- Los filtros de columna de la lista de flujos de trabajo se combinan con AND.
  Con un filtro de nombre y otro de fecha activos, filas que solo coincidían
  con el nombre se colaban en el resultado.
- Las fechas límite de las tareas usan el formato de fecha de su configuración
  de usuario en la lista, el tablero y la vista de detalle.

### Analytics: Touchless Intelligence

La pestaña Touchless (Analytics → Touchless) mide cuántos documentos pasan por
DocBits sin que una persona los toque, y por qué los demás no. Esta versión la
completa:

- **Clústeres de problemas con evidencia.** Los documentos que necesitaron
  intervención se agrupan por causa. Cada tarjeta de clúster nombra los campos,
  los códigos de validación y los mensajes de error en los que falla, y su
  proveedor, o indica que no hay ninguno. Los clústeres que DocBits puede
  corregir (una regla, un ajuste de campo) se separan de los que solo el
  proveedor puede corregir, y el presupuesto de análisis de IA se destina
  primero a los corregibles.
- **Análisis de IA, etiquetado como tal.** Una tarjeta de clúster indica si el
  consejo lo escribió un modelo de lenguaje o una regla, qué contó el análisis
  y cuándo dejó de ser válido, y si un clic reutilizará un análisis en caché.
  Si el asesor de IA no puede ejecutarse en este entorno, la pestaña explica
  por qué.
- **Análisis masivo.** Analice muchos clústeres en una sola ejecución, vea
  clúster por clúster qué está haciendo la ejecución y encuentre los resultados
  después. La lista de resultados sobrevive a la navegación y a la recarga, y
  la ejecución ya no se queda colgada en "Running · 0/6 done" en una vista de
  suborganización.
- **Propuestas de cambio.** Una recomendación se convierte en algo sobre lo que
  puede actuar: la tarjeta explica el cambio propuesto en cuatro preguntas,
  permite ajustarlo, muestra una vista previa de lo que haría (no se guarda
  nada), lo aplica, mide el efecto y puede deshacerlo. Los pasos de corrección
  enlazan directamente con la página de configuración que nombran, prefiltrada
  por tipo de documento, campo o regla.
- **Página de proveedor.** Elija un proveedor desde la pestaña o busque en la
  cola de oportunidades por nombre o número. La página muestra la tasa
  touchless del proveedor a lo largo del tiempo (de 30 días a 1 año), sus
  documentos problemáticos y los documentos que fueron bien, y ofrece un
  diagnóstico de IA por proveedor. Se pueden comparar hasta cinco proveedores
  lado a lado. Se muestra el número de proveedor en lugar de un hash interno.
- **Flujo del pipeline.** Un diagrama por documento y por clúster muestra el
  recorrido por entrada, clasificación, comprobación de documento electrónico,
  proveedor, OCR, extracción, validación, coincidencia de OC, aprobación y
  exportación, con la etapa que lo detuvo.
- **Coincidencia de órdenes de compra, explicada.** El conjunto de reglas de
  OC se dibuja como un diagrama de flujo en la página de configuración y en
  Touchless, con el recorrido que siguió un documento y un motivo en lenguaje
  sencillo de por qué no pasó. Los códigos de motivo distinguen "orden de
  compra no encontrada" de "discrepancia de línea" y "falta un campo
  obligatorio".
- **Segmentación.** Los KPI, los clústeres y las propuestas pueden desglosarse
  por un campo del documento, por ejemplo Order Type = Direct / Indirect.
- **Cifras correctas.** Los mosaicos de KPI respetan el filtro de
  suborganización y cuentan solo los documentos que el desglose puede listar.
  Una sesión de navegador del usuario de sistema de la organización cuenta como
  humana, de modo que los documentos corregidos a mano ya no se archivan como
  touchless.
- La barra de herramientas del informe acomoda sus controles en pantallas
  anchas, y los colores del modo oscuro provienen del tema.

### DocNet

- El feed de Actividades, el widget de Actividad reciente y la línea de tiempo
  de misiones están traducidos. Los resúmenes de auditoría aparecían en inglés
  en los 22 idiomas.
- Los agentes ven los campos que el tipo de documento define pero que la
  extracción dejó vacíos. Antes concluían que esos campos no existían y omitían
  las actualizaciones obligatorias sin intentar escribir.

### Seguridad

- Los source maps del frontend se eliminan de cada despliegue. Todos los
  entornos los servían, producción incluida.

---

## API Service — `12.83.156`

### Reconocimiento de proveedores y datos maestros

- Un proveedor se identifica cuando un campo de búsqueda es único. Con varios
  campos de búsqueda, los resultados se combinaban como una unión, de modo que
  una coincidencia amplia de nombre con cuatro proveedores ahogaba un número de
  identificación fiscal que coincidía exactamente con uno. Los campos que no
  coinciden con nada ya no vetan a los que sí coincidieron. Consulte
  [Configuración de datos maestros](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  para saber cómo funcionan los campos en conjunto.
- Los reemplazos de datos maestros se registran con su origen: conjunto de
  datos, configuración, campo de origen, operador y tipo de coincidencia. La
  pantalla de validación lo muestra y puede restaurar el valor extraído.
- Cash Discount Term se importa desde el BOD de proveedor; los proveedores
  sincronizados desde el ERP lo tenían vacío. Un Discount Term Overwrite
  introducido como código completo ("143", "012", "X08") se aplica; antes solo
  se consultaba el prefijo de porcentaje.
- Las búsquedas de datos maestros se limitan a 1.000 filas por página y pivotan
  en SQL. Una búsqueda sobre 19.000 registros tardaba cinco segundos por
  llamada y bloqueaba la API.
- Los nombres de propiedad y los tipos de datos de los filtros en la búsqueda
  de datos maestros se vinculan como parámetros SQL. Antes se interpolaban en
  la consulta.

### Procesamiento de documentos

- Los documentos de una organización que carga de forma continua se degradaban
  a prioridad 9, que la cola solo atiende cuando todas las prioridades
  superiores están vacías. La degradación se limita ahora a 3. El reconciliador
  que debía volver a encolar los documentos atascados no tenía credenciales
  válidas en producción; ahora sí.
- Un documento terminado y exportado nunca se sobrescribe con "error". Un
  indicador de flujo de trabajo que nunca se limpiaba hacía que el barrido de
  reintentos recogiera una vez por minuto un documento exportado correctamente,
  hasta que el límite de reintentos lo marcaba como "error" y enviaba el correo
  de error de exportación del cliente, 2 h 17 min después de la exportación.
- Fusionar y anexar acepta archivos `.PDF` y `.Pdf`. La salida de un escáner
  con nombre `SCAN0001.PDF` se rechazaba con "Only PDF files are allowed."
- La invalidación de caché recorre el espacio de claves una vez en lugar de dos
  y solo limpia los tipos de datos de búsqueda que un BOD cambió. Cada BOD
  borraba toda la caché de búsqueda de la organización, bloqueando la API
  mientras recorría las claves de todos.
- El reentrenamiento del modelo se ejecuta como tarea en segundo plano y
  devuelve de inmediato un estado que la interfaz consulta periódicamente.
- Un token de procesamiento de otra organización se rechaza con independencia
  de la comprobación de pertenencia a suborganización que lo precede.
- La sincronización de usuarios deja intacto el indicador de usuario de sistema
  en lugar de restablecerlo en cada ejecución.

### Exportación

- Las líneas de recepción de M3 emparejan el precio unitario exportado con la
  base de precio propia de la línea de factura. El precio viajaba con el
  divisor de la línea de OC y el ERP recalculaba el precio de la línea a 1.000
  veces el importe facturado.
- Una exportación de tabla sobrevive a una línea cuya orden de compra se ha
  eliminado; la línea se exporta sin base de precio.
- Exportación IDM: un campo multivalor mapeado a un campo numérico (por
  ejemplo, una cantidad) hacía fallar la carga útil de la exportación. El valor
  se convierte primero a texto.

### Documentos electrónicos

- Las facturas XRechnung CII cuyo importe pendiente de pago es 0,00 porque un
  importe pagado por adelantado compensa el total muestran el total general
  (BT-112) como importe total. El cliente veía "importe total 0,00".
- Los documentos XRechnung CII y Facturae vuelven a entregar sus campos de
  proveedor. Sobrescrituras obsoletas a nivel de organización ocultaban el
  mapeo predeterminado correcto, por lo que el reconocimiento de proveedores
  nunca podía coincidir.
- El catálogo de reglas de validación se pagina, busca y ordena en el servidor,
  con facetas para la barra de filtros.

### Clasificación

- Los documentos suizos se clasifican como `de_CH`, `fr_CH` o `it_CH` a partir
  de su contenido (importes en CHF, números de IVA CHE, IBAN CH). La
  configuración regional se tomaba del valor predeterminado de la organización
  y los documentos suizos recibían `de_DE`.

### Búsqueda del dashboard

- Una única semántica de operadores en Postgres y ClickHouse: `=` exacto, `:`
  contiene con comodines en los extremos, `!=` complemento incluidos los
  valores vacíos. En Postgres, `=` era una coincidencia de prefijo, de modo que
  `invoice_id=911892112` devolvía también 911892112333.
- Una búsqueda simple es una búsqueda de subcadena en todos los campos,
  identificadores de negocio incluidos. Orden de compra, número de pedido,
  código de barras, tipo de factura, subtipo de factura y número de requisición
  no tenían ninguna rama de texto simple.
- El chip de número de factura es exacto en Postgres, como ya lo era en el
  índice. Los ceros a la izquierda, las formas decimales y las mayúsculas se
  tratan igual en texto libre y en los chips.
- La búsqueda por WebSocket del dashboard lleva la credencial del solicitante
  al servicio de texto completo. Antes se rechazaba toda delegación, por lo que
  el dashboard buscaba silenciosamente solo en Postgres y presentaba la
  respuesta como completa.
- Los mosaicos de estado, el recuento de resultados y la lista de resultados se
  ejecutan sobre un mismo conjunto de predicados. Los mosaicos describían toda
  la organización durante cualquier búsqueda.
- Los permisos de suborganización y de tipo de documento se aplican antes de la
  ventana de resultados, de modo que los documentos permitidos ya no quedan
  fuera del límite de 500 / 10.000.
- La búsqueda vectorial se limita a la ventana real de resultados e informa del
  límite en lugar de mostrar "(50)" como total exacto.
- Una búsqueda que se ejecutó sin el índice de texto completo (índice
  inexistente, índice con minutos de retraso, fallo en la consulta de
  capacidades, resolución de campos degradada) informa del estado de su ventana
  en lugar de "completa".
- Las exportaciones del dashboard de una búsqueda truncada llevan una fila de
  aviso en el CSV/XLSX y en el correo de notificación.
- Los scripts de documentos que llaman a la búsqueda de texto completo se
  autentican correctamente y muestran los fallos en lugar de devolver un
  resultado vacío.

### Coincidencia de órdenes de compra (matcher en proceso)

Para las organizaciones que realizan la coincidencia en la API en lugar de en
el PO Match Service:

- Se registra cada comparación de columna, incluidos el precio unitario y la
  cantidad, de modo que el tooltip de discrepancia puede nombrar la columna que
  falló.
- Las órdenes de compra eliminadas por el usuario permanecen eliminadas en la
  coincidencia automática.
- Un número de OC corregido se compara en el mismo guardado que lo corrige.

### Analytics

- Touchless: todos los cambios de backend detrás de la sección de Web App
  anterior, incluida la evidencia de etapa registrada por cada etapa del
  pipeline, la traza de coincidencia de OC, las propuestas de cambio con vista
  previa, aplicación y reversión, la segmentación, el estado masivo en una sola
  llamada por ciclo, y el endpoint de tendencia que acepta cualquier ventana y
  un proveedor.
- Se corrigieron tres tareas en segundo plano de analytics que fallaban en cada
  ejecución programada.

---

## PO Match Service — `1.59.34`

- El precio unitario de una línea de OC se deriva de su importe neto, no de su
  total con impuestos, y la instantánea de OC de un documento vuelve a derivar
  sus precios unitarios en el momento de la coincidencia.
- El servicio registra de dónde procede cada candidato a número de OC y qué
  números consultó una ejecución. El número de factura propio de un documento
  nunca es candidato a OC. Una coincidencia descartada deja su motivo en el
  documento para la pantalla.
- Se registra la columna que no coincidió, y se miden las columnas que una
  regla de respaldo eliminó.
- Las órdenes de compra eliminadas por el usuario se respetan, y las
  coincidencias en segundo plano obsoletas se limpian tras la exclusión final.
- La coincidencia manual funciona para organizaciones cuyas reglas no llevan el
  indicador `is_fallback`. Los usuarios seleccionaban líneas, pulsaban
  coincidir y no recibían nada.
- No más documentos huérfanos en "Cola": los tiempos de espera de sentencias de
  base de datos, los keepalives y un manejador explícito de límite de tiempo
  blando marcan la tarea como fallida en lugar de depender de una terminación
  forzada que no dejaba rastro.
- Dos errores de producción (un precio unitario `NaN`, un grupo sin cantidades)
  ya no hacen fallar toda la coincidencia.
- Los cambios de tolerancia se leen en cada petición de coincidencia, de modo
  que una tolerancia guardada hace un momento la usa la siguiente coincidencia.
- La traza de decisión de cinco etapas se persiste por documento para
  Touchless.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` puede omitir el saldo de créditos, y el cálculo
  de créditos ejecuta todas las ventanas de año de contrato en una sola
  sentencia en lugar de una consulta por ventana (32 consultas de unos 700 ms
  cada una para la organización más grande). Se prepara un resumen diario de
  uso para usos posteriores.
- Las cifras de tokens restantes en los lectores de organización se calculan
  por año de contrato.
- La caducidad del token se aplica en los aciertos de caché. Una entrada en
  caché podía autenticar hasta nueve horas después de que el token caducara.
- La verificación del token deja de escribir un `org_id` sin cambios en la fila
  del usuario en cada petición, lo que producía un UPDATE por llamada.
- Las comprobaciones de estado omiten la E/S de Redis, y el cliente de Redis se
  agrupa en un pool. Se corrigió una fuga de memoria que llevaba el
  autoescalador al máximo de réplicas, y el servicio vuelve a funcionar con dos
  workers.
- Un registro de proveedor repetido (enlace mágico abierto dos veces) reutiliza
  la pertenencia existente en lugar de fallar con un error de clave duplicada.
- El hilo de correo de restablecimiento de contraseña usa la única app Flask
  registrada; el restablecimiento fallaba con "current Flask app is not
  registered" desde el 25 de agosto.
- El indicador de usuario de sistema puede cambiarse en un usuario existente
  cuando ningún otro miembro lo tiene.
- Inicio de sesión MCP: MFA vinculada a la transacción, consentimiento de un
  solo uso y una elección forzada de cuenta cuando el navegador guarda dos
  identidades de sesión.

---

## Auth Bridge Service — `0.5.7`

Replicación de autenticación entre la UE y EE. UU.:

- La reconciliación periódica mantiene vivo el flujo de replicación. Tardaba
  unos 95 s mientras el tiempo de espera del emisor era de 60 s, de modo que
  cada reconciliación de seis horas cortaba el flujo puntualmente.
- Cuando el flujo muere, el slot de replicación se vuelve a enganchar en el
  sitio en lugar de reconstruir el puente y volver a ejecutar la reconciliación
  completa de arranque.
- La reconciliación compara las claves primarias por páginas en lugar de cargar
  ambos lados en memoria, lo que ya no cabe desde que la tabla de tokens se
  unió a la replicación.
- Un origen de replicación existente se trata como éxito, no como degradación.

---

## Extraction Service — `1.55.33`

- La extracción estructurada se resuelve por proveedor: el ajuste de un layout
  entrenado prevalece sobre la preferencia de la organización, del mismo modo
  que lo hace el modelo de IA.
- Un mapeo de columnas aprendido no puede prohibir columnas que la factura
  tiene.
- Extracción de tablas con IA: las columnas de importe se tipan como números
  con una descripción, y los valores no numéricos inventados en columnas de
  importe (un "St." copiado de la celda vecina en precio unitario por) se
  descartan en lugar de almacenarse.
- Facturas de EE. UU.: cuando el importe neto ya es igual al total, el impuesto
  se resuelve como 0 en lugar de conservar un impuesto extraído espurio. El
  ruido de coma flotante por debajo del céntimo ya no decide entre pares
  candidatos de neto/impuesto (268.28 + 22.13 perdía frente a neto = total,
  impuesto = 0).
- Una tabla cuya fila de encabezado nunca se mapeó a nombres reales se extrae
  en lugar de fallar por completo.

---

## Fulltext Service — `1.42.35`

- La caché de resultados de búsqueda está activada en todos los entornos;
  producción, sandbox y stage funcionaban sin ella desde que se crearon los
  archivos de entorno activos. La carga y la eliminación la invalidan, de modo
  que una búsqueda tras una carga ve el nuevo documento.
- El `=` exacto en un campo de texto dinámico compara solo el valor completo.
  Un comodín en la ruta analizada hacía que `note_field=53173` coincidiera con
  "PO 53173 / 2024".
- Un identificador con guiones sin más como `2026-003` es un único literal, no
  una bolsa de tokens.
- Los números de orden de compra se encuentran en todas las formas de
  almacenamiento, incluidos los identificadores solo numéricos cuya cláusula
  exacta se descartaba silenciosamente.
- Las rutas de lectura dejan de crear el índice que leen. Un índice inexistente
  o vacío informaba "completa, 0 resultados"; toda respuesta con cero
  resultados lleva ahora un estado de ventana y un motivo.
- Los valores de moneda escritos en texto, los mapeos booleanos heredados, las
  fechas y los indicadores de impuestos sobreviven a la reconstrucción del
  índice reducido, y las entradas del índice sin campos se detectan y se
  recuperan desde la extracción.

---

## Docflow Service — `2.10.11`

- Las importaciones de flujos de trabajo avanzados dependen del derecho de la
  organización, y un lote se comprueba antes de escribir nada. Una organización
  sin el módulo avanzado podía importar un flujo de trabajo avanzado que luego
  no tenía forma de abrir.
- El cambio de nombre de un flujo de trabajo va con el guardado, y los cambios
  de nombre de plantillas se persisten.
- La actualización de "ejecución de flujo de trabajo pendiente" se reintenta
  cuando se pierde la conexión. Una sola petición fallida dejaba el indicador
  sin cambios y mantenía el documento fuera de la exportación hasta que alguien
  lo reiniciaba.

---

## Docnet Service — `1.56.12`

- El descubrimiento de campos devuelve todos los campos de cabecera que el
  layout define, estén rellenados o no, y coincide con lo que comprueba la
  protección de escritura. Los agentes omitían actualizaciones de campo
  obligatorias porque los campos vacíos parecían inexistentes.
- Las identidades se almacenan en caché bajo la misma clave con ámbito de
  organización que usa la API, de modo que el límite de la clave de API de la
  organización se mantiene en ambos servicios.

---

## Email Service — `1.41.6`

- Los buzones compartidos de Office 365 con más de diez subcarpetas resuelven
  todas las carpetas. Microsoft Graph pagina las carpetas de diez en diez; la
  configuración 11.ª y las siguientes fallaban en cada sondeo con "unable to
  find the selected Folder".

---

## FTP Service — `1.32.18`

- El planificador SFTP se inicia en cada proceso worker en lugar de antes del
  fork. Las importaciones SFTP periódicas fallaban silenciosamente con un
  estado del planificador corrupto, mientras que un proceso nuevo funcionaba
  bien.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Solo cambios de compilación y despliegue (actualización de la imagen base,
credenciales de CI). Sin cambios en el comportamiento.

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->
