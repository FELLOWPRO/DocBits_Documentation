# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits comprueba si una tabla de decisión especificada tiene valores de retorno para un documento dado y determina si los datos devueltos deben utilizarse en los pasos posteriores del flujo de trabajo. Garantiza que los flujos de trabajo puedan adaptarse dinámicamente según los resultados de la tabla de decisión.

## **Funcionalidad:**

* **Validación de la tabla de decisión:** Esta tarjeta verifica si la tabla de decisión seleccionada proporciona valores de retorno para el documento que se está procesando.
* **Selección de la tabla de decisión:** Los usuarios especifican el nombre de la tabla de decisión que se comprobará.
* **Usar los datos de retorno:** Los usuarios pueden especificar si utilizar los datos de retorno en tarjetas posteriores con una configuración **Boolean**:
  * **True:** Los datos de retorno están disponibles y se utilizarán en los pasos posteriores del flujo de trabajo.
  * **False:** Los datos de retorno no se utilizarán y el flujo de trabajo continúa sin ellos.

## **Uso:**

Esta tarjeta es ideal para flujos de trabajo que implican lógica condicional o toma de decisiones basada en reglas predefinidas en una tabla de decisión. Garantiza una integración fluida de los resultados de la tabla de decisión en los procesos del flujo de trabajo.

## **Ejemplo de escenario:**

* Un usuario configura la tarjeta para comprobar la tabla de decisión **"Invoice Processing Rules"** en busca de valores de retorno. El **Boolean** se establece en **True**, lo que indica que los datos de retorno (p. ej., requisitos de aprobación) se utilizarán en tarjetas posteriores para guiar las decisiones del flujo de trabajo.

Al usar la tarjeta "Decision Table Check", las organizaciones pueden mejorar la flexibilidad del flujo de trabajo, agilizar el procesamiento basado en reglas y garantizar la coherencia en la toma de decisiones en los flujos de trabajo automatizados.
