# Assign to group

<figure><img src="../../../../.gitbook/assets/image (304).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

La tarjeta de flujo de trabajo **"Assign to Group"** facilita la asignación de documentos a un **grupo** específico dentro del sistema. Esto garantiza que el documento sea procesado por el equipo adecuado, agilizando el flujo de trabajo. Mejorada en versiones posteriores, introduce la funcionalidad de árbol de decisión para la asignación dinámica de grupos.

## Componentes de la tarjeta:

1. **Groups**
   * **Descripción:** Especifica el **grupo** al que se asignará el documento.
   * **Detalle:** Se selecciona de una lista desplegable de **grupos** disponibles.



## **Componentes adicionales en la versión 3**

1. **Decision Tree (solo en la versión 3)**
   * **Descripción:** Permite usar un árbol de decisión para determinar dinámicamente el **grupo** al que debe asignarse el documento.
   * **Opciones:**
     * **True:** Habilita el procesamiento del árbol de decisión.
     * **False:** Deshabilita el procesamiento del árbol de decisión.

## Funcionalidad:

* **Evaluación de la condición:** La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Asignación del documento:** Asigna el documento al **grupo** seleccionado. En la **versión 3**, el **árbol de decisión** determina el grupo de destino dinámicamente si está habilitado.

## Configuración:

* **Seleccionar el Group:** Elija el **grupo** de la lista desplegable para asignar el documento.
* **Use Decision Tree (solo en la versión 3):** Habilite esta opción si debe usarse el **árbol de decisión** para la asignación dinámica.

## Conclusión:

La tarjeta de flujo de trabajo **"Assign to Group"** automatiza la asignación de documentos a **grupos** predefinidos, mejorando la coordinación de los equipos. La **versión 3** introduce la capacidad de asignar grupos dinámicamente según la lógica del árbol de decisión.
