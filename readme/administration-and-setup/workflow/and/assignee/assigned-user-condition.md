# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Scopo**

Questa scheda di workflow gestisce l'esecuzione di operazioni in base al fatto che un'attività o un documento sia assegnato a un determinato utente o insieme di utenti. Impiega una logica condizionale per attivare o impedire azioni specifiche, rendendola ideale per i workflow che richiedono una gestione specifica per utente.

**Componenti della scheda**

1. **Operator**
   * **Descrizione**: Definisce la condizione logica da applicare all'assegnazione dell'utente.
   * **Opzioni**:
     * **IS**: Attiva l'operazione se l'utente assegnato del documento o dell'attività corrisponde a un utente qualsiasi nell'elenco specificato.
     * **IS NOT**: Attiva l'operazione se l'utente assegnato del documento o dell'attività non corrisponde a nessun utente nell'elenco specificato.
2. **User List**
   * **Descrizione**: Un elenco o una selezione di utenti da confrontare con l'utente assegnato.
   * **Dettaglio**: Questo elenco può includere uno o più utenti, consentendo alla scheda di gestire efficacemente sia condizioni di utente singolo che multiplo. La selezione può avvenire tramite caselle di controllo, un menu a discesa a selezione multipla o elementi UI simili.

**Funzionalità**

* **Identificazione dell'assegnazione dell'utente**: Identifica automaticamente l'utente o gli utenti assegnati a una determinata attività o documento all'interno del sistema ERP.
* **Valutazione della condizione**:
  * Con l'operatore **IS**, la scheda verifica se l'utente assegnato è tra quelli elencati nella User List.
  * Con l'operatore **IS NOT**, la scheda garantisce che l'utente assegnato non sia tra quelli elencati.
* **Esecuzione dell'azione**:
  * **Condizione vera**: Se l'assegnazione dell'utente soddisfa la condizione (IS o IS NOT), vengono attivate le azioni pertinenti, come notifiche, avvio di attività, approvazioni o altri passaggi del workflow.
  * **Condizione falsa**: Se la condizione non è soddisfatta, il workflow non proseguirà.

**Interazioni dell'utente**

* **Configurazione e impostazione**: Gli utenti configurano la scheda selezionando un operatore e specificando gli utenti pertinenti dalla User List. La configurazione dovrebbe essere semplice e intuitiva per gestire selezioni da basi di utenti potenzialmente ampie.
* **Monitoraggio e reporting**: Il sistema ERP dovrebbe fornire funzionalità per monitorare e generare report sulle operazioni attivate da questa scheda, offrendo informazioni sull'accuratezza delle assegnazioni e sull'efficienza del processo.
* **Gestione degli errori e notifiche**: Gli utenti dovrebbero avere la possibilità di ricevere avvisi o notifiche in caso di problemi con le assegnazioni, come attività non assegnate o errori nella selezione degli utenti.

#### Conclusione

La scheda di workflow "Assigned User Condition" è uno strumento fondamentale per gestire i workflow di documenti e attività che dipendono dalle assegnazioni agli utenti. Consentendo condizioni basate sul fatto che un'attività o un documento sia assegnato a utenti specifici, garantisce che i workflow vengano attivati solo da interazioni utente appropriate, migliorando sia la responsabilità che l'allineamento delle attività all'interno dei team. Documentare chiaramente questa scheda aiuterà gli utenti a comprenderne l'importanza e a integrarla efficacemente nei loro workflow, garantendo operazioni fluide ed efficienti adattate ai ruoli e alle responsabilità degli utenti.
