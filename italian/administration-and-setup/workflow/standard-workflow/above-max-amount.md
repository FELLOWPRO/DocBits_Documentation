# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Fattura 2"><figcaption></figcaption></figure>

Questo titolo indica che la regola è progettata per gestire i casi in cui il totale della fattura è maggiore dell'importo massimo che un approvatore è autorizzato a gestire.

#### Configurazione della Regola:

1. **When…**
   * **Document Type is Invoice**: questa condizione garantisce che la regola si applichi solo alle fatture, aspetto essenziale per instradare correttamente il workflow.
2. **And…**
   * **Document Status is Pending Approval**: la fattura deve trovarsi nello stato "Pending Approval". Questo stato è fondamentale per garantire che la regola venga applicata alle fatture ancora in elaborazione e non ancora finalizzate.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: questa condizione verifica se l'importo totale della fattura supera l'importo massimo che un approvatore è autorizzato a gestire. Questo confronto può includere anche un'impostazione di tolleranza, consentendo lievi variazioni in base a criteri predefiniti.

#### Azione (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: se la fattura supera l'importo massimo specificato, viene assegnata automaticamente a un approvatore di livello superiore, indicato dal campo 'Next Level Approver'. Se questo campo non è compilato o l'utente specificato non è disponibile, viene utilizzato un utente predefinito (probabilmente un amministratore o un altro membro del personale designato) come fallback per garantire che la fattura venga esaminata senza ritardi.

#### Elementi dell'Interfaccia:

* **Add Card**: questa opzione consente di aggiungere condizioni o azioni aggiuntive alla regola, offrendo flessibilità per affrontare scenari complessi.
* **Save**: questo pulsante salva la configurazione della regola nel sistema.

#### Scopo di Questa Regola:

Lo scopo di questa regola è garantire che le fatture che superano determinate soglie finanziarie vengano esaminate da approvatori con i livelli di autorizzazione appropriati. Questo aiuta a mantenere il controllo e la supervisione finanziaria, assicurando che le spese vengano esaminate da personale con i limiti di approvazione richiesti, tutelando così l'organizzazione da spese non autorizzate o inappropriate.

Questa regola, come la precedente, aiuta ad automatizzare il workflow, riducendo lo sforzo manuale e migliorando la conformità alle politiche finanziarie dell'organizzazione. È un esempio di come l'automazione dei workflow possa essere utilizzata efficacemente per gestire processi finanziari complessi all'interno di un'azienda.
