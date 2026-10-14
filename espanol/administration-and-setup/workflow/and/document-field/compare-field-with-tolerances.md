# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para comparar el valor de un campo con un valor de referencia especificado, permitiendo tolerancias. Posibilita un procesamiento condicional preciso en flujos de trabajo donde se aceptan pequeñas desviaciones, lo que la hace ideal para escenarios como el control de calidad, el análisis financiero o las acciones basadas en umbrales.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción:** El campo que se evaluará en la comparación.
   * **Detalle:** Debe coincidir con el identificador exacto del primer campo dentro del documento.
2. **Comparison Operator**
   * **Descripción:** Especifica cómo se comparará el valor del campo seleccionado con el valor de referencia.
   * **Opciones:**
     * **Equals (=):** Verifica si el valor del campo coincide exactamente con el valor de referencia.
     * **Not Equals (≠):** Verifica si el valor del campo no coincide con el valor de referencia.
     * **Greater Than (>):** Comprueba si el valor del campo es mayor que el valor de referencia.
     * **Greater or Equals (≥):** Comprueba si el valor del campo es mayor o igual que el valor de referencia.
     * **Lesser Than (<):** Comprueba si el valor del campo es menor que el valor de referencia.
     * **Lesser or Equals (≤):** Comprueba si el valor del campo es menor o igual que el valor de referencia.
3. **Reference Value**
   * **Descripción:** El valor con el que se compara el campo.
   * **Detalle:** Este valor puede ser numérico, de texto o de fecha, según el contexto de la comparación.
4. **Tolerance Amount**
   * **Descripción:** Define el margen de error aceptable para la comparación.
   * **Detalle:** El importe de tolerancia es un valor numérico que indica la diferencia máxima admisible entre los dos valores de campo para que la comparación se considere verdadera.
5. **Tolerance Type**
   * **Descripción:** Especifica la unidad de medida del importe de tolerancia.
   * **Opciones:**
     * **Value:** La tolerancia es un valor absoluto, lo que significa que los dos campos pueden diferir en el importe de tolerancia especificado.
     * **Percent:** La tolerancia se calcula como un porcentaje del valor del segundo campo, permitiendo un margen de error relativo.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema evalúa el valor del campo frente al valor de referencia usando el operador de comparación seleccionado. Si se configura una tolerancia, el sistema considera la comparación correcta si el valor del campo está dentro del rango de tolerancia definido.
* **Ejecución de la acción:**
  * **Dentro de la tolerancia:** Si el valor del campo cumple la condición dentro de la tolerancia especificada, el flujo de trabajo continúa, disparando las acciones asociadas.
  * **Fuera de la tolerancia:** Si el valor del campo no cumple la condición o queda fuera del rango de tolerancia, pueden ejecutarse acciones alternativas, como registro, envío de alertas o detención del flujo de trabajo.

## **Configuración:**

* Los usuarios configuran la tarjeta seleccionando el campo que se evaluará de una lista de campos disponibles y eligiendo el operador de comparación (p. ej., igual, mayor que) de una lista desplegable. A continuación, especifican el valor de referencia con el que comparar y definen el importe de tolerancia, y luego seleccionan el tipo de tolerancia (p. ej., porcentaje o valor).&#x20;

## **Conclusión:**

La tarjeta "Field Comparison with Tolerances" es una herramienta versátil para los flujos de trabajo que requieren evaluaciones flexibles. Al permitir comparaciones con tolerancias, garantiza que los flujos de trabajo sigan siendo eficientes y adaptables, acomodando las variaciones del mundo real sin comprometer la precisión.
