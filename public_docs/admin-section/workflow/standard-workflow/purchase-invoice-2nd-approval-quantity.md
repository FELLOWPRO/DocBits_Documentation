# Fattura d'acquisto - Quantità di approvazione 2°

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Approvazione Fattura 4"><figcaption></figcaption></figure>

Questo titolo indica che la regola si riferisce specificamente alla gestione delle fatture d'acquisto durante una fase di approvazione secondaria, con un focus sulla verifica dell'accuratezza delle quantità elencate.

#### Configurazione della regola:

1. **Quando...**
* **Il tipo di documento è Fattura**: Questa condizione garantisce che la regola sia attivata solo per i documenti classificati come fatture. Questo è essenziale per mantenere specificità e rilevanza nel flusso di lavoro.
2. **E...**
* **Lo stato del documento è in attesa di seconda approvazione**: Questo specifica che la fattura è attualmente in attesa di una seconda approvazione. Questa fase è tipicamente destinata a fornire un controllo aggiuntivo prima di finalizzare la fattura.
* **Il sotto tipo di fattura è Uguale a Fattura d'acquisto**: Questa condizione raffina ulteriormente la regola per applicarsi esclusivamente alle fatture identificate come "Fatture d'acquisto". Questa categorizzazione aiuta a differenziarle da altri tipi di fatture.
* **Quantità logica nella conferma dell'ordine Non Uguale all'ordine d'acquisto**: Questa condizione critica verifica se la quantità indicata nella conferma dell'ordine corrisponde alla quantità nell'ordine d'acquisto originale. L'azione viene attivata in caso di discrepanza, indicando un potenziale errore o problema che necessita di risoluzione.

#### Azione (Quindi...):

* **Assegna utente dal campo Nome acquirente, utilizza utente Utente come fallback**: Se le condizioni della regola sono soddisfatte (cioè c'è una discrepanza nelle quantità), la fattura viene automaticamente assegnata alla persona elencata nel campo 'Nome acquirente' per ulteriore revisione. Se questo campo è vuoto o la persona specificata non è disponibile, un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) interviene per garantire una revisione e risoluzione tempestive.

#### Scopo di questa regola:

* **Precisione e conformità**: La regola è vitale per garantire che il processo di fatturazione sia preciso e allineato con i termini concordati nell'ordine d'acquisto. Aiuta a prevenire discrepanze finanziarie e potenziali errori di inventario.
* **Approvazioni ottimizzate**: Automatizzare il processo di revisione per specifiche discrepanze aiuta ad ottimizzare le approvazioni e garantisce che eventuali problemi siano affrontati rapidamente dal personale appropriato.
* **Miglioramento della supervisione finanziaria**: Richiedere un'approvazione secondaria per le verifiche di quantità rafforza i controlli finanziari e la responsabilità all'interno dell'organizzazione.

Questa configurazione esemplifica come l'automazione del flusso di lavoro possa essere utilizzata per migliorare l'efficienza operativa e garantire l'integrità finanziaria, in particolare nella gestione dei processi di acquisto complessi all'interno di un'azienda.
