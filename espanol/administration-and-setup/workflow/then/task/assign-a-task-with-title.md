# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo "Assign Task / Notification from Decision Table" está diseñada para asignar dinámicamente tareas o notificaciones según los resultados de una tabla de decisión. Esta tarjeta garantiza que las tareas o notificaciones se asignen al usuario o grupo correcto según la lógica definida en la tabla de decisión, con una notificación opcional por correo electrónico enviada al destinatario.

## **Componentes de la tarjeta:**

1. **Title**
   * **Descripción**: Especifica el título de la tarea o notificación que se está creando.
   * **Detalle**: El título debe proporcionar contexto y describir el propósito de la tarea o notificación.
2. **Description**
   * **Descripción**: Define el contenido o el propósito de la tarea o notificación.
   * **Detalle**: Proporciona información adicional sobre la tarea o notificación, explicando el contexto o la acción requerida.
3. **Priority**
   * **Descripción**: Define el nivel de urgencia de la tarea o notificación.
   * **Opciones**:
     * **High**: Tareas o notificaciones que requieren atención inmediata.
     * **Medium**: Tareas importantes que deben abordarse con prontitud.
     * **Low**: Tareas que pueden atenderse más adelante.
4. **Assignee Type**
   * **Descripción**: Especifica el usuario o grupo asignado a la tarea o notificación según el resultado de la tabla de decisión.
   * **Detalle**: La tabla de decisión evalúa dinámicamente las condiciones y devuelve el usuario o grupo adecuado para la asignación.
5. **Email Notification**
   * **Descripción**: Configura si se enviará una notificación por correo electrónico al usuario o grupo asignado.
   * **Opciones**:
     * **True**: Envía una notificación por correo electrónico al destinatario.
     * **False**: No se envía ninguna notificación por correo electrónico.

#### **Componentes adicionales en la versión 3**

1. **Notification Type**
   * **Descripción**: Especifica si la tarjeta crea una tarea o una notificación.
   * **Opciones**:
     * **Task**: Crea una tarea asignada al usuario o grupo de la tabla de decisión.
     * **Notification**: Envía una notificación al usuario o grupo de la tabla de decisión.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Asignación de tarea / notificación**\
  La tarjeta asigna la tarea o notificación al usuario o grupo identificado por la tabla de decisión. La tabla de decisión evalúa dinámicamente las condiciones predefinidas y devuelve el destinatario correspondiente.
* **Notificación por correo electrónico**\
  Si está configurado para ello, se envía una notificación por correo electrónico al usuario o grupo asignado.
* **Funcionalidad de la versión 3**\
  En la versión 3, la tarjeta permite crear una tarea o una notificación, proporcionando más flexibilidad para la gestión de tareas y la comunicación.

## **Configuración:**

1. **Definir los detalles de la tarea o notificación**:\
   Introduzca el título, la descripción y la prioridad de la tarea o notificación.
2. **Configurar la tabla de decisión**:\
   Configure la tabla de decisión para determinar dinámicamente qué usuario o grupo debe recibir la tarea o notificación.
3. **Habilitar la notificación por correo electrónico**:\
   Especifique si debe enviarse una notificación por correo electrónico al usuario o grupo asignado.
4. **Especificar el Notification Type (versión 3)**:\
   Elija si la tarjeta creará una tarea o enviará una notificación.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Assign Task / Notification from Decision Table"** automatiza la asignación de tareas o notificaciones según condiciones dinámicas definidas en una tabla de decisión. La versión 3 mejora su funcionalidad al permitir a los usuarios elegir entre crear una tarea o una notificación, y garantiza que siempre se asigne el destinatario correcto. La función de notificación por correo electrónico mantiene informados a los usuarios, agilizando la comunicación y la gestión de tareas.
