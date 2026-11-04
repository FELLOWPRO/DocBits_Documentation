---
description: "P1: seguire la tabella decisionale fino all’assegnazione"
---

# P1: seguire la tabella decisionale fino all’assegnazione

Una tabella decisionale collega campi di ingresso a risultati tipizzati. L’esempio usa `cost_center=4711` e `total_amount`: revisore A fino a 1000, B oltre 1000. Creare due regole senza sovrapposizioni e usare utenti validi dell’organizzazione di test. Il file del kit descrive la configurazione; non garantisce l’importazione nell’editor.

In **Decision Table has Returns** v3, attivare `store_data=wf_store_data`. La v2 legge invece l’opzione booleana di memorizzazione. L’assegnazione successiva richiede risultati salvati nella stessa esecuzione. Una tabella eseguita correttamente non conferma ancora un utente valido.

Un risultato utente può contenere `output_type=user` e `value=101`; 101 è sintetico e va sostituito con un utente di test esistente. Scegliere poi **Assign document based on decision table** con `assignee_type=user`. La versione 2 esaminata di questa azione sceglie l’ultimo risultato corrispondente. Più risultati non richiedono automaticamente l’approvazione di tutti gli utenti.

Provare uno, nessuno e più risultati, tipo errato, utente non valido e memorizzazione disattivata. Collegare nessun risultato ed errore di assegnazione a un ripiego esplicito. Definire ordine e politica di corrispondenza, senza trasformare un ordine casuale in regola aziendale. Collaudare l’assegnazione effettiva sul documento.

La condizione di tabella decisionale chiama realmente il servizio per valutarla. Il test non garantisce l’assenza di ogni effetto: usare solo dati propri di test e controllare le azioni coinvolte.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `condition_decision_tree_data` · v3

Identità: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identità: `699912a7-2369-47e0-9092-8d027e13752a`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | nessun risultato / utente non valido / tipo errato | Percorso di ripiego |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | nessun risultato salvato per assegnazione |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
