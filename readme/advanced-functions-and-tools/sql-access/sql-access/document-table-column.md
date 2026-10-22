# Colonna della tabella del documento

## Colonne

* `id`: interno
* `document_table_id`: interno
* `table_name`: interno
* `org_id`: ID dell'organizzazione
* `column_name`: interno
* `column_type`: interno
* `title`: interno
* `translation_key`: interno
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.document_table_column`

## Introduzione

La tabella `public.document_table_column` è progettata per memorizzare i metadati delle colonne di varie tabelle relative ai documenti, come le tabelle delle fatture o dei documenti di trasporto. Questi metadati comprendono il nome, il tipo e le proprietà di ciascuna colonna, nonché gli identificatori organizzativi e tecnici. La tabella supporta la generazione e la gestione dinamica degli schemi dei documenti all'interno del sistema.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni voce di colonna nella tabella.
- **Ruolo**: chiave primaria.
- **Nota**: di norma una stringa UUID che identifica in modo univoco una riga di questa tabella.

### document_table_id
- **Significato**: fa riferimento alla tabella che contiene il documento di cui questa colonna fa parte.
- **Ruolo**: chiave esterna.
- **Nota**: probabilmente un UUID che rimanda a un'altra tabella in cui sono definite le tabelle dei documenti.

### table_name
- **Significato**: il nome della tabella del documento a cui appartiene questa colonna.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: nomi come `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Nota**: facilita la comprensione di quale struttura di documento appartenga la colonna.

### org_id
- **Significato**: identificatore dell'organizzazione che possiede o gestisce la tabella del documento.
- **Ruolo**: chiave esterna.
- **Nota**: di norma un UUID che rimanda a un'entità organizzazione.

### column_name
- **Significato**: il nome tecnico della colonna all'interno della sua tabella del documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: nomi come `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Nota**: rappresenta il nome effettivo del campo nella tabella del documento.

### column_type
- **Significato**: descrive il tipo di dati della colonna.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: `STRING`, `DATE`.
- **Nota**: indica il tipo di dati memorizzati nella colonna.

### title
- **Significato**: un titolo o un'etichetta leggibile per la colonna.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Nota**: utilizzato per mostrare i nomi delle colonne in modo comprensibile per l'utente.

### translation_key
- **Significato**: chiave utilizzata per l'internazionalizzazione e la localizzazione del titolo della colonna.
- **Ruolo**: campo tecnico.
- **Nota**: attualmente vuota nei dati di esempio, il che suggerisce un uso facoltativo.

### sort_order
- **Significato**: definisce l'ordine delle colonne quando vengono visualizzate.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: numeri interi come `16`, `5`.
- **Nota**: determina la sequenza delle colonne nella vista della tabella del documento.

### clean_field
- **Significato**: indica se la colonna contiene dati sanificati.
- **Ruolo**: flag booleano.
- **Contenuto tipico**: `True` o `False`.
- **Nota**: utilizzato per la validazione dei dati o per lo stato di pulizia.

### alphanumeric_field
- **Significato**: specifica se la colonna deve essere trattata come campo alfanumerico.
- **Ruolo**: flag booleano.
- **Contenuto tipico**: `True` o `False`.
- **Nota**: utile per la validazione dell'input o per scopi di formattazione.

### created_by
- **Significato**: identificatore dell'utente che ha creato questa voce di colonna.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: valori interi come `1`, `8`.
- **Nota**: rimanda a un utente o a un'entità di sistema responsabile della creazione.

### created_on
- **Significato**: timestamp di creazione della voce di colonna.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valori di data e ora in UTC.
- **Nota**: utile per l'audit e il tracciamento delle modifiche.

### last_modified_on
- **Significato**: timestamp dell'ultima modifica apportata alla voce di colonna.
- **Ruolo**: campo tecnico.
- **Nota**: attualmente `None` nei dati di esempio, a indicare che dopo la creazione non sono state effettuate modifiche.

### is_deleted
- **Significato**: indica se la voce di colonna è stata eliminata logicamente.
- **Ruolo**: flag booleano.
- **Contenuto tipico**: `True` o `False`.
- **Nota**: aiuta a gestire le eliminazioni logiche senza rimuovere fisicamente i dati.

```
