# Nodos

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
