# Scripting en DocBits

## Guía de scripting de DocBits

¡Bienvenido a la guía de scripting de DocBits! Aquí aprenderá a utilizar scripts para automatizar y mejorar el procesamiento de documentos dentro de DocBits. Los scripts permiten la manipulación personalizada de campos, la transformación de datos y la implementación de lógica en varios tipos de documentos.

### Primeros pasos

Los scripts en DocBits están escritos en Python. Interactúan con los campos y los metadatos del documento para realizar una amplia gama de operaciones, desde el simple formato de datos hasta la lógica compleja.

#### Funciones clave

* `get_field_value(fields_dict, field_name, default=None)`: Recupera el valor de un campo especificado.
* `set_field_value(fields_dict, field_name, value)`: Establece el valor de un campo especificado.
* `create_new_field(field_name, value)`: Crea un nuevo campo con un nombre y un valor especificados.
* `format_decimal_to_locale(value, locale)`: Formatea un valor decimal según una configuración regional especificada.

### Scripts de ejemplo

A continuación se presentan varios ejemplos que demuestran tareas de scripting habituales.

#### Ejemplo 1: Asignación de monedas para facturas

Estandariza símbolos o textos de moneda a códigos de moneda ISO.

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


