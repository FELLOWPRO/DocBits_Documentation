# Elenco delle Condizioni dello Stato del Documento

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda è progettata per controllare le azioni del flusso di lavoro in base allo stato attuale di un documento, utilizzando la logica condizionale per attivare o limitare determinati processi. Garantisce che i documenti procedano solo attraverso i flussi di lavoro quando soddisfano i criteri di stato predefiniti.

**Componenti della Scheda**

1. **Operatore**
* **Descrizione**: Determina come lo stato del documento verrà valutato rispetto a una condizione specificata.
* **Opzioni**:
* **è**: Attiva le azioni associate se lo stato attuale del documento corrisponde a uno degli stati specificati.
* **non è**: Attiva le azioni se lo stato del documento non corrisponde a nessuno degli stati specificati.
2. **Stato ( Elenco )**&#x20;
* **Descrizione**: Elenca gli stati specifici rispetto ai quali lo stato attuale del documento verrà confrontato.
* **Esempi**: "Errore", "Errore di Esportazione", "Pronto in Validazione", "Pronto in Revisione", "Approvazione in Sospeso", "Seconda Approvazione in Sospeso". Questi rappresentano diverse fasi o condizioni in cui un documento potrebbe trovarsi all'interno di un processo di flusso di lavoro.

**Funzionalità**

* **Identificazione dello Stato**: Identifica automaticamente lo stato attuale di un documento mentre si sposta attraverso il flusso di lavoro del sistema ERP.
* **Valutazione della Condizione**: Applica l'operatore scelto (è o non è) allo stato del documento in confronto agli stati elencati:
* Se **è**, controlla se lo stato del documento corrisponde a uno degli stati nell'elenco.
* Se **non è**, controlla se lo stato del documento non appare nell'elenco.
* **Esecuzione dell'Azione**: A seconda dell'esito della valutazione della condizione:
* **Vero**: Esegue azioni predefinite o flussi di lavoro se la condizione è soddisfatta.
* **Falso**: Salta o attiva flussi di lavoro alternativi se la condizione non è soddisfatta.
* **Integrazione del Flusso di Lavoro**: Si integra senza problemi con altri componenti del flusso di lavoro, garantendo che la gestione dei documenti sia coordinata in tutto il sistema.

**Interazioni dell'Utente**

* **Configurazione e Impostazione**: Gli utenti configurano la scheda selezionando l'operatore e specificando gli stati rilevanti. Questa configurazione può coinvolgere semplici menu a discesa o caselle di controllo per la selezione di stati e operatori.
* **Monitoraggio e Gestione**: Gli utenti possono monitorare l'attività della scheda tramite un cruscotto, che fornisce informazioni sulle condizioni di stato monitorate e sulle azioni intraprese in base a tali condizioni.
* **Gestione degli Errori e Avvisi**: Supporta l'impostazione di avvisi per i fallimenti dei processi o per le discrepanze negli stati attesi dei documenti, consentendo risposte rapide ai problemi operativi.

#### Conclusione

La scheda di flusso di lavoro "Condizione dello Stato del Documento" è fondamentale per garantire che i documenti vengano elaborati correttamente in base al loro stato attuale, migliorando il controllo e l'efficienza all'interno del sistema ERP. Documentare chiaramente questa scheda nel manuale del sistema aiuterà gli utenti a implementarla e gestirla in modo efficace, sfruttando la sua funzionalità per mantenere flussi di lavoro documentali regolari e conformi. Questa scheda è particolarmente utile nella gestione dei cicli di vita dei documenti e nell'assicurare che solo i documenti che soddisfano criteri specifici avanzino alle fasi successive dei processi aziendali.
