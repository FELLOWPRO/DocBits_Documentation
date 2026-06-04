# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Scopo:**

Questa scheda di workflow esegue operazioni in base al fatto che un'attività o un documento sia assegnato a un determinato gruppo o insieme di gruppi. Utilizza una logica condizionale per attivare o impedire azioni specifiche a seconda dell'assegnazione del gruppo, rendendola ideale per i workflow che richiedono una gestione specifica per gruppo.

**Componenti della scheda:**

1. **Operator**
   * **Descrizione:** Definisce la condizione logica da applicare all'assegnazione del gruppo.
   * **Opzioni:**
     * **IS:** Attiva l'operazione se il gruppo assegnato del documento o dell'attività corrisponde a uno dei gruppi nell'elenco specificato.
     * **IS NOT:** Attiva l'operazione se il gruppo assegnato del documento o dell'attività non corrisponde a nessuno dei gruppi nell'elenco specificato.
2. **Groups List**
   * **Descrizione:** Un elenco o una selezione di gruppi da confrontare con il gruppo assegnato.
   * **Dettaglio:** Questo elenco può includere uno o più gruppi, consentendo alla scheda di gestire efficacemente sia condizioni di gruppo singolo che multiplo.

**Funzionalità:**

* **Identificazione dell'assegnazione del gruppo:** Identifica automaticamente il gruppo o i gruppi assegnati a una determinata attività o documento all'interno del sistema.
* **Valutazione della condizione:**
  * Con l'operatore **IS**, la scheda verifica se il gruppo assegnato è uno dei gruppi elencati nella Groups List.
  * Con l'operatore **IS NOT**, la scheda garantisce che il gruppo assegnato non faccia parte dei gruppi elencati.
* **Esecuzione dell'azione:**
  * **Condizione vera:** Se l'assegnazione del gruppo soddisfa la condizione (sia **IS** che **IS NOT**), vengono attivate le azioni pertinenti, come notifiche, avvio di attività, approvazioni o altri passaggi del workflow.
  * **Condizione falsa:** Se la condizione non è soddisfatta, il workflow non proseguirà.

**Interazioni dell'utente:**

* **Configurazione e impostazione:** Gli utenti configurano la scheda selezionando un operatore e specificando i gruppi pertinenti dalla Groups List. La configurazione dovrebbe essere semplice e intuitiva per gestire selezioni da basi di gruppi potenzialmente ampie.
* **Monitoraggio e reporting:**\
  Il sistema dovrebbe fornire funzionalità per monitorare e generare report sulle operazioni attivate da questa scheda, offrendo informazioni sull'accuratezza delle assegnazioni e sull'efficienza del processo.
* **Gestione degli errori e notifiche:**\
  Gli utenti dovrebbero avere la possibilità di ricevere avvisi o notifiche in caso di problemi con le assegnazioni, come attività non assegnate o errori nella selezione dei gruppi.

**Conclusione:**\
La scheda di workflow "Assigned Group Condition" è essenziale per gestire i workflow di documenti e attività che dipendono dalle assegnazioni di gruppo. Consentendo condizioni basate sul fatto che un'attività o un documento sia assegnato a gruppi specifici, garantisce che i workflow vengano attivati solo da interazioni di gruppo appropriate, migliorando la responsabilità e la gestione delle attività tra i team.
