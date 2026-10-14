# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni in base alla presenza o all'assenza di un testo specifico all'interno di un campo del documento specificato. Garantisce che i workflow possano adattarsi dinamicamente al contenuto dei documenti, supportando un'elaborazione efficiente e un processo decisionale accurato.

## **Componenti della scheda:**

1. **Text**
   * **Descrizione:** Specifica la stringa di testo da verificare all'interno del campo.
   * **Dettaglio:** Può essere una parola, una frase o una sequenza di caratteri pertinente al workflow.
2. **Operator**
   * **Descrizione:** Definisce la condizione per la presenza del testo nel campo.
   * **Opzioni:**
     * **Is:** Attiva il workflow se il testo specificato è presente nel campo.
     * **Is Not:** Attiva il workflow se il testo specificato non è presente nel campo.
3. **Field Name**
   * **Descrizione:** Specifica il nome del campo del documento da valutare.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del campo all'interno del documento.

## **Funzionalità:**

1. **Valutazione della condizione:** Il sistema verifica se il testo specificato esiste nel campo, in base all'operatore selezionato (Is o Is Not).
2. **Esecuzione dell'azione:**
   * **Condizione vera:**\
     Se la presenza del testo nel campo corrisponde alla condizione specificata, il sistema avvia le azioni associate. Queste potrebbero includere l'attivazione di avvisi, l'avanzamento dei workflow o l'aggiornamento di record.
   * **Condizione falsa:**\
     Se la presenza del testo nel campo non corrisponde alla condizione, possono essere intraprese azioni alternative o nessuna azione, a seconda della configurazione del workflow.

## **Configurazione e impostazione:**&#x20;

* L'utente inserisce il testo da verificare. Seleziona quindi il nome del campo del documento pertinente.

## **Conclusione:**

La scheda di workflow "Text Presence in Field" è uno strumento semplice ma potente per l'analisi del contenuto dei documenti. Automatizzando le azioni in base al rilevamento del testo, questa scheda supporta workflow più intelligenti, migliora l'accuratezza nella gestione dei documenti e riduce lo sforzo manuale.
