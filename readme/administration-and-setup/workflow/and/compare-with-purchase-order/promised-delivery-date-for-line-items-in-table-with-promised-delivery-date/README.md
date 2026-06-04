# Promised delivery date for line items in table with promised delivery date

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Propósito:

Esta tarjeta de flujo de trabajo está diseñada para validar la **fecha de entrega prometida de las líneas** frente a la **fecha de entrega prometida de la orden de compra**, usando operadores de comparación y reglas de tolerancia configurables. Permite a los flujos de trabajo detectar automáticamente fechas de entrega conformes, tempranas o tardías y reaccionar en consecuencia.

## Componentes de la tarjeta:

1. **Operator**
   * **Descripción:**\
     Define cómo se compara la fecha de entrega prometida de la línea con la fecha de entrega prometida de la orden de compra.
   * **Opciones:**
     * **Equals (=):** La fecha de la línea debe quedar dentro de la ventana de tolerancia.
     * **Not Equals (≠):** La fecha de la línea debe quedar fuera de la ventana de tolerancia.
     * **Greater Than (>):** La fecha de la línea debe ser posterior a la ventana de tolerancia.
     * **Greater or Equals (≥):** La fecha de la línea debe ser igual o posterior al inicio de la ventana de tolerancia.
     * **Lesser Than (<):** La fecha de la línea debe ser anterior a la ventana de tolerancia.
     * **Lesser or Equals (≤):** La fecha de la línea debe ser igual o anterior al final de la ventana de tolerancia.<br>
2. **Tolerance Days**
   * **Descripción:**\
     Especifica el número de días utilizados para calcular la ventana de tolerancia aceptable en torno a la fecha de entrega prometida de la orden de compra.
   * **Detalle:**\
     Este valor es un número entero y define cuántos días antes y después de la fecha de la orden de compra se consideran durante la validación.<br>
3. **Allowed Tolerance Days**
   * **Descripción:**\
     Define qué días de la semana se cuentan al calcular los días de tolerancia.
   * **Detalle:**\
     Los usuarios pueden seleccionar días de la semana específicos (por ejemplo, de lunes a viernes). Solo los días seleccionados se incluyen al calcular la ventana de tolerancia.

### Funcionalidad:

* **Evaluación de la condición:** El sistema calcula una ventana de tolerancia en torno a la fecha de entrega prometida de la orden de compra según los **Tolerance Days** y los **Allowed Tolerance Days** configurados.\
  A continuación, la fecha de entrega prometida de cada línea se compara con esta ventana usando el operador seleccionado.
* Ejecución de la acción:
  * **Condición verdadera:** Si la diferencia de fecha de entrega está dentro del rango de tolerancia y cumple la condición establecida por el operador, el flujo de trabajo continúa.
  * **Condición falsa:** Si la condición no se cumple, el flujo de trabajo no continuará.

### Configuración:

* Seleccione el operador de comparación adecuado.
* Introduzca el número de días de tolerancia.
* Elija qué días de la semana deben contarse como días de tolerancia.

### Conclusión:

La tarjeta de flujo de trabajo **Compare with Purchase Order – Promised Delivery Date for Line Items** proporciona una forma flexible de aplicar reglas de fechas de entrega. Al combinar operadores con un tratamiento de la tolerancia que tiene en cuenta los días de la semana, permite una validación precisa de los compromisos de entrega a la vez que reduce las comprobaciones manuales y las excepciones.
