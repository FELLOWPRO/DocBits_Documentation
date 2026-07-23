# Notas de versión de DocBits — 14–23 de julio de 2026

_Lo que cambió en la actualización de producción de DocBits del 23 de julio de
2026 (la actualización del canal Nova), que abarca todo lo ocurrido desde la
versión del 14 de julio. Cada servicio indica la versión ahora activa y, a
continuación, las novedades o correcciones en lenguaje sencillo. Los servicios
que no aparecen en la lista no tuvieron cambios visibles para el cliente._

---

## Aspectos destacados

- **Tickets de soporte desde la pantalla de error.** Cuando algo falla, ahora
  puede abrir un ticket de soporte directamente desde el registro de error. El
  ticket ya incluye el contexto técnico, por lo que no tiene que describirlo.
- **Correo entrante en la región correcta.** Las organizaciones de EE. UU.
  reciben direcciones de importación entrante en su propia región, y los
  buzones de Microsoft 365 en tenants de nube nacional (GCC, 21Vianet y
  similares) ahora pueden configurarse con una selección de Cloud Instance.
- **Estado de coincidencia de PO más claro.** Las facturas cuya tabla de
  líneas no se pudo mapear se etiquetaban como "orden de compra no encontrada",
  lo que llevaba a buscar el problema equivocado. Ahora tienen su propio estado
  de "tabla incompleta", con detalle a nivel de columna de lo que no se pudo
  mapear.
- **Mapeo de códigos de impuestos para documentos electrónicos.** Una nueva
  página de configuración mapea sus códigos de impuestos del ERP para los
  documentos electrónicos, y las exportaciones comprueban el mapeo de
  antemano en lugar de fallar en el ERP.
- **Los cambios en scripts están protegidos con contraseña.** Los scripts
  personalizados pueden cambiar cómo se procesan los documentos, así que cada
  edición de un script requiere ahora una contraseña que rota cada hora. Pida
  la actual a su administrador.
- **Retirada del nivel de IA Turbo.** El modelo Turbo ha llegado al final de
  su vida útil. Quienes lo tenían seleccionado pasaron automáticamente a Fast;
  no se requiere ninguna acción.

---

## Web App — activa: `10.45.1`

### Trabajo con documentos

- **Documentos eliminados:** abrir un documento eliminado entretanto muestra
  un mensaje adecuado en lugar de errores de script.
- **Validación de campos:** el campo de número de página es más ancho y salta
  a la página al pulsar Enter. Un campo convertido en solo lectura por un
  script sigue mostrando su conexión de campo.
- **Extracción de tablas:** eliminar una columna libera su nombre para poder
  reutilizarlo, y las cabeceras eliminadas ya no reaparecen en la tabla
  guardada.
- **Aprobaciones:** los usuarios ya no pueden aprobar un paso de Sales Tax
  para el que su grupo no tiene permiso, y el historial de aprobaciones
  vuelve a mostrar todas las entradas. El historial también indica quién
  aprobó realmente, incluidas las aprobaciones que un administrador realizó
  en nombre del asignado.
- **Proveedores:** la página de contabilidad ya no muestra una advertencia
  falsa de "Supplier is missing" (falta el proveedor), y eliminar un
  proveedor que solo existe a partir de la extracción ya no deja el diálogo
  colgado.
- **Tareas y notificaciones:** la opción de eliminar queda oculta para los
  usuarios sin derechos de administrador.

### Panel y búsqueda

- **Exportación:** las exportaciones usan el panel que tiene seleccionado, y
  la aplicación le avisa antes de exportar un panel con cambios sin guardar.
- **Búsqueda:** Invoice Type está disponible como campo de búsqueda con su
  lista de valores.
- **Registro de importación:** los documentos divididos pueden encontrarse a
  través de su documento padre, y la columna Failed Filenames solo lista los
  archivos que realmente fallaron o se omitieron.

### Inicio de sesión

- **Cuentas eliminadas:** iniciar sesión con una cuenta eliminada lo indica,
  en lugar de fallar con un error genérico.
- **SSO:** se corrigió un error al iniciar sesión con una región distinta
  seleccionada.

### Configuración y administración

- **Tickets de soporte:** cree un ticket directamente desde un registro de
  error. Los tickets incluyen el entorno y el canal de versión, y la captura
  de pantalla ya no se queda colgada.
- **Workflow Builder:** las tarjetas recién creadas o renombradas, las
  plantillas de correo y otros elementos de listas desplegables aparecen de
  inmediato, sin recargar la página.
- **Tipos de documento:** nuevo ajuste de Structured Extraction en la sección
  de extracción.
- **Códigos de impuestos de E-Doc:** nueva página de configuración para
  mapear sus códigos de impuestos del ERP para documentos electrónicos
  (véase Aspectos destacados).
- **Selección de modelo de IA:** el nivel Turbo retirado desaparece del
  desplegable; las selecciones existentes muestran Fast.
- **Diálogo de versiones de servicio:** ahora permite desplazarse, incluye el
  servicio Auth Bridge y muestra los nombres de los canales de versión Vesta
  y Nova.
- **Página de importación:** ya no se bloquea en organizaciones con una
  entrada de suscripción vacía.

### Correcciones menores

Se suprimen las notificaciones emergentes vacías, el diálogo de nueva/editar
idea permite desplazarse, las casillas desalineadas en la configuración de
campos vuelven a estar alineadas, las eliminaciones de documentos bloqueadas
explican el motivo, y la configuración de E-Document gestiona sin problemas
el cambio de Default a Custom.

## API Service — activa: `12.64.3`

- **Seguridad de scripts:** los cambios en scripts requieren una contraseña
  temporal (véase Aspectos destacados).
- **Códigos de impuestos de E-Doc:** mapeo de los códigos de impuestos del
  ERP para documentos electrónicos, con una comprobación central antes de la
  exportación para que los códigos ausentes se detecten pronto.
- **Control de acceso:** los administradores pueden conceder a usuarios sin
  derechos de administrador la visibilidad de los documentos sin clasificar.
- **Paneles personales:** se corrigieron los ajustes de compartición que no
  se guardaban.
- **Búsqueda del panel:** Invoice Type se suma a los campos de búsqueda
  ampliados, y los documentos creados por una división por código de barras o
  QR se encuentran a través de su documento padre.
- **Cargas:** las cargas repetidas del mismo archivo durante un reintento de
  red ya no crean documentos duplicados.
- **Búsqueda de proveedores:** los resultados llegan en cuanto los datos están
  listos, en lugar de tras una espera fija.
- **Exportación a Infor:** los precios unitarios conservan cuatro decimales.
  Las exportaciones a M3 pueden incluir cargos de línea con importe cero, y
  las líneas de coste negativas de LN se envían como abonos positivos.
- **Aprobaciones:** una aprobación solo se vincula a una solicitud de
  aprobación cuando el aprobador es su asignado.
- **Estabilidad del inicio de sesión:** un fallo temporal en la validación de
  tokens ya no cierra la sesión de los usuarios; la aplicación reintenta.
- **Clasificación:** las reglas de origen ahora comparan contra todos los
  campos de origen del documento, no contra posiciones fijas.
- **Estabilidad de la validación:** un campo sin nombre ya no bloquea la
  validación del documento.
- **Modelos de IA:** el nivel Turbo (retirado) se reasigna a Fast en todas
  partes, incluidas las variantes ajustadas (fine-tuned), con una salvaguarda
  para que un modelo retirado nunca pueda ejecutarse.

## Auth Service — activa: `1.72.8`

- **Historial de inicios de sesión:** los inicios de sesión mediante
  SSO/SAML aparecen ahora en el historial de inicios de sesión, y la marca
  de tiempo del último acceso se registra de forma fiable para todos los
  tipos de inicio de sesión. Ver el historial de inicios de sesión de otro
  usuario requiere el nivel de administrador adecuado.
- **Cuentas heredadas:** eliminar una cuenta de usuario heredada vuelve a
  funcionar, en lugar de no hacer nada en silencio.
- **Administración masiva de usuarios:** añada usuarios existentes a
  suborganizaciones y grupos de forma masiva mediante CSV, emparejados por
  dirección de correo. También se corrigió un fallo con filas CSV rellenadas
  de forma desigual y un error de servidor al añadir dos o más usuarios
  nuevos a la vez.
- **Listas de miembros:** los usuarios eliminados ya no aparecen en las
  listas de miembros de las suborganizaciones.
- **Single sign-on:** una serie de mejoras de robustez. Los tokens caducados
  devuelven ahora una respuesta limpia de "caducado", las organizaciones sin
  configuración SAML reciben una respuesta correcta de "no encontrado" en
  lugar de un flujo de inicio de sesión equivocado, el cierre de sesión se
  completa siempre aunque la solicitud de cierre no pueda verificarse, y
  desaparecen varios fallos relacionados con configuraciones de proveedor de
  identidad ausentes.
- **Tokens de sesión:** se corrigió que tokens de sesión de corta duración se
  rechazaran como inválidos aunque no hubieran caducado.
- **Herramientas de gestión:** la región de la organización es visible en la
  API de gestión, el usuario de sistema de una organización puede
  reasignarse, y la administración de planes y consumo cuenta con endpoints
  dedicados. Estos cambios afectan a las herramientas internas del personal
  de DocBits, no a la aplicación del cliente.

## Email Service — activa: `1.39.9`

- **Importación en la región correcta:** los dominios de correo entrante
  existen por región, y los correos que llegan a la región equivocada se
  reenvían a la correcta. Las organizaciones de EE. UU. ya no dependen de la
  ruta de entrada de la UE.
- **Microsoft 365:** los tenants de nube nacional se configuran mediante una
  selección de Cloud Instance, lo que corrige las importaciones de O365 para
  clientes de EE. UU. Un tenant no válido produce ahora un error de inicio de
  sesión claro en lugar de un error de servidor, y unas credenciales de
  tenant incompletas fallan de inmediato con un mensaje en lugar de hacerlo
  en silencio.
- **Higiene de la bandeja de entrada:** los correos sin adjuntos se sacan de
  la bandeja de entrada en lugar de acumularse.
- **Sin duplicados al reintentar:** las cargas a la API de documentos llevan
  una clave de idempotencia, de modo que una entrega reintentada no puede
  crear el mismo documento dos veces.
- **Nombres de origen:** los orígenes de O365 con una carpeta configurada
  incluyen el correo de la cuenta en su nombre, para poder distinguir
  orígenes similares.
- **Mantenimiento del registro de importación:** las entradas del registro de
  importación se conservan durante 90 días y después se limpian
  automáticamente.

## PO Match Service — activa: `1.59.1`

- **Estado "tabla incompleta":** las facturas cuya tabla de líneas no se pudo
  mapear reciben su propio estado en lugar del engañoso "orden de compra no
  encontrada" (véase Aspectos destacados). El panel lo muestra con el icono
  de no coincidente.
- **Mejor detalle de errores:** los fallos de mapeo de tablas indican la
  columna concreta que no se pudo mapear.
- **Comportamiento de API más limpio:** las solicitudes de reglas de PO
  inexistentes devuelven una respuesta correcta de "no encontrado", y las
  entradas de caché corruptas se descartan en lugar de causar errores
  repetidos.
- **Coincidencia por total:** se corrigió un error en la coincidencia contra
  el total de la orden de compra.

## Fulltext Service — activa: `1.38.3`

- **Formatos numéricos europeos:** los importes escritos con coma decimal
  (`1.234,56`) se normalizan antes de indexarse, de modo que las búsquedas y
  filtros por importe funcionan sea cual sea el formato numérico.
- **Recuentos de ERP:** se corrigió un error de token que podía interrumpir
  el flujo de recuentos en vivo del panel.
- **Resiliencia de la indexación:** la indexación supera ahora los cortes
  temporales de la base de datos y del servicio de autenticación (reintento
  automático, retorno a la base de datos primaria) y descarta los mensajes de
  cola malformados en lugar de reintentarlos indefinidamente.

## OCR Service — activa: `1.9.9`

- **Documentos grandes:** el tiempo asignado al OCR escala con el tamaño del
  documento, de modo que los archivos muy grandes ya no fallan por exceder el
  tiempo de espera.
- **Caracteres inusuales:** un saneador limpia los caracteres que el motor de
  OCR no puede representar, lo que corrige fallos en documentos con símbolos
  exóticos.
- **Menos fallos transitorios:** los errores temporales de conexión al
  almacenamiento se reintentan automáticamente.

## Extraction Service — activa: `1.52.0`

- **Facturas de EE. UU. sin impuestos:** se corrigió un caso en el que el par
  correcto de neto/impuesto se descartaba cuando el importe del impuesto es
  cero.
- **Extracción de tablas:** las tablas permanecen editables cuando el mapeo
  configurado espera más columnas de las que ofrece el documento, y se
  corrigió un fallo con datos de fila inusuales.
- **Modelos de IA:** retirada del nivel Turbo, replicada desde el API
  Service.

## Docflow Service — activa: `2.7.2`

- **Coincidencia de PO en flujos de trabajo:** los valores de comparación
  ausentes se tratan como datos faltantes y no como una discrepancia.
- **Tarjetas de confirmación de pedido:** el comprador y la persona
  responsable se resuelven de forma fiable.
- **Cargos de transporte:** cuando ninguna de las partes tiene cargos, el
  caso se resuelve mediante la tarjeta del operador en lugar de quedarse
  atascado.
- **Seguridad:** los tokens de API de flujos de trabajo se validan contra la
  organización a la que pertenecen.
- **Activación más rápida:** la comprobación de flujos de trabajo activos se
  guarda en caché, y los procesos de trabajo en segundo plano se reinician
  limpiamente en lugar de dejar procesos atascados.

## Barcode Service — activa: `1.17.4`

- **Divisiones de larga duración:** la conexión con la cola de tareas se
  mantiene viva durante los trabajos largos de códigos de barras, de modo que
  dividir lotes grandes ya no se atasca cerca del final.

## FTP Service — activa: `1.31.2`

- **Mantenimiento del registro de importación:** la misma retención y
  limpieza de 90 días que en el Email Service.

---

## Sin cambios en esta versión

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) e **Ideas** (`0.3.1`) no presentan
cambios en este período.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
