# Tipo di documento dell’organizzazione

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `document_type_id`: interno
* `document_type_key`: interno
* `document_locale`: interno
* `classification_method`: interno
* `is_active`: boolean
* `extraction_type`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `sub_org_id`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.organisation_document_type`

## Introduzione

La tabella `public.organisation_document_type` è progettata per gestire e memorizzare le informazioni sui vari tipi di documento associati alle organizzazioni. Include dettagli come la chiave del tipo di documento, la lingua (locale), i metodi di classificazione e lo stato del tipo di documento (attivo, eliminato, ecc.). Sembra fungere da mappatura tra le organizzazioni e i tipi di documento che queste utilizzano o gestiscono, insieme ai metadati relativi a tali documenti.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni record della tabella.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco una voce di tipo di documento.
- **Nota**: essenziale per distinguere ogni record.

### org_id
- **Significato**: identificatore dell'organizzazione relativa al tipo di documento.
- **Ruolo**: chiave esterna, che probabilmente fa riferimento a una tabella delle organizzazioni.
- **Contenuto tipico**: una stringa UUID.
- **Nota**: collega il tipo di documento a una specifica organizzazione.

### document_type_id
- **Significato**: identificatore del tipo di documento.
- **Ruolo**: chiave esterna, possibilmente collegata a una tabella di riferimento dei tipi di documento.
- **Contenuto tipico**: una stringa UUID.
- **Nota**: consente la mappatura a specifici tipi di documento.

### document_type_key
- **Significato**: una chiave o un codice che rappresenta il tipo di documento.
- **Ruolo**: campo descrittivo per la classificazione del tipo di documento.
- **Contenuto tipico**: una stringa che funge da identificatore o etichetta del tipo di documento.
- **Nota**: utilizzata per identificare il tipo di documento in una forma leggibile.

### document_locale
- **Significato**: impostazione di lingua o locale per il tipo di documento.
- **Ruolo**: campo descrittivo per la specifica del locale.
- **Contenuto tipico**: una stringa, spesso 'auto', che indica la determinazione automatica del locale.
- **Nota**: utile per scopi di internazionalizzazione e localizzazione.

### classification_method
- **Significato**: metodo utilizzato per classificare il tipo di documento.
- **Ruolo**: campo descrittivo che indica come viene classificato il documento.
- **Contenuto tipico**: una stringa, spesso 'auto', che suggerisce una classificazione automatica.
- **Nota**: importante per comprendere il processo di classificazione.

### is_active
- **Significato**: stato che indica se il tipo di documento è attivo.
- **Ruolo**: campo di stato booleano.
- **Contenuto tipico**: `True` o `False`.
- **Nota**: determina se il tipo di documento è attualmente in uso.

### extraction_type
- **Significato**: tipo di metodo di estrazione utilizzato per il documento.
- **Ruolo**: campo descrittivo per il processo di estrazione.
- **Contenuto tipico**: stringhe come 'FIX_COORDINATES', 'FLEX_COORDINATES' oppure `None`.
- **Nota**: fornisce indicazioni su come vengono estratti i dati dai documenti.

### created_by
- **Significato**: identificatore dell'utente che ha creato il record.
- **Ruolo**: campo tecnico a fini di audit.
- **Contenuto tipico**: un intero che rappresenta l'ID di un utente.
- **Nota**: utile per tracciare le modifiche e le responsabilità.

### created_on
- **Significato**: timestamp di creazione del record.
- **Ruolo**: campo tecnico a fini di audit.
- **Contenuto tipico**: un timestamp con fuso orario.
- **Nota**: importante per tracciare la data e l'ora di creazione del record.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica del record.
- **Ruolo**: campo tecnico a fini di audit.
- **Contenuto tipico**: un timestamp con fuso orario.
- **Nota**: utile per tracciare gli aggiornamenti e le modifiche del record.

### is_deleted
- **Significato**: stato che indica se il record è stato contrassegnato come eliminato.
- **Ruolo**: campo di stato booleano.
- **Contenuto tipico**: `True` o `False`.
- **Nota**: aiuta a implementare la funzionalità di eliminazione logica (soft delete).

### sub_org_id
- **Significato**: identificatore di una sottorganizzazione relativa al tipo di documento.
- **Ruolo**: possibile chiave esterna, che aggiunge una struttura organizzativa gerarchica.
- **Contenuto tipico**: una stringa UUID oppure `None`.
- **Nota**: fornisce un contesto aggiuntivo sulla struttura dell'organizzazione.

```
