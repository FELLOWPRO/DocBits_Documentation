# Notas de versión de DocBits — 3–4 de julio de 2026

_Lo que esta actualización de producción ofreció, explicado de forma sencilla. Cada
servicio muestra la versión que ahora está activa en producción. Los servicios que
no aparecen en la lista no tuvieron cambios visibles para el cliente en este período._

---

## Aspectos destacados

- **Cierres más limpios en todo el sistema.** Varios servicios principales (API,
  Auto Accounting, Docflow, Extraction, OCR, PO Match) ahora se apagan
  correctamente durante una versión, de modo que un despliegue continuo ya no
  corre el riesgo de cortar una solicitud que ya estaba en curso.
- **Mejoras en la exportación de facturas electrónicas.** Exportar un documento
  a varias configuraciones de exportación a la vez ahora es más fiable: las
  comprobaciones de exportación duplicada se ejecutan una vez por lote en lugar
  de una vez por elemento, y un nuevo endpoint de exportación evita que el
  estado de exportación parpadee cuando se activan varias exportaciones a la
  vez. Los documentos XRechnung/ZUGFeRD también obtienen una asignación de
  campos más consistente.
- **Procesamiento de documentos más estable.** Se corrigió un bloqueo que podía
  hacer caer todo un documento OCR cuando fallaba una sola página, se corrigió
  la sincronización de entregas de órdenes de compra, que solo obtenía los
  primeros 100 registros, y se reforzó la resiliencia de varios servicios ante
  breves interrupciones de la conexión a la base de datos.
- **Adjuntos de correo electrónico recuperados.** Se corrigió un caso en el que
  los adjuntos de correo electrónico podían llegar dañados o con bytes
  faltantes durante la importación entrante.
- **Fiabilidad de los flujos de trabajo.** Se corrigió que los flujos de trabajo
  se quedaran bloqueados por un bloqueo (lock) que no se liberaba
  correctamente, y se corrigió la lógica de reprogramación para que los pasos
  de flujo de trabajo omitidos se gestionen y registren correctamente.
- **Novedad: Ideas Service.** Un nuevo servicio de backend (Ideas, v0.3.0) se ha
  incorporado a la flota de producción.

---

## API Service — activa: `12.52.4`

- **Fiabilidad de OCR:** un bloqueo en una sola página ya no hace fallar todo
  el documento.
- **Exportación:** las comprobaciones de exportación duplicada ahora se
  ejecutan una vez por lote en lugar de una vez por elemento; un nuevo
  endpoint de exportación evita que el estado de exportación parpadee cuando
  se ejecutan varias exportaciones al mismo tiempo; los documentos
  XRechnung/ZUGFeRD obtienen una asignación de campos canónicos más
  consistente.
- **Órdenes de compra:** se corrigió que la sincronización de entregas solo
  obtuviera los primeros 100 registros por pedido.
- **Registros de Actividad:** se corrigió que el botón de página "Siguiente"
  saltara a una ventana de tiempo no relacionada.
- **Búsqueda de datos maestros:** se corrigió un error de servidor (HTTP 500).
- **Indexación de búsqueda:** se añadió un marcador de entrega comprobada y
  reintentos para que los documentos se pongan en cola de forma fiable para la
  búsqueda de texto completo.
- Correcciones generales de estabilidad que resuelven varios errores de fondo
  recurrentes.

## Auth Service — activa: `1.68.7`

- Solo mantenimiento interno y de fiabilidad en este período.

## Auto Accounting — activa: `1.18.8`

- **Cierres más limpios** durante los despliegues, evitando solicitudes
  interrumpidas que estaban en curso.

## Barcode Service — activa: `1.15.8`

- Solo corrección interna de configuración de despliegue en este período.

## Docflow Service — activa: `2.5.3`

- **Nueva opción de exportación** para enviar un documento a varias
  configuraciones de exportación a la vez.
- **Se corrigió que los flujos de trabajo se quedaran bloqueados** por un
  bloqueo (lock) que no se liberaba correctamente, independientemente del
  estado.
- **Se corrigió la reprogramación de flujos de trabajo** para que los pasos
  omitidos se gestionen y registren correctamente en lugar de descartarse
  silenciosamente.
- **Arranque más rápido:** las bases de datos ahora se precalientan en segundo
  plano.
- Mayor resiliencia frente a breves interrupciones de la conexión a la base de
  datos.
- Mejora en el análisis de campos de fecha para las tarjetas de flujo de
  trabajo.

## Email Service — activa: `1.37.9`

- **Se corrigieron los adjuntos entrantes** que podían llegar dañados o con
  bytes faltantes.
- **Errores más claros** cuando no se puede obtener una carpeta del buzón, en
  lugar de un fallo genérico.

## Extraction Service — activa: `1.49.6`

- **Se corrigieron bloqueos** en documentos con un tipo de documento no
  reconocido y en tablas con una forma inusual o malformada.
- Mayor resiliencia frente a breves interrupciones de la conexión a la base de
  datos durante una consulta.

## FTP Service — activa: `1.30.3`

- Solo actualización interna del framework en este período.

## Fulltext Service — activa: `1.36.3`

- **Indexación de búsqueda:** un barrido periódico ahora repara cualquier
  documento que no haya llegado al índice de búsqueda de cualquier
  organización.
- **Sincronización con ERP:** se corrigió un bloqueo (lock) atascado que podía
  impedir la sincronización con ERP tras un reintento fallido.

## OCR Service — activa: `1.7.8`

- **Se corrigió la autenticación de OCR** para que las claves de API de
  organización vuelvan a funcionar correctamente.
- Cierres más limpios durante los despliegues.

## Operator Service — activa: `1.39.7`

- Solo correcciones internas de fiabilidad de despliegue en este período.

## PO Match Service — activa: `1.56.0`

- **Se corrigió un bloqueo** al ordenar cantidades de PO Match que incluían
  valores vacíos.
- Cierres más limpios durante los despliegues.

## Web App — activa: `10.36.9`

- **Se corrigió un error** al volver a la Validación de Campos desde otra
  pantalla.
- **Se corrigió el botón "Scripts"**, que dirigía a una página 404.
- **Registros de Actividad:** se corrigió una visualización incorrecta de
  "Página 2 de 1" y se corrigió que el filtro de severidad WARN no coincidiera
  con nada.

---

## Sin cambios visibles para el cliente en este período

Auth Service, Barcode Service, FTP Service, Operator Service y Docnet Service
(`1.54.6`, sin cambios) recibieron solo mantenimiento interno o de
configuración de despliegue.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
