# Notas de versión de DocBits — 30 de junio – 3 de julio de 2026

_Lo que esta actualización de producción ofreció, explicado de forma sencilla. Cada
servicio muestra la versión que ahora está activa en producción. Los servicios que
no aparecen en la lista no tuvieron cambios visibles para el cliente en este período._

---

## Aspectos destacados

- **Chat de IA en los Registros de Actividad.** Un nuevo panel de chat de IA en la
  página de Registros de Actividad le permite hacer preguntas sobre la actividad de
  los registros directamente, sin tener que revisar las entradas en bruto.
- **Seguimiento de importación de correo saliente.** El Registro de Importación ahora
  registra el correo saliente junto con el entrante, con chips de filtro rápido para
  Errores / Entrante / Saliente: los buzones con fallos se desactivan automáticamente
  tras fallos repetidos, los administradores pueden recibir una notificación por
  correo electrónico cuando falla una importación, y los reintentos ahora se ejecutan
  hasta 15 veces a lo largo de aproximadamente 5 horas antes de desistir.
- **Errores de importación de correo más claros.** Los fallos de inicio de sesión
  ahora muestran el motivo real subyacente, con mensajes específicos para un
  certificado no válido o una contraseña de aplicación de Gmail incorrecta.
- **Bucle de inicio de sesión corregido.** Algunos usuarios podían quedar atrapados
  en un bucle repetido de inicio de sesión durante la renovación del token; esto ya
  se ha solucionado.
- **Procesamiento de documentos más estable.** Se corrigió un bloqueo durante la
  extracción de datos provocado por valores de coordenadas sin redondear, la lectura
  de códigos de barras ahora reintenta los fallos recuperables en lugar de abandonar
  silenciosamente, y se corrigió un caso poco frecuente en el que un documento podía
  exportarse dos veces al mismo tiempo.
- **Mejoras en la pantalla de validación.** Ahora puede ampliar más el zoom de los
  documentos, los campos ya no se vacían por scripts cuando su valor en realidad no
  ha cambiado, y el panel recuerda la posición de página al volver atrás.

---

## Web App — activa: `10.35.7`

- **Panel de chat de IA** añadido a la página de Registros de Actividad (#15512).
- **Registro de Importación:** nuevos chips de filtro rápido Errores / Entrante /
  Saliente; conmutador de destinatarios de notificación de fallos y campo para la
  configuración de correo entrante.
- **Pantalla de validación:** el zoom del documento ahora va más allá del tamaño
  predeterminado anterior; los campos vaciados por scripts de validación ahora
  conservan correctamente su valor cuando el script devuelve el mismo valor.
- **Panel:** la posición de página se conserva al volver a la tabla; el controlador
  de redimensionado de columnas ya no se desborda fuera del encabezado de la tabla.
- **Pantalla de Contabilidad Automática:** se corrigió un error de validación.
- **Tareas de DocBits:** se corrigió un problema de permisos.
- **Registros de Watchdog:** se añadió un filtro de rango de fechas y un selector
  ajustable de filas por página.
- **Correcciones:** un error de gráfico ("Element not found") en la página de
  Boards; un enlace roto de exportación-eliminación en Registros de Actividad;
  correcciones de diseño en la pantalla de Layout Builder; una traducción faltante
  en el filtro de rango de fechas de Registros de Actividad.
- **Actualización automática:** se siguió reforzando el mecanismo de actualización
  automática de la aplicación (limpieza de arranque más rápida, detección de
  versión más fiable, purga de caché antes de una recarga de recuperación).

## API Service — activa: `12.48.1`

- **Carga más rápida de scripts de documento:** los scripts de validación ahora se
  almacenan en caché en el servidor (caché de 6 horas) en lugar de obtenerse cada
  vez.
- **Confianza de importe más precisa:** el cálculo de confianza ahora tiene en
  cuenta los documentos que usan distintas convenciones de separador decimal.
- **Fiabilidad:** la validación de documentos siempre ejecuta la única versión de
  script activa, y ahora se registra qué versión se ejecutó; se corrigió un caso
  poco frecuente en el que un documento podía exportarse dos veces al mismo tiempo;
  las reglas de extracción específicas de proveedor vuelven a aplicarse
  correctamente tras un nuevo OCR forzado.
- **Importación de correo:** se añadió soporte de backend para el registro de
  correo saliente y los correos de notificación de fallos (véase Email Service, a
  continuación).

## Auth Service — activa: `1.68.5`

- **Se corrigió un bucle de inicio de sesión** que algunos usuarios podían sufrir
  mientras se renovaba el token de su sesión.
- **Pantallas de administración de organización más rápidas:** los datos de
  usuarios y suscripciones ahora se cargan en bloque en lugar de un registro a la
  vez.
- **Se corrigió un conflicto poco frecuente de base de datos** al vincular un
  usuario a una organización.

## Email Service — activa: `1.37.4`

- **El Registro de Importación ahora registra el correo saliente** además del
  entrante, con un filtro para mostrar solo importaciones entrantes, salientes o
  fallidas.
- **Los buzones con fallos ahora se desactivan automáticamente** tras fallos
  repetidos, y los administradores pueden recibir una notificación por correo
  electrónico cuando falla una importación; los reintentos ahora se ejecutan hasta
  15 veces a lo largo de aproximadamente 5 horas antes de desistir.
- **Mensajes de fallo de inicio de sesión más claros:** muestra el motivo real
  subyacente, un mensaje específico para un certificado no válido y un mensaje
  concreto para una contraseña de aplicación de Gmail incorrecta.
- **Se corrigió el enrutamiento entrante** que reescribía incorrectamente las
  direcciones de servidor de las cuentas de la región de la UE.
- Mayor resiliencia frente a caídas breves de la conexión a Redis.

## Extraction Service — activa: `1.49.0`

- **Se corrigió un bloqueo durante la extracción** provocado por valores de
  coordenadas sin redondear.
- **Confianza de importe más precisa** para documentos con formatos de separador
  decimal mixtos; las pequeñas diferencias de redondeo en el total de impuestos ya
  no bloquean una coincidencia.

## Docflow Service — activa: `2.4.2`

- **Se rediseñó la autenticación para los flujos de trabajo avanzados (basados en
  Celery)**, con protecciones para que un fallo en la comprobación de autenticación
  ya no pueda bloquear la ejecución de un flujo de trabajo.
- **Respuesta más clara** cuando un paso de flujo de trabajo intenta ejecutarse
  contra un flujo de trabajo que ya no existe.

## Barcode Service — activa: `1.15.7`

- **La lectura de códigos de barras ahora reintenta automáticamente** los fallos
  recuperables en lugar de abandonar silenciosamente.

## OCR Service — activa: `1.7.3`

- **Se corrigió un fallo de OCR** provocado por un problema de resolución de
  nombre de host de Redis.
- Las desconexiones de Redis durante las comprobaciones de estado ya no se
  registran como errores, lo que reduce las falsas alertas.

## PO Match Service — activa: `1.55.8`

- **Se corrigió la falta de aparición de notas** en los registros de PO Match.

---

## Sin cambios visibles para el cliente en este período

Estables, sin cambios destacables de producto entre el 30 de junio y el 3 de
julio: Auto Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext
(`1.35.7`), Operator (`1.39.5`). Auto Accounting solo recibió mantenimiento
interno de configuración de despliegue. No fue posible contactar con Ideas
Service para una comprobación de versión durante este período.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
