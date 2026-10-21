# Asignar documento a la suborganización coincidente

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-5dbe455ae32f-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Asignar documento a una suborganización coincidente según el campo"** asigna un documento a una suborganización de forma dinámica, según un campo especificado del documento. Si no se encuentra ninguna suborganización coincidente, la tarjeta utiliza una suborganización alternativa predefinida.

## **Componentes de la tarjeta:**

1. **Nombre de campo**
   * **Descripción:** Especifica el campo del documento que se utilizará para determinar la suborganización coincidente.
   * **Detalle:** La tarjeta busca un valor en el campo especificado para hacerlo coincidir con una suborganización disponible.
2. **Suborganización (alternativa)**
   * **Descripción:** Define la suborganización alternativa que se utilizará si no se encuentra ninguna coincidencia en el campo especificado.
   * **Detalle:** Si el valor del campo no coincide con ninguna suborganización, el documento se asignará a la suborganización alternativa seleccionada.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Donde"** y **"Y"** se evalúan como verdaderas.
* **Asignación dinámica:**\
  La tarjeta comprueba el valor del campo especificado y asigna el documento a la suborganización que coincide con este valor.
* **Mecanismo alternativo:**\
  Si no se encuentra ninguna suborganización coincidente, el documento se asigna a la suborganización alternativa.

## **Configuración:**

* **Seleccionar el Field Name:**\
  Elija el campo del documento que contiene el valor que se hará coincidir con una suborganización.
* **Seleccionar la suborganización alternativa:**\
  Elija la suborganización que se utilizará si no se encuentra ninguna coincidencia en el campo del documento.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Asignar documento a una suborganización coincidente según el campo"** ofrece flexibilidad al enrutar dinámicamente los documentos a la suborganización adecuada, con una opción alternativa añadida para garantizar que ningún documento quede sin asignar.
