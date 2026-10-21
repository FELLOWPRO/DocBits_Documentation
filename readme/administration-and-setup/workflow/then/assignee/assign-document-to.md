# Asignar documento a

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-0e17d9fb5a83-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

## Propósito:

La tarjeta de flujo de trabajo **"Asignar documento a \[Usuario/grupo] según la tabla de decisiones"** asigna dinámicamente documentos a usuarios o grupos según el resultado de una **tabla de decisión**. Esta función garantiza que la asignación de documentos se gestione de forma eficiente y coherente según condiciones predefinidas.

## Componentes de la tarjeta:

1. **Usuario/Grupo**
   * **Descripción:** Especifica el **usuario** o **grupo** al que se asignará el documento.
   * **Detalle:** Se selecciona según el resultado de la **tabla de decisión**.
2. **Tabla de decisiones**
   * **Descripción:** Se utiliza una **tabla de decisión** para determinar el **usuario** o **grupo** adecuado para la asignación del documento.
   * **Detalle:** Usa la tabla de decisión definida en la sección **"y"**.

## Funcionalidad:

* **Evaluación de la condición:** La tarjeta solo ejecuta su acción si las secciones **"Cuando"** y **"Y"** se evalúan como verdaderas.
* **Asignación dinámica del documento:** El documento se asigna al **usuario** o **grupo** determinado por la **tabla de decisión**.

## Configuración:

* **Definir la Decision Table:** Configure la **tabla de decisión** para incluir las condiciones para determinar el **usuario** o **grupo** de destino.
* **Asignar el documento al Usuario/Grupo:** El documento se asignará dinámicamente según el resultado de la tabla de decisión.

## Conclusión:

La tarjeta de flujo de trabajo **"Asignar documento a \[Usuario/grupo] según la tabla de decisiones"** proporciona capacidades de asignación dinámica de documentos basadas en lógica de decisión. Esto garantiza un procesamiento preciso y eficiente al dirigir automáticamente los documentos al **usuario** o **grupo** adecuado, mejorando la automatización del flujo de trabajo.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Elija un documento asignado de una tabla de decisiones.

**Configuración:** Seleccione una tabla de decisión de demostración cuya regla de coincidencia devuelva el revisor configurado y elija el tipo de asignado que ofrece esta versión de tarjeta.

**Resultado esperado y contraejemplo:** El usuario o grupo devuelto se convierte en el responsable del documento. Un resultado de tabla de decisiones vacía debe diagnosticarse por separado.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
