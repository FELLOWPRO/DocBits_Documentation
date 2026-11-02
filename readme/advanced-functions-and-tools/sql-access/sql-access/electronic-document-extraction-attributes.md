# Attributi di estrazione dei documenti elettronici

## Tabella `public.electronic_document_extraction_attributes`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `electronic_document_type`: interno
* `attribute_name`: interno
* `attribute_type`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `deleted_on`: timestamp con fuso orario
* `last_modified_by`: interno
* `deleted_by`: interno

### Analisi e descrizione

## Documentazione tecnica della tabella `public.electronic_document_extraction_attributes`

### Introduzione

La tabella `public.electronic_document_extraction_attributes` gestisce gli attributi relativi all'estrazione dei documenti elettronici. Ciò comporta la memorizzazione di varie caratteristiche e metadati sui tipi di documento elettronico, sui relativi metodi di elaborazione e sulle organizzazioni associate. La tabella sembra supportare funzionalità come l'identificazione del tipo di documento, le trasformazioni, le anteprime e le descrizioni della struttura, essenziali per gestire in modo efficace i documenti elettronici.

### Descrizione delle colonne

#### id

* **Significato**: un identificatore univoco per ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni voce degli attributi di estrazione del documento.
* **Nota**: funge da riferimento univoco per ogni riga.

#### org\_id

* **Significato**: identificatore dell'organizzazione correlata agli attributi del documento.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rimanda all'organizzazione associata.
* **Nota**: collega gli attributi di estrazione del documento a una specifica organizzazione.

#### doc\_type\_key

* **Significato**: una chiave che rappresenta il tipo di documento.
* **Ruolo**: identificatore per la categorizzazione dei documenti.
* **Contenuto tipico**: una stringa che indica il tipo di documento, come 'INVOICE' o 'ORDER\_CONFIRMATION'.
* **Nota**: utilizzata per determinare la categoria del documento.

#### sub\_doc\_type\_key

* **Significato**: rappresenta una sottocategoria del tipo di documento principale.
* **Ruolo**: identificatore per un'ulteriore classificazione.
* **Contenuto tipico**: null oppure una stringa di sottotipo specifica.
* **Nota**: utile per una maggiore granularità nella classificazione dei documenti.

#### electronic\_document\_type

* **Significato**: il formato o lo standard del documento elettronico.
* **Ruolo**: campo descrittivo del formato del documento.
* **Contenuto tipico**: stringhe come 'EDI' o 'FACTURX'.
* **Nota**: indica lo standard o il formato del documento.

#### attribute\_name

* **Significato**: il nome dell'attributo relativo al processo di estrazione del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringhe come 'PREVIEW' o 'TRANSFORMATION'.
* **Nota**: descrive lo specifico attributo relativo alla gestione del documento.

#### attribute\_type

* **Significato**: il tipo dell'attributo relativo all'estrazione del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringhe come 'XSLT' o 'JSON'.
* **Nota**: specifica il formato dei dati o il metodo utilizzato per l'attributo.

#### created\_by

* **Significato**: ID dell'utente che ha creato il record.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: numero intero che rappresenta un ID utente.
* **Nota**: traccia chi ha creato inizialmente il record.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora in UTC.
* **Nota**: indica l'ora di creazione del record.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica del record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora in UTC, oppure null se non modificato.
* **Nota**: traccia l'aggiornamento più recente del record.

#### is\_deleted

* **Significato**: indica se il record è contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano, `True` o `False`.
* **Nota**: aiuta nella gestione dell'eliminazione logica.

#### deleted\_on

* **Significato**: timestamp in cui il record è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora in UTC, oppure una data predefinita molto remota se non eliminato.
* **Nota**: utilizzato per tracciare quando il record è stato eliminato.

#### last\_modified\_by

* **Significato**: ID dell'utente che ha modificato per ultimo il record.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: stringa UUID, oppure null se non modificato.
* **Nota**: identifica l'utente responsabile dell'ultima modifica.

#### deleted\_by

* **Significato**: ID dell'utente che ha contrassegnato il record come eliminato.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: stringa UUID, oppure null se non eliminato.
* **Nota**: traccia chi ha eseguito l'azione di eliminazione.

Questa documentazione offre una panoramica dettagliata della struttura della tabella e delle sue colonne, per favorirne la comprensione e l'utilizzo da parte di sviluppatori e amministratori di database.
