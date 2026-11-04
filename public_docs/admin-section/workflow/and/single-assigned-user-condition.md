# Condición de Usuario Asignado Único

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo facilita operaciones basadas en la asignación de una tarea o documento a un único usuario específico. Utilizando un enfoque directo de lógica condicional, gestiona flujos de trabajo que requieren la participación dirigida del usuario, asegurando precisión en el manejo de tareas basadas en usuarios.

**Componentes de la Tarjeta**

1. **Operador**
* **Descripción**: Especifica la lógica a aplicar a la asignación del usuario.
* **Opciones**:
* **ES**: Activa la operación si el usuario asignado del documento o tarea coincide con el usuario especificado.
* **NO ES**: Activa la operación si el usuario asignado no coincide con el usuario especificado.
2. **Usuario**
* **Descripción**: Permite la selección de un único usuario con el que se comparará el usuario asignado.
* **Detalle**: Involucra un simple menú desplegable o campo de autocompletar donde se puede seleccionar un usuario a la vez.

**Funcionalidad**

* **Identificación de Asignación de Usuario**: Identifica al usuario actualmente asignado a una tarea o documento específico.
* **Evaluación de Condición**:
* Para el operador **ES**, la tarjeta verifica si el usuario asignado es el mismo que el usuario seleccionado.
* Para el operador **NO ES**, verifica que el usuario asignado sea diferente al usuario seleccionado.
* **Ejecución de Acción**:
* **Condición Verdadera**: Si la asignación cumple con la condición establecida (ES o NO ES), activa acciones predefinidas, que podrían incluir avanzar con aprobaciones, iniciar más tareas, enviar notificaciones u otros flujos de trabajo relacionados.
* **Condición Falsa**: Si la condición falla, el sistema puede redirigir la tarea, retenerla para revisión o activar acciones predefinidas alternativas.

**Interacciones del Usuario**

* **Configuración y Configuración**: Los usuarios configuran la tarjeta eligiendo un operador y seleccionando un usuario del campo de usuario. Esta configuración debería ser sencilla, asegurando una selección y configuración de usuario fácil.
* **Monitoreo e Informes**: Ofrece herramientas para monitorear el rendimiento de la tarjeta, como rastrear qué tareas son activadas por asignaciones de usuario específicas y los resultados de estas activaciones.
* **Manejo de Errores y Notificaciones**: Proporciona mecanismos para alertar a los usuarios si las tareas se asignan incorrectamente o si ocurren errores operativos debido a problemas de asignación.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Usuario Asignado Único" es esencial para la gestión precisa de documentos y tareas específicas de usuario dentro de un sistema ERP. Simplifica los flujos de trabajo al centrarse en asignaciones individuales de usuarios, asegurando que las acciones solo se ejecuten cuando sea apropiado, basado en el rol y responsabilidades del usuario. Documentar claramente esta tarjeta ayudará a los usuarios a comprender su aplicación, permitiéndoles implementarla y gestionarla de manera efectiva dentro de sus operaciones diarias. Esta documentación garantiza que todos los usuarios potenciales puedan comprender fácilmente el propósito de la tarjeta e integrarla sin problemas en sus flujos de trabajo.
