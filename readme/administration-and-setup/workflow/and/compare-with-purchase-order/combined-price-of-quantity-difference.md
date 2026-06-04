# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**:

Esta tarjeta de flujo de trabajo evalúa el precio combinado de una diferencia de cantidad, comparándolo con un valor especificado. Ayuda a automatizar acciones basadas en discrepancias de precio y cantidad entre documentos relacionados, mejorando los flujos de trabajo de compras y recepción. La **versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades, como la orden de compra, las cantidades recibidas y el propio documento, añadiendo más flexibilidad y control al flujo de trabajo.

## **Componentes de la tarjeta**:

1. **Operator**:&#x20;
   * **Descripción:** La condición para comparar el precio combinado con un valor especificado.
   * **Opciones:**
     * **Equals (=)**: Comprueba si el precio combinado coincide con el valor especificado.
     * **Not Equals (≠)**: Garantiza que el precio combinado sea distinto del valor especificado.
     * **Greater Than (>)**: Verifica si el precio combinado es mayor que el valor especificado.
     * **Greater or Equals (≥)**: Comprueba si el precio combinado es mayor o igual que el valor especificado.
     * **Lesser Than (<)**: Verifica si el precio combinado es menor que el valor especificado.
     * **Lesser or Equals (≤)**: Comprueba si el precio combinado es menor o igual que el valor especificado.
2. **Value**:&#x20;
   * **Descripción:** Especifica el valor con el que se comparará el precio combinado de la diferencia de cantidad.
   * **Detalle:** El valor debe ser un valor numérico.

## **Componentes adicionales en la versión 4**:

* **Comparison Type**: Selecciona las entidades a comparar. Las opciones incluyen:
  * **Purchase Order to Document**: Compara las cantidades y los precios entre la orden de compra y el documento relacionado.
  * **Received to Document**: Compara las cantidades recibidas con las cantidades del documento.
  * **Purchase Order to Received**: Compara las cantidades de la orden de compra con las cantidades recibidas.

## **Funcionalidad**:

* **Evaluación de la condición**: Calcula el precio combinado multiplicando la diferencia de cantidad por el precio por unidad y lo compara con el valor especificado usando el operador seleccionado.\
  La **versión 4** añade la opción de comparar entidades adicionales según la configuración del usuario, como orden de compra con recibido u orden de compra con documento.
* **Ejecución de la acción**: Según si el precio combinado cumple la condición especificada, el flujo de trabajo continuará con condiciones verdaderas o falsas para disparar acciones o detener el flujo de trabajo. La **versión 4** también permite una ejecución de acciones más dinámica, donde el tipo de condición (p. ej., orden de compra con recibido) influye en el siguiente paso.

## **Configuración**:

* **Versión 3**: Los usuarios configuran la tarjeta seleccionando los campos del documento para la diferencia de cantidad y el precio por unidad. A continuación, se elige el operador para definir cómo se comparará el precio combinado con el valor especificado. Por último, los usuarios establecen la condición de continuación (verdadera o falsa), que determina el siguiente paso del flujo de trabajo.
* **Versión 4**: Además de la configuración de la **versión 3**, los usuarios tienen una opción adicional para configurar el **Comparison Type**. Esto define qué entidades se compararán, como **Purchase Order to Document**, **Received to Document** o **Purchase Order to Received**.

## **Ejemplo de escenario**:

* Una factura muestra 50 unidades de un producto a 100 $ cada una, con un total de 5000 $. La orden de compra relacionada autorizó una compra de 4500 $ por 45 unidades. La diferencia de cantidad es de 5 unidades y el precio combinado de la diferencia es de 500 $. La tarjeta compara la cantidad de la orden de compra (45 unidades) con la cantidad recibida (50 unidades) y comprueba si el precio combinado es mayor que 400 $ (el valor especificado). Usando el operador **Greater Than (>)**, la tarjeta identifica la discrepancia y la señala para que la revise el equipo financiero.

## **Conclusión**:

La **versión 3** de la tarjeta de flujo de trabajo "Combined Price of Quantity Difference" ofrece un enfoque sencillo para comparar discrepancias de cantidad y disparar acciones según umbrales de precio.\
La **versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades (orden de compra, recibido, documento), proporcionando más flexibilidad y control sobre el flujo de trabajo. Las organizaciones ahora pueden automatizar escenarios más complejos y aplicar un control más estricto sobre sus procesos de compras y recepción.
