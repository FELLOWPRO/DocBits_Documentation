# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Assign Document to Disponent / Purchaser"** asigna un documento a un **Disponent** o a un **Purchaser**. Si no se encuentra ningún usuario válido, se selecciona un usuario alternativo para garantizar que el documento siempre se asigne a alguien.

## **Componentes de la tarjeta:**

1. **Disponent / Purchaser**
   * **Descripción:** Especifica si el documento se asignará a un Disponent o a un Purchaser.
   * **Opciones:**
     * **Disponent:** Asigna el documento al Disponent.
     * **Purchaser:** Asigna el documento al Purchaser.
2. **Fallback User**
   * **Descripción:** Especifica un usuario alternativo en caso de que el documento no pueda asignarse al Disponent o Purchaser seleccionado.
   * **Detalle:** La lista desplegable de usuarios disponibles le permite elegir un usuario alternativo para garantizar que el documento se asigne aunque no se pueda determinar el usuario principal.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
* **Asignación del documento:**\
  La tarjeta asigna el documento al **Disponent** o al **Purchaser** según lo seleccionado. Si la persona seleccionada no está disponible o no es válida, el documento se asigna al usuario alternativo.

## **Configuración:**

* **Seleccionar Disponent / Purchaser:**\
  Elija si asignar el documento al **Disponent** o al **Purchaser**.
* **Seleccionar el Fallback User:**\
  Elija un usuario alternativo de la lista desplegable que recibirá el documento si la asignación principal no es posible.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Assign Document to Disponent / Purchaser"** garantiza que el documento siempre se asigne, ya sea al Disponent/Purchaser seleccionado o, si es necesario, al usuario alternativo. Esto minimiza las interrupciones del flujo de trabajo y garantiza que el procesamiento de documentos continúe sin problemas.
