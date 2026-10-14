# Script de Calculo de Cargos Totales para DocBits

El script "Calculating Total Charges" automatiza el proceso de sumar varios cargos y montos adicionales dentro de documentos de factura. Esta guia le explica la configuracion, logica y aplicacion del script para garantizar calculos precisos de cargos totales en sus documentos.

### Proposito

Este script tiene como objetivo proporcionar una forma dinamica de calcular los cargos totales en una factura sumando diferentes tipos de cargos, como cargos base, flete (Fracht) y embalaje (Verpackung). Luego actualiza el campo de cargos totales de la factura con la suma calculada, asegurando informacion de facturacion precisa.

### Descripcion del Script

El script recupera valores de campos especificados, los convierte a numeros de punto flotante, los suma y luego actualiza el campo `total_charges` con el resultado. Si el campo `total_charges` no existe, el script crea este campo y establece su valor en consecuencia.

#### Fragmento de Codigo

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Inicializar total en 0
total = 0

# Agregar flete al total si existe
if fracht:
    fracht = float(fracht)
    total += fracht

# Agregar embalaje al total si existe
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatear el total a dos decimales
formatted_total = "{0:.2f}".format(total)

# Verificar si el campo total_charges existe y actualizar o crear segun corresponda
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
