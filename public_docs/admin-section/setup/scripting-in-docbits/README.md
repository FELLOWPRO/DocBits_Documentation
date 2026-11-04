# Scripting en DocBits

## Guía de Scripting de DocBits

¡Bienvenido a la guía de scripting de DocBits! Aquí aprenderás cómo usar scripts para automatizar y mejorar el procesamiento de documentos dentro de DocBits. Los scripts permiten la manipulación de campos personalizados, la transformación de datos y la implementación de lógica en varios tipos de documentos.

### Empezando

Los scripts en DocBits se escriben en Python. Interactúan con los campos de documentos y metadatos para realizar una amplia gama de operaciones, desde el formateo de datos simples hasta la lógica compleja.

#### Funciones Clave

* `get_field_value(fields_dict, field_name, default=None)`: Obtiene el valor de un campo especificado.
* `set_field_value(fields_dict, field_name, value)`: Establece el valor de un campo especificado.
* `create_new_field(field_name, value)`: Crea un nuevo campo con un nombre y valor especificados.
* `format_decimal_to_locale(value, locale)`: Formatea un valor decimal de acuerdo con un locale especificado.

### Ejemplos de Scripts

A continuación se muestran varios ejemplos que demuestran tareas comunes de scripting.

#### Ejemplo 1: Mapeo de Monedas para Facturas

Estandariza los símbolos o texto de moneda a códigos de moneda ISO.
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

