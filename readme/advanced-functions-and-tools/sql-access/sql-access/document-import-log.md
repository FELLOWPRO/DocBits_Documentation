# Registro di importazione dei documenti

## Colonne

* `id`: integer
* `org_id`: ID dell'organizzazione
* `sub_org_id`: interno
* `original_filename`: interno
* `filename`: interno
* `imported_on`: interno
* `source_type`: interno
* `source`: interno
* `success`: boolean
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: interno
* `email_connection_id`: integer
* `subject`: interno
* `body`: text
* `sender`: interno
* `error_resp`: interno
* `source_received_on`: timestamp con fuso orario

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.document_import_log`

## Introduzione

La tabella `public.document_import_log` è progettata per registrare i dettagli delle importazioni di documenti nel sistema. Raccoglie informazioni su ciascun documento, tra cui l'origine, lo stato dell'importazione e i metadati correlati. Questa tabella è essenziale per tracciare le attività di importazione dei documenti e diagnosticare eventuali problemi che possono sorgere durante il processo di importazione.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni voce del log di importazione.
- **Ruolo**: chiave primaria
- **Contenuto tipico**: valori interi sequenziali che identificano in modo univoco ogni record.

### org_id
- **Significato**: l'identificatore dell'organizzazione associata all'importazione.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: UUID o analoga stringa identificativa univoca che rappresenta l'organizzazione.

### sub_org_id
- **Significato**: l'identificatore di una sotto-organizzazione o di un reparto all'interno dell'organizzazione principale.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: UUID o analoga stringa identificativa univoca; può essere `None` se non applicabile.

### original_filename
- **Significato**: il nome originale del file del documento al momento del caricamento.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa che rappresenta il nome del file, ad esempio `anton_invoice-1.pdf`.

### filename
- **Significato**: il nome del file del documento dopo l'elaborazione o l'archiviazione nel sistema.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa che rappresenta il nome del file, spesso identico a `original_filename`.

### imported_on
- **Significato**: la data e l'ora in cui il documento è stato importato.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: timestamp in formato ISO 8601.

### source_type
- **Significato**: il tipo di origine da cui il documento è stato importato.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa, ad esempio `EMAIL`, che indica il tipo di origine.

### source
- **Significato**: informazioni dettagliate sull'origine dell'importazione.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa che descrive l'origine, ad esempio `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Significato**: indica se l'importazione è riuscita.
- **Ruolo**: campo di stato
- **Contenuto tipico**: valore booleano (`True` o `False`).

### created_by
- **Significato**: l'identificatore dell'utente che ha avviato l'importazione.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: numero intero che rappresenta l'ID utente.

### created_on
- **Significato**: la data e l'ora in cui è stata creata la voce del log di importazione.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: timestamp con fuso orario.

### last_modified_on
- **Significato**: la data e l'ora dell'ultima modifica della voce del log di importazione.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: timestamp con fuso orario; può essere `None` se non è stata modificata.

### is_deleted
- **Significato**: indica se la voce del log di importazione è stata contrassegnata come eliminata.
- **Ruolo**: campo di stato
- **Contenuto tipico**: valore booleano (`True` o `False`).

### import_id
- **Significato**: un identificatore univoco del processo di importazione.
- **Ruolo**: campo tecnico
- **Contenuto tipico**: stringa o testo che rappresenta un ID di processo univoco.

### extra_data
- **Significato**: metadati aggiuntivi relativi all'importazione.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa JSON contenente dati aggiuntivi, come data, mittente, oggetto e conteggio.

### doc_id
- **Significato**: l'identificatore del documento.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: UUID o analoga stringa identificativa univoca; può essere `None`.

### email_connection_id
- **Significato**: l'identificatore della connessione e-mail utilizzata per l'importazione.
- **Ruolo**: chiave esterna
- **Contenuto tipico**: numero intero che rappresenta l'ID della connessione e-mail; può essere `None`.

### subject
- **Significato**: la riga dell'oggetto dell'e-mail da cui è stato importato il documento.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa che rappresenta l'oggetto dell'e-mail.

### body
- **Significato**: il contenuto del corpo dell'e-mail da cui è stato importato il documento.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: testo contenente il corpo dell'e-mail; può essere `None`.

### sender
- **Significato**: l'indirizzo e-mail del mittente del documento.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: stringa contenente l'indirizzo e-mail del mittente.

### error_resp
- **Significato**: risposta o messaggio di errore in caso di importazione non riuscita.
- **Ruolo**: campo di stato
- **Contenuto tipico**: stringa contenente i dettagli dell'errore; può essere `None`.

### source_received_on
- **Significato**: la data e l'ora in cui il documento è stato ricevuto dall'origine.
- **Ruolo**: campo descrittivo
- **Contenuto tipico**: timestamp con fuso orario.

Questa documentazione offre una panoramica dettagliata della tabella `public.document_import_log` e delle sue colonne, essenziale per comprendere e gestire le importazioni di documenti nel sistema.
```
