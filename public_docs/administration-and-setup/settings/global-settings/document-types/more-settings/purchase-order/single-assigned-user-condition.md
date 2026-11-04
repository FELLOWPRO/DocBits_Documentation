<figure><img src="../../../../.gitbook/assets/docbits_single_assigned_user.png" alt="DocBits Single Assigned Usuario" width="552"><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo facilita las operaciones basándose en la asignación de una tarea o documento a un usuario único y específico. Utilizando un enfoque de lógica condicional directa, gestiona flujos de trabajo que requieren la participación de un usuario objetivo, asegurando la precisión en el manejo de tareas basado en el usuario.

**Componentes de la Tarjeta**

1. **Operador**
   * **Descripción**: Especifica la lógica a aplicar a la asignación del usuario.
   * **Opciones**:
     * **ES (IS)**: Activa la operación si el usuario asignado del documento o tarea coincide con el usuario especificado.
     * **NO ES (IS NOT)**: Activa la operación si el usuario asignado no coincide con el usuario especificado.
2. **Usuario**
   * **Descripción**: Permite la selección de un solo usuario contra el cual se comparará el usuario asignado.
   * **Detalle**: Esto implica un menú desplegable simple o un campo de autocompletado donde se puede seleccionar un usuario a la vez.

**Funcionalidad**

* **Identificación de la Asignación de Usuario**: Identifica al usuario actualmente asignado a una tarea o documento específico.
* **Evaluación de la Condición**:
  * Para el operador **ES**, la tarjeta verifica si el usuario asignado es el mismo que el usuario seleccionado.
  * Para el operador **NO ES**, verifica que el usuario asignado sea diferente del usuario seleccionado.
* **Ejecución de la Acción**:
  * **Condición Verdadera**: Si la asignación cumple con la condición establecida (ES o NO ES), activa acciones predefinidas, que podrían incluir avanzar con aprobaciones, iniciar tareas posteriores, enviar notificaciones u otros flujos de trabajo relacionados.
  * **Condición Falsa**: Si no se cumple la condición, el flujo de trabajo no continuará.

**Interacciones del Usuario**

* **Configuración**: Los usuarios configuran la tarjeta eligiendo un operador y seleccionando un usuario del campo de usuario. Esta configuración debe ser sencilla, asegurando una fácil selección y configuración del usuario.
* **Monitoreo e Informes**: Ofrece herramientas para monitorear el rendimiento de la tarjeta, como el seguimiento de qué tareas se activan por asignaciones de usuarios específicos y los resultados de estos disparadores.
* **Manejo de Errores y Notificaciones**: Proporciona mecanismos para alertar a los usuarios si las tareas están asignadas incorrectamente o si ocurren errores operativos debido a problemas de asignación.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Usuario Asignado Único" es esencial para la gestión precisa de documentos y tareas específicos de cada usuario dentro de un sistema ERP. Simplifica los flujos de trabajo al centrarse en las asignaciones de usuarios individuales, asegurando así que las acciones solo se ejecuten cuando sea apropiado, basándose en el rol y las responsabilidades del usuario. Documentar claramente esta tarjeta ayudará a los usuarios a comprender su aplicación, permitiéndoles implementarla y gestionarla de manera efectiva dentro de sus operaciones diarias. Esta documentación asegura que todos los usuarios potenciales puedan captar fácilmente el propósito de la tarjeta e integrarla sin problemas en sus flujos de trabajo.
