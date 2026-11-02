# Configuración de Búsqueda de Texto Completo

<figure><img src="../../../.gitbook/assets/fulltext-search-settings-module-required-es-20261011.png" alt="Configuración de Búsqueda de Texto Completo en la sandbox, con un diálogo que explica que se requiere el módulo y los botones Ir a Módulos y Habilitar ahora"><figcaption><p>Cuando la Búsqueda de Texto Completo está desactivada, este diálogo explica los siguientes pasos.</p></figcaption></figure>

La Configuración de Búsqueda de Texto Completo define qué indexa DocBits y cómo hace ese contenido buscable en documentos, datos maestros del ERP y plantillas. La página de configuración muestra un diálogo de requisito hasta que el **módulo de Búsqueda de Texto Completo** está activado — consulte [Búsqueda de Texto Completo](../document-processing/module/fulltext-search.md) para el lenguaje de consulta del usuario final.

## Requisitos previos

El módulo de Búsqueda de Texto Completo debe activarse en **Ajustes → Módulo → Dashboards & Analytics → Full text search**. Si el módulo no está activado, el diálogo ofrece tres acciones:

* **Ayuda (?)** — Abre la documentación de la Búsqueda de Texto Completo en una pestaña nueva antes de cambiar cualquier configuración.
* **Ir a Módulos** — Abre la configuración de módulos de Dashboards & Analytics para revisar la configuración.
* **Habilitar ahora** — Abre el diálogo de suscripción. Revise y confirme ese diálogo antes de que el módulo se active; hacer clic solo en este botón no lo activa.

La página de configuración estará disponible una vez que el módulo esté activo.

## Disposición de la página

La página de configuración está organizada en tres pestañas, cada una abarca un tipo de contenido distinto que la Búsqueda de Texto Completo puede indexar.

### Pestaña Documentos

La pestaña Documentos cubre todo lo relacionado con la indexación de documentos procesados:

* **Estadísticas de indexación** — totales de documentos indexados y pendientes, actualizables a petición.
* **Preferencias de vectores** — tres conmutadores a nivel de organización que controlan si la indexación vectorial se ejecuta junto con el índice de texto para documentos. La indexación vectorial alimenta el modo de consulta `vector:` y la función "Buscar similares".
* **Acciones de reindexación** — inicie una reindexación completa o incremental. Mientras se ejecuta una reindexación, verá el progreso en vivo (documentos por minuto, tiempo estimado), el estado actual del flujo y el último error (si lo hay).
* **Diagnóstico de sincronización** — diagnóstico a petición para los casos en que el índice parece estar desincronizado con el almacén de documentos subyacente.

<mark>La reindexación no es destructiva — la búsqueda existente sigue funcionando mientras se reconstruye el nuevo índice.</mark>

### Pestaña ERP

La pestaña ERP controla la indexación de los datos maestros del ERP — proveedores, clientes, artículos y entidades similares. Cada entidad tiene sus propios conmutadores:

* **Indexación** — indexa textualmente la entidad para que sea buscable desde el panel.
* **Vector** — indexa vectorialmente la entidad para que pueda encontrarse mediante consultas semánticas.

Use la acción **Conmutar todo** al principio de la lista para aplicar el mismo estado de activado/desactivado a todas las entidades a la vez. La indexación se inicia en segundo plano; un indicador en cada fila muestra cuándo está en curso.

### Pestaña Plantillas

La pestaña Plantillas enumera las versiones de plantilla conocidas por el índice de Texto Completo. Use esta vista para confirmar, tras un nuevo despliegue, que las versiones de plantilla de las que depende están presentes en el índice.

## Qué se indexa

Una vez activada y configurada, la Búsqueda de Texto Completo permite a los usuarios:

* Buscar en todo el contenido de los documentos (no solo en los campos de metadatos).
* Encontrar documentos por el texto contenido en los archivos cargados.
* Usar operadores de búsqueda avanzados para consultas precisas.
* Acceder a los resultados de búsqueda directamente desde el panel.
* Usar búsqueda semántica (prefijo `vector:`) cuando la indexación vectorial esté activada para ese tipo de contenido.

Consulte la página del módulo [Búsqueda de Texto Completo](../document-processing/module/fulltext-search.md) para la referencia completa del lenguaje de consulta, incluidas consultas de rango, filtros inteligentes y el modo de búsqueda con IA.
