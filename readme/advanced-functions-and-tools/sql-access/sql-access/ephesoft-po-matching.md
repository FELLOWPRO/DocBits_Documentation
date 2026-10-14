# Ephesoft PO matching

## Tabella `public.ephesoft_po_matching`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `doc_type`: tipo di documento
* `ephesoft_doc_id`: interno
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.ephesoft_po_matching`

### Introduzione

La tabella `public.ephesoft_po_matching` è progettata per memorizzare e gestire i dati relativi all'abbinamento degli ordini di acquisto ai documenti, come le fatture, elaborati dal sistema Ephesoft. Questa tabella raccoglie vari dettagli sui documenti, sul relativo processo di estrazione e sullo stato di abbinamento con gli ordini di acquisto.

### Descrizione delle colonne

#### id

* **Significato**: un identificatore univoco per ogni record della tabella, che rappresenta probabilmente uno specifico documento o una transazione elaborata.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: identificatore univoco universale (UUID) in formato stringa, ad esempio `ea587c89-0d4f-4a47-a3ac-89cfb2bed9cb`.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata al documento o alla transazione.
* **Ruolo**: chiave esterna, che rimanda eventualmente a una tabella delle organizzazioni.
* **Contenuto tipico**: UUID in formato stringa, ad esempio `23f3d697-7411-4c95-981d-faf089d266be`.

#### doc\_id

* **Significato**: identificatore del documento elaborato dal sistema.
* **Ruolo**: chiave esterna, che rimanda a una tabella dei documenti o simile.
* **Contenuto tipico**: UUID in formato stringa, ad esempio `f46c6c90-568b-42ee-ae71-c5a3c22211de`.

#### doc\_type

* **Significato**: tipo del documento elaborato, che indica la natura del documento (ad esempio INVOICE).
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringa che indica il tipo di documento, ad esempio `INVOICE`.

#### ephesoft\_doc\_id

* **Significato**: identificatore utilizzato dal sistema Ephesoft per tracciare il documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringa breve, eventualmente un identificatore, ad esempio `DOC1`.

#### extracted\_data

* **Significato**: dati JSON contenenti le informazioni estratte dal documento, inclusi campi, tabelle e metadati.
* **Ruolo**: campo di archiviazione dei contenuti estratti dal documento.
* **Contenuto tipico**: struttura JSON con dettagli come tipo di documento, campi, tabelle e metadati.

#### created\_by

* **Significato**: identificatore dell'utente o del sistema che ha creato il record.
* **Ruolo**: chiave esterna, che rimanda eventualmente a una tabella utenti.
* **Contenuto tipico**: numero intero che rappresenta l'ID utente, ad esempio `1`.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo tecnico per il tracciamento del record.
* **Contenuto tipico**: timestamp con fuso orario, ad esempio `2022-02-19 10:43:37 UTC`.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica al record.
* **Ruolo**: campo tecnico per il tracciamento del record.
* **Contenuto tipico**: timestamp con fuso orario, può essere null se non modificato dopo la creazione.

#### is\_deleted

* **Significato**: flag che indica se il record è contrassegnato come eliminato.
* **Ruolo**: campo tecnico per l'eliminazione logica.
* **Contenuto tipico**: booleano, `true` se il record è eliminato, `false` in caso contrario.
