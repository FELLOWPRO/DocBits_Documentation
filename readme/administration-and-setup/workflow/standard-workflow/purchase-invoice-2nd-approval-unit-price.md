# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Aprobación Factura 3"><figcaption></figcaption></figure>

Este título indica que la regla está configurada para gestionar la segunda fase de aprobación de una factura de compra, con un enfoque específico en la validación del precio unitario.

#### Configuración de la regla:

1. **When…**
   * **Document Type is Invoice**: Esta condición garantiza que la regla se active únicamente para los documentos identificados como facturas, filtrando otros tipos de documentos y manteniendo la relevancia del flujo de trabajo.
2. **And…**
   * **Document Status is Pending Second Approval**: Esto especifica que la factura se encuentra en la fase en la que está a la espera de una segunda aprobación. Suele ser un paso diseñado para garantizar una supervisión adicional antes del procesamiento final.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Esto restringe aún más la aplicación de esta regla únicamente a las facturas clasificadas como "Purchase Invoices", distinguiéndolas de otros subtipos de facturas.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Esta comprobación lógica es crucial, ya que compara el precio unitario indicado en la confirmación del pedido con el precio unitario del pedido de compra original. La acción se activa si estos valores no coinciden, lo que podría indicar una discrepancia que requiere resolución.

#### Acción (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Si se cumplen las condiciones especificadas (es decir, hay una discrepancia en los precios unitarios), la factura se asigna automáticamente a un comprador (el nombre especificado en el campo 'Buyer Name') para su revisión adicional. Si el campo 'Buyer Name' está vacío o no se especifica, se asigna un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para gestionar la aprobación.

#### Propósito de esta regla:

* **Ensure Accuracy and Compliance**: Esta regla es fundamental para garantizar que el proceso de facturación sea preciso y cumpla con los términos acordados. Al activar una revisión cuando hay una discrepancia en los precios unitarios, el sistema ayuda a prevenir errores financieros o posibles fraudes.
* **Streamline Approvals**: La automatización de la asignación para revisión basada en discrepancias específicas ayuda a agilizar el proceso de aprobación y garantiza que los problemas sean abordados rápidamente por el personal adecuado.
* **Financial Oversight**: Exigir una segunda aprobación, especialmente basada en la coincidencia de precios, refuerza los controles financieros y la rendición de cuentas dentro de la organización.
