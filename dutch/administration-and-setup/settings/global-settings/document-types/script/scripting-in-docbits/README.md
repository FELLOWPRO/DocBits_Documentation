# Scripts in DocBits

## Videohandleiding: de belangrijkste scriptfuncties

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v3/nl.mp4" %}
De belangrijkste scriptfuncties in DocBits
{% endembed %}

De video toont in de scripteditor hoe u een veld leest (`get_field_value`), een waarde instelt (`set_field_value`), een vervaldatum berekent (`set_date_value`), een veld als ongeldig markeert (`set_field_as_invalid`) en verplicht maakt (`set_is_required`).

## Docbits Scripting Gids

Welkom bij de Docbits scripting gids! Hier leer je hoe je scripts kunt gebruiken om je documentverwerking binnen Docbits te automatiseren en te verbeteren. Scripts maken aangepaste veldmanipulatie, datatransformatie en logica-implementatie mogelijk voor verschillende documenttypen.

### Aan de Slag

Scripts in Docbits worden geschreven in Python. Ze werken samen met documentvelden en metadata om een breed scala aan bewerkingen uit te voeren, van eenvoudige dataopmaak tot complexe logica.

#### **Belangrijke Functies**

Elk script ontvangt het document onder de naam `document_data`. Geef dit als eerste argument door aan de veldfuncties. De volledige referentie vind je op de pagina [Veldfuncties](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Leest de waarde van een veld.
* `set_field_value(document_data, field_name, value)`: Schrijft een waarde naar een veld en maakt het veld aan als het nog niet bestaat.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Schrijft een datum, eventueel met extra dagen en zonder weekenden.
* `set_amount_value(document_data, field_name, value)`: Schrijft een bedrag in de notatie van de locale van het document.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Markeert een veld als ongeldig en toont de melding aan de gebruiker.
* `set_is_required(document_data, field_name, value)`: Maakt een veld verplicht of heft die verplichting op.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```
