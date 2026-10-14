# Training data

## Tabella `public.training_data`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type`: tipo di documento
* `doc_origin`: origine del documento
* `doc_locale`: locale del documento
* `doc_language`: lingua
* `first_page_content`: text
* `supplier_name`: nome del fornitore
* `supplier_vat`: interno
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: interno
* `sample_file_name`: interno
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.training_data`

### Introduzione

La tabella `public.training_data` sembra essere progettata per memorizzare vari dati relativi ai documenti, probabilmente utilizzati per addestrare modelli o sistemi che elaborano e analizzano il contenuto dei documenti. La tabella include informazioni sul tipo di documento, sull'origine, sulla lingua, sui dettagli del fornitore e sui timestamp di creazione e modifica dei record, oltre ad altri attributi. Sembra concentrarsi in particolare su fatture e ricevute mediche, il che suggerisce un utilizzo in applicazioni di elaborazione di dati finanziari o sanitari.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: un identificatore univoco universale (UUID) in formato carattere.
* **Nota**: essenziale per identificare in modo univoco ogni voce.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata al documento.
* **Ruolo**: chiave esterna che rimanda a un record di organizzazione.
* **Contenuto tipico**: UUID che rappresenta un'organizzazione.
* **Nota**: aiuta ad associare i documenti a specifiche organizzazioni.

#### doc\_type

* **Significato**: tipo di documento memorizzato nel record.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: valori come 'INVOICE' o 'MEDICAL\_RECEIPT'.
* **Nota**: utile per categorizzare i documenti.

#### doc\_origin

* **Significato**: origine o codice del paese di provenienza del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: codice paese come 'DE' per la Germania.
* **Nota**: indica l'origine geografica del documento.

#### doc\_locale

* **Significato**: informazioni sul locale del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: codice locale come 'en\_DE'.
* **Nota**: combina lingua e regione a fini di localizzazione.

#### doc\_language

* **Significato**: lingua in cui è scritto il documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: codice lingua come 'en' o 'de'.
* **Nota**: indica la lingua principale utilizzata nel documento.

#### first\_page\_content

* **Significato**: contenuto della prima pagina del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: dati di testo contenenti il contenuto della prima pagina del documento.
* **Nota**: può essere utilizzato per l'analisi o l'elaborazione del testo.

#### supplier\_name

* **Significato**: nome del fornitore associato al documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: nome del fornitore in formato testo.
* **Nota**: importante per identificare la fonte o l'autore del documento.

#### supplier\_vat

* **Significato**: partita IVA (numero di identificazione IVA) del fornitore.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: ID IVA, ad es. 'DE 129375678'.
* **Nota**: utile per i processi fiscali e tributari.

#### doc\_created\_on

* **Significato**: timestamp di creazione del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: data e ora in formato UTC.
* **Nota**: fornisce il contesto temporale della creazione del documento.

#### is\_training\_sample

* **Significato**: indicatore che segnala se il record è utilizzato come campione di addestramento.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano (`True` o `False`).
* **Nota**: identifica i record specificamente contrassegnati per l'addestramento.

#### sample\_doc\_id

* **Significato**: identificatore del documento campione.
* **Ruolo**: campo descrittivo o possibile chiave esterna.
* **Contenuto tipico**: UUID che rimanda a un altro documento.
* **Nota**: può fare riferimento a un documento correlato o originale utilizzato per il campionamento.

#### sample\_file\_name

* **Significato**: nome del file associato al documento campione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: nome del file in formato testo.
* **Nota**: utile per i processi di gestione o di recupero dei file.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora in formato UTC.
* **Nota**: indica quando il record è stato aggiunto al database.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica del record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora in formato UTC.
* **Nota**: tiene traccia dell'ultimo aggiornamento del record.

#### is\_deleted

* **Significato**: indicatore che segnala se il record è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano (`True` o `False`).
* **Nota**: supporta la funzionalità di eliminazione logica (soft delete).

#### is\_table\_training\_sample

* **Significato**: indicatore che segnala se il record è un campione di addestramento specifico per le tabelle.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valore booleano (`True` o `False`).
* **Nota**: si distingue dai campioni di addestramento generali, concentrandosi sui dati tabellari.
