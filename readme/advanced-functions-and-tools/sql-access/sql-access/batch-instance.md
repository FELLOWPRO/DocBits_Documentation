# Istanza di batch

## Tabella `public.batch_instance`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione della tabella: `public.batch_instance`

### Introduzione

La tabella `public.batch_instance` è progettata per memorizzare informazioni sulle varie istanze di batch all'interno di un'organizzazione. Contiene i principali metadati di ciascuna istanza, tra cui l'identificazione univoca, l'organizzazione di appartenenza e i dettagli di creazione e modifica. Questa tabella è essenziale per tracciare il ciclo di vita e la gestione delle istanze di batch, probabilmente in un'applicazione che si occupa di elaborazione batch.

### Colonne

#### `id`

* **Significato**: questa colonna memorizza l'identificatore univoco di ciascuna istanza di batch.
* **Ruolo**: chiave primaria (`id`).
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni istanza di batch, ad esempio `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Significato**: questa colonna memorizza l'identificatore dell'organizzazione associata all'istanza di batch.
* **Ruolo**: chiave esterna (`org_id`).
* **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione, ad esempio `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Significato**: questa colonna indica l'utente o l'entità di sistema che ha creato l'istanza di batch.
* **Ruolo**: possibile chiave esterna, che rimanda a una tabella utenti o simile.
* **Contenuto tipico**: un numero intero che rappresenta l'ID del creatore, ad esempio `1`.

#### `created_on`

* **Significato**: questa colonna registra il timestamp di creazione dell'istanza di batch.
* **Ruolo**: campo tecnico a fini di audit e tracciamento.
* **Contenuto tipico**: un timestamp con fuso orario, ad esempio `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Significato**: questa colonna riporta il timestamp dell'ultima modifica apportata all'istanza di batch.
* **Ruolo**: campo tecnico per l'audit delle modifiche.
* **Contenuto tipico**: di norma null, oppure un timestamp con fuso orario se sono state effettuate modifiche.

#### `is_deleted`

* **Significato**: questa colonna indica se l'istanza di batch è contrassegnata come eliminata.
* **Ruolo**: campo tecnico per l'eliminazione logica.
* **Contenuto tipico**: un valore booleano, di norma `False` se l'istanza è attiva, ad esempio `False`.

Questa documentazione offre una panoramica completa della tabella `public.batch_instance`, descrivendo lo scopo e la struttura di ciascuna colonna, fondamentale per gli sviluppatori che lavorano con questo modello di dati.
