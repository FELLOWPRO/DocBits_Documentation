# Condición de Usuario Asignado

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo gestiona la ejecución de operaciones basadas en si una tarea o documento está asignado a un usuario específico o a un conjunto de usuarios. Emplea lógica condicional para activar o prevenir acciones específicas, siendo ideal para flujos de trabajo que requieren un manejo específico de usuarios.

**Componentes de la Tarjeta**

1. **Operador**
* **Descripción**: Define la condición lógica a aplicar a la asignación de usuario.
* **Opciones**:
* **ES**: Activa la operación si el usuario asignado al documento o tarea coincide con cualquier usuario en la lista especificada.
* **NO ES**: Activa la operación si el usuario asignado al documento o tarea no coincide con ningún usuario en la lista especificada.
2. **Lista de Usuarios**
* **Descripción**: Una lista o selección de usuarios para comparar con el usuario asignado.
* **Detalle**: Esta lista puede incluir uno o varios usuarios, permitiendo que la tarjeta maneje condiciones de usuario singular y múltiple de manera efectiva. La selección se puede realizar a través de casillas de verificación, un menú desplegable de selección múltiple u elementos de interfaz de usuario similares.

**Funcionalidad**

* **Identificación de Asignación de Usuario**: Identifica automáticamente al usuario o usuarios asignados a una tarea o documento específico dentro del sistema ERP.
* **Evaluación de Condición**:
* Utilizando el operador **ES**, la tarjeta verifica si el usuario asignado está entre los listados en la Lista de Usuarios.
* Utilizando el operador **NO ES**, la tarjeta asegura que el usuario asignado no esté entre los listados.
* **Ejecución de Acción**:
* **Condición Verdadera**: Si la asignación de usuario cumple con la condición (ya sea ES o NO ES), se activan acciones relevantes, como notificaciones, inicio de tareas, aprobaciones u otros pasos del flujo de trabajo.
* **Condición Falsa**: Si la condición no se cumple, el documento o tarea puede pasar por una ruta diferente, o se pueden especificar acciones alternativas.

**Interacciones de Usuario**

* **Configuración e Instalación**: Los usuarios configuran la tarjeta seleccionando un operador y especificando los usuarios relevantes de la Lista de Usuarios. La configuración debe ser amigable e intuitiva para acomodar selecciones de bases de usuarios potencialmente grandes.
* **Monitoreo e Informes**: El sistema ERP debe proporcionar funcionalidad para monitorear e informar sobre las operaciones activadas por esta tarjeta, ofreciendo información sobre la precisión de las asignaciones y la eficiencia del proceso.
* **Manejo de Errores y Notificaciones**: Los usuarios deben tener opciones para recibir alertas o notificaciones si hay problemas con las asignaciones, como tareas no asignadas o errores en la selección de usuarios.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Usuario Asignado" es una herramienta crítica para gestionar flujos de trabajo de documentos y tareas que dependen de asignaciones de usuarios. Al permitir condiciones basadas en si una tarea o documento está asignado a usuarios específicos, asegura que los flujos de trabajo solo se activen por interacciones de usuario apropiadas, mejorando tanto la responsabilidad como la alineación de tareas dentro de los equipos. Documentar claramente esta tarjeta ayudará a los usuarios a comprender su importancia e integrarla de manera efectiva en sus flujos de trabajo, garantizando operaciones fluidas y eficientes adaptadas a roles y responsabilidades de usuario.
