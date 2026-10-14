# Module active

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits comprueba si un módulo específico del sistema está activo o inactivo. Permite que los flujos de trabajo continúen según el estado de activación de un módulo, garantizando que las acciones solo se realicen si el módulo necesario está disponible.

## **Funcionalidad:**

* **Validación del estado del módulo:** Esta tarjeta verifica el estado de activación de un módulo especificado y lo evalúa frente a una condición definida por el usuario.
* **Selección del módulo:** Los usuarios especifican el nombre del módulo que se comprobará, garantizando una validación precisa.
* **Operators:** Se pueden aplicar las siguientes condiciones:
  * **Is:** El flujo de trabajo continúa si el módulo seleccionado está activo.
  * **Is Not:** El flujo de trabajo continúa si el módulo seleccionado está inactivo.

## **Uso:**

Esta tarjeta es especialmente útil para los administradores o gestores del sistema que necesitan crear flujos de trabajo dependientes de la disponibilidad o la funcionalidad de módulos específicos. Ayuda a garantizar que los flujos de trabajo solo se ejecuten cuando todos los módulos necesarios estén configurados adecuadamente.

## **Ejemplo de escenario**

* Un usuario configura la tarjeta para comprobar si el módulo **"Document Processing"** **está activo.** Si el módulo está activo, el flujo de trabajo continúa, disparando tareas automatizadas de procesamiento de documentos. Si el módulo está inactivo, el flujo de trabajo se detiene, evitando acciones innecesarias.

Al usar la tarjeta "Module Active Check", las organizaciones pueden mejorar la fiabilidad del flujo de trabajo, evitar errores debidos a módulos inactivos y garantizar que los procesos se ajusten a la configuración del sistema.
