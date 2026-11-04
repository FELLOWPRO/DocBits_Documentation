# Script de Cálculo de Cargos Totales para Docbits

### Introducción

Este documento proporciona una guía detallada sobre el script "Cálculo de Cargos Totales" dentro de la plataforma Docbits. El script está diseñado para calcular automáticamente el monto total cobrado en una factura sumando varios cargos individuales. Esta automatización mejora la precisión y eficiencia en el procesamiento de documentos.

### Objetivo

El objetivo de este script es agilizar el proceso de cálculo de cargos totales en las facturas. Al sumar automáticamente cargos especificados, como cargos base, impuestos y tarifas adicionales, el script garantiza que los cargos totales reflejados en cada factura sean precisos y completos.

### Detalles del Script

#### Implementación del Código
```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
total += float(fracht)
if verpackung:
total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

