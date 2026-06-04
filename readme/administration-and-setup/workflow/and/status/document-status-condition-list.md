# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta está diseñada para controlar las acciones del flujo de trabajo según el estado actual de un documento, usando lógica condicional para disparar o restringir ciertos procesos. Garantiza que los documentos solo avancen por los flujos de trabajo cuando cumplen criterios de estado predefinidos.

**Componentes de la tarjeta**

1. **Operator**
   * **Descripción**: Determina cómo se evaluará el estado del documento frente a una condición especificada.
   * **Opciones**:
     * **is**: Dispara las acciones asociadas si el estado actual del documento coincide con uno de los estados especificados.
     * **is not**: Dispara las acciones si el estado del documento no coincide con ninguno de los estados especificados.
2. **Status ( List )**
   * **Descripción**: Enumera los estados específicos con los que se comparará el estado actual del documento.
   * **Ejemplos**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Estos representan diferentes etapas o condiciones en las que puede encontrarse un documento dentro de un proceso de flujo de trabajo.

**Funcionalidad**

* **Identificación del estado**: Identifica automáticamente el estado actual de un documento a medida que avanza por el flujo de trabajo del sistema ERP.
* **Evaluación de la condición**: Aplica el operador elegido (is o is not) al estado del documento en comparación con los estados enumerados:
  * Si es **is**, comprueba si el estado del documento coincide con algún estado de la lista.
  * Si es **is not**, comprueba si el estado del documento no aparece en la lista.
* **Ejecución de la acción**: Según el resultado de la evaluación de la condición:
  * **True**: Ejecuta acciones o flujos de trabajo predefinidos si se cumple la condición.
  * **False**: Omite o dispara flujos de trabajo alternativos si no se cumple la condición.
* **Integración con el flujo de trabajo**: Se integra sin problemas con otros componentes del flujo de trabajo, garantizando que el manejo de documentos esté coordinado en todo el sistema.

**Interacciones del usuario**

* **Configuración**: Los usuarios configuran la tarjeta seleccionando el operador y especificando los estados pertinentes. Esta configuración puede implicar sencillos menús desplegables o casillas de verificación para seleccionar estados y operadores.
* **Supervisión y gestión**: Los usuarios pueden hacer seguimiento de la actividad de la tarjeta a través de un panel, que proporciona información sobre las condiciones de estado que se supervisan y las acciones que se realizan según esas condiciones.
* **Gestión de errores y alertas**: Permite configurar alertas para fallos de procesos o desajustes en los estados de documento esperados, posibilitando respuestas rápidas a los problemas operativos.

#### Conclusión

La tarjeta de flujo de trabajo "Document Status Condition" es vital para garantizar que los documentos se procesen correctamente según su estado actual, mejorando el control y la eficiencia dentro del sistema ERP. Documentar claramente esta tarjeta en el manual del sistema ayudará a los usuarios a implementarla y gestionarla de forma eficaz, aprovechando su funcionalidad para mantener flujos de trabajo de documentos fluidos y conformes. Esta tarjeta es especialmente útil para gestionar los ciclos de vida de los documentos y garantizar que solo los documentos que cumplen criterios específicos avancen a las etapas posteriores de los procesos de negocio.
