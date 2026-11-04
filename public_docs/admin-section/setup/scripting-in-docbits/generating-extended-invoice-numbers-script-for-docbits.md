# Generación de Script de Números de Factura Extendidos para Docbits

### Visión general

Esta guía se centra en automatizar la creación de números de factura extendidos en Docbits, una característica crucial para mejorar la gestión y seguimiento de facturas. El script "Generación de Números de Factura Extendidos" concatena varios identificadores de documentos, como el ID de factura y el número de orden de compra, para crear un identificador completo y único para cada factura.

### Objetivo

El objetivo principal de este script es automatizar la generación de números de factura extendidos, facilitando el seguimiento y la gestión de facturas al combinar múltiples identificadores en un número único y completo.

### Implementación del Script

#### Fragmento de código
```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
if 'invoice_extended_number' not in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

