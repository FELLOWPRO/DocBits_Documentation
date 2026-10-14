# Infraestructura

La página **Infraestructura** ofrece a los administradores una vista en vivo de dónde se ejecuta cada parte de DocBits (UE o EE. UU.), cómo fluye un documento por el sistema y si el procesamiento en segundo plano está en buen estado. Es de solo lectura — aquí no se configura nada; responde a la pregunta: *«¿está todo funcionando y mis datos permanecen en mi región?»*

> **Acceso:** Infraestructura es una página exclusiva para administradores. Abra **Configuración → Organización y Acceso → Infraestructura**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Página de Infraestructura con la pestaña Topología abierta"><figcaption><p>La página de Infraestructura, pestaña Topología</p></figcaption></figure>

La página se divide en tres pestañas:

| Pestaña | Responde |
|---------|----------|
| **Topología** | ¿Dónde se ejecuta cada componente y está todo en mi región? |
| **Procesamiento** | ¿Se están ejecutando los pasos de procesamiento (OCR, extracción, conciliación de PO …) y están al día? |
| **Tareas programadas** | ¿Se ejecutan los trabajos recurrentes en segundo plano según lo previsto? |

## Topología

La pestaña Topología dibuja toda la plataforma DocBits como un diagrama, agrupado en capas — **Edge / Web**, **Core API**, **Importación**, **Servicios en segundo plano**, **Almacenes de datos** y **Autenticación**. Cada recuadro es un componente (la Web App/CDN, la pasarela de API, el worker de OCR, la base de datos, etc.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Diagrama de topología con distintivos de región"><figcaption><p>Cada componente está etiquetado con la región en la que se ejecuta</p></figcaption></figure>

### Transparencia de región

Cada componente lleva un distintivo de región para que pueda confirmar la residencia de sus datos de un vistazo:

| Distintivo | Significado |
|------------|-------------|
| **UE ✓** / **US ✓** | El componente se ejecuta en la región de su organización. |
| **SHARED** | Un componente global (p. ej. la CDN) sin una región única — esto es lo esperado y no supone ningún problema. |
| **Discrepancia de región** | El componente se ejecuta en una región *diferente* a la de su organización. Se resalta para que pueda plantearlo al soporte. |

El banner superior resume el resultado: **«Todos los componentes se ejecutan en su región (UE)»** cuando todo coincide, o una advertencia si algún componente crítico está en otra región.

### Arquitectura vs. Reproducir proceso

Use el conmutador situado sobre el diagrama para cambiar de vista:

- **Arquitectura** — el mapa estático de todos los componentes y cómo se conectan.
- **Reproducir proceso** — anima el recorrido de un documento por el sistema, paso a paso, para que vea el orden en que intervienen los componentes.

El indicador **● live** muestra que la información de estado del diagrama refleja el estado actual del sistema.

### Módulos opcionales

Los componentes que pertenecen a un módulo opcional (Búsqueda de texto completo, DocFlow, Auto-Accounting, DocNet, Conciliación de PO) muestran un distintivo **activado** o **desactivado**. Al hacer clic en un módulo desactivado, irá directamente a la página donde puede activarlo — **Configuración → Módulo** para la mayoría de los módulos, o **Tipos de documento** para la Conciliación de PO (que se activa por tipo de documento).

## Procesamiento

La pestaña Procesamiento muestra la canalización de procesamiento de documentos de **su organización** — cuándo se ejecutó cada paso por última vez y si el trabajo fluye o se acumula.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tabla de procesamiento con distintivos de estado"><figcaption><p>Estado de procesamiento por paso para su organización</p></figcaption></figure>

| Columna | Descripción |
|---------|-------------|
| **Proceso** | El paso de procesamiento — Procesamiento de documentos, OCR, TR-OCR, División de código de barras, Extracción de código de barras, Extracción, Conciliación de PO. |
| **Última ejecución** | Hace cuánto se ejecutó el paso por última vez. Pase el ratón por encima para ver la marca de tiempo exacta. *«Nunca ejecutado»* significa que aún ningún documento ha llegado a este paso. |
| **Estado** | Un distintivo tipo semáforo (véase abajo). |

Distintivos de estado:

| Distintivo | Significado |
|------------|-------------|
| **OK** (verde) | Sin errores recientes y nada en espera — el paso está sano. |
| **En curso (N)** (ámbar) | `N` documentos se están procesando actualmente en este paso. |
| **Error (N)** (rojo) | `N` documentos fallaron recientemente en este paso. |

Los errores y *en curso* son señales independientes, por lo que un paso puede mostrar ambos distintivos a la vez — así ve un fallo aunque otro trabajo siga en marcha. Use **Actualizar** (arriba a la derecha) para obtener las cifras más recientes.

## Tareas programadas

La pestaña Tareas programadas enumera los trabajos recurrentes en segundo plano que mantienen DocBits en funcionamiento (actualizaciones de caché, alertas de estado, tiempos de espera de documentos, sincronizaciones salientes y más) y confirma que cada uno se ejecuta puntualmente.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabla de tareas programadas"><figcaption><p>Trabajos recurrentes en segundo plano y su estado de planificación</p></figcaption></figure>

| Columna | Descripción |
|---------|-------------|
| **Tarea** | El nombre del trabajo programado. |
| **Última ejecución** | Hace cuánto se ejecutó por última vez. Pase el ratón por encima para ver la marca de tiempo exacta; *«Nunca ejecutado»* significa que aún no se ha disparado. |
| **Estado** | Estado de planificación (véase abajo). |

Valores de estado:

| Distintivo | Significado |
|------------|-------------|
| **En horario** (verde) | La tarea se ejecuta en su intervalo previsto. |
| **Retrasada** (rojo) | La tarea no se ha ejecutado cuando se esperaba — conviene investigar o plantearlo al soporte. |
| **Desconocido** (gris) | No se pudo determinar el estado de planificación. |

Use **Actualizar** para volver a comprobar el estado de planificación cuando lo necesite.
