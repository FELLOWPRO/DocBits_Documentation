# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo gestiona la ejecución de operaciones en función de si una tarea o documento está asignado a un usuario o conjunto de usuarios en particular. Emplea lógica condicional para disparar o impedir acciones específicas, lo que la hace ideal para flujos de trabajo que requieren un tratamiento específico por usuario.

**Componentes de la tarjeta**

1. **Operator**
   * **Descripción**: Define la condición lógica que se aplica a la asignación de usuario.
   * **Opciones**:
     * **IS**: Dispara la operación si el usuario asignado del documento o tarea coincide con algún usuario de la lista especificada.
     * **IS NOT**: Dispara la operación si el usuario asignado del documento o tarea no coincide con ningún usuario de la lista especificada.
2. **User List**
   * **Descripción**: Una lista o selección de usuarios con los que comparar el usuario asignado.
   * **Detalle**: Esta lista puede incluir uno o varios usuarios, lo que permite a la tarjeta manejar de forma eficaz tanto condiciones de un solo usuario como de varios. La selección puede realizarse mediante casillas de verificación, un desplegable de selección múltiple o elementos de interfaz similares.

**Funcionalidad**

* **Identificación de la asignación de usuario**: Identifica automáticamente el usuario o usuarios asignados a una tarea o documento concreto dentro del sistema ERP.
* **Evaluación de la condición**:
  * Con el operador **IS**, la tarjeta comprueba si el usuario asignado está entre los enumerados en la User List.
  * Con el operador **IS NOT**, la tarjeta garantiza que el usuario asignado no esté entre los enumerados.
* **Ejecución de la acción**:
  * **Condición verdadera**: Si la asignación de usuario cumple la condición (ya sea IS o IS NOT), se disparan las acciones pertinentes, como notificaciones, inicios de tareas, aprobaciones u otros pasos del flujo de trabajo.
  * **Condición falsa**: Si la condición no se cumple, el flujo de trabajo no continuará.

**Interacciones del usuario**

* **Configuración**: Los usuarios configuran la tarjeta seleccionando un operador y especificando los usuarios pertinentes de la User List. La configuración debe ser fácil de usar e intuitiva para acomodar selecciones de bases de usuarios potencialmente grandes.
* **Supervisión e informes**: El sistema ERP debe ofrecer funcionalidad para supervisar e informar sobre las operaciones disparadas por esta tarjeta, proporcionando información sobre la precisión de las asignaciones y la eficiencia del proceso.
* **Gestión de errores y notificaciones**: Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas sin asignar o errores en la selección de usuarios.

#### Conclusión

La tarjeta de flujo de trabajo "Assigned User Condition" es una herramienta fundamental para gestionar flujos de trabajo de documentos y tareas que dependen de las asignaciones de usuario. Al permitir condiciones basadas en si una tarea o documento está asignado a usuarios específicos, garantiza que los flujos de trabajo solo se disparen por las interacciones de usuario adecuadas, mejorando tanto la responsabilidad como la alineación de las tareas dentro de los equipos. Documentar claramente esta tarjeta ayudará a los usuarios a comprender su importancia e integrarla de forma eficaz en sus flujos de trabajo, garantizando operaciones fluidas y eficientes adaptadas a los roles y responsabilidades de los usuarios.
