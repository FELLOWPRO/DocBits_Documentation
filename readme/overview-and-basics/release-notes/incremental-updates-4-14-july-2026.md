# Notas de versión de DocBits — 4–14 de julio de 2026

_Un resumen de lo que ha cambiado para usted en esta versión de DocBits. Cada
servicio a continuación muestra la versión que se está desplegando ahora,
seguida de las novedades o correcciones explicadas en lenguaje sencillo — sin
números de ticket ni jerga de ingeniería. Los servicios que no aparecen en la
lista no tuvieron cambios visibles para el cliente en este período._

---

## Aspectos destacados

- **Inicio de sesión multiorganización.** Los usuarios que pertenecen a varias
  organizaciones ahora disponen de un selector de organización adecuado al
  iniciar sesión, un conmutador de organización en la cabecera y un ajuste de
  organización predeterminada. Las sesiones se vinculan de forma segura a una
  organización a la vez, y la aplicación sigue automáticamente la región de la
  organización activa. Iniciar sesión contra la región equivocada ahora
  reintenta automáticamente la correcta en lugar de fallar.
- **Canales de versión (frozen / latest).** Las organizaciones ahora pueden
  fijarse a una versión estable ("frozen") mientras otras reciben las
  actualizaciones más recientes — lo que permite despliegues controlados. El
  diálogo de Versiones de servicio muestra una nueva columna *Release*, y los
  administradores gestionan el canal desde la Información de la empresa.
  Varios servicios muestran saltos de versión mayores en este período debido
  únicamente a la nueva numeración de versiones por canal — esos saltos no
  conllevan ningún cambio funcional.
- **Motores de reglas configurables.** Llegan tres nuevos sistemas de reglas a
  la API (cada uno desactivado por defecto, habilitable por organización):
  **reglas de validación** que comprueban los valores extraídos y marcan los
  fallos directamente en el documento, **reglas de transformación** que
  limpian o reescriben automáticamente los valores extraídos de campos y
  tablas, y **selección de diseño basada en reglas** que elige el diseño de
  documento correcto mediante reglas en lugar de según el origen del
  documento.
- **Transparencia en la importación de correo electrónico.** El registro de
  importación de correo ahora muestra una fila desplegable por adjunto, indica
  qué documentos se crearon (con botones que llevan directamente a ellos en el
  panel), marca los elementos omitidos y divididos, y permite descargar el
  correo original como archivo `.eml`.
- **Extracción de tablas con IA.** Un nuevo modo de extracción estructurada
  con IA para tablas, con una casilla "Usar IA" por tabla y por columna en la
  configuración del Tipo de documento.
- **Estabilidad de la Web App.** Se corrigió un bucle infinito de recarga tras
  una sesión caducada, se corrigió el Layout Builder, que estaba roto, y las
  tablas de extracción ahora cuentan con un control de altura arrastrable.
- **Novedad: Auth Bridge Service.** Un nuevo servicio mantiene los datos de
  inicio de sesión sincronizados de forma continua entre las regiones de la UE
  y de EE. UU., con autorreparación y monitorización integradas.

---

## API Service — activa: `12.57.8`

- **Reglas de validación (novedad, por organización):** un motor de reglas
  configurable por el administrador comprueba los valores extraídos (totales,
  campos obligatorios y más) y marca los fallos directamente en el documento,
  indicando qué regla se activó. Las reglas se pueden probar en un ensayo
  (dry run) antes de habilitarlas, se pueden activar por tipo de documento y
  se entregan con un catálogo inicial de reglas predeterminadas (todas
  desactivadas hasta que usted decida activarlas).
- **Reglas de transformación (novedad, por organización):** limpian o
  reescriben automáticamente los valores extraídos de campos y tablas durante
  el procesamiento — configurables por tipo de documento o para toda la
  organización.
- **Selección de diseño basada en reglas (novedad):** los diseños de documento
  ahora pueden elegirse mediante reglas configurables en lugar de estar
  ligados al origen del documento. El comportamiento existente basado en el
  origen se migra automáticamente, las plantillas de diseño pueden renombrarse
  y se evitan los títulos de diseño duplicados.
- **Exportaciones del panel más rápidas:** las exportaciones lanzadas desde el
  panel ahora se envían a un worker dedicado en lugar de esperar a un ciclo de
  sondeo, por lo que comienzan de inmediato.
- **Corregido el bloque de exportación de Detección de duplicados:** el bloque
  de exportación para presuntos duplicados vuelve a funcionar.
- **Ajustes que no se guardaban:** se corrigió que las preferencias guardadas
  ocasionalmente no persistieran cuando existía una copia antigua eliminada
  del mismo ajuste.
- **Documentos con caracteres inusuales:** se corrigieron errores de guardado
  causados por caracteres NUL invisibles en los datos extraídos.
- **"Actualizado por" correcto:** los documentos cargados automáticamente como
  documentos electrónicos ya no muestran un usuario del sistema como último
  editor — el campo permanece vacío hasta que una persona edita realmente.
- **PDF escaneados con una buena capa de texto:** una nueva opción permite que
  DocBits confíe en el texto ya incrustado en una página escaneada en lugar de
  volver a ejecutar el OCR — más rápido y, a menudo, más preciso.
- **Facturas electrónicas:** detección más robusta del XML incrustado cuando
  el archivo original necesita volver a comprobarse.
- **Tareas:** nuevo conmutador de organización que permite a los usuarios no
  administradores usar el filtro "Todos" en la lista de tareas.
- **Coincidencia de líneas de pedido:** el comportamiento de coincidencia
  difusa ahora es configurable por línea.
- **Estabilidad:** las conexiones WebSocket se cierran limpiamente ante
  errores en lugar de provocar excepciones en el servidor; la sincronización
  de la caché de permisos se verifica y se repara a sí misma; la versión del
  servicio ahora es visible en el endpoint de salud.

## Auth Service — activa: `1.71.1`

- **Inicio de sesión multiorganización:** el inicio de sesión ahora pregunta a
  qué organización entrar cuando un usuario pertenece a varias, las sesiones
  se vinculan a esa organización, y nuevos endpoints permiten seleccionar,
  cambiar y establecer una organización predeterminada. Las membresías de
  organización duplicadas o en conflicto se depuraron y ahora se evitan a
  nivel de base de datos, con búsquedas de membresía más rápidas.
- **Correcciones de la organización predeterminada:** al iniciar sesión se
  selecciona automáticamente su organización predeterminada (no una
  arbitraria), y cambiar la predeterminada surte efecto de inmediato en lugar
  de mostrar datos de perfil obsoletos.
- **Cierre de sesión corregido:** se resolvió un error de servidor (HTTP 500)
  al cerrar sesión y se restauró el endpoint de revocación de tokens.
- **Seguridad de tokens:** la verificación y el almacenamiento en caché de
  tokens ahora respetan la organización para la que se emitió el token, y la
  revocación de tokens está centralizada.
- **Canales de versión:** el canal de versión de la organización se almacena
  aquí, es gestionable por los administradores de la organización y se expone
  a la aplicación y a la capa de enrutamiento.

## Auth Bridge Service — activa: `0.2.4.2` _(nuevo servicio)_

- **Qué es:** un nuevo servicio que replica continuamente los datos de
  autenticación entre las regiones de la UE y de EE. UU., de modo que las
  cuentas y los inicios de sesión se mantienen consistentes entre regiones.
- **Autorreparación:** detecta y repara desviaciones de datos entre regiones —
  incluyendo asegurarse de que las eliminaciones se propaguen — y se recupera
  automáticamente de pérdidas de conexión en lugar de perder datos.
- **Seguridad y monitorización:** un bucle anterior de replicación
  bidireccional se detuvo y ahora se detecta y bloquea de forma activa; el
  seguimiento de errores y las alertas están integrados; y el servicio informa
  de su versión en el diálogo de Versiones de servicio.

## Docflow Service — activa: `2.6.1`

- **Las tarjetas de flujo de trabajo aceptan valores vacíos:** las tarjetas de
  casilla de verificación y de socio comercial ya no fallan cuando un campo
  está legítimamente vacío; las comprobaciones de tipo de tarjeta son más
  estrictas y predecibles.
- **Los flujos de trabajo se vuelven a ejecutar ante cambios reales:** el
  bloqueo (lock) del flujo de trabajo vuelve a respetar el estado del
  documento del disparador, y ahora también rastrea la versión del documento —
  de modo que un documento cuyos datos cambiaron de verdad puede pasar de
  nuevo por el flujo de trabajo incluso con el mismo estado, mientras que los
  duplicados reales siguen bloqueados.
- **Flujos de trabajo avanzados más grandes:** se elevó el límite de nodos de
  flujo de trabajo y ahora es configurable por entorno.
- **Exportación alternativa:** las exportaciones alternativas disparadas por
  flujos de trabajo ahora se etiquetan como tales para que los sistemas
  posteriores puedan distinguirlas.
- **Resiliencia:** el servicio se reconecta automáticamente cuando una
  conexión a la base de datos se pierde durante su uso, tolera un broker de
  mensajes más lento en lugar de fallar, y las solicitudes de API fallidas
  ahora se registran con contexto completo e identificadores de ejecución
  rastreables.

## Email Service — activa: `1.38.4`

- **Registro de importación, reconstruido para la trazabilidad:** cada correo
  importado ahora registra qué documentos se crearon a partir de él, con filas
  de detalle por adjunto.
- **Descarga del correo original:** el mensaje original puede descargarse como
  archivo `.eml` directamente desde el registro de importación.
- **Recuperación de adjuntos:** la ruta de recuperación ante corrupción ahora
  también gestiona mensajes de texto plano, por lo que se recuperan más
  correos entrantes dañados en lugar de omitirse.

## Extraction Service — activa: `1.51.6`

- **Impuesto/neto ya no se intercambian:** se corrigió un caso en documentos
  de EE. UU. en el que el importe del impuesto podía asignarse como mayor que
  el importe neto cuando se encontraban varios pares candidatos.
- **Varios tipos impositivos por proveedor:** la extracción ahora gestiona
  proveedores cuyas facturas llevan distintos tipos impositivos en un mismo
  documento.
- **Extracción de tablas con IA (novedad, opcional):** endpoints de extracción
  estructurada con IA para tablas, activados por organización mediante un
  indicador de funcionalidad (feature flag).
- **Llamadas de IA más rápidas:** se ajustó la configuración del modelo de IA
  utilizado durante la extracción para evitar tiempos de procesamiento
  innecesarios.
- **Corrección de bloqueo:** se resolvió un error en documentos que producían
  una lista de candidatos vacía durante la extracción.

## Fulltext Service — activa: `1.37.2`

- **Migraciones del índice de búsqueda reparadas:** se restauraron
  definiciones de migración que se habían desviado, manteniendo fiables las
  actualizaciones del índice de búsqueda.
- Trabajo interno de enrutamiento para la nueva infraestructura de canales de
  versión.

## PO Match Service — activa: `1.58.2`

- **Coincidencia más tolerante:** la coincidencia de órdenes de compra ya no
  falla con datos inusuales — los números de artículo no textuales, las
  cantidades ausentes y los importes no textuales ahora se gestionan
  correctamente en lugar de producir errores.

## Web App — activa: `10.41.8`

- **Experiencia multiorganización:** nueva página de selección de organización
  al iniciar sesión, un icono dedicado de cambio de organización en la
  cabecera, ajustes de organización predeterminada, y la aplicación sigue la
  región de su organización activa. Iniciar sesión contra la región
  equivocada reintenta silenciosamente la región correcta y le dirige al
  selector de organización cuando es necesario.
- **Se acabaron las recargas infinitas:** se corrigió un bucle infinito de
  recarga que podía producirse cuando el servidor rechazaba un token de sesión
  almacenado — la aplicación ahora fuerza una renovación real del token en
  lugar de recargar indefinidamente.
- **Layout Builder corregido:** el Layout Builder vuelve a funcionar, y la
  selección de diseño se desacopló del origen del documento (en línea con la
  nueva selección basada en reglas de la API).
- **Tablas de extracción:** las tablas de líneas de pedido ahora tienen un
  control de redimensionado arrastrable para dar más espacio a la tabla
  durante la validación.
- **Registro de importación de correo:** nuevo estado de omitido e insignias
  de división, filas desplegables por adjunto, descarga del correo original y
  botones con el ID del documento que llevan directamente al panel filtrado
  por ese documento.
- **Búsqueda del panel:** el desplegable de valores de consulta ahora muestra
  la etiqueta localizada para los campos de lista de valores, y se rediseñaron
  los ejemplos de la ayuda de búsqueda.
- **Fiabilidad de los ajustes:** las preferencias de usuario ahora se cargan
  de forma fiable al iniciar sesión mediante SSO, y la confirmación de
  guardado solo se muestra cuando el guardado realmente se ha realizado con
  éxito.
- **Tareas:** el filtro "Todos" puede restaurarse para usuarios no
  administradores mediante un nuevo conmutador de organización.
- **Registros del watchdog:** ya no están limitados a 10 000 entradas, además
  de mejoras generales de usabilidad.
- **Tickets de soporte:** el formulario de soporte rellena previamente su
  dirección de correo electrónico a partir de su perfil.
- **Configuración del Tipo de documento:** nueva casilla "Usar IA" en tablas y
  columnas para controlar la extracción de tablas asistida por IA.
- **Diálogo de Versiones de servicio:** nueva columna *Release* que muestra el
  canal de cada servicio (frozen/latest), enrutada para que siga siendo rápida
  en las organizaciones fijadas.
- **Validación de Campos:** se corrigió un error al volver a la Validación de
  Campos desde otra pantalla, y el botón "Scripts" ya no dirige a una página
  404.

---

## Solo renumeración de versiones (sin cambios funcionales)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) e **Ideas Service** (`0.3.1`) fueron reversionados como parte de la
nueva infraestructura de canales de versión. Sus saltos de versión, que
parecen mayores, no conllevan cambios de funcionalidad ni de comportamiento en
este período. **Docnet Service** (`1.54.6`) no ha cambiado desde el 19 de
junio.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
