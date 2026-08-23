# Notas de versión de DocBits — 29 de julio – 12 de agosto de 2026

_Lo que cambió en la actualización de producción de DocBits desplegada el
10–12 de agosto de 2026, que abarca todo lo ocurrido desde la versión del 29 de
julio. Cada servicio indica la versión que entró en producción y, a
continuación, las novedades o correcciones en lenguaje sencillo. Los servicios
que no aparecen en la lista (Auto Accounting `1.21.1`, Ideas `0.3.1`, OCR
`1.10.3`, Operator `1.42.1`, PO Match `1.59.3`, FTP `1.32.4`) no tuvieron
cambios visibles para el cliente._

---

## Aspectos destacados

- **Compatibilidad con FacturaE.** Las facturas electrónicas españolas
  FacturaE 3.1 se clasifican y extraen de fábrica, con mapeos de campos
  completos. En la misma oleada, los mapeos de ebInterface (Austria) pasaron a
  ser fieles a cada versión, los valores predeterminados de Factur-X y ZUGFeRD
  ganaron la ruta del nombre de la empresa y se corrigieron varios mapeos
  predeterminados erróneos de descuentos, IVA y precios unitarios.
- **Búsqueda y ordenación del dashboard reparadas.** La ordenación ya no
  depende de qué columnas estén visibles en ese momento, un filtro OR
  combinado con un rango o una igualdad ya no borra las frases de búsqueda,
  los nombres de proveedor vuelven a aparecer en la búsqueda rápida y las
  fechas en formato ISO se leen correctamente.
- **La extracción con IA se corrige a sí misma.** Un intercambio demostrable
  de los importes neto/total hecho por la IA se deshace automáticamente, los
  campos escaneados con IA ya no vuelven mal tras reiniciar un documento, y la
  extracción de tablas con IA procesa los documentos en lotes de páginas, de
  modo que las tablas largas llegan completas.
- **Los flujos de trabajo sobreviven a un fallo pasajero de autenticación.**
  Un servicio de autenticación brevemente inaccesible se reintenta en lugar de
  hacer fallar la ejecución, y un disparador de flujo de trabajo que no puede
  autenticarse informa del error en lugar de dejar el documento atascado.
- **Los PDF difíciles de leer se extraen de nuevo.** Cuando el decodificador
  de texto PDF estándar no puede leer una página (habitual en archivos
  producidos con Ghostscript), la extracción recurre a un segundo motor en
  lugar de no devolver nada.
- **MFA funciona entre regiones.** Los datos de inscripción de dos factores se
  replican entre las regiones de la UE y EE. UU., de modo que un segundo
  factor configurado en una región se acepta en la otra.

---

## Web App — `10.49.4`

### Inicio de sesión y cuentas

- Cerrar sesión en una pestaña del navegador cierra también la sesión en las
  demás pestañas, sin los mensajes de error que antes aparecían cuando las
  pestañas discrepaban sobre la sesión.
- Cambiar su propia contraseña desde el perfil pasa por el endpoint dedicado
  de autoservicio, de modo que funciona sin permisos de administrador.
- El inicio de sesión con clave de acceso desde la región no principal muestra
  mensajes de error traducidos, y su botón de envío es visible.

### Pantalla de validación

- La pestaña "Tabla extraída" ya no gira indefinidamente cuando ya existe una
  tabla de IA.
- Los documentos a los que les faltan los datos de código de barras ya no
  rompen la vista de asignación de códigos de barras.
- Las líneas multi-impuesto de M3 ofrecen el código de impuesto como
  desplegable alimentado por la lista de valores, en lugar de un campo de
  texto libre.
- Abrir facturas de proveedor grandes es notablemente más rápido.

### Tareas

- Las columnas del Kanban se paginan a medida que se desplaza, de modo que los
  tableros con muchas tareas cargan rápido.
- El contador de tareas abiertas de la barra lateral cuenta las tareas en el
  contexto de su suborganización, no en el contexto del documento que
  casualmente esté abierto.

### Workflow Builder

- La lista de flujos de trabajo conserva su búsqueda, orden, página y tamaño
  de página cuando abre un flujo de trabajo y vuelve, incluso a través de la
  ruta de navegación (breadcrumb), y la página se abre por defecto en la
  pestaña List.

### Configuración y administración

- La página de Datos maestros ya no aparece en blanco por una condición de
  carrera en la ordenación, y ordenar por insignias ya no bloquea la página.
- Una suscripción en estado de "cancelación" puede reanudarse.
- La página de detalle de XSLT informa de los errores de carga en lugar de no
  mostrar nada, y los ajustes de notificaciones por correo usan todo el ancho
  de la página con un panel de registros operativo.
- El selector de organización para usuarios con varias organizaciones tiene un
  diseño de filas, un tamaño y unos colores de tema correctos, se desplaza
  correctamente y ofrece un filtro para cuentas con muchas organizaciones.
- Analytics: una petición de métricas fallida muestra un estado de error en
  lugar de mostrar ceros, y los widgets de uso informan con honestidad cuando
  no hay datos de medición disponibles.
- Se eliminaron opciones de caché obsoletas de la página de gestión de caché,
  y las páginas de Usuarios y Grupos perdieron sus dobles barras de
  desplazamiento anidadas.
- "Use Default Template" en el gestor de layouts ya no falla ni se queda
  inerte; también deja de afirmar que no existe ningún layout predeterminado.
- Las reglas de selección conservan sus operadores de coincidencia de texto,
  de presencia y de regex cuando se reabre una regla.
- Los tipos de documento admiten reglas de transformación por tipo, y la
  interfaz de la lista de reglas ganó una acción de valor fijo.
- Las insignias de estado de las órdenes de compra se mapean correctamente
  para valores de estado con la capitalización del ERP.
- Las pantallas de DocNet (AI Workforce), incluido el Agent Wizard, están
  traducidas, y el diálogo de nueva/editar idea se desplaza horizontalmente.
- Cotizaciones del portal de proveedores: las unidades de medida gestionadas
  se muestran en la tabla de líneas, el estilo de aprobación se aplica solo a
  las cotizaciones de contrato y la línea de comparación ya no aparece cuando
  ambos valores son idénticos.
- El JSON de respaldo de la página de error es legible en modo oscuro, y los
  informes usan una etiqueta adecuada de "últimos 7 días" en lugar de un "7"
  suelto.

## API Service — `12.74.0`

### Dashboard y búsqueda

- La ordenación funciona con independencia de qué columnas estén visibles, y
  una palabra clave que la búsqueda delega al texto completo ya no deja atrás
  un fragmento SQL roto.
- Los nombres de proveedor vuelven a aparecer en la búsqueda rápida para
  organizaciones sin indexación de texto completo.
- Las fechas en formato ISO (2026-08-12) ya no las malinterpreta el
  normalizador de fechas que asume el día primero.
- Las exportaciones del dashboard dirigen los valores de texto sueltos, como
  los números de factura, a la columna correcta.

### Facturas electrónicas

- FacturaE 3.1 (España): regla de clasificación y mapeos de campos completos.
- Las reglas de clasificación de XRechnung están ancladas a su familia de
  sintaxis, de modo que un documento UBL ya no lo capturan las reglas CII, y
  viceversa.
- La versión aceptada "3.0" cubre toda su familia de parches (3.0.1, 3.0.2).
- Las facturas CII toman el nombre legal del proveedor y usan el nombre
  comercial solo como alternativa.
- Los mapeos de ebInterface (Austria) son fieles a cada versión, con una regla
  comodín corregida y datos de prueba reconstruidos.
- Los valores predeterminados de Factur-X y ZUGFeRD ganaron la ruta de
  extracción del nombre de la empresa, y se corrigieron las transformaciones
  de cabecera predeterminadas para el tipo impositivo, el tipo de factura y
  los campos de nivel 3, junto con la semántica de descuentos, IVA y precios
  unitarios en toda la familia.
- Los códigos de categoría de impuestos de origen ya no se mapean a ciegas
  sobre sus códigos del ERP.
- Los documentos que mencionan tanto "factura" como "nota de crédito"
  prefieren la clasificación de nota de crédito.

### Documentos y extracción

- Cuando el decodificador PDF estándar no puede leer el texto incrustado de
  una página, la extracción recurre a un segundo motor, de modo que los PDF
  afectados se extraen en lugar de volver vacíos.
- El interruptor maestro de códigos de barras es ahora `BARCODE_EXTRACTION`;
  el antiguo ajuste de códigos QR sigue funcionando como alias.
- Se taponó una fuga de memoria en el planificador en segundo plano; degradaba
  lentamente el procesamiento tras días de actividad continuada.
- Los proveedores importados sin país se quedan en blanco en lugar de asumir
  Alemania por defecto.

### Exportación y datos maestros

- Guardar reglas ("Save Rules") informa del fallo cuando no escribe nada, en
  lugar de afirmar que tuvo éxito.
- Las líneas con importe cero ya no se descartan de las exportaciones de
  contabilidad automática, y se corrigió un filtro que coincidía con todos los
  grupos.
- Las exportaciones M3 admiten post-hooks de información adicional.
- Una sonda de conjunto de datos fallida ya no deja en blanco toda la pantalla
  de Datos maestros.
- Las cachés de PO se invalidan cuando el ERP actualiza el estado de una orden
  de compra, de modo que el dashboard deja de mostrar el estado obsoleto.

### Administración

- Cada preferencia muestra qué usuario la cambió por última vez.
- Las reglas de extracción pueden eliminarse por proveedor y clonarse mediante
  nuevos endpoints.
- Los destinatarios de correos de alerta de estado se comparan de forma segura
  frente a NULL, lo que corrige un fallo en la entrega de notificaciones.

## Auth Service — `1.75.9`

- Una clave de API de organización usada contra una organización ajena se
  rechaza.
- Crear una organización devolvía un error aunque en realidad guardaba la
  fila; ahora responde correctamente.
- Iniciar sesión con una clave de acceso cuando no hay ninguna registrada
  devuelve su propio código de error, de modo que la pantalla de inicio de
  sesión puede decir qué ocurre.

## Auth Bridge Service — `0.4.2`

- Las tablas de inscripción de dos factores se replican entre las regiones de
  la UE y EE. UU., y las filas se identifican por su clave primaria real.

## Docflow Service — `2.8.7`

- Un disparador de flujo de trabajo que no puede autenticarse informa del
  fallo en lugar de dejar el documento atascado, y un servicio de
  autenticación brevemente inaccesible se reintenta en lugar de tratarse como
  un token inválido.
- Tarjetas de comparación de cotizaciones: los números de artículo se comparan
  solo para las líneas que describe la matriz de precios de artículos, y las
  líneas sin unidad de medida o sin precio se omiten en lugar de hacer fallar
  la comparación.
- La tarjeta de comparación de precios contratados ganó una opción de operador
  cualquiera/todos (any/all), y las cachés de tarjetas se invalidan
  correctamente tras migraciones y actualizaciones de código.
- Las conexiones SSL caídas se tratan como transitorias y se reintentan en
  lugar de hacer fallar la ejecución.

## Docnet Service — `1.56.4`

- Los endpoints de estado y de versión ya no se bloquean en comprobaciones en
  vivo, lo que antes hacía que el diálogo de Versiones de servicios se
  colgara.

## Email Service — `1.40.6`

- Cuando un correo entrante se omite, el motivo se muestra en la fila del
  evento de importación en lugar de quedar en silencio.
- Los archivos contenedores `.eml` adjuntos ya no se importan como documentos.
- Un inicio de sesión fallido de Microsoft Office produce un mensaje de error
  legible, y un error de transporte del servicio de IA cuenta como "no claro"
  en lugar de como un rechazo.

## Extraction Service — `1.53.8`

- Un intercambio demostrable de los importes neto/total hecho por la IA se
  deshace tras la extracción de campos, y los fallos de las salvaguardas se
  registran en lugar de pasar en silencio.
- Los campos escaneados con IA ya no vuelven mal tras reiniciar un documento.
- La extracción de tablas con IA procesa por lotes de páginas y acumula todos
  los lotes, de modo que las tablas largas llegan completas.
- Los documentos que mencionan tanto "factura" como "nota de crédito"
  prefieren la clasificación de nota de crédito.
- La limpieza repetida de cabeceras y pies de página se almacena en caché, lo
  que acelera la extracción en documentos de varias páginas.

## Fulltext Service — `1.41.7`

- Un filtro OR combinado con una condición de rango o de igualdad ya no borra
  las frases de búsqueda.
- La ordenación usa las rutas de índice correctas y muestra el motivo real
  cuando el backend de búsqueda rechaza una consulta; una regresión de
  ordenación que rompió por completo la búsqueda con consultas en bruto se
  corrigió la misma semana en que apareció.
- Las búsquedas de documentos funcionan en índices antiguos con mapeo de
  texto.
- La caché de tokens se limita al par de token y organización, de modo que
  cambiar de organización no puede servir resultados bajo el contexto
  anterior.
