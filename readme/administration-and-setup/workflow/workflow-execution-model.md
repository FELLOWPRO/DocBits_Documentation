---
description: "Distinguere eventi, condizioni, ordine di esecuzione, test e attivazione dei workflow."
---

# Quando viene eseguito il mio workflow?

Un workflow richiede un motivo di esecuzione e condizioni corrispondenti. **Il tipo di documento è Fattura** seleziona i documenti; non significa che ogni modifica a una fattura avvii automaticamente una nuova esecuzione.

## Dall’evento all’azione

1. Controllare organizzazione, autorizzazioni e modulo Workflow, oltre all’abilitazione Advanced quando necessaria.
2. Individuare il motivo: elaborazione del documento, chiamata manuale esplicita o trigger di evento supportato. Usare solo i trigger realmente disponibili nel catalogo della propria versione.
3. In Standard Workflow devono risultare vere When e tutte le condizioni And. Una condizione falsa interrompe quella sequenza lineare.
4. In Advanced Workflow, ingresso e uscite dei risultati collegate determinano il percorso. Una condizione And falsa può proseguire tramite arancione; rosso gestisce un errore di valutazione.
5. Verificare il risultato nel punto appropriato: risposta del test, esecuzione persistita, documento o sistema destinatario.

**Start** è un ingresso manuale. Il pacchetto utilizza When per Fattura e il numero esatto di formazione per soddisfare i requisiti dell’interfaccia corrente. Importarlo disattivato ed eseguire test manuali. Un test manuale riuscito non dimostra l’attivazione automatica tramite eventi documentali.

## Salvare, provare e attivare

| Stato | Significato |
| --- | --- |
| Bozza locale | La copia nel browser non sostituisce il salvataggio sul server. |
| Salvato | La configurazione esiste. Controllare separatamente l’attivazione: salvare una nuova regola può già attivarla. |
| Test Advanced | Valuta il grafico corrente, comprese modifiche non salvate. Le azioni documentali vengono simulate. |
| Attivato | La regola può essere considerata per il relativo evento. Provare tale evento separatamente. |

Test Manager e la finestra di test Advanced sono superfici di esecuzione diverse. Il solo confronto dello stato non conferma assegnazione, notifica o consegna di un’esportazione. Verificare gli effetti della modalità scelta prima di usare documenti reali.

## Più workflow ed esecuzioni ripetute

I valori inferiori dell’**ordine di esecuzione** vengono elaborati prima. Per esempio, il workflow 100 prepara un campo e il 200 lo controlla. Usare valori distinti e confermare i dati effettivamente letti in una nuova esecuzione. La posizione di una scheda Advanced sul canvas non determina l’ordine.

**Change Status to → Trigger Workflows** può avviare un’altra esecuzione. **Run Workflow** richiama un workflow selezionato. Entrambi richiedono condizioni deliberate; nessuno garantisce una sola esecuzione. Limitare attività ed esportazioni mediante lo stato del processo e provare esplicitamente un secondo passaggio. Una semplice marca di completamento non protegge in generale dai duplicati simultanei.

Proseguire con il [caso Advanced](advanced-workflow-case-study.md), il [pacchetto di formazione](workflow-training-kit.md) e la [diagnosi](workflow-troubleshooting.md).

## WF-01: Esercizio e collaudo

Registrare evento, filtro, attivazione e versione. Verificare due esecuzioni e ordine 100/200 con un campo successivo realmente letto. Distinguere richiesta attesa ed esecuzione osservata.

[Percorso](workflow-learning-path.md)
