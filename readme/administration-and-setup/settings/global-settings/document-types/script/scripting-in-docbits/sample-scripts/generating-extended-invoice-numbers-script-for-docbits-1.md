# Script de Generacion de Numeros de Factura Extendidos para DocBits

Este documento detalla el script "Generating Extended Invoice Numbers", que automatiza la creacion de numeros de factura extendidos en DocBits. Los numeros de factura extendidos combinan multiples identificadores de documentos, como el ID de factura y el numero de orden de compra, en un solo identificador completo. Este script mejora la trazabilidad de documentos y simplifica el mantenimiento de registros.

### Proposito

El proposito de este script es optimizar el proceso de generacion de numeros de factura extendidos concatenando automaticamente el ID de factura y el numero de orden de compra, proporcionando asi un identificador unificado y unico para cada documento de factura.

### Descripcion del Script

El script verifica la presencia de los campos ID de factura y numero de orden de compra dentro del documento, concatena sus valores si ambos estan presentes (separados por un guion), y actualiza o crea un nuevo campo para almacenar el valor combinado.

#### Fragmento de Codigo

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combinar ID de factura y numero de orden de compra con un separador de guion
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Verificar si hay un numero extendido para establecer
if extended_number:
    # Actualizar el campo 'invoice_extended_number' con el valor combinado
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
