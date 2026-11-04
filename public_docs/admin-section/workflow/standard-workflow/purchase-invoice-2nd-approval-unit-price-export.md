# Factura de Compra - Exportación de Precio Unitario de 2da Aprobación

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Compra Pedido Exportar 5"><figcaption></figcaption></figure>

Este título indica que la regla está configurada para gestionar la segunda fase de aprobación de facturas de compra con un enfoque en el precio unitario, asegurando que coincida con los términos acordados.

#### Configuración de la Regla:

1. **Cuando…**
* **El Tipo de Documento es Factura**: Esta condición asegura que la regla se active solo para documentos identificados como facturas, lo cual es crucial para dirigir el flujo de trabajo con precisión.
2. **Y…**
* **El Estado del Documento es Pendiente de Segunda Aprobación**: Esto especifica que la factura está esperando una segunda aprobación. Esta etapa a menudo proporciona una supervisión adicional para garantizar la precisión antes de finalizar la transacción.
* **El Subtipo de Factura es Igual a Factura de Compra**: Esta condición especifica que la regla se aplica solo a facturas categorizadas específicamente como "Facturas de Compra", diferenciándolas de otros tipos de facturas.
* **La Lógica del Precio Unitario en la confirmación del pedido es Igual a la orden de compra**: Esta condición verifica si el precio unitario listado en la confirmación del pedido coincide con el precio unitario en la orden de compra. Asegura que el procesamiento de la factura solo avance si hay consistencia en los precios, lo cual es fundamental para la presupuestación y la presentación de informes financieros.

#### Acción (Entonces…):

* **Iniciar Exportación**: Una vez que la factura cumple con las condiciones especificadas (es decir, los precios unitarios coinciden entre la confirmación del pedido y la orden de compra), se activa la acción de "Iniciar Exportación". Esto probablemente implica exportar los datos de la factura para su procesamiento adicional, posiblemente a otro sistema financiero o con fines de informes.

#### Propósito de Esta Regla:

* **Garantizar Precisión y Consistencia**: Al verificar que los precios unitarios coinciden entre la confirmación del pedido y la orden de compra, el sistema ayuda a mantener la precisión financiera y evita el cobro excesivo o insuficiente.
* **Optimizar el Procesamiento Financiero**: Automatizar la exportación de datos una vez que los precios están confirmados reduce la manipulación manual y acelera el ciclo de procesamiento financiero.
* **Mejorar el Cumplimiento y la Supervisión**: Requerir una segunda aprobación para la verificación de precios agrega una capa adicional de supervisión, lo cual es crucial para el cumplimiento de políticas y controles financieros.

Esta regla es un ejemplo de cómo la automatización del flujo de trabajo puede utilizarse de manera efectiva para garantizar el manejo preciso y eficiente de documentos financieros dentro de una organización, especialmente en el contexto de grandes volúmenes de transacciones que requieren una validación meticulosa.
