# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

Esta tarjeta de DocBits está diseñada para comparar un campo de datos de pedido específico —como la cantidad, el descuento o el precio unitario— entre una confirmación de pedido y una orden de compra. Al permitir una comparación centrada de un campo a la vez, garantiza la precisión en la validación de puntos de datos clave, manteniendo la exactitud del pedido. La **versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades, como la orden de compra, las cantidades recibidas y el propio documento, añadiendo más flexibilidad y control al flujo de trabajo.

## Componentes de la tarjeta:

1. **Any/All**&#x20;
   * **Descripción:** Determina si la condición se aplica a alguna o a todas las líneas de la confirmación de pedido.\
     **Opciones:**
     * **Any**: La comparación se disparará si el valor del campo seleccionado en alguna línea de la confirmación de pedido coincide con el valor correspondiente de la orden de compra.
     * **All**: La comparación se disparará solo si el valor del campo seleccionado en todas las líneas de la confirmación de pedido coincide con el valor correspondiente de la orden de compra.
2. **Order Data Field**
   * **Descripción**: Especifica el campo de datos que se comparará entre la confirmación de pedido y la orden de compra.
   * **Detalle**: Los usuarios pueden seleccionar uno de los siguientes campos para la comparación:
     * **Quantity**: Compara la cantidad pedida con la cantidad confirmada.
     * **Discount**: Valida que el descuento de la confirmación coincida con la orden de compra.
     * **Unit Price**: Garantiza que el precio unitario de la confirmación se ajuste a la orden de compra.
3. **Operator**
   * **Descripción**: Define la condición que se aplica a la comparación del campo de datos seleccionado.
   * **Opciones**:
     * **Equals (=)**: Confirma que el valor coincide con la orden de compra.
     * **Not Equals (≠)**: Garantiza que el valor sea distinto del de la orden de compra.
     * **Greater Than (>)**: Verifica que el valor supere el valor de la orden de compra.
     * **Greater or Equals (≥)**: Confirma que el valor sea igual o superior al valor de la orden de compra.
     * **Less Than (<)**: Comprueba que el valor esté por debajo del valor de la orden de compra.
     * **Less or Equals (≤)**: Confirma que el valor esté por debajo o sea igual al valor de la orden de compra.

## **Componentes adicionales en la versión 4**:

* **Comparison Type**: Selecciona las entidades a comparar. Las opciones incluyen:
  * **Purchase Order to Document**: Compara los datos de la orden de compra con el documento relacionado.
  * **Received to Document**: Compara los datos recibidos (p. ej., cantidades recibidas) con el documento.
  * **Purchase Order to Received**: Compara los datos de la orden de compra con las cantidades recibidas.

## Funcionalidad:

* **Comparación de campos**: El sistema compara el campo de datos de pedido seleccionado (Unit Price, Discount o Quantity) de la confirmación de pedido con el valor correspondiente de la orden de compra.
* **Ejecución de la acción**: Según el resultado de la comparación y la condición del operador, la tarjeta puede disparar acciones de seguimiento, como notificaciones o alertas.

## Ejemplo de escenario:

* Una confirmación de pedido especifica un **precio unitario** de 50 $, mientras que la orden de compra indica 45 $. Usando el operador "Greater Than", la tarjeta señala la discrepancia, permitiendo al equipo de compras abordarla antes de procesarla.

## Conclusión:

Esta tarjeta simplifica la validación de campos de datos de pedido individuales, garantizando el cumplimiento de los términos de la orden de compra. Al aislar un campo a la vez para la comparación, facilita revisiones específicas y la prevención de errores en el procesamiento de pedidos.
