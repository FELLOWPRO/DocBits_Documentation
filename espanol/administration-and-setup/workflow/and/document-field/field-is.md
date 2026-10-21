# El campo es

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-db30554e1eb1-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para automatizar acciones según la presencia o el estado de un campo especificado dentro de un documento. Al evaluar si el campo está vacío, ausente o completado, permite que los flujos de trabajo manejen los documentos con precisión y exactitud.

## **Componentes de la tarjeta:**

1. **Nombre de campo**
   * **Descripción:** Especifica el nombre del campo que se evaluará.
   * **Detalle:** Debe coincidir con el identificador exacto utilizado en el documento para garantizar una detección precisa del campo.
2. **Operadores**
   * **Descripción**: Define la condición que dispara el flujo de trabajo, según la presencia o el estado del campo.
   * **Opciones**:
     * **Vacío/No en el documento:** El flujo de trabajo se dispara si el campo está ausente del documento o si está presente pero vacío.
     * **En documento/no vacío:** El flujo de trabajo se dispara si el campo existe en el documento y contiene un valor.

## **Funcionalidad:**

* **Detección de estado:** La tarjeta supervisa el campo especificado para evaluar su presencia y estado.
* **Evaluación de la condición:**
  * El sistema evalúa si el campo especificado está en el estado (Empty/Not in Document o In Document/Not Empty) definido por el operador seleccionado.
*

**Ejecución de la acción:**
* **Condición Empty/Not in Document:** Si el estado del campo coincide con esta condición (es decir, el campo está ausente del documento o presente pero vacío), el sistema inicia las acciones asociadas. Estas pueden incluir generar alertas, señalar el documento para su revisión o detener el flujo de trabajo.
* **Condición In Document/Not Empty:** Si el estado del campo coincide con esta condición (es decir, el campo existe en el documento y contiene un valor), el sistema dispara las acciones asociadas. Estas podrían implicar habilitar pasos posteriores del flujo de trabajo, actualizar registros o disparar notificaciones.
## **Configuración:**

* Los usuarios seleccionan el campo de una lista de campos disponibles del documento. El operador se elige mediante un menú desplegable, que ofrece opciones claras para "Empty/Not in Document" o "In Document/Not Empty".

## **Conclusión:**

La tarjeta de flujo de trabajo "Field Presence and State Validation" es una herramienta fundamental para los flujos de trabajo de procesamiento de documentos, garantizando un manejo preciso de los campos ausentes o completados. Al automatizar acciones según los estados de los campos, esta tarjeta mejora la integridad de los datos, reduce los errores y garantiza que los flujos de trabajo funcionen de forma fluida y eficiente.
