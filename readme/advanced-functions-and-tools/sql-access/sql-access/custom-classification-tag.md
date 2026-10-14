# Custom classification tag

## Tabella `public.custom_classification_tag`

### Colonne

* `id`: integer
* `org_id`: ID dell'organizzazione
* `name`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.custom_classification_tag`

### Introduzione

La tabella `public.custom_classification_tag` è progettata per gestire i tag di classificazione personalizzati all'interno di un'organizzazione. Raccoglie le informazioni essenziali su ciascun tag, tra cui l'associazione a un'organizzazione, i dettagli di creazione e modifica e lo stato del ciclo di vita.

### Descrizione delle colonne

#### id

* **Significato**: un identificatore univoco per ogni tag di classificazione.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: un valore intero che identifica in modo univoco ogni record della tabella.

#### org\_id

* **Significato**: l'identificatore dell'organizzazione a cui appartiene il tag di classificazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa di caratteri, probabilmente un UUID, che rappresenta l'ID univoco dell'organizzazione.

#### name

* **Significato**: il nome o l'etichetta del tag di classificazione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che indica il nome o la descrizione del tag. Può essere una stringa vuota se il nome non è stato indicato.

#### created\_by

* **Significato**: l'identificatore dell'utente che ha creato il tag di classificazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un numero intero che rappresenta l'ID utente del creatore.

#### created\_on

* **Significato**: il timestamp che indica quando è stato creato il tag di classificazione.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp con fuso orario che registra la data e l'ora esatte di creazione.

#### last\_modified\_on

* **Significato**: il timestamp dell'ultima modifica apportata al tag di classificazione.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp con fuso orario, che può essere `None` se dopo la creazione non sono state effettuate modifiche.

#### is\_deleted

* **Significato**: un flag che indica se il tag di classificazione è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un valore booleano (`True` o `False`), dove `False` significa che il tag è attivo e `True` indica che è stato eliminato o disattivato.
