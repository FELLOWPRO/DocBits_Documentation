# Script per la Generazione di Numeri di Fattura Estesi per Docbits

Questo documento descrive in dettaglio lo script "Generating Extended Invoice Numbers", che automatizza la creazione di numeri di fattura estesi in Docbits. I numeri di fattura estesi combinano piu identificatori di documenti, come l'ID fattura e il numero dell'ordine di acquisto, in un unico identificatore completo. Questo script migliora la tracciabilita dei documenti e semplifica la tenuta dei registri.

### Scopo

Lo scopo di questo script e ottimizzare il processo di generazione di numeri di fattura estesi concatenando automaticamente l'ID fattura e il numero dell'ordine di acquisto, fornendo cosi un identificatore unificato e univoco per ogni documento di fattura.

### Panoramica dello Script

Lo script verifica la presenza dei campi ID fattura e numero dell'ordine di acquisto all'interno del documento, concatena i loro valori se entrambi sono presenti (separati da un trattino) e aggiorna o crea un nuovo campo per memorizzare il valore combinato.

#### Frammento di Codice

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combinare l'ID fattura e il numero dell'ordine di acquisto con un trattino come separatore
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Verificare se c'e un numero esteso da impostare
if extended_number:
    # Aggiornare il campo 'invoice_extended_number' con il valore combinato
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
