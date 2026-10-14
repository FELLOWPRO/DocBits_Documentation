# Document extracted data

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `field_name`: interno
* `field_value`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `field_type`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.document_extracted_data`

## Introduzione

La tabella `public.document_extracted_data` è progettata per memorizzare i dati estratti da vari documenti, probabilmente ai fini dell'elaborazione e dell'analisi dei documenti. Ogni voce della tabella corrisponde a uno specifico campo estratto da un documento, ad esempio una fattura, e include i metadati sul processo di estrazione. La tabella facilita il tracciamento e la gestione dei dati dei documenti associandoli alle organizzazioni e a documenti specifici.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni voce di dati estratti.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa in formato UUID che identifica in modo univoco il record dei dati estratti.

### org_id
- **Significato**: identificatore dell'organizzazione associata ai dati del documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa in formato UUID che rappresenta l'organizzazione.

### doc_id
- **Significato**: identificatore del documento da cui sono stati estratti i dati.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa in formato UUID che rappresenta il documento.

### field_name
- **Significato**: il nome del campo estratto dal documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe come 'invoice_id', 'invoice_date', ecc., che indicano il tipo di dati estratti.

### field_value
- **Significato**: il valore associato al campo estratto.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe che rappresentano vari tipi di dati, come numeri di fattura, date o importi.

### created_by
- **Significato**: l'identificatore dell'utente o del processo che ha creato la voce di dati.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: numero intero che rappresenta un ID utente o un ID processo.

### created_on
- **Significato**: il timestamp di creazione della voce di dati.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: timestamp con dati sul fuso orario che indica la data e l'ora di creazione.

### last_modified_on
- **Significato**: il timestamp dell'ultima modifica apportata alla voce di dati.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: timestamp con dati sul fuso orario che indica la data e l'ora dell'ultima modifica (può essere null se la voce non è mai stata modificata).

### is_deleted
- **Significato**: un flag che indica se la voce di dati è stata contrassegnata come eliminata.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano, dove `False` indica le voci attive e `True` le voci eliminate.

### field_type
- **Significato**: il tipo di dati memorizzato nella colonna `field_value`.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe come 'date', 'AMOUNT', oppure null se il tipo non è specificato.

Questo modello di dati strutturato consente un'archiviazione e un recupero efficienti dei dati relativi ai documenti, supportando una gamma di applicazioni che va dall'elaborazione delle fatture alla gestione della conformità.
```
