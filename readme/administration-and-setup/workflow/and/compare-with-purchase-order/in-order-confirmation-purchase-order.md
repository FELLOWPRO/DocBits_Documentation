---
hidden: true
---

# Comparación entre la confirmación de pedido y el pedido de compra

Use **Comparar con la orden de compra** en el Constructor de flujo de trabajo cuando una confirmación de pedido deba comprobarse frente a su orden de compra. Añada la tarjeta bajo **Y....**, elija los datos del pedido, un operador y qué debe ocurrir con el resultado. Las capturas siguientes muestran dos versiones disponibles de la tarjeta en la interfaz en español. Sus campos aún son marcadores de posición; configúrelos para su propio flujo de trabajo antes de guardar.

## Escribir el resultado en un campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-77711a53d4d0-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

Elija **Datos del pedido** de la confirmación de pedido y un **Operador** para la comparación con la orden de compra. Escriba el **Texto** que se debe escribir, seleccione el **Nombre del campo** y elija el **Resultado de la condición** que debe activar la escritura.

## Comparar los datos

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-d49578e0648e-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

Elija **Cualquiera/Todos** para decidir si una o todas las condiciones seleccionadas deben coincidir. Después seleccione los **Datos del pedido**, el **Operador** y los **Datos comparativos** para la comparación con la orden de compra.

Para los pasos siguientes, vea [Flujo de trabajo](../..) y [Comparar con la orden de compra](.).

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Verifique la confirmación de un pedido con su orden de compra vinculada.

**Configuración:** Utilice un pedido de demostración y confirmación con el mismo proveedor, referencia de artículo y valores comparados. Seleccione la dirección de comparación deseada y los campos que ofrece esta versión.

**Resultado esperado y contraejemplo:** Se pasa la comparación coincidente. Cambie el valor de un elemento comparado en un caso de prueba separado y verifique que se detecte; la falta de un pedido vinculado es un problema de datos aparte.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
