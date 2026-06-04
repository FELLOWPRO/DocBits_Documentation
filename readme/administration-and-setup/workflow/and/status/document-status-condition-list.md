# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Scopo**

Questa scheda è progettata per controllare le azioni del workflow in base allo stato corrente di un documento, utilizzando una logica condizionale per attivare o limitare determinati processi. Garantisce che i documenti procedano attraverso i workflow solo quando soddisfano criteri di stato predefiniti.

**Componenti della scheda**

1. **Operator**
   * **Descrizione**: Determina come lo stato del documento verrà valutato rispetto a una condizione specificata.
   * **Opzioni**:
     * **is**: Attiva le azioni associate se lo stato corrente del documento corrisponde a uno degli stati specificati.
     * **is not**: Attiva le azioni se lo stato del documento non corrisponde a nessuno degli stati specificati.
2. **Status ( List )**
   * **Descrizione**: Elenca gli stati specifici con cui verrà confrontato lo stato corrente del documento.
   * **Esempi**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Questi rappresentano le diverse fasi o condizioni in cui un documento potrebbe trovarsi all'interno di un processo di workflow.

**Funzionalità**

* **Identificazione dello stato**: Identifica automaticamente lo stato corrente di un documento mentre attraversa il workflow del sistema ERP.
* **Valutazione della condizione**: Applica l'operatore scelto (is o is not) allo stato del documento confrontandolo con gli stati elencati:
  * Con **is**, verifica se lo stato del documento corrisponde a uno stato qualsiasi nell'elenco.
  * Con **is not**, verifica se lo stato del documento non compare nell'elenco.
* **Esecuzione dell'azione**: A seconda dell'esito della valutazione della condizione:
  * **True**: Esegue azioni o workflow predefiniti se la condizione è soddisfatta.
  * **False**: Salta o attiva workflow alternativi se la condizione non è soddisfatta.
* **Integrazione nel workflow**: Si integra perfettamente con gli altri componenti del workflow, garantendo che la gestione dei documenti sia coordinata in tutto il sistema.

**Interazioni dell'utente**

* **Configurazione e impostazione**: Gli utenti configurano la scheda selezionando l'operatore e specificando gli stati pertinenti. Questa configurazione può comportare semplici menu a discesa o caselle di controllo per selezionare stati e operatori.
* **Monitoraggio e gestione**: Gli utenti possono tracciare l'attività della scheda tramite una dashboard, che fornisce informazioni sulle condizioni di stato monitorate e sulle azioni intraprese in base a tali condizioni.
* **Gestione degli errori e avvisi**: Supporta la configurazione di avvisi per i fallimenti di processo o le discrepanze negli stati attesi dei documenti, consentendo risposte rapide ai problemi operativi.

#### Conclusione

La scheda di workflow "Document Status Condition" è fondamentale per garantire che i documenti vengano elaborati correttamente in base al loro stato corrente, migliorando il controllo e l'efficienza all'interno del sistema ERP. Documentare chiaramente questa scheda nel manuale del sistema aiuterà gli utenti a implementarla e gestirla efficacemente, sfruttandone la funzionalità per mantenere workflow documentali fluidi e conformi. Questa scheda è particolarmente utile per gestire i cicli di vita dei documenti e garantire che solo i documenti che soddisfano criteri specifici avanzino alle fasi successive dei processi aziendali.
