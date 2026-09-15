# Hoja de ruta de DocBits

_Estado de la planificación a 15 de septiembre de 2026. Cada versión indica la
fecha prevista en sandbox (cuando los clientes pueden probarla) y la fecha
prevista en producción. Los temas describen lo que está previsto para la
versión, no lo que ya se ha publicado; el alcance y las fechas pueden cambiar.
Las correcciones urgentes entre versiones se documentan en las
[Notas de versión](release-notes/README.md)._

| Versión | Sandbox | Producción |
|---|---|---|
| R1.1 | 16 de septiembre de 2026 | 23 de septiembre de 2026 |
| R1.2 | 21 de octubre de 2026 | 28 de octubre de 2026 |
| R1.3 | 25 de noviembre de 2026 | 2 de diciembre de 2026 |
| R1.4 | 27 de enero de 2027 | 3 de febrero de 2027 |
| R1.5 | 10 de marzo de 2027 | 17 de marzo de 2027 |

---

## R1.1 — Sandbox 16 de septiembre de 2026 · Producción 23 de septiembre de 2026

**Reglas de transformación y layouts**

- Un motor de reglas para los valores extraídos de campos y columnas:
  establecer, reemplazar o derivar valores con grupos de condiciones anidados,
  con una pantalla de configuración para gestionar las reglas. Las reglas de
  selección de layout reciben las mismas condiciones anidadas.
- La selección de layout funciona con independencia del origen del documento.
- Reglas de precedencia claras para las etiquetas de campo en los campos de
  cabecera y en las columnas de tabla.

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
  avanzados, y los pasos de flujo de trabajo que cambian un campo o una casilla
  se aplican de forma fiable.
- Los correos de aprobación llegan a los aprobadores asignados en los flujos de
  trabajo de facturas de compra.
- Cada cambio de estado de un documento queda registrado.

**Importación**

- La importación de correo mueve un mensaje fuera de la bandeja de entrada solo
  después de confirmarse la carga, trata un reenvío entregado de nuevo como una
  única entrega, registra quién guardó por última vez y acepta correos firmados
  con S/MIME.
- La importación FTP recibe una verdadera opción de eliminar tras importar,
  junto a mover y archivar.
- La carga desde la app de escáner vuelve a funcionar.

**Procesamiento de documentos y extracción**

- Cuando el servicio de códigos de barras se bloquea, el documento muestra el
  error en lugar de permanecer indefinidamente en "Procesando".
- "Restringir a páginas" solo limita el OCR y el recuento de páginas; ya no
  recorta páginas del documento.
- Guardar un documento deja intactos los datos no relacionados.
- Un nuevo nivel de modelo de IA más económico ("Eco") para la extracción, y
  la aplicación de etiquetas de tabla en la tabla de IA vuelve a funcionar.
- Fusionar un PDF ZUGFeRD con otro PDF conserva los datos de la factura
  electrónica; se ajustan las plantillas de documentos electrónicos UBL;
  correcciones de extracción para importes, tipos impositivos y números de
  orden de compra en layouts de proveedores concretos.
- Se reconocen formatos de fecha adicionales.

**Coincidencia de órdenes de compra**

- La coincidencia requiere una columna de cantidad, usa el precio por cantidad
  de unidad base, y el respaldo a la última línea puede activarse o
  desactivarse por cliente.
- La pantalla de documentos electrónicos ya no se congela con facturas de más
  de 250 líneas.
- Los diagnósticos miden la cantidad incluso cuando una línea de OC no tiene
  precio.

**Touchless Intelligence**

- Más detalle en el informe Touchless, y un bloqueo por orden de compra se
  notifica como tal en lugar de como un fallo de validación de campo.

**Dashboard**

- El dashboard puede contener hasta 10.000 documentos por búsqueda.
- La fecha de vencimiento del descuento y la fecha de vencimiento de la factura
  están disponibles como campos de layout y se rellenan en la importación.
- Los usuarios compartidos de un dashboard se conservan al guardarlo;
  "Asignado a" y "Actualizado por" muestran la persona correcta.
- Los permisos de documento se aplican también al índice de texto completo.

**Exportación y EDI**

- La exportación BOD conserva los valores de columna de tabla de más de 30
  caracteres.
- Un paso adicional de exportación a Infor M3 para información adicional de la
  factura, y precios unitarios en las exportaciones de tipo de línea 5.
- Reimportar una recepción de entrega ya no falla por una clave duplicada.
- Se actualizan los mapeos EDI X12 para factura (810), orden de compra (850),
  confirmación de pedido (855), aviso de envío (856, incluida la exportación
  WMS) y orden de cambio (860).

**Seguridad**

- Los mapeos de plan de cuentas de proveedor se almacenan con parámetros SQL
  vinculados, y la protección de organización para las claves de API se aplica
  en todos los entornos.

---

## R1.2 — Sandbox 21 de octubre de 2026 · Producción 28 de octubre de 2026

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
- Un flujo de solicitud de cambio de OC y el propietario del documento en el
  mapeo de exportación a Infor.

**Exportación**

- El historial de exportación vuelve a listar los documentos exportados.
- Las facturas de flete se exportan a Infor LN.

---

## R1.3 — Sandbox 25 de noviembre de 2026 · Producción 2 de diciembre de 2026

**Rule Manager de Auto Accounting**

- Las reglas asignan cuentas y dimensiones automáticamente, con ámbito por
  suborganización y tipo de documento, y una pantalla de auditoría muestra qué
  regla se activó.
- Una regla puede rellenar un valor a partir de una columna de línea de tabla.
- Los campos y las dimensiones pueden vaciarse individualmente, las líneas sin
  importe pueden eliminarse, y las reglas siguen funcionando en campos que
  cambiaron de texto a lista desplegable.

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

## R1.4 — Sandbox 27 de enero de 2027 · Producción 3 de febrero de 2027

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
- Varias entradas de almacén pueden coincidir con una misma línea de factura, y
  las unidades de medida se convierten durante la coincidencia de la factura.

**Otros**

- Ronda de comentarios sobre el Rule Manager.
- El formulario de tickets de soporte acepta adjuntos y vincula la organización
  automáticamente.
- Integración fiscal con Vertex ampliada.

---

## R1.5 — Sandbox 10 de marzo de 2027 · Producción 17 de marzo de 2027

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

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
