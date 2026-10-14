# Scripting in DocBits

## Guida allo Scripting di Docbits

Benvenuti nella guida allo scripting di Docbits! Qui imparerete come utilizzare gli script per automatizzare e migliorare l'elaborazione dei documenti in Docbits. Gli script consentono la manipolazione personalizzata dei campi, la trasformazione dei dati e l'implementazione di logiche su vari tipi di documento.

### Per Iniziare

Gli script in Docbits sono scritti in Python. Interagiscono con i campi e i metadati dei documenti per eseguire un'ampia gamma di operazioni, dalla semplice formattazione dei dati alla logica complessa.

#### Funzioni Chiave

* `get_field_value(fields_dict, field_name, default=None)`: Recupera il valore di un campo specificato.
* `set_field_value(fields_dict, field_name, value)`: Imposta il valore di un campo specificato.
* `create_new_field(field_name, value)`: Crea un nuovo campo con un nome e un valore specificati.
* `format_decimal_to_locale(value, locale)`: Formatta un valore decimale secondo una localizzazione specificata.

### Script di Esempio

Di seguito sono riportati diversi esempi che dimostrano attivita di scripting comuni.

#### Esempio 1: Mappatura Valute per Fatture

Standardizzare i simboli o il testo delle valute nei codici valuta ISO.

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
