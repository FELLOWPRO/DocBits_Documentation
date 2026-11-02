# Sottotipo di documento

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `name`: interno
* `title`: interno
* `translation_key`: interno
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean

## Analisi e descrizione

```markdown
# Tabella `public.sub_document_type`

## Introduzione

La tabella `sub_document_type` è progettata per memorizzare informazioni dettagliate sui vari sottotipi di documento all'interno di un'organizzazione. Comprende identificatori univoci, associazioni organizzative, nomi descrittivi e metadati relativi alla creazione e alla modifica di questi sottotipi di documento. La tabella mantiene inoltre lo stato di eliminazione logica (soft delete) dei record.

## Descrizione delle colonne

### id
- **Significato**: questa colonna memorizza l'identificatore univoco di ogni sottotipo di documento.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco un record di sottotipo di documento (ad es. `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Significato**: questa colonna indica l'organizzazione a cui appartiene il sottotipo di documento.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che fa riferimento a un'organizzazione (ad es. `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Significato**: rappresenta la chiave del tipo di documento associata al sottotipo di documento.
- **Ruolo**: chiave esterna (implicita nella convenzione di denominazione).
- **Contenuto tipico**: una chiave stringa che rimanda a un tipo di documento più ampio (ad es. `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Significato**: indica una chiave specifica per il sottotipo di documento all'interno di una categoria di documenti.
- **Ruolo**: identificatore univoco del sottotipo di documento nell'ambito di un tipo di documento.
- **Contenuto tipico**: una chiave stringa che identifica in modo univoco un sottotipo di documento (ad es. `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Significato**: memorizza un nome breve o un codice per il sottotipo di documento.
- **Ruolo**: descrittivo.
- **Contenuto tipico**: un identificatore o codice sintetico (ad es. `'TEST_SUB_TEST'`).

### title
- **Significato**: contiene un titolo leggibile per il sottotipo di documento.
- **Ruolo**: descrittivo.
- **Contenuto tipico**: un titolo descrittivo per le interfacce utente o i report (ad es. `'Test Sub Test'`).

### translation_key
- **Significato**: chiave utilizzata per l'internazionalizzazione e la localizzazione, per tradurre il nome del sottotipo di documento.
- **Ruolo**: tecnico.
- **Contenuto tipico**: una stringa utilizzata nei file di traduzione (ad es. `'test_sub_test'`).

### created_by
- **Significato**: identifica l'utente che ha creato la voce del sottotipo di documento.
- **Ruolo**: tecnico.
- **Contenuto tipico**: un intero che rappresenta l'ID dell'utente (ad es. `8`).

### created_on
- **Significato**: timestamp che indica quando è stato creato il sottotipo di documento.
- **Ruolo**: tecnico.
- **Contenuto tipico**: un timestamp con fuso orario (ad es. `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Significato**: timestamp che indica quando il sottotipo di documento è stato modificato per l'ultima volta.
- **Ruolo**: tecnico.
- **Contenuto tipico**: un timestamp con fuso orario, eventualmente `None` se mai modificato dopo la creazione.

### is_deleted
- **Significato**: flag booleano che indica se il sottotipo di documento è stato eliminato logicamente (soft delete).
- **Ruolo**: tecnico.
- **Contenuto tipico**: `True` o `False` per indicare lo stato di eliminazione (ad es. `False`).
```
