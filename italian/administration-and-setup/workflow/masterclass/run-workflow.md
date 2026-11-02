---
description: "P0: comprendere Run Workflow, condizioni ed errori"
---

# P0: comprendere Run Workflow, condizioni ed errori

**Run Workflow** chiama un workflow per ID e ne attende l’esecuzione. Il nome non basta. Il designer gestisce l’ID nascosto del workflow chiamante; non modificarlo come parametro aziendale. Il documento corrente viene passato alla destinazione, dove ingresso e condizioni sono rivalutati.

La chiamata esplicita esaminata raggiunge anche una destinazione **inattiva**. Inattiva non significa irraggiungibile tramite Run Workflow. I test Dev comprendono una destinazione didattica inattiva, un’autorichiamata e un ID sconosciuto. Gli ultimi due casi seguono Error. I limiti integrati di ricorsione e catena non sostituiscono regole contro chiamate ripetute.

Distinguere variabili di organizzazione e campi documentali dai risultati locali di un’esecuzione. La chiamata non inoltra automaticamente tutti i risultati di tabelle decisionali o HTTP del chiamante. Concordare i campi necessari e verificarne i valori effettivi nella scheda seguente.

Una chiamata verde non conferma tutte le condizioni aziendali della destinazione: un risultato Advanced senza errore tecnico è considerato una chiamata riuscita e può comprendere `failed_condition`. Esaminare percorso scelto ed effetto. Gestire esplicitamente gli errori nel chiamante; evitare A→B→A e chiamate ripetute alla stessa destinazione.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `run_workflow` · v2

Identità: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | chiamata eventualmente riuscita; verificare destinazione |

## Prove e limiti

Risultati selezionati di schede e nodi sono stati verificati con dati sintetici in Advanced Test. Le risposte sono nel kit. Le azioni documentali sono simulate e non provano esecuzione persistente o consegna esterna.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
