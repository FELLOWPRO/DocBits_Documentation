# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para comparar la cantidad de un documento con la tolerancia definida en la orden de compra. Permite a los usuarios evaluar si la cantidad cumple ciertas condiciones, como la igualdad o el exceso de la tolerancia especificada. En la versión 4, la tarjeta amplía su funcionalidad añadiendo la capacidad de comparar varias entidades, incluida la orden de compra, las cantidades recibidas y las cantidades del documento, ofreciendo mayor flexibilidad para manejar diferentes escenarios.

## **Componentes de la tarjeta:**

1. **Any / All:**
   * **Descripción**: Especifica cómo debe aplicarse la comparación entre varios elementos o condiciones.
   * **Opciones**:
     * **Any**: Al menos una de las condiciones debe ser verdadera para que se dispare la acción.
     * **All**: Todas las condiciones deben ser verdaderas para que la acción continúe.
2. **Operator:**
   * **Descripción**: Define la condición que se aplicará para comparar la cantidad del documento con la tolerancia especificada.
   * **Opciones**:
     * **Equals (=)**: Comprueba si la cantidad coincide con el valor de tolerancia especificado.
     * **Not Equals (≠)**: Garantiza que la cantidad sea distinta del valor de tolerancia especificado.
     * **Greater Than (>)**: Verifica si la cantidad es mayor que la tolerancia especificada.
     * **Greater or Equals (≥)**: Comprueba si la cantidad es mayor o igual que la tolerancia especificada.
     * **Lesser Than (<)**: Verifica si la cantidad es menor que la tolerancia especificada.
     * **Lesser or Equals (≤)**: Comprueba si la cantidad es menor o igual que la tolerancia especificada.
3. **Tolerance Amount:**
   * **Descripción**: Especifica el valor de tolerancia con el que se comparará la cantidad del documento.
   * **Detalle**: Este valor es numérico y representa el umbral de variación permitida en la cantidad.
4. **Tolerance Type:**
   * **Descripción**: Define el tipo de tolerancia que se aplicará.
   * **Opciones**:
     * **Percentage**: La tolerancia se calcula como un porcentaje de la cantidad de la orden de compra.
     * **Value**: La tolerancia se especifica como un valor numérico fijo.

## **Componentes adicionales en la versión 4:**

* **Comparison Type**: Selecciona las entidades a comparar, proporcionando más flexibilidad en cómo se evalúan las cantidades en la versión 4.
  * **Purchase Order to Document**: Compara la cantidad de la orden de compra con la cantidad del documento relacionado.
  * **Received to Document**: Compara la cantidad recibida con la cantidad del documento.
  * **Purchase Order to Received**: Compara la cantidad de la orden de compra con la cantidad recibida.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema compara la cantidad del documento con la tolerancia de la orden de compra según el operador y el importe/tipo de tolerancia seleccionados. En la versión 4, el **Comparison Type** permite comparar diferentes cantidades, como orden de compra con recibido, u orden de compra con documento, proporcionando una comparación más dinámica.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si la comparación resulta verdadera (p. ej., la cantidad del documento está dentro del rango de tolerancia aceptable), el flujo de trabajo continuará.
  * **Condición falsa**: Si la comparación resulta falsa (p. ej., la cantidad no cumple la tolerancia), el flujo de trabajo no continuará.

## **Configuración:**

**Versión 3:**

* Los usuarios configuran la tarjeta seleccionando la cantidad del documento, definiendo el importe y el tipo de tolerancia, y eligiendo el operador adecuado para comparar la cantidad con la tolerancia. La tarjeta evalúa si la cantidad está dentro del umbral de tolerancia y continúa con la acción "True" o "False" según el resultado.

**Versión 4:**

* Además de la configuración de la versión 3, los usuarios pueden seleccionar el **Comparison Type**, lo que permite comparaciones entre diferentes entidades, como:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Ejemplo de escenario:**

Una factura muestra que se entregaron 100 unidades, pero la orden de compra solo autorizó 90 unidades. El importe de tolerancia se establece en 10 unidades y el tipo de tolerancia es absoluto.

* **Versión 3**: La tarjeta compara las 100 unidades del documento con la tolerancia de 90 unidades de la orden de compra. Si la cantidad supera la tolerancia, la tarjeta señala la discrepancia para una revisión adicional.
* **Versión 4**: La tarjeta podría comparar la **cantidad de la orden de compra** (90 unidades) con la **cantidad recibida** (100 unidades) o la **cantidad del documento** (100 unidades). Dependiendo del **Comparison Type** seleccionado, comprueba si la diferencia entre las dos entidades supera la tolerancia y dispara la acción correspondiente.

## **Conclusión:**

* **Versión 3**: Esta tarjeta de flujo de trabajo compara la cantidad del documento con la tolerancia de la orden de compra, ayudando a garantizar que las discrepancias de cantidad se señalen y se gestionen adecuadamente.
* **Versión 4**: Amplía esta funcionalidad permitiendo a los usuarios comparar diferentes entidades, como orden de compra con recibido u orden de compra con documento, proporcionando mayor flexibilidad para manejar escenarios más complejos. La versión 4 garantiza un control más estricto sobre los flujos de trabajo de compras y recepción, ofreciendo comparaciones y acciones más dinámicas según el tipo de comparación elegido.
