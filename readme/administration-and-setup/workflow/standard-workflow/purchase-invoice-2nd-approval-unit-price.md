# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Approvazione Fattura 3"><figcaption></figcaption></figure>

Questo titolo indica che la regola è configurata per gestire la seconda fase di approvazione di una fattura d'acquisto, con particolare attenzione alla convalida del prezzo unitario.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione garantisce che la regola venga attivata solo per i documenti identificati come fatture, escludendo gli altri tipi di documento e mantenendo la pertinenza del workflow.
2. **And…**
   * **Document Status is Pending Second Approval**: questo specifica che la fattura si trova nella fase in cui è in attesa di una seconda approvazione. Si tratta di solito di un passaggio progettato per garantire una supervisione aggiuntiva prima dell'elaborazione finale.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: questo restringe ulteriormente l'applicazione di questa regola alle sole fatture classificate come "Purchase Invoices", distinguendole dagli altri sottotipi di fattura.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: questa verifica logica è fondamentale poiché confronta il prezzo unitario indicato nella conferma d'ordine con il prezzo unitario nell'ordine di acquisto originale. L'azione viene attivata se questi valori non corrispondono, il che potrebbe indicare una discrepanza che deve essere risolta.

#### Azione (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: se le condizioni specificate sono soddisfatte (ovvero esiste una mancata corrispondenza nei prezzi unitari), la fattura viene assegnata automaticamente a un acquirente (il nome specificato nel campo 'Buyer Name') per ulteriore revisione. Se il campo 'Buyer Name' è vuoto o non specificato, viene assegnato un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) come fallback per gestire l'approvazione.

#### Scopo di Questa Regola:

* **Ensure Accuracy and Compliance**: questa regola è fondamentale per garantire che il processo di fatturazione sia accurato e conforme ai termini concordati. Attivando una revisione in presenza di una discrepanza nei prezzi unitari, il sistema aiuta a prevenire errori finanziari o potenziali frodi.
* **Streamline Approvals**: l'automazione dell'assegnazione per la revisione in base a discrepanze specifiche aiuta a semplificare il processo di approvazione e garantisce che i problemi vengano affrontati tempestivamente dal personale appropriato.
* **Financial Oversight**: richiedere una seconda approvazione, soprattutto basata sulla corrispondenza dei prezzi, rafforza i controlli finanziari e la responsabilità all'interno dell'organizzazione.
