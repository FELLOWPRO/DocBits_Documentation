# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para comparar los ID de artículo entre una orden de compra y un documento relacionado para garantizar que se incluyan los artículos correctos. La tarjeta evalúa si el ID de artículo de la orden de compra coincide con el ID de artículo del documento. Esta comparación puede disparar acciones si se encuentran discrepancias, garantizando que los artículos del documento se ajusten a la orden de compra.

## **Componentes de la tarjeta:**

1. **Any / All:**
   * **Descripción**: Define si la condición se aplica a alguna o a todas las instancias de comparación de ID de artículo.
   * **Opciones**:
     * **Any**: La condición se cumple si algún ID de artículo de la orden de compra coincide con el ID de artículo del documento.
     * **All**: La condición se cumple solo si todos los ID de artículo de la orden de compra coinciden con los ID de artículo del documento.
2. **Operator:**
   * **Descripción**: Define la condición para comparar el ID de artículo de la orden de compra con el ID de artículo del documento.
   * **Opciones**:
     * **Equals (=)**: Verifica si el ID de artículo de la orden de compra coincide exactamente con el ID de artículo del documento.
     * **Not Equals (≠)**: Garantiza que el ID de artículo de la orden de compra no coincida con el ID de artículo del documento.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema compara el ID de artículo de la orden de compra con el ID de artículo del documento según el operador seleccionado. Si la condición de comparación es verdadera (p. ej., los ID de artículo coinciden o no coinciden), el flujo de trabajo continuará en consecuencia.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si la condición se evalúa como verdadera (p. ej., el ID de artículo de la orden de compra es igual al ID de artículo del documento), el flujo de trabajo continuará con la acción verdadera (p. ej., aprobación o procesamiento adicional).
  * **Condición falsa**: Si la condición se evalúa como falsa (p. ej., el ID de artículo de la orden de compra no coincide con el ID de artículo del documento), el flujo de trabajo no continuará.

## **Configuración:**

* Los usuarios configuran la tarjeta seleccionando el ID de artículo tanto en la orden de compra como en el documento. A continuación, eligen el operador adecuado (Equals o Not Equals) para definir cómo se compararán los ID de artículo. Por último, los usuarios seleccionan si la condición se aplica a alguno o a todos los ID de artículo de la comparación.

## **Ejemplo de escenario:**

* Una factura incluye un artículo con el ID "ABC123" y la orden de compra relacionada también incluye un artículo con el ID "ABC123". Usando el operador "Equals", la tarjeta compara el ID de artículo del documento con el ID de artículo de la orden de compra. Dado que los ID de artículo coinciden, el flujo de trabajo continúa sin problemas.

## **Conclusión:**

La tarjeta de flujo de trabajo "Item ID Comparison" garantiza que los ID de artículo de los documentos se ajusten a los de las órdenes de compra. Esto ayuda a evitar discrepancias en los listados de artículos y garantiza que se procesen los artículos correctos según la orden de compra. La capacidad de comparar en función de alguna o de todas las instancias proporciona flexibilidad en diferentes casos de uso, mejorando la precisión y la eficiencia de los flujos de trabajo de compras.
