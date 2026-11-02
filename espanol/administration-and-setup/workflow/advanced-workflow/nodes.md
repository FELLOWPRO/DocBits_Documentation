# Nodos

## Vídeo: Nodos y rutas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/es.mp4" %}

[Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/es.vtt) · 2:00

<details>
<summary>Transcripción</summary>

**La función de cada nodo**

Start inicia manualmente. When define un evento. Ninguno admite conexiones entrantes. And comprueba una condición. Then ejecuta una acción. Ambos constructores comparten el catálogo de tarjetas. Las notas explican el diseño sin ejecutarse.

**Tres resultados diferentes**

Arrastre una salida a la siguiente entrada. En el diseñador, azul indica éxito, naranja condición falsa y rojo error. And ofrece tres resultados; Then, éxito y error. La vista de ejecución representa el éxito en verde.

**Construya una alternativa**

Compruebe si una factura supera el umbral. Conecte azul con aprobación, naranja con procesamiento normal y rojo con gestión de errores. Una condición falsa puede continuar por su ruta conectada; no detiene todas las ramas.

**Unir con Wait ALL**

Wait ALL une ramas. Cada nodo de origen debe haber seguido una ruta conectada a la unión. Conecte ambas comprobaciones requeridas y la siguiente acción. Una ruta no seleccionada no aporta el resultado necesario.

**Alternativas con ANY y OR**

Wait ANY y OR unen ramas si al menos un origen siguió una ruta conectada. OR requiere dos nodos de origen distintos. Estas uniones no crean opciones exclusivas ni cancelan otras acciones. Pruebe el grafo completo.

**Mantenga el grafo ejecutable**

Los nodos de procesamiento deben ser accesibles desde una entrada. Evite ciclos y conexiones entrantes a Start o When. Incluya una acción Then y valide las rutas. Los nodos Delay importados requieren una duración positiva; Añadir no ofrece Delay.

</details>

[Ver los cinco capítulos](../advanced-workflow-videos.md)

Un Advanced Workflow es un grafo de **nodos** conectados por aristas. Añades nodos desde el menú **+ Add** (o haciendo clic derecho en el lienzo) y los conectas para definir el flujo de ejecución.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menú para añadir nodos con los tipos de nodo disponibles"><figcaption><p>El menú de nodos <strong>+ Add</strong> — los tipos de nodo disponibles.</p></figcaption></figure>

## Tipos de nodo

- **Start** — el punto de entrada del flujo de trabajo. Se añade automáticamente; cada flujo comienza aquí.
- **When** — una tarjeta de activación, la misma que en el constructor Standard.
- **And** — una tarjeta de condición. Se evalúa como verdadero o falso y puede ramificar el flujo.
- **Then** — una tarjeta de acción que realiza trabajo (establecer campos, crear tareas, llamar a APIs, …).
- **Wait ALL** — espera hasta que *todas* las ramas entrantes se completen antes de continuar.
- **Wait ANY** — continúa en cuanto *cualquier* rama entrante se complete.
- **OR** — ramifica el flujo por rutas alternativas.
- **Note** — una anotación de texto libre en el lienzo; no afecta a la ejecución.

Los nodos **When / And / Then** usan exactamente las mismas tarjetas descritas en la sección [Tarjetas](../cards-overview.md).

## Conectar nodos

Los nodos se conectan mediante **aristas de colores**. Arrastra desde un conector en el lado **derecho** de un nodo hasta el conector de entrada en el lado **izquierdo** de otro nodo para crear una conexión. Cada color indica un resultado de ejecución diferente:

- **Success** (azul) — la ruta predeterminada que se toma cuando un nodo se completa correctamente. Disponible en todos los tipos de nodo.
- **Failed Condition** (naranja) — se toma cuando una condición se evalúa como falsa. Disponible en los nodos **And** (condición).
- **Error** (rojo) — se toma cuando un nodo encuentra un error durante la ejecución. Disponible en los nodos **And** y **Then** (acción).

## Resaltado de la ruta de ejecución

Haz clic en cualquier nodo para ver su ruta de ejecución. Todos los nodos que conducen a él y todos los nodos que parten de él se resaltan — todo lo demás se atenúa. En los nodos **Wait ALL**, se muestra cada rama entrante para que puedas ver exactamente qué espera la compuerta antes de continuar.

## Próximos pasos

- Pasa datos entre nodos con [Variables](variables.md).
- Comprueba y ejecuta tu flujo con [Validación y pruebas](validation-and-testing.md).
