---
description: "P1: distinguere assegnazione, attività e approvazione sequenziale"
---

# P1: distinguere assegnazione, attività e approvazione sequenziale

Un’**assegnazione documentale** determina la responsabilità attuale. Un’**attività** è un lavoro separato. Una **notifica** informa. Nessuna costituisce già l’approvazione di una persona. Assegnare un gruppo non prova il consenso di tutti i membri.

Le schede sequenziali raccolgono destinatari e ordine di approvazione. L’esempio usa A con ordine 10 e B con 20. La finalizzazione esaminata comincia dal valore minore. Il passaggio a B segue la decisione utente elaborata nel processo di approvazione; un nodo Wait non compie da solo tale passaggio.

Evitare un’assegnazione diretta nella stessa esecuzione se si attende il primo destinatario sequenziale: la finalizzazione può saltare la prima assegnazione quando il documento è già stato assegnato direttamente. Configurare `task_type`, priorità, destinatario e `send_email` separatamente. Tenere disattivata l’e-mail negli esercizi.

Il collaudo aziendale richiede A→approva→B→approva, rifiuto di A, destinatario assente e attivazione ripetuta. Il rifiuto deve impedire l’export finale; un destinatario non risolto non deve sembrare un’approvazione completata. Verificare separatamente responsabilità e attività. La simulazione non dimostra un passaggio reale tra utenti.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `action_assign_doc_to_user_sequential` · v2

Identità: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identità: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Approvare → B → Approvare |
| ASSIGN-02 | A → Rifiutare | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Percorso di ripiego |
| ASSIGN-04 | RUN-1 → RUN-2 | verificare duplicati |
| ASSIGN-05 | direct + sequential | verificare primo destinatario |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
