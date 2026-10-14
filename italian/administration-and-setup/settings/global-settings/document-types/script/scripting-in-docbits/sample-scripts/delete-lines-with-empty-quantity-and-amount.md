# Eliminare righe con quantita e importo vuoti

#### Parte 1: Eliminare Righe con Quantita e Importo Vuoti

Questa sezione dello script elabora una tabella di fattura per rimuovere tutte le righe in cui sia la quantita che l'importo totale sono zero o non forniti.

* **Verifica INVOICE\_TABLE:** Inizia verificando se la chiave `INVOICE_TABLE` esiste nel dizionario `tables_dict`.
* **Iterare sulle Righe:** Per ogni riga nella tabella, lo script inizializza flag e variabili per determinare se esistono le colonne `TOTAL_AMOUNT` e `QUANTITY` e per catturare i loro valori.
* **Verificare i Nomi delle Colonne:** Iterando attraverso ogni colonna di una riga, cerca le colonne chiamate `TOTAL_AMOUNT` e `QUANTITY`.
  * Se viene trovato `TOTAL_AMOUNT`, cattura il valore. Se questo valore non e zero, lo converte in un numero a virgola mobile.
  * Analogamente per `QUANTITY`, catturando e convertendo il valore se non e zero.
* **Marcare la Riga per l'Eliminazione:** Dopo aver verificato entrambe le colonne in una riga, se sia l'importo totale che la quantita sono effettivamente zero (o essendo zero o non esistendo), la riga viene marcata per l'eliminazione impostando `row['is_deleted']` su `True`.

#### Parte 2: Validare il Totale delle Righe rispetto al Totale della Fattura

Questa sezione calcola l'importo totale da tutte le righe di una fattura e lo confronta con il totale riportato della fattura per validare la loro coerenza.

* **Inizializzare il Totale delle Righe:** Inizia impostando una variabile `lines_total` a 0.0 per accumulare l'importo totale da tutte le righe.
* **Sommare gli Importi delle Righe:** Itera su ogni riga nella `INVOICE_TABLE`, estraendo il `TOTAL_AMOUNT` da ciascuna e aggiungendolo a `lines_total`.
* **Recuperare e Convertire il Totale della Fattura:** Ottiene l'importo totale della fattura usando la funzione helper `get_field_value` e lo converte in un numero a virgola mobile.
* **Confrontare i Totali:** Infine, verifica se la differenza assoluta tra il totale calcolato delle righe (`lines_total`) e il totale riportato della fattura (`total_amount`) supera una soglia di 0,05. Se si, contrassegna il campo del totale fattura come non valido usando la funzione helper `set_field_as_invalid`, segnalando una discrepanza.

```python
##################################################
# Eliminare righe con quantita e importo vuoti
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True

##################################################
# Fine: Eliminare righe con quantita e importo vuoti
##################################################

##################################################
# Validare il totale delle righe rispetto al totale della fattura
##################################################
lines_total = 0.0
# Ottenere il totale delle righe
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Ottenere il totale della fattura
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Confrontare il totale delle righe con il totale della fattura
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Fine: Validare il totale delle righe rispetto al totale della fattura
##################################################
```

#### Riepilogo

Lo script garantisce efficacemente l'integrita dei dati mediante:

1. Rimozione delle righe di dati che non contribuiscono al totale finanziario della fattura a causa di quantita o importi mancanti.
2. Validazione della coerenza tra la somma degli importi delle singole righe e il totale complessivo della fattura, evidenziando le discrepanze per ulteriori azioni.

Questa automazione aiuta a mantenere registri finanziari accurati e puo essere cruciale per sistemi come ERP che richiedono dati precisi per la contabilita e la reportistica finanziaria.
