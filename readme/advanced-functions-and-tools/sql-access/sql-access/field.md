# Field

## Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `doc_type`: tipo di documento
* `is_sub_doc_type_field`: boolean
* `profile`: interno
* `field_name`: interno
* `field_type`: interno
* `title`: interno
* `translation_key`: interno
* `hide_label`: boolean
* `input_type`: interno
* `input_size`: interno
* `icon_left`: interno
* `icon_right`: interno
* `icon_above`: interno
* `group_id`: interno
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: interno
* `fuzzy_field`: interno
* `fuzzy_primary_field`: boolean
* `label_align`: interno
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: interno
* `coordinates`: interno
* `normalized_coordinates`: interno
* `threshold`: interno
* `reference_point`: interno
* `checkbox_group`: interno
* `list_of_values`: interno
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `costing_element`: interno
* `erp_field_name`: interno

## Analisi e descrizione

```markdown
# Documentazione tecnica della tabella `public.field`

## Introduzione

La tabella `public.field` sembra essere concepita per gestire i metadati e la configurazione dei diversi campi associati ai documenti, probabilmente nell'ambito assicurativo. Ogni riga della tabella sembra rappresentare la configurazione di un campo specifico, comprensiva del tipo, dell'etichetta, delle impostazioni di visibilità e di altre proprietà che determinano come il campo debba essere presentato ed elaborato.

## Colonne

### id
- **Significato**: identificatore univoco di ogni configurazione di campo.
- **Ruolo**: chiave primaria.
- **Contenuto tipico**: una stringa UUID che identifica in modo univoco ogni voce della tabella.

### org_id
- **Significato**: identificatore dell'organizzazione associata alla configurazione del campo.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: un UUID che fa riferimento a un'organizzazione.

### doc_type
- **Significato**: specifica il tipo di documento a cui è associato il campo.
- **Ruolo**: possibile chiave esterna o identificatore categoriale.
- **Contenuto tipico**: una stringa nel formato `INSURANCE_DOCUMENTS_<UUID>` che indica il tipo di documento.

### is_sub_doc_type_field
- **Significato**: indica se il campo è un sottotipo del tipo di documento.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### profile
- **Significato**: definisce potenzialmente il profilo o l'ambito del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: spesso vuoto o una breve descrizione testuale.

### field_name
- **Significato**: il nome interno del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: una stringa che rappresenta il nome del campo in un contesto tecnico (ad es. `Schadennummer`).

### field_type
- **Significato**: definisce il tipo di dati contenuti nel campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringhe descrittive come `STRING`, `AMOUNT`.

### title
- **Significato**: il titolo visualizzato per il campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: stringa in maiuscolo utilizzata per visualizzare l'etichetta del campo.

### translation_key
- **Significato**: chiave per la traduzione in diverse lingue.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: stringa in minuscolo che rappresenta la chiave di traduzione.

### hide_label
- **Significato**: indica se l'etichetta del campo deve essere nascosta nell'interfaccia utente.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### input_type
- **Significato**: specifica la modalità di inserimento del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: può essere vuoto o contenere stringhe che definiscono il tipo di input.

### input_size
- **Significato**: determina la dimensione del campo di input.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: può essere vuoto o contenere stringhe che definiscono la dimensione dell'input.

### icon_left
- **Significato**: icona da visualizzare a sinistra del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene identificatori di icone.

### icon_right
- **Significato**: icona da visualizzare a destra del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene identificatori di icone.

### icon_above
- **Significato**: icona da visualizzare sopra il campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene identificatori di icone.

### group_id
- **Significato**: identificatore del gruppo di campi a cui appartiene questo campo.
- **Ruolo**: chiave esterna.
- **Contenuto tipico**: un UUID che fa riferimento a un gruppo di campi.

### row_order
- **Significato**: determina l'ordine del campo in un elenco o in un modulo.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: intero che indica la posizione.

### sort_order
- **Significato**: specifica l'ordinamento del campo.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: intero che definisce la precedenza di ordinamento.

### fuzzy_name
- **Significato**: un nome alternativo per la corrispondenza approssimativa (fuzzy matching).
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: spesso vuoto o contiene una stringa a fini di corrispondenza.

### fuzzy_field
- **Significato**: specifica se il campo viene utilizzato nella corrispondenza approssimativa.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene una stringa.

### fuzzy_primary_field
- **Significato**: indica se questo è il campo principale per la corrispondenza approssimativa.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### label_align
- **Significato**: impostazione di allineamento dell'etichetta del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: spesso vuoto o contiene informazioni di allineamento (ad es. sinistra, destra, centro).

### calculation_formula
- **Significato**: formula utilizzata per i calcoli che coinvolgono il campo.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: testo contenente una formula o una logica di calcolo.

### clean_field
- **Significato**: indica se il campo deve essere sottoposto a pulizia dei dati.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### alphanumeric_field
- **Significato**: specifica se il campo deve accettare solo caratteri alfanumerici.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### placeholder
- **Significato**: testo segnaposto per il campo di input.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: spesso vuoto o contiene un testo di orientamento.

### coordinates
- **Significato**: dati di coordinate associati al campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene informazioni sulle coordinate.

### normalized_coordinates
- **Significato**: versione normalizzata delle coordinate, per garantire coerenza.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene dati di coordinate normalizzate.

### threshold
- **Significato**: valore soglia relativo alla convalida o all'elaborazione del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene valori soglia.

### reference_point
- **Significato**: punto di riferimento utilizzato nei calcoli o nel posizionamento.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: spesso vuoto o contiene dati del punto di riferimento.

### checkbox_group
- **Significato**: identificatore di raggruppamento per i campi casella di controllo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene identificatori di gruppo.

### list_of_values
- **Significato**: specifica un elenco di valori consentiti per il campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene un elenco di valori.

### enforce_list_of_values
- **Significato**: indica se l'elenco di valori deve essere applicato in modo rigoroso.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### created_by
- **Significato**: identificatore dell'utente che ha creato la voce del campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: intero che fa riferimento all'ID di un utente.

### created_on
- **Significato**: data e ora di creazione del campo.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: data e ora in UTC.

### last_modified_on
- **Significato**: data e ora dell'ultima modifica del campo.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: data e ora in UTC.

### is_deleted
- **Significato**: indica se il campo è stato contrassegnato come eliminato.
- **Ruolo**: campo tecnico.
- **Contenuto tipico**: valore booleano (True o False).

### costing_element
- **Significato**: elemento di costo associato al campo.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene identificatori di elementi di costo.

### erp_field_name
- **Significato**: nome del campo utilizzato nei sistemi ERP.
- **Ruolo**: campo descrittivo.
- **Contenuto tipico**: in genere vuoto o contiene nomi di campo specifici dell'ERP.

Questa documentazione offre una panoramica dettagliata della struttura e dello scopo di ciascuna colonna della tabella `public.field`. Serve da guida per gli sviluppatori per comprendere il modello di dati e la sua applicazione nel sistema.
```
