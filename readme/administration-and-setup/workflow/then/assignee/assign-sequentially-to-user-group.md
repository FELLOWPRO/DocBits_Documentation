# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo "**Assign the Document Sequentially to User/Group Based on Decision Table**" asigna dinámicamente documentos a un usuario o a un grupo, según la evaluación de la tabla de decisión. Esto garantiza que los documentos se enruten de forma adecuada según reglas predefinidas.

## **Componentes de la tarjeta**

1. **Priority (Value)**
   * **Descripción**: Especifica el nivel de prioridad de las asignaciones, donde los números más bajos representan una mayor prioridad.
   * **Detalle**: Un campo de entrada numérico donde se puede establecer el valor de prioridad para controlar la secuencia de asignación.

## **Funcionalidad**

* **Evaluación de la tabla de decisión**:\
  La tabla de decisión evalúa condiciones predefinidas para decidir si el documento se asigna a un usuario o a un grupo.
* **Asignación del documento**:
  * Si la tabla de decisión devuelve un usuario, el documento se asigna directamente a ese usuario.
  * Si la tabla de decisión devuelve un grupo, el documento se asigna al grupo de forma secuencial, respetando el valor de prioridad especificado.

## **Configuración**

1. Añada la tarjeta **Assign the Document Sequentially** a su flujo de trabajo.
2. Configure el campo **Priority (Value)**:
   * Introduzca un valor numérico para establecer la prioridad de asignación.
3. Guarde y active el flujo de trabajo para aplicar la configuración.

## **Conclusión**

La tarjeta de flujo de trabajo "**Assign the Document Sequentially to User/Group Based on Decision Table**" garantiza un enrutamiento de documentos eficiente y dinámico. Al aprovechar la lógica de la tabla de decisión y los valores de prioridad, la tarjeta facilita una asignación precisa a un usuario o a un grupo, agilizando los flujos de trabajo de documentos.
