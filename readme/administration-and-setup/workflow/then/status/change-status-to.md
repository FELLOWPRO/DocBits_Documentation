# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Change Status"** se utiliza para cambiar el estado de un documento a uno de los estados predefinidos —**Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval**— y, opcionalmente, disparar flujos de trabajo asociados según el cambio de estado. Esta tarjeta automatiza el proceso de actualización de estados y disparadores de flujo de trabajo, garantizando una gestión eficiente de documentos y un manejo de errores.

## **Componentes de la tarjeta:**

1. **Status**
   * **Descripción**: Especifica el nuevo estado que se aplicará al documento.
   * **Opciones**:
     * **Error**: Marca el documento como que ha encontrado un error.
     * **Rejected**: Indica que el documento ha sido rechazado y no continuará.
     * **Ready for Validation**: Establece el documento para que sea revisado y validado por el siguiente usuario o proceso del sistema.
     * **Pending Approval**: Coloca el documento en estado pendiente de aprobación.
     * **Pending Second Approval**: Pone el documento en espera de un segundo nivel de aprobación si procede.
2. **Trigger Workflows**
   * **Descripción**: Determina si deben dispararse flujos de trabajo posteriores tras el cambio de estado.
   * **Opciones**:
     * **True**: Inicia los flujos de trabajo pertinentes según el cambio de estado.
     * **False**: Impide la ejecución de flujos de trabajo tras el cambio de estado.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones establecidas en las secciones **"Where"** y **"And"**. Si estas condiciones son verdaderas, la tarjeta continúa para cambiar el estado del documento al valor seleccionado.
* **Actualización del estado**: Una vez que se cumplen las condiciones, el estado del documento se actualiza a una de las opciones predefinidas (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), según la selección del usuario.
* **Acción de disparar el flujo de trabajo**: Si **Trigger Workflows** se establece en **True**, el sistema inicia automáticamente cualquier flujo de trabajo asociado tras la actualización del estado. Si se establece en **False**, no se disparan flujos de trabajo adicionales y el proceso finaliza con el cambio de estado.

## **Configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. Especificar el **Status** deseado al que se establecerá el documento tras la evaluación de la condición (Error, Rejected, Ready for Validation, Pending Approval o Pending Second Approval).
2. Elegir si **Trigger Workflows** tras el cambio de estado seleccionando **True** o **False**.
3. La tarjeta solo ejecuta su acción si ambas condiciones de las secciones **"Where"** y **"And"** se evalúan como verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Change Status"** ofrece un enfoque ágil para gestionar los estados de los documentos y disparar flujos de trabajo relacionados. Garantiza que los documentos se enruten automáticamente al estado correcto y que se tomen las acciones necesarias, según el cambio de estado. Al establecer condiciones claras para la ejecución, reduce el esfuerzo manual y mejora la eficiencia del flujo de trabajo.
