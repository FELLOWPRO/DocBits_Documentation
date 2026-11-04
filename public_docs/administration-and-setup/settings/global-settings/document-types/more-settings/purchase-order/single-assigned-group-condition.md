<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Propósito:**
Esta tarjeta de flujo de trabajo ejecuta operaciones basándose en si una tarea o documento está asignado a un grupo particular. Utiliza una condición directa para activar o prevenir acciones basadas en la asignación del grupo.

**Componentes de la Tarjeta:**

1. **Operador**
   * **Descripción:** Define la condición lógica a aplicar a la asignación del grupo.
   * **Opciones:**
     * **ES (IS):** Activa la operación si el grupo asignado del documento o tarea coincide con el grupo especificado.
     * **NO ES (IS NOT):** Activa la operación si el grupo asignado del documento o tarea no coincide con el grupo especificado.
2. **Grupo**
   * **Descripción:** Especifica el grupo para comparar con el grupo asignado.
   * **Detalle:** Este campo le permite seleccionar un solo grupo para comparar la asignación.

**Funcionalidad:**

* **Identificación de la Asignación de Grupo:** Identifica automáticamente el grupo asignado a una tarea o documento particular.
* **Evaluación de la Condición:**
  * Utilizando el operador **ES**, la tarjeta verifica si el grupo asignado coincide con el grupo especificado.
  * Utilizando el operador **NO ES**, la tarjeta asegura que el grupo asignado no coincida con el grupo especificado.
* **Ejecución de la Acción:**
  * **Condición Verdadera:** Si la asignación del grupo cumple con la condición (ya sea **ES** o **NO ES**), se activan las acciones pertinentes, como notificaciones, iniciación de tareas, aprobaciones u otros pasos del flujo de trabajo.
  * **Condición Falsa:** Si no se cumple la condición, el documento o tarea puede pasar por un enrutamiento diferente, o se pueden especificar acciones alternativas.

**Interacciones del Usuario:**

* **Configuración:** Los usuarios configuran la tarjeta seleccionando un operador y especificando el grupo pertinente. La configuración debe ser sencilla e intuitiva.
* **Monitoreo e Informes:** El sistema debe proporcionar funcionalidad para monitorear e informar sobre las operaciones activadas por esta tarjeta, ofreciendo información sobre la precisión de la asignación y la eficiencia del proceso.
* **Manejo de Errores y Notificaciones:** Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas no asignadas o errores en la selección de grupos.

**Conclusión:**
La tarjeta de flujo de trabajo "Condición de Grupo Asignado" es esencial para gestionar flujos de trabajo de documentos y tareas basados en las asignaciones de grupos. Al permitir condiciones basadas en si una tarea o documento está asignado a un grupo específico, asegura que los flujos de trabajo solo se activen por las interacciones de grupo apropiadas, mejorando la gestión de tareas y la eficiencia del flujo de trabajo.
