# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para comparar el tipo de pedido de una orden de compra con un valor especificado. La tarjeta comprueba si el tipo de pedido de la orden de compra cumple la condición especificada (p. ej., si es igual, distinto, mayor que o cumple otra condición) para garantizar que la orden de compra esté clasificada correctamente. Esta comparación puede disparar acciones según condiciones específicas, como enrutar el pedido para una revisión o aprobación adicional si se encuentran discrepancias.

## **Componentes de la tarjeta:**

1. **Any/All:**
   * **Descripción**: Define si la condición se aplica a alguna o a todas las órdenes de compra que se evalúan en el flujo de trabajo.
   * **Opciones**:
     * **Any**: La condición se cumple si alguna de las órdenes de compra coincide con la condición especificada.
     * **All**: La condición se cumple solo si todas las órdenes de compra cumplen la condición especificada.
2. **Operator:**
   * **Descripción**: Define la condición que se aplicará para comparar el tipo de pedido con un valor especificado.
   * **Opciones**:
     * **Equals (=)**: Comprueba si el tipo de pedido coincide con el valor especificado.
     * **Not Equals (≠)**: Garantiza que el tipo de pedido sea distinto del valor especificado.
3. **Order Type:**
   * **Descripción**: Especifica el valor con el que se comparará el tipo de pedido de la orden de compra.
   * **Detalle**: El valor debe coincidir con el tipo de pedido o la clasificación del sistema.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema evalúa el tipo de pedido de la orden de compra frente a la condición especificada usando el operador seleccionado. Si el tipo de pedido coincide (o no coincide) con el valor especificado, el flujo de trabajo continúa en consecuencia.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si la condición se evalúa como verdadera (p. ej., el tipo de pedido coincide con el valor especificado), el flujo de trabajo continuará, posiblemente disparando acciones o pasos de procesamiento adicionales.
  * **Condición falsa**: Si la condición se evalúa como falsa (p. ej., el tipo de pedido no coincide con el valor especificado), el flujo de trabajo no continuará.

## **Configuración:**

* Los usuarios configuran la tarjeta seleccionando el campo del tipo de pedido de la orden de compra y eligiendo el operador que define cómo se comparará el tipo de pedido. A continuación, establecen el valor especificado y deciden si aplicar la condición a alguna o a todas las líneas de la orden de compra.

## **Ejemplo de escenario:**

* Una orden de compra tiene el tipo de pedido "Standard". El flujo de trabajo está configurado para comprobar si el tipo de pedido es "Urgent". Usando el operador "Equals", la tarjeta compara el tipo de pedido y descubre que no coincide con el valor especificado, lo que dispara el flujo de trabajo para enviar el pedido a revisión debido al desajuste.

## **Conclusión:**

La tarjeta de flujo de trabajo "Order Type of Purchase Order" garantiza que las órdenes de compra se clasifiquen correctamente según su tipo de pedido especificado. Al automatizar la comparación de los tipos de pedido, las organizaciones pueden garantizar que las órdenes de compra se procesen según sus clasificaciones previstas, ayudando a aplicar el cumplimiento y a agilizar los flujos de trabajo de compras.
