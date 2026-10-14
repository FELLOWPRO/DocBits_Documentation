# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para automatizar acciones según la presencia o ausencia de un texto específico dentro de un campo de documento especificado. Garantiza que los flujos de trabajo puedan adaptarse dinámicamente al contenido de los documentos, facilitando un procesamiento eficiente y una toma de decisiones precisa.

## **Componentes de la tarjeta:**

1. **Text**
   * **Descripción:** Especifica la cadena de texto que se comprobará dentro del campo.
   * **Detalle:** Puede ser una palabra, frase o secuencia de caracteres relevante para el flujo de trabajo.
2. **Operator**
   * **Descripción:** Define la condición para la presencia de texto en el campo.
   * **Opciones:**
     * **Is:** Dispara el flujo de trabajo si el texto especificado está presente en el campo.
     * **Is Not:** Dispara el flujo de trabajo si el texto especificado no está presente en el campo.
3. **Field Name**
   * **Descripción:** Especifica el nombre del campo del documento que se evaluará.
   * **Detalle:** Debe coincidir con el identificador exacto del campo dentro del documento.

## **Funcionalidad:**

1. **Evaluación de la condición:** El sistema comprueba si el texto especificado existe en el campo, según el operador seleccionado (Is o Is Not).
2. **Ejecución de la acción:**
   * **Condición verdadera:**\
     Si la presencia del texto en el campo coincide con la condición especificada, el sistema inicia las acciones asociadas. Estas podrían incluir disparar alertas, avanzar flujos de trabajo o actualizar registros.
   * **Condición falsa:**\
     Si la presencia del texto en el campo no coincide con la condición, pueden tomarse acciones alternativas o ninguna acción, según la configuración del flujo de trabajo.

## **Configuración:**&#x20;

* El usuario introduce el texto que se comprobará. A continuación, selecciona el nombre del campo del documento pertinente.

## **Conclusión:**

La tarjeta de flujo de trabajo "Text Presence in Field" es una herramienta sencilla pero potente para el análisis del contenido de los documentos. Al automatizar acciones según la detección de texto, esta tarjeta facilita flujos de trabajo más inteligentes, mejora la precisión en el manejo de documentos y reduce el esfuerzo manual.
