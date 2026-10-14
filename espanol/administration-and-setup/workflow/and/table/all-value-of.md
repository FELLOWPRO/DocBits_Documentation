# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits se utiliza para validar si **todos los valores** de una columna específica de una tabla coinciden con un patrón regex proporcionado. Para que el flujo de trabajo continúe, todas las entradas de la columna deben cumplir la condición, lo que hace que esta tarjeta sea ideal para garantizar la coherencia y la integridad de los datos en todas las entradas.

## **Funcionalidad:**

* **Validación de patrón regex:** Esta tarjeta comprueba que **todos los valores** de una columna especificada de una tabla coincidan con el patrón de expresión regular proporcionado. El flujo de trabajo solo continuará si todas las entradas de la columna cumplen la condición.
* **Operator:** Los usuarios definen la columna y especifican el patrón regex. La condición disponible incluye:
  * **Matches Regex Pattern:** Verifica que todos los valores de la columna especificada coincidan con el patrón regex.
* **Selección de tabla y columna:** Los usuarios especifican la tabla y la columna que desean comprobar para detectar coincidencias completas del patrón regex.

## **Uso:**

Esta tarjeta es ideal para los casos en los que se requiere uniformidad de datos, como garantizar que todos los números de teléfono, los ID de producto u otras entradas de campo se ajusten a un formato específico. Garantiza que los flujos de trabajo solo continúen cuando todas las entradas pertinentes sean coherentes con el patrón.

## **Ejemplo de escenario:**

* Un usuario configura la tarjeta para comprobar la columna "Phone Number" de la tabla "Contacts", usando un patrón regex para validar los formatos de los números de teléfono. Si todas las entradas de números de teléfono de la columna coinciden con el patrón, la tarjeta dispara el siguiente paso del flujo de trabajo, confirmando un formato de datos uniforme.

Al usar la tarjeta "All Values Regex Pattern Matching", las organizaciones pueden aplicar estándares de datos estrictos y mejorar la precisión del flujo de trabajo, garantizando que todas las entradas de una columna especificada cumplan el formato requerido antes de continuar.
