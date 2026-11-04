# Configurazione del campo di ricerca

## Tabella `public.lookup_field_configuration`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `lookup_rec_id`: interno
* `field_id`: interno
* `lookup_field`: interno
* `is_searchable`: boolean
* `parent_field_id`: interno
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `deleted_on`: timestamp con fuso orario
* `search_operator`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Analisi e descrizione

## Documentazione della tabella: `public.lookup_field_configuration`

### Introduzione

La tabella `public.lookup_field_configuration` sembra essere una tabella di configurazione utilizzata per definire e gestire i campi lookup all'interno di un'applicazione. La tabella include metadati su ciascun campo, come il suo identificatore, l'organizzazione associata, la ricercabilità e le informazioni di audit. Fa probabilmente parte di un sistema più ampio per la gestione di campi dinamici o definiti dall'utente, che consente funzionalità complesse di interrogazione e configurazione.

### Descrizione delle colonne

#### `id`

* **Significato**: l'identificatore univoco di ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni voce di configurazione.

#### `org_id`

* **Significato**: l'identificatore dell'organizzazione a cui è associata questa configurazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione.

#### `lookup_rec_id`

* **Significato**: un identificatore del record lookup specifico a cui si applica questa configurazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che fa riferimento a un record lookup specifico.

#### `field_id`

* **Significato**: l'identificatore del campo che viene configurato.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che fa riferimento a un determinato campo.

#### `lookup_field`

* **Significato**: il nome o l'etichetta del campo che viene configurato.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta il nome del campo, come "address\_1" o "taxratefree".

#### `is_searchable`

* **Significato**: indica se il campo può essere incluso nelle operazioni di ricerca.
* **Ruolo**: flag di configurazione.
* **Contenuto tipico**: un valore booleano (`True` o `False`).

#### `parent_field_id`

* **Significato**: identificatore del campo padre, se applicabile.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID oppure `None` se non esiste un campo padre.

#### `auto_trigger`

* **Significato**: specifica se la configurazione del campo deve attivare automaticamente determinate azioni.
* **Ruolo**: flag di configurazione.
* **Contenuto tipico**: un valore booleano (`True` o `False`).

#### `created_by`

* **Significato**: l'identificatore dell'utente che ha creato la voce di configurazione.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: un intero che rappresenta l'ID dell'utente.

#### `created_on`

* **Significato**: il timestamp di creazione della voce di configurazione.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.

#### `last_modified_on`

* **Significato**: il timestamp della modifica più recente della voce di configurazione.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, oppure `None` se non è mai stata modificata.

#### `is_deleted`

* **Significato**: indica se la voce di configurazione è stata contrassegnata come eliminata.
* **Ruolo**: flag di eliminazione logica (soft delete).
* **Contenuto tipico**: un valore booleano (`True` o `False`).

#### `deleted_on`

* **Significato**: il timestamp del momento in cui la voce di configurazione è stata contrassegnata come eliminata.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, oppure `None` se non eliminata.

#### `search_operator`

* **Significato**: definisce l'operatore di ricerca utilizzato per il campo.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: una stringa come "contains" che indica il tipo di operazione di ricerca.

#### `last_modified_by`

* **Significato**: identificatore dell'utente che ha modificato per ultimo la voce di configurazione.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: una stringa UUID oppure `None` se non è mai stata modificata.

#### `deleted_by`

* **Significato**: identificatore dell'utente che ha contrassegnato la voce come eliminata.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: una stringa UUID oppure `None` se non eliminata.

Questa documentazione offre una visione dettagliata della struttura e dello scopo di ciascuna colonna della tabella `public.lookup_field_configuration`, fornendo agli sviluppatori una comprensione completa di come vengono configurati e gestiti i campi lookup nel sistema.
