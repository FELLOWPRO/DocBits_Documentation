# Factura de Compra - 2da Aprobación Precio Unitario

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Aprobación Factura 3"><figcaption></figcaption></figure>

Este título indica que la regla está configurada para gestionar la segunda fase de aprobación de una factura de compra, con un enfoque específico en validar el precio unitario.

#### Configuración de la Regla:

1. **Cuando…**
* **Tipo de Documento es Factura**: Esta condición asegura que la regla se active solo para documentos identificados como facturas, filtrando otros tipos de documentos y manteniendo la relevancia del flujo de trabajo.
2. **Y…**
* **Estado del Documento es Pendiente de Segunda Aprobación**: Esto especifica que la factura se encuentra en la fase donde está esperando una segunda aprobación. Este suele ser un paso diseñado para garantizar una supervisión adicional antes del procesamiento final.
* **Tipo de Factura del Campo del Documento es Igual a Factura de Compra**: Esto limita aún más la aplicación de esta regla solo a aquellas facturas clasificadas como "Facturas de Compra", distinguiéndolas de otros subtipos de facturas.
* **Lógica Precio Unitario en confirmación de pedido No es Igual a orden de compra**: Esta verificación lógica es crucial ya que compara el precio unitario indicado en la confirmación del pedido con el precio unitario en la orden de compra original. La acción se activa si estos valores no coinciden, lo que podría indicar una discrepancia que necesita resolverse.

#### Acción (Entonces…):

* **Asignar usuario del campo Nombre del Comprador, usar usuario Usuario como alternativa**: Si se cumplen las condiciones especificadas (es decir, hay una discrepancia en los precios unitarios), la factura se asigna automáticamente a un comprador (el nombre especificado en el campo 'Nombre del Comprador') para una revisión adicional. Si el campo 'Nombre del Comprador' está vacío o no especificado, se asigna un usuario predeterminado (probablemente un administrador u otro miembro del personal designado) como alternativa para manejar la aprobación.

#### Propósito de Esta Regla:

* **Garantizar Precisión y Cumplimiento**: Esta regla es crucial para asegurar que el proceso de facturación sea preciso y cumpla con los términos acordados. Al activar una revisión cuando hay una discrepancia en los precios unitarios, el sistema ayuda a prevenir errores financieros o posibles fraudes.
* **Agilizar Aprobaciones**: Automatizar la asignación para revisión basada en discrepancias específicas ayuda a agilizar el proceso de aprobación y garantiza que los problemas sean abordados rápidamente por el personal adecuado.
* **Supervisión Financiera**: Requerir una segunda aprobación, especialmente basada en la coincidencia de precios, refuerza los controles financieros y la responsabilidad dentro de la organización.
