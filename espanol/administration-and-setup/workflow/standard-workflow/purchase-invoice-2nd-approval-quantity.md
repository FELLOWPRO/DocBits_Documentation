# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Aprobación Factura 4"><figcaption></figcaption></figure>

Este título indica que la regla se refiere específicamente al tratamiento de las facturas de compra durante una fase de aprobación secundaria, con énfasis en la verificación de la exactitud de las cantidades indicadas.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición garantiza que la regla se active únicamente para los documentos clasificados como facturas. Esto es esencial para mantener la especificidad y la relevancia en el flujo de trabajo.
2. **And…**
   * **Document Status is Pending Second Approval**: Esto especifica que la factura está actualmente pendiente de una segunda aprobación. Esta fase suele estar destinada a proporcionar una supervisión adicional antes de finalizar la factura.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Esta condición refina aún más la regla para que se aplique exclusivamente a las facturas identificadas como "Purchase Invoices". Esta categorización ayuda a diferenciarlas de otros tipos de facturas.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Esta condición crítica comprueba si la cantidad indicada en la confirmación del pedido coincide con la cantidad del pedido de compra original. La acción se activa si hay una discrepancia, lo que indica un posible error o problema que requiere resolución.

#### Acción (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Si se cumplen las condiciones de la regla (es decir, hay una discrepancia en las cantidades), la factura se asigna automáticamente a la persona indicada en el campo 'Buyer Name' para su revisión adicional. Si este campo está vacío o la persona especificada no está disponible, un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) se hace cargo para garantizar una revisión y resolución oportunas.

#### Propósito de esta regla:

* **Accuracy and Compliance**: La regla es vital para garantizar que el proceso de facturación sea preciso y se ajuste a los términos acordados en el pedido de compra. Ayuda a prevenir discrepancias financieras y posibles errores de inventario.
* **Streamlined Approvals**: La automatización del proceso de revisión para discrepancias específicas ayuda a agilizar las aprobaciones y garantiza que cualquier problema sea abordado rápidamente por el personal adecuado.
* **Enhanced Financial Oversight**: Exigir una aprobación secundaria para las verificaciones de cantidad refuerza los controles financieros y la rendición de cuentas dentro de la organización.

Esta configuración ejemplifica cómo la automatización de flujos de trabajo puede utilizarse para mejorar la eficiencia operativa y garantizar la integridad financiera, especialmente en la gestión de procesos de compra complejos dentro de una empresa.
