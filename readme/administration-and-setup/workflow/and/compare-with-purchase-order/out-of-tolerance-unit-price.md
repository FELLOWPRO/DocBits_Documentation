# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para evaluar si el valor combinado de los precios unitarios y un campo especificado supera o queda por debajo de un umbral definido. Ayuda a identificar cualquier discrepancia en la que los precios unitarios, al combinarse con otros campos, queden fuera de tolerancia, garantizando que las condiciones de precios cumplan las expectativas y señalando cualquier problema para su revisión o acción adicional.

## **Componentes de la tarjeta:**

1. **Field Name:**
   * **Descripción**: Especifica el campo del documento que contiene el valor que se combinará con el precio unitario.
   * **Detalle**: El valor de este campo se combinará con el precio unitario para crear el valor combinado total para la comparación.
2. **Operator:**
   * **Descripción**: Define la condición para comparar el valor combinado del precio unitario y el valor del campo con el valor especificado.
   * **Opciones**:
     * **Equals (=)**: Verifica si el valor combinado del precio unitario y el campo coincide con el valor especificado.
     * **Not Equals (≠)**: Garantiza que el valor combinado del precio unitario y el campo sea distinto del valor especificado.
     * **Greater Than (>)**: Verifica si el valor combinado del precio unitario y el campo supera el valor especificado.
     * **Greater or Equals (≥)**: Verifica si el valor combinado del precio unitario y el campo es mayor o igual que el valor especificado.
     * **Lesser Than (<)**: Verifica si el valor combinado del precio unitario y el campo es menor que el valor especificado.
     * **Lesser or Equals (≤)**: Verifica si el valor combinado del precio unitario y el campo es menor o igual que el valor especificado.
3. **Value:**
   * **Descripción**: Especifica el valor con el que se comparará el valor combinado del precio unitario y el campo.
   * **Detalle**: Este valor numérico representa el umbral para la comparación. Si el valor combinado del precio unitario y el campo supera o queda por debajo de este valor (según el operador seleccionado), la condición disparará las acciones especificadas.

## **Funcionalidad:**

* &#x20;**Evaluación de la condición:** El sistema calcula el valor combinado multiplicando o sumando el precio unitario con el valor del campo, según la configuración. A continuación, el resultado se compara con el valor especificado usando el operador seleccionado. Si la condición se cumple (es decir, el valor combinado está fuera de tolerancia), el flujo de trabajo continúa con el siguiente paso, ya sea aprobación, rechazo o revisión adicional.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si la comparación resulta verdadera (es decir, el valor combinado cumple la condición), el flujo de trabajo dispara la acción asociada a la condición verdadera (p. ej., aprobación o notificación).
  * **Condición falsa**: Si la comparación resulta falsa (es decir, el valor combinado no cumple la condición), el flujo de trabajo no continuará.

## **Configuración:**

* Los usuarios seleccionan el campo que contiene el valor que se combinará con el precio unitario. A continuación, eligen el operador adecuado para determinar cómo se comparará el valor combinado con el valor especificado. Por último, el usuario establece el valor con el que se comparará el precio combinado.

## **Ejemplo de escenario:**

* Una factura incluye 50 unidades de un producto a 30 $ cada una, con un total de 1500 $. El documento relacionado tiene un campo de cantidad con un valor de 10. El precio combinado se calcula multiplicando el precio unitario (30 $) y la cantidad (10), lo que da 300 $. A continuación, la tarjeta compara este valor combinado con un umbral de 250 $. Usando el operador "Greater Than", la tarjeta identifica que 300 $ es mayor que 250 $, lo que dispara un proceso de aprobación para el documento.

## **Conclusión:**

La tarjeta de flujo de trabajo "Out of Tolerance Unit Prices Combined with Fields" ayuda a garantizar que los valores de precios y campos estén alineados con las reglas de negocio. Al automatizar esta comprobación, las organizaciones pueden identificar discrepancias de forma temprana en el proceso, garantizando que cualquier precio unitario fuera de tolerancia se señale para su revisión o la acción necesaria.
