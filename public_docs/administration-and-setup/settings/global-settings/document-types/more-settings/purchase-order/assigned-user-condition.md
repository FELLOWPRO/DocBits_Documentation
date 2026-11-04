<figure><img src="../../../../.gitbook/assets/docbits_assigned_user_cond.png" alt="DocBits Assigned Usuario Cond" width="552"><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo gestiona la ejecución de operaciones basándose en si una tarea o documento está asignado a un usuario particular o conjunto de usuarios. Emplea lógica condicional para activar o prevenir acciones específicas, lo que la hace ideal para flujos de trabajo que requieren un manejo específico por usuario.

**Componentes de la Tarjeta**

1. **Operador**
   * **Descripción**: Define la condición lógica a aplicar a la asignación del usuario.
   * **Opciones**:
     * **ES (IS)**: Activa la operación si el usuario asignado del documento o tarea coincide con cualquier usuario en la lista especificada.
     * **NO ES (IS NOT)**: Activa la operación si el usuario asignado del documento o tarea no coincide con ningún usuario en la lista especificada.
2. **Lista de Usuarios**
   * **Descripción**: Una lista o selección de usuarios para comparar con el usuario asignado.
   * **Detalle**: Esta lista puede incluir uno o múltiples usuarios, permitiendo que la tarjeta maneje condiciones de usuario tanto singulares como múltiples de manera efectiva. La selección se puede realizar a través de casillas de verificación, un menú desplegable de selección múltiple o elementos de interfaz de usuario similares.

**Funcionalidad**

* **Identificación de la Asignación de Usuario**: Identifica automáticamente al usuario o usuarios asignados a una tarea o documento particular dentro del sistema ERP.
* **Evaluación de la Condición**:
  * Utilizando el operador **ES**, la tarjeta verifica si el usuario asignado se encuentra entre los enumerados en la Lista de Usuarios.
  * Utilizando el operador **NO ES**, la tarjeta asegura que el usuario asignado no esté entre los enumerados.
* **Ejecución de la Acción**:
  * **Condición Verdadera**: Si la asignación del usuario cumple con la condición (ya sea ES o NO ES), se activan las acciones pertinentes, como notificaciones, iniciación de tareas, aprobaciones u otros pasos del flujo de trabajo.
  * **Condición Falsa**: Si no se cumple la condición, el flujo de trabajo no continuará.

**Interacciones del Usuario**

* **Configuración**: Los usuarios configuran la tarjeta seleccionando un operador y especificando los usuarios pertinentes de la Lista de Usuarios. La configuración debe ser fácil de usar e intuitiva para acomodar selecciones de bases de usuarios potencialmente grandes.
* **Monitoreo e Informes**: El sistema ERP debe proporcionar funcionalidad para monitorear e informar sobre las operaciones activadas por esta tarjeta, ofreciendo información sobre la precisión de la asignación y la eficiencia del proceso.
* **Manejo de Errores y Notificaciones**: Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas no asignadas o errores en la selección de usuarios.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Usuario Asignado" es una herramienta crítica para gestionar flujos de trabajo de documentos y tareas que dependen de las asignaciones de usuarios. Al permitir condiciones basadas en si una tarea o documento está asignado a usuarios específicos, asegura que los flujos de trabajo solo se activen por las interacciones de usuario apropiadas, mejorando tanto la responsabilidad como la alineación de tareas dentro de los equipos. Documentar claramente esta tarjeta ayudará a los usuarios a entender su importancia e integrarla de manera efectiva en sus flujos de trabajo, asegurando operaciones fluidas y eficientes adaptadas a los roles y responsabilidades de los usuarios.
