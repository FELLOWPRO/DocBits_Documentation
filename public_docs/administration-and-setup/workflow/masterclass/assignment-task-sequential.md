---
description: "P1: distinguere assegnazione, attività e approvazione sequenziale"
---

# P1: distinguere assegnazione, attività e approvazione sequenziale

Un’**assegnazione documentale** determina la responsabilità attuale. Un’**attività** è un lavoro separato. Una **notifica** informa. Nessuna costituisce già l’approvazione di una persona. Assegnare un gruppo non prova il consenso di tutti i membri.

Le schede sequenziali raccolgono destinatari e ordine di approvazione. L’esempio usa A con ordine 10 e B con 20. La finalizzazione esaminata comincia dal valore minore. Il passaggio a B segue la decisione utente elaborata nel processo di approvazione; un nodo Wait non compie da solo tale passaggio.

Evitare un’assegnazione diretta nella stessa esecuzione se si attende il primo destinatario sequenziale: la finalizzazione può saltare la prima assegnazione quando il documento è già stato assegnato direttamente. Configurare `task_type`, priorità, destinatario e `send_email` separatamente. Tenere disattivata l’e-mail negli esercizi.

Il collaudo aziendale richiede A→approva→B→approva, rifiuto di A, destinatario assente e attivazione ripetuta. Il rifiuto deve impedire l’export finale; un destinatario non risolto non deve sembrare un’approvazione completata. Verificare separatamente responsabilità e attività. La simulazione non dimostra un passaggio reale tra utenti.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4" %}

**Video:** Approvazione in due passi con tabelle decisionali · 3:04 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Due passi, due tabelle decisionali** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=0.25)

Un'approvazione in due passi: prima gli approvatori restituiti da una tabella decisionale, poi un gruppo finale che viene sempre per ultimo. Due tabelle decisionali: una restituisce utenti, l'altra un gruppo.

**Una catena: tabella, assegnazione, tabella, assegnazione** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=14.683)

Metti ogni scheda di assegnazione subito dopo la sua tabella decisionale, in un'unica catena: tabella, assegnazione, tabella, assegnazione. Entrambe le tabelle salvano i risultati.

**Ogni assegnazione subito dopo la sua tabella** · [0:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=28.816)

Un Workflow conserva solo l'ultimo risultato di una tabella decisionale. Ogni scheda di assegnazione lo legge quando parte, quindi deve partire prima che la tabella successiva lo sostituisca.

**Le priorità decidono l'ordine** · [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=41.983)

L'ordine delle approvazioni viene dalle priorità, non dall'ordine delle schede: il numero più basso riceve il documento per primo. Dai al gruppo finale il numero più alto.

**Test: approvatori, poi il gruppo** · [0:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=53.483)

Il test mostra ogni scheda riuscita. La prima scheda di assegnazione mette in coda i due approvatori, la seconda il gruppo finale. Alla fine dell'esecuzione, un'ultima assegnazione dà il documento al primo di loro.

**Affiancati: non funziona** · [1:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=81.55)

Questa disposizione non funziona. Due percorsi affiancati sembrano uguali, ma il Workflow li esegue passo per passo: prima entrambe le tabelle, poi entrambe le schede di assegnazione.

**Approvatori persi - senza errore** · [1:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=96.15)

Il test esegue prima entrambe le tabelle, poi entrambe le schede di assegnazione. Tutte e due leggono il risultato della seconda tabella: il gruppo va in coda due volte e gli approvatori si perdono. Ogni scheda mostra comunque successo, nulla ti avvisa. Usa la catena.

**Un ultimo approvatore fisso: priorità 99** · [2:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=126.283)

In un Workflow Standard un approvatore fisso può venire sempre per ultimo: assegna gli utenti della tabella, poi aggiungi una scheda che assegna un utente con priorità alta, per esempio 99.

**Priorità della tabella più basse** · [2:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=140.483)

Le priorità della tabella devono restare sotto quel numero. Se la tabella non trova nessuno, il Workflow si ferma alla scheda della tabella e nessuno viene assegnato. Un utente restituito da entrambe viene interpellato due volte.

**Verificalo in un test** · [2:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/it.mp4#t=155.483)

Un Workflow Standard testa una scheda alla volta, quindi testa le stesse schede in un Advanced Workflow. La prima scheda mette in coda gli approvatori della tabella, la seconda aggiunge l'utente fisso. Le priorità lo mettono per ultimo.

</details>

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
