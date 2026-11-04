<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para comparar la cantidad en un documento contra la tolerancia definida en la orden de compra. Permite a los usuarios evaluar si la cantidad cumple ciertas condiciones, como igualdad o exceder la tolerancia especificada. En la Versión 4, la tarjeta amplía su funcionalidad añadiendo la capacidad de comparar múltiples entidades, incluyendo la orden de compra, cantidades recibidas y cantidades del documento, ofreciendo una mayor flexibilidad en el manejo de diferentes escenarios.

## **Componentes de la Tarjeta:**

1. **Cualquiera / Todos (Any / All):**
   * **Descripción**: Especifica cómo se debe aplicar la comparación a través de múltiples ítems o condiciones.
   * **Opciones**:
     * **Cualquiera (Any)**: Al menos una de las condiciones debe ser verdadera para que se active la acción.
     * **Todos (All)**: Todas las condiciones deben ser verdaderas para que la acción proceda.
2. **Operador:**
   * **Descripción**: Define la condición que se aplicará para comparar la cantidad del documento contra la tolerancia especificada.
   * **Opciones**:
     * **Igual a (=)**: Verifica si la cantidad coincide con el valor de tolerancia especificado.
     * **No es igual a (≠)**: Asegura que la cantidad sea diferente del valor de tolerancia especificado.
     * **Mayor que (>)**: Verifica si la cantidad es mayor que la tolerancia especificada.
     * **Mayor o igual que (≥)**: Verifica si la cantidad es mayor o igual que la tolerancia especificada.
     * **Menor que (<)**: Verifica si la cantidad es menor que la tolerancia especificada.
     * **Menor o igual que (≤)**: Verifica si la cantidad es menor o igual que la tolerancia especificada.
3. **Monto de Tolerancia:**
   * **Descripción**: Especifica el valor de tolerancia contra el cual se comparará la cantidad del documento.
   * **Detalle**: Este valor es numérico y representa el umbral de varianza permitida en la cantidad.
4. **Tipo de Tolerancia:**
   * **Descripción**: Define el tipo de tolerancia que se aplicará.
   * **Opciones**:
     * **Porcentaje**: La tolerancia se calcula como un porcentaje de la cantidad de la orden de compra.
     * **Valor**: La tolerancia se especifica como un valor numérico fijo.

## **Componentes Adicionales en la Versión 4:**

* **Tipo de Comparación**: Selecciona las entidades a comparar, proporcionando más flexibilidad en cómo se evalúan las cantidades en la Versión 4.
  * **Orden de Compra a Documento**: Compara la cantidad en la orden de compra con la cantidad en el documento relacionado.
  * **Recibido a Documento**: Compara la cantidad recibida con la cantidad en el documento.
  * **Orden de Compra a Recibido**: Compara la cantidad de la orden de compra con la cantidad recibida.

## **Funcionalidad:**

* **Evaluación de la Condición:** El sistema compara la cantidad en el documento contra la tolerancia en la orden de compra basándose en el operador seleccionado y el monto/tipo de tolerancia. En la Versión 4, el **Tipo de Comparación** permite comparar diferentes cantidades, como orden de compra a recibido, u orden de compra a documento, proporcionando una comparación más dinámica.
* **Ejecución de la Acción:**
  * **Condición Verdadera**: Si la comparación resulta verdadera (por ejemplo, la cantidad del documento está dentro del rango de tolerancia aceptable), el flujo de trabajo procederá.
  * **Condición Falsa**: Si la comparación resulta falsa (por ejemplo, la cantidad no cumple con la tolerancia), el flujo de trabajo no procederá.

## **Configuración:**

**Versión 3:**

* Los usuarios configuran la tarjeta seleccionando la cantidad del documento, definiendo el monto y tipo de tolerancia, y eligiendo el operador adecuado para comparar la cantidad contra la tolerancia. La tarjeta evalúa si la cantidad está dentro del umbral de tolerancia y procede con la acción "Verdadera" o "Falsa" basándose en el resultado.

**Versión 4:**

* Además de la configuración en la Versión 3, los usuarios pueden seleccionar el **Tipo de Comparación**, permitiendo comparaciones entre diferentes entidades, tales como:
  * **Orden de Compra a Documento**
  * **Recibido a Documento**
  * **Orden de Compra a Recibido**

## **Escenario de Ejemplo:**

Una factura muestra que se entregaron 100 unidades, pero la orden de compra solo autorizó 90 unidades. El monto de tolerancia se establece en 10 unidades y el tipo de tolerancia es absoluto.

* **Versión 3**: La tarjeta compara las 100 unidades en el documento contra la tolerancia de la orden de compra de 90 unidades. Si la cantidad excede la tolerancia, la tarjeta señala la discrepancia para una revisión posterior.
* **Versión 4**: La tarjeta podría comparar la **cantidad de la orden de compra** (90 unidades) con la **cantidad recibida** (100 unidades) o la **cantidad del documento** (100 unidades). Dependiendo del **Tipo de Comparación** seleccionado, verifica si la diferencia entre las dos entidades excede la tolerancia y activa la acción correspondiente.

## **Conclusión:**

* **Versión 3**: Esta tarjeta de flujo de trabajo compara la cantidad del documento con la tolerancia de la orden de compra, ayudando a asegurar que las discrepancias en la cantidad sean señaladas y manejadas adecuadamente.
* **Versión 4**: Amplía esta funcionalidad permitiendo a los usuarios comparar diferentes entidades, como orden de compra a recibido u orden de compra a documento, proporcionando una mayor flexibilidad en el manejo de escenarios más complejos. La Versión 4 asegura un control más estricto sobre los flujos de trabajo de adquisición y recepción, ofreciendo comparaciones y acciones más dinámicas basadas en el tipo de comparación elegido.
