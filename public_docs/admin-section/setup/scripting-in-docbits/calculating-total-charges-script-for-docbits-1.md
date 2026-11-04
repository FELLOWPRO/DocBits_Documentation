# Script de Cálculo de Cargos Totales para DocBits

##

El script "Calculando Cargos Totales" automatiza el proceso de sumar varios cargos y cantidades adicionales dentro de documentos de factura. Esta guía te lleva a través de la configuración del script, la lógica y la aplicación para garantizar cálculos precisos de cargos totales en tus documentos.

### Propósito

Este script tiene como objetivo proporcionar una forma dinámica de calcular los cargos totales en una factura sumando diferentes tipos de cargos, como cargos base, flete y embalaje. Luego actualiza el campo de cargos totales de la factura con la suma calculada, garantizando información de facturación precisa.

### Resumen del Script

El script recupera valores de campos especificados, los convierte en números decimales, los suma y luego actualiza el campo `total_charges` con el resultado. Si el campo `total_charges` no existe, el script crea este campo y establece su valor en consecuencia.

#### Fragmento de Código
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

