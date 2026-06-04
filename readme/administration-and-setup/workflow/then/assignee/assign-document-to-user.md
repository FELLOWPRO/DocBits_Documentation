# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Assign Document to User"** permite a los usuarios asignar un documento a un usuario específico, garantizando una gestión fluida del flujo de trabajo al enrutar los documentos a la persona adecuada. La versión 3 añade la capacidad de usar un árbol de decisión para determinar dinámicamente la asignación de usuario según las condiciones disponibles.

## **Componentes de la tarjeta:**

1. **User**
   * **Descripción:** Especifica el usuario al que se asignará el documento.
   * **Detalle:** Se proporciona una lista desplegable de todos los usuarios disponibles para su selección. Al usuario seleccionado se le asignará el documento para una acción adicional.

## **Componentes adicionales en la versión 3:**

1. **Use Decision Tree**
   * **Descripción:** Si está habilitado, la tarjeta usa un árbol de decisión para determinar dinámicamente la asignación de usuario.
   * **Opciones:**
     * **True:** Usa el árbol de decisión para la asignación dinámica de usuario.
     * **False:** Asigna el documento al usuario seleccionado sin usar el árbol de decisión.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Asignación del documento:**\
  La tarjeta asigna el documento al usuario seleccionado, garantizando que la tarea se enrute a la persona adecuada para su acción. Esto ayuda con la responsabilidad y la gestión eficaz de documentos.
* **Árbol de decisión (versión 3):**\
  Si el árbol de decisión está habilitado, la tarjeta evalúa las condiciones definidas dentro del árbol para seleccionar dinámicamente el usuario para la asignación del documento.

## **Configuración:**

* **Seleccionar el User:**\
  Elija el **usuario** de la lista desplegable al que se asignará el documento.
* **Use Decision Tree (versión 3):**\
  Habilite o deshabilite el uso del árbol de decisión para seleccionar dinámicamente el usuario.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Assign Document to User"** facilita un enrutamiento eficiente de los documentos al asignarlos al usuario seleccionado, con la flexibilidad añadida en la versión 3 de determinar dinámicamente el usuario mediante un árbol de decisión. Esto garantiza un proceso de flujo de trabajo más adaptable y eficiente.
