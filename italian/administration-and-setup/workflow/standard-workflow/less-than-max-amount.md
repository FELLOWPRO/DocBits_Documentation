# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Fattura"><figcaption></figcaption></figure>

Questo titolo suggerisce che la regola o condizione in fase di configurazione è progettata per gestire le fatture in cui l'importo totale è minore o uguale a un importo massimo specificato.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione verifica se il documento in elaborazione è una fattura. Questo è fondamentale per garantire che la regola si applichi solo alle fatture e non ad altri tipi di documenti.
2. **And…**
   * **Document Status is Pending Approval**: questo specifica che la fattura deve trovarsi nello stato "Pending Approval". Questa verifica dello stato garantisce che la regola si applichi solo alle fatture in attesa di approvazione.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: questa condizione confronta l'importo totale della fattura con l'importo massimo autorizzato di un approvatore. Se l'importo totale della fattura è minore o uguale a questo importo massimo, la regola prosegue al passaggio successivo. Probabilmente include un livello di tolleranza che consente lievi deviazioni entro limiti specificati.

#### Azione (Then…):

* **Assign user from field Approver Name, use user User as fallback**: se le condizioni specificate sono soddisfatte, la fattura viene assegnata automaticamente a un approvatore il cui nome è specificato in un campo. Se questo campo è vuoto o non disponibile, viene assegnato un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) come fallback per gestire l'approvazione.

#### Elementi dell'Interfaccia:

* **Add Card**: questo pulsante consente probabilmente agli utenti di aggiungere ulteriori condizioni o azioni alla regola, migliorando la flessibilità e la specificità del workflow.
* **Save**: salva la regola configurata nel sistema.

#### Scopo di Questa Regola:

Questa configurazione è progettata per semplificare il processo di approvazione delle fatture indirizzandole automaticamente all'approvatore appropriato in base all'importo e garantendo che solo quelle entro una determinata soglia vengano gestite in questo modo automatizzato. Aiuta nella gestione dei controlli finanziari e accelera il workflow riducendo i controlli manuali per ciascuna fattura.

\
