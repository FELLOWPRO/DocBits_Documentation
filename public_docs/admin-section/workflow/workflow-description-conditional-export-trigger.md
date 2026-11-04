# Ejemplo de Flujo de Trabajo: Disparador de Exportación Condicional



<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_7.png" alt="DocBits Flujo de trabajo Compra Pedido 7"><figcaption></figcaption></figure>

Este flujo de trabajo describe las condiciones bajo las cuales se debe iniciar un proceso de exportación. Asegura que solo los documentos que cumplen con todos los criterios especificados sean procesados para la exportación, mejorando la integridad de los datos y la alineación con las reglas comerciales.

### Cuándo:

* Se evalúa la elegibilidad de un documento dentro del sistema para la exportación.

### Lógica:

1. **Verificación del Tipo de Documento**
* El documento debe ser de un cierto tipo (por ejemplo, "Factura" o "Recibo"). Especifique el tipo de documento que califica para el proceso de exportación.
2. **Verificación del Estado**
* El estado actual del documento debe cumplir con criterios predefinidos (por ejemplo, "Aprobado" o "Listo para Exportar"), lo que indica que está listo para ser procesado más adelante.
3. **Condiciones Contextuales**
* Se realizan verificaciones adicionales para asegurar que los detalles del documento se alineen con requisitos específicos. Estas verificaciones pueden implicar verificar información dentro de confirmaciones de pedidos u órdenes de compra. Especifique las condiciones particulares que deben cumplirse. Por ejemplo:
* Todos los elementos enumerados en la confirmación del pedido coinciden con los de la orden de compra.
* El monto total en la confirmación del pedido coincide con el monto total en la orden de compra.
* Las fechas de entrega especificadas en la confirmación del pedido se alinean con las de la orden de compra.

### Entonces:

#### Acción:

* **Iniciar Exportación**
* Si se cumplen todas las condiciones anteriores, el sistema inicia automáticamente el proceso de exportación para el documento.
* Esto puede implicar generar un archivo de exportación, enviar datos a un sistema externo o activar un flujo de trabajo en otra aplicación.

#### Ejemplo de Implementación:
```yaml
rules:
- description: "Conditional Export Trigger"
conditions:
- type: "DocumentType"
criteria: "<SpecifyDocumentType>"
- type: "Status"
criteria: "<SpecifyStatus>"
- type: "DetailMatch"
criteria:
- "ItemMatch"
- "AmountMatch"
- "DateMatch"
actions:
- operation: "StartExport"
```

