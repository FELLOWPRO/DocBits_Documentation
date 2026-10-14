# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Compra Pedido Exportar 5"><figcaption></figcaption></figure>

Este título indica que la regla está configurada para gestionar la segunda fase de aprobación de las facturas de compra, con énfasis en el precio unitario, garantizando que coincida con los términos acordados.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición garantiza que la regla se active únicamente para los documentos identificados como facturas, lo cual es crucial para dirigir el flujo de trabajo con precisión.
2. **And…**
   * **Document Status is Pending Second Approval**: Esto especifica que la factura está a la espera de una segunda aprobación. Esta fase suele proporcionar una supervisión adicional para garantizar la exactitud antes de finalizar la transacción.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Esta condición especifica además que la regla se aplica únicamente a las facturas clasificadas específicamente como "Purchase Invoices", diferenciándolas de otros tipos de facturas.
   * **Logic Unit Price in order confirmation Equals purchase order**: Esta condición comprueba si el precio unitario indicado en la confirmación del pedido coincide con el precio unitario del pedido de compra. Garantiza que el procesamiento de la factura solo avance si hay coherencia en los precios, lo cual es fundamental para la elaboración de presupuestos y la generación de informes financieros.

#### Acción (Then…):

* **Start Export**: Una vez que la factura cumple las condiciones especificadas (es decir, los precios unitarios coinciden entre la confirmación del pedido y el pedido de compra), se activa la acción "Start Export". Esto probablemente implica exportar los datos de la factura para su procesamiento posterior, posiblemente a otro sistema financiero o con fines de generación de informes.

#### Propósito de esta regla:

* **Ensure Accuracy and Consistency**: Al verificar que los precios unitarios coinciden entre la confirmación del pedido y el pedido de compra, el sistema ayuda a mantener la exactitud financiera y evita cobros excesivos o insuficientes.
* **Streamline Financial Processing**: La automatización de la exportación de datos una vez confirmados los precios reduce el tratamiento manual y acelera el ciclo de procesamiento financiero.
* **Enhance Compliance and Oversight**: Exigir una segunda aprobación para la verificación de precios añade una capa adicional de supervisión, lo cual es crucial para el cumplimiento de las políticas y controles financieros.

Esta regla es un ejemplo de cómo la automatización de flujos de trabajo puede utilizarse eficazmente para garantizar un tratamiento preciso y eficiente de los documentos financieros dentro de una organización, especialmente en el contexto de grandes volúmenes de transacciones que requieren una validación meticulosa.
