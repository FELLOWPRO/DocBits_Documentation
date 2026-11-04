# Condición de Estado de Documento Único

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Esta tarjeta de flujo de trabajo está diseñada para gestionar operaciones en documentos basadas en un único estado de documento especificado. Al simplificar la condición a un solo estado, la tarjeta se enfoca en desencadenantes de flujo de trabajo muy específicos, lo que la hace ideal para actividades de procesamiento de documentos dirigidas dentro de un sistema ERP.

**Componentes de la Tarjeta**

1. **Operador**
* **Descripción**: Especifica el método para evaluar el estado del documento frente a la condición seleccionada.
* **Opciones**:
* **es**: Activa la operación si el estado actual del documento coincide con el estado seleccionado.
* **no es**: Activa la operación si el estado actual del documento no coincide con el estado seleccionado.
2. **Estado**
* **Descripción**: Permite la selección de un único estado de documento para establecer la condición.
* **Ejemplos de Estados**: "Error", "Error de Exportación", "Listo en Validación", "Listo en Revisión", "Aprobación Pendiente", "Segunda Aprobación Pendiente".
* **Detalle**: Los usuarios eligen un estado de un menú desplegable o un conjunto de botones de radio. Este estado luego sirve como criterio para la operación de la tarjeta.

**Funcionalidad**

* **Identificación del Estado del Documento**: Identifica el estado actual de un documento mientras se procesa a través del sistema ERP.
* **Evaluación de la Condición**:
* Basado en el operador seleccionado (`es` o `no es`), la tarjeta verifica si el estado actual del documento coincide con el criterio de estado elegido.
* **Ejecución de la Acción**:
* **Condición Verdadera**: Si el estado coincide (o no coincide, según el operador), se inicia la acción correspondiente. Esto podría ser enrutamiento para un procesamiento adicional, generación de notificaciones u otros flujos de trabajo predefinidos.
* **Condición Falsa**: Si la condición no se cumple, no se realiza ninguna acción o se activa un camino alternativo.
* **Integración con Otros Flujos de Trabajo**: Aunque está diseñada para evaluación de un solo estado, esta tarjeta se puede integrar eficazmente en secuencias de flujos de trabajo más amplias para garantizar un manejo preciso de documentos.

**Interacciones del Usuario**

* **Configuración e Instalación**: Los usuarios configuran la tarjeta seleccionando un operador y luego eligiendo un estado de las opciones disponibles. Este proceso de selección es sencillo y está diseñado para evitar confusiones.
* **Monitoreo e Informes**: Permite el monitoreo a través de informes generados por el sistema o paneles que rastrean el procesamiento de documentos según su estado, ayudando a supervisar la efectividad de los flujos de trabajo implementados.
* **Manejo de Errores y Notificaciones**: Configurable para alertar a los usuarios sobre anomalías en el procesamiento o para marcar documentos que no cumplen con las condiciones establecidas, asegurando una atención y resolución rápidas.

#### Conclusión

La tarjeta de flujo de trabajo "Condición de Estado de Documento Único" simplifica la gestión de documentos al centrarse en condiciones de estado individuales. Esta especificación ayuda en casos donde se requiere un control preciso sobre los flujos de documentos, especialmente en entornos con criterios de procesamiento estrictos. Documentar claramente esta versión de la tarjeta garantizará que los usuarios comprendan completamente su aplicación y puedan integrarla de manera efectiva en sus operaciones diarias, mejorando tanto la conformidad como la eficiencia en el procesamiento de documentos.
