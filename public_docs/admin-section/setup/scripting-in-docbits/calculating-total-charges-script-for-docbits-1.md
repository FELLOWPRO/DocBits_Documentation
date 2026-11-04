# Calcolo dello script delle spese totali per Docbits

##

Lo script "Calcolo delle spese totali" automatizza il processo di somma di varie spese e importi aggiuntivi all'interno dei documenti di fatturazione. Questa guida ti guiderà attraverso la configurazione dello script, la logica e l'applicazione per garantire calcoli precisi delle spese totali nei tuoi documenti.

### Scopo

Questo script mira a fornire un modo dinamico per calcolare le spese totali su una fattura sommando diversi tipi di spese, come spese di base, trasporto (Fracht) e imballaggio (Verpackung). Aggiorna quindi il campo delle spese totali della fattura con la somma calcolata, garantendo informazioni di fatturazione accurate.

### Panoramica dello script

Lo script recupera i valori dai campi specificati, li converte in float, li somma e quindi aggiorna il campo `total_charges` con il risultato. Se il campo `total_charges` non esiste, lo script crea questo campo e imposta il suo valore di conseguenza.

#### Frammento di codice
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

