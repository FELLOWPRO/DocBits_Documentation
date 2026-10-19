# Custom classification document

## Tabella `public.custom_classification_document`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.custom_classification_document`

### Introduzione

La tabella `public.custom_classification_document` è progettata per memorizzare informazioni dettagliate sulle classificazioni dei documenti all'interno di un'organizzazione. Comprende i metadati del documento, come il contenuto, i dettagli di creazione e il contesto organizzativo. La struttura della tabella suggerisce un utilizzo per la gestione di documenti legati ai processi organizzativi, possibilmente fatture o moduli d'ordine, come si deduce dai dati di esempio.

### Descrizione delle colonne

#### id

* **Significato**: questa colonna memorizza probabilmente un identificatore univoco per ogni voce di documento.
* **Ruolo**: chiave primaria
* **Contenuto tipico**: un UUID che rappresenta un identificatore univoco del documento.

#### org\_id

* **Significato**: questa colonna memorizza l'identificatore dell'organizzazione associata al documento.
* **Ruolo**: chiave esterna
* **Contenuto tipico**: un UUID che collega il documento a una specifica organizzazione.

#### first\_page\_content

* **Significato**: questa colonna contiene il contenuto testuale della prima pagina del documento.
* **Ruolo**: campo dati
* **Contenuto tipico**: rappresentazione testuale del documento di un'organizzazione, che può includere intestazioni, indirizzi e i dettagli iniziali di una fattura o di un ordine.

#### content

* **Significato**: questa colonna memorizza il contenuto testuale completo del documento.
* **Ruolo**: campo dati
* **Contenuto tipico**: contenuto testuale integrale del documento, inclusi tutti i dettagli presenti nella prima pagina e nelle pagine successive.

#### created\_by

* **Significato**: questa colonna indica l'utente che ha creato la voce di documento.
* **Ruolo**: campo dati
* **Contenuto tipico**: un numero intero che rappresenta l'ID utente del creatore.

#### created\_on

* **Significato**: questa colonna registra la data e l'ora di creazione della voce di documento.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, che indica la data e l'ora di creazione.

#### last\_modified\_on

* **Significato**: questa colonna memorizza la data e l'ora dell'ultima modifica della voce di documento.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un timestamp con informazioni sul fuso orario, che indica la data e l'ora dell'ultima modifica. A volte è `None` se dopo la creazione non sono state effettuate modifiche.

#### is\_deleted

* **Significato**: questa colonna indica se la voce di documento è stata contrassegnata come eliminata.
* **Ruolo**: campo tecnico
* **Contenuto tipico**: un valore booleano (`True` o `False`) che mostra lo stato di eliminazione della voce di documento.

Questa tabella offre una struttura solida per la gestione dei dati dei documenti: garantisce che ogni documento possa essere identificato in modo univoco, associato a un'organizzazione e tracciato lungo il ciclo di creazione e modifica.
