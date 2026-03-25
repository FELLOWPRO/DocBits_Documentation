# Script per il Calcolo degli Addebiti Totali per Docbits

Lo script "Calculating Total Charges" automatizza il processo di somma di vari addebiti e importi aggiuntivi all'interno dei documenti di fattura. Questa guida illustra la configurazione, la logica e l'applicazione dello script per garantire calcoli accurati degli addebiti totali nei documenti.

### Scopo

Questo script mira a fornire un modo dinamico per calcolare gli addebiti totali su una fattura sommando diversi tipi di addebiti, come spese base, trasporto (Fracht) e imballaggio (Verpackung). Aggiorna quindi il campo degli addebiti totali della fattura con la somma calcolata, garantendo informazioni di fatturazione accurate.

### Panoramica dello Script

Lo script recupera i valori dai campi specificati, li converte in numeri a virgola mobile, li somma e poi aggiorna il campo `total_charges` con il risultato. Se il campo `total_charges` non esiste, lo script crea questo campo e imposta il suo valore di conseguenza.

#### Frammento di Codice

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Inizializzare il totale a 0
total = 0

# Aggiungere il trasporto al totale se esiste
if fracht:
    fracht = float(fracht)
    total += fracht

# Aggiungere l'imballaggio al totale se esiste
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formattare il totale a due cifre decimali
formatted_total = "{0:.2f}".format(total)

# Verificare se il campo total_charges esiste e aggiornare o creare di conseguenza
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
