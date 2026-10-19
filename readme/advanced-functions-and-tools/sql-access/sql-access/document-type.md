# Document type

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `document_key`: interno
* `document_name`: interno
* `title`: interno
* `translation_key`: interno
* `extraction_type`: interno
* `document_type_category`: interno
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analisi e descrizione

```markdown
# Tabella: public.document_type

## Introduzione
La tabella `public.document_type` è progettata per memorizzare le informazioni relative ai vari tipi di documento all'interno di un'organizzazione. Comprende identificatori e metadati per la categorizzazione, la gestione e l'elaborazione dei documenti, come chiavi del documento, nomi, titoli, chiavi di traduzione e altri attributi che facilitano la gestione e il recupero dei documenti. La tabella traccia inoltre la creazione e la modifica di queste voci, supportando sia lo stato attivo sia quello eliminato.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni voce di tipo di documento.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco una voce di tipo di documento.

### org_id
- **Significato**: identificatore dell'organizzazione a cui appartiene il tipo di documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che fa riferimento a un'organizzazione.

### document_key
- **Significato**: una chiave univoca per identificare il tipo di documento, potenzialmente utilizzata nei sistemi di archiviazione o di elaborazione dei documenti.
- **Ruolo**: identificatore.
- **Contenuto tipico**: una stringa che combina le informazioni sul tipo di documento con l'ID dell'organizzazione.

### document_name
- **Significato**: il nome interno del tipo di documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa in maiuscolo che rappresenta il nome del tipo di documento.

### title
- **Significato**: il titolo visualizzato del tipo di documento nelle interfacce utente.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa in formato titolo, leggibile e descrittiva del tipo di documento.

### translation_key
- **Significato**: una chiave utilizzata per localizzare il titolo o il nome del documento in diverse lingue.
- **Ruolo**: supporto all'internazionalizzazione.
- **Contenuto tipico**: una stringa in minuscolo che funge da riferimento per i sistemi di traduzione.

### extraction_type
- **Significato**: indica il metodo o il processo con cui i dati vengono estratti dal documento.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: attualmente non valorizzato nei dati di esempio.

### document_type_category
- **Significato**: classifica il tipo di documento in categorie o classificazioni più ampie.
- **Ruolo**: campo di categorizzazione.
- **Contenuto tipico**: attualmente non valorizzato nei dati di esempio.

### has_table
- **Significato**: indica se il tipo di documento comprende dati tabellari.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: valore booleano (`True` o `False`) che indica la presenza di dati tabellari.

### sort_order
- **Significato**: definisce l'ordine in cui i tipi di documento vengono ordinati o visualizzati.
- **Ruolo**: campo di ordinamento.
- **Contenuto tipico**: un numero intero che rappresenta la sequenza di ordinamento.

### created_by
- **Significato**: identificatore dell'utente che ha creato la voce di tipo di documento.
- **Ruolo**: campo di metadati.
- **Contenuto tipico**: un numero intero che fa riferimento a un ID utente.

### created_on
- **Significato**: timestamp che indica quando è stata creata la voce di tipo di documento.
- **Ruolo**: campo di audit.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario.

### last_modified_on
- **Significato**: timestamp che indica la data dell'ultima modifica della voce di tipo di documento.
- **Ruolo**: campo di audit.
- **Contenuto tipico**: data e ora con informazioni sul fuso orario, `None` se mai modificata.

### is_deleted
- **Significato**: indica se la voce di tipo di documento è contrassegnata come eliminata.
- **Ruolo**: campo di stato.
- **Contenuto tipico**: valore booleano (`True` o `False`) che indica lo stato di eliminazione.
```
