# Factura de Compra - Cantidad de 2da Aprobación

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Aprobación Factura 4"><figcaption></figcaption></figure>

Este título indica que la regla se refiere específicamente al manejo de facturas de compra durante una fase de aprobación secundaria, con un enfoque en verificar la precisión de las cantidades listadas.

#### Configuración de la Regla:

1. **Cuando…**
* **Tipo de Documento es Factura**: Esta condición asegura que la regla se active solo para documentos clasificados como facturas. Esto es esencial para mantener especificidad y relevancia en el flujo de trabajo.
2. **Y…**
* **Estado del Documento es Pendiente de 2da Aprobación**: Esto especifica que la factura está actualmente pendiente de una segunda aprobación. Esta etapa generalmente está destinada a proporcionar una supervisión adicional antes de finalizar la factura.
* **Subtipo de Factura es Igual a Factura de Compra**: Esta condición refina aún más la regla para aplicarse exclusivamente a facturas identificadas como "Facturas de Compra". Esta categorización ayuda a diferenciarlas de otros tipos de facturas.
* **Lógica Cantidad en confirmación de pedido No es Igual a orden de compra**: Esta condición crítica verifica si la cantidad indicada en la confirmación del pedido coincide con la cantidad en la orden de compra original. La acción se activa si hay una discrepancia, lo que indica un posible error o problema que necesita resolución.

#### Acción (Entonces…):

* **Asignar usuario del campo Nombre del Comprador, usar usuario Usuario como alternativa**: Si se cumplen las condiciones de la regla (es decir, hay una discrepancia en las cantidades), la factura se asigna automáticamente a la persona indicada en el campo 'Nombre del Comprador' para una revisión adicional. Si este campo está vacío o la persona especificada no está disponible, un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) se encarga de garantizar una revisión y resolución oportuna.

#### Propósito de Esta Regla:

* **Precisión y Cumplimiento**: La regla es vital para garantizar que el proceso de facturación sea preciso y se alinee con los términos acordados en la orden de compra. Ayuda a prevenir discrepancias financieras y posibles errores de inventario.
* **Aprobaciones Simplificadas**: Automatizar el proceso de revisión para discrepancias específicas ayuda a simplificar las aprobaciones y garantiza que cualquier problema sea abordado rápidamente por el personal adecuado.
* **Supervisión Financiera Mejorada**: Requerir una segunda aprobación para verificaciones de cantidad fortalece los controles financieros y la responsabilidad dentro de la organización.

Esta configuración ejemplifica cómo la automatización del flujo de trabajo puede utilizarse para mejorar la eficiencia operativa y garantizar la integridad financiera, especialmente en la gestión de procesos de compra complejos dentro de una empresa.
