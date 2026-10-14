# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para automatizar acciones según el estado (marcado o sin marcar) de una casilla de verificación dentro de su sistema ERP. Al evaluar la condición de la casilla de verificación, facilita el disparo de procesos específicos o la aplicación de ciertas reglas dentro de la aplicación.

## **Componentes de la tarjeta:**

* **Field Name**
  * **Descripción:** Especifica el nombre del campo de casilla de verificación que se evaluará.
  * **Detalle:** Debe coincidir con el identificador exacto del campo utilizado en el sistema. Determina qué casilla de verificación se está supervisando.
* **Boolean**
  * **Descripción:** Define la condición que dispara el flujo de trabajo.
  * **Opciones:**
    * **True:** El flujo de trabajo se dispara si la casilla de verificación está marcada.
    * **False:** El flujo de trabajo se dispara si la casilla de verificación está sin marcar.

#### **Funcionalidad:**

* **Detección de estado:** La tarjeta supervisa continuamente el estado del campo de casilla de verificación especificado.
* **Evaluación de la condición:** El sistema comprueba si la casilla de verificación está en el estado (marcado o sin marcar) especificado por la condición Boolean.
* **Ejecución de la acción:**
  * **Condición verdadera:**\
    Si el estado de la casilla de verificación coincide con la condición Boolean especificada (true para marcado o false para sin marcar), el sistema inicia las acciones asociadas. Estas podrían incluir habilitar o deshabilitar campos de formulario, disparar notificaciones, iniciar flujos de trabajo o actualizar registros.
  * **Condición falsa:**\
    Si el estado de la casilla de verificación no coincide con la condición, pueden tomarse acciones alternativas o ninguna acción, según la configuración del flujo de trabajo.

## **Configuración:**

* Los usuarios configuran la tarjeta seleccionando el campo de casilla de verificación de una lista de campos disponibles y estableciendo la condición Boolean.&#x20;

## Conclusión:

La tarjeta de flujo de trabajo "Checkbox Field Condition" es una herramienta fundamental para gestionar formularios y documentos dinámicos dentro de un sistema ERP, donde las entradas del usuario pueden determinar los procesos de datos posteriores. Al automatizar acciones según el estado de una casilla de verificación, esta tarjeta mejora la eficiencia del flujo de trabajo y garantiza que los comportamientos del sistema se ajusten a las entradas del usuario. Una documentación clara de esta tarjeta ayudará a los usuarios a implementarla de forma eficaz en sus operaciones, permitiendo un mejor control sobre los comportamientos de los formularios y las automatizaciones de procesos.



**Nota: No todos los clientes tienen la casilla de verificación, pero se puede añadir si se desea.**
