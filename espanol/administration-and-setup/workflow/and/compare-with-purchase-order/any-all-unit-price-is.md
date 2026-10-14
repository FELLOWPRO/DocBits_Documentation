# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo se utiliza para comparar el precio unitario de un documento con el precio unitario de una orden de compra, garantizando que los precios coincidan dentro de los niveles de tolerancia definidos. La comparación puede disparar acciones si el precio unitario no cumple las expectativas. La **versión 4** añade más flexibilidad al permitir a los usuarios elegir diferentes entidades para la comparación, proporcionando un mayor nivel de control sobre los procesos de precios y compras.

## **Componentes de la tarjeta:**

1. **Any / All:**
   * **Descripción**: Define si la condición se aplica a alguna o a todas las instancias en las que se compara el precio unitario.
   * **Opciones**:
     * **Any**: La condición se cumple si algún precio unitario cumple la condición de comparación especificada.
     * **All**: La condición se cumple solo si todos los precios unitarios cumplen la condición de comparación especificada.
2. **Operator:**
   * **Descripción**: Define la condición para comparar el precio unitario con el valor especificado.
   * **Opciones**:
     * **Equals (=)**: Verifica si el precio unitario coincide con el valor especificado.
     * **Not Equals (≠)**: Garantiza que el precio unitario sea distinto del valor especificado.
     * **Greater Than (>)**: Verifica si el precio unitario es mayor que el valor especificado.
     * **Greater or Equals (≥)**: Verifica si el precio unitario es mayor o igual que el valor especificado.
     * **Lesser Than (<)**: Verifica si el precio unitario es menor que el valor especificado.
     * **Lesser or Equals (≤)**: Verifica si el precio unitario es menor o igual que el valor especificado.

## **Componentes adicionales en la versión 4:**

**Comparison Type:**

* **Descripción**: Permite a los usuarios elegir qué entidades se compararán además del precio unitario.
* **Opciones**:
  * **Purchase Order to Document**: Compara el precio unitario de la orden de compra con el precio unitario del documento.
  * **Received to Document**: Compara la cantidad recibida con el precio unitario del documento.
  * **Purchase Order to Received**: Compara el precio unitario de la orden de compra con la cantidad recibida.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema compara el precio unitario del documento con el precio unitario de la orden de compra (u otra entidad seleccionada, en la versión 4) según el operador seleccionado. Si la comparación es verdadera, el flujo de trabajo continúa según los siguientes pasos, ya sea disparando la aprobación o deteniendo el proceso.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si la condición se evalúa como verdadera (p. ej., el precio unitario del documento es mayor que el valor especificado), el flujo de trabajo continuará con la acción verdadera (p. ej., aprobación, procesamiento del documento).
  * **Condición falsa**: Si la condición se evalúa como falsa (p. ej., el precio unitario del documento no cumple la comparación), el flujo de trabajo no continuará.

## **Configuración:**

* **Configuración de la versión 3:** Los usuarios configuran la tarjeta seleccionando el precio unitario del documento, eligiendo el operador adecuado para definir cómo se comparará el precio unitario con el valor especificado y estableciendo el valor con el que comparar. Además, los usuarios seleccionan si la condición se aplica a alguna o a todas las instancias de la comparación de precio unitario.
* **Configuración de la versión 4:** En la versión 4, los usuarios tienen la opción adicional de seleccionar el Comparison Type. Esto les permite definir las entidades a comparar, como Purchase Order to Document, Received to Document o Purchase Order to Received. Esto mejora la flexibilidad de la tarjeta para comparar precios unitarios en escenarios más complejos.

## **Ejemplo de escenario:**

*   **Ejemplo de la versión 3:**&#x20;

    Una factura muestra un precio unitario de 50 $. La orden de compra relacionada tiene un precio unitario de 45 $. La tarjeta compara los dos precios unitarios usando el operador "Greater Than". Dado que el precio unitario del documento (50 $) es mayor que el precio unitario de la orden de compra (45 $), el flujo de trabajo disparará la condición verdadera (p. ej., enviar el documento para revisión).
* **Ejemplo de la versión 4:**\
  Una factura muestra un precio unitario de 50 $ y la orden de compra relacionada autorizó un precio unitario de 45 $. Además, la cantidad recibida es de 60 unidades. La tarjeta compara la cantidad recibida con el precio unitario del documento usando el operador "Greater Than". Dado que la cantidad recibida (60) es mayor que el precio unitario (50 $), el flujo de trabajo dispara la condición verdadera y el documento se señala para una revisión adicional.

## **Conclusión:**

La versión 3 de la tarjeta de flujo de trabajo "Unit Price Comparison" está diseñada para garantizar que los precios unitarios de los documentos coincidan con los de las órdenes de compra, disparando acciones según las condiciones definidas. La versión 4 amplía esta funcionalidad introduciendo opciones de comparación más complejas, como comparar órdenes de compra con documentos, cantidades recibidas con documentos y órdenes de compra con cantidades recibidas. Esta flexibilidad añadida permite a las organizaciones manejar escenarios de precios y compras más sofisticados, mejorando el control y la precisión en sus flujos de trabajo.
