# Modello e-mail

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `name`: interno
* `email_type`: interno
* `value`: text
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `deleted_on`: timestamp con fuso orario
* `subject`: interno
* `last_modified_by`: interno
* `deleted_by`: interno
* `doc_type`: tipo di documento

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.email_template`

## Introduzione

La tabella `public.email_template` è progettata per memorizzare i modelli e-mail utilizzati nel sistema. Questi modelli sono associati a diverse organizzazioni e vengono probabilmente utilizzati per inviare comunicazioni e-mail standardizzate. La tabella contiene i metadati dei modelli, inclusi i dettagli di creazione e modifica, e traccia inoltre se un modello è stato eliminato.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni modello e-mail.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID come `da34c6ed-e659-4392-91ea-3c89f9602198`.
- **Nota**: funge da identificatore principale del record del modello.

### org_id
- **Significato**: identificatore dell'organizzazione associata al modello e-mail.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID.
- **Nota**: collega il modello a una specifica organizzazione.

### name
- **Significato**: il nome del modello e-mail.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: testo descrittivo come `Supplier Magic Link Email`.
- **Nota**: utilizzato per identificare lo scopo del modello.

### email_type
- **Significato**: tipo o categoria del modello e-mail.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe come `supplier_invite`.
- **Nota**: indica il contesto o l'utilizzo del modello.

### value
- **Significato**: il contenuto del modello e-mail, di norma in formato HTML.
- **Ruolo**: campo di contenuto.
- **Contenuto tipico**: stringa HTML contenente il layout e il contenuto dell'e-mail.
- **Nota**: è il modello effettivamente utilizzato nelle e-mail.

### created_by
- **Significato**: identificatore dell'utente che ha creato il modello.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un numero intero che rappresenta un ID utente.
- **Nota**: traccia chi ha creato il modello.

### created_on
- **Significato**: timestamp di creazione del modello.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un timestamp come `2024-07-18 13:29:59 UTC`.
- **Nota**: registra la data e l'ora di creazione.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica del modello.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un timestamp.
- **Nota**: traccia l'aggiornamento più recente del modello.

### is_deleted
- **Significato**: indica se il modello è contrassegnato come eliminato.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano, `True` o `False`.
- **Nota**: utilizzato per l'eliminazione logica del modello.

### deleted_on
- **Significato**: timestamp in cui il modello è stato contrassegnato come eliminato.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un timestamp oppure `None` se non eliminato.
- **Nota**: registra quando il modello è stato eliminato.

### subject
- **Significato**: la riga dell'oggetto del modello e-mail.
- **Ruolo**: campo di contenuto.
- **Contenuto tipico**: testo come `Welcome to Testing Ruiz Foods Supplier Portal. Let's help you get set up`.
- **Nota**: utilizzato come oggetto dell'e-mail quando il modello viene inviato.

### last_modified_by
- **Significato**: identificatore dell'utente che ha modificato per ultimo il modello.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un identificatore utente.
- **Nota**: traccia chi ha modificato per ultimo il modello.

### deleted_by
- **Significato**: identificatore dell'utente che ha contrassegnato il modello come eliminato.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un identificatore utente.
- **Nota**: registra chi ha eliminato il modello.

### doc_type
- **Significato**: tipo o formato del documento correlato al modello.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe che indicano il tipo di documento.
- **Nota**: potrebbe riferirsi al formato o alla categoria del contenuto dell'e-mail.
```
