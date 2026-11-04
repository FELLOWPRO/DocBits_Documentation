# Importo inferiore al massimo

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Fattura"><figcaption></figcaption></figure>

Questo titolo suggerisce che la regola o la condizione in fase di configurazione è progettata per gestire le fatture in cui l'importo totale è inferiore o uguale a un importo massimo specificato.

#### Configurazione della regola:

1. **Quando…**
* **Il tipo di documento è Fattura**: Questa condizione verifica se il documento in fase di elaborazione è una fattura. Questo è cruciale per garantire che la regola si applichi solo alle fatture e non ad altri tipi di documenti.
2. **E…**
* **Lo stato del documento è In attesa di approvazione**: Questo specifica che la fattura deve trovarsi in uno stato di "In attesa di approvazione". Questo controllo di stato garantisce che la regola si applichi solo alle fatture in attesa di approvazione.
* **Confronta due campi: Importo totale inferiore o uguale all'importo massimo dell'approvatore**: Questa condizione confronta l'importo totale della fattura con l'importo massimo autorizzato di un approvatore. Se l'importo totale della fattura è inferiore o uguale a questo importo massimo, la regola passa al passaggio successivo. Questo probabilmente include un livello di tolleranza che consente piccole deviazioni entro limiti specificati.

#### Azione (Quindi…):

* **Assegna utente dal campo Nome dell'approvatore, utilizza l'utente Utente come fallback**: Se le condizioni specificate sono soddisfatte, la fattura viene automaticamente assegnata a un approvatore il cui nome è specificato in un campo. Se questo campo è vuoto o non disponibile, viene assegnato un utente predefinito (probabilmente un amministratore o un altro membro dello staff designato) come fallback per gestire l'approvazione.

#### Elementi dell'interfaccia:

* **Aggiungi carta**: Questo pulsante probabilmente consente agli utenti di aggiungere ulteriori condizioni o azioni alla regola, migliorando la flessibilità e la specificità del flusso di lavoro.
* **Salva**: Salva la regola configurata nel sistema.

#### Scopo di questa regola:

Questa configurazione è progettata per razionalizzare il processo di approvazione delle fatture, indirizzando automaticamente le fatture all'approvatore appropriato in base all'importo e garantendo che solo quelle entro una certa soglia siano gestite in questo modo automatizzato. Aiuta a gestire i controlli finanziari e velocizza il flusso di lavoro riducendo i controlli manuali per ciascuna fattura.
