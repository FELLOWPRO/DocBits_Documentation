# Notas de versión de DocBits — 21–25 de junio de 2026

_Lo que esta actualización de producción ofreció, explicado de forma sencilla. Cada
servicio muestra la versión que ahora está activa en producción. Los servicios que
no aparecen en la lista no tuvieron cambios visibles para el cliente en este período._

---

## Aspectos destacados

- **Búsqueda en el panel más inteligente.** Busque documentos de forma fiable por
  importes y números: encuentre facturas por encima de un valor o busque por
  **número de requisición**, con rangos de importes que comparan números reales, no
  texto. Los subtipos de factura se pueden buscar por sus nombres traducidos.
- **Notificaciones por correo electrónico fiables.** Las alertas de cambio de estado
  ahora se envían para todos los estados (no más correos descartados de forma
  silenciosa), y los acuses de recibo de importación entrante y los avisos de fallo
  ahora llevan la marca de DocBits correctamente, con controles por destinatario.
- **Inicio de sesión más fluido entre regiones (EU/US).** El cambio de región ahora
  es un pequeño banner en lugar de una interrupción a pantalla completa, el inicio de
  sesión único (SSO) lleva a la región correcta y mantener la sesión iniciada en
  varias pestañas del navegador es más fiable.
- **Correcciones de permisos.** Los usuarios obtienen el acceso que les otorga su
  grupo: abrir, editar, aprobar y reiniciar documentos ahora funciona correctamente
  incluso cuando los grupos y los permisos se configuran de formas menos habituales.
- **Procesamiento de documentos más estable.** Los documentos que antes se quedaban
  bloqueados tras la carga se vuelven a procesar automáticamente, y una ráfaga de un
  cliente ya no ralentiza a los demás.

---

## Web App — activa: `10.32.4`

- **Salto de búsqueda rápida (Cmd/Ctrl + K)** directo a la configuración de
  **Validación de e-Factura**.
- **Región e inicio de sesión:** el cambio de región se muestra como un banner
  persistente en lugar de una pantalla bloqueante; el inicio de sesión único ahora
  redirige a la región correcta (EU/US); mantener la sesión iniciada en varias
  pestañas es más fiable.
- **Permisos:** se corrigieron casos en los que los usuarios no podían **aprobar**,
  **editar**, **abrir** o **reiniciar** documentos a pesar de tener los permisos de
  grupo adecuados.
- **Configuración de correo entrante:** nuevas opciones “Notificar al remitente” y
  “Responder al remitente al recibir”.
- **Usabilidad:** la advertencia de documento duplicado ahora debe descartarse antes
  de continuar; el banner de “backend no disponible” solo aparece durante
  interrupciones reales; los contadores de tareas se actualizan de inmediato cuando
  se completan las tareas; corrección del modo oscuro en la pantalla de validación de
  tablas con IA.
- **Rendimiento:** se corrigió un bloqueo en la pantalla de documentos electrónicos
  durante la validación de campos y la conciliación de pedidos (PO matching).
- **Búsqueda de subtipos de factura por sus nombres traducidos.**

## API Service — activa: `12.41.9`

- **Renovación de la búsqueda en el panel:** el número de requisición y el
  solicitante ahora se pueden buscar; las búsquedas por importe y por número
  devuelven resultados correctos (comparación numérica real); el importe neto total y
  las columnas calculadas se muestran correctamente.
- **Correos de alerta de estado fiables** para cualquier estado de documento, sin que
  los fallos de envío queden ocultos.
- **Permisos:** los usuarios sin grupo pueden abrir y aprobar sus propios documentos;
  se restauró la visibilidad de documentos para los usuarios sin grupo.
- **Fiabilidad del procesamiento de documentos:** los documentos atascados en “nuevo”
  se vuelven a poner en cola automáticamente; procesamiento equitativo para que una
  gran ráfaga de una organización no deje sin recursos a las demás; autorreparación
  de problemas poco frecuentes en secuencias de base de datos.
- **Los PDF escaneados con una capa de texto defectuosa se enrutan a OCR** en lugar
  de producir texto poco fiable.
- **Precisión de extracción y de pedidos (PO):** el nombre del proveedor se rellena a
  partir del pedido de compra vinculado; se eliminan columnas duplicadas de número de
  artículo; mejor tratamiento de espacios especiales (de no separación).
- **Exportación a Infor ERP / SAP:** se corrigió la autenticación de la exportación
  por SFTP.
- **Facturación electrónica:** mejoras en la ruta de extracción de ZUGFeRD /
  documentos electrónicos.

## Auth Service — activa: `1.66.0`

- **Se corrigió la asignación de organización ausente** para algunos usuarios (id de
  organización vacío).

## Docflow Service — activa: `2.3.4`

- **El tiempo de espera (cooldown) del disparador de flujo de trabajo** ahora es
  configurable por entorno.

## Email Service — activa: `1.35.9`

- **Correos con marca:** los acuses de recibo de importación entrante y los avisos de
  fallo ahora usan el logotipo y los colores reales de DocBits.
- **Controles por organización:** correo de confirmación al recibir, “notificar al
  remitente” en caso de fallo y opciones de responder al remitente.
- **Importación entrante más fiable:** los resultados de la importación se registran
  correctamente, los fallos parciales se reportan como fallos (no como éxitos
  silenciosos) y los caracteres problemáticos en el cuerpo de los correos ya no
  rompen la importación.
- **Enrutamiento EU/US:** enrutamiento por organización a la API regional correcta.

## Fulltext Service — activa: `1.34.5`

- **La búsqueda por importes y números** ahora funciona de forma fiable, incluidos
  los separadores de miles y los rangos de importes (el motor detrás de la renovación
  de la búsqueda en el panel).
- **Infraestructura de búsqueda más estable:** se limpian las colas en segundo plano
  huérfanas para que ya no retengan recursos compartidos.

## PO Match Service — activa: `1.54.7`

- **Conciliación de pedidos de compra más robusta:** los códigos de embalaje/unidad
  de empaque basados en texto ya no bloquean una coincidencia, y la conciliación
  manual de líneas gestiona los resultados vacíos de forma segura.

---

## Sin cambios visibles para el cliente en este período

Estables, sin cambios destacables de producto entre el 21 y el 25 de junio: Auto
Accounting (`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`),
FTP (`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
