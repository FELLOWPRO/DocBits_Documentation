# Tfidf preferences

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `tfidf_id`: interno
* `pref_key`: interno
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: interno
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: interno
* `deleted_on`: timestamp with time zone
* `supplier_id`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.tfidf_preferences`

## Introduzione

La tabella `public.tfidf_preferences` sembra essere progettata per memorizzare le preferenze relative alle configurazioni o ai modelli TF-IDF (Term Frequency-Inverse Document Frequency). Questa tabella contiene informazioni sulle preferenze specifiche impostate dalle organizzazioni, comprese le chiavi di preferenza e i relativi valori, insieme ai metadati sulle attività di creazione, modifica ed eliminazione.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni record della tabella.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che rappresenta l'ID univoco di una voce di preferenza.

### org_id
- **Significato**: identificatore dell'organizzazione associata alla preferenza.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che collega la preferenza a una specifica organizzazione.

### tfidf_id
- **Significato**: identificatore della specifica configurazione o del modello TF-IDF.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta la configurazione TF-IDF collegata.

### pref_key
- **Significato**: la chiave o il nome dell'impostazione di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che rappresenta il nome della preferenza, come 'USE_ETEXT_IF_AVAILABLE' o 'AI_MODEL'.

### pref_value
- **Significato**: il valore associato alla chiave di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa o un valore di testo corrispondente alla chiave di preferenza, ad es. 'true', 'false' o 'Full'.

### created_by
- **Significato**: identificatore dell'utente che ha creato la voce di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un intero che rappresenta l'ID dell'utente autore.

### created_on
- **Significato**: timestamp di creazione della voce di preferenza.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica la data e l'ora di creazione.

### last_modified_by
- **Significato**: identificatore dell'utente che ha modificato per ultimo la voce di preferenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un UUID che rappresenta l'ID dell'ultimo utente che ha modificato la voce, se applicabile.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica della voce di preferenza.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica la data e l'ora dell'ultima modifica.

### is_deleted
- **Significato**: flag che indica se la voce di preferenza è stata contrassegnata come eliminata.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore booleano; `True` se la voce è eliminata, altrimenti `False`.

### deleted_by
- **Significato**: identificatore dell'utente che ha contrassegnato la voce di preferenza come eliminata.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un UUID che rappresenta l'ID dell'utente che ha eliminato la voce, se applicabile.

### deleted_on
- **Significato**: timestamp del momento in cui la voce di preferenza è stata contrassegnata come eliminata.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica quando la voce è stata eliminata.

### supplier_id
- **Significato**: identificatore del fornitore associato alla preferenza.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che rappresenta il fornitore collegato alla preferenza.

Questa documentazione offre una panoramica dettagliata dello scopo e della struttura della tabella `public.tfidf_preferences`, aiutando gli sviluppatori a comprendere come interagire con questi dati e utilizzarli in modo efficace.
```
