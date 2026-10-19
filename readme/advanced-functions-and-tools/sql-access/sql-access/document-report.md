# Document Report

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `doc_type`: tipo di documento
* `sub_doc_type`: interno
* `time_spent`: interno
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: interno

## Analisi e descrizione

```markdown
# Documentazione della tabella Document Report

## Introduzione
La tabella `public.document_report` è progettata per memorizzare informazioni dettagliate sui report di elaborazione dei documenti, in particolare relativi alla validazione e all'estrazione dei campi da documenti come le fatture. La tabella raccoglie i metadati del documento, le metriche di elaborazione e gli esiti della validazione, che possono essere utilizzati per l'audit, il tracciamento e il miglioramento dei flussi di lavoro di elaborazione dei documenti.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni voce del report del documento.
- **Ruolo**: chiave primaria
- **Contenuto tipico**: un UUID che rappresenta il report del documento univoco.

### org_id
- **Significato**: identificatore dell'organizzazione associata al documento.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: un UUID che rimanda a un'organizzazione.

### doc_id
- **Significato**: identificatore dello specifico documento oggetto del report.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: un UUID che rappresenta il documento univoco.

### doc_type
- **Significato**: tipo del documento in elaborazione, ad esempio una fattura.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: valori come `INVOICE`.

### sub_doc_type
- **Significato**: sottotipo del documento, che fornisce un'ulteriore categorizzazione.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: può essere `null` oppure sottotipi specifici come "Cost Invoice".

### time_spent
- **Significato**: tempo impiegato per la validazione del documento.
- **Ruolo**: campo metrico
- **Contenuto tipico**: di norma '0', espresso in unità di tempo predefinite.

### fields_total
- **Significato**: numero totale di campi estratti dal documento.
- **Ruolo**: campo metrico
- **Contenuto tipico**: un numero intero che rappresenta il totale dei campi, ad esempio 13.

### fields_correct
- **Significato**: numero di campi estratti e validati correttamente.
- **Ruolo**: campo metrico
- **Contenuto tipico**: un numero intero che rappresenta i campi elaborati correttamente, ad esempio 12.

### checkbox_fields_total
- **Significato**: numero totale di campi casella di controllo elaborati.
- **Ruolo**: campo metrico
- **Contenuto tipico**: di solito `0`, a indicare i campi casella di controllo elaborati.

### checkbox_fields_correct
- **Significato**: numero di campi casella di controllo validati correttamente.
- **Ruolo**: campo metrico
- **Contenuto tipico**: di solito `0`, a indicare i campi casella di controllo validati correttamente.

### table_values_total
- **Significato**: numero totale di valori di tabella estratti dal documento.
- **Ruolo**: campo metrico
- **Contenuto tipico**: di solito `0`, a indicare il totale dei valori di tabella elaborati.

### table_values_correct
- **Significato**: numero di valori di tabella validati correttamente.
- **Ruolo**: campo metrico
- **Contenuto tipico**: di solito `0`, a indicare i valori di tabella validati correttamente.

### detail_report
- **Significato**: contenuto JSON che fornisce un report dettagliato dei campi del documento e del loro stato di validazione.
- **Ruolo**: campo descrittivo/tecnico
- **Contenuto tipico**: stringa JSON contenente informazioni dettagliate sui campi.

### created_on
- **Significato**: timestamp di creazione della voce del report del documento.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: timestamp in UTC, ad esempio `2025-03-10 08:07:24+00`.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica al report del documento.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: timestamp in UTC che indica l'ora dell'ultimo aggiornamento.

### is_deleted
- **Significato**: indica se il report del documento è stato contrassegnato come eliminato.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: valore booleano; `False` se non eliminato.

### validated_by
- **Significato**: identificatore dell'utente che ha validato il documento.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: numero intero che rappresenta l'ID del validatore, ad esempio `1`.

### sub_org_id
- **Significato**: identificatore di una sotto-organizzazione collegata al documento.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: un UUID che rimanda a una sotto-organizzazione.
```
