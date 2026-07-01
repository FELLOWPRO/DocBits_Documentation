# Notas de versión de DocBits — 26–30 de junio de 2026

_Lo que esta actualización de producción ofreció, explicado de forma sencilla. Cada
servicio muestra la versión que ahora está activa en producción. Los servicios que
no aparecen en la lista no tuvieron cambios visibles para el cliente en este período._

---

## Aspectos destacados

- **Una única conexión para los asistentes de IA (DocBits MCP).** Ahora una única
  puerta de enlace unificada sirve todas las herramientas de DocBits, incluida
  DocFlow, a través de la API principal, de modo que los asistentes de IA (Claude,
  Gemini CLI, Codex) se conectan mediante un único endpoint fiable en lugar de varios.
- **Búsqueda multilingüe en el panel más inteligente.** Los conectores de búsqueda
  (**AND / OR**) ahora aparecen en su idioma con resaltado por colores, los subtipos
  de factura ofrecen un desplegable de valores y los mensajes de sintaxis de búsqueda
  están traducidos, con un manejo del teclado más fluido en todo momento.
- **Aprobaciones y permisos más fluidos.** La aprobación ya no se activa cuando la
  unidad de embalaje de una confirmación de pedido está vacía, los usuarios normales
  pueden volver a aprobar elementos de costeo tras la migración del control de acceso,
  y los permisos a nivel de documento se aplican correctamente incluso cuando una
  columna de tabla ya existe.
- **La aplicación se actualiza sola.** Cuando se publica una nueva versión, DocBits
  ahora se recarga automáticamente en lugar de interrumpirle con una ventana emergente
  de “Actualizar ahora”.
- **Conciliación de pedidos de compra más robusta.** Las transformaciones de valores
  de columna, las protecciones frente a bloqueos en líneas sin precio o cantidad y el
  reintento automático ante conexiones de base de datos caídas hacen que la
  conciliación sea más estable.
- **Menos errores en general.** Se localizaron y corrigieron muchos errores de
  servidor poco frecuentes en los paneles, las facturas de proveedor, los registros de
  pedido (PO) y los trabajos de OCR.

---

## Web App — activa: `10.34.4`

- **Búsqueda rápida en el panel:** conectores **AND / OR** traducidos (de/fr) con
  resaltado de sintaxis por colores; desplegable de valores para el subtipo de
  factura; mensajes de error de sintaxis de búsqueda traducidos; experiencia de
  teclado más fluida; el aviso de “se requiere texto completo” ahora se muestra en
  línea para que el diseño ya no salte.
- **Aprobaciones y permisos:** se corrigió la aprobación activada por error cuando la
  unidad de embalaje de una confirmación de pedido está vacía; los usuarios normales
  pueden volver a aprobar elementos de costeo tras la migración del control de acceso;
  los permisos a nivel de documento ahora se aplican cuando una columna de tabla ya
  existe.
- **Actualización automática:** la aplicación se recarga automáticamente con una nueva
  versión en lugar de mostrar una ventana emergente de “Actualizar ahora”; se eliminó
  el antiguo diálogo de información de versión.
- **Configuración de correo entrante:** nueva opción y campo de destinatarios para las
  notificaciones de fallo; el registro de importación ahora muestra la actividad
  saliente y el motivo del fallo; la dirección de entrada se copia de forma fiable.
- **División de documentos:** la pantalla de división de documentos ahora permite
  desplazarse.
- **Modo oscuro:** correcciones para la extracción de tablas, el contador de tareas y
  los marcadores de documentos cerrados en el panel.
- **Usabilidad y estabilidad:** correcciones en la interfaz de exportación del panel;
  los encabezados de tabla fijos ya no se transparentan a través de los diálogos; el
  panel de DocNet ya no se bloquea ante una solicitud de estadísticas fallida; los
  scripts de campo ya no revierten los campos vaciados a sus valores anteriores;
  correcciones en las casillas de verificación y el diseño de la configuración de
  pedidos (PO); correcciones en la visualización de la lista de clasificación.
- **Proveedores:** las organizaciones de proveedores ahora pueden registrarse mediante
  un magic link.

## API Service — activa: `12.46.8`

- **Puerta de enlace de DocBits MCP:** ahora una puerta de enlace unificada actúa como
  proxy de las herramientas de DocFlow a través de la API principal, de modo que los
  asistentes de IA acceden a todas las herramientas de DocBits mediante un único
  endpoint; el endpoint de MCP se sirve sin una redirección que pudiera romper las
  conexiones.
- **Contabilidad:** se añadió la validación del centro de costes para el ID contable.
- **Enrutamiento de OCR:** los documentos se envían para un nuevo OCR completo cuando
  el texto electrónico (e-text) del proveedor está desactivado, de modo que el texto
  sigue siendo fiable.
- **Infor ERP / SAP:** los cargos adicionales se enrutan correctamente cuando el ERP
  ya tiene el cargo con importe cero.
- **Fiabilidad (menos errores de servidor):** se reforzaron las consultas del panel,
  de facturas de proveedor, de registros de pedido (PO) y del gestor de tareas para
  que ya no devuelvan errores 500 poco frecuentes; sincronización de la caché de
  organización y limpieza de archivos almacenados más resistentes.
- **Filtros del panel más limpios:** se eliminó el campo de filtro redundante de
  número de factura; se corrigió la cantidad conciliada de pedido (PO).
- **Documentación de la API para desarrolladores:** la Swagger UI ahora ofrece un
  desplegable de especificaciones (OpenAPI 3.0 más la vista Swagger 2.0 de Infor) con
  la marca de DocBits.

## Auth Service — activa: `1.68.0`

- **Cierre de sesión / revocación de tokens más rápidos:** la revocación masiva de
  tokens ya no tarda minutos ni cierra la conexión.
- **Se corrigieron los correos de establecimiento de contraseña** para que se muestren
  correctamente.
- **Proveedores:** las organizaciones de proveedores pueden registrarse con un magic
  link.
- **Estabilidad del inicio de sesión:** un miembro ya no queda bloqueado ante un fallo
  transitorio de búsqueda de organización, y un id de organización no válido ahora
  devuelve un mensaje claro en lugar de un error.

## Docflow Service — activa: `2.4.1`

- **Puerta de enlace de IA fiable:** se corrigieron los bloqueos y los tiempos de
  espera en el endpoint de DocFlow MCP (handshake, desconexiones del cliente,
  respuestas duplicadas): la parte de DocFlow de la puerta de enlace unificada de
  DocBits MCP.

## OCR Service — activa: `1.7.1`

- **Procesamiento de OCR más estable:** las colas de respuesta en segundo plano
  caducan automáticamente y se reintentan los fallos transitorios de conexión, de modo
  que menos trabajos de OCR se quedan atascados.

## PO Match Service — activa: `1.55.7`

- **Las transformaciones de valores** ahora se aplican en las columnas item-id,
  unit-code y valor estático durante la conciliación por reglas.
- **Protecciones frente a bloqueos:** una línea sin precio o cantidad, una combinación
  inusual de clave ponderada o una división imposible ya no bloquean la conciliación.
- **Fiabilidad:** las escrituras en la base de datos se reintentan automáticamente
  ante conexiones caídas o cerradas por SSL.
- **Infor ERP / SAP:** los cargos adicionales se enrutan correctamente cuando el ERP
  tiene el cargo con importe cero.

## Fulltext Service — activa: `1.35.6`

- **Reindexación más rápida:** todas las fases de sincronización ahora se distribuyen
  para que se active el autoescalado, lo que corrige la reindexación en serie lenta y
  un widget de progreso atascado en 0 %.
- **Estadísticas más estables:** las solicitudes de estadísticas de documentos entre
  regiones están acotadas para que ya no agoten el tiempo de espera.

---

## Sin cambios visibles para el cliente en este período

Estables, sin cambios destacables de producto entre el 26 y el 30 de junio: Auto
Accounting (`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`),
Extraction (`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting y FTP
solo recibieron mantenimiento interno.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
