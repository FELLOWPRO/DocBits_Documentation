# Cache delle sotto-organizzazioni

## Tabella `public.sub_organisation_cache`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `name`: interno
* `description`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.sub_organisation_cache`

### Introduzione

La tabella `public.sub_organisation_cache` sembra memorizzare le informazioni in cache sulle sottorganizzazioni all'interno di una struttura organizzativa più ampia. Questa tabella funge probabilmente da archivio di metadati relativi alle sottorganizzazioni, con dettagli quali identificatori, nomi, descrizioni e timestamp di creazione e modifica. La tabella tiene inoltre traccia dello stato delle voci, ad esempio se sono state eliminate logicamente.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni voce della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID che identifica in modo univoco una voce della cache delle sottorganizzazioni.
* **Nota**: questo campo garantisce che ogni record possa essere referenziato in modo univoco.

#### org\_id

* **Significato**: identificatore dell'organizzazione principale a cui appartiene la sottorganizzazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rappresenta un riferimento a un record di organizzazione.
* **Nota**: collega la sottorganizzazione alla propria organizzazione principale.

#### name

* **Significato**: il nome della sottorganizzazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una breve stringa di testo, eventualmente un acronimo o un nome, che rappresenta la sottorganizzazione.
* **Nota**: utilizzato a fini di identificazione e visualizzazione.

#### description

* **Significato**: una breve descrizione o un dettaglio aggiuntivo sulla sottorganizzazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa di testo che fornisce maggiore contesto o dettagli relativi alla sottorganizzazione.
* **Nota**: può essere simile a `name` quando non sono disponibili informazioni dettagliate.

#### created\_by

* **Significato**: identificatore dell'utente o del sistema che ha creato la voce.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: un intero che rappresenta l'ID dell'utente che ha eseguito l'azione di creazione.
* **Nota**: utile per tracciare chi ha inizializzato il record.

#### created\_on

* **Significato**: timestamp di creazione della voce.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: una data e un'ora, incluso il fuso orario, che indicano quando il record è stato creato.
* **Nota**: fondamentale per comprendere la cronologia dell'inserimento dei dati.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica della voce.
* **Ruolo**: campo di audit.
* **Contenuto tipico**: una data e un'ora, incluso il fuso orario, che indicano l'aggiornamento più recente del record.
* **Nota**: consente di tracciare le modifiche nel tempo. Può essere `None` se non sono state apportate modifiche dopo la creazione.

#### is\_deleted

* **Significato**: indica se la voce è stata eliminata logicamente.
* **Ruolo**: campo di stato.
* **Contenuto tipico**: un valore booleano, `True` se la voce è contrassegnata come eliminata, altrimenti `False`.
* **Nota**: questo campo supporta l'eliminazione logica (soft delete), consentendo se necessario il ripristino delle voci eliminate.

Questa documentazione offre una panoramica dettagliata della struttura e dello scopo della tabella `public.sub_organisation_cache`, facilitandone la comprensione e l'uso da parte di sviluppatori e amministratori di database.
