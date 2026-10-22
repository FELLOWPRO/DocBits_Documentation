# Custom\_classification\_document\_label

## Tabella `public.custom_classification_document_label`

### Colonne

* `id`: integer
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `label_id`: integer
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.custom_classification_document_label`

### Introduzione

La tabella `public.custom_classification_document_label` è progettata per gestire e memorizzare le associazioni tra i documenti e le rispettive etichette all'interno di un'organizzazione. Questa tabella facilita la categorizzazione e il recupero dei documenti in base a etichette personalizzate, offrendo un modo strutturato per gestire la classificazione dei documenti secondo le diverse esigenze organizzative.

### Descrizione delle colonne

#### id

* **Significato**: questa colonna funge da identificatore univoco di ogni record della tabella.
* **Ruolo**: chiave primaria
* **Contenuto tipico**: un valore intero che identifica in modo univoco ogni riga.
* **Nota**: ogni voce della tabella ha un `id` distinto per garantire l'integrità dei dati e consentire riferimenti efficienti.

#### org\_id

* **Significato**: rappresenta l'organizzazione a cui appartiene l'associazione documento-etichetta.
* **Ruolo**: chiave esterna
* **Contenuto tipico**: una stringa di caratteri, probabilmente un UUID, che identifica in modo univoco un'organizzazione.
* **Nota**: garantisce che l'associazione tra documenti ed etichette sia limitata al corretto contesto organizzativo.

#### doc\_id

* **Significato**: identifica il documento a cui viene applicata l'etichetta.
* **Ruolo**: chiave esterna
* **Contenuto tipico**: una stringa di caratteri, probabilmente un UUID, che identifica in modo univoco un documento.
* **Nota**: consente di collegare documenti specifici alle etichette, rendendo possibile la categorizzazione dei documenti.

#### label\_id

* **Significato**: fa riferimento all'etichetta applicata al documento.
* **Ruolo**: chiave esterna
* **Contenuto tipico**: un numero intero che fa riferimento a un'etichetta di una tabella di etichette separata.
* **Nota**: facilita l'associazione tra i documenti e le rispettive etichette.

#### created\_by

* **Significato**: identifica l'utente che ha creato il record.
* **Ruolo**: chiave esterna (potenzialmente verso una tabella utenti)
* **Contenuto tipico**: un numero intero che rappresenta l'ID utente.
* **Nota**: traccia l'origine di ogni associazione documento-etichetta a fini di audit e responsabilità.

#### created\_on

* **Significato**: indica quando è stato creato il record.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario.
* **Nota**: fornisce il contesto temporale di quando è stata stabilita la relazione documento-etichetta.

#### last\_modified\_on

* **Significato**: registra il timestamp dell'ultima modifica del record.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, può essere `None` se il record non è mai stato modificato.
* **Nota**: utile per tracciare la cronologia delle modifiche alle associazioni documento-etichetta.

#### is\_deleted

* **Significato**: segnala se il record è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un valore booleano (`True` o `False`).
* **Nota**: supporta le pratiche di eliminazione logica, consentendo la rimozione logica dei dati senza eliminarli fisicamente dal database.
