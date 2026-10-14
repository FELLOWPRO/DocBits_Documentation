# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Create Group Task or Notification"** facilita la creación de tareas o notificaciones para grupos especificados, garantizando una comunicación y una gestión de tareas eficientes. Mejorada con la funcionalidad de árbol de decisión en versiones posteriores, determina dinámicamente el grupo asignado o el método, agilizando las operaciones.

## **Componentes de la tarjeta:**

1. **Title**
   * **Descripción**: Especifica el título de la tarea o notificación.
   * **Detalle**: Actúa como identificador de la tarea o notificación creada.
2. **Description**
   * **Descripción**: Describe el contexto o los detalles de la tarea o notificación.
   * **Detalle**: Proporciona claridad sobre su propósito.
3. **Priority**
   * **Descripción**: Establece el nivel de importancia de la tarea.
   * **Opciones**:
     * **High**: Requiere acción inmediata.
     * **Medium**: Importante pero menos urgente.
     * **Low**: Puede abordarse más adelante.
4. **Assigned Group**
   * **Descripción**: Especifica el grupo responsable de la tarea o notificación.
   * **Detalle**: Se selecciona de una lista desplegable de grupos disponibles.
5. **Email Notification**
   * **Descripción**: Posibilita el envío de un correo electrónico para notificar al grupo asignado.
   * **Opciones**:
     * **True**: Envía una notificación por correo electrónico.
     * **False**: No se envía ninguna notificación por correo electrónico.

## **Componentes adicionales en la versión 3 y la versión 4**

1. **Decision Tree (solo en la versión 3)**
   * **Descripción**: Posibilita el uso de un árbol de decisión para la creación dinámica de tareas.
   * **Opciones**:
     * **True**: Activa el procesamiento del árbol de decisión.
     * **False**: Deshabilita el procesamiento del árbol de decisión.
2. **Task/Notification Option (solo en la versión 4)**
   * **Descripción**: Permite crear una tarea o una notificación.
   * **Opciones**:
     * **Task**: Crea una tarea para el grupo seleccionado.
     * **Notification**: Envía una notificación en lugar de crear una tarea.

## **Funcionalidad:**

* **Evaluación de la condición**:\
  Ejecuta la acción de la tarjeta solo cuando las secciones **"Where"** y **"And"** son verdaderas.
* **Creación de tarea o notificación**:
  * Se crea una tarea para el grupo seleccionado con el título, la descripción y la prioridad especificados.
  * En la versión 4, la tarjeta puede crear una notificación en lugar de una tarea.
* **Asignación dinámica (solo en la versión 3)**:\
  Si está habilitado, el árbol de decisión determina el grupo de destino dinámicamente.
* **Notificación por correo electrónico**:\
  Envía una notificación por correo electrónico al grupo si la opción de correo electrónico se establece en true.

## **Configuración:**

1. **Definir los detalles de la tarea o notificación**: Introduzca el título, la descripción y la prioridad.
2. **Asignar a un grupo**: Seleccione un grupo de la lista desplegable para la asignación de la tarea o notificación.
3. **Habilitar la notificación por correo electrónico**: Indique si el grupo debe ser notificado por correo electrónico.
4. **Use Decision Tree (solo en la versión 3)**: Habilite el árbol de decisión para asignar el grupo dinámicamente.
5. **Seleccionar el tipo de salida (solo en la versión 4)**: Elija si la tarjeta crea una tarea o una notificación.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Create Group Task or Notification"** simplifica la gestión de tareas y notificaciones dirigiéndose directamente a los grupos. Su función de asignación dinámica, posibilitada por el árbol de decisión, mejora la flexibilidad, mientras que las notificaciones por correo electrónico garantizan una comunicación oportuna. Las versiones 3 y 4 añaden funcionalidad avanzada, lo que la convierte en una herramienta versátil para una ejecución eficiente del flujo de trabajo.
