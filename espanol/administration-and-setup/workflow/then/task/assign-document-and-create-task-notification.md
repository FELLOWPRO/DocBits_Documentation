# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo "**Assign Document and Create Task/Notification Based on Decision Table**" asigna un documento y crea una tarea o notificación con detalles configurables. El asignatario se determina por el resultado de una tabla de decisión, y la tarjeta permite establecer prioridades y enviar notificaciones por correo electrónico.

## **Componentes de la tarjeta**

1. **Assignee Type**
   * **Descripción:** Especifica si el resultado de la tabla de decisión asigna el documento y la tarea/notificación a un usuario o a un grupo.
   * **Detalle:** Un campo para configurar el tipo de asignatario como "User" o "Group" según el resultado de la tabla de decisión.
2. **Task/Notification**
   * **Descripción:** Especifica el tipo de acción que se creará para el asignatario.
   * **Detalle:** Un desplegable para seleccionar "Task" o "Notification" según las necesidades del flujo de trabajo.
3. **Title**
   * **Descripción:** El título de la tarea o notificación.
   * **Detalle:** Un campo para proporcionar un título conciso que identifique la tarea o notificación.
4. **Description**
   * **Descripción:** Detalles adicionales sobre la tarea o notificación.
   * **Detalle:** Un campo para describir el propósito y el contexto de la tarea o notificación.
5. **Priority**
   * **Descripción:** Define el nivel de urgencia de la tarea o notificación.
   * **Opciones:**
     * **High:** Requiere atención inmediata.
     * **Medium:** Importante pero no urgente.
     * **Low:** Puede abordarse más adelante.
6. **Assignee Type**
   * **Descripción:** Este campo determina el tipo de asignatario (User o Group) al que se asignan el documento y la tarea/notificación.
   * **Detalle:** Un menú desplegable para seleccionar si la tarea/notificación se asigna a un usuario o a un grupo según el resultado de la tabla de decisión.
7. **Send Mail**
   * **Descripción:** Configura si se envía una notificación por correo electrónico al asignatario.
   * **Opciones:**
     * **True:** Envía una notificación por correo electrónico.
     * **False:** No se envía ninguna notificación por correo electrónico.
8. **Value**
   * **Descripción:** Establece la prioridad numérica para la asignación del documento.
   * **Detalle:** Un campo para introducir un valor numérico, donde los números más bajos indican una mayor prioridad.

## **Funcionalidad**

* **Evaluación de la condición:**\
  La tarjeta ejecuta sus acciones solo si se cumplen las condiciones del flujo de trabajo.
* **Evaluación de la tabla de decisión:**\
  La tabla de decisión determina si el documento y la tarea/notificación se asignan a un usuario o a un grupo.
* **Asignación del documento y creación de tarea/notificación:**\
  El documento se asigna al resultado de la tabla de decisión. Se crea una tarea o notificación con el título, la descripción y el nivel de prioridad especificados.
* **Notificación por correo electrónico:**\
  Si "Send Mail" se establece en True, se envía una notificación por correo electrónico al asignatario.

## **Configuración**

1. **Definir el Assignee Type:**
   * Configure el campo Assignee Type como "User" o "Group" según el resultado de la tabla de decisión.
2. **Seleccionar Task/Notification:**
   * Elija "Task" o "Notification" en el desplegable Task/Notification.
3. **Establecer los detalles de la tarea/notificación:**
   * Introduzca el Title y la Description de la tarea o notificación.
   * Seleccione la Priority (High, Medium o Low) en el desplegable.
4. **Habilitar la notificación por correo electrónico:**
   * Establezca la opción Send Mail en True o False, según si debe enviarse una notificación por correo electrónico.
5. **Establecer la prioridad numérica:**
   * Introduzca un valor numérico en el campo Value para determinar la prioridad de la asignación, donde los números más bajos se procesan primero.
6. Guarde la configuración de la tarjeta y active el flujo de trabajo.

## **Conclusión**

La tarjeta de flujo de trabajo "Assign Document and Create Task/Notification Based on Decision Table" garantiza que las tareas o notificaciones se asignen dinámicamente al usuario o grupo adecuado según los resultados de la tabla de decisión. Esta tarjeta facilita una delegación de tareas eficiente, prioridades personalizables y notificaciones opcionales por correo electrónico para mejorar la capacidad de respuesta del flujo de trabajo.
