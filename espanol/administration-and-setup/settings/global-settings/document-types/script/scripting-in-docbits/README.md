# Scripting en DocBits

## Videotutorial: las funciones de guion más importantes

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v2/es.mp4" %}
Las funciones de guion más importantes en DocBits
{% endembed %}

El vídeo muestra en el editor de scripts cómo leer un campo (`get_field_value`), establecer un valor (`set_field_value`), calcular una fecha de vencimiento (`set_date_value`), marcar un campo como no válido (`set_field_as_invalid`) y hacer que un campo sea obligatorio (`set_is_required`).

## Guía de scripting de DocBits

¡Bienvenido a la guía de scripting de DocBits! Aquí aprenderá a utilizar scripts para automatizar y mejorar el procesamiento de documentos dentro de DocBits. Los scripts permiten la manipulación personalizada de campos, la transformación de datos y la implementación de lógica en varios tipos de documentos.

### Primeros pasos

Los scripts en DocBits están escritos en Python. Interactúan con los campos y los metadatos del documento para realizar una amplia gama de operaciones, desde el simple formato de datos hasta la lógica compleja.

#### Funciones clave

Cada script recibe el documento como `document_data`. Páselo como primer argumento a las funciones de campo. Encontrará la referencia completa en la página [Funciones de campo](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Lee el valor de un campo.
* `set_field_value(document_data, field_name, value)`: Escribe un valor en un campo y crea el campo si no existe.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Escribe una fecha, opcionalmente con días añadidos y sin fines de semana.
* `set_amount_value(document_data, field_name, value)`: Escribe un importe con el formato de la configuración regional del documento.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Marca un campo como no válido y muestra el mensaje al usuario.
* `set_is_required(document_data, field_name, value)`: Convierte un campo en obligatorio o lo deja de ser.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```


