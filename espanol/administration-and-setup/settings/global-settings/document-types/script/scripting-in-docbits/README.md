# Programación en DocBits

## Guía de Scripting de Docbits

¡Bienvenido a la guía de scripting de Docbits! Aquí, aprenderás cómo usar scripts para automatizar y mejorar el procesamiento de documentos dentro de Docbits. Los scripts permiten la manipulación personalizada de campos, la transformación de datos y la implementación de lógica a través de varios tipos de documentos.

### Comenzando

Los scripts en Docbits están escritos en Python. Interactúan con los campos y metadatos del documento para realizar una amplia gama de operaciones, desde el formato simple de datos hasta la lógica compleja.

**Funciones Clave**

* `get_field_value(fields_dict, field_name, default=None)`: Recupera el valor de un campo especificado.
* `set_field_value(fields_dict, field_name, value)`: Establece el valor de un campo especificado.
* `create_new_field(field_name, value)`: Crea un nuevo campo con un nombre y valor especificados.
* `format_decimal_to_locale(value, locale)`: Formatea un valor decimal según una configuración regional especificada.

### Scripts de Ejemplo

A continuación se presentan varios ejemplos que demuestran tareas comunes de scripting.

**Ejemplo 1: Mapeo de Moneda para Facturas**

Estandariza símbolos o texto de moneda a códigos de moneda ISO.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```
