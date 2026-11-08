# Infraestructura

La página **Infrastructure** ofrece a los administradores una visión actual de dónde se ejecuta cada parte de la plataforma (EU o US) y de si el procesamiento está en buen estado. Es de solo lectura, por lo que aquí no se configura nada.

> **Access:** Infrastructure es una página solo para administradores. Abra **Settings → Organization & Access → Infrastructure**.

La página tiene tres pestañas. Cada una carga sus datos la primera vez que se abre, así que cambiar de una a otra no lo vuelve a solicitar todo.

| Tab | Answers |
|-----|---------|
| **Topology** | ¿Dónde se ejecuta cada componente y cómo recorre un documento DocBits? |
| **Processing** | ¿Se ejecutan los pasos del procesamiento de documentos y se acumula trabajo? |
| **Scheduled Tasks** | ¿Se ejecutan a tiempo las tareas en segundo plano recurrentes? |

## Topology

**Topology** se abre de forma predeterminada. Muestra la plataforma en dos vistas: **Architecture** y **Process**. Con el conmutador situado encima del diagrama cambia entre ellas; el indicador que lo acompaña muestra **live** mientras la vista transmite su estado.

Un aviso encima del diagrama resume la comprobación de regiones:

* **Green**: todos los componentes se ejecutan en la región de su organización y el aviso indica esa región (por ejemplo **EU**).
* **Red**: un componente marcado como crítico se ejecuta fuera de la región de su organización.
* **Amber**: el aviso indica componentes que están en otra región aunque la comprobación general se supere. Es una diferencia de región, no un fallo.

### Vista de arquitectura

La vista de arquitectura dibuja la plataforma como carriles de tarjetas de componentes, por ejemplo Edge / Web, Core API, Import, Background Services y Modules. Las flechas muestran las conexiones entre las tarjetas.

Cada tarjeta muestra el nombre del componente, una insignia de región y, en los componentes críticos, un punto de estado que se vuelve verde cuando el componente responde y muestra su latencia en milisegundos cuando se informa de un valor.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | El componente se ejecuta en la región de su organización. |
| **SHARED** | Un componente global, como la CDN, que no tiene una región única. Es lo esperado. |
| **EU ⓘ** / **US ⓘ** | El componente se ejecuta en otra región y se informa como aviso. |
| **EU ⚠** / **US ⚠** | El componente se ejecuta en otra región y se informa como error. Consúltelo con el soporte. |
| Insignia gris, sin marca | No se conoce la región de este componente. |

### Vista de proceso

La vista de proceso anima un único documento por la canalización: las fuentes de entrada **Email**, **FTP** y **Web** convergen en **API** y después pasan por **OCR**, **Extraction**, **PO matching**, **Auto Accounting** y **Export**. Cada etapa se conecta con una barra de almacenes de datos con **Postgres** y almacenamiento de archivos. Un pie de ilustración indica el paso que se está animando y el botón de reproducción pausa o reanuda la animación.

PO matching y Auto Accounting son opcionales. Cuando uno de ellos está desactivado para su organización, su etapa aparece en gris y la animación lo omite.

### Módulos opcionales

Los módulos opcionales (Full-Text Search, DocFlow, Auto-Accounting, DocNet y PO Matching) llevan una insignia **active** o **inactive** en su tarjeta. Un módulo desactivado ofrece un botón **Activate** que le lleva a la página donde se activa: los ajustes de Modules para la mayoría de los módulos, o **Document Types** para PO Matching, que se activa por tipo de documento.

## Processing

La pestaña **Processing** enumera los pasos del procesamiento de documentos de su organización e indica si el trabajo fluye o se acumula.

| Column | Description |
|--------|-------------|
| **Process** | El paso de procesamiento: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction y PO Match. |
| **Last run** | Cuánto tiempo hace que se ejecutó el paso por última vez. Pase el cursor por encima para ver la marca de tiempo exacta. **Never run** significa que ningún documento ha llegado todavía a este paso. |
| **Status** | Una o varias insignias (véase más abajo). |

Las insignias de estado son señales independientes:

* Insignia roja **Errors (N)**: `N` documentos han fallado recientemente en este paso.
* Insignia ámbar con un recuento: `N` documentos se están procesando en este paso ahora mismo.
* Insignia verde **OK**: no hay errores recientes ni nada en espera.

Como los errores y el trabajo en curso se cuentan por separado, un paso puede mostrar ambos a la vez, de modo que un fallo sigue visible mientras otros documentos se siguen procesando.

## Scheduled Tasks

La pestaña **Scheduled Tasks** enumera las tareas en segundo plano recurrentes que mantienen DocBits en funcionamiento, por ejemplo actualizaciones de caché, alertas de estado, tiempos de espera de documentos y sincronizaciones salientes. Cada fila indica si la tarea se ejecuta a su hora.

| Column | Description |
|--------|-------------|
| **Task** | El nombre de la tarea programada, con los separadores sustituidos por espacios. |
| **Last run** | Cuánto tiempo hace que se ejecutó por última vez. Pase el cursor por encima para ver la marca de tiempo exacta. **Never run** significa que aún no se ha ejecutado. |
| **Status** | Estado de la programación (véase más abajo). |

| Status | Meaning |
|--------|---------|
| **On schedule** (verde) | La tarea se ejecuta en el intervalo previsto. |
| **Delayed** (rojo) | La tarea no se ha ejecutado cuando se esperaba. Investíguelo o consúltelo con el soporte. |
| **Unknown** (gris) | No se ha podido determinar el estado de la programación. |

Ambas tablas tienen un botón **Refresh** que vuelve a cargar las cifras actuales a petición.
