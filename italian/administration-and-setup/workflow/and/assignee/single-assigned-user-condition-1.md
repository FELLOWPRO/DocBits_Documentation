# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Scopo:**\
Questa scheda di workflow esegue operazioni in base al fatto che un'attività o un documento sia assegnato a un determinato gruppo. Utilizza una condizione semplice per attivare o impedire azioni in base all'assegnazione del gruppo.

**Componenti della scheda:**

1. **Operator**
   * **Descrizione:** Definisce la condizione logica da applicare all'assegnazione del gruppo.
   * **Opzioni:**
     * **IS:** Attiva l'operazione se il gruppo assegnato del documento o dell'attività corrisponde al gruppo specificato.
     * **IS NOT:** Attiva l'operazione se il gruppo assegnato del documento o dell'attività non corrisponde al gruppo specificato.
2. **Group**
   * **Descrizione:** Specifica il gruppo da confrontare con il gruppo assegnato.
   * **Dettaglio:** Questo campo ti consente di selezionare un singolo gruppo con cui confrontare l'assegnazione.

**Funzionalità:**

* **Identificazione dell'assegnazione del gruppo:** Identifica automaticamente il gruppo assegnato a una determinata attività o documento.
* **Valutazione della condizione:**
  * Con l'operatore **IS**, la scheda verifica se il gruppo assegnato corrisponde al gruppo specificato.
  * Con l'operatore **IS NOT**, la scheda garantisce che il gruppo assegnato non corrisponda al gruppo specificato.
* **Esecuzione dell'azione:**
  * **Condizione vera:** Se l'assegnazione del gruppo soddisfa la condizione (sia **IS** che **IS NOT**), vengono attivate le azioni pertinenti, come notifiche, avvio di attività, approvazioni o altri passaggi del workflow.
  * **Condizione falsa:** Se la condizione non è soddisfatta, il documento o l'attività possono seguire un instradamento diverso, oppure possono essere specificate azioni alternative.

**Interazioni dell'utente:**

* **Configurazione e impostazione:**\
  Gli utenti configurano la scheda selezionando un operatore e specificando il gruppo pertinente. La configurazione dovrebbe essere semplice e intuitiva.
* **Monitoraggio e reporting:**\
  Il sistema dovrebbe fornire funzionalità per monitorare e generare report sulle operazioni attivate da questa scheda, offrendo informazioni sull'accuratezza delle assegnazioni e sull'efficienza del processo.
* **Gestione degli errori e notifiche:**\
  Gli utenti dovrebbero avere la possibilità di ricevere avvisi o notifiche in caso di problemi con le assegnazioni, come attività non assegnate o errori nella selezione dei gruppi.

**Conclusione:**\
La scheda di workflow "Assigned Group Condition" è essenziale per gestire i workflow di documenti e attività basati sulle assegnazioni di gruppo. Consentendo condizioni basate sul fatto che un'attività o un documento sia assegnato a un gruppo specifico, garantisce che i workflow vengano attivati solo dalle interazioni di gruppo appropriate, migliorando la gestione delle attività e l'efficienza del workflow.
