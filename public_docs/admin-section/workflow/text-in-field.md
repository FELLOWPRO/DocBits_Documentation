# Testo nel campo

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta di flusso di lavoro è progettata per automatizzare le azioni in base alla presenza o all'assenza di un testo specifico all'interno di un campo del documento specificato. Garantisce che i flussi di lavoro possano adattarsi dinamicamente al contenuto dei documenti, supportando un'elaborazione efficiente e un processo decisionale accurato.

## **Componenti della carta:**

1. **Testo**
   * **Descrizione:** Specifica la stringa di testo da controllare all'interno del campo.
   * **Dettaglio:** Può trattarsi di una parola, una frase o una sequenza di caratteri rilevanti per il flusso di lavoro.
2. **Operatore**
   * **Descrizione:** Definisce la condizione per la presenza del testo nel campo.
   * **Opzioni:**
     * **È (Is):** Attiva il flusso di lavoro se il testo specificato è presente nel campo.
     * **Non è (Is Not):** Attiva il flusso di lavoro se il testo specificato non è presente nel campo.
3. **Nome del campo**
   * **Descrizione:** Specifica il nome del campo del documento da valutare.
   * **Dettaglio:** Deve corrispondere esattamente all'identificatore del campo all'interno del documento.

## **Funzionalità:**

1. **Valutazione della condizione:** Il sistema controlla se il testo specificato esiste nel campo, in base all'operatore selezionato (È o Non è).
2. **Esecuzione dell'azione:**
   * **Condizione vera:**
     Se la presenza del testo nel campo corrisponde alla condizione specificata, il sistema avvia le azioni associate. Queste potrebbero includere l'attivazione di avvisi, l'avanzamento dei flussi di lavoro o l'aggiornamento dei record.
   * **Condizione falsa:**
     Se la presenza del testo nel campo non corrisponde alla condizione, possono essere intraprese azioni alternative o nessuna azione, a seconda della configurazione del flusso di lavoro.

## **Installazione e configurazione:**

* L'utente inserisce il testo da controllare. Seleziona quindi il nome del campo del documento pertinente.

## **Conclusione:**

La carta di flusso di lavoro "Presenza di testo nel campo" è uno strumento semplice ma potente per l'analisi del contenuto dei documenti. Automatizzando le azioni basate sul rilevamento del testo, questa carta supporta flussi di lavoro più intelligenti, migliora l'accuratezza della gestione dei documenti e riduce lo sforzo manuale.
