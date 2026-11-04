# Scripting in DocBits

## Guida allo scripting di DocBits

Benvenuti alla guida allo scripting di DocBits! Qui imparerai come utilizzare script per automatizzare e migliorare l'elaborazione dei documenti all'interno di DocBits. Gli script consentono la manipolazione dei campi personalizzati, la trasformazione dei dati e l'implementazione della logica su vari tipi di documenti.

### Per iniziare

Gli script in DocBits sono scritti in Python. Interagiscono con i campi e i metadati del documento per eseguire una vasta gamma di operazioni, dalla formattazione semplice dei dati alla logica complessa.

#### Funzioni chiave

* `get_field_value(fields_dict, field_name, default=None)`: Recupera il valore di un campo specificato.
* `set_field_value(fields_dict, field_name, value)`: Imposta il valore di un campo specificato.
* `create_new_field(field_name, value)`: Crea un nuovo campo con un nome e un valore specificati.
* `format_decimal_to_locale(value, locale)`: Formatta un valore decimale secondo una località specificata.

### Esempi di script

Di seguito sono riportati diversi esempi che illustrano compiti di scripting comuni.

#### Esempio 1: Mappatura valuta per le fatture

Standardizzare i simboli o il testo della valuta nei codici valuta ISO.
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

