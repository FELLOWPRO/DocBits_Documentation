# Script de Formato de Numeros de Referencia de Certificado de Exportacion para DocBits

Este documento describe el script "Formatting Export Certificate Reference Numbers", destinado a estandarizar los numeros de referencia en certificados de exportacion en DocBits. El formato adecuado asegura que los numeros de referencia cumplan con los requisitos de sistemas externos o regulaciones.

### Proposito

El objetivo principal del script es formatear numeros de referencia en certificados de exportacion, asegurando que cumplan con un requisito de longitud predefinido rellenandolos con ceros a la izquierda. Esta consistencia ayuda a mantener un formato estandarizado para todos los documentos de exportacion procesados a traves de DocBits.

### Descripcion del Script

El script identifica el campo `reference_number` en un certificado de exportacion, verifica su longitud y, si es necesario, rellena el numero con ceros a la izquierda para asegurar que cumpla con el requisito de longitud minima.

#### Fragmento de Codigo

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Asegurar que el numero de referencia cumpla con una longitud minima de 10 caracteres
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
