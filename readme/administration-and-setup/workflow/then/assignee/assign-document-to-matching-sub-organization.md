# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Assign Document to Matching Sub-Organization Based on Field"** asigna un documento a una suborganización de forma dinámica, según un campo especificado del documento. Si no se encuentra ninguna suborganización coincidente, la tarjeta utiliza una suborganización alternativa predefinida.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción:** Especifica el campo del documento que se utilizará para determinar la suborganización coincidente.
   * **Detalle:** La tarjeta busca un valor en el campo especificado para hacerlo coincidir con una suborganización disponible.
2. **Sub-Organization (Fallback)**
   * **Descripción:** Define la suborganización alternativa que se utilizará si no se encuentra ninguna coincidencia en el campo especificado.
   * **Detalle:** Si el valor del campo no coincide con ninguna suborganización, el documento se asignará a la suborganización alternativa seleccionada.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Where"** y **"And"** se evalúan como verdaderas.
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

La tarjeta de flujo de trabajo **"Assign Document to Matching Sub-Organization Based on Field"** ofrece flexibilidad al enrutar dinámicamente los documentos a la suborganización adecuada, con una opción alternativa añadida para garantizar que ningún documento quede sin asignar.
