# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para evaluar si el precio unitario, combinado con el valor de un campo especificado (como cantidad, descuento o cargos adicionales), cumple una condición definida. La tarjeta compara el precio unitario y el valor del campo con un umbral especificado para ayudar a garantizar que los precios se ajusten a las expectativas. Esta comparación puede disparar acciones según condiciones específicas, como señalar discrepancias o automatizar procesos de aprobación en los flujos de trabajo de compras o recepción.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción:** Especifica el campo del documento que contiene el valor que se combinará con el precio unitario.
   * **Detalle:** Debe coincidir con el identificador exacto del primer campo dentro del documento.
2. **Operator**
   * **Descripción:** Define la condición que se aplicará a la comparación entre el valor combinado y el valor especificado.
   * **Opciones:**
     * **Equals (=):** Comprueba si el valor combinado del precio unitario y el campo coincide con el valor especificado.
     * **Not Equals (≠):** Garantiza que el valor combinado del precio unitario y el campo sea distinto del valor especificado.
     * **Greater Than (>):** Verifica si el valor combinado es mayor que el valor especificado.
     * **Greater or Equals (≥):** Comprueba si el valor combinado es mayor o igual que el valor especificado.
     * **Lesser Than (<):** Verifica si el valor combinado es menor que el valor especificado.
     * **Lesser or Equals (≤):** Comprueba si el valor combinado es menor o igual que el valor especificado.
3. **Value**
   * **Descripción:** Especifica el valor con el que se comparará el valor combinado del precio unitario y el campo.
   * **Detalle:** El valor debe ser un valor numérico.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema evalúa el valor combinado del precio unitario y el campo según el operador seleccionado y lo compara con el valor especificado. El resultado de esta evaluación determina si la condición es verdadera o falsa.
* **Ejecución de la acción:**
  * **Condición verdadera:** Si la comparación resulta verdadera (p. ej., el valor combinado supera el valor especificado), el flujo de trabajo continúa con la condición verdadera. Esto podría disparar acciones como aprobación, enrutamiento de documentos o la aplicación de reglas de procesamiento.
  * **Condición falsa:** Si la comparación resulta falsa (p. ej., el valor combinado no cumple la condición), el flujo de trabajo continúa con la condición falsa. Esto podría disparar una notificación, enviar el documento a revisión manual o detener el flujo de trabajo.

## **Configuración:**

* Los usuarios comienzan seleccionando el campo o campos del documento que contienen los valores que se combinarán con el precio unitario. Tras seleccionar el campo, eligen el operador adecuado para definir cómo se comparará el valor combinado con el valor especificado. A continuación, pueden establecer el valor.

## **Ejemplo de escenario:**

* Una factura incluye 50 unidades de un producto a 20 $ cada una, con un total de 1000 $. El documento relacionado tiene un campo de cantidad con un valor de 10. Usando el operador "Greater Than", la tarjeta compara el valor combinado del precio unitario (20 $) y la cantidad (10), que equivale a 200 $. La tarjeta comprueba si el valor combinado es mayor que 150 $ (el valor especificado). Dado que el valor combinado de 200 $ es mayor que el umbral de 150 $, el flujo de trabajo continúa para disparar una aprobación del documento.

## **Conclusión:**

La tarjeta de flujo de trabajo "Unit Price Combined with Fields" garantiza que se cumplan las condiciones de precios evaluando el valor combinado del precio unitario y un campo especificado. Al automatizar esta comparación, las organizaciones pueden garantizar la coherencia y señalar discrepancias en precios o cantidades antes de continuar con la aprobación, ayudando a agilizar los procesos de compras y financieros.
