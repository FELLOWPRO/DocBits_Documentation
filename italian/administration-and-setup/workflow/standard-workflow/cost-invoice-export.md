# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Acquisto Ordine Esporta 4"><figcaption></figcaption></figure>

Questo titolo indica che la regola è configurata specificamente per la gestione delle fatture di costo e prevede un'azione di esportazione, eventualmente per la reportistica, l'ulteriore elaborazione o l'integrazione con altri sistemi.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione garantisce che la regola venga attivata solo per i documenti classificati come fatture, mantenendo la specificità del workflow alla gestione delle fatture.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: questo specifica che la regola si applica solo alle fatture esplicitamente contrassegnate come "Cost Invoices" in un determinato campo del documento. Questo aiuta a distinguerle da altri tipi di fatture.
   * **Document Status is Pending Second Approval**: la fattura deve trovarsi nello stato "Pending Second Approval". Questo indica che la fattura ha già superato un'approvazione iniziale ed è in attesa di una seconda revisione, possibilmente definitiva.

#### Azione (Then…):

* **Start Export**: una volta che la fattura soddisfa le condizioni specificate (essere una fattura di costo e in attesa di seconda approvazione), viene eseguita l'azione "Start Export". Questo può comportare l'invio dei dati della fattura a un altro sistema per analisi finanziaria, reportistica o finalità di conformità.

#### Scopo di Questa Regola:

* **Workflow Efficiency**: questa regola aiuta ad automatizzare la gestione delle fatture di costo garantendo che vengano elaborate attraverso le fasi di approvazione necessarie senza intervento manuale, aumentando la velocità e l'accuratezza delle operazioni finanziarie.
* **Control and Compliance**: richiedendo una seconda approvazione, il sistema applica un meccanismo di controllo che garantisce una revisione approfondita delle fatture di costo, migliorando la supervisione finanziaria.
* **Integration and Reporting**: l'azione di esportazione suggerisce che, una volta completamente approvate, le fatture possono essere integrate in altri sistemi per ulteriore elaborazione o analisi, aspetto fondamentale per la reportistica finanziaria e gli audit.

Questo tipo di regola è essenziale per le organizzazioni che trattano vari tipi di fatture e devono garantire che ciascun tipo sia gestito secondo protocolli specifici. Riduce il rischio di errori e garantisce la conformità ai controlli interni e alle normative esterne.
