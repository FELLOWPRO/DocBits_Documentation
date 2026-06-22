# Advanced Workflow

El constructor **Advanced Workflow** es un editor de grafos de nodos para flujos de trabajo que necesitan ramificaciones, rutas paralelas y control de flujo, más allá del modelo lineal When/And/Then del constructor Standard. Usted dispone los nodos en un lienzo y los conecta para definir el flujo de ejecución.

{% embed url="https://youtu.be/EeNFVR6z7G8" %}
Advanced Workflow Designer
{% endembed %}

## Cómo acceder

Abra el diseñador Advanced Workflow desde el área de flujos de trabajo (el lienzo del constructor avanzado). Comienza desde un nodo **Start** y construye el flujo añadiendo nodos.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Lienzo de grafo de nodos de Advanced Workflow con barra de herramientas"><figcaption><p>El lienzo de Advanced Workflow — un grafo de nodos con controles de zoom, ejecución, cuadrícula y guardado. Asigne un nombre al flujo de trabajo en la barra de herramientas.</p></figcaption></figure>

## Añadir nodos

Haga clic en **+ Add** para abrir el menú de nodos. Además de las conocidas tarjetas **When**, **And** y **Then**, el constructor avanzado añade nodos de control de flujo:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menú Add de Advanced Workflow con tipos de nodo"><figcaption><p>El menú de nodos <strong>+ Add</strong>: When / And / Then más Wait ALL, Wait ANY, OR y Note.</p></figcaption></figure>

- **When / And / Then** — las mismas tarjetas de condición y de acción que en el constructor Standard.
- **Wait ALL** — espera hasta que *todas* las ramas entrantes se completen antes de continuar.
- **Wait ANY** — continúa en cuanto *cualquiera* de las ramas entrantes se complete.
- **OR** — ramifica el flujo por rutas alternativas.
- **Note** — una anotación de texto libre en el lienzo (no afecta a la ejecución).

Ejecute el flujo con el control de reproducción, valídelo y guárdelo con el botón de guardar de la barra de herramientas.

## Próximos pasos

- Vea qué hace cada tarjeta en la sección **Cards**.
- Para automatizaciones lineales sencillas, el constructor **Standard Workflow** es más rápido de configurar.
