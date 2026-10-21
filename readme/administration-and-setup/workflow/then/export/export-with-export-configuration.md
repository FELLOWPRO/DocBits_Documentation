# Exportar con configuración de exportación

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-10e6b7590bc6-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Exportar documento con configuración de exportación"** está diseñada para exportar un documento utilizando una configuración de exportación específica. Proporciona la flexibilidad de ignorar cualquier tarea pendiente asociada con el documento, lo que garantiza un proceso de exportación fluido independientemente de su estado actual.

## **Componentes de la Tarjeta:**

1. **Exportar configuración**
   * **Descripción**: Especifica la configuración de exportación que se utilizará para procesar el documento.
   * **Detalle**: Esta configuración determina el formato, estructura y destino del documento exportado.
2. **Ignorar tareas pendientes**
   * **Descripción**: Determina si las tareas pendientes vinculadas al documento deben ignorarse durante el proceso de exportación.
   * **Opciones**:
     * **True**: Exporta el documento independientemente de las tareas pendientes.
     * **False**: garantiza que las tareas pendientes se completen antes de la exportación.

## **Funcionalidad:**

* **Evaluación de condición**: el sistema evalúa las condiciones establecidas en **"Dónde"** y **"Y secciones"** del flujo de trabajo. Si se cumplen ambas condiciones, se inicia el proceso de exportación.
* **Exportación de documento**: utilizando la **Configuración de exportación** especificada, el documento se procesa y exporta en el formato y destino definidos.
* **Manejo de tareas pendientes**: si **Ignorar tareas pendientes** está configurado en **Verdadero**, el proceso de exportación omite cualquier tarea pendiente vinculada al documento. Si se establece en **False**, las tareas pendientes pueden impedir la exportación. Resuélvalos y organice el desencadenador del flujo de trabajo previsto o vuelva a intentarlo.

## **Instalación y configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. Seleccione la **Configuración de exportación** deseada para definir cómo se exportará el documento.
2. Elija si desea **Ignorar tareas pendientes** estableciendo el valor en **Verdadero** o **Falso.**
3. Asegúrese de que las condiciones en **"Dónde"** y **"Y Secciones"** estén configuradas correctamente, ya que la tarjeta solo ejecuta su acción cuando estas condiciones son verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Exportar documento con configuración de exportación"** garantiza que los documentos se exporten de manera eficiente y de acuerdo con configuraciones predefinidas. Con la capacidad de ignorar tareas pendientes, esta tarjeta ofrece flexibilidad en el manejo de documentos en varias etapas, reduciendo demoras y agilizando el proceso de exportación.

## Versiones actuales y tareas pendientes

En v3, elija también **Estado después de la exportación**: `finished` cierra el documento después de una exportación exitosa; `exported` lo deja abierto para su posterior procesamiento. Las versiones anteriores conservan `finished`. Una selección que falta tiene por defecto `finished`; se rechaza una selección no válida.

Si las tareas abiertas impiden la exportación, la tarjeta informa el rechazo. Resolver las tareas y organizar el desencadenante o reintento previsto; Esta tarjeta no garantiza la espera y reanudación automáticas. La tarjeta de exportación en cola independiente recopila una configuración para la exportación final al final de la ejecución. Consulte [Exportar tarjetas y estado de resultados](../../cards-overview/export-cards-guide.md).
