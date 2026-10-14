# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Compra Pedido Exportar 4"><figcaption></figcaption></figure>

Este título indica que la regla está configurada específicamente para gestionar facturas de coste e implica una acción de exportación, posiblemente para la generación de informes, el procesamiento posterior o la integración con otros sistemas.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición garantiza que la regla se active únicamente para los documentos clasificados como facturas, manteniendo la especificidad del flujo de trabajo en la gestión de facturas.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Esto especifica que la regla se aplica únicamente a las facturas que están marcadas explícitamente como "Cost Invoices" en un campo concreto del documento. Esto ayuda a distinguirlas de otros tipos de facturas.
   * **Document Status is Pending Second Approval**: La factura debe estar en estado "Pending Second Approval". Esto indica que la factura ya ha pasado por una aprobación inicial y está a la espera de una segunda revisión, posiblemente final.

#### Acción (Then…):

* **Start Export**: Una vez que la factura cumple las condiciones especificadas (ser una factura de coste y estar pendiente de segunda aprobación), se ejecuta la acción "Start Export". Esto podría implicar el envío de los datos de la factura a otro sistema para su análisis financiero, generación de informes o fines de cumplimiento.

#### Propósito de esta regla:

* **Workflow Efficiency**: Esta regla ayuda a automatizar el tratamiento de las facturas de coste, garantizando que se procesen a través de las fases de aprobación necesarias sin intervención manual, aumentando la velocidad y la precisión de las operaciones financieras.
* **Control and Compliance**: Al exigir una segunda aprobación, el sistema impone un mecanismo de control que garantiza que las facturas de coste se revisen exhaustivamente, mejorando la supervisión financiera.
* **Integration and Reporting**: La acción de exportación sugiere que, una vez que las facturas están totalmente aprobadas, pueden integrarse en otros sistemas para su procesamiento o análisis posterior, lo cual es fundamental para la elaboración de informes financieros y las auditorías.

Este tipo de regla es vital para las organizaciones que manejan diversos tipos de facturas y necesitan garantizar que cada tipo se gestione conforme a protocolos específicos. Reduce el riesgo de errores y garantiza el cumplimiento de los controles internos y las normativas externas.
