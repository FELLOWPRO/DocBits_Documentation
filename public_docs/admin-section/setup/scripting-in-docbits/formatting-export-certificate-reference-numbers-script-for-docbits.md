# Formateo de Script de Números de Referencia de Certificado de Exportación para Docbits

Este documento describe el script "Formateo de Números de Referencia de Certificado de Exportación", con el objetivo de estandarizar los números de referencia en los certificados de exportación en Docbits. El formateo adecuado garantiza que los números de referencia cumplan con los requisitos de sistemas externos o regulaciones.

### Propósito

El objetivo principal del script es formatear los números de referencia en los certificados de exportación, asegurando que cumplan con un requisito de longitud predefinido rellenándolos con ceros a la izquierda. Esta consistencia ayuda a mantener un formato estandarizado para todos los documentos de exportación procesados a través de Docbits.

### Resumen del Script

El script identifica el campo `reference_number` en un certificado de exportación, verifica su longitud y, si es necesario, rellena el número con ceros a la izquierda para asegurar que cumpla con el requisito de longitud mínima.

#### Fragmento de Código
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

