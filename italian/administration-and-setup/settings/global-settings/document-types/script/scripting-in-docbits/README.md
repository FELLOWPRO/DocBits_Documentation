# Script in DocBits

## Video tutorial: le funzioni di script più importanti

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v3/it.mp4" %}
Le funzioni di script più importanti in DocBits
{% endembed %}

Il video mostra nell'editor di script come leggere un campo (`get_field_value`), impostare un valore (`set_field_value`), calcolare una data di scadenza (`set_date_value`), contrassegnare un campo come non valido (`set_field_as_invalid`) e renderlo obbligatorio (`set_is_required`).

## Guida allo Scripting di Docbits

Benvenuti nella guida allo scripting di Docbits! Qui imparerete come utilizzare gli script per automatizzare e migliorare l'elaborazione dei documenti in Docbits. Gli script consentono la manipolazione personalizzata dei campi, la trasformazione dei dati e l'implementazione di logiche su vari tipi di documento.

### Per Iniziare

Gli script in Docbits sono scritti in Python. Interagiscono con i campi e i metadati dei documenti per eseguire un'ampia gamma di operazioni, dalla semplice formattazione dei dati alla logica complessa.

#### Funzioni Chiave

Ogni script riceve il documento con il nome `document_data`. Passatelo come primo argomento alle funzioni di campo. Il riferimento completo si trova nella pagina [Funzioni di Campo](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Legge il valore di un campo.
* `set_field_value(document_data, field_name, value)`: Scrive un valore in un campo e crea il campo se non esiste.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Scrive una data, se necessario con giorni aggiunti e senza fine settimana.
* `set_amount_value(document_data, field_name, value)`: Scrive un importo nel formato della localizzazione del documento.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Contrassegna un campo come non valido e mostra il messaggio all'utente.
* `set_is_required(document_data, field_name, value)`: Rende un campo obbligatorio o rimuove l'obbligo.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```
