# Elenco condizioni stato documento

<figure><img src="../../../../.gitbook/assets/docbits_doc_status_list.png" alt="DocBits Doc Stato Elenco" width="521"><figcaption></figcaption></figure>

**Scopo**

Questa carta è progettata per controllare le azioni del flusso di lavoro in base allo stato attuale di un documento, utilizzando la logica condizionale per attivare o limitare determinati processi. Garantisce che i documenti procedano attraverso i flussi di lavoro solo quando soddisfano i criteri di stato predefiniti.

**Componenti della carta**

1. **Operatore**
   * **Descrizione**: Determina come verrà valutato lo stato del documento rispetto a una condizione specificata.
   * **Opzioni**:
     * **è (is)**: Attiva le azioni associate se lo stato attuale del documento corrisponde a uno degli stati specificati.
     * **non è (is not)**: Attiva le azioni se lo stato del documento non corrisponde a nessuno degli stati specificati.
2. **Stato (Elenco)**
   * **Descrizione**: Elenca gli stati specifici rispetto ai quali verrà confrontato lo stato attuale del documento.
   * **Esempi**: "Errore", "Errore di esportazione", "Pronto in convalida", "Pronto in revisione", "In attesa di approvazione", "In attesa di seconda approvazione". Questi rappresentano diverse fasi o condizioni in cui un documento potrebbe trovarsi all'interno di un processo di flusso di lavoro.

**Funzionalità**

* **Identificazione dello stato**: Identifica automaticamente lo stato attuale di un documento mentre si muove attraverso il flusso di lavoro del sistema ERP.
* **Valutazione della condizione**: Applica l'operatore scelto (è o non è) allo stato del documento in confronto agli stati elencati:
  * Se **è**, controlla se lo stato del documento corrisponde a qualsiasi stato nell'elenco.
  * Se **non è**, controlla se lo stato del documento non appare nell'elenco.
* **Esecuzione dell'azione**: A seconda dell'esito della valutazione della condizione:
  * **Vero**: Esegue azioni o flussi di lavoro predefiniti se la condizione è soddisfatta.
  * **Falso**: Salta o attiva flussi di lavoro alternativi se la condizione non è soddisfatta.
* **Integrazione del flusso di lavoro**: Si integra perfettamente con altri componenti del flusso di lavoro, garantendo che la gestione dei documenti sia coordinata in tutto il sistema.

**Interazioni dell'utente**

* **Installazione e configurazione**: Gli utenti configurano la carta selezionando l'operatore e specificando gli stati rilevanti. Questa configurazione può comportare semplici menu a discesa o caselle di controllo per la selezione di stati e operatori.
* **Monitoraggio e gestione**: Gli utenti possono monitorare l'attività della carta tramite una dashboard, che fornisce approfondimenti sulle condizioni di stato monitorate e sulle azioni intraprese in base a tali condizioni.
* **Gestione degli errori e avvisi**: Supporta l'impostazione di avvisi per errori di processo o discrepanze negli stati dei documenti previsti, consentendo risposte rapide ai problemi operativi.

#### Conclusione

La carta di flusso di lavoro "Condizione stato documento" è fondamentale per garantire che i documenti vengano elaborati correttamente in base al loro stato attuale, migliorando il controllo e l'efficienza all'interno del sistema ERP. Documentare chiaramente questa carta nel manuale del sistema aiuterà gli utenti a implementarla e gestirla in modo efficace, sfruttando la sua funzionalità per mantenere flussi di lavoro dei documenti fluidi e conformi. Questa carta è particolarmente utile nella gestione dei cicli di vita dei documenti e nel garantire che solo i documenti che soddisfano criteri specifici avanzino alle fasi successive dei processi aziendali.
