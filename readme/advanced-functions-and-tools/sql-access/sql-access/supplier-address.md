# Supplier address

## Colonne

* `org_id`: ID dell'organizzazione
* `customer_number`: interno
* `supplier_number`: interno
* `address_id`: interno
* `supplier_name`: nome del fornitore
* `address_1`: interno
* `address_2`: interno
* `address_3`: interno
* `address_4`: interno
* `zip_code`: interno
* `town_city`: interno
* `country_code`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: interno
* `id`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.supplier_address`

## Introduzione

La tabella `public.supplier_address` è progettata per memorizzare le informazioni relative agli indirizzi dei fornitori. Contiene vari campi che acquisiscono dettagli come gli ID organizzativi, i numeri di cliente e di fornitore, più righe di indirizzo, i recapiti, i metadati di creazione e modifica e lo stato di eliminazione. Questa tabella è probabilmente utilizzata in un sistema per gestire le informazioni sui fornitori e i relativi indirizzi, che possono essere fondamentali per la logistica, la fatturazione e i contatti.

## Descrizione delle colonne

### org_id
- **Significato**: questa colonna memorizza l'identificatore univoco dell'organizzazione.
- **Ruolo**: chiave esterna, che probabilmente rimanda a una tabella delle organizzazioni.
- **Contenuto tipico**: UUID che rappresenta un'organizzazione.

### customer_number
- **Significato**: questa colonna può memorizzare un numero univoco assegnato ai clienti.
- **Ruolo**: identificatore dei clienti.
- **Contenuto tipico**: stringa alfanumerica che rappresenta i numeri di cliente.

### supplier_number
- **Significato**: questa colonna memorizza un numero univoco assegnato ai fornitori.
- **Ruolo**: identificatore dei fornitori.
- **Contenuto tipico**: stringa numerica che rappresenta i numeri di fornitore.

### address_id
- **Significato**: questa colonna memorizza probabilmente il tipo di indirizzo, ad esempio 'Discrete' o 'Text'.
- **Ruolo**: campo descrittivo per la categorizzazione degli indirizzi.
- **Contenuto tipico**: valori come 'Discrete', 'Text'.

### supplier_name
- **Significato**: questa colonna memorizza il nome del fornitore.
- **Ruolo**: campo descrittivo per l'identificazione del fornitore.
- **Contenuto tipico**: nome del fornitore, ad es. "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Significato**: questa colonna memorizza la riga principale dell'indirizzo del fornitore.
- **Ruolo**: campo descrittivo per le informazioni sull'indirizzo.
- **Contenuto tipico**: indirizzo stradale, ad es. "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Significato**: questa colonna memorizza la seconda riga dell'indirizzo del fornitore, se applicabile.
- **Ruolo**: campo supplementare per le informazioni sull'indirizzo.
- **Contenuto tipico**: dettagli aggiuntivi dell'indirizzo, spesso lasciati vuoti.

### address_3
- **Significato**: questa colonna memorizza la terza riga dell'indirizzo del fornitore, se applicabile.
- **Ruolo**: campo supplementare per le informazioni sull'indirizzo.
- **Contenuto tipico**: dettagli aggiuntivi dell'indirizzo, spesso lasciati vuoti.

### address_4
- **Significato**: questa colonna memorizza la quarta riga dell'indirizzo del fornitore, se applicabile.
- **Ruolo**: campo supplementare per le informazioni sull'indirizzo.
- **Contenuto tipico**: dettagli aggiuntivi dell'indirizzo, spesso lasciati vuoti.

### zip_code
- **Significato**: questa colonna memorizza il codice postale (CAP) dell'indirizzo del fornitore.
- **Ruolo**: campo descrittivo per l'identificazione geografica.
- **Contenuto tipico**: codice postale numerico, ad es. "06449".

### town_city
- **Significato**: questa colonna memorizza il nome della località o della città dell'indirizzo del fornitore.
- **Ruolo**: campo descrittivo per l'identificazione geografica.
- **Contenuto tipico**: nome della località o della città, ad es. "Aschersleben".

### country_code
- **Significato**: questa colonna memorizza il codice paese ISO dell'indirizzo del fornitore.
- **Ruolo**: campo descrittivo per l'identificazione del paese.
- **Contenuto tipico**: codice paese di due lettere, ad es. "DE".

### created_by
- **Significato**: questa colonna memorizza l'identificatore dell'utente o del sistema che ha creato il record.
- **Ruolo**: campo tecnico per tracciare la creazione del record.
- **Contenuto tipico**: intero che rappresenta l'ID di un utente.

### created_on
- **Significato**: questa colonna memorizza il timestamp di creazione del record.
- **Ruolo**: campo tecnico per tracciare l'ora di creazione del record.
- **Contenuto tipico**: timestamp con fuso orario, ad es. "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Significato**: questa colonna memorizza il timestamp dell'ultima modifica del record.
- **Ruolo**: campo tecnico per tracciare l'ora dell'ultimo aggiornamento.
- **Contenuto tipico**: timestamp con fuso orario, spesso lasciato come `None`.

### is_deleted
- **Significato**: questa colonna indica se il record è contrassegnato come eliminato.
- **Ruolo**: campo tecnico per la funzionalità di eliminazione logica (soft delete).
- **Contenuto tipico**: valore booleano, ad es. `False`.

### sub_org_id
- **Significato**: questa colonna memorizza un identificatore di sottorganizzazione, se applicabile.
- **Ruolo**: chiave esterna o identificatore delle sottorganizzazioni.
- **Contenuto tipico**: UUID, spesso lasciato vuoto.

### id
- **Significato**: questa colonna memorizza l'identificatore univoco del record.
- **Ruolo**: chiave primaria della tabella.
- **Contenuto tipico**: UUID che rappresenta il record.

```
