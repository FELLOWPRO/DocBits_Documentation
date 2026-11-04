# Tipo di documento

<figure><img src="../../../../.gitbook/assets/docbits_document_type_card.png" alt="DocBits Document Tipo Scheda" width="563"><figcaption></figcaption></figure>

## Scopo:

Questa carta di flusso di lavoro è progettata per valutare se un documento corrisponde a un tipo specifico. Controllando se il documento corrisponde al tipo dato, i flussi di lavoro possono continuare o intraprendere azioni alternative basate su questa condizione. Ciò aiuta ad automatizzare i processi in cui il tipo di documento determina i passaggi successivi nel flusso di lavoro.

## Componenti della carta:

1. **Operatore**
   * **Descrizione**: Definisce se il documento deve essere del tipo specificato o meno.
   * **Opzioni**:
     * **È (Is)**: Il documento deve corrispondere al tipo specificato affinché la condizione sia vera.
     * **Non è (Is Not)**: Il documento non deve corrispondere al tipo specificato affinché la condizione sia vera.
2. **Tipo**
   * **Descrizione**: Specifica il tipo di documento con cui confrontare.
   * **Dettaglio**: Include una varietà di tipi di documento come "Fattura", "Ordine di acquisto", ecc., in base ai quali verrà valutata la condizione (è/non è).

## Funzionalità:

* **Valutazione della condizione**: Il sistema valuta se il tipo di documento nel campo specificato corrisponde alla condizione definita dall'operatore. Confronta il valore del campo con il tipo di documento fornito.
* **Esecuzione dell'azione**:
  * **Condizione vera**: Se il tipo di documento corrisponde al tipo specificato (o meno, in base all'operatore), il flusso di lavoro procede con la condizione vera. Ciò può attivare azioni come l'ulteriore elaborazione del documento, l'invio per l'approvazione o l'applicazione di regole specifiche basate sul tipo di documento.
  * **Condizione falsa**: Se il tipo di documento non corrisponde al tipo specificato, il flusso di lavoro procede con la condizione falsa. Ciò può attivare azioni alternative, come l'instradamento del documento a un processo diverso o l'interruzione di ulteriori azioni.

## Installazione e configurazione:

* Gli utenti configurano la carta selezionando il campo del documento che contiene il tipo di documento da un elenco di campi disponibili. Quindi, viene selezionato l'operatore per definire se il documento deve essere del tipo specificato o meno. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina l'azione successiva basata sul tipo di documento.

## Conclusione:

La carta di flusso di lavoro "Confronto tipo di documento" è essenziale per garantire che i flussi di lavoro procedano in base al tipo di documento in fase di elaborazione. Confrontando il tipo di documento, aiuta le organizzazioni ad automatizzare le attività di instradamento ed elaborazione dei documenti, assicurando che i documenti vengano gestiti in modo appropriato in base al loro tipo.
