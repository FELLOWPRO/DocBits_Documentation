<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

Esta tarjeta de DocBits está diseñada para comparar un campo de datos de pedido específico, como cantidad, descuento o precio unitario, entre una confirmación de pedido y una orden de compra. Al permitir una comparación enfocada de un campo a la vez, asegura la precisión en la validación de los puntos de datos clave, manteniendo la exactitud del pedido. La **Versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades como la orden de compra, cantidades recibidas y el documento mismo, añadiendo más flexibilidad y control al flujo de trabajo.

## Componentes de la Tarjeta:

1. **Cualquiera/Todos (Any/All)**
   * **Descripción:** Determina si la condición se aplica a cualquiera o a todas las líneas de la confirmación del pedido.
     **Opciones:**
     * **Cualquiera (Any)**: La comparación se activará si el valor del campo seleccionado en cualquier línea de la confirmación del pedido coincide con el valor correspondiente en la orden de compra.
     * **Todos (All)**: La comparación se activará solo si el valor del campo seleccionado en todas las líneas de la confirmación del pedido coincide con el valor correspondiente en la orden de compra.
2. **Campo de Datos del Pedido**
   * **Descripción**: Especifica el campo de datos que se comparará entre la confirmación del pedido y la orden de compra.
   * **Detalle**: Los usuarios pueden seleccionar uno de los siguientes campos para la comparación:
     * **Cantidad**: Compara la cantidad pedida con la cantidad confirmada.
     * **Descuento**: Valida que el descuento en la confirmación coincida con la orden de compra.
     * **Precio Unitario**: Asegura que el precio unitario en la confirmación se alinee con la orden de compra.
3. **Operador**
   * **Descripción**: Define la condición aplicada a la comparación del campo de datos seleccionado.
   * **Opciones:**
     * **Igual a (=)**: Confirma que el valor coincide con la orden de compra.
     * **No es igual a (≠)**: Asegura que el valor sea diferente de la orden de compra.
     * **Mayor que (>)**: Verifica que el valor exceda el valor de la orden de compra.
     * **Mayor o igual que (≥)**: Confirma que el valor sea igual o exceda el valor de la orden de compra.
     * **Menor que (<)**: Verifica que el valor esté por debajo del valor de la orden de compra.
     * **Menor o igual que (≤)**: Confirma que el valor sea inferior o igual al valor de la orden de compra.

## **Componentes Adicionales en la Versión 4**:

* **Tipo de Comparación**: Selecciona las entidades a comparar. Las opciones incluyen:
  * **Orden de Compra a Documento**: Compara los datos de la orden de compra con el documento relacionado.
  * **Recibido a Documento**: Compara los datos recibidos (por ejemplo, cantidades recibidas) con el documento.
  * **Orden de Compra a Recibido**: Compara los datos de la orden de compra con las cantidades recibidas.

## Funcionalidad:

* **Comparación de Campos**: El sistema compara el campo de datos del pedido seleccionado (Precio Unitario, Descuento o Cantidad) de la confirmación del pedido con el valor correspondiente en la orden de compra.
* **Ejecución de la Acción**: Basándose en el resultado de la comparación y la condición del operador, la tarjeta puede activar acciones de seguimiento, como notificaciones o alertas.

## Escenario de Ejemplo:

* Una confirmación de pedido especifica un **precio unitario** de $50, mientras que la orden de compra indica $45. Utilizando el operador "Mayor que", la tarjeta señala la discrepancia, permitiendo que el equipo de adquisiciones la aborde antes del procesamiento.

## Conclusión:

Esta tarjeta simplifica la validación de los campos de datos de pedidos individuales, asegurando el cumplimiento de los términos de la orden de compra. Al aislar un campo a la vez para la comparación, admite revisiones específicas y la prevención de errores en el procesamiento de pedidos.
