# Notas de versión de DocBits — 14–29 de julio de 2026

_Lo que cambió en la actualización de producción de DocBits del 29 de julio de
2026 (la actualización del canal Nova), que abarca todo lo ocurrido desde la
versión del 14 de julio. Cada servicio indica la versión ahora activa y, a
continuación, las novedades o correcciones en lenguaje sencillo. Los servicios
que no aparecen en la lista no tuvieron cambios visibles para el cliente._

---

## Aspectos destacados

- **Autenticación de dos factores.** Las cuentas de DocBits pueden protegerse
  ahora con un segundo factor: una aplicación de autenticación (TOTP), un
  código de un solo uso por correo electrónico o una clave de acceso mediante
  Touch ID, Windows Hello, YubiKey y similares. Los códigos de respaldo cubren
  el caso de un dispositivo perdido, y un dispositivo de confianza puede
  omitir el segundo factor durante un tiempo. Cada usuario puede activarla por
  su cuenta; los administradores pueden exigirla para toda la organización.
  Consulte la
  [guía de Autenticación de Dos Factores](../two-factor-authentication.md).
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
- **Retirada del nivel de IA Turbo.** El modelo Turbo ha llegado al final de
  su vida útil. Quienes lo tenían seleccionado pasaron automáticamente a Fast;
  no se requiere ninguna acción.

---

## Web App — activa: `10.46.2`

### Inicio de sesión

- **Autenticación de dos factores:** configure una aplicación de
  autenticación, códigos por correo electrónico o una clave de acceso en su
  perfil, imprima códigos de respaldo y marque un dispositivo como de
  confianza para que no se lo pida cada vez. Los usuarios de claves de acceso
  pueden iniciar sesión sin contraseña alguna. Los administradores de la
  organización disponen de un interruptor de obligatoriedad y de una vista
  general de adopción que muestra quién se ha registrado.
- **Cuentas eliminadas:** iniciar sesión con una cuenta eliminada lo indica,
  en lugar de fallar con un error genérico.
- **SSO:** se corrigió un error al iniciar sesión con una región distinta
  seleccionada. Las sesiones SSO caducan ahora cuando lo indica el proveedor
  de identidad, y no según un temporizador local fijo.

### Trabajo con documentos

- **Documentos eliminados:** abrir un documento eliminado entretanto muestra
  un mensaje adecuado en lugar de errores de script.
- **Validación de Campos:** el campo de número de página es más ancho y salta
  a la página al pulsar Enter. Un campo convertido en solo lectura por un
  script sigue mostrando su conexión de campo. Una ventana emergente de aviso
  que mostraba código JavaScript en bruto muestra ahora el mensaje real, y la
  pantalla ya no se queda bloqueada en documentos con tablas de líneas de
  documentos electrónicos muy largas.
- **Extracción de tablas:** eliminar una columna libera su nombre para poder
  reutilizarlo, y las cabeceras eliminadas ya no reaparecen en la tabla
  guardada.
- **Aprobaciones:** al abrir un documento recién puesto en pendiente se llega
  a la pantalla de aprobación correcta. Los usuarios ya no pueden aprobar un
  paso de Sales Tax para el que su grupo no tiene permiso, y el historial de
  aprobaciones vuelve a mostrar todas las entradas. El historial también
  indica quién aprobó realmente, incluidas las aprobaciones que un
  administrador realizó en nombre del asignado.
- **Proveedores:** la página de contabilidad ya no muestra una advertencia
  falsa de "Supplier is missing" (falta el proveedor), y eliminar un
  proveedor que solo existe a partir de la extracción ya no deja el diálogo
  colgado.
- **Datos maestros:** las tablas de la página de datos maestros vuelven a
  permitir el desplazamiento.
- **Tareas y notificaciones:** eliminar una tarea ya no está reservado a los
  administradores. Que los usuarios sin derechos de administrador puedan
  eliminar sus propias tareas es ahora un ajuste de la organización, y los
  usuarios que tienen una tarea en un documento que no pueden abrir obtienen
  una vista limitada a la tarea en lugar de un error.

### Dashboard y búsqueda

- **Exportación:** las exportaciones usan el panel que tiene seleccionado, y
  la aplicación le avisa antes de exportar un panel con cambios sin guardar.
- **Búsqueda:** Invoice Type está disponible como campo de búsqueda con su
  lista de valores. Cuando un conjunto de resultados supera lo que el panel
  puede mostrar, el indicador de recuento lo señala en lugar de truncar los
  resultados en silencio.
- **Registro de importación:** los documentos divididos pueden encontrarse a
  través de su documento padre, y la columna Failed Filenames solo lista los
  archivos que realmente fallaron o se omitieron.

### Configuración y administración

- **Tickets de soporte:** cree un ticket directamente desde un registro de
  error. Los tickets incluyen el entorno y el canal de versión, y la captura
  de pantalla ya no se queda colgada.
- **Grupos y permisos:** los documentos sin clasificar pueden concederse como
  permiso igual que cualquier otro tipo de documento.
- **Workflow Builder:** las tarjetas recién creadas o renombradas, las
  plantillas de correo y otros elementos de listas desplegables aparecen de
  inmediato, sin recargar la página.
- **Árboles de decisión:** las etiquetas de los campos de documento en el
  diseñador siguen el idioma de la interfaz, en lugar de mostrar siempre el
  nombre en inglés.
- **Tipos de documento:** nuevo ajuste de Structured Extraction en la sección
  de extracción.
- **Códigos de impuestos de E-Doc:** nueva página de configuración para
  mapear sus códigos de impuestos del ERP para documentos electrónicos
  (véase Aspectos destacados).
- **Auto Accounting:** las dimensiones se muestran de forma fiable, y no de
  manera intermitente.
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

## API Service — activa: `12.68.1`

- **Autenticación de dos factores:** todas las vías de inicio de sesión
  basadas en contraseña pasan por la comprobación del segundo factor, de modo
  que ninguna ruta de integración la elude.
- **Códigos de impuestos de E-Doc:** mapeo de los códigos de impuestos del
  ERP para documentos electrónicos, con una comprobación central antes de la
  exportación para que los códigos ausentes se detecten pronto.
- **Control de acceso:** los administradores pueden conceder a usuarios sin
  derechos de administrador la visibilidad de los documentos sin clasificar.
- **Registro de auditoría de eliminaciones:** los documentos registran quién
  los eliminó y cuándo.
- **Paneles personales:** se corrigieron los ajustes de compartición que no
  se guardaban.
- **Búsqueda del panel:** Invoice Type se suma a los campos de búsqueda
  ampliados, y los documentos creados por una división por código de barras o
  QR se encuentran a través de su documento padre.
- **Actualidad del panel:** actualizar una tabla o reprocesar un documento
  vacía la caché del panel, de modo que la lista ya no muestra los valores
  anteriores al cambio.
- **Cargas:** las cargas repetidas del mismo archivo durante un reintento de
  red ya no crean documentos duplicados.
- **Búsqueda de proveedores:** los resultados llegan en cuanto los datos están
  listos, en lugar de tras una espera fija.
- **Exportación a Infor:** los precios unitarios conservan cuatro decimales.
  Las exportaciones a M3 pueden incluir cargos de línea con importe cero, y
  las líneas de coste negativas de LN se envían como abonos positivos. La
  exportación también espera a que termine un flujo de trabajo pendiente en
  lugar de ejecutarse en mitad del flujo.
- **Aprobaciones:** una aprobación solo se vincula a una solicitud de
  aprobación cuando el aprobador es su asignado. Los cambios que un flujo de
  trabajo realiza por su cuenta se atribuyen al usuario System y no a la
  última persona que tocó el documento.
- **Estabilidad del inicio de sesión:** un fallo temporal en la validación de
  tokens ya no cierra la sesión de los usuarios; la aplicación reintenta. Los
  documentos reciben el mismo tratamiento y ya no fallan de plano ante un
  contratiempo breve de autenticación.
- **Clasificación:** las reglas de origen ahora comparan contra todos los
  campos de origen del documento, no contra posiciones fijas.
- **Estabilidad de la validación:** un campo sin nombre ya no bloquea la
  validación del documento.
- **Modelos de IA:** el nivel Turbo (retirado) se reasigna a Fast en todas
  partes, incluidas las variantes ajustadas (fine-tuned), con una salvaguarda
  para que un modelo retirado nunca pueda ejecutarse.
- **Trabajos en segundo plano:** un planificador atascado se detecta y se
  reinicia, de modo que los trabajos recurrentes no pueden detenerse en
  silencio.

## Auth Service — activa: `1.75.3`

- **Autenticación de dos factores:** el backend que hay detrás de la entrada
  de Aspectos destacados. Aplicaciones de autenticación, códigos de un solo
  uso por correo electrónico, claves de acceso y dispositivos de confianza,
  además de códigos de respaldo, obligatoriedad por organización e inicio de
  sesión sin contraseña con clave de acceso. Registrarse cierra sus demás
  sesiones, cambiar la contraseña revoca los dispositivos de confianza, y los
  endpoints de verificación tienen límite de intentos, con bloqueo y una
  protección contra la reutilización de códigos.
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
  identidad ausentes. La duración del token que devuelve el proveedor se
  transmite ahora a la aplicación.
- **Tokens de sesión:** se corrigió que tokens de sesión de corta duración se
  rechazaran como inválidos aunque no hubieran caducado.
- **Herramientas de gestión:** la región de la organización es visible en la
  API de gestión, el usuario de sistema de una organización puede
  reasignarse, y la administración de planes y consumo cuenta con endpoints
  dedicados. Estos cambios afectan a las herramientas internas del personal
  de DocBits, no a la aplicación del cliente.

## Email Service — activa: `1.40.2`

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
- **Prueba de conexión:** probar un buzón IMAP que no responde falla con un
  mensaje de tiempo de espera al cabo de unos segundos, en lugar de acabar en
  un tiempo de espera de la pasarela.
- **Higiene de la bandeja de entrada:** los correos sin adjuntos se sacan de
  la bandeja de entrada en lugar de acumularse.
- **Sin duplicados al reintentar:** las cargas a la API de documentos llevan
  una clave de idempotencia, de modo que una entrega reintentada no puede
  crear el mismo documento dos veces.
- **Nombres de origen:** los orígenes de O365 con una carpeta configurada
  incluyen el correo de la cuenta en su nombre, para poder distinguir
  orígenes similares. La dirección del buzón se toma de la cuenta autenticada
  y no de un campo escrito a mano.
- **Mantenimiento del registro de importación:** las entradas del registro de
  importación se conservan durante 90 días y después se limpian
  automáticamente.

## PO Match Service — activa: `1.59.3`

- **Estado "tabla incompleta":** las facturas cuya tabla de líneas no se pudo
  mapear reciben su propio estado en lugar del engañoso "orden de compra no
  encontrada" (véase Aspectos destacados). El panel lo muestra con el icono
  de no coincidente.
- **Mejor detalle de errores:** los fallos de mapeo de tablas indican la
  columna concreta que no se pudo mapear.
- **Más rápido en facturas grandes:** la coincidencia basada en reglas agrupa
  los candidatos por número de artículo y lee los ajustes de tolerancia una
  vez por organización, en lugar de una vez por línea.
- **Comportamiento de API más limpio:** las solicitudes de reglas de PO
  inexistentes devuelven una respuesta correcta de "no encontrado", y las
  entradas de caché corruptas se descartan en lugar de causar errores
  repetidos.
- **Coincidencia por total:** se corrigió un error en la coincidencia contra
  el total de la orden de compra.

## Fulltext Service — activa: `1.39.1`

- **Formatos numéricos europeos:** los importes escritos con coma decimal
  (`1.234,56`) se normalizan antes de indexarse, de modo que las búsquedas y
  filtros por importe funcionan sea cual sea el formato numérico.
- **Recuentos de resultados honestos:** cuando una búsqueda encuentra más
  documentos de los que devuelve la ventana del panel, la respuesta lo indica
  en lugar de presentar una lista truncada como si estuviera completa.
- **Recuentos de ERP:** se corrigió un error de token que podía interrumpir
  el flujo de recuentos en vivo del panel.
- **Resiliencia de la indexación:** la indexación supera ahora los cortes
  temporales de la base de datos y del servicio de autenticación (reintento
  automático, retorno a la base de datos primaria) y descarta los mensajes de
  cola malformados en lugar de reintentarlos indefinidamente.

## OCR Service — activa: `1.10.3`

- **Orden de lectura estable:** el texto se lee en un orden determinista, de
  modo que un mismo documento se extrae siempre de la misma manera.
- **Documentos grandes:** el tiempo asignado al OCR escala con el tamaño del
  documento, de modo que los archivos muy grandes ya no fallan por exceder el
  tiempo de espera.
- **Caracteres inusuales:** un saneador limpia los caracteres que el motor de
  OCR no puede representar, lo que corrige fallos en documentos con símbolos
  exóticos.
- **Menos fallos transitorios:** los errores temporales de conexión al
  almacenamiento se reintentan automáticamente, y un proceso de trabajo
  atascado se detecta según esté consumiendo trabajo realmente o no.

## Extraction Service — activa: `1.53.3`

- **Facturas de EE. UU. sin impuestos:** se corrigió un caso en el que el par
  correcto de neto/impuesto se descartaba cuando el importe del impuesto es
  cero.
- **Extracción de tablas:** las tablas permanecen editables cuando el mapeo
  configurado espera más columnas de las que ofrece el documento, y se
  corrigió un fallo con datos de fila inusuales.
- **Orden de lectura estable:** refleja el cambio del OCR descrito arriba, de
  modo que la extracción ve el mismo orden de tokens que produjo el OCR.
- **Modelos de IA:** retirada del nivel Turbo, replicada desde el API
  Service.

## Docflow Service — activa: `2.7.3`

- **Coincidencia de PO en flujos de trabajo:** los valores de comparación
  ausentes se tratan como datos faltantes y no como una discrepancia.
- **Tarjetas de confirmación de pedido:** el comprador y la persona
  responsable se resuelven de forma fiable.
- **Tarjetas de oferta:** el registro anota ahora cuándo existe un precio
  ofertado que queda fuera del rango de fechas permitido, algo que antes
  parecía una falta de datos.
- **Cargos de transporte:** cuando ninguna de las partes tiene cargos, el
  caso se resuelve mediante la tarjeta del operador en lugar de quedarse
  atascado.
- **Seguridad:** los tokens de API de flujos de trabajo se validan contra la
  organización a la que pertenecen.
- **Activación más rápida:** la comprobación de flujos de trabajo activos se
  guarda en caché, y los procesos de trabajo en segundo plano se reinician
  limpiamente en lugar de dejar procesos atascados.

## Barcode Service — activa: `1.18.1`

- **Divisiones de larga duración:** la conexión con la cola de tareas se
  mantiene viva durante los trabajos largos de códigos de barras, de modo que
  dividir lotes grandes ya no se atasca cerca del final.

## FTP Service — activa: `1.31.2`

- **Mantenimiento del registro de importación:** la misma retención y
  limpieza de 90 días que en el Email Service.

## Auth Bridge Service — activa: `0.4.1`

- **Alertas de replicación precisas:** el puente de replicación de cuentas
  entre la UE y EE. UU. mide un bloqueo desde el último progreso real y no
  desde el primer error, y solo cuenta como progreso el movimiento real de
  replicación. Desaparecen las falsas alertas nocturnas de "bridge stalled".
  Nada cambia en la aplicación.

## Operator Service — activa: `1.42.1`

- **Estabilidad de los procesos de trabajo:** un proceso de trabajo atascado
  se detecta según esté consumiendo trabajo realmente o no, y se desactiva la
  comunicación ociosa entre procesos.

---

## Sin cambios en esta versión

**Auto Accounting** (`1.21.1`) se reconstruyó sin cambios visibles para el
cliente. **Docnet** (`1.55.1`) e **Ideas** (`0.3.1`) no presentan cambios en
este período.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
