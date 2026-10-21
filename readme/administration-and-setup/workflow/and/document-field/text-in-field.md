# Texto en el campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61d692604341-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para automatizar acciones según la presencia o ausencia de un texto específico dentro de un campo de documento especificado. Garantiza que los flujos de trabajo puedan adaptarse dinámicamente al contenido de los documentos, facilitando un procesamiento eficiente y una toma de decisiones precisa.

## **Componentes de la tarjeta:**

1. **Texto**
   * **Descripción:** Especifica la cadena de texto que se comprobará dentro del campo.
   * **Detalle:** Puede ser una palabra, frase o secuencia de caracteres relevante para el flujo de trabajo.
2. **Operador**
   * **Descripción:** Define la condición para la presencia de texto en el campo.
   * **Opciones:**
     * **Is:** Dispara el flujo de trabajo si el texto especificado está presente en el campo.
     * **No es:** Dispara el flujo de trabajo si el texto especificado no está presente en el campo.
3. **Nombre de campo**
   * **Descripción:** Especifica el nombre del campo del documento que se evaluará.
   * **Detalle:** Debe coincidir con el identificador exacto del campo dentro del documento.

## **Funcionalidad:**

1. **Evaluación de la condición:** El sistema comprueba si el texto especificado existe en el campo, según el operador seleccionado (Is o Is Not).
2. **Ejecución de la acción:**
   * **Condición verdadera:**\
     Si la presencia del texto en el campo coincide con la condición especificada, el sistema inicia las acciones asociadas. Estas podrían incluir disparar alertas, avanzar flujos de trabajo o actualizar registros.
   * **Condición falsa:**\
     Si la presencia del texto en el campo no coincide con la condición, pueden tomarse acciones alternativas o ninguna acción, según la configuración del flujo de trabajo.

## **Configuración:**

* El usuario introduce el texto que se comprobará. A continuación, selecciona el nombre del campo del documento pertinente.

## **Conclusión:**

La tarjeta de flujo de trabajo "Text Presence in Field" es una herramienta sencilla pero potente para el análisis del contenido de los documentos. Al automatizar acciones según la detección de texto, esta tarjeta facilita flujos de trabajo más inteligentes, mejora la precisión en el manejo de documentos y reduce el esfuerzo manual.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Busque documentos que lleven un marcador de revisión.

**Configuración:** Seleccione el campo de texto `review_note`, que contiene el operador y el texto `manual review`.

**Resultado esperado y contraejemplo:** `Please start manual review` pasa. `Ready for export` no contiene el texto seleccionado y falla.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
