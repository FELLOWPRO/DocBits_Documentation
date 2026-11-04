# Generación de Script de Números de Factura Extendidos para Docbits

Este documento detalla el script "Generación de Números de Factura Extendidos", el cual automatiza la creación de números de factura extendidos en Docbits. Los números de factura extendidos combinan múltiples identificadores de documentos, como el ID de factura y el número de orden de compra, en un identificador único y completo. Este script mejora la trazabilidad de documentos y simplifica el mantenimiento de registros.

### Propósito

El propósito de este script es agilizar el proceso de generación de números de factura extendidos al concatenar automáticamente el ID de factura y el número de orden de compra, proporcionando así un identificador unificado y único para cada documento de factura.

### Resumen del Script

El script verifica la presencia de los campos de ID de factura y número de orden de compra dentro del documento, concatena sus valores si ambos están presentes (separados por un guion), y actualiza o crea un nuevo campo para almacenar el valor combinado.

#### Fragmento de Código
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

