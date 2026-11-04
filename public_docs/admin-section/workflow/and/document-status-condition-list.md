# Lista de Condiciones de Estado del Documento

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta está diseñada para controlar las acciones del flujo de trabajo basadas en el estado actual de un documento, utilizando lógica condicional para activar o restringir ciertos procesos. Asegura que los documentos solo avancen a través de los flujos de trabajo cuando cumplan con criterios de estado predefinidos.

**Componentes de la Tarjeta**

1. **Operador**
* **Descripción**: Determina cómo se evaluará el estado del documento frente a una condición especificada.
* **Opciones**:
* **es**: Activa las acciones asociadas si el estado actual del documento coincide con uno de los estados especificados.
* **no es**: Activa las acciones si el estado del documento no coincide con ninguno de los estados especificados.
2. **Estado ( Lista )**&#x20;
* **Descripción**: Enumera los estados específicos con los que se comparará el estado actual del documento.
* **Ejemplos**: "Error", "Error de Exportación", "Listo en Validación", "Listo en Revisión", "Aprobación Pendiente", "Segunda Aprobación Pendiente". Estos representan diferentes etapas o condiciones en las que un documento podría encontrarse dentro de un proceso de flujo de trabajo.

**Funcionalidad**

* **Identificación de Estado**: Identifica automáticamente el estado actual de un documento a medida que avanza a través del flujo de trabajo del sistema ERP.
* **Evaluación de Condiciones**: Aplica el operador elegido (es o no es) al estado del documento en comparación con los estados enumerados:
* Si **es**, verifica si el estado del documento coincide con algún estado de la lista.
* Si **no es**, verifica si el estado del documento no aparece en la lista.
* **Ejecución de Acciones**: Dependiendo del resultado de la evaluación de la condición:
* **Verdadero**: Ejecuta acciones o flujos de trabajo predefinidos si se cumple la condición.
* **Falso**: Omite o activa flujos de trabajo alternativos si no se cumple la condición.
* **Integración de Flujos de Trabajo**: Se integra perfectamente con otros componentes de flujo de trabajo, asegurando que el manejo de documentos esté coordinado en todo el sistema.

**Interacciones del Usuario**

* **Configuración y Ajustes**: Los usuarios configuran la tarjeta seleccionando el operador y especificando los estados relevantes. Esta configuración puede implicar menús desplegables simples o casillas de verificación para seleccionar estados y operadores.
* **Monitoreo y Gestión**: Los usuarios pueden seguir la actividad de la tarjeta a través de un panel, que proporciona información sobre las condiciones de estado que se están monitoreando y las acciones que se están tomando en función de esas condiciones.
* **Manejo de Errores y Alertas**: Admite la configuración de alertas para fallos en el proceso o discrepancias en los estados esperados de los documentos, lo que permite respuestas rápidas a problemas operativos.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Estado del Documento" es vital para garantizar que los documentos se procesen correctamente según su estado actual, mejorando el control y la eficiencia dentro del sistema ERP. Documentar claramente esta tarjeta en el manual del sistema ayudará a los usuarios a implementar y gestionarla de manera efectiva, aprovechando su funcionalidad para mantener flujos de trabajo de documentos fluidos y conformes. Esta tarjeta es particularmente útil para gestionar los ciclos de vida de los documentos y garantizar que solo los documentos que cumplen con criterios específicos avancen a etapas posteriores de los procesos comerciales.
