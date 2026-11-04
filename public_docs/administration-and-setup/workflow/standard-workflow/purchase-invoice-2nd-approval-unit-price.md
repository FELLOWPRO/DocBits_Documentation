# Factura de compra: segunda aprobación del precio unitario

Este ejemplo dirige una discrepancia de precio unitario a una revisión adicional. Las condiciones y los nombres de campos que aparecen a continuación pertenecen a la configuración descrita; no establecen valores predeterminados para todas las organizaciones.

## Condiciones de la regla

* **Document Type is Invoice:** limita el ejemplo al tipo de documento de factura configurado.
* **Document Status is Pending Second Approval:** exige el estado de segunda aprobación de este flujo.
* **Document Field Invoice Sub Type is Equals Purchase Invoice:** comprueba el subtipo de factura de compra configurado.
* **Logic Unit Price in order confirmation Not Equals purchase order:** compara el precio unitario de la confirmación con el del pedido de compra, según las referencias y la lógica de la regla.

Son referencias a la regla del ejemplo. Antes de reproducirla, compruebe los nombres técnicos, los estados, las tolerancias y la disponibilidad de los datos en su entorno. La comparación de precios no demuestra por sí sola que el documento esté aprobado o que todas sus condiciones comerciales sean correctas.

## Acción de asignación

**Assign user from field Buyer Name, use user User as fallback** intenta resolver al responsable a partir del campo **Buyer Name** y utiliza el usuario alternativo que se haya configurado. **User** representa la selección de este ejemplo; no significa que DocBits elija automáticamente un administrador predeterminado.

Configure un destinatario principal y un respaldo válidos, con los permisos necesarios. Pruebe ambas rutas y compruebe la asignación almacenada y los registros. Si no puede resolverse ningún usuario autorizado, corrija la configuración antes de confiar en la automatización.

## Propósito de la revisión

La regla ayuda a dirigir las discrepancias al personal responsable para que revise el precio. La asignación no constituye una aprobación, un control de fraude completo, un pago ni una exportación. El resultado depende de la configuración y de los datos disponibles.
