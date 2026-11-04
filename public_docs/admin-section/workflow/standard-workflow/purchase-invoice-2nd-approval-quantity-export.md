# Fattura di acquisto - Esportazione della quantità di approvazione 2

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Acquisto Ordine Esporta 6"><figcaption></figcaption></figure>

Questo titolo indica che la regola è impostata per gestire la seconda fase di approvazione per le fatture di acquisto con un'enfasi sui dettagli della quantità, garantendo che le quantità sulla fattura corrispondano a quelle dell'ordine di acquisto originale.

#### Configurazione della regola:

1. **Quando...**
* **Il tipo di documento è Fattura**: Questa condizione garantisce che la regola sia attivata solo per i documenti identificati come fatture, il che è cruciale per indirizzare il flusso di lavoro in modo accurato.
2. **E...**
* **Lo stato del documento è in attesa di seconda approvazione**: Questo specifica che la fattura è attualmente in attesa di una seconda approvazione. Questa fase fornisce spesso un controllo aggiuntivo per garantire l'accuratezza prima che la transazione venga finalizzata.
* **Il sottotipo di fattura è Uguale a Fattura di acquisto**: Questa condizione specifica ulteriormente che la regola si applica solo alle fatture categorizzate specificamente come "Fatture di acquisto", differenziandole da altri tipi di fatture.
* **Quantità logica nella conferma dell'ordine Uguale all'ordine di acquisto**: Questa condizione verifica se la quantità elencata nella conferma dell'ordine corrisponde alla quantità nell'ordine di acquisto. Garantisce che l'elaborazione della fattura proceda solo se le quantità sono coerenti, il che è fondamentale per la gestione dell'inventario e l'accuratezza finanziaria.

#### Azione (Quindi...):

* **Avvia esportazione**: Una volta che la fattura soddisfa le condizioni specificate (cioè le quantità corrispondono tra la conferma dell'ordine e l'ordine di acquisto), viene attivata l'azione "Avvia esportazione". Questo probabilmente comporta l'esportazione dei dati della fattura per ulteriore elaborazione, eventualmente verso un altro sistema finanziario o per scopi di reportistica.

#### Scopo di questa regola:

* **Garantire accuratezza e coerenza**: Verificando che le quantità corrispondano tra la conferma dell'ordine e l'ordine di acquisto, il sistema aiuta a mantenere l'accuratezza dell'inventario e a prevenire discrepanze che potrebbero influenzare la reportistica finanziaria o la gestione delle scorte.
* **Ottimizzare l'elaborazione finanziaria**: L'automazione dell'esportazione dei dati una volta confermate le quantità riduce la manipolazione manuale e accelera il ciclo di elaborazione finanziaria.
* **Potenziare la conformità e il controllo**: Richiedere una seconda approvazione per la verifica delle quantità aggiunge un ulteriore livello di controllo, cruciale per la conformità alle politiche e ai controlli finanziari.

Questa regola è un chiaro esempio di come l'automazione del flusso di lavoro possa essere utilizzata in modo efficace per garantire un'elaborazione precisa ed efficiente dei documenti finanziari all'interno di un'organizzazione, in particolare nel contesto dei processi di acquisto che coinvolgono grandi volumi di transazioni che richiedono una valida validazione.
