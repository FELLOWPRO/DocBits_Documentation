# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para evaluar si el valor de impuesto de un campo de documento coincide con el valor de impuesto de una orden de compra, teniendo en cuenta las tolerancias basadas en el charge ID. La tarjeta compara estos dos valores de impuesto (uno del campo del documento y otro de la orden de compra) y comprueba si cumplen una condición especificada (p. ej., igual, mayor que, menor que, etc.). Esto ayuda a garantizar que los valores de impuesto sean coherentes y a señalar discrepancias para su revisión o aprobación adicional en los flujos de trabajo de compras.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción**: Especifica el campo del documento que contiene el valor de impuesto que se comparará con el valor de impuesto de la orden de compra.
   * **Detalle**: Este campo debe coincidir con el identificador exacto del valor de impuesto del documento.
2. **Operator**
   * **Descripción**: Define la condición que se aplicará a la comparación entre el valor de impuesto del documento y el valor de impuesto de la orden de compra.
   * **Opciones**:
     * **Equals (=)**: Comprueba si el impuesto del campo del documento coincide con el impuesto de la orden de compra.
     * **Not Equals (≠)**: Garantiza que el impuesto del campo del documento no coincida con el impuesto de la orden de compra.
     * **Greater Than (>)**: Verifica si el impuesto del campo del documento es mayor que el impuesto de la orden de compra.
     * **Greater or Equals (≥)**: Comprueba si el impuesto del campo del documento es mayor o igual que el impuesto de la orden de compra.
     * **Lesser Than (<)**: Verifica si el impuesto del campo del documento es menor que el impuesto de la orden de compra.
     * **Lesser or Equals (≤)**: Comprueba si el impuesto del campo del documento es menor o igual que el impuesto de la orden de compra.
3. **Master Data Table**
   * **Descripción**: La tabla que contiene los detalles de la orden de compra, incluidos el charge ID y los valores de impuesto.
   * **Detalle**: Esta tabla debe tener una referencia al charge ID asociado al valor de impuesto de la orden de compra.
4. **Tolerance Amount**
   * **Descripción**: El importe umbral dentro del cual pueden variar los valores de impuesto. Se utiliza para tener en cuenta pequeñas discrepancias en los cálculos de impuestos.
   * **Detalle**: El importe de tolerancia debe ser un valor numérico que defina la diferencia máxima permitida entre los valores de impuesto.
5. **Tolerance Type**
   * **Descripción**: Especifica el tipo de tolerancia que se aplica, ya sea absoluta o basada en porcentaje.
   * **Opciones**:
     * **Value**: La tolerancia es un valor numérico fijo.
     * **Percentage**: La tolerancia se calcula como un porcentaje del valor de impuesto.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema evalúa si el valor de impuesto del campo del documento cumple la condición especificada al compararlo con el valor de impuesto de la orden de compra (con la referencia del charge ID de la tabla de datos maestros). El importe y el tipo de tolerancia se tienen en cuenta en esta evaluación para permitir pequeñas diferencias en los cálculos de impuestos.
* **Ejecución de la acción:**
  * **Condición verdadera**: Si el impuesto del campo del documento cumple la condición al compararlo con el impuesto de la orden de compra (dentro del importe y el tipo de tolerancia), el flujo de trabajo continúa.
  * **Condición falsa**: Si el impuesto del campo del documento no cumple la condición (ya sea que no esté dentro del rango de tolerancia o que la comparación falle), el flujo de trabajo se detendrá.

## **Configuración:**

* Los usuarios deben seleccionar el campo del documento que contiene el valor de impuesto que se comparará. A continuación, eligen el operador para definir cómo debe realizarse la comparación (p. ej., igual, mayor que). Después, los usuarios deben especificar la referencia de la tabla de datos maestros y establecer el importe y el tipo de tolerancia para tener en cuenta pequeñas discrepancias de impuestos.

## **Ejemplo de escenario:**

* Una factura indica un importe de impuesto de 100 $. La orden de compra correspondiente, que se encuentra en la tabla de datos maestros, especifica un valor de impuesto de 95 $. Usando el operador "Greater Than", el sistema compara el valor de impuesto del documento (100 $) con el valor de impuesto de la orden de compra (95 $) con una tolerancia de 10 $ (tipo de tolerancia absoluta). Dado que la diferencia de 5 $ está dentro del rango de tolerancia, el flujo de trabajo continúa sin disparar ninguna alerta.

## **Conclusión:**

La tarjeta de flujo de trabajo "Tax in Document Field Comparison" garantiza que los valores de impuesto de los documentos se ajusten a los detalles de la orden de compra, permitiendo pequeñas discrepancias según las tolerancias especificadas. Al automatizar esta comprobación, las organizaciones pueden minimizar los errores en los cálculos de impuestos y agilizar los procesos de compras, reduciendo la necesidad de intervención o aprobaciones manuales.
