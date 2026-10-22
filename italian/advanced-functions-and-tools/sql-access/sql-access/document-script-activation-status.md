# Stato di attivazione dello script del documento

## Tabella `public.document_script_activation_status`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp con fuso orario
* `last_modified_on`: timestamp con fuso orario
* `is_deleted`: boolean
* `script_id`: interno

### Analisi e descrizione

## Documentazione della tabella: `public.document_script_activation_status`

### Introduzione

La tabella `public.document_script_activation_status` è progettata per gestire lo stato di attivazione degli script associati ai documenti all'interno di un'organizzazione. Ogni voce della tabella corrisponde a uno specifico script e al suo attuale stato di attivazione, consentendo potenzialmente alle organizzazioni di controllare e organizzare l'esecuzione degli script in relazione ai propri documenti.

### Descrizione delle colonne

#### id

* **Significato**: questa colonna memorizza un identificatore univoco per ogni voce della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: identificatore univoco universale (UUID) come `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Nota**: garantisce che ogni record sia identificabile in modo univoco.

#### org\_id

* **Significato**: rappresenta l'identificatore di un'organizzazione.
* **Ruolo**: chiave esterna, probabilmente verso una tabella delle organizzazioni.
* **Contenuto tipico**: UUID che identifica l'organizzazione, ad esempio `23f3d697-7411-4c95-981d-faf089d266be`.
* **Nota**: collega lo stato di attivazione dello script a una specifica organizzazione.

#### sort\_order

* **Significato**: indica l'ordine in cui gli script devono essere eseguiti o visualizzati.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valori interi che rappresentano la sequenza, ad esempio `0`.
* **Nota**: può essere utilizzato per assegnare priorità o organizzare gli script.

#### is\_active

* **Significato**: indica se uno script è attualmente attivo.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valori booleani, `True` o `False`.
* **Nota**: determina se lo script associato deve essere eseguito.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato il record.
* **Ruolo**: chiave esterna, probabilmente verso una tabella utenti.
* **Contenuto tipico**: valore intero che rappresenta un ID utente, ad esempio `1`.
* **Nota**: traccia il creatore del record a fini di audit.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora con fuso orario, ad esempio `2023-11-20 10:44:14.685170+00:00`.
* **Nota**: fornisce un timestamp di creazione per la tenuta dei registri.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica al record.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data e ora con fuso orario, oppure `None` se il record non è mai stato modificato.
* **Nota**: utile per tracciare le modifiche nel tempo.

#### is\_deleted

* **Significato**: indica se il record è contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valori booleani, `True` o `False`.
* **Nota**: consente l'eliminazione logica dei record senza rimozione fisica dal database.

#### script\_id

* **Significato**: identificatore dello script associato al record.
* **Ruolo**: chiave esterna, probabilmente verso una tabella degli script.
* **Contenuto tipico**: UUID che identifica lo script, ad esempio `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Nota**: collega lo stato di attivazione a uno specifico script.
