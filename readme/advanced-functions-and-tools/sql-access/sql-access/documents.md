# Documenti

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `batch_id`: interno
* `doc_path`: interno
* `doc_type`: tipo di documento
* `status`: interno
* `message`: text
* `export_attempts`: integer
* `last_attempted_on`: timestamp con fuso orario
* `next_attempt_on`: timestamp con fuso orario
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `task_id`: interno
* `filename`: interno
* `assigned_on`: timestamp con fuso orario
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: text
* `doc_language`: lingua
* `is_trimmed`: boolean
* `doc_origin`: origine del documento
* `doc_locale`: impostazioni locali del documento
* `is_doc2landing_doc`: boolean
* `extraction_time`: double precision
* `export_time`: double precision
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: interno
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: timestamp con fuso orario
* `lock_renewed_on`: timestamp con fuso orario
* `lock_key`: interno
* `last_saved_by`: integer
* `last_saved_on`: timestamp con fuso orario
* `document_version`: integer
* `lock_session_key`: interno
* `sub_org_id`: interno
* `doc_source`: interno
* `sub_doc_type`: interno
* `assigned_to_group`: interno
* `status_changed_on`: timestamp con fuso orario
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: interno
* `doc_start_page`: integer
* `doc_classification_class`: interno
* `celery_task_token`: interno
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: timestamp con fuso orario
* `exception_details`: text
* `has_annotated_version`: boolean
* `po_match_status`: interno
* `tr_ocr_extracted_data`: text
* `pending_workflow_execution`: boolean
* `extracted_document_id`: interno
* `extracted_supplier_id`: interno
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: interno
* `extracted_data_basic`: jsonb
* `celery_task_queue`: interno
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.documents`

## Introduzione

La tabella `public.documents` è progettata per memorizzare e gestire i metadati e le informazioni di elaborazione relativi alla gestione dei documenti all'interno di un'organizzazione. Comprende il tracciamento dello stato del documento, dei tentativi di elaborazione, della lingua e di altri dettagli amministrativi. La tabella è strutturata per supportare la classificazione dei documenti, il flusso di elaborazione e le assegnazioni agli utenti, e risulta quindi parte integrante del sistema di gestione documentale.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni documento.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che rappresenta il documento.

### org_id
- **Significato**: identificatore dell'organizzazione associata al documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione.

### batch_id
- **Significato**: identificatore del batch in cui il documento è stato elaborato.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta il batch.

### doc_path
- **Significato**: percorso del file in cui è archiviato il documento.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: percorso del file del documento, ad esempio `documents/{id}/{id}.pdf`.

### doc_type
- **Significato**: tipo di documento archiviato (ad esempio una fattura).
- **Ruolo**: classificazione del documento.
- **Contenuto tipico**: una stringa come `INVOICE`.

### status
- **Significato**: stato attuale di elaborazione del documento.
- **Ruolo**: indicatore del flusso di lavoro.
- **Contenuto tipico**: una stringa che indica lo stato, ad esempio `ready_for_validation`.

### message
- **Significato**: informazioni sullo stato di elaborazione del documento o su eventuali errori.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: testo che descrive errori o messaggi relativi all'elaborazione del documento.

### export_attempts
- **Significato**: numero di tentativi di esportazione effettuati per il documento.
- **Ruolo**: tracciamento dell'elaborazione.
- **Contenuto tipico**: conteggio intero dei tentativi di esportazione.

### last_attempted_on
- **Significato**: timestamp dell'ultimo tentativo di elaborare o esportare il documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### next_attempt_on
- **Significato**: timestamp pianificato per il prossimo tentativo di elaborare o esportare il documento.
- **Ruolo**: campo di pianificazione.
- **Contenuto tipico**: data e ora con fuso orario.

### assigned_to
- **Significato**: identificatore dell'utente assegnato a questo documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: numero intero che rappresenta l'ID utente.

### created_by
- **Significato**: identificatore dell'utente che ha creato o caricato il documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: numero intero che rappresenta l'ID utente.

### created_on
- **Significato**: timestamp di creazione o caricamento del documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica apportata al record del documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### is_deleted
- **Significato**: indica se il documento è contrassegnato come eliminato.
- **Ruolo**: flag di eliminazione logica.
- **Contenuto tipico**: valore booleano (True o False).

### task_id
- **Significato**: identificatore del task associato all'elaborazione del documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta il task.

### filename
- **Significato**: nome originale del file del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: nome del file, ad esempio `document.pdf`.

### assigned_on
- **Significato**: timestamp di assegnazione del documento a un utente.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### pages
- **Significato**: numero di pagine del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: numero intero che indica il conteggio delle pagine.

### auto_processed
- **Significato**: indica se il documento è stato elaborato automaticamente.
- **Ruolo**: flag di stato dell'elaborazione.
- **Contenuto tipico**: valore booleano (True o False).

### exception_info
- **Significato**: informazioni su eventuali eccezioni riscontrate durante l'elaborazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: testo che descrive le eccezioni di elaborazione.

### doc_language
- **Significato**: lingua del contenuto del documento.
- **Ruolo**: classificazione della lingua.
- **Contenuto tipico**: codice lingua ISO, ad esempio `en`, `de`.

### is_trimmed
- **Significato**: indica se il documento è stato rifilato o ritagliato.
- **Ruolo**: flag di modifica del documento.
- **Contenuto tipico**: valore booleano (True o False).

### doc_origin
- **Significato**: origine del documento, che può indicare il paese o il sistema di provenienza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: codice paese o identificatore di origine, ad esempio `DE`.

### doc_locale
- **Significato**: impostazioni locali del documento, che indicano lingua e regione.
- **Ruolo**: classificazione delle impostazioni locali.
- **Contenuto tipico**: stringa di impostazioni locali, ad esempio `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Significato**: indica se il documento è collegato a uno specifico flusso di elaborazione (Doc2Landing).
- **Ruolo**: flag del flusso di lavoro.
- **Contenuto tipico**: valore booleano (True o False).

### extraction_time
- **Significato**: tempo impiegato per estrarre i dati dal documento.
- **Ruolo**: metrica di prestazione.
- **Contenuto tipico**: valore double precision che rappresenta il tempo di estrazione.

### export_time
- **Significato**: tempo impiegato per esportare il documento.
- **Ruolo**: metrica di prestazione.
- **Contenuto tipico**: valore double precision che rappresenta il tempo di esportazione.

### po_all_matched
- **Significato**: indica se tutti gli ordini di acquisto correlati al documento sono stati abbinati.
- **Ruolo**: flag di stato dell'abbinamento.
- **Contenuto tipico**: valore booleano (True o False).

### restart_allowed
- **Significato**: indica se l'elaborazione del documento può essere riavviata.
- **Ruolo**: flag di controllo del flusso di lavoro.
- **Contenuto tipico**: valore booleano (True o False).

### table_version
- **Significato**: versione della struttura della tabella utilizzata per il documento.
- **Ruolo**: controllo delle versioni.
- **Contenuto tipico**: stringa che indica la versione, ad esempio `v3`.

### force_ocr
- **Significato**: indica se per il documento è forzata l'elaborazione OCR.
- **Ruolo**: flag di controllo dell'elaborazione.
- **Contenuto tipico**: valore booleano (True o False).

### locked_by
- **Significato**: identificatore dell'utente che ha bloccato il documento per la modifica.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: numero intero che rappresenta l'ID utente.

### locked_on
- **Significato**: timestamp del blocco del documento per la modifica.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### lock_renewed_on
- **Significato**: timestamp dell'ultimo rinnovo del blocco del documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### lock_key
- **Significato**: chiave associata al blocco del documento.
- **Ruolo**: controllo del blocco.
- **Contenuto tipico**: stringa che rappresenta la chiave di blocco.

### last_saved_by
- **Significato**: identificatore dell'utente che ha salvato per ultimo il documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: numero intero che rappresenta l'ID utente.

### last_saved_on
- **Significato**: timestamp dell'ultimo salvataggio del documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### document_version
- **Significato**: numero di versione del documento.
- **Ruolo**: tracciamento delle versioni.
- **Contenuto tipico**: numero intero che rappresenta la versione del documento.

### lock_session_key
- **Significato**: chiave di sessione associata al blocco del documento.
- **Ruolo**: controllo del blocco.
- **Contenuto tipico**: stringa che rappresenta la chiave di sessione.

### sub_org_id
- **Significato**: identificatore di una sotto-organizzazione associata al documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta la sotto-organizzazione.

### doc_source
- **Significato**: sistema di origine o provenienza del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa che indica l'origine, ad esempio `doc2app`.

### sub_doc_type
- **Significato**: classificazione del sottotipo del documento.
- **Ruolo**: classificazione del documento.
- **Contenuto tipico**: stringa che indica il sottotipo.

### assigned_to_group
- **Significato**: identificatore del gruppo a cui è assegnato il documento.
- **Ruolo**: tracciamento delle assegnazioni.
- **Contenuto tipico**: una stringa UUID che rappresenta il gruppo.

### status_changed_on
- **Significato**: timestamp dell'ultima modifica dello stato del documento.
- **Ruolo**: campo timestamp.
- **Contenuto tipico**: data e ora con fuso orario.

### improve_quality
- **Significato**: indica se al documento vengono applicati processi di miglioramento della qualità.
- **Ruolo**: flag di controllo qualità.
- **Contenuto tipico**: valore booleano (True o False).

### priority
- **Significato**: priorità di elaborazione del documento.
- **Ruolo**: controllo del flusso di lavoro.
- **Contenuto tipico**: numero intero che indica il livello di priorità.

### metadata_field
- **Significato**: campo JSON contenente i metadati relativi al documento.
- **Ruolo**: archiviazione dei metadati.
- **Contenuto tipico**: struttura JSON con vari campi di metadati.

### doc_classification_label
- **Significato**: etichetta che indica la classificazione del documento.
- **Ruolo**: etichetta di classificazione.
- **Contenuto tipico**: stringa che indica la classificazione, ad esempio `INVOICE`.

### doc_start_page
- **Significato**: numero della pagina da cui inizia il contenuto del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: numero intero che indica la pagina iniziale.

### doc_classification_class
- **Significato**: classe che indica la classificazione dettagliata del documento.
- **Ruolo**: dettaglio della classificazione.
- **Contenuto tipico**: stringa che indica la classe di classificazione.

### celery_task_token
- **Significato**: token per tracciare il task Celery associato al documento.
- **Ruolo**: tracciamento dei task.
- **Contenuto tipico**: stringa che rappresenta il token del task.

### celery_task_attempt
- **Significato**: numero di tentativi effettuati per il task Celery.
- **Ruolo**: tracciamento dei task.
- **Contenuto tipico**: conteggio intero dei tentativi del task.

### celery_task_priority
- **Significato**: livello di priorità del task Celery.
- **Ruolo**: controllo dei task.
- **Contenuto tipico**: numero intero che indica la priorità del task.

### has_zugferd
- **Significato**: indica se il documento è in formato ZUGFeRD.
- **Ruolo**: indicatore di formato.
- **Contenuto tipico**: valore booleano (True o False).

### has_peppol
- **Significato**: indica se il documento è in formato PEPPOL.
- **Ruolo**: indicatore di formato.
- **Contenuto tipico**: valore booleano (True o False).

### timestamp_for_validation
- **Significato**: timestamp di validazione del documento.
- **Ruolo**: tracciamento della validazione.
- **Contenuto tipico**: data e ora con fuso orario.

### exception_details
- **Significato**: informazioni dettagliate sulle eccezioni verificatesi durante l'elaborazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: testo con i dettagli dell'eccezione.

### has_annotated_version
- **Significato**: indica se esiste una versione annotata del documento.
- **Ruolo**: indicatore di versione.
- **Contenuto tipico**: valore booleano (True o False).

### po_match_status
- **Significato**: stato dell'abbinamento degli ordini di acquisto.
- **Ruolo**: indicatore dello stato di abbinamento.
- **Contenuto tipico**: stringa che indica lo stato dell'abbinamento.

### tr_ocr_extracted_data
- **Significato**: dati estratti dal documento tramite OCR.
- **Ruolo**: archiviazione dei dati.
- **Contenuto tipico**: testo contenente i dati estratti.

### pending_workflow_execution
- **Significato**: indica se sono presenti esecuzioni di flussi di lavoro in sospeso.
- **Ruolo**: flag di stato del flusso di lavoro.
- **Contenuto tipico**: valore booleano (True o False).

### extracted_document_id
- **Significato**: identificatore del documento estratto.
- **Ruolo**: tracciamento dell'estrazione.
- **Contenuto tipico**: una stringa UUID che rappresenta il documento estratto.

### extracted_supplier_id
- **Significato**: identificatore del fornitore estratto.
- **Ruolo**: tracciamento dell'estrazione.
- **Contenuto tipico**: una stringa UUID che rappresenta il fornitore estratto.

### classification_manually_corrected
- **Significato**: indica se la classificazione del documento è stata corretta manualmente.
- **Ruolo**: flag di stato della classificazione.
- **Contenuto tipico**: valore booleano (True o False).

### supplier_as_org_id
- **Significato**: identificatore del fornitore trattato come organizzazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione fornitore.

### extracted_data_basic
- **Significato**: dati estratti di base in formato JSONB.
- **Ruolo**: archiviazione dei dati.
- **Contenuto tipico**: struttura JSONB con i campi dei dati estratti.

### celery_task_queue
- **Significato**: nome della coda dei task Celery.
- **Ruolo**: gestione dei task.
- **Contenuto tipico**: stringa che indica il nome della coda.

### extracted_data
- **Significato**: dati estratti dal documento in formato JSONB.
- **Ruolo**: archiviazione dei dati.
- **Contenuto tipico**: struttura JSONB con i campi dei dati estratti.

### extracted_data_jsonb
- **Significato**: campo JSONB contenente i dati estratti in dettaglio.
- **Ruolo**: archiviazione dei dati.
- **Contenuto tipico**: struttura JSONB con i campi dei dati estratti.

### warnings
- **Significato**: avvisi relativi all'elaborazione del documento, memorizzati in formato JSONB.
- **Ruolo**: archiviazione degli avvisi.
- **Contenuto tipico**: struttura JSONB con i messaggi di avviso.
```
