# Hoja de ruta de DocBits

_Estado de la planificación a 18 de septiembre de 2026. Cada versión indica la
fecha prevista en sandbox (cuando los clientes pueden probarla) y la fecha
prevista en producción. Los temas describen lo que está previsto para la
versión, no lo que ya se ha publicado; el alcance y las fechas pueden cambiar.
Las correcciones urgentes entre versiones se documentan en las
[Notas de versión](release-notes/README.md)._

| Versión | Sandbox | Producción |
|---|---|---|
| R1.1 | 5 de octubre de 2026 | 14 de octubre de 2026 |
| R1.2 | 23 de noviembre de 2026 | 2 de diciembre de 2026 |
| R1.3 | 8 de febrero de 2027 | 17 de febrero de 2027 |
| R1.4 | 7 de abril de 2027 | 15 de abril de 2027 |
| R1.5 | 18 de mayo de 2027 | 27 de mayo de 2027 |
| R1.6 | 6 de julio de 2027 | 15 de julio de 2027 |
| R1.7 | 21 de septiembre de 2027 | 30 de septiembre de 2027 |
| R2.0 | por anunciar | por anunciar |

---

## R1.1 — Sandbox 5 de octubre de 2026 · Producción 14 de octubre de 2026

**Reglas de transformación y layouts**

- Un motor de reglas para los valores extraídos de campos y columnas:
  establecer, reemplazar o derivar valores con grupos de condiciones anidados,
  con una pantalla de configuración para gestionar las reglas. Las reglas de
  selección de layout reciben las mismas condiciones anidadas.
- La selección de layout funciona con independencia del origen del documento.
- Reglas de precedencia claras para las etiquetas de campo en los campos de
  cabecera y en las columnas de tabla.
- Una columna de tabla puede asignarse de nuevo después de haberse eliminado, y
  la tabla de precios de artículos de proveedor muestra todas sus columnas.

**Pantallas de aprobación y validación**

- Las tres tablas de líneas de la pantalla de aprobación (líneas de factura,
  líneas de comparación, coincidencia de OC) comparten un mismo estilo, y la
  vista de comparación muestra el número de artículo que corresponde a la
  línea.
- El último panel lateral abierto (flujo de actividad o historial de
  aprobación) se recuerda por usuario.
- Fusionar documentos desde la pantalla de aprobación con el cargador de
  documentos.
- Las reglas de validación personalizadas tratan los gastos de envío de forma
  genérica, y se corrigen las reglas que informaban de un falso negativo.
- Una barra de carga sustituye al icono de carga simple; URLs de página más
  amigables.

**Detección de duplicados**

- Los campos personalizados aparecen en el resultado de la detección de
  duplicados, y se puede buscar en la configuración de duplicados.

**Flujos de trabajo y tareas**

- Un botón "Nuevo flujo de trabajo", registros para los flujos de trabajo
  avanzados, una pantalla de registro de Watchdog más clara, y los pasos de
  flujo de trabajo que cambian un campo o una casilla se aplican de forma
  fiable.
- Al añadir una línea en un árbol de decisión se conservan los nombres de
  usuario en lugar de mostrar IDs.
- Cada cambio de estado de un documento queda registrado.
- La creación de una nueva plantilla de correo vuelve a funcionar.

**Importación**

- La importación de correo mueve un mensaje fuera de la bandeja de entrada solo
  después de confirmarse la carga, trata un reenvío entregado de nuevo como una
  única entrega, registra quién guardó por última vez y acepta correos firmados
  con S/MIME.
- La importación FTP recibe una verdadera opción de eliminar tras importar,
  junto a mover y archivar.
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

**Dashboard**

- El dashboard puede contener hasta 10.000 documentos por búsqueda.
- La fecha de vencimiento del descuento y la fecha de vencimiento de la factura
  están disponibles como campos de layout y se rellenan en la importación.
- Los usuarios compartidos de un dashboard se conservan al guardarlo, y
  "Actualizado por" muestra la persona correcta.
- Los documentos archivados pueden volver a sacarse del estado "Archivado".

**Exportación y EDI**

- Un paso adicional de exportación a Infor M3 para información adicional de la
  factura.
- Una lista de embalaje con varios números de contenedor se exporta como un
  registro por contenedor.
- Reimportar una recepción de entrega ya no falla por una clave duplicada, y
  los BOD de recepción de entrega se aplican en el orden correcto.
- Se actualizan los mapeos EDI para factura, orden de compra y confirmación de
  pedido.

**Seguridad**

- La protección de organización para las claves de API se aplica en todos los
  entornos.

---

## R1.2 — Sandbox 23 de noviembre de 2026 · Producción 2 de diciembre de 2026

**Aprobación y coincidencia de órdenes de compra**

- Un estado "Pendiente de respuesta" pausa un documento hasta que alguien
  responde, sin romper el flujo de trabajo ni el historial de auditoría, y los
  aprobadores pueden hacer preguntas sin interrumpir el flujo de aprobación.
- Las facturas de prepago pueden emparejarse antes de la recepción de
  mercancías mientras "Coincidencia sobre cantidad recibida" permanece activa.
- Un indicador de disponibilidad de recepción compara las cantidades facturadas
  y recibidas.
- Confirmaciones de pedido: los elementos de costeo se muestran mientras la
  aprobación está pendiente, posiciones de recargo con código de color en la
  coincidencia de OC, y la columna de número de artículo en las líneas de la
  factura.
- Las columnas sin mapear ya no alimentan el cálculo del importe de la tabla.
- Se gestionan las líneas RMA de proveedor.

**Importación y clasificación**

- La dirección del remitente está disponible desde la importación de correo.
- El tipo de proveedor se deriva de las líneas de artículo.

**Configuración y automatización**

- El script "Establecer suborganización" se convierte en una regla de
  transformación.
- Las columnas estándar pueden eliminarse de un tipo de documento.

**Exportación**

- El historial de exportación vuelve a listar los documentos exportados.
- Las facturas de flete se exportan a Infor LN.

---

## R1.3 — Sandbox 8 de febrero de 2027 · Producción 17 de febrero de 2027

**Rule Manager de Auto Accounting**

- Las reglas asignan cuentas y dimensiones automáticamente, con ámbito por
  suborganización y tipo de documento, y una pantalla de auditoría muestra qué
  regla se activó.
- Una regla puede rellenar un valor a partir de una columna de línea de tabla.
- Los campos y las dimensiones pueden vaciarse individualmente, las líneas de
  artículo pueden eliminarse (incluidas las líneas sin importe), y las reglas
  siguen funcionando en campos que cambiaron de texto a lista desplegable.

**Coincidencia de órdenes de compra**

- El icono de coincidencia navega, desplaza y resalta entre pestañas, incluidas
  las coincidencias de uno a varios.
- Conversión de unidades con alias (por ejemplo KG y TO), una varianza de
  redondeo configurable con una cuenta de redondeo, y cálculos con cuatro
  decimales mostrados como tres.

**Exportación**

- Nombres de archivo de exportación configurables.
- Un documento incompleto en Infor LN se elimina tras una exportación fallida.
- El conector de base de datos incluye todas las tablas relevantes.

---

## R1.4 — Sandbox 7 de abril de 2027 · Producción 15 de abril de 2027

**Importación**

- Un mecanismo de reintento para la importación FTP, de correo y de correo
  entrante, con reprocesamiento automático y manual.

**DocNet Agents**

- Entrada de pedidos: un pedido de cliente se convierte en una orden de venta
  en Infor M3 o Infor LN (primera versión, documentos de texto).

**Aprobación**

- Un flujo de aprobación mejorado, delegación a otro usuario durante la
  aprobación, y un botón "Exportar y siguiente".

**Coincidencia de órdenes de compra**

- En la pantalla de coincidencia solo se ofrecen las líneas de OC viables.
- Las facturas emparejadas en exceso, en las que la cantidad facturada supera
  la cantidad recibida, se reconocen en la pantalla de coincidencia, y las
  unidades de medida se convierten durante la coincidencia de la factura.

**Otros**

- Ronda de comentarios sobre el Rule Manager.
- El formulario de tickets de soporte acepta adjuntos y vincula la organización
  automáticamente.
- Integración fiscal con Vertex ampliada.

---

## R1.5 — Sandbox 18 de mayo de 2027 · Producción 27 de mayo de 2027

**Auto Accounting**

- Acción de búsqueda del Rule Manager: coincidir con los datos maestros y
  asignar varios campos a la vez.
- Las predicciones admiten varios códigos de impuesto y dimensiones,
  comprobantes y referencias de contabilización.
- Pantallas de Auto Accounting en varios idiomas.

**Aprobación y coincidencia de órdenes de compra**

- Reasignar un documento a otro usuario.
- El orden de las columnas en la pantalla de coincidencia de OC se guarda por
  usuario.
- Los códigos de cargo (peaje, transporte, energía) se reconocen y su coste se
  distribuye.

**Controles de exportación**

- La exportación se bloquea con una advertencia cuando la cantidad emparejada
  supera o difiere demasiado de la cantidad recibida, o cuando la fecha de
  contabilización es anterior a la fecha de entrada en almacén.

**Usabilidad**

- El orden de ejecución de los scripts de documento es visible en el frontend.
- Intro y Tabulador permiten moverse entre los campos con el teclado.

---

## R1.6 — Sandbox 6 de julio de 2027 · Producción 15 de julio de 2027

**Configuración**

- La configuración admite búsquedas en todos los interruptores y subpáginas.
- La configuración del servidor de correo permite sustituir un secreto OAuth o
  de cliente caducado sin volver a configurar el buzón.
- El mapa de números de artículo de proveedor (tabla de conversión de números
  de artículo) puede rellenarse desde una importación CSV.

**Auto Accounting**

- Las dimensiones se almacenan en una nueva estructura para que los conjuntos
  grandes de dimensiones se carguen más rápido.

---

## R1.7 — Sandbox 21 de septiembre de 2027 · Producción 30 de septiembre de 2027

**Auto Accounting en la pantalla de aprobación**

- Los aprobadores pueden trabajar con Auto Accounting directamente en la
  pantalla de aprobación.
- La aprobación puede condicionarse a campos de contabilidad como el código de
  cuenta o el país, con una corrección de cuentas por pagar cuando se devuelve
  un documento.
- Una lista desplegable de códigos de impuesto en Auto Accounting sin necesidad
  de configurar varias líneas de impuestos.

---

## R2.0 — Sandbox por anunciar · Producción por anunciar

**Auto Accounting**

- Los campos basados en una lista también aceptan texto libre.
- Se validan los campos obligatorios.
- Las predicciones del modelo rellenan automáticamente los campos contables
  (modo híbrido con el modelo de predicción entrenado), con un registro de
  auditoría de lo que rellenó el modelo.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
