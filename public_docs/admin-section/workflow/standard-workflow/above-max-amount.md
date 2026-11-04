# Importo massimo superato

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Fattura 2"><figcaption></figcaption></figure>

Questo titolo indica che la regola è progettata per gestire i casi in cui l'importo totale della fattura è maggiore dell'importo massimo che un approvatore è autorizzato a gestire.

#### Configurazione della regola:

1. **Quando…**
* **Il tipo di documento è Fattura**: Questa condizione garantisce che la regola si applichi solo alle fatture, il che è essenziale per indirizzare correttamente il flusso di lavoro.
2. **E…**
* **Lo stato del documento è in attesa di approvazione**: La fattura deve trovarsi in uno stato di "In attesa di approvazione". Questo stato è cruciale per garantire che la regola venga applicata alle fatture che sono ancora in fase di elaborazione e non sono ancora state finalizzate.
* **Confronta due campi: Importo totale maggiore dell'importo massimo dell'approvatore**: Questa condizione verifica se l'importo totale della fattura supera l'importo massimo che un approvatore è autorizzato a gestire. Questo confronto potrebbe includere anche un'impostazione di tolleranza, consentendo variazioni minori basate su criteri predefiniti.

#### Azione (Quindi…):

* **Assegna utente dal campo Prossimo Livello Approvatore, utilizza l'utente Utente come fallback**: Se la fattura supera l'importo massimo specificato, viene automaticamente assegnata a un approvatore di livello superiore, indicato dal campo 'Prossimo Livello Approvatore'. Se questo campo non è compilato o l'utente specificato non è disponibile, viene utilizzato un utente predefinito (probabilmente un amministratore o un altro membro dello staff designato) come fallback per garantire che la fattura venga esaminata senza ritardi.

#### Elementi dell'interfaccia:

* **Aggiungi Carta**: Questa opzione consente di aggiungere condizioni o azioni aggiuntive alla regola, offrendo flessibilità per affrontare scenari complessi.
* **Salva**: Questo pulsante salva la configurazione della regola nel sistema.

#### Scopo di questa regola:

Lo scopo di questa regola è garantire che le fatture che superano determinate soglie finanziarie siano esaminate da approvatori con i livelli di autorizzazione appropriati. Ciò aiuta a mantenere il controllo finanziario e la supervisione, garantendo che le spese siano esaminate da personale con i limiti di approvazione richiesti, proteggendo così l'organizzazione da spese non autorizzate o inappropriati.

Questa regola, come la precedente, aiuta ad automatizzare il flusso di lavoro, riducendo lo sforzo manuale e migliorando la conformità con le politiche finanziarie dell'organizzazione. È un esempio di come l'automazione del flusso di lavoro possa essere utilizzata in modo efficace per gestire processi finanziari complessi all'interno di un'azienda.
