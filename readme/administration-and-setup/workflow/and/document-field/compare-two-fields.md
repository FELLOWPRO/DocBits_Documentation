# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para automatizar acciones comparando los valores de dos campos de documento especificados. Posibilita una toma de decisiones dinámica basada en los datos de los campos y garantiza que los flujos de trabajo se ejecuten en función de las comparaciones entre diferentes valores del documento.

## **Componentes de la tarjeta:**

1. **Field Name (1)**
   * **Descripción:** Especifica el primer campo de documento que se comparará.
   * **Detalle:** Debe coincidir con el identificador exacto del primer campo dentro del documento.
2. **Operator**
   * **Descripción:** Define el tipo de comparación que se realizará entre los dos campos.
   * **Opciones:**
     * **Equals (=):** Comprueba si los valores de los dos campos son iguales.
     * **Not Equals (≠):** Garantiza que los valores de los dos campos sean distintos.
     * **Greater Than (>):** Confirma que el valor del primer campo es mayor que el del segundo campo.
     * **Greater or Equals (≥):** Valida que el valor del primer campo sea igual o mayor que el del segundo campo.
     * **Lesser Than (<):** Comprueba si el valor del primer campo es menor que el del segundo campo.
     * **Less or Equals (≤):** Garantiza que el valor del primer campo sea menor o igual que el del segundo campo.
3. **Field Name (2)**
   * **Descripción:** Especifica el segundo campo de documento que se comparará con el primero.
   * **Detalle:** Debe coincidir con el identificador exacto del segundo campo dentro del documento.

## **Funcionalidad:**

**Evaluación de la condición:** El sistema evalúa si los valores de los dos campos especificados cumplen la condición de comparación definida por el operador.

**Ejecución de la acción:**

* **Condición verdadera:**\
  Si los valores de los dos campos cumplen la condición de comparación, el sistema dispara las acciones asociadas. Estas acciones podrían incluir actualizar registros o disparar alertas.
* **Condición falsa:**\
  Si los valores de los dos campos no cumplen la condición especificada, pueden ejecutarse acciones alternativas o ninguna acción, según la configuración de los flujos de trabajo.

## **Configuración:**&#x20;

* Los usuarios configuran la tarjeta seleccionando los dos campos que se compararán de una lista de campos disponibles en el sistema. El operador se selecciona de una lista desplegable de opciones de comparación disponibles.

## **Conclusión:**

La tarjeta de flujo de trabajo "Compare Two Fields" es una herramienta esencial para comparar datos entre campos dentro de los documentos. Al automatizar acciones según las comparaciones de campos, esta tarjeta ayuda a optimizar la toma de decisiones, facilita la validación de datos y mejora la automatización del flujo de trabajo.
