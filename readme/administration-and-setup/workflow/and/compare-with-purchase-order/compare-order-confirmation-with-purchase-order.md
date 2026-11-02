# Comparar la confirmación del pedido con el pedido de compra

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v1-es-es.png" alt="Comparar la confirmación del pedido con el pedido de compra, Versión 1" width="634"><figcaption><p>Versión 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v2-es-es.png" alt="Comparar la confirmación del pedido con el pedido de compra, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v3-es-es.png" alt="Comparar la confirmación del pedido con el pedido de compra, Versión 3" width="634"><figcaption><p>Versión 3</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v4-es-es.png" alt="Comparar la confirmación del pedido con el pedido de compra, Versión 4" width="634"><figcaption><p>Versión 4</p></figcaption></figure>

## Propósito:

Esta tarjeta DocBits está diseñada para comparar un campo de datos de pedido específico (como cantidad, descuento o precio unitario) entre una confirmación de pedido y una orden de compra. Al permitir una comparación enfocada de un campo a la vez, garantiza la precisión en la validación de puntos de datos clave, manteniendo la precisión de los pedidos. **Versión 4** amplía esta funcionalidad al permitir comparaciones entre diferentes entidades, como la orden de compra, las cantidades recibidas y el documento en sí, agregando más flexibilidad y control al flujo de trabajo.

## Componentes de la Tarjeta:

1. **Cualquiera/Todos**
   * **Descripción:** Determina si la condición se aplica a alguna o todas las líneas en la confirmación del pedido.\
     **Opciones:**
     * **Cualquiera**: La comparación se activará si el valor del campo seleccionado en cualquier línea de la confirmación del pedido coincide con el valor correspondiente en la orden de compra.
     * **Todos**: La comparación se activará solo si el valor del campo seleccionado en todas las líneas de la confirmación del pedido coincide con el valor correspondiente en la orden de compra.
2. **Campo de datos del pedido**
   * **Descripción**: Especifica el campo de datos a comparar entre la confirmación del pedido y la orden de compra.
   * **Detalle**: los usuarios pueden seleccionar uno de los siguientes campos para comparar:
     * **Cantidad**: Compara la cantidad pedida con la cantidad confirmada.
     * **Descuento**: Valida que el descuento en la confirmación coincide con la orden de compra.
     * **Precio unitario**: Garantiza que el precio unitario en la confirmación se alinee con la orden de compra.
3. **Operador**
   * **Descripción**: Define la condición aplicada a la comparación del campo de datos seleccionado.
   * **Opciones**:
     * **Igual a (=)**: Confirma que el valor coincide con la orden de compra.
     * **No es igual a (≠)**: Asegura que el valor sea diferente al de la orden de compra.
     * **Mayor que (>)**: Verifica que el valor exceda el valor de la orden de compra.
     * **Mayor o Igual (≥)**: Confirma que el valor iguala o excede el valor de la orden de compra.
     * **Less Than (<)**: Comprueba que el valor esté por debajo del valor de la orden de compra.
     * **Menor o Igual (≤)**: Confirma que el valor es inferior o igual al valor de la orden de compra.

## **Componentes adicionales en la versión 4**:

* **Tipo de comparación**: Selecciona las entidades a comparar. Las opciones incluyen:
  * **Orden de Compra a Documento**: Compara los datos de la orden de compra con el documento relacionado.
  * **Recibido en documento**: Compara los datos recibidos (por ejemplo, cantidades recibidas) con el documento.
  * **Orden de Compra a Recibir**: Compara los datos de la orden de compra con las cantidades recibidas.

## Funcionalidad:

* **Comparación de campos**: El sistema compara el campo de datos del pedido seleccionado (Precio unitario, Descuento o Cantidad) de la confirmación del pedido con el valor correspondiente en la orden de compra.
* **Ejecución de acción**: según el resultado de la comparación y la condición del operador, la tarjeta puede activar acciones de seguimiento, como notificaciones o alertas.

## Escenario de ejemplo:

* Una confirmación de pedido especifica un **precio unitario** de $50, mientras que la orden de compra indica $45. Utilizando el operador "Mayor que", la tarjeta señala la discrepancia, lo que permite al equipo de adquisiciones abordarla antes de procesarla.

## Conclusión:

Esta tarjeta simplifica la validación de los campos de datos de pedidos individuales, garantizando el cumplimiento de los términos de la orden de compra. Al aislar un campo a la vez para compararlo, admite revisiones específicas y prevención de errores en el procesamiento de pedidos.

Consulte [dirección de comparación, base de tolerancia y versiones de tarjetas guardadas](../../cards-overview/po-comparison-versions-guide.md) antes de cambiar los lados de comparación.
