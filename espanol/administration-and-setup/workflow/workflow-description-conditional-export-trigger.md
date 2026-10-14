# Workflow Description: Conditional Export Trigger



<figure><img src="../../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Configuración Flujo de trabajo"><figcaption></figcaption></figure>

Este flujo de trabajo describe las condiciones bajo las cuales debe iniciarse un proceso de exportación. Garantiza que solo los documentos que cumplen todos los criterios especificados se procesen para su exportación, mejorando la integridad de los datos y la alineación con las reglas de negocio.

### When:

* Un documento dentro del sistema se evalúa para determinar su elegibilidad para la exportación.

### Logic:

1. **Document Type Check**
   * El documento debe ser de un tipo determinado (por ejemplo, "Invoice" o "Receipt"). Especifique el tipo de documento que califica para el proceso de exportación.
2. **Status Verification**
   * El estado actual del documento debe cumplir criterios predefinidos (por ejemplo, "Approved" o "Ready for Export") que indiquen que está listo para su procesamiento posterior.
3. **Contextual Conditions**
   * Se realizan comprobaciones adicionales para garantizar que los detalles del documento se ajusten a requisitos específicos. Estas comprobaciones pueden implicar la verificación de información en las confirmaciones de pedidos o los pedidos de compra. Especifique las condiciones concretas que deben cumplirse. Por ejemplo:
     * Todos los artículos indicados en la confirmación del pedido coinciden con los del pedido de compra.
     * El importe total de la confirmación del pedido coincide con el importe total del pedido de compra.
     * Las fechas de entrega especificadas en la confirmación del pedido se ajustan a las del pedido de compra.

### Then:

#### Action:

* **Initiate Export**
  * Si se cumplen todas las condiciones anteriores, el sistema inicia automáticamente el proceso de exportación del documento.
  * Esto puede implicar la generación de un archivo de exportación, el envío de datos a un sistema externo o la activación de un flujo de trabajo en otra aplicación.

#### Implementation Example:

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
