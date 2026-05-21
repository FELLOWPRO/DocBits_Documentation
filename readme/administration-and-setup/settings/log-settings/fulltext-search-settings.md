# Configuración de Búsqueda de Texto Completo

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Configuración de Búsqueda de Texto Completo"><figcaption><p>Configuración de Búsqueda de Texto Completo — Diálogo "Módulo Requerido"</p></figcaption></figure>

La Configuración de Búsqueda de Texto Completo controla qué indexa DocBits y cómo ese contenido se puede buscar en documentos, datos maestros del ERP y plantillas. La página de configuración solo se abre cuando el **módulo de Búsqueda de Texto Completo** está activado — consulte [Búsqueda de Texto Completo](../document-processing/module/fulltext-search.md) para el lenguaje de consulta del usuario final.

## Requisitos previos

El módulo de Búsqueda de Texto Completo debe activarse en **Configuración → Procesamiento de Documentos → Módulo → Paneles → Búsqueda de texto completo**. Si el módulo no está activado, un diálogo le pide que:

* **Ir a Módulos** — Navegue a la página de configuración de Módulos para revisar la configuración.
* **Activar ahora** — Active el módulo de Búsqueda de Texto Completo directamente (inicia una suscripción a DocSearch).

La página de configuración estará disponible una vez que el módulo esté activo.

## Disposición de la página

La página de configuración está organizada en tres pestañas, cada una abarcando un tipo de contenido distinto que la Búsqueda de Texto Completo puede indexar.

### Pestaña Documentos

La pestaña Documentos cubre todo lo relacionado con la indexación de documentos procesados:

* **Estadísticas de indexación** — totales de documentos indexados y pendientes, actualizables a petición.
* **Preferencias de vectores** — tres conmutadores de organización que controlan si la indexación vectorial se ejecuta junto con la indexación textual para documentos. La indexación vectorial impulsa el modo de consulta `vector:` y la función "Buscar similares".
* **Acciones de reindexación** — inicie una reindexación completa o incremental. Mientras se ejecuta una reindexación, ve el progreso en vivo (documentos por minuto, tiempo estimado), el estado actual del flujo y el último fallo (si lo hay).
* **Diagnóstico de sincronización** — diagnóstico bajo demanda para casos en los que el índice parece estar desincronizado del almacén de documentos subyacente.

<mark>La reindexación no es destructiva — la búsqueda existente sigue funcionando mientras se reconstruye el nuevo índice.</mark>

### Pestaña ERP

La pestaña ERP controla la indexación de los datos maestros del ERP — proveedores, clientes, artículos y entidades similares. Cada entidad tiene su propio conmutador:

* **Indexación** — indexa textualmente la entidad para que se pueda buscar desde el panel.
* **Vector** — indexa vectorialmente la entidad para que pueda emparejarse con consultas semánticas.

Use la acción **Conmutar todo** en la parte superior de la lista para aplicar el mismo estado a todas las entidades a la vez. La indexación se lanza en segundo plano; un indicador en cada fila muestra cuándo está en curso.

### Pestaña Plantillas

La pestaña Plantillas lista las versiones de plantilla conocidas por el índice de Texto Completo. Use esta vista para confirmar que las versiones de plantilla de las que depende están presentes en el índice tras un redepliegue.

## Qué se indexa

Una vez activada y configurada, la Búsqueda de Texto Completo permite a los usuarios:

* Buscar en todo el contenido del documento (no solo en los campos de metadatos).
* Encontrar documentos por texto contenido en los archivos cargados.
* Usar operadores de búsqueda avanzados para consultas precisas.
* Acceder a los resultados directamente desde el panel.
* Usar búsqueda semántica (prefijo `vector:`) cuando la indexación vectorial esté activada para ese tipo de contenido.

Consulte la página del módulo [Búsqueda de Texto Completo](../document-processing/module/fulltext-search.md) para la referencia completa del lenguaje de consulta, incluidas consultas de rango, filtros inteligentes y el modo de búsqueda con IA.
