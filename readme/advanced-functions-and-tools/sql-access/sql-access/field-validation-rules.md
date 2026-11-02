# Regole di convalida dei campi

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `field_id`: interno
* `doc_type`: tipo di documento
* `is_sub_doc_type_field`: boolean
* `profile`: interno
* `field_name`: interno
* `field_length`: integer
* `field_label`: interno
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: interno
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `additional_attributes`: text

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.field_validation_rules`

## Introduzione

La tabella `public.field_validation_rules` sembra memorizzare i metadati e le regole di validazione dei campi associati a vari tipi di documento all'interno di un'organizzazione. Viene probabilmente utilizzata per garantire l'integrità e la coerenza dei dati in moduli o documenti, specificando requisiti come l'obbligatorietà di un campo, la sua lunghezza, la visibilità ed eventuali pattern di validazione da applicare.

## Descrizione delle colonne

### id
- **Significato**: un identificatore univoco per ogni regola di validazione del campo.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco un record.

### org_id
- **Significato**: identificatore dell'organizzazione a cui si applica la regola di validazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che fa riferimento a una specifica organizzazione.

### field_id
- **Significato**: identificatore dello specifico campo a cui è associata la regola di validazione.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: una stringa UUID che fa riferimento a un campo specifico.

### doc_type
- **Significato**: specifica il tipo di documento a cui è associata la regola di validazione del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che indica il tipo di documento (ad esempio `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Significato**: indica se il campo fa parte di un sottotipo di documento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### profile
- **Significato**: rappresenta il profilo o il contesto in cui viene applicata la validazione del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa come `DEFAULT`.

### field_name
- **Significato**: il nome del campo per cui è definita la regola di validazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che rappresenta il nome del campo (ad esempio `Test`).

### field_length
- **Significato**: la lunghezza massima consentita per il contenuto del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un numero intero che specifica il limite di caratteri.

### field_label
- **Significato**: l'etichetta o il nome visualizzato del campo nell'interfaccia utente.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: di norma null nei dati di esempio.

### is_required
- **Significato**: indica se il campo è obbligatorio per il documento.
- **Ruolo**: indicatore di vincolo.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### is_readonly
- **Significato**: specifica se il campo è modificabile o di sola lettura.
- **Ruolo**: indicatore di vincolo.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### is_hidden
- **Significato**: indica se il campo deve essere nascosto nell'interfaccia utente.
- **Ruolo**: indicatore di vincolo.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### force_validation
- **Significato**: determina se la validazione deve essere applicata a prescindere dalle altre condizioni.
- **Ruolo**: indicatore di vincolo.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### validation_pattern
- **Significato**: un pattern (probabilmente regex) a cui il contenuto del campo deve corrispondere.
- **Ruolo**: regola di validazione.
- **Contenuto tipico**: di norma null nei dati di esempio.

### confidence_threshold
- **Significato**: il livello minimo di confidenza richiesto per la validazione del campo.
- **Ruolo**: vincolo di validazione.
- **Contenuto tipico**: un valore intero che rappresenta la soglia di confidenza.

### match_score_threshold
- **Significato**: il punteggio minimo di corrispondenza richiesto per la validazione del contenuto del campo.
- **Ruolo**: vincolo di validazione.
- **Contenuto tipico**: un valore intero che rappresenta la soglia del punteggio di corrispondenza.

### created_by
- **Significato**: identificatore dell'utente che ha creato questa regola di validazione.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: un numero intero che rappresenta l'ID utente.

### created_on
- **Significato**: timestamp che indica quando è stata creata la regola di validazione.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario.

### last_modified_on
- **Significato**: timestamp che indica l'ultima modifica della regola di validazione.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: un timestamp con fuso orario, può essere null se mai modificata.

### is_deleted
- **Significato**: indica se la regola di validazione è stata contrassegnata come eliminata.
- **Ruolo**: indicatore di eliminazione logica.
- **Contenuto tipico**: valore booleano (`True` o `False`).

### additional_attributes
- **Significato**: memorizza attributi o metadati aggiuntivi associati alla regola di validazione del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: testo, spesso null nei dati di esempio.
```
