# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Assign User from Field with Fallback"** asigna dinámicamente un usuario según el valor encontrado en un campo de documento especificado. Si el campo no contiene un usuario válido, se selecciona un usuario alternativo de una lista predefinida de usuarios disponibles para garantizar que la tarea o acción se asigne correctamente.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción:** Especifica el **campo del documento** que contiene la información del usuario que se asignará.
   * **Detalle:** Este campo se evalúa para determinar qué usuario debe asignarse. Si el campo contiene un usuario válido, se le asignará la tarea a ese usuario. Si el campo está vacío o no es válido, se asignará el usuario alternativo.
2. **User (Fallback)**
   * **Descripción:** Especifica el **usuario alternativo** que se asignará si el campo del documento no contiene un usuario válido.
   * **Detalle:** Se proporciona una lista desplegable de todos los usuarios disponibles para su selección. Este usuario se asignará si el campo del documento está vacío o no contiene un usuario válido.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Asignación de usuario basada en campo:**\
  La tarjeta primero intenta asignar la tarea o acción al usuario identificado en el **Field Name**.
* **Asignación de usuario alternativo:**\
  Si el campo no contiene un usuario válido (o está vacío), la tarjeta asigna la tarea al usuario alternativo seleccionado de la lista desplegable **User (Fallback)**.

## **Configuración:**

* **Seleccionar el Field Name:**\
  Elija el **campo del documento** que especifica el usuario para la asignación.
* **Seleccionar el Fallback User:**\
  Elija el **usuario alternativo** de la lista desplegable. A este usuario se le asignará la tarea si el campo del documento no contiene un usuario válido.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Assign User from Field with Fallback"** garantiza que una tarea o acción siempre se asigne a un usuario válido. Si el usuario del campo del documento no está disponible, el usuario alternativo se asigna automáticamente, proporcionando flexibilidad y garantizando la finalización de la tarea.
