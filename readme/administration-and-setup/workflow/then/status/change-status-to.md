# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Change Status"** viene utilizzata per cambiare lo stato di un documento in uno degli stati predefiniti — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — e, facoltativamente, attivare i workflow associati in base al cambiamento di stato. Questa scheda automatizza il processo di aggiornamento degli stati e di attivazione dei workflow, garantendo una gestione documentale efficiente e una corretta gestione degli errori.

## **Componenti della scheda:**

1. **Status**
   * **Descrizione**: Specifica il nuovo stato da applicare al documento.
   * **Opzioni**:
     * **Error**: Contrassegna il documento come affetto da un errore.
     * **Rejected**: Indica che il documento è stato rifiutato e non proseguirà ulteriormente.
     * **Ready for Validation**: Imposta il documento per essere revisionato e validato dall'utente o dal processo di sistema successivo.
     * **Pending Approval**: Mette il documento in uno stato di attesa per l'approvazione.
     * **Pending Second Approval**: Mette il documento in attesa di un secondo livello di approvazione, se applicabile.
2. **Trigger Workflows**
   * **Descrizione**: Determina se eventuali workflow successivi debbano essere attivati dopo il cambiamento di stato.
   * **Opzioni**:
     * **True**: Avvia eventuali workflow pertinenti in base al cambiamento di stato.
     * **False**: Impedisce l'esecuzione dei workflow dopo il cambiamento di stato.

## **Funzionalità:**

* **Valutazione della condizione**: Il sistema valuta le condizioni impostate nelle sezioni **"Where"** e **"And"**. Se queste condizioni sono vere, la scheda procede a cambiare lo stato del documento al valore selezionato.
* **Aggiornamento dello stato**: Una volta soddisfatte le condizioni, lo stato del documento viene aggiornato a una delle opzioni predefinite (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), a seconda della selezione dell'utente.
* **Attivazione dell'azione di workflow**: Se **Trigger Workflows** è impostato su **True**, il sistema avvia automaticamente eventuali workflow associati dopo l'aggiornamento dello stato. Se impostato su **False**, non vengono attivati workflow aggiuntivi e il processo termina con il cambiamento di stato.

## **Configurazione e impostazione:**

Per configurare questa scheda, gli utenti devono:

1. Specificare lo **Status** desiderato su cui verrà impostato il documento al momento della valutazione della condizione (Error, Rejected, Ready for Validation, Pending Approval o Pending Second Approval).
2. Scegliere se **Trigger Workflows** dopo il cambiamento di stato selezionando **True** o **False**.
3. La scheda esegue la sua azione solo se entrambe le condizioni nelle sezioni **"Where"** e **"And"** risultano vere.

## **Conclusione:**

La scheda di workflow **"Change Status"** offre un approccio semplificato per gestire gli stati dei documenti e attivare i workflow correlati. Garantisce che i documenti vengano automaticamente instradati allo stato corretto e che vengano intraprese le azioni necessarie, a seconda del cambiamento di stato. Impostando condizioni chiare per l'esecuzione, riduce lo sforzo manuale e migliora l'efficienza del workflow.
