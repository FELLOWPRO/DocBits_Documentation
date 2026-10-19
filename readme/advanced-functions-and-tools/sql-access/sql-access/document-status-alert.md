# Document Status alert

## Tabella `public.document_status_alert`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type_id`: interno
* `doc_type_key`: interno
* `doc_status`: interno
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `name`: interno
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: interno
* `email_template_id`: interno

### Analisi e descrizione

## Documentazione della tabella: `public.document_status_alert`

### Introduzione

La tabella `public.document_status_alert` è progettata per gestire gli avvisi relativi agli stati dei documenti all'interno di un'organizzazione. In base ai nomi delle colonne, la tabella memorizza informazioni sui vari tipi di documento e sui loro stati, compresi i dettagli sulle notifiche e sulla tempistica degli avvisi. Probabilmente viene utilizzata per attivare avvisi in base a determinati stati e condizioni dei documenti, ad esempio per notificare gli utenti o scalare i processi.

### Descrizione delle colonne

#### `id`

* **Significato**: identificatore univoco di ogni record di avviso.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni riga della tabella.

#### `org_id`

* **Significato**: identificatore dell'organizzazione associata all'avviso.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rimanda al record di un'organizzazione.

#### `doc_type_id`

* **Significato**: identificatore del tipo di documento.
* **Ruolo**: chiave esterna (presunta).
* **Contenuto tipico**: di norma un UUID, anche se i dati di esempio mostrano `None`, il che indica che questo campo potrebbe essere facoltativo.

#### `doc_type_key`

* **Significato**: chiave che rappresenta il tipo di documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa come 'INVOICE' o 'XML\_INVOICE'.

#### `doc_status`

* **Significato**: stato attuale del documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringhe di stato descrittive come 'validated\_pending\_approval' o 'error'.

#### `email_address`

* **Significato**: indirizzo e-mail a cui vengono inviati gli avvisi.
* **Ruolo**: campo di notifica.
* **Contenuto tipico**: un indirizzo e-mail; può essere `None` se non è specificato alcun indirizzo.

#### `send_to_assigned_user`

* **Significato**: indica se l'avviso deve essere inviato all'utente assegnato al documento.
* **Ruolo**: campo booleano.
* **Contenuto tipico**: `True` o `False`.

#### `delay_delta`

* **Significato**: intervallo di tempo di ritardo dell'avviso.
* **Ruolo**: campo di temporizzazione.
* **Contenuto tipico**: numero intero che rappresenta la durata del ritardo.

#### `delay_delta_type`

* **Significato**: unità di tempo di `delay_delta`.
* **Ruolo**: campo di temporizzazione.
* **Contenuto tipico**: di norma 'minutes'.

#### `created_by`

* **Significato**: identificatore dell'utente che ha creato il record dell'avviso.
* **Ruolo**: chiave esterna (presunta).
* **Contenuto tipico**: numero intero che rappresenta un ID utente.

#### `created_on`

* **Significato**: timestamp di creazione del record dell'avviso.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora con informazioni sul fuso orario.

#### `last_modified_on`

* **Significato**: timestamp dell'ultima modifica al record dell'avviso.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora con informazioni sul fuso orario; può essere `None` se non modificato.

#### `is_deleted`

* **Significato**: indica se il record dell'avviso è contrassegnato come eliminato.
* **Ruolo**: campo booleano.
* **Contenuto tipico**: `True` o `False`.

#### `name`

* **Significato**: nome o etichetta dell'avviso.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il nome dell'avviso.

#### `is_recursive`

* **Significato**: indica se l'avviso deve ripetersi a intervalli stabiliti.
* **Ruolo**: campo booleano.
* **Contenuto tipico**: `True` o `False`.

#### `is_active`

* **Significato**: indica se l'avviso è attualmente attivo.
* **Ruolo**: campo booleano.
* **Contenuto tipico**: `True` o `False`.

#### `priority`

* **Significato**: livello di priorità dell'avviso.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: possono essere stringhe come 'High', 'Medium', 'Low'; i dati di esempio mostrano `None`.

#### `email_template_id`

* **Significato**: identificatore del modello e-mail utilizzato per l'avviso.
* **Ruolo**: chiave esterna (presunta).
* **Contenuto tipico**: di norma un UUID; i dati di esempio mostrano `None`, il che indica che questo campo potrebbe essere facoltativo.
