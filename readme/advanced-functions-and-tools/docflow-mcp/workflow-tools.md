# Strumenti per i Workflow

DocFlow MCP espone strumenti per la gestione e il test dei workflow avanzati, oltre a strumenti per leggere i log dei workflow e gestire le variabili dei workflow.

{% hint style="info" %}
**Nomi degli strumenti tramite il gateway DocBits MCP.** Quando ti connetti tramite il DocBits MCP unificato (`api.docbits.com/v3/mcp`), ogni strumento DocFlow porta il prefisso `docflow_`: `list_workflows` si chiama `docflow_list_workflows`, `run_workflow_with_assertions` diventa `docflow_run_workflow_with_assertions`. I parametri sono identici. I nomi riportati qui sotto sono i nomi DocFlow senza prefisso.

I workflow vengono **creati e modificati nel designer DocFlow** nell'app web. L'MCP li legge, li testa, li esegue e li elimina; non crea né modifica i grafi dei workflow.
{% endhint %}

Gli strumenti Card SDK hanno una pagina dedicata, vedi [Strumenti Card SDK](card-sdk-tools.md).

## list\_workflows

Elenca tutti i workflow dell'organizzazione corrente.

**Parametri:** Nessuno

## get\_workflow

Ottieni i dettagli di un workflow specifico, inclusa la struttura di nodi e archi.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sì | UUID del workflow |

## delete\_workflow

Elimina un flusso di lavoro tramite ID (eliminazione logica).

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sì | UUID del workflow da eliminare |

## test\_advanced\_workflow

Testa l'esecuzione di un workflow avanzato. Fornisci opzionalmente un ID documento per testare con un documento reale.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sì | UUID del workflow avanzato |
| `doc_id` | string | No | UUID di un documento per il test |

## list\_test\_scenarios

Elenca tutti gli scenari di test dei workflow per l'organizzazione.

**Parametri:** Nessuno

## list\_cards

Elenca tutte le card disponibili per i workflow con le relative condizioni e configurazione.

**Parametri:** Nessuno

{% hint style="info" %}
Le card hanno flag di ruolo: `when_condition` (trigger), `and_condition` (condizione aggiuntiva) e `then_condition` (azione). Usa questi flag per determinare in quali tipi di nodo una card può essere utilizzata.
{% endhint %}

## list\_workflow\_variables

Elenca tutte le variabili dei workflow dell'organizzazione con nome, tipo e valore corrente.

**Parametri:** Nessuno

## set\_workflow\_variable

Crea una variabile di workflow o ne aggiorna il valore. Le variabili di tipo documento non hanno un valore proprio; vengono impostate dal workflow in fase di esecuzione.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `name` | string | Sì | Nome della variabile |
| `value` | string | No | Nuovo valore |
| `var_type` | string | No | Tipo della variabile al momento della creazione (ad esempio `string`, `number`, `document`) |

## search\_workflow\_logs

Cerca nei log di esecuzione dei workflow per scoprire perché le esecuzioni sono fallite, sono riuscite o hanno incontrato una condizione non soddisfatta.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | No | Limita a un solo workflow |
| `doc_id` | string | No | Limita alle esecuzioni per un solo documento |
| `status` | string | No | Stato dell'esecuzione da filtrare |
| `keyword` | string | No | Filtro a testo libero sul log |
| `include_workflow_data` | boolean | No | Include lo snapshot della definizione del workflow per ogni esecuzione |
| `limit` / `offset` | integer | No | Paginazione |

## get\_workflow\_log\_detail

Dettaglio completo di una singola esecuzione: i log grezzi di esecuzione delle card e la definizione del workflow così com'era al momento dell'esecuzione.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `log_id` | string | Sì | ID della voce di log da `search_workflow_logs` |

## run\_workflow\_with\_assertions

Inizializza le variabili del workflow, esegue un workflow avanzato con l'esecutore reale e verifica il risultato rispetto al database. Le variabili sono scritture reali, non mock: usalo per fare il test di integrazione di un workflow da un assistente.

**Parametri:**

| Parametro | Tipo | Obbligatorio | Descrizione |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sì | UUID del workflow da eseguire |
| `doc_id` | string | No | Documento su cui eseguire il workflow |
| `seed_variables` | array | No | Variabili da creare o aggiornare prima dell'esecuzione; le variabili di tipo documento possono puntare a un `doc_id` tramite `value` |
