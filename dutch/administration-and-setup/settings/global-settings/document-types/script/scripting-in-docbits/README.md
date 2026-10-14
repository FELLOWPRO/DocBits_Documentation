# Scripting in DocBits

## Docbits Scripting Gids

Welkom bij de Docbits scripting gids! Hier leer je hoe je scripts kunt gebruiken om je documentverwerking binnen Docbits te automatiseren en te verbeteren. Scripts maken aangepaste veldmanipulatie, datatransformatie en logica-implementatie mogelijk voor verschillende documenttypen.

### Aan de Slag

Scripts in Docbits worden geschreven in Python. Ze werken samen met documentvelden en metadata om een breed scala aan bewerkingen uit te voeren, van eenvoudige dataopmaak tot complexe logica.

#### **Belangrijke Functies**

* `get_field_value(fields_dict, field_name, default=None)`: Haalt de waarde van een opgegeven veld op.
* `set_field_value(fields_dict, field_name, value)`: Stelt de waarde van een opgegeven veld in.
* `create_new_field(field_name, value)`: Creëert een nieuw veld met een opgegeven naam en waarde.
* `format_decimal_to_locale(value, locale)`: Formatteert een decimale waarde volgens een opgegeven locale.

### Voorbeeldscripts

Hieronder staan verschillende voorbeelden die veelvoorkomende scriptingtaken demonstreren.

#### **Voorbeeld 1: Valuta Mapping voor Facturen**

Standaardiseer valutatekens of tekst naar ISO valutacodes.

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
