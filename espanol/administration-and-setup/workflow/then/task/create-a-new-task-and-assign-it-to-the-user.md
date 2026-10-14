# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo **"Create Task or Notification"** agiliza la gestión de tareas y notificaciones dentro de los flujos de trabajo. Según la versión, la tarjeta puede crear tareas, enviar notificaciones y aprovechar funcionalidades adicionales, como árboles de decisión para el procesamiento dinámico.

## **Componentes de la tarjeta**

1. **Title**
   * **Descripción**: Define el título de la tarea o notificación que se está creando.
   * **Detalle**: El título proporciona un identificador claro y conciso para la tarea o notificación.
2. **Description**
   * **Descripción**: Proporciona detalles sobre la tarea o notificación.
   * **Detalle**: Ayuda a aclarar el propósito o el contexto de la tarea o notificación para el usuario asignado.
3. **Priority**
   * **Descripción**: Establece el nivel de urgencia de la tarea.
   * **Opciones**:
     * **High**: Requiere atención inmediata.
     * **Medium**: Importante pero no urgente.
     * **Low**: Puede abordarse más adelante.
4. **Assigned User**
   1. **Descripción**: Especifica el usuario al que se asigna la tarea.
   2. **Detalle**: Los usuarios se seleccionan de una lista desplegable del personal disponible.
5. **Email Notification**
   * **Descripción**: Determina si el usuario asignado recibe una notificación por correo electrónico.
   * **Opciones**:
     * **True**: Envía una notificación por correo electrónico al usuario.
     * **False**: No se envía ninguna notificación por correo electrónico.

## Componentes adicionales **en la versión 3 y la versión 4**

1. **Decision Tree (solo en la versión 3)**
   * **Descripción**: Posibilita el uso de un árbol de decisión para la creación dinámica de tareas.
   * **Opciones**:
     * **True**: Activa el procesamiento del árbol de decisión.
     * **False**: Deshabilita el procesamiento del árbol de decisión.
2. **Task or Notification (solo en la versión 4)**
   * **Descripción**: Permite seleccionar entre crear una tarea o una notificación.
   * **Opciones**:
     * **Task**: Crea una tarea.
     * **Notification**: Crea una notificación en lugar de una tarea.

## **Funcionalidad:**

* **Evaluación de la condición**:\
  Esta tarjeta se dispara solo si se cumplen las condiciones de las secciones **"Where"** y **"And"**.
* **Creación de tarea o notificación**:
  * Versiones 2 y 3: Se crea una tarea con el título, la descripción, la prioridad y el usuario asignado especificados.
  * Versión 4: Permite crear una tarea o una notificación.
* **Asignación dinámica**:
  * En la versión 3, el árbol de decisión determina dinámicamente el usuario al que se asignará la tarea según los parámetros del flujo de trabajo.
* **Notificación por correo electrónico**:\
  Envía un correo electrónico al usuario asignado si la opción de notificación está habilitada.

## **Configuración:**

1. **Seleccionar la versión**: Elija la versión de la tarjeta según la funcionalidad requerida:
   * Versión 2: Creación básica de tareas con asignación manual de usuario y notificaciones por correo electrónico.
   * Versión 3: Incluye la funcionalidad de árbol de decisión para la asignación dinámica de usuario.
   * Versión 4: Añade la capacidad de crear una notificación en lugar de una tarea.
2. **Introducir los detalles de la tarea**: Especifique el título, la descripción y la prioridad de la tarea o notificación.
3. **Asignar el usuario**:
   * Para las versiones 2 y 4, seleccione manualmente un usuario de la lista desplegable.
   * Para la versión 3, habilite el árbol de decisión para determinar dinámicamente el usuario asignado.
4. **Habilitar la notificación por correo electrónico**: Especifique si el usuario asignado debe recibir una notificación por correo electrónico.
5. (Para la versión 4) **Elegir tarea o notificación**: Indique si desea crear una tarea o una notificación.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Create Task or Notification"** es una herramienta versátil para gestionar tareas y notificaciones. Al admitir la asignación dinámica de usuario mediante árboles de decisión y proporcionar opciones para la creación de tareas o notificaciones, mejora la adaptabilidad del flujo de trabajo y la eficiencia de la colaboración.
