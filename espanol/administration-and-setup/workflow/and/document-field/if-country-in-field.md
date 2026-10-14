# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para evaluar si un país especificado, ubicado en un campo designado, forma parte de un área comercial o política particular (Unión Europea, espacio Schengen o NAFTA). Según esta evaluación, el flujo de trabajo puede continuar con una condición verdadera o falsa, posibilitando acciones adicionales dentro del sistema. Es especialmente útil para automatizar reglas de negocio específicas de la región, garantizar el cumplimiento o disparar flujos de trabajo específicos según las afiliaciones geográficas.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción:** Especifica el campo del documento donde se almacena el nombre o el código del país.
   * **Detalle:** Debe coincidir con el identificador exacto del campo de los datos del país dentro del documento.&#x20;
2. **Operator**
   * **Descripción:** Especifica si el país del campo seleccionado debe coincidir o no con la región o el acuerdo seleccionado.
   * **Opciones:**
     * **Is:** El país debe formar parte del acuerdo seleccionado (UE, Schengen o NAFTA) para que la condición sea verdadera.
     * **Is Not:** El país no debe formar parte del acuerdo seleccionado para que la condición sea verdadera.
3. **Country Comparison**
   * **Descripción:** Define si el país del campo se comprueba frente a un acuerdo político o comercial específico.
   * **Opciones:**
     * **European Union:** La tarjeta comprueba si el país es miembro de la Unión Europea.
     * **Schengen Area:** La tarjeta comprueba si el país forma parte del espacio Schengen.
     * **NAFTA:** La tarjeta comprueba si el país es miembro del acuerdo NAFTA.
4. **Boolean**
   * **Descripción:** Define el resultado de la comparación. Si el país cumple la condición, el flujo de trabajo continúa con el valor booleano especificado.
   * **Opciones:**
     * **True:** El flujo de trabajo continúa si la condición coincide.
     * **False:** El flujo de trabajo continúa si la condición no coincide.

## **Funcionalidad:**

* **Evaluación de la condición:**
  * El sistema evalúa si el país especificado en el campo forma parte de la región o el acuerdo elegido (UE, espacio Schengen o NAFTA) según el operador seleccionado. Esta evaluación comprueba el nombre o el código del país frente a una lista predefinida de países que pertenecen a cada grupo respectivo.
* **Ejecución de la acción:**
  * **Condición verdadera:** Si el país del campo coincide con la región seleccionada (según el operador), el flujo de trabajo continúa con la condición verdadera especificada. Esto puede disparar acciones adicionales, como enrutar documentos, aplicar reglas de procesamiento especiales o habilitar funciones específicas de la región.
  * **Condición falsa:** Si el país no coincide con la región seleccionada (según el operador), el flujo de trabajo continúa con la condición falsa especificada, permitiendo la ejecución de acciones alternativas o la finalización del flujo de trabajo según la configuración del sistema.

## **Configuración:**&#x20;

* Los usuarios configuran la tarjeta seleccionando el campo del documento que contiene el país y especificando la región (Unión Europea, espacio Schengen o NAFTA). A continuación, se elige el operador de una lista desplegable para definir si el país debe formar parte o no de la región seleccionada. Por último, los usuarios establecen la condición de continuación (verdadera o falsa), que determina el siguiente paso del flujo de trabajo.

## **Conclusión:**

La tarjeta de flujo de trabajo "Country in Field Comparison" es una herramienta esencial para automatizar procesos que dependen de reglas geográficas, como el cumplimiento de acuerdos comerciales o afiliaciones políticas. Al comparar los datos del país con regiones específicas como la Unión Europea, el espacio Schengen o NAFTA, esta tarjeta garantiza que el sistema aplique la lógica de procesamiento correcta, mejorando la eficiencia y garantizando una ejecución precisa del flujo de trabajo según las condiciones geográficas.
