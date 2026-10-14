# Hoja de ruta de DocBits

_Estado de la planificación a 7 de octubre de 2026. Cada versión indica la
fecha prevista en sandbox (cuando los clientes pueden probarla) y la fecha
prevista en producción. Los temas describen lo que está previsto para la
versión, no lo que ya se ha publicado; el alcance y las fechas pueden cambiar.
Las correcciones urgentes entre versiones se documentan en las
[Notas de versión](release-notes/README.md)._

| Versión | Sandbox | Producción |
|---|---|---|
| R1.1 | 16 de octubre de 2026 | 4 de noviembre de 2026 |
| R1.2 | 16 de febrero de 2027 | 3 de marzo de 2027 |
| R1.3 | 1 de junio de 2027 | 16 de junio de 2027 |
| R1.4 | 5 de octubre de 2027 | 20 de octubre de 2027 |

---

## R1.1 — Sandbox 16 de octubre de 2026 · Producción 4 de noviembre de 2026

**Reglas de transformación y layouts**

- Un motor de reglas para los valores extraídos de campos y columnas:
  establecer, reemplazar o derivar valores con grupos de condiciones anidados,
  con una pantalla de configuración para gestionar las reglas. La condición "es
  uno de" admite varios valores, la lista de reglas puede buscarse por ID de
  regla, y las reglas también se ejecutan después de la consulta de datos
  maestros.
- Las reglas de selección de layout reciben las mismas condiciones anidadas y un
  registro de ejecución opcional. La selección de layout funciona con
  independencia del origen del documento.
- Manage Layouts, las reglas de validación personalizadas y las reglas de
  transformación ya no necesitan el interruptor beta.
- Reglas de precedencia claras para las etiquetas de campo en los campos de
  cabecera y en las columnas de tabla. Los usuarios pueden crear sus propias
  claves de traducción para los ajustes de campo y las columnas de tabla.
- Una columna de tabla puede asignarse de nuevo después de haberse eliminado, y
  la tabla de precios de artículos de proveedor muestra todas sus columnas.

**Pantallas de aprobación y validación**

- Las tres tablas de líneas de la pantalla de aprobación (líneas de factura,
  líneas de comparación, coincidencia de OC) comparten un mismo estilo.
- El último panel lateral abierto (flujo de actividad o historial de
  aprobación) se recuerda por usuario.
- Fusionar documentos desde la pantalla de aprobación con el cargador de
  documentos.
- Las reglas de validación personalizadas tratan los gastos de envío de forma
  genérica, muestran un mensaje de campo en lugar de un error general cuando un
  campo obligatorio está vacío, y se corrigen las reglas que informaban de un
  falso negativo. Las reglas predeterminadas del sistema pueden duplicarse.
- Se notifica una discrepancia entre cantidad e importe neto en una tabla
  extraída por IA, una factura con una orden de compra emparejada ya no se
  clasifica como factura de costes, y se acepta una fecha reformateada por una
  regla.
- Se corrige una pantalla de aprobación que se quedaba bloqueada en la
  superposición de carga tras aprobar o rechazar. Una barra de carga sustituye
  al icono de carga simple, y las URLs de página son más amigables.
- Abrir un enlace a un documento después de que la sesión haya caducado lleva a
  la página de inicio de sesión en lugar de a un 404.

**Detección de duplicados**

- Los campos personalizados aparecen en el resultado de la detección de
  duplicados, y se puede buscar en la configuración de duplicados.
- "Bloquear exportación de documentos duplicados" bloquea la exportación de un
  duplicado detectado.

**Flujos de trabajo y tareas**

- Un botón "Nuevo flujo de trabajo", registros para los flujos de trabajo
  avanzados, una pantalla de registro de Watchdog más clara, y los pasos de
  flujo de trabajo que cambian un campo o una casilla se aplican de forma
  fiable.
- Al añadir una línea en un árbol de decisión se conservan los nombres de
  usuario en lugar de mostrar IDs.
- Cada cambio de estado de un documento queda registrado.
- La creación de una nueva plantilla de correo vuelve a funcionar.
- La lista de tareas muestra sus tareas en la primera carga.

**Importación**

- La importación de correo mueve un mensaje fuera de la bandeja de entrada solo
  después de confirmarse la carga, trata un reenvío entregado de nuevo como una
  única entrega, registra quién guardó por última vez y lista un adjunto una
  sola vez con el motivo cuando falla.
- La importación FTP y SFTP recibe una verdadera opción de eliminar tras
  importar, junto a mover y archivar. Las contraseñas ya no se corrompen al
  editar una configuración, la prueba de conexión funciona para las nuevas
  conexiones SFTP, y una conexión SFTP fallida o un inicio de sesión incorrecto
  muestra un mensaje específico en lugar de un error general.
- Se avisa a los administradores en el asistente de configuración cuando una
  importación FTP o de correo configurada deja de funcionar.
- La carga desde la app de escáner vuelve a funcionar.
- Los archivos BOD de orden de compra cargados en la región de EE. UU.
  permanecen en la región de EE. UU.

**Procesamiento de documentos y extracción**

- Cuando el servicio de códigos de barras se bloquea, el documento muestra el
  error en lugar de permanecer indefinidamente en "Procesando".
- Un nuevo nivel de modelo de IA más económico ("Eco") para la extracción.
- Con la extracción estructurada por IA, los números de artículo de proveedor
  entrenados se mantienen entrenados, y el número de artículo y el número de
  artículo de proveedor ya no se intercambian.
- Se ajustan las plantillas de documentos electrónicos UBL; correcciones de
  extracción para importes, tipos impositivos, precios unitarios y números de
  orden de compra en layouts de proveedores concretos.
- Se reconocen formatos de fecha adicionales.
- Una factura de costes con dos tipos de IVA conserva ambas líneas contables.

**Coincidencia de órdenes de compra**

- La coincidencia requiere una columna de cantidad, usa el precio por cantidad
  de unidad base, y el respaldo a la última línea puede activarse o
  desactivarse por cliente.
- Las líneas de albarán pueden seleccionarse individualmente.
- La pantalla de documentos electrónicos ya no se congela con facturas de más
  de 250 líneas.

**Touchless Intelligence**

- Más detalle en el informe Touchless, y la casilla Touchless refleja la
  configuración guardada.

**Dashboard, cuentas y suscripción**

- El dashboard puede contener hasta 10.000 documentos por búsqueda, y un filtro
  de fecha personalizado se aplica correctamente.
- La fecha de vencimiento del descuento y la fecha de vencimiento de la factura
  están disponibles como campos de layout y se rellenan en la importación.
- Los usuarios compartidos de un dashboard se conservan al guardarlo, y
  "Actualizado por" muestra la persona correcta.
- Los documentos archivados pueden volver a sacarse del estado "Archivado".
- Los usuarios pueden volver a iniciar sesión tras restablecer la contraseña.
- La página del plan de suscripción muestra el uso del plan y de sus
  funciones.

**Exportación y EDI**

- Un paso adicional de exportación a Infor M3 para información adicional de la
  factura.
- Una lista de embalaje con varios números de contenedor se exporta como un
  registro por contenedor.
- Reimportar una recepción de entrega ya no falla por una clave duplicada, y
  los BOD de recepción de entrega se aplican en el orden correcto.
- Se actualizan los mapeos EDI para factura, orden de compra y confirmación de
  pedido.
- Funciona la prueba de conexión de una nueva configuración de exportación a
  Infor IDM o Infor LN.

**Seguridad**

- La protección de organización para las claves de API se aplica en todos los
  entornos.

---

## R1.2 — Sandbox 16 de febrero de 2027 · Producción 3 de marzo de 2027

**Aprobación y coincidencia de órdenes de compra**

- Un estado "Pendiente de respuesta" pausa un documento hasta que alguien
  responde, sin romper el flujo de trabajo ni el historial de auditoría, y los
  aprobadores pueden hacer preguntas sin interrumpir el flujo de aprobación.
- Un documento puede reasignarse a otro usuario (primera fase).
- Las facturas de prepago pueden emparejarse antes de la recepción de
  mercancías mientras "Coincidencia sobre cantidad recibida" permanece activa.
- La pantalla de coincidencia ofrece solo las líneas de OC viables, y las
  coincidencias de varias líneas que omiten la comparación de precios siguen
  mostrando el precio unitario en la pantalla de aprobación.
- Un indicador de disponibilidad de recepción compara las cantidades facturadas
  y recibidas.
- Confirmaciones de pedido: los elementos de costeo se muestran mientras la
  aprobación está pendiente, posiciones de recargo con código de color en la
  coincidencia de OC, y la columna de número de artículo en las líneas de la
  factura.
- Se gestionan las líneas RMA de proveedor.

**Importación y clasificación**

- El tipo de proveedor se deriva de las líneas de artículo.
- El formulario de tickets de soporte acepta adjuntos y vincula la organización
  automáticamente.

**Configuración y automatización**

- El script "Establecer suborganización" se convierte en una regla de
  transformación.
- Las columnas estándar pueden eliminarse de un tipo de documento.

**Exportación**

- El historial de exportación vuelve a listar los documentos exportados.
- Las facturas de flete se exportan a Infor LN.
- Nombres de archivo de exportación configurables.
- Integración fiscal con Vertex ampliada.

---

## R1.3 — Sandbox 1 de junio de 2027 · Producción 16 de junio de 2027

**Rule Manager de Auto Accounting**

- Las reglas asignan cuentas y dimensiones automáticamente, con ámbito por
  suborganización y tipo de documento, y una pantalla de auditoría muestra qué
  regla se activó.
- Una regla puede consultar los datos maestros y asignar varios campos a la
  vez, o rellenar un valor a partir de una columna de línea de tabla.
- Los campos y las dimensiones pueden vaciarse individualmente, las líneas de
  artículo pueden eliminarse (incluidas las líneas sin importe), y las reglas
  siguen funcionando en campos que cambiaron de texto a lista desplegable.
- Las predicciones admiten varios códigos de impuesto y dimensiones,
  comprobantes y referencias de contabilización. Las pantallas de Auto
  Accounting están disponibles en varios idiomas.

**Coincidencia de órdenes de compra**

- El icono de coincidencia navega, desplaza y resalta entre pestañas, incluidas
  las coincidencias de uno a varios.
- Conversión de unidades con alias (por ejemplo KG y TO), una varianza de
  redondeo configurable con una cuenta de redondeo, y cálculos con cuatro
  decimales mostrados como tres.

**Usabilidad**

- El orden de ejecución de los scripts de documento es visible en el frontend.
- Intro y Tabulador permiten moverse entre los campos con el teclado.

**Exportación**

- Un documento incompleto en Infor LN se elimina tras una exportación fallida.
- El conector de base de datos incluye todas las tablas relevantes.

---

## R1.4 — Sandbox 5 de octubre de 2027 · Producción 20 de octubre de 2027

**Auto Accounting en la pantalla de aprobación**

- Los aprobadores pueden trabajar con Auto Accounting directamente en la
  pantalla de aprobación.
- La aprobación puede condicionarse a campos de contabilidad como el código de
  cuenta o el país, con una corrección de cuentas por pagar cuando se devuelve
  un documento.
- Una lista desplegable de códigos de impuesto en Auto Accounting sin necesidad
  de configurar varias líneas de impuestos.
- Las dimensiones se almacenan en una nueva estructura para que los conjuntos
  grandes de dimensiones se carguen más rápido, y el Rule Manager recibe una
  ronda de comentarios.

**Aprobación**

- Un flujo de aprobación mejorado, delegación a otro usuario durante la
  aprobación, y un botón "Exportar y siguiente".

**Coincidencia de órdenes de compra y controles de exportación**

- Las facturas emparejadas en exceso, en las que la cantidad facturada supera
  la cantidad recibida, se reconocen en la pantalla de coincidencia, y las
  unidades de medida se convierten durante la coincidencia de la factura.
- Los códigos de cargo (peaje, transporte, energía) se reconocen y su coste se
  distribuye.
- La exportación se bloquea con una advertencia cuando la cantidad emparejada
  supera o difiere demasiado de la cantidad recibida, o cuando la fecha de
  contabilización es anterior a la fecha de entrada en almacén.

**Importación y configuración**

- Un mecanismo de reintento para la importación FTP, de correo y de correo
  entrante, con reprocesamiento automático y manual, y la dirección del
  remitente está disponible desde la importación de correo.
- La configuración admite búsquedas en todos los interruptores y subpáginas.
- La configuración del servidor de correo permite sustituir un secreto OAuth o
  de cliente caducado sin volver a configurar el buzón.
- El mapa de números de artículo de proveedor (tabla de conversión de números
  de artículo) puede rellenarse desde una importación CSV.
- El historial de aprobación puede exportarse mediante la exportación SFTP.

**DocNet Agents**

- Entrada de pedidos: un pedido de cliente se convierte en una orden de venta
  en Infor M3 o Infor LN (primera versión, documentos de texto).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
