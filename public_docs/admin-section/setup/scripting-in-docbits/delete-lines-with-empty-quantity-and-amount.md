# Elimina le righe con quantità e importo vuoti

#### Parte 1: Eliminazione delle righe con quantità e importo vuoti

Questa sezione dello script elabora una tabella delle fatture per rimuovere qualsiasi riga in cui sia sia la quantità che l'importo totale siano zero o non forniti.

* **Verifica di INVOICE\_TABLE:** Inizia controllando se la chiave `INVOICE_TABLE` esiste nel dizionario `tables_dict`.
* **Itera sulle righe:** Per ogni riga nella tabella, lo script inizializza flag e variabili per determinare se le colonne `TOTAL_AMOUNT` e `QUANTITY` esistono e per catturare i loro valori.
* **Controlla i nomi delle colonne:** Mentre itera su ciascuna colonna in una riga, cerca colonne chiamate `TOTAL_AMOUNT` e `QUANTITY`.
* Se viene trovato `TOTAL_AMOUNT`, cattura il valore. Se questo valore è diverso da zero, lo converte in un float.
* Allo stesso modo per `QUANTITY`, catturando e convertendo il valore se è diverso da zero.
* **Segna la riga per l'eliminazione:** Dopo aver controllato entrambe le colonne in una riga, se sia l'importo totale che la quantità sono effettivamente zero (sia per essere zero o non esistere), la riga viene contrassegnata per l'eliminazione impostando `row['is_deleted']` su `True`.

#### Parte 2: Convalida del totale della riga rispetto al totale della fattura

Questa sezione calcola l'importo totale di tutte le righe di una fattura e lo confronta con il totale segnalato della fattura per convalidarne la coerenza.

* **Inizializza il totale delle righe:** Inizia impostando una variabile `lines_total` su 0.0 per accumulare l'importo totale di tutte le righe.
* **Somma gli importi delle righe:** Itera su ciascuna riga nella `INVOICE_TABLE`, estraendo il `TOTAL_AMOUNT` da ciascuna e aggiungendolo a `lines_total`.
* **Recupera e converte il totale della fattura:** Recupera l'importo totale della fattura utilizzando una funzione ausiliaria `get_field_value` e lo converte in un float.
* **Confronta i totali:** Infine, controlla se la differenza assoluta tra il totale della riga calcolato (`lines_total`) e il totale della fattura segnalato (`total_amount`) supera una soglia di 0.05. In tal caso, contrassegna il campo del totale della fattura come non valido utilizzando un'altra funzione ausiliaria `set_field_as_invalid`, citando una discrepanza.
```python
##################################################
# Delete lines with empty quantity and amount
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
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
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

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################







```
#### Sommario

Lo script garantisce efficacemente l'integrità dei dati:

1. Rimuovendo le righe di dati che non contribuiscono al totale finanziario della fattura a causa della mancanza di quantità o importi.
2. Convalidando la coerenza tra la somma degli importi delle singole righe e il totale generale della fattura, evidenziando eventuali discrepanze per ulteriori azioni.

Questa automazione aiuta a mantenere registri finanziari accurati e può essere cruciale per sistemi come ERP che richiedono dati precisi per la contabilità e la segnalazione finanziaria.
