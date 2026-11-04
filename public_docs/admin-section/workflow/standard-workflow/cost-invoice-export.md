# Fattura di Costo - Esportazione

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Acquisto Ordine Esporta 4"><figcaption></figcaption></figure>

Questo titolo indica che la regola è configurata specificamente per gestire le fatture di costo e coinvolge un'azione di esportazione, eventualmente per scopi di reportistica, ulteriore elaborazione o integrazione con altri sistemi.

#### Configurazione della Regola:

1. **Quando…**
* **Il Tipo di Documento è Fattura**: Questa condizione garantisce che la regola venga attivata solo per i documenti categorizzati come fatture, mantenendo la specificità del flusso di lavoro per la gestione delle fatture.
2. **E…**
* **Il Sotto Tipo di Fattura è Uguale a Fattura di Costo**: Questo specifica che la regola si applica solo a quelle fatture contrassegnate esplicitamente come "Fatture di Costo" in un campo specifico all'interno del documento. Questo aiuta a distinguerle da altri tipi di fatture.
* **Lo Stato del Documento è in Attesa di Seconda Approvazione**: La fattura deve trovarsi in uno stato di "Attesa di Seconda Approvazione". Questo indica che la fattura ha già superato un'approvazione iniziale ed è in attesa di una seconda, eventualmente finale, revisione.

#### Azione (Quindi…):

* **Avvia Esportazione**: Una volta che la fattura soddisfa le condizioni specificate (essere una fattura di costo e in attesa di seconda approvazione), viene eseguita l'azione di "Avvio dell'Esportazione". Questo potrebbe comportare l'invio dei dati della fattura a un altro sistema per analisi finanziarie, reportistica o scopi di conformità.

#### Scopo di Questa Regola:

* **Efficienza del Flusso di Lavoro**: Questa regola aiuta ad automatizzare la gestione delle fatture di costo garantendo che vengano elaborate attraverso le fasi di approvazione necessarie senza intervento manuale, aumentando la velocità e l'accuratezza delle operazioni finanziarie.
* **Controllo e Conformità**: Richiedendo una seconda approvazione, il sistema applica un meccanismo di controllo che garantisce che le fatture di costo siano attentamente esaminate, migliorando la supervisione finanziaria.
* **Integrazione e Reportistica**: L'azione di esportazione suggerisce che una volta che le fatture sono completamente approvate, possono essere integrate in altri sistemi per ulteriori elaborazioni o analisi, il che è fondamentale per la reportistica finanziaria e le verifiche.

Questo tipo di regola è vitale per le organizzazioni che gestiscono vari tipi di fatture e devono garantire che ciascun tipo venga gestito secondo protocolli specifici. Riduce il rischio di errori e garantisce la conformità con i controlli interni e le normative esterne.
