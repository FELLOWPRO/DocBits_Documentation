<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Propósito:**

Esta tarjeta de flujo de trabajo ejecuta operaciones basándose en si una tarea o documento está asignado a un grupo particular o conjunto de grupos. Utiliza lógica condicional para activar o prevenir acciones específicas dependiendo de la asignación del grupo, lo que la hace ideal para flujos de trabajo que requieren un manejo específico por grupo.

**Componentes de la Tarjeta:**

1. **Operador**
   * **Descripción:** Define la condición lógica a aplicar a la asignación del grupo.
   * **Opciones:**
     * **ES (IS):** Activa la operación si el grupo asignado del documento o tarea coincide con uno de los grupos en la lista especificada.
     * **NO ES (IS NOT):** Activa la operación si el grupo asignado del documento o tarea no coincide con ninguno de los grupos en la lista especificada.
2. **Lista de Grupos**
   * **Descripción:** Una lista o selección de grupos para comparar con el grupo asignado.
   * **Detalle:** Esta lista puede incluir uno o múltiples grupos, permitiendo que la tarjeta maneje condiciones de grupo tanto singulares como múltiples de manera efectiva.

**Funcionalidad:**

* **Identificación de la Asignación de Grupo:** Identifica automáticamente el grupo o grupos asignados a una tarea o documento particular dentro del sistema.
* **Evaluación de la Condición:**
  * Utilizando el operador **ES**, la tarjeta verifica si el grupo asignado es uno de los grupos enumerados en la Lista de Grupos.
  * Utilizando el operador **NO ES**, la tarjeta asegura que el grupo asignado no sea parte de los grupos enumerados.
* **Ejecución de la Acción:**
  * **Condición Verdadera:** Si la asignación del grupo cumple con la condición (ya sea **ES** o **NO ES**), se activan las acciones pertinentes, como notificaciones, iniciación de tareas, aprobaciones u otros pasos del flujo de trabajo.
  * **Condición Falsa:** Si no se cumple la condición, el flujo de trabajo no continuará.

**Interacciones del Usuario:**

* **Configuración:** Los usuarios configuran la tarjeta seleccionando un operador y especificando los grupos pertinentes de la Lista de Grupos. La configuración debe ser fácil de usar e intuitiva para acomodar selecciones de bases de grupos potencialmente grandes.
* **Monitoreo e Informes:**
  El sistema debe proporcionar funcionalidad para monitorear e informar sobre las operaciones activadas por esta tarjeta, ofreciendo información sobre la precisión de la asignación y la eficiencia del proceso.
* **Manejo de Errores y Notificaciones:**
  Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas no asignadas o errores en la selección de grupos.

**Conclusión:**
La tarjeta de flujo de trabajo "Condición de Grupo Asignado" es esencial para gestionar flujos de trabajo de documentos y tareas que dependen de las asignaciones de grupos. Al permitir condiciones basadas en si una tarea o documento está asignado a grupos específicos, asegura que los flujos de trabajo solo se activen por las interacciones de grupo apropiadas, mejorando la responsabilidad y la gestión de tareas entre los equipos.
