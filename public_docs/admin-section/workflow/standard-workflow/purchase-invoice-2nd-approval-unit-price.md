# Fattura d'acquisto - 2° Approvazione Prezzo Unitario

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Approvazione Fattura 3"><figcaption></figcaption></figure>

Questo titolo indica che la regola è impostata per gestire la seconda fase di approvazione di una fattura d'acquisto, con un focus specifico sulla convalida del prezzo unitario.

#### Configurazione della Regola:

1. **Quando…**
* **Il Tipo di Documento è Fattura**: Questa condizione garantisce che la regola venga attivata solo per documenti identificati come fatture, escludendo altri tipi di documenti e mantenendo la rilevanza del flusso di lavoro.
2. **E…**
* **Lo Stato del Documento è in Attesa di Seconda Approvazione**: Questo specifica che la fattura si trova nella fase in cui è in attesa di una seconda approvazione. Questo è di solito un passaggio progettato per garantire un'ulteriore supervisione prima dell'elaborazione finale.
* **Il Campo del Documento Sottotipo Fattura è Uguale a Fattura d'Acquisto**: Questo restringe ulteriormente l'applicazione di questa regola solo alle fatture classificate come "Fatture d'Acquisto", distinguendole dagli altri sottotipi di fatture.
* **Logica Prezzo Unitario nella conferma dell'ordine Non Uguale all'ordine d'acquisto**: Questo controllo logico è cruciale poiché confronta il prezzo unitario indicato nella conferma dell'ordine con il prezzo unitario nell'ordine d'acquisto originale. L'azione viene attivata se questi valori non corrispondono, il che potrebbe indicare una discrepanza che necessita di risoluzione.

#### Azione (Quindi…):

* **Assegna utente dal campo Nome Acquirente, utilizza utente Utente come fallback**: Se le condizioni specificate sono soddisfatte (cioè c'è una discrepanza nei prezzi unitari), la fattura viene automaticamente assegnata a un acquirente (il nome specificato nel campo 'Nome Acquirente') per ulteriore revisione. Se il campo 'Nome Acquirente' è vuoto o non specificato, un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) viene assegnato come fallback per gestire l'approvazione.

#### Scopo di Questa Regola:

* **Garantire Precisione e Conformità**: Questa regola è fondamentale per garantire che il processo di fatturazione sia preciso e conforme ai termini concordati. Attivando una revisione in presenza di una discrepanza nei prezzi unitari, il sistema aiuta a prevenire errori finanziari o potenziali frodi.
* **Ottimizzare le Approvazioni**: Automatizzare l'assegnazione per la revisione in base a discrepanze specifiche aiuta a ottimizzare il processo di approvazione e garantisce che i problemi siano prontamente affrontati dal personale appropriato.
* **Supervisione Finanziaria**: Richiedere una seconda approvazione, specialmente basata sull'abbinamento dei prezzi, rafforza i controlli finanziari e la responsabilità all'interno dell'organizzazione.
