# Configurazione delle ricerche

## Tabella `public.lookup_configuration`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type`: tipo di documento
* `lookup_dataset_name`: interno
* `lookup_name`: interno
* `conflict_handle`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `deleted_on`: timestamp con fuso orario
* `match_all`: boolean
* `last_modified_by`: interno
* `deleted_by`: interno
* `context`: interno
* `context_detail`: interno

### Analisi e descrizione

## Documentazione tecnica della tabella `public.lookup_configuration`

### Introduzione

La tabella `public.lookup_configuration` è progettata per memorizzare le impostazioni di configurazione di varie operazioni di ricerca dati (lookup) all'interno di un'organizzazione. Contiene informazioni sull'organizzazione, sul tipo di documenti coinvolti e sui dataset e nomi specifici utilizzati per le ricerche. La tabella tiene inoltre traccia della creazione e della modifica di queste configurazioni, nonché del loro stato attuale (attiva o eliminata).

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni voce di configurazione lookup nella tabella.
* **Ruolo**: chiave primaria che identifica in modo univoco ogni riga.
* **Contenuto tipico**: valori UUID, ad es. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Significato**: rappresenta l'organizzazione associata alla configurazione lookup.
* **Ruolo**: chiave esterna, collegata a un'organizzazione in un'altra tabella.
* **Contenuto tipico**: valori UUID che indicano gli identificatori delle organizzazioni, ad es. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Significato**: specifica il tipo di documento a cui si applica la configurazione lookup.
* **Ruolo**: campo descrittivo che indica il contesto della configurazione.
* **Contenuto tipico**: stringhe come `'MEDI_ORDER'`, `'INVOICE'`, ecc.

#### lookup\_dataset\_name

* **Significato**: il nome del dataset utilizzato per eseguire le ricerche.
* **Ruolo**: campo descrittivo utilizzato per identificare i dataset.
* **Contenuto tipico**: stringhe descrittive come `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Significato**: il nome specifico o l'alias utilizzato per l'operazione di ricerca.
* **Ruolo**: campo descrittivo che indica il nome operativo.
* **Contenuto tipico**: stringhe come `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Significato**: indica la strategia per gestire i conflitti durante le ricerche.
* **Ruolo**: campo descrittivo per la strategia di risoluzione dei conflitti.
* **Contenuto tipico**: valori come `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Significato**: l'ID dell'utente che ha creato la configurazione lookup.
* **Ruolo**: campo tecnico per tracciare l'autore della voce.
* **Contenuto tipico**: valori interi che rappresentano ID di utenti, ad es. `1`.

#### created\_on

* **Significato**: timestamp di creazione della configurazione lookup.
* **Ruolo**: campo tecnico per tracciare il momento di creazione.
* **Contenuto tipico**: timestamp, ad es. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica apportata alla configurazione lookup.
* **Ruolo**: campo tecnico per tracciare il momento dell'ultimo aggiornamento.
* **Contenuto tipico**: timestamp, in genere `None` se non modificata.

#### is\_deleted

* **Significato**: indica se la configurazione lookup è stata contrassegnata come eliminata.
* **Ruolo**: campo booleano per il tracciamento dello stato.
* **Contenuto tipico**: valori booleani, `False` per le voci attive.

#### deleted\_on

* **Significato**: timestamp del momento in cui la configurazione lookup è stata contrassegnata come eliminata.
* **Ruolo**: campo tecnico per tracciare il momento dell'eliminazione.
* **Contenuto tipico**: spesso impostato su una data segnaposto, ad es. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Significato**: specifica se la ricerca deve soddisfare tutte le condizioni.
* **Ruolo**: campo booleano per le impostazioni di configurazione.
* **Contenuto tipico**: valori booleani, in genere `False`.

#### last\_modified\_by

* **Significato**: l'ID dell'utente che ha modificato per ultimo la configurazione lookup.
* **Ruolo**: campo tecnico per tracciare l'utente che ha aggiornato per ultimo la voce.
* **Contenuto tipico**: UUID o identificatore dell'utente che ha effettuato la modifica, spesso `None`.

#### deleted\_by

* **Significato**: l'ID dell'utente che ha contrassegnato la configurazione lookup come eliminata.
* **Ruolo**: campo tecnico per tracciare l'utente responsabile dell'eliminazione.
* **Contenuto tipico**: UUID o identificatore, spesso `None`.

#### context

* **Significato**: il contesto in cui viene applicata la ricerca, ad esempio una sezione di un documento.
* **Ruolo**: campo descrittivo per il contesto operativo.
* **Contenuto tipico**: stringhe come `'header'`.

#### context\_detail

* **Significato**: dettagli aggiuntivi sul contesto della ricerca.
* **Ruolo**: campo descrittivo per informazioni di contesto estese.
* **Contenuto tipico**: spesso `None`, utilizzato per una descrizione supplementare del contesto.
