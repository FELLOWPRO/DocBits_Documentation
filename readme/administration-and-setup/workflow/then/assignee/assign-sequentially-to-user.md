# Assign Sequentially to User

<figure><img src="../../../../.gitbook/assets/image (9) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo "**Assign Sequentially to User**" automatiza la asignación de documentos a un usuario seleccionado de forma secuencial. El valor de prioridad determina el orden de asignación, donde los números más bajos representan una mayor prioridad.

## **Componentes de la tarjeta**

1. **User**
   * **Descripción**: Al usuario seleccionado se le asignará el documento según la secuencia del flujo de trabajo.
   * **Detalle**: Un menú desplegable que enumera todos los usuarios disponibles para la asignación.
2. **Priority (Value)**
   * **Descripción**: Un campo de entrada numérico donde se puede establecer el nivel de prioridad del usuario.
   * **Detalle**: Los números más bajos indican una mayor prioridad. Los documentos se asignan a los usuarios en orden ascendente de prioridad.

## **Funcionalidad**

* **Asignación del documento**:\
  La tarjeta asigna los documentos al usuario seleccionado de forma secuencial, teniendo en cuenta el nivel de prioridad.\
  Si varios usuarios tienen la misma prioridad, los documentos se asignan en el orden en que aparecen los usuarios en el menú desplegable.

## **Configuración**

1. Añada la tarjeta **Assign the Document Sequentially** a su flujo de trabajo.
2. Configure el campo **User**:
   * Seleccione un usuario del menú desplegable.
3. Configure el campo **Priority (Value)**:
   * Introduzca un valor numérico para establecer la prioridad de asignación.
4. Guarde y active el flujo de trabajo para aplicar la configuración.

## **Conclusión**

La tarjeta de flujo de trabajo "Assign the Document Sequentially to User" garantiza una distribución organizada de los documentos al asignarlos en una secuencia priorizada. Esto mejora la gestión de tareas y reduce los retrasos en el procesamiento.
