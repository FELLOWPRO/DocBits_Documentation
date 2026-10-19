# REST API Lookup Configurations

## Tabella `public.rest_api_lookup_configurations`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `sub_org_id`: interno
* `data_key`: interno
* `url`: interno
* `method`: interno
* `params`: text
* `headers`: text
* `body`: text
* `body_type`: interno
* `authentication_type`: interno
* `authentication_json`: text
* `data_base_path`: interno
* `column_paths`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `is_template`: boolean
* `is_dynamic`: boolean

### Analisi e descrizione

## Documentazione tecnica: tabella `public.rest_api_lookup_configurations`

### Introduzione

La tabella `public.rest_api_lookup_configurations` è progettata per memorizzare le configurazioni delle ricerche (lookup) tramite API REST all'interno di un'organizzazione. Questa tabella contiene le informazioni essenziali per eseguire le richieste API, inclusi i dettagli sugli endpoint, sui metodi di autenticazione e sulle configurazioni di richiesta/risposta. Sembra essere utilizzata per costruire dinamicamente le chiamate API e analizzarne i risultati.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni voce di configurazione.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: stringhe UUID come `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Nota**: è la chiave univoca per identificare una specifica configurazione di lookup API.

#### org\_id

* **Significato**: identificatore dell'organizzazione proprietaria della configurazione.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: stringhe UUID che rappresentano gli ID delle organizzazioni.
* **Nota**: collega la configurazione a un'organizzazione.

#### sub\_org\_id

* **Significato**: identificatore di una sottorganizzazione all'interno dell'organizzazione principale.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: stringhe UUID che rappresentano gli ID delle sottorganizzazioni.
* **Nota**: consente una granularità ulteriore all'interno delle organizzazioni.

#### data\_key

* **Significato**: un'etichetta o una chiave per identificare i dati o l'endpoint API.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: testo descrittivo come `bank_codes`.
* **Nota**: utilizzata per distinguere tra diversi tipi di dati o endpoint.

#### url

* **Significato**: l'URL dell'endpoint API da chiamare.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: stringhe URL come `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Nota**: rappresenta l'endpoint a cui viene inviata la richiesta HTTP.

#### method

* **Significato**: metodo HTTP utilizzato per la richiesta API.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: metodi HTTP comuni come `GET`.
* **Nota**: stabilisce il tipo di richiesta HTTP da eseguire.

#### params

* **Significato**: parametri da includere nella richiesta API.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: JSON o coppie chiave-valore (spesso `None` se non utilizzati).
* **Nota**: contiene i parametri dinamici della richiesta.

#### headers

* **Significato**: intestazioni HTTP da includere nella richiesta.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: dati JSON o di testo (spesso `None` se non utilizzati).
* **Nota**: utilizzate per includere metadati aggiuntivi nella richiesta.

#### body

* **Significato**: il corpo della richiesta HTTP.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: dati JSON o altri dati serializzati (spesso `None` se non utilizzati).
* **Nota**: contiene il payload per le richieste POST/PUT.

#### body\_type

* **Significato**: specifica il formato del corpo della richiesta.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: tipi MIME come `application/json`.
* **Nota**: indica il tipo di contenuto del corpo.

#### authentication\_type

* **Significato**: tipo di autenticazione utilizzato per la richiesta API.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: metodi di autenticazione come `ionapi`.
* **Nota**: determina il modo in cui la richiesta verrà autenticata.

#### authentication\_json

* **Significato**: dettagli della configurazione di autenticazione in formato JSON.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: stringhe JSON con le informazioni di autenticazione.
* **Nota**: contiene le credenziali e i dettagli degli endpoint per l'autenticazione.

#### data\_base\_path

* **Significato**: percorso all'interno della risposta API da cui estrarre i dati.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: espressioni di percorso JSON come `$[results][0][records]`.
* **Nota**: utilizzato per analizzare i dati della risposta API.

#### column\_paths

* **Significato**: associa i campi di dati alle colonne per l'estrazione.
* **Ruolo**: campo di configurazione.
* **Contenuto tipico**: stringhe JSON che associano i campi della risposta API ai nomi delle colonne.
* **Nota**: facilita l'estrazione dei dati dalla risposta API.

#### created\_by

* **Significato**: identificatore dell'utente che ha creato la configurazione.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: ID interi come `1`.
* **Nota**: tiene traccia dell'autore della voce di configurazione.

#### created\_on

* **Significato**: timestamp di creazione della configurazione.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: timestamp come `2024-01-24T09:14:24.788788Z`.
* **Nota**: indica la data e l'ora di creazione.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: timestamp (spesso `None` se non modificata).
* **Nota**: registra l'ora dell'ultimo aggiornamento.

#### is\_deleted

* **Significato**: flag che indica se una configurazione è contrassegnata come eliminata.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: valori booleani come `False`.
* **Nota**: utilizzato per l'eliminazione logica (soft delete) delle configurazioni.

#### deleted\_on

* **Significato**: timestamp del momento in cui la configurazione è stata contrassegnata come eliminata.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: timestamp (spesso un segnaposto se non eliminata).
* **Nota**: registra quando la configurazione è stata contrassegnata come eliminata.

#### is\_template

* **Significato**: indica se la configurazione funge da modello.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: valori booleani come `True`.
* **Nota**: identifica i modelli da riutilizzare.

#### is\_dynamic

* **Significato**: specifica se la configurazione è dinamica.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: valori booleani come `False`.
* **Nota**: determina se la configurazione si adatta ai dati che cambiano.
