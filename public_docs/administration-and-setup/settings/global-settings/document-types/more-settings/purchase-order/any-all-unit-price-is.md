<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo se utiliza para comparar el precio unitario en un documento con el precio unitario en una orden de compra, asegurando que los precios se alineen dentro de los niveles de tolerancia definidos. La comparación puede activar acciones si el precio unitario no cumple con las expectativas. La **Versión 4** añade más flexibilidad permitiendo a los usuarios elegir diferentes entidades para la comparación, proporcionando un nivel más profundo de control sobre los procesos de precios y adquisiciones.

## **Componentes de la Tarjeta:**

1. **Cualquiera / Todos (Any / All):**
   * **Descripción**: Define si la condición se aplica a cualquiera o a todas las instancias donde se compara el precio unitario.
   * **Opciones**:
     * **Cualquiera (Any)**: La condición se cumple si algún precio unitario cumple con la condición de comparación especificada.
     * **Todos (All)**: La condición se cumple solo si todos los precios unitarios cumplen con la condición de comparación especificada.
2. **Operador:**
   * **Descripción**: Define la condición para comparar el precio unitario con el valor especificado.
   * **Opciones**:
     * **Igual a (=)**: Verifica si el precio unitario coincide con el valor especificado.
     * **No es igual a (≠)**: Asegura que el precio unitario sea diferente del valor especificado.
     * **Mayor que (>)**: Verifica si el precio unitario es mayor que el valor especificado.
     * **Mayor o igual que (≥)**: Verifica si el precio unitario es mayor o igual que el valor especificado.
     * **Menor que (<)**: Verifica si el precio unitario es menor que el valor especificado.
     * **Menor o igual que (≤)**: Verifica si el precio unitario es menor o igual que el valor especificado.

## **Componentes Adicionales en la Versión 4:**

**Tipo de Comparación:**

* **Descripción**: Permite a los usuarios elegir qué entidades se compararán además del precio unitario.
* **Opciones**:
  * **Orden de Compra a Documento**: Compara el precio unitario en la orden de compra con el precio unitario en el documento.
  * **Recibido a Documento**: Compara la cantidad recibida con el precio unitario en el documento.
  * **Orden de Compra a Recibido**: Compara el precio unitario en la orden de compra con la cantidad recibida.

## **Funcionalidad:**

* **Evaluación de la Condición:** El sistema compara el precio unitario en el documento con el precio unitario en la orden de compra (u otra entidad seleccionada, en la Versión 4) basándose en el operador seleccionado. Si la comparación es verdadera, el flujo de trabajo procede de acuerdo con los siguientes pasos, ya sea activando la aprobación o deteniendo el proceso.
* **Ejecución de la Acción:**
  * **Condición Verdadera**: Si la condición se evalúa como verdadera (por ejemplo, el precio unitario en el documento es mayor que el valor especificado), el flujo de trabajo procederá con la acción verdadera (por ejemplo, aprobación, procesamiento del documento).
  * **Condición Falsa**: Si la condición se evalúa como falsa (por ejemplo, el precio unitario en el documento no cumple con la comparación), el flujo de trabajo no procederá.

## **Configuración:**

* **Configuración de la Versión 3:** Los usuarios configuran la tarjeta seleccionando el precio unitario en el documento, eligiendo el operador adecuado para definir cómo se comparará el precio unitario con el valor especificado y estableciendo el valor con el que comparar. Además, los usuarios seleccionan si la condición se aplica a cualquiera o a todas las instancias de la comparación de precios unitarios.
* **Configuración de la Versión 4:** En la Versión 4, los usuarios tienen la opción adicional de seleccionar el Tipo de Comparación. Esto les permite definir las entidades a comparar, como Orden de Compra a Documento, Recibido a Documento u Orden de Compra a Recibido. Esto mejora la flexibilidad de la tarjeta para comparar precios unitarios en escenarios más complejos.

## **Escenario de Ejemplo:**

*   **Ejemplo de la Versión 3:**

    Una factura muestra un precio unitario de $50. La orden de compra relacionada tiene un precio unitario de $45. La tarjeta compara los dos precios unitarios utilizando el operador "Mayor que". Dado que el precio unitario en el documento ($50) es mayor que el precio unitario en la orden de compra ($45), el flujo de trabajo activará la condición verdadera (por ejemplo, enviar el documento para revisión).
* **Ejemplo de la Versión 4:**
  Una factura muestra un precio unitario de $50, y la orden de compra relacionada autorizó un precio unitario de $45. Además, la cantidad recibida es de 60 unidades. La tarjeta compara la cantidad recibida con el precio unitario del documento utilizando el operador "Mayor que". Dado que la cantidad recibida (60) es mayor que el precio unitario ($50), el flujo de trabajo activa la condición verdadera y el documento se marca para una revisión posterior.

## **Conclusión:**

La Versión 3 de la tarjeta de flujo de trabajo "Comparación de Precios Unitarios" está diseñada para asegurar que los precios unitarios en los documentos se alineen con los de las órdenes de compra, activando acciones basadas en condiciones definidas. La Versión 4 amplía esta funcionalidad introduciendo opciones de comparación más complejas, como la comparación de órdenes de compra con documentos, cantidades recibidas con documentos y órdenes de compra con cantidades recibidas. Esta flexibilidad añadida permite a las organizaciones manejar escenarios de precios y adquisiciones más sofisticados, mejorando el control y la precisión en sus flujos de trabajo.
