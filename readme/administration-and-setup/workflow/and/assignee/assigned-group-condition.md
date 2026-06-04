# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Propósito:**

Esta tarjeta de flujo de trabajo ejecuta operaciones en función de si una tarea o documento está asignado a un grupo o conjunto de grupos en particular. Utiliza lógica condicional para disparar o impedir acciones específicas según la asignación de grupo, lo que la hace ideal para flujos de trabajo que requieren un tratamiento específico por grupo.

**Componentes de la tarjeta:**

1. **Operator**
   * **Descripción:** Define la condición lógica que se aplica a la asignación de grupo.
   * **Opciones:**
     * **IS:** Dispara la operación si el grupo asignado del documento o tarea coincide con uno de los grupos de la lista especificada.
     * **IS NOT:** Dispara la operación si el grupo asignado del documento o tarea no coincide con ninguno de los grupos de la lista especificada.
2. **Groups List**
   * **Descripción:** Una lista o selección de grupos con los que comparar el grupo asignado.
   * **Detalle:** Esta lista puede incluir uno o varios grupos, lo que permite a la tarjeta manejar de forma eficaz tanto condiciones de un solo grupo como de varios.

**Funcionalidad:**

* **Identificación de la asignación de grupo:** Identifica automáticamente el grupo o grupos asignados a una tarea o documento concreto dentro del sistema.
* **Evaluación de la condición:**
  * Con el operador **IS**, la tarjeta comprueba si el grupo asignado es uno de los grupos enumerados en la Groups List.
  * Con el operador **IS NOT**, la tarjeta garantiza que el grupo asignado no forme parte de los grupos enumerados.
* **Ejecución de la acción:**
  * **Condición verdadera:** Si la asignación de grupo cumple la condición (ya sea **IS** o **IS NOT**), se disparan las acciones pertinentes, como notificaciones, inicios de tareas, aprobaciones u otros pasos del flujo de trabajo.
  * **Condición falsa:** Si la condición no se cumple, el flujo de trabajo no continuará.

**Interacciones del usuario:**

* **Configuración:** Los usuarios configuran la tarjeta seleccionando un operador y especificando los grupos pertinentes de la Groups List. La configuración debe ser fácil de usar e intuitiva para acomodar selecciones de bases de grupos potencialmente grandes.
* **Supervisión e informes:**\
  El sistema debe ofrecer funcionalidad para supervisar e informar sobre las operaciones disparadas por esta tarjeta, proporcionando información sobre la precisión de las asignaciones y la eficiencia del proceso.
* **Gestión de errores y notificaciones:**\
  Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas sin asignar o errores en la selección de grupos.

**Conclusión:**\
La tarjeta de flujo de trabajo "Assigned Group Condition" es esencial para gestionar flujos de trabajo de documentos y tareas que dependen de las asignaciones de grupo. Al permitir condiciones basadas en si una tarea o documento está asignado a grupos específicos, garantiza que los flujos de trabajo solo se disparen por las interacciones de grupo adecuadas, mejorando la responsabilidad y la gestión de tareas entre equipos.
