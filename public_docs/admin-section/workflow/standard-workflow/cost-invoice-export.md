# Factura de Costo - Exportar

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Compra Pedido Exportar 4"><figcaption></figcaption></figure>

Este título indica que la regla está configurada específicamente para gestionar facturas de costos e implica una acción de exportación, posiblemente para informes, procesamiento adicional o integración con otros sistemas.

#### Configuración de la Regla:

1. **Cuando…**
* **El Tipo de Documento es Factura**: Esta condición asegura que la regla se active solo para documentos categorizados como facturas, manteniendo la especificidad del flujo de trabajo para la gestión de facturas.
2. **Y…**
* **El Subtipo de Factura del Campo del Documento es Igual a Factura de Costo**: Esto especifica que la regla se aplica solo a aquellas facturas marcadas explícitamente como "Facturas de Costo" en un campo particular dentro del documento. Esto ayuda a distinguirlas de otros tipos de facturas.
* **El Estado del Documento es Pendiente de Segunda Aprobación**: La factura debe estar en estado de "Pendiente de Segunda Aprobación". Esto indica que la factura ya ha pasado por una aprobación inicial y está esperando una segunda revisión, posiblemente final.

#### Acción (Entonces…):

* **Iniciar Exportación**: Una vez que la factura cumple con las condiciones especificadas (ser una factura de costo y estar pendiente de segunda aprobación), se ejecuta la acción de "Iniciar Exportación". Esto podría implicar enviar los datos de la factura a otro sistema para análisis financiero, informes o fines de cumplimiento.

#### Propósito de Esta Regla:

* **Eficiencia del Flujo de Trabajo**: Esta regla ayuda a automatizar el manejo de facturas de costos al garantizar que se procesen a través de las etapas de aprobación necesarias sin intervención manual, aumentando la velocidad y precisión de las operaciones financieras.
* **Control y Cumplimiento**: Al requerir una segunda aprobación, el sistema aplica un mecanismo de control que garantiza que las facturas de costos se revisen a fondo, mejorando la supervisión financiera.
* **Integración e Informes**: La acción de exportación sugiere que una vez que las facturas estén completamente aprobadas, pueden integrarse en otros sistemas para procesamiento o análisis adicional, lo cual es fundamental para informes financieros y auditorías.

Este tipo de regla es vital para organizaciones que manejan varios tipos de facturas y necesitan garantizar que cada tipo se maneje según protocolos específicos. Reduce el riesgo de errores y asegura el cumplimiento con controles internos y regulaciones externas.
