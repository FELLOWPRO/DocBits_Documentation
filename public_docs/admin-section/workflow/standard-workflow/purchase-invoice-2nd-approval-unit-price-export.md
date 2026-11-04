# Fattura di acquisto - Esportazione del prezzo unitario di approvazione 2°

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Acquisto Ordine Esporta 5"><figcaption></figcaption></figure>

Questo titolo indica che la regola è impostata per gestire la seconda fase di approvazione delle fatture di acquisto con un focus sul prezzo unitario, garantendo che corrisponda ai termini concordati.

#### Configurazione della regola:

1. **Quando…**
* **Il tipo di documento è Fattura**: Questa condizione garantisce che la regola sia attivata solo per i documenti identificati come fatture, il che è cruciale per indirizzare il flusso di lavoro in modo accurato.
2. **E…**
* **Lo stato del documento è in attesa di seconda approvazione**: Questo specifica che la fattura è in attesa di una seconda approvazione. Questa fase fornisce spesso un controllo aggiuntivo per garantire l'accuratezza prima di finalizzare la transazione.
* **Il sottotipo di fattura è Uguale a Fattura di acquisto**: Questa condizione specifica ulteriormente che la regola si applica solo alle fatture categorizzate specificamente come "Fatture di acquisto", differenziandole da altri tipi di fatture.
* **Logica Prezzo unitario nella conferma dell'ordine Uguale all'ordine di acquisto**: Questa condizione verifica se il prezzo unitario indicato nella conferma dell'ordine corrisponde al prezzo unitario nell'ordine di acquisto. Garantisce che l'elaborazione della fattura proceda solo se c'è coerenza nei prezzi, che è fondamentale per la pianificazione del budget e la rendicontazione finanziaria.

#### Azione (Quindi…):

* **Avvia esportazione**: Una volta che la fattura soddisfa le condizioni specificate (cioè i prezzi unitari corrispondono tra la conferma dell'ordine e l'ordine di acquisto), viene attivata l'azione "Avvia esportazione". Questo probabilmente comporta l'esportazione dei dati della fattura per ulteriore elaborazione, eventualmente verso un altro sistema finanziario o per scopi di rendicontazione.

#### Scopo di questa regola:

* **Garantire accuratezza e coerenza**: Verificando che i prezzi unitari corrispondano tra la conferma dell'ordine e l'ordine di acquisto, il sistema aiuta a mantenere l'accuratezza finanziaria e a prevenire sovraccarichi o sottovalutazioni.
* **Ottimizzare l'elaborazione finanziaria**: Automatizzando l'esportazione dei dati una volta confermati i prezzi, si riduce la manipolazione manuale e si accelera il ciclo di elaborazione finanziaria.
* **Potenziare la conformità e il controllo**: Richiedere una seconda approvazione per la verifica dei prezzi aggiunge un ulteriore livello di controllo, che è cruciale per la conformità alle politiche e ai controlli finanziari.

Questa regola è un esempio di come l'automazione del flusso di lavoro possa essere utilizzata in modo efficace per garantire un'elaborazione precisa ed efficiente dei documenti finanziari all'interno di un'organizzazione, in particolare nel contesto di grandi volumi di transazioni che richiedono una valida validazione.
