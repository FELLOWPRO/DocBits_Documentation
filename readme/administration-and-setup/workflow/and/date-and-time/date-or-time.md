# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits comprueba si un valor de fecha/hora especificado está dentro de un rango definido. Permite que los flujos de trabajo continúen o se detengan según si la condición se cumple, lo que la hace adecuada para operaciones sensibles al tiempo o para la programación de flujos de trabajo.

## **Funcionalidad:**

* **Validación de fecha/hora:** Esta tarjeta evalúa si una fecha/hora determinada está dentro de un rango especificado usando las siguientes condiciones:
  * **Is:** Comprueba si la fecha/hora está dentro del rango de inicio y fin definido (ambos incluidos).
  * **Is Not:** Garantiza que la fecha/hora quede fuera del rango definido.

**Rango de fecha/hora:** Los usuarios especifican los valores de fecha/hora de inicio y fin para definir el rango de comparación.

## **Uso:**

Esta tarjeta es ideal para la programación, las comprobaciones de cumplimiento o la validación de condiciones basadas en el tiempo en los flujos de trabajo. Por ejemplo, se puede usar para garantizar que las tareas se ejecuten solo durante los plazos predefinidos o para verificar fechas límite.

## **Ejemplo de escenario:**

* Un usuario configura la tarjeta para comprobar si la **fecha de envío** de una factura **está entre** **"2024-11-01"** y **"2024-11-30"**. Si la fecha de envío está dentro de este rango, el flujo de trabajo continúa con el procesamiento del pago. Si no, el flujo de trabajo dispara una notificación para una revisión adicional.

Al usar la tarjeta "Date/Time Range Validation", las organizaciones pueden garantizar una programación precisa, mejorar el cumplimiento y agilizar los flujos de trabajo al ajustarse a las restricciones de tiempo predefinidas.
