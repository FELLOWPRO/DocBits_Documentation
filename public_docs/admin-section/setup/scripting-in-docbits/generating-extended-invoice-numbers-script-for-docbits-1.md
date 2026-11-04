# Generazione dello Script per Numeri di Fattura Estesi per Docbits

Questo documento dettaglia lo script "Generazione di Numeri di Fattura Estesi", che automatizza la creazione di numeri di fattura estesi in Docbits. I numeri di fattura estesi combinano più identificatori di documento, come l'ID della fattura e il numero dell'ordine d'acquisto, in un unico identificatore completo. Questo script migliora la tracciabilità dei documenti e semplifica la tenuta dei registri.

### Scopo

Lo scopo di questo script è semplificare il processo di generazione dei numeri di fattura estesi concatenando automaticamente l'ID della fattura e il numero dell'ordine d'acquisto, fornendo così un identificatore unificato e unico per ciascun documento di fattura.

### Panoramica dello Script

Lo script controlla la presenza dei campi ID della fattura e numero dell'ordine d'acquisto nel documento, concatena i loro valori se entrambi sono presenti (separati da un trattino) e aggiorna o crea un nuovo campo per memorizzare il valore combinato.

#### Frammento di Codice
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

