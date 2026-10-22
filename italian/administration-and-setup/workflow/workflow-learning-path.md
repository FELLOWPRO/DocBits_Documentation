---
description: "Percorso dal principiante all’esperto"
---

# Percorso dal principiante all’esperto

Seguire i livelli nell’ordine. Leggere non basta: ogni livello termina con una configurazione propria, un’aspettativa verificabile e una prova. P0 evita errori fondamentali di esecuzione; P1 approfondisce dati, decisioni aziendali e integrazioni.

1. [Orientamento e modello di esecuzione](#level-1)
2. [Prima regola propria](#level-2)
3. [Campi, tipi e limiti](#level-3)
4. [Regole aziendali e approvazioni](#level-4)
5. [Controllo Advanced e sotto-workflow](#level-5)
6. [Calcolo, integrazione ed export](#level-6)
7. [Modifiche e gestione esperta](#level-7)

## Prerequisiti

Usare un’organizzazione di test propria e un documento sintetico. Verificare organizzazione, ruolo, licenza workflow e abilitazione Advanced. Lasciare inattivi gli esercizi importati. I JSON completi sono per Advanced Test → Custom Data. Approvazioni e integrazioni reali richiedono utenti e destinatari di test dedicati.

## 1. Orientamento e modello di esecuzione <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/it.mp4" %}

[Apri il video con sottotitoli in italiano e trascrizione](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/it.html).

**Esercizio:** Spiegare organizzazione, accesso, When–And–Then e differenza tra regola lineare e grafo Advanced. Distinguere filtro documentale, evento, salvataggio e attivazione.

**Criterio di completamento:** Si sa spiegare quando la regola viene considerata e quale prova distingue simulazione ed esecuzione documentale.

Leggere e costruire: [Quando viene eseguito il mio workflow?](workflow-execution-model.md) · [P0: cambiare stato e limitare le nuove esecuzioni](masterclass/status-and-reentry.md).

## 2. Prima regola propria <a id="level-2"></a>

**Esercizio:** Creare When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Lasciarla inattiva. Provare dati completi per 999, 1000 e 1000.01. Non serve ancora un nodo di controllo.

**Criterio di completamento:** REVIEW si raggiunge solo oltre 1000. Registrare tipo, operatore e uscita scelta. Gestire separatamente l’input assente.

Leggere e costruire: [Caso Advanced: instradamento delle fatture](advanced-workflow-case-study.md) · [Pacchetto di formazione sui workflow](workflow-training-kit.md).

## 3. Campi, tipi e limiti <a id="level-3"></a>

**Esercizio:** Provare assente, null, testo vuoto, spazi, false, 0 e numeri testuali. Calcolare tolleranze con riferimento ordine e documento. Confrontare una e tutte le righe effettivamente abbinate.

**Criterio di completamento:** Spiegare vero, falso ed errore da valore, tipo, riferimento e dati. Nessuna riga confrontabile non equivale ad approvazione riuscita.

Leggere e costruire: [P1: scegliere Field is, Docfield is o Compare two Fields](masterclass/field-conditions.md) · [P1: definire riferimento delle tolleranze e confronto PO](masterclass/tolerances-and-po.md).

## 4. Regole aziendali e approvazioni <a id="level-4"></a>

**Esercizio:** Configurare due regole di importo senza sovrapposizione. Seguire il risultato utente salvato fino all’assegnazione. Pianificare A con ordine 10 e B con 20, rifiuto e ripiego.

**Criterio di completamento:** Distinguere responsabilità, attività, notifica e approvazione reale. Il passaggio a B richiede una decisione di A elaborata.

Leggere e costruire: [P1: seguire la tabella decisionale fino all’assegnazione](masterclass/decision-table-routing.md) · [P1: distinguere assegnazione, attività e approvazione sequenziale](masterclass/assignment-task-sequential.md).

## 5. Controllo Advanced e sotto-workflow <a id="level-5"></a>

**Esercizio:** Confrontare ALL, ANY e OR con due controlli raggiunti. Esaminare un ramo non scelto. Eseguire i sette casi v2 e provare Run Workflow con un proprio destinatario inattivo.

**Criterio di completamento:** Spiegare differenza test/scheduler, conteggio sorgenti ed errori. V2 termina senza OR bloccato; controllare la destinazione di una chiamata verde.

Leggere e costruire: [P0: collegare correttamente Wait ALL, Wait ANY e OR](masterclass/control-nodes.md) · [P0: comprendere Run Workflow, condizioni ed errori](masterclass/run-workflow.md) · [Caso Advanced: instradamento delle fatture](advanced-workflow-case-study.md).

## 6. Calcolo, integrazione ed export <a id="level-6"></a>

**Esercizio:** Confrontare tutta la tabella prima/dopo, inclusi regex senza corrispondenza e divisione per zero. Definire il contratto reale di scrittura dei risultati. Pianificare export dopo approvazione con una propria configurazione di test.

**Criterio di completamento:** Provare separatamente valori successivi, ricezione ed elaborazione ERP. Non registrare simulazione o richiesta di export come consegna.

Leggere e costruire: [P1: calcolare colonne e verificare dipendenze regex](masterclass/table-calculations.md) · [P1: verificare chiamate API e uso successivo delle risposte](masterclass/api-response-contract.md) · [P1: scegliere export, attività aperte e stato finale](masterclass/export-lifecycle.md).

## 7. Modifiche e gestione esperta <a id="level-7"></a>

**Esercizio:** Salvare l’export del workflow e le versioni prima di modificarlo. Ripetere casi positivi, negativi, errori, limiti e una seconda esecuzione. Collegare il primo errore a input e configurazione precisi.

**Criterio di completamento:** Si sa accettare una modifica, ripristinare la configurazione e confrontare un nuovo documento con i suoi effetti. Registrare causa, correzione e limiti.

Leggere e costruire: [Diagnosticare sistematicamente i problemi di workflow](workflow-troubleshooting.md) · [Comprendere e configurare le schede workflow](card-reference-standard.md).

## Verificare le conoscenze

| Domanda | Risposta |
| --- | --- |
| false è vuoto per Field is v2? | Sì; il numero 0 e il testo "false" non lo sono. |
| Un test OR verde garantisce l’esecuzione documentale? | No. I predecessori non raggiunti sono trattati diversamente nel test e nello scheduler esaminato. |
| Run Workflow può chiamare una destinazione inattiva? | Sì, nella chiamata esplicita esaminata. Verificare comunque condizioni e risultato. |
| HTTP 200 espone automaticamente api.response.cost_center? | No. Le azioni esaminate non offrono tale contratto automatico di uscita JSON. |
| Un test verde prova la ricezione dell’export? | No. Esecuzione documentale, ricezione ed elaborazione ERP richiedono prove distinte. |

## Le cinque guide di accompagnamento

Usare durante gli esercizi: modello di esecuzione → caso riproducibile → kit → diagnosi → riferimento delle schede. Sono materiali dei livelli, non cinque ulteriori attività non verificate.

1. [Quando viene eseguito il mio workflow?](workflow-execution-model.md)
2. [Caso Advanced: instradamento delle fatture](advanced-workflow-case-study.md)
3. [Pacchetto di formazione sui workflow](workflow-training-kit.md)
4. [Diagnosticare sistematicamente i problemi di workflow](workflow-troubleshooting.md)
5. [Comprendere e configurare le schede workflow](card-reference-standard.md)

## Verbale di completamento

Usare acceptance-record-template.json del kit. Registrare scenario, revisione, aspettativa, osservazione e tipo di prova. Distinguere test Dev, verifica isolata del codice, esecuzione documentale reale, ricezione ed elaborazione ERP. Lasciare esplicitamente aperti i passi non verificati.
