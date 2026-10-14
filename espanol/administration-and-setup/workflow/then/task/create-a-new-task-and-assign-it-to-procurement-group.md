# Create a New Task and assign it to Procurement Group

<figure><img src="../../../../.gitbook/assets/image (292).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Create Task for Procurement Group"** crea una nueva tarea asignada dinámicamente al grupo de compras especificado en la configuración. Esta tarea puede asignarse con diferentes niveles de prioridad, y se puede enviar una notificación opcional por correo electrónico para informar al grupo sobre la tarea. Esta tarjeta garantiza que se avise al equipo adecuado según las condiciones del flujo de trabajo.

## **Componentes de la tarjeta:**

1. **Title**
   * **Descripción:** Especifica el título de la tarea.
   * **Detalle:** Este campo identifica la tarea que se está creando, proporcionando un título conciso para una fácil identificación.
2. **Description**
   * **Descripción:** Proporciona más detalles sobre la tarea.
   * **Detalle:** Este campo se utiliza para describir el objetivo de la tarea y cualquier contexto o instrucción necesarios.
3. **Priority**
   * **Descripción:** Define la urgencia de la tarea.
   * **Opciones:**
     * **High:** La tarea requiere atención inmediata.
     * **Medium:** La tarea es importante pero no urgente.
     * **Low:** La tarea puede gestionarse más adelante.
4. **Group Name**
   * **Descripción:** Especifica el grupo de compras al que se asignará la tarea.
   * **Detalle:** Este campo designa el grupo de compras responsable de la tarea. Garantiza que la tarea se dirija al equipo adecuado.
5. **Email Notification**
   * **Descripción:** Configura si debe enviarse una notificación por correo electrónico al grupo de compras asignado.
   * **Opciones:**
     * **True:** Envía una notificación por correo electrónico al grupo de compras.
     * **False:** No se envía ninguna notificación por correo electrónico.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Creación de la tarea:**\
  La tarjeta crea una nueva tarea, asignándola al grupo de compras definido en el campo "Group Name". Esta tarea incluirá el título, la descripción y el nivel de prioridad especificados.
* **Notificación por correo electrónico:**\
  Si la opción de notificación por correo electrónico se establece en true, se envía un correo electrónico al grupo de compras informándole sobre la tarea.

## **Configuración:**

* **Definir los detalles de la tarea:**\
  Introduzca el título, la descripción y el nivel de prioridad de la tarea.
* **Seleccionar el grupo de compras:**\
  Elija el grupo de compras que será responsable de la tarea.
* **Habilitar la notificación por correo electrónico:**\
  Especifique si debe enviarse una notificación por correo electrónico al grupo tras la creación de la tarea.

## **Conclusión:**

La tarjeta de flujo de trabajo "Create Task for Procurement Group" garantiza que las tareas se asignen automáticamente al grupo de compras adecuado con prioridades definidas. Esta tarjeta también puede notificar al grupo por correo electrónico para garantizar que las tareas se atiendan con prontitud, mejorando la eficiencia del flujo de trabajo y la gestión de tareas.
