# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

La scheda di workflow **"Reject the Document"** viene utilizzata per contrassegnare un documento come rifiutato all'interno di un workflow. Questa azione arresta l'avanzamento del documento e ne impedisce il passaggio alla fase successiva del workflow. Garantisce che i documenti che non soddisfano le condizioni o i criteri necessari vengano segnalati e bloccati da ulteriori elaborazioni.

## **Componenti della scheda:**

1. **Rejection Status**
   * **Descrizione**: Questo componente contrassegna il documento come rifiutato, segnalando che non ha soddisfatto le condizioni richieste per l'approvazione.
   * **Dettaglio**: Quando viene attivata, questa scheda aggiorna lo stato del documento a "rifiutato". Questa decisione viene presa in base alle condizioni impostate nelle sezioni **"Where"** e **"And"**.

## **Funzionalità:**

* **Valutazione della condizione**: Il sistema valuta le condizioni impostate nelle sezioni **"Where"** e **"And"**.
  * Se **entrambe le condizioni sono vere**, il documento verrà rifiutato.
  * Se **una delle condizioni è falsa**, la scheda non verrà eseguita e lo stato del documento rimarrà invariato.
* **Esecuzione dell'azione**: Quando le condizioni sono soddisfatte, il documento viene contrassegnato come rifiutato. Questa azione garantisce che solo i documenti che soddisfano criteri specifici proseguano, mentre gli altri vengono segnalati e bloccati per la revisione o la correzione.

## **Conclusione:**

La scheda di workflow **"Reject the Document"** è uno strumento essenziale per controllare il flusso dei documenti nei processi automatizzati. Consentendo il rifiuto dei documenti non conformi, garantisce che solo i documenti validi e accurati proseguano attraverso il workflow, migliorando l'efficienza e l'accuratezza nella gestione documentale.
