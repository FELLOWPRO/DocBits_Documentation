# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

La tarjeta **"Run Workflow"** permite a los usuarios ejecutar dinámicamente un flujo de trabajo seleccionado de una lista de flujos de trabajo disponibles. Esta tarjeta es útil para automatizar procesos en los que varios flujos de trabajo están interconectados, posibilitando operaciones más ágiles.

## Componentes de la tarjeta:

1. **Workflow**
   * **Descripción:** Especifica el flujo de trabajo que se ejecutará cuando las condiciones se evalúen como verdaderas.
   * **Detalle:** Se proporciona una lista desplegable de todos los flujos de trabajo disponibles para su selección.

## Funcionalidad:

* **Evaluación de la condición:** La tarjeta ejecuta el flujo de trabajo seleccionado solo si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
  * Si cualquiera de las condiciones es falsa, no se realiza ninguna acción y el flujo de trabajo permanece sin disparar.
* **Ejecución del flujo de trabajo:**
  * Cuando se cumplen las condiciones, el flujo de trabajo especificado se dispara automáticamente.
  * Si no se cumplen las condiciones, no se ejecuta ningún flujo de trabajo.

## Configuración:

1. **Seleccionar el Workflow:** Elija el flujo de trabajo que se disparará de la **lista desplegable** de flujos de trabajo disponibles.
2. **Definir las condiciones:** Configure las secciones **"Where"** y **"And"** para especificar los criterios que deben cumplirse para que se ejecute el flujo de trabajo.

## Conclusión:

La tarjeta **"Run Workflow"** ofrece una forma cómoda y eficiente de vincular flujos de trabajo, automatizando procesos de varios pasos con facilidad. Al garantizar que se cumplan las condiciones de las secciones **"Where"** y **"And"**, los usuarios pueden ejecutar flujos de trabajo de forma dinámica y reducir la intervención manual.
