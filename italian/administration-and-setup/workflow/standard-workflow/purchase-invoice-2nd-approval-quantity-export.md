# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Acquisto Ordine Esporta 6"><figcaption></figcaption></figure>

Questo titolo indica che la regola è configurata per gestire la seconda fase di approvazione delle fatture d'acquisto con particolare attenzione ai dettagli sulle quantità, garantendo che le quantità sulla fattura corrispondano a quelle sull'ordine di acquisto originale.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione garantisce che la regola venga attivata solo per i documenti identificati come fatture, aspetto fondamentale per instradare correttamente il workflow.
2. **And…**
   * **Document Status is Pending Second Approval**: questo specifica che la fattura è attualmente in attesa di una seconda approvazione. Questa fase fornisce spesso una supervisione aggiuntiva per garantire l'accuratezza prima che la transazione sia finalizzata.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: questa condizione specifica ulteriormente che la regola si applica solo alle fatture classificate specificamente come "Purchase Invoices", differenziandole dagli altri tipi di fattura.
   * **Logic Quantity in order confirmation Equals purchase order**: questa condizione verifica se la quantità indicata nella conferma d'ordine corrisponde alla quantità nell'ordine di acquisto. Garantisce che l'elaborazione della fattura proceda solo se le quantità sono coerenti, aspetto fondamentale per la gestione dell'inventario e l'accuratezza finanziaria.

#### Azione (Then…):

* **Start Export**: una volta che la fattura soddisfa le condizioni specificate (ovvero le quantità corrispondono tra la conferma d'ordine e l'ordine di acquisto), viene attivata l'azione "Start Export". Questo comporta probabilmente l'esportazione dei dati della fattura per ulteriore elaborazione, eventualmente verso un altro sistema finanziario o a fini di reportistica.

#### Scopo di Questa Regola:

* **Ensure Accuracy and Consistency**: verificando che le quantità corrispondano tra la conferma d'ordine e l'ordine di acquisto, il sistema aiuta a mantenere l'accuratezza dell'inventario e previene discrepanze che potrebbero influire sulla reportistica finanziaria o sulla gestione delle scorte.
* **Streamline Financial Processing**: l'automazione dell'esportazione dei dati una volta confermate le quantità riduce la gestione manuale e accelera il ciclo di elaborazione finanziaria.
* **Enhance Compliance and Oversight**: richiedere una seconda approvazione per la verifica delle quantità aggiunge un ulteriore livello di supervisione, fondamentale per la conformità alle politiche e ai controlli finanziari.

Questa regola è un chiaro esempio di come l'automazione dei workflow possa essere utilizzata efficacemente per garantire una gestione precisa ed efficiente dei documenti finanziari all'interno di un'organizzazione, in particolare nel contesto di processi di acquisto che coinvolgono grandi volumi di transazioni che richiedono una convalida meticolosa.
