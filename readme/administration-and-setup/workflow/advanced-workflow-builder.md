# Advanced Workflow

El constructor **Advanced Workflow** es un editor de grafos de nodos para flujos de trabajo que necesitan ramificaciones, rutas paralelas y control de flujo, más allá del modelo lineal When/And/Then del constructor Standard. Usted dispone los nodos en un lienzo y los conecta para definir el flujo de ejecución.

## Vídeo: rutas de facturas en DocBits

El vídeo muestra un flujo configurado en la interfaz real de DocBits: comprobación del importe, dos acciones, conexiones y preparación de los casos de prueba.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.mp4" %}

[Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/es.vtt)

Las imágenes muestran un borrador de demostración sin guardar. `total_amount` y `approval_route` son claves de campo de ejemplo. `Approval` y `Standard` identifican las rutas. Configure las acciones de negocio que necesita su proceso.

<details>
<summary>Transcripción</summary>

**Una factura con dos rutas**

Este es un flujo avanzado real en DocBits. Una comprobación del importe de la factura conduce a dos acciones. Las conexiones determinan qué acción se ejecuta. El ejemplo utiliza un borrador sin guardar y campos de demostración.

**Configurar la comprobación**

Abra Añadir, elija And y seleccione una condición de campo del documento. Indique el campo del importe, elija Mayor que e introduzca mil. Utilice la clave exacta del campo en la configuración del documento.

**Configurar las acciones**

Añada dos tarjetas Then. Ambas establecen el campo de demostración approval route. Una escribe Approval y la otra Standard. Estos valores identifican la ruta. Configure las acciones de su proceso para un flujo de producción.

**Conectar las salidas**

Conecte Start con la entrada de la condición. Conecte la salida azul de éxito con Approval y la salida naranja de condición falsa con Standard. La salida roja trata los errores de evaluación por separado. La posición de una tarjeta no crea una ruta.

**Preparar los casos de prueba**

Abra Probar en la barra de herramientas. Seleccione un documento de prueba o introduzca sus datos completos en JSON. Compruebe importes superiores, inferiores e iguales a mil, además de valores ausentes. Revise los resultados de los nodos después de ejecutar.

**Validar, guardar y activar**

Valide las conexiones y la configuración de las tarjetas. Guarde explícitamente en el servidor y compruebe la activación por separado. Los borradores automáticos del navegador no sustituyen a Guardar. La ejecución y los registros requieren el módulo y la suscripción adecuados.

</details>

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

[Ver los cinco capítulos](advanced-workflow-videos.md)
