# Documento di test automatico

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_id`: interno
* `doc_type`: tipo di documento
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `filename`: interno

## Analisi e descrizione

```markdown
# Documentazione della tabella: `public.auto_test_document`

## Introduzione

La tabella `public.auto_test_document` è progettata per memorizzare i metadati e i risultati di estrazione dell'elaborazione dei documenti all'interno di un'organizzazione. La tabella raccoglie informazioni sui documenti, sui loro tipi e sui dati estratti. Include campi per l'identificazione del documento, i metadati di elaborazione e i flag di stato, essenziali per gestire i flussi di lavoro dei documenti e garantire l'integrità dei dati.

## Descrizione delle colonne

### id
- **Significato**: identificatore univoco di ogni voce di documento nella tabella.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: stringa UUID.
- **Nota**: funge da identificatore univoco dei record e garantisce che ogni voce sia distinta.

### org_id
- **Significato**: identificatore dell'organizzazione associata al documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: stringa UUID.
- **Nota**: collega il documento a una specifica organizzazione del sistema.

### doc_id
- **Significato**: identificatore del documento in elaborazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: stringa UUID.
- **Nota**: utilizzato per associare i dati estratti al documento originale.

### doc_type
- **Significato**: tipo o categoria del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa come "MEDI_ORDER".
- **Nota**: aiuta a classificare i documenti per l'elaborazione e l'analisi.

### extracted_data
- **Significato**: struttura JSON contenente i dati dettagliati estratti dal documento.
- **Ruolo**: campo dati.
- **Contenuto tipico**: testo JSON con campi, valori e metadati di estrazione.
- **Nota**: memorizza i risultati del processo di estrazione dei dati del documento.

### created_by
- **Significato**: identificatore dell'utente che ha creato il record del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: numero intero che rappresenta l'ID di un utente.
- **Nota**: traccia quale utente ha avviato l'inserimento del documento nel sistema.

### created_on
- **Significato**: timestamp che indica quando è stato creato il record del documento.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario.
- **Nota**: utile per l'audit e per tracciare il ciclo di vita del documento.

### last_modified_on
- **Significato**: timestamp che indica l'ultima modifica apportata al record del documento.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario.
- **Nota**: aiuta a tracciare modifiche e aggiornamenti del record del documento.

### is_deleted
- **Significato**: flag che indica se il record del documento è stato contrassegnato come eliminato.
- **Ruolo**: campo di stato.
- **Contenuto tipico**: valore booleano.
- **Nota**: facilita l'eliminazione logica dei record, consentendone il ripristino se necessario.

### filename
- **Significato**: nome del file associato al documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa, ad esempio "7.pdf".
- **Nota**: fornisce un riferimento al file fisico associato alla voce del documento.

```
