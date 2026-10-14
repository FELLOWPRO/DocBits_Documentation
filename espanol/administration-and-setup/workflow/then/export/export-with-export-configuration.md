# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Export Document with Export Configuration"** está diseñada para exportar un documento usando una configuración de exportación especificada. Proporciona la flexibilidad de ignorar cualquier tarea pendiente asociada al documento, garantizando un proceso de exportación fluido independientemente de su estado actual.

## **Componentes de la tarjeta:**

1. **Export Configuration**
   * **Descripción**: Especifica la configuración de exportación que se utilizará para procesar el documento.
   * **Detalle**: Esta configuración determina el formato, la estructura y el destino del documento exportado.
2. **Ignore Pending Tasks**
   * **Descripción**: Determina si las tareas pendientes vinculadas al documento deben ignorarse durante el proceso de exportación.
   * **Opciones**:
     * **True**: Exporta el documento independientemente de las tareas pendientes.
     * **False**: Garantiza que las tareas pendientes se completen antes de la exportación.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones establecidas en las secciones **"Where"** y **"And"** del flujo de trabajo. Si ambas condiciones son verdaderas, se inicia el proceso de exportación.
* **Exportación del documento**: Usando la **Export Configuration** especificada, el documento se procesa y se exporta en el formato y destino definidos.
* **Gestión de tareas pendientes**: Si **Ignore Pending Tasks** se establece en **True**, el proceso de exportación omite cualquier tarea pendiente vinculada al documento. Si se establece en **False**, la exportación se pospone hasta que todas las tareas se resuelvan.

## **Configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. Seleccionar la **Export Configuration** deseada para definir cómo se exportará el documento.
2. Elegir si **Ignore Pending Tasks** estableciendo el valor en **True** o **False**.
3. Asegurarse de que las condiciones de las secciones **"Where"** y **"And"** estén configuradas correctamente, ya que la tarjeta solo ejecuta su acción cuando estas condiciones son verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Export Document with Export Configuration"** garantiza que los documentos se exporten de forma eficiente y según configuraciones predefinidas. Con la capacidad de ignorar las tareas pendientes, esta tarjeta ofrece flexibilidad en el manejo de documentos en diversas etapas, reduciendo los retrasos y agilizando el proceso de exportación.
