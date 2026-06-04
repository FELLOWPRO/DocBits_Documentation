# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Approvazione Fattura 4"><figcaption></figcaption></figure>

Questo titolo indica che la regola riguarda specificamente la gestione delle fatture d'acquisto durante una fase di approvazione secondaria, con particolare attenzione alla verifica dell'accuratezza delle quantità elencate.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione garantisce che la regola venga attivata solo per i documenti classificati come fatture. Questo è essenziale per mantenere la specificità e la pertinenza nel workflow.
2. **And…**
   * **Document Status is Pending Second Approval**: questo specifica che la fattura è attualmente in attesa di una seconda approvazione. Questa fase è in genere intesa a fornire una supervisione aggiuntiva prima di finalizzare la fattura.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: questa condizione affina ulteriormente la regola affinché si applichi esclusivamente alle fatture identificate come "Purchase Invoices". Questa categorizzazione aiuta a differenziarle dagli altri tipi di fattura.
   * **Logic Quantity in order confirmation Not Equals purchase order**: questa condizione fondamentale verifica se la quantità indicata nella conferma d'ordine corrisponde alla quantità sull'ordine di acquisto originale. L'azione viene attivata in presenza di una discrepanza, che indica un potenziale errore o problema che deve essere risolto.

#### Azione (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: se le condizioni della regola sono soddisfatte (ovvero esiste una discrepanza nelle quantità), la fattura viene assegnata automaticamente alla persona indicata nel campo 'Buyer Name' per ulteriore revisione. Se questo campo è vuoto o la persona specificata non è disponibile, subentra un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) per garantire una revisione e una risoluzione tempestive.

#### Scopo di Questa Regola:

* **Accuracy and Compliance**: la regola è essenziale per garantire che il processo di fatturazione sia accurato e in linea con i termini concordati nell'ordine di acquisto. Aiuta a prevenire discrepanze finanziarie e potenziali errori di inventario.
* **Streamlined Approvals**: l'automazione del processo di revisione per discrepanze specifiche aiuta a semplificare le approvazioni e garantisce che eventuali problemi vengano affrontati rapidamente dal personale appropriato.
* **Enhanced Financial Oversight**: richiedere un'approvazione secondaria per le verifiche delle quantità rafforza i controlli finanziari e la responsabilità all'interno dell'organizzazione.

Questa configurazione esemplifica come l'automazione dei workflow possa essere utilizzata per migliorare l'efficienza operativa e garantire l'integrità finanziaria, in particolare nella gestione di processi di acquisto complessi all'interno di un'azienda.
