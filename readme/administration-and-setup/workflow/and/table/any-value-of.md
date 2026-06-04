# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits se utiliza para validar si algún valor de una columna específica de una tabla coincide con un patrón regex proporcionado. Si una sola entrada de la columna coincide con el patrón, el flujo de trabajo continuará, lo que la hace ideal para casos de uso en los que identificar incluso una única coincidencia dispara los siguientes pasos del proceso.

## **Funcionalidad:**

* **Validación de patrón regex:** Esta tarjeta comprueba si algún valor de una columna dada de una tabla coincide con el patrón de expresión regular proporcionado. La tarjeta se disparará y permitirá que el flujo de trabajo continúe si al menos una entrada de la columna cumple la condición.
* **Operator:** Los usuarios definen la columna y especifican el patrón regex. La condición disponible incluye:
  * **Matches Regex Pattern:** Verifica que al menos un valor de la columna especificada coincida con el patrón regex.
* **Selección de tabla y columna:** Los usuarios especifican la tabla y la columna que desean comprobar para detectar coincidencias del patrón regex.

## **Uso:**

Esta tarjeta es especialmente útil para escenarios en los que una tabla contiene datos que pueden requerir coincidencias específicas, como validar direcciones de correo electrónico, números de factura o ID de producto. Garantiza que los flujos de trabajo continúen cuando alguna entrada pertinente coincida con el patrón definido, sin necesidad de comprobar todas las entradas.

## **Ejemplo de escenario:**

* Un usuario configura la tarjeta para buscar entradas en la columna "Email Address" de la tabla "Customers", usando un patrón regex para formatos de correo electrónico válidos. Si al menos una dirección de correo electrónico de la columna coincide con el patrón, la tarjeta dispara el siguiente paso del flujo de trabajo, garantizando que el sistema procese la entrada válida.

Al usar la tarjeta "Regex Pattern Matching", las organizaciones pueden automatizar flujos de trabajo basados en validaciones dinámicas basadas en patrones, agilizando los procesos y garantizando que solo las entradas pertinentes disparen acciones adicionales.
