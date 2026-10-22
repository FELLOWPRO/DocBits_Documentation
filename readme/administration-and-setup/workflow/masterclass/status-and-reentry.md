---
description: "P0: cambiare stato e limitare le nuove esecuzioni"
---

# P0: cambiare stato e limitare le nuove esecuzioni

**Change Status to** aggiorna lo stato del documento. Nella versione 3, `trigger_docflow` controlla la richiesta di ulteriore elaborazione dei workflow. Impostarlo esplicitamente. Se manca, il codice usa `true`; le versioni 1/2 non leggono il parametro nello stesso percorso di esecuzione. Controllare la versione salvata.

Iniziare con `validated_pending_approval` e `trigger_docflow=false`. Lo stato è un’opzione tecnica: un `pending_approval` inventato non è equivalente. Advanced Test simula l’aggiornamento. Non dimostra né la persistenza dello stato né l’elaborazione di un’esecuzione successiva richiesta.

Un processo delimitato controlla stato iniziale e indicatore di elaborazione, esegue l’azione e passa allo stato seguente. Un evento ripetuto non deve più soddisfare la condizione iniziale. Due esecuzioni concorrenti possono però leggere lo stesso vecchio indicatore: attività e destinazioni di esportazione richiedono ulteriori controlli dei duplicati.

Per il collaudo, confrontare prima e seconda esecuzione reale: stato, elaborazione successiva richiesta e numero di attività o registrazioni di destinazione. Non alternare due stati solo per sperimentare. Cambiare stato non concede un’approvazione la cui condizione aziendale resta insoddisfatta.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `staus_change` · v3

Identità: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | esecuzione successiva richiesta ≠ completata |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Prove e limiti

Risultati selezionati di schede e nodi sono stati verificati con dati sintetici in Advanced Test. Le risposte sono nel kit. Le azioni documentali sono simulate e non provano esecuzione persistente o consegna esterna.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
