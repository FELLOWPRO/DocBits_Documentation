# Document type attributes

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `attribute_key`: interno
* `attribute_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.document_type_attributes`

## Introduzione

La tabella `public.document_type_attributes` è progettata per gestire gli attributi relativi ai vari tipi di documento in un contesto organizzativo. Questa tabella supporta probabilmente la gestione della configurazione o dei metadati per diversi tipi di documento, come fatture o documenti di trasporto, associando attributi specifici a ciascun tipo di documento.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni record della tabella.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco una riga della tabella.

### org_id
- **Significato**: rappresenta l'organizzazione a cui appartiene l'attributo del tipo di documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che fa riferimento a un'organizzazione.

### doc_type_key
- **Significato**: il tipo di documento a cui si applica l'attributo (ad esempio INVOICE, DELIVERY_NOTE).
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che rappresenta un tipo di documento.

### sub_doc_type_key
- **Significato**: una categorizzazione più specifica all'interno del tipo di documento, se applicabile.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: di norma `None`, a indicare che potrebbe non essere sempre utilizzato.

### attribute_key
- **Significato**: la chiave dello specifico attributo o proprietà relativa al tipo di documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che rappresenta una chiave di attributo, come `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Significato**: il valore associato alla chiave dell'attributo per il tipo di documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un valore stringa o numerico che fornisce il valore dell'attributo, ad esempio `true`, `123`.

### created_by
- **Significato**: l'identificatore dell'utente che ha creato il record.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un numero intero che rappresenta un ID utente.

### created_on
- **Significato**: il timestamp di creazione del record.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica quando il record è stato creato.

### last_modified_on
- **Significato**: il timestamp dell'ultima modifica apportata al record.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario che indica l'ora dell'ultimo aggiornamento.

### is_deleted
- **Significato**: indica se il record è contrassegnato come eliminato.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un valore booleano, dove `false` implica che il record è attivo.

### sub_org_id
- **Significato**: rappresenta una sotto-organizzazione all'interno dell'organizzazione principale, se applicabile.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: di norma `None`, a indicare che potrebbe non essere sempre utilizzato.
```

Questa documentazione offre una panoramica strutturata della tabella `public.document_type_attributes`, consentendo agli sviluppatori di comprendere lo scopo e l'utilizzo di ciascuna colonna.
