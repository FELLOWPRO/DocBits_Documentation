# Assign to Procurement Group and Create a Task/Notification

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo "**Assign Document to Procurement Group and Create Task/Notification**" asigna un documento a un grupo de compras especificado, crea una tarea o notificación con detalles definidos y, opcionalmente, notifica al grupo por correo electrónico. Prioriza la ejecución de tareas según un valor de prioridad numérico configurable.

## **Componentes de la tarjeta**

1. **Group Name**
   * **Descripción:** Especifica el grupo de compras responsable de gestionar el documento.
   * **Detalle:** Un campo donde el usuario puede introducir manualmente el nombre del grupo de compras.
2. **Task/Notification**
   * **Descripción:** Define si se crea una tarea o una notificación para el grupo.
   * **Detalle:** Un campo donde el usuario puede elegir entre crear una tarea o una notificación.
3. **Title**
   * **Descripción:** El título de la tarea o notificación creada para el grupo.
   * **Detalle:** Un campo para proporcionar un título conciso e identificable para la tarea o notificación.
4. **Description**
   * **Descripción:** Detalles adicionales sobre la tarea o notificación.
   * **Detalle:** Un campo para describir el propósito de la tarea y proporcionar contexto o instrucciones.
5. **Priority**
   * **Descripción:** Define el nivel de urgencia de la tarea o notificación.
   * **Opciones:**
     * **High:** La tarea requiere atención inmediata.
     * **Medium:** La tarea es importante pero no urgente.
     * **Low:** La tarea puede gestionarse más adelante.
6. **Send Mail**
   * **Descripción:** Configura si debe enviarse una notificación por correo electrónico al grupo.
   * **Opciones:**
     * **True:** Envía una notificación por correo electrónico al grupo de compras.
     * **False:** No se envía ninguna notificación por correo electrónico.
7. **Value**
   * **Descripción:** Establece la prioridad numérica para la ejecución de la tarea.
   * **Detalle:** Un campo para introducir un valor numérico, donde un número más bajo representa una mayor prioridad.

## **Funcionalidad**

* **Evaluación de la condición:**\
  La tarjeta realiza sus acciones solo si se cumplen las condiciones del flujo de trabajo definidas.
* **Asignación al grupo y creación de tarea/notificación:**\
  El documento se asigna al grupo de compras especificado. Se crea una tarea o notificación con el título, la descripción y la prioridad proporcionados.
* **Notificación por correo electrónico:**\
  Si "Send Mail" se establece en True, el grupo recibe un correo electrónico sobre la tarea o notificación.

## **Configuración**

1. **Definir el Group Name:**
   * Introduzca el nombre del grupo de compras en el campo Group Name.
2. **Configurar los detalles de la tarea/notificación:**
   * Especifique el Title y la Description de la tarea o notificación.
   * Seleccione la Priority en el menú desplegable (High, Medium o Low).
3. **Habilitar la notificación por correo electrónico:**
   * Establezca "Send Mail" en True o False según si el grupo debe recibir un correo electrónico.
4. **Establecer la prioridad numérica:**
   * Introduzca un valor numérico en el campo Value para determinar la prioridad de la tarea, donde los valores más bajos se procesan primero.
5. Guarde la configuración de la tarjeta y active el flujo de trabajo.

## **Conclusión**

La tarjeta de flujo de trabajo "Assign Document to Procurement Group and Create Task/Notification" garantiza que los documentos se dirijan al grupo adecuado con instrucciones de tarea y niveles de prioridad claros. Al posibilitar notificaciones opcionales por correo electrónico, esta tarjeta mejora la visibilidad de las tareas y garantiza una ejecución fluida del flujo de trabajo.
