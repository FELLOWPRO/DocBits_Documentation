# Factura de Compra - Exportación de Cantidad de 2da Aprobación

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Compra Pedido Exportar 6"><figcaption></figcaption></figure>

Este título indica que la regla está configurada para gestionar la segunda fase de aprobación para facturas de compra con un énfasis en los detalles de cantidad, asegurando que las cantidades en la factura coincidan con las del pedido de compra original.

#### Configuración de la Regla:

1. **Cuando…**
* **El Tipo de Documento es Factura**: Esta condición asegura que la regla se active solo para documentos identificados como facturas, lo cual es crucial para dirigir el flujo de trabajo con precisión.
2. **Y…**
* **El Estado del Documento es Pendiente de 2da Aprobación**: Esto especifica que la factura está actualmente pendiente de una segunda aprobación. Esta etapa a menudo proporciona una supervisión adicional para garantizar la precisión antes de que se finalice la transacción.
* **El Subtipo de Factura es Igual a Factura de Compra**: Esta condición especifica además que la regla se aplica solo a facturas categorizadas específicamente como "Facturas de Compra", diferenciándolas de otros tipos de facturas.
* **La Cantidad Lógica en la confirmación del pedido es Igual al pedido de compra**: Esta condición verifica si la cantidad indicada en la confirmación del pedido coincide con la cantidad en el pedido de compra. Asegura que el procesamiento de la factura solo avance si las cantidades son consistentes, lo cual es crítico para la gestión de inventario y la precisión financiera.

#### Acción (Entonces…):

* **Iniciar Exportación**: Una vez que la factura cumple con las condiciones especificadas (es decir, las cantidades coinciden entre la confirmación del pedido y el pedido de compra), se activa la acción de "Iniciar Exportación". Esto probablemente implica exportar los datos de la factura para su procesamiento adicional, posiblemente a otro sistema financiero o con fines de informes.

#### Propósito de Esta Regla:

* **Garantizar Precisión y Consistencia**: Al verificar que las cantidades coincidan entre la confirmación del pedido y el pedido de compra, el sistema ayuda a mantener la precisión del inventario y evita discrepancias que podrían afectar los informes financieros o la gestión de stock.
* **Optimizar el Procesamiento Financiero**: Automatizar la exportación de datos una vez que las cantidades están confirmadas reduce la manipulación manual y acelera el ciclo de procesamiento financiero.
* **Mejorar el Cumplimiento y la Supervisión**: Requerir una segunda aprobación para la verificación de cantidades agrega una capa adicional de supervisión, crucial para el cumplimiento de políticas financieras y controles.

Esta regla es un claro ejemplo de cómo la automatización del flujo de trabajo puede utilizarse de manera efectiva para garantizar el manejo preciso y eficiente de documentos financieros dentro de una organización, especialmente en el contexto de procesos de compra que involucran grandes volúmenes de transacciones que requieren una validación meticulosa.
