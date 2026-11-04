# Singola condizione stato documento

<figure><img src="../../../../.gitbook/assets/docbits_single_doc_status.png" alt="DocBits Single Doc Stato" width="528"><figcaption></figcaption></figure>

**Scopo**

Questa carta di flusso di lavoro è progettata per gestire le operazioni sui documenti in base a un singolo stato del documento specificato. Semplificando la condizione a un unico stato, la carta si focalizza su trigger di flusso di lavoro molto specifici, rendendola ideale per attività di elaborazione documenti mirate all'interno di un sistema ERP.

**Componenti della carta**

1. **Operatore**
   * **Descrizione**: Specifica il metodo per valutare lo stato del documento rispetto alla condizione selezionata.
   * **Opzioni**:
     * **è (is)**: Attiva l'operazione se lo stato attuale del documento corrisponde allo stato selezionato.
     * **non è (is not)**: Attiva l'operazione se lo stato attuale del documento non corrisponde allo stato selezionato.
2. **Stato**
   * **Descrizione**: Consente la selezione di un singolo stato del documento per impostare la condizione.
   * **Esempi di stati**: "Errore", "Errore di esportazione", "Pronto in convalida", "Pronto in revisione", "In attesa di approvazione", "In attesa di seconda approvazione".
   * **Dettaglio**: Gli utenti scelgono uno stato da un menu a discesa o da un set di pulsanti di opzione. Questo stato funge quindi da criterio per l'operazione della carta.

**Funzionalità**

* **Identificazione dello stato del documento**: Identifica lo stato attuale di un documento mentre viene elaborato attraverso il sistema ERP.
* **Valutazione della condizione**:
  * In base all'operatore selezionato (`è` o `non è`), la carta controlla se lo stato attuale del documento è in linea con il criterio dello stato scelto.
* **Esecuzione dell'azione**:
  * **Condizione vera**: Se lo stato corrisponde (o non corrisponde, in base all'operatore), viene avviata l'azione corrispondente. Ciò potrebbe includere l'instradamento per un'ulteriore elaborazione, la generazione di notifiche o altri flussi di lavoro predefiniti.
  * **Condizione falsa**: Se la condizione non è soddisfatta, non viene intrapresa alcuna azione o viene attivato un percorso alternativo.
* **Integrazione con altri flussi di lavoro**: Sebbene sia progettata per la valutazione di un singolo stato, questa carta può essere integrata efficacemente in sequenze di flussi di lavoro più ampie per garantire una gestione precisa dei documenti.

**Interazioni dell'utente**

* **Installazione e configurazione**: Gli utenti impostano la carta selezionando un operatore e quindi scegliendo uno stato dalle opzioni disponibili. Questo processo di selezione è semplice e progettato per evitare confusioni.
* **Monitoraggio e reporting**: Consente il monitoraggio tramite report generati dal sistema o dashboard che tracciano l'elaborazione dei documenti in base al loro stato, aiutando a supervisionare l'efficacia dei flussi di lavoro implementati.
* **Gestione degli errori e notifiche**: Configurabile per avvisare gli utenti di eventuali anomalie di elaborazione o per segnalare documenti che non soddisfano le condizioni impostate, garantendo un'attenzione e una risoluzione tempestive.

#### Conclusione

La carta di flusso di lavoro "Singola condizione stato documento" semplifica la gestione dei documenti concentrandosi sulle singole condizioni di stato. Questa specifica aiuta nei casi in cui è necessario un controllo preciso sui flussi dei documenti, specialmente in ambienti con criteri di elaborazione rigorosi. Documentare chiaramente questa versione della carta garantirà che gli utenti ne comprendano appieno l'applicazione e possano integrarla efficacemente nelle loro operazioni quotidiane, migliorando sia la conformità che l'efficienza nell'elaborazione dei documenti.
