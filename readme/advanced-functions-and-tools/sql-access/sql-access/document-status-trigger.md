# Document status trigger

## Tabella `public.document_status_trigger`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `trigger_doc_type`: interno
* `trigger_doc_status`: interno
* `trigger_url`: interno
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.document_status_trigger`

### Introduzione

La tabella `public.document_status_trigger` è progettata per gestire e tracciare lo stato dei documenti all'interno di un'organizzazione. Questa tabella sembra gestire i trigger legati all'elaborazione dei documenti, probabilmente in un sistema di flussi di lavoro. Raccoglie informazioni sui tipi di documento e sui cambi di stato, con la possibilità di avviare azioni o flussi di lavoro tramite URL specificati.

### Descrizione delle colonne

#### id

* **Significato**: questa colonna memorizza un identificatore univoco per ogni record della tabella.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID, ad esempio `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Significato**: rappresenta l'identificatore univoco di un'organizzazione.
* **Ruolo**: chiave esterna, che rimanda a un'entità organizzazione.
* **Contenuto tipico**: una stringa UUID, ad esempio `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Significato**: specifica il tipo di documento associato al trigger.
* **Ruolo**: campo descrittivo che indica il tipo di documento.
* **Contenuto tipico**: nomi di tipi di documento, come `INVOICE`.

#### trigger\_doc\_status

* **Significato**: indica lo stato specifico del documento che attiva il trigger.
* **Ruolo**: campo descrittivo che dettaglia lo stato del documento.
* **Contenuto tipico**: descrizioni di stato, come `approved_pending_second_approval`.

#### trigger\_url

* **Significato**: URL che viene richiamato quando lo stato del documento soddisfa determinate condizioni.
* **Ruolo**: campo tecnico per l'automazione dei flussi di lavoro.
* **Contenuto tipico**: URL, ad esempio `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Significato**: indica se il trigger è attualmente attivo.
* **Ruolo**: campo tecnico per la gestione degli stati del trigger.
* **Contenuto tipico**: valori booleani, `True` o `False`.

#### created\_by

* **Significato**: identifica l'utente che ha creato il record.
* **Ruolo**: chiave esterna verso un'entità utente.
* **Contenuto tipico**: ID utente interi, ad esempio `1`.

#### created\_on

* **Significato**: timestamp di creazione del record.
* **Ruolo**: campo tecnico per l'audit e il tracciamento delle modifiche.
* **Contenuto tipico**: timestamp con fuso orario, ad esempio `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica al record.
* **Ruolo**: campo tecnico per l'audit e il tracciamento delle modifiche.
* **Contenuto tipico**: timestamp con fuso orario, può essere `None` se non modificato.

#### is\_deleted

* **Significato**: indica se il record è considerato eliminato o inattivo.
* **Ruolo**: campo tecnico per l'eliminazione logica.
* **Contenuto tipico**: valori booleani, `True` o `False`.

Questa tabella offre un approccio strutturato alla gestione degli stati dei documenti e dei trigger associati all'interno del sistema di flussi di lavoro di un'organizzazione, garantendo che le azioni possano essere eseguite automaticamente man mano che i documenti avanzano tra i vari stati.
