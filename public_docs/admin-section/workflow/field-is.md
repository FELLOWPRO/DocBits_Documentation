# Il campo è

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta di flusso di lavoro è progettata per automatizzare le azioni in base alla presenza o allo stato di un campo specificato all'interno di un documento. Valutando se il campo è vuoto, mancante o popolato, consente ai flussi di lavoro di gestire i documenti con precisione e accuratezza.

## **Componenti della carta:**

1. **Nome del campo**
   * **Descrizione:** Specifica il nome del campo da valutare.
   * **Dettaglio:** Deve corrispondere esattamente all'identificatore utilizzato nel documento per garantire un rilevamento accurato del campo.
2. **Operatori**
   * **Descrizione**: Definisce la condizione che attiva il flusso di lavoro, in base alla presenza o allo stato del campo.
   * **Opzioni**:
     * **Vuoto/Non nel documento:** Il flusso di lavoro si attiva se il campo è assente dal documento o è presente ma vuoto.
     * **Nel documento/Non vuoto:** Il flusso di lavoro si attiva se il campo esiste nel documento e contiene un valore.

## **Funzionalità:**

* **Rilevamento dello stato:** La carta monitora il campo specificato per valutarne la presenza e lo stato.
* **Valutazione della condizione:**
  * Il sistema valuta se il campo specificato si trova nello stato (Vuoto/Non nel documento o Nel documento/Non vuoto) definito dall'operatore selezionato.
*

    **Esecuzione dell'azione:**

    * **Condizione Vuoto/Non nel documento:** Se lo stato del campo corrisponde a questa condizione (ovvero, il campo è assente dal documento o presente ma vuoto), il sistema avvia le azioni associate. Queste possono includere la generazione di avvisi, la segnalazione del documento per la revisione o l'interruzione del flusso di lavoro.
    * **Condizione Nel documento/Non vuoto:** Se lo stato del campo corrisponde a questa condizione (ovvero, il campo esiste nel documento e contiene un valore), il sistema attiva le azioni associate. Queste potrebbero comportare l'abilitazione di passaggi successivi del flusso di lavoro, l'aggiornamento dei record o l'attivazione di notifiche.

## **Installazione e configurazione:**

* Gli utenti selezionano il campo da un elenco di campi documento disponibili. L'operatore viene scelto tramite un menu a discesa, che offre opzioni chiare per "Vuoto/Non nel documento" o "Nel documento/Non vuoto".

## **Conclusione:**

La carta di flusso di lavoro "Convalida della presenza e dello stato del campo" è uno strumento fondamentale per i flussi di lavoro di elaborazione dei documenti, garantendo una gestione accurata dei campi mancanti o popolati. Automatizzando le azioni basate sugli stati dei campi, questa carta migliora l'integrità dei dati, riduce gli errori e assicura che i flussi di lavoro operino in modo fluido ed efficiente.
