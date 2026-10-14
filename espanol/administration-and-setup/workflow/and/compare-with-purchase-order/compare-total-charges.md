# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo compara los cargos totales de un campo de documento con los cargos correspondientes de una orden de compra. La tarjeta ayuda a garantizar que los cargos del documento se ajusten a los de la orden de compra, teniendo en cuenta los niveles de tolerancia especificados. La comparación puede disparar acciones si se encuentran discrepancias, como señalar discrepancias para su revisión o ajustar los cargos en consecuencia.

## **Componentes de la tarjeta:**

1. **Field Name:**
   * **Descripción**: Especifica el campo del documento que contiene los valores de cargo total que se compararán con los cargos de la orden de compra.
   * **Detalle**: El valor de este campo representa los cargos totales aplicados en el documento (p. ej., factura) y se comparará con el cargo de la orden de compra.
2. **Operator:**
   * **Descripción**: Define la condición que se aplicará a la comparación entre el cargo total del documento y el cargo de la orden de compra.
   * **Opciones**:
     * **Equals (=)**: Verifica si el cargo total del documento coincide con el cargo de la orden de compra.
     * **Not Equals (≠)**: Garantiza que el cargo total del documento sea distinto del cargo de la orden de compra.
     * **Greater Than (>)**: Verifica si el cargo total del documento es mayor que el cargo de la orden de compra.
     * **Greater or Equals (≥)**: Verifica si el cargo total del documento es mayor o igual que el cargo de la orden de compra.
     * **Lesser Than (<)**: Verifica si el cargo total del documento es menor que el cargo de la orden de compra.
     * **Lesser or Equals (≤)**: Verifica si el cargo total del documento es menor o igual que el cargo de la orden de compra.
3. **Tolerance Amount**
   * **Descripción**: Especifica el umbral de tolerancia para comparar los cargos totales.
   * **Detalle**: Este valor numérico representa la variación permitida en los cargos entre el documento y la orden de compra.
4. **Tolerance Type:**
   * **Descripción**: Especifica el tipo de tolerancia que se aplicará.
   * **Opciones**:
     * **Percentage**: La tolerancia se aplica como un porcentaje del cargo de la orden de compra.
     * **Value**: La tolerancia se aplica como un importe numérico fijo.
5. **Separator:**
   * **Descripción**: Especifica el separador utilizado para distinguir el Charge ID al final del nombre del campo.
   * **Detalle**: El separador separa el campo de cargo del Charge ID único que se utilizará para vincular el cargo del documento con el cargo correspondiente de la orden de compra.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema compara el cargo total del campo del documento con el cargo correspondiente de la orden de compra según el operador y la tolerancia. La tolerancia se aplica para determinar si la diferencia entre los dos cargos está dentro de un rango aceptable.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si los cargos coinciden (teniendo en cuenta la tolerancia) y la condición es verdadera, el flujo de trabajo continuará con la acción definida, como la aprobación del documento o un procesamiento adicional.
  * **Condición falsa**: Si la condición es falsa (es decir, los cargos no coinciden dentro de la tolerancia), el flujo de trabajo no continuará.

## **Configuración:**

* Los usuarios comienzan seleccionando el campo del documento que contiene el valor de cargo total. A continuación, seleccionan el operador para definir cómo se comparará el cargo con el cargo de la orden de compra. Después, los usuarios establecen el importe de tolerancia y el tipo de tolerancia (porcentaje o absoluto). Por último, especifican el separador y el Charge ID que se utilizarán para la comparación.

## **Ejemplo de escenario:**

Una factura indica un cargo de 500 $ en el campo "total charges". El cargo correspondiente de la orden de compra es de 480 $ y la tolerancia se establece en 20 $ (tolerancia absoluta). La tarjeta compara el cargo del documento con el cargo de la orden de compra:

* El cargo total del documento está dentro de la tolerancia de 20 $ de la orden de compra, y el flujo de trabajo continúa sin problemas.
* Si el cargo supera la tolerancia, el flujo de trabajo señala la discrepancia para su revisión.

## **Conclusión:**

La tarjeta de flujo de trabajo "Compare Total Charges" garantiza que los cargos de los documentos se ajusten a los de las órdenes de compra, teniendo en cuenta los niveles de tolerancia especificados. Esto ayuda a las organizaciones a automatizar el proceso de verificación, identificar discrepancias de forma temprana y mantener un mejor control sobre los procesos relacionados con los cargos.
