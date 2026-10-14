# Approve the Document



<figure><img src="../../../../.gitbook/assets/image (281).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Approve the Document"** se utiliza para marcar un documento como aprobado. Permite que el documento avance a la siguiente etapa del flujo de trabajo, posibilitando la ejecución de flujos de trabajo de procesamiento o aprobación automatizados. Esta tarjeta ayuda a agilizar los procesos de gestión de documentos, garantizando que solo los documentos aprobados avancen para acciones adicionales.

## **Componentes de la tarjeta:**

1. **Approval Status**
   * **Descripción**: Este componente marca el documento como aprobado.
   * **Detalle**: Cuando se dispara esta tarjeta, el estado de aprobación del documento se actualiza para indicar la aprobación. Esta acción se puede establecer según las condiciones definidas en las secciones **"Where"** y **"And"**.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones establecidas en las secciones **"Where"** y **"And"**.
  * Si **ambas condiciones son verdaderas**, el documento se marcará como aprobado.
  * Si **cualquiera de las condiciones es falsa**, la tarjeta no se ejecutará y el estado de aprobación del documento permanecerá sin cambios.
* **Ejecución de la acción**: Cuando se cumplen las condiciones, el documento se aprueba. Este cambio se refleja en el estado del documento, permitiéndole continuar avanzando en el flujo de trabajo.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Approve the Document"** es un componente clave para automatizar la aprobación de documentos en los flujos de trabajo de negocio. Al garantizar que solo se aprueben los documentos que cumplen criterios específicos, ayuda a mantener la coherencia, reduce la supervisión manual y posibilita un procesamiento de documentos más fluido.
