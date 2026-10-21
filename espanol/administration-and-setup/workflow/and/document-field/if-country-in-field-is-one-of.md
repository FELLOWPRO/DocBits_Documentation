# Si el país en el campo es uno de

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-364a45ddb67d-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito**

Esta tarjeta de flujo de trabajo está diseñada para evaluar si un país especificado, ubicado en un campo designado, forma parte de una lista predefinida de países. Según esta evaluación, el flujo de trabajo puede continuar con una condición verdadera o falsa. Ayuda a automatizar procesos en los que las acciones dependen de si el país está incluido en un conjunto de países permitidos o restringidos.

## **Componentes de la tarjeta:**

1. **Nombre de campo**
   * **Descripción:** Especifica el campo del documento donde se almacena el nombre o el código del país.
   * **Detalle:** Debe coincidir con el identificador exacto del campo de los datos del país dentro del documento.
2. **Operador**
   * **Descripción:** Define si el país del campo debe formar parte de una lista predefinida de países.
   * **Opciones:**
     * **Is:** El país debe estar incluido en la lista de países especificados para que la condición sea verdadera.
     * **No es:** El país no debe estar incluido en la lista de países especificados para que la condición sea verdadera.
3. **Países**
   * **Descripción:** Especifica la lista de países con los que se comparará el país seleccionado.
   * **Detalle:** Es una lista de países separados por comas. La comparación comprueba si el país del campo está incluido en esta lista.
4. **Continuar condición**
   * **Descripción:** Define el resultado de la comparación. Si el país cumple la condición, el flujo de trabajo continúa con el valor booleano especificado.
   * **Opciones:**
     * **True:** El flujo de trabajo continúa si la condición coincide.
     * **False:** El flujo de trabajo continúa si la condición no coincide.

## **Funcionalidad:**

* **Evaluación de la condición:** El sistema evalúa si el país especificado en el campo forma parte de la lista de países predefinidos. Esta evaluación comprueba el nombre o el código del país frente a la lista proporcionada.
* **Ejecución de la acción:**
  * **Condición verdadera:**\
    Si el país del campo forma parte de la lista de países especificada, el flujo de trabajo continúa con la condición verdadera. Esto puede disparar acciones adicionales, como enrutar documentos al departamento adecuado, aplicar reglas de procesamiento específicas o habilitar funciones específicas de la región.
  * **Condición falsa:**\
    Si el país no coincide con la lista, el flujo de trabajo continúa con la condición falsa. Esto permite ejecutar acciones alternativas o detener el flujo de trabajo según la configuración del sistema.

## **Configuración:**

* Los usuarios configuran la tarjeta seleccionando el campo del documento que contiene el país y especificando la lista de países con la que comparar. A continuación, se elige el operador de una lista desplegable para definir si el país debe formar parte o no de la lista de países especificada. Por último, los usuarios establecen la condición de continuación (verdadera o falsa), que determina el siguiente paso del flujo de trabajo.

## **Conclusión:**

La tarjeta de flujo de trabajo "Country in Field Comparison with List" es una herramienta valiosa para automatizar acciones según si un país forma parte de un grupo predefinido. Al comparar los datos del país con una lista de países permitidos o restringidos, esta tarjeta mejora la eficiencia del flujo de trabajo y garantiza que los procesos del sistema sigan las reglas geográficas correctas.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Enrutar facturas de dos países específicos.

**Configuración:** Seleccione el campo de país, es uno de, códigos de país `DE` y `FR`, y continuación `true`.

**Resultado esperado y contraejemplo:** `DE` pasa; `US` no cumple con la lista de países seleccionados.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
