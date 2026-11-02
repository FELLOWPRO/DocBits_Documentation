# public.document\_log

## Tabella `public.document_log`

### Colonne

* `id`: integer
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `action_type`: interno
* `action_description`: text
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: interno
* `current_status`: interno

### Analisi e descrizione

## Documentazione tecnica: tabella `public.document_log`

### Introduzione

La tabella `public.document_log` è progettata per tracciare la cronologia e i cambi di stato dei documenti all'interno di un'organizzazione. Registra le azioni eseguite sui documenti, come gli aggiornamenti di stato, insieme ai dettagli sull'utente che ha eseguito l'azione e ai timestamp che indicano quando tali azioni sono avvenute. Questa tabella è fondamentale per l'audit dei flussi di elaborazione dei documenti e per comprendere il ciclo di vita di ciascun documento.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni voce di log.
* **Ruolo**: chiave primaria. Questa colonna funge da identificatore univoco di ogni record della tabella.
* **Contenuto tipico**: valori interi che si incrementano a ogni nuova voce.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata al documento.
* **Ruolo**: chiave esterna. Rimanda a un'entità organizzazione, anche se non definita esplicitamente in questo contesto.
* **Contenuto tipico**: stringhe di caratteri, probabilmente UUID, che rappresentano gli identificatori delle organizzazioni.

#### doc\_id

* **Significato**: identificatore del documento associato alla voce di log.
* **Ruolo**: chiave esterna. Questa colonna fa riferimento a un documento specifico nel sistema.
* **Contenuto tipico**: stringhe di caratteri, probabilmente UUID, che rappresentano gli identificatori dei documenti.

#### action\_type

* **Significato**: tipo di azione registrata.
* **Ruolo**: campo descrittivo. Indica la categoria dell'azione eseguita.
* **Contenuto tipico**: stringhe come `STATUS_CHANGE`, che indicano la natura dell'azione.

#### action\_description

* **Significato**: descrizione dettagliata dell'azione eseguita.
* **Ruolo**: campo descrittivo. Fornisce contesto o dettagli sull'azione.
* **Contenuto tipico**: descrizioni testuali, ad es. "Data extraction started", "Error occurred processing document".

#### created\_by

* **Significato**: identificatore dell'utente che ha creato la voce di log.
* **Ruolo**: chiave esterna. Rimanda a un'entità utente e indica chi ha eseguito l'azione.
* **Contenuto tipico**: valori interi che rappresentano gli identificatori degli utenti.

#### created\_on

* **Significato**: timestamp di creazione della voce di log.
* **Ruolo**: campo tecnico. Registra l'ora esatta in cui un'azione è stata registrata.
* **Contenuto tipico**: timestamp con informazioni sul fuso orario, ad es. `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica della voce di log.
* **Ruolo**: campo tecnico. Indica l'ora dell'ultimo aggiornamento della voce di log.
* **Contenuto tipico**: timestamp, potenzialmente null se non modificata dopo la creazione.

#### is\_deleted

* **Significato**: flag che indica se la voce di log è contrassegnata come eliminata.
* **Ruolo**: campo tecnico. Utilizzato per l'eliminazione logica delle voci.
* **Contenuto tipico**: valori booleani, `False` per le voci attive e `True` per quelle eliminate.

#### is\_hidden

* **Significato**: flag che indica se la voce di log è nascosta nella visualizzazione normale.
* **Ruolo**: campo tecnico. Utilizzato per controllare la visibilità delle voci di log.
* **Contenuto tipico**: valori booleani, `False` per le voci visibili e `True` per quelle nascoste.

#### previous\_status

* **Significato**: stato del documento prima dell'esecuzione dell'azione.
* **Ruolo**: campo descrittivo. Fornisce lo stato del documento precedente all'azione registrata.
* **Contenuto tipico**: stringhe come `new`, `validating`, `running`, che rappresentano gli stati del documento.

#### current\_status

* **Significato**: stato del documento dopo l'esecuzione dell'azione.
* **Ruolo**: campo descrittivo. Indica lo stato aggiornato del documento in seguito all'azione.
* **Contenuto tipico**: stringhe come `running`, `ready_for_validation`, `error`, che rappresentano gli stati del documento.

Questa documentazione offre una panoramica della tabella `public.document_log`, illustrando lo scopo e la struttura di ciascuna colonna, aspetti fondamentali per gli sviluppatori che gestiscono i flussi di lavoro dei documenti e mantengono le tracce di audit.
