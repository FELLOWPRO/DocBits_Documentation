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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4" %}

**Vídeo:** Cambiar la versión de una tarjeta · 0:34 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**La etiqueta indica la versión de la tarjeta** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4#t=0.25)

Las tarjetas pueden tener varias versiones. La pequeña etiqueta de una tarjeta, por ejemplo v1, indica qué versión usa. Una versión más nueva puede hacer más.

**Clic para ver las versiones** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4#t=10.383)

Haga clic en la etiqueta para ver las versiones de la tarjeta.

**Versión 3: Estado después de la exportación** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4#t=14.75)

Elija la versión más nueva: también fija el estado del documento después de la exportación.

**Fijar de nuevo los valores** · [0:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4#t=20.816)

Los valores no se conservan. Vuelva a fijarlos, aquí la configuración de exportación y el estado.

**Validar y probar** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/es.mp4#t=27.983)

Luego valide y pruebe el Workflow, como tras cualquier cambio. Guárdelo cuando haga lo que espera.

</details>

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4" %}

**Vídeo:** Éxito, condición fallida y error en una ejecución · 1:13 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.vtt)

<details>

<summary>Transcripción</summary>

**Cuando, Y, Entonces al ejecutarse** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=0.25)

Cuando un flujo se ejecuta, la tarjeta Cuando lo inicia. Las tarjetas Y comprueban condiciones y las tarjetas Entonces actúan. Lo que pasa después depende del resultado de cada tarjeta.

**Éxito, condición fallida o error** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=11.416)

Cada tarjeta Y termina con uno de tres resultados. El éxito sigue el camino azul, una condición fallida el camino naranja y un error el camino rojo.

**Los datos que faltan son un error** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=21.783)

Los datos que faltan no son una condición fallida. Si falta un campo que la tarjeta necesita, una variable o el documento, la tarjeta informa de un error y toma el camino rojo.

**Sin camino naranja: se detiene** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=32.616)

Si una condición falla y su camino naranja no está conectado, el flujo se detiene en esa tarjeta. La ejecución termina como condición fallida.

**Conectado: solo otra rama** · [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=41.15)

Si el camino naranja está conectado, una condición fallida es solo otra rama. El flujo sigue por ahí y aún puede terminar con éxito.

**Camino rojo: capturar errores** · [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=49.283)

Conecte el camino rojo a una alternativa, por ejemplo una tarea para una persona, para que los errores no pasen desapercibidos. La alternativa se ejecuta, pero la ejecución sigue marcada como error.

**Cómo termina una ejecución** · [1:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v2/es.mp4#t=60.916)

En resumen: cualquier error convierte la ejecución en error. Una condición fallida sin camino naranja conectado la convierte en condición fallida. Todo lo demás termina con éxito.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4" %}

**Vídeo:** Y y O: combinar condiciones · 4:09 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.vtt)

<details>

<summary>Transcripción</summary>

**Y y O** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=0.25)

Las condiciones se combinan de dos formas. Tarjetas una tras otra funcionan como Y: todas deben ser verdaderas. Tarjetas en paralelo, conectadas a la misma tarjeta siguiente, funcionan como O: basta una tarjeta verdadera. Los nodos de unión lo muestran en el lienzo.

**Y: tarjetas una tras otra** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=16.45)

Una tarjeta tras otra es Y: cada tarjeta del camino debe ser verdadera antes de que se ejecute la siguiente. Esta factura está lista para validación y no pendiente de aprobación, así que ambas tarjetas son verdaderas y la acción se ejecuta.

**O: tarjetas en paralelo** · [0:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=32.716)

O significa tarjetas en paralelo. Conecte la salida verde de ambas tarjetas Y directamente a la entrada de la tarjeta siguiente. Pruébelo: la primera tarjeta es falsa, la segunda verdadera, y basta un camino verdadero para que se ejecute la acción. El banner de la prueba sigue indicando una condición no cumplida, porque la salida naranja de la tarjeta falsa no está conectada, pero la acción se ejecuta.

**Lo mismo con una tarjeta O** · [0:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=54.683)

También puede unir los caminos con una tarjeta O. Hace lo mismo, pero deja el O visible en el lienzo. Clic derecho en el lienzo, Agregar y luego O. Conecte ambas tarjetas Y a ella, y la tarjeta O a la acción.

**A O le basta un caso verdadero** · [1:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=71.516)

La prueba da el mismo resultado: a la tarjeta O le basta un caso verdadero, así que la acción se ejecuta. También aquí el banner indica la condición no cumplida de la tarjeta falsa.

**Esperar a CUALQUIERA: lo mismo que O** · [1:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=85.483)

Esperar a CUALQUIERA funciona exactamente como O: espera a cada tarjeta que tiene delante y continúa cuando se ha tomado al menos un camino. Las dos son intercambiables, use el nombre que se lea mejor en su workflow.

**Y con Esperar a TODOS** · [1:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=107.183)

Para un Y con tarjetas en paralelo, use Esperar a TODOS. Clic derecho en el lienzo, Agregar y luego Esperar a TODOS. Conecte ambas tarjetas Y a ella, y Esperar a TODOS a la acción. Pruébelo: espera a las dos tarjetas, ambas son verdaderas, así que la acción se ejecuta.

**El orden: como se dibujaron las conexiones** · [2:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=134.316)

¿En qué orden se ejecuta esto? El workflow recorre una lista. Las tarjetas detrás de una tarjeta se añaden en el orden en que se dibujaron sus conexiones, así que primero se ejecuta la condición de arriba y luego la de abajo. La tarjeta O espera hasta que ambas se hayan ejecutado, y la acción se ejecuta una vez, sin importar cuántas condiciones fueran verdaderas.

**Directo a una acción: sin espera** · [2:44](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=164.416)

Las tarjetas conectadas directamente a una acción no esperan. La acción se alcanza por el camino corto y se ejecuta antes de que se compruebe la última tarjeta del camino largo, así que esa tarjeta ya no cambia nada. Si la acción debe esperar a todas las comprobaciones, ponga delante una tarjeta O, Esperar a CUALQUIERA o Esperar a TODOS.

**Cada salida puede llevar a otro sitio** · [3:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=185.583)

Cada tarjeta tiene hasta tres salidas: éxito, condición no cumplida y error. Cada salida puede llevar a su propia tarjeta siguiente.

**Varias salidas a una entrada: basta una** · [3:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=197.05)

También puede conectar varias salidas de una tarjeta a la misma entrada. Solo se puede tomar una, porque una tarjeta termina con exactamente un resultado, así que la tarjeta siguiente espera solo esa. Esto vale para cualquier entrada, no solo para estos nodos de unión. Pruébelo: la condición no se cumple y Esperar a TODOS continúa igualmente.

**Nodos de unión: qué caminos se tomaron** · [3:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/es.mp4#t=223.016)

Los nodos de unión sirven sobre todo para que un Workflow se lea mejor. O y Esperar a CUALQUIERA continúan en cuanto se tomó al menos un camino conectado. Esperar a TODOS espera a que terminen todas las tarjetas anteriores y solo continúa si se tomaron todos los caminos conectados. Se puede conectar cualquier salida de una tarjeta, no solo la verde: si una tarjeta termina con una condición no cumplida, su salida naranja cuenta como tomada.

</details>

Los nodos se conectan mediante **aristas de colores**. Arrastra desde un conector en el lado **derecho** de un nodo hasta el conector de entrada en el lado **izquierdo** de otro nodo para crear una conexión. Cada color indica un resultado de ejecución diferente:

- **Success** (azul) — la ruta predeterminada que se toma cuando un nodo se completa correctamente. Disponible en todos los tipos de nodo.
- **Failed Condition** (naranja) — se toma cuando una condición se evalúa como falsa. Disponible en los nodos **And** (condición).
- **Error** (rojo) — se toma cuando un nodo encuentra un error durante la ejecución. Disponible en los nodos **And** y **Then** (acción).

## Resaltado de la ruta de ejecución

Haz clic en cualquier nodo para ver su ruta de ejecución. Todos los nodos que conducen a él y todos los nodos que parten de él se resaltan — todo lo demás se atenúa. En los nodos **Wait ALL**, se muestra cada rama entrante para que puedas ver exactamente qué espera la compuerta antes de continuar.

## Próximos pasos

- Pasa datos entre nodos con [Variables](variables.md).
- Comprueba y ejecuta tu flujo con [Validación y pruebas](validation-and-testing.md).
