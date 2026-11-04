# Condizione dello Stato del Singolo Documento

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda di flusso di lavoro è progettata per gestire le operazioni sui documenti basate su uno stato di documento specifico. Semplificando la condizione a uno stato, la scheda si concentra su trigger di flusso di lavoro molto specifici, rendendola ideale per attività di elaborazione documenti mirate all'interno di un sistema ERP.

**Componenti della Scheda**

1. **Operatore**
* **Descrizione**: Specifica il metodo per valutare lo stato del documento rispetto alla condizione selezionata.
* **Opzioni**:
* **è**: Attiva l'operazione se lo stato attuale del documento corrisponde allo stato selezionato.
* **non è**: Attiva l'operazione se lo stato attuale del documento non corrisponde allo stato selezionato.
2. **Stato**
* **Descrizione**: Consente la selezione di uno stato di documento singolo per impostare la condizione.
* **Esempi di Stati**: "Errore", "Errore di Esportazione", "Pronto per la Validazione", "Pronto per la Revisione", "Approvazione in Attesa", "Seconda Approvazione in Attesa".
* **Dettaglio**: Gli utenti scelgono uno stato da un menu a discesa o da un insieme di pulsanti radio. Questo stato funge da criterio per l'operazione della scheda.

**Funzionalità**

* **Identificazione dello Stato del Documento**: Identifica lo stato attuale di un documento mentre viene elaborato attraverso il sistema ERP.
* **Valutazione della Condizione**:
* In base all'operatore selezionato (`è` o `non è`), la scheda verifica se lo stato attuale del documento corrisponde al criterio di stato scelto.
* **Esecuzione dell'Azione**:
* **Condizione Vera**: Se lo stato corrisponde (o non corrisponde, in base all'operatore), viene avviata l'azione corrispondente. Questo potrebbe essere l'instradamento per ulteriore elaborazione, la generazione di notifiche o altri flussi di lavoro predefiniti.
* **Condizione Falsa**: Se la condizione non è soddisfatta, non viene intrapresa alcuna azione o viene attivato un percorso alternativo.
* **Integrazione con Altri Flussi di Lavoro**: Anche se è progettata per la valutazione di uno stato singolo, questa scheda può essere integrata efficacemente in sequenze di flussi di lavoro più ampie per garantire una gestione precisa dei documenti.

**Interazioni con l'Utente**

* **Configurazione e Impostazione**: Gli utenti configurano la scheda selezionando un operatore e quindi scegliendo uno stato dalle opzioni disponibili. Questo processo di selezione è semplice e progettato per evitare confusione.
* **Monitoraggio e Reporting**: Consente il monitoraggio attraverso report generati dal sistema o dashboard che tracciano l'elaborazione dei documenti in base al loro stato, aiutando a supervisionare l'efficacia dei flussi di lavoro implementati.
* **Gestione degli Errori e Notifiche**: Configurabile per avvisare gli utenti su eventuali anomalie di elaborazione o per segnalare documenti che non soddisfano le condizioni impostate, garantendo un'attenzione e una risoluzione tempestive.

#### Conclusione

La scheda di flusso di lavoro "Condizione dello Stato del Singolo Documento" semplifica la gestione dei documenti concentrandosi sulle condizioni di stato individuali. Questa specifica è utile nei casi in cui è necessario un controllo preciso sui flussi dei documenti, specialmente in ambienti con criteri di elaborazione rigorosi. Documentare chiaramente questa versione della scheda garantirà che gli utenti comprendano appieno la sua applicazione e possano integrarla efficacemente nelle loro operazioni quotidiane, migliorando sia la conformità che l'efficienza nell'elaborazione dei documenti.
