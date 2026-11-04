# Condizione Utente Assegnato

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda di flusso di lavoro gestisce l'esecuzione delle operazioni in base al fatto che un compito o un documento sia assegnato a un utente specifico o a un insieme di utenti. Utilizza la logica condizionale per attivare o impedire azioni specifiche, rendendola ideale per flussi di lavoro che richiedono gestione specifica degli utenti.

**Componenti della Scheda**

1. **Operatore**
* **Descrizione**: Definisce la condizione logica da applicare all'assegnazione dell'utente.
* **Opzioni**:
* **IS**: Attiva l'operazione se l'utente assegnato al documento o al compito corrisponde a un utente nell'elenco specificato.
* **IS NOT**: Attiva l'operazione se l'utente assegnato al documento o al compito non corrisponde a un utente nell'elenco specificato.
2. **Elenco Utenti**
* **Descrizione**: Un elenco o una selezione di utenti da confrontare con l'utente assegnato.
* **Dettaglio**: Questo elenco può includere uno o più utenti, consentendo alla scheda di gestire in modo efficace condizioni singole e multiple degli utenti. La selezione può essere effettuata tramite caselle di controllo, un menu a discesa multi-selezione o elementi UI simili.

**Funzionalità**

* **Identificazione Assegnazione Utente**: Identifica automaticamente l'utente o gli utenti assegnati a un compito o documento specifico all'interno del sistema ERP.
* **Valutazione Condizione**:
* Utilizzando l'operatore **IS**, la scheda verifica se l'utente assegnato è tra quelli elencati nell'Elenco Utenti.
* Utilizzando l'operatore **IS NOT**, la scheda garantisce che l'utente assegnato non sia tra quelli elencati.
* **Esecuzione Azione**:
* **Condizione Vera**: Se l'assegnazione dell'utente soddisfa la condizione (sia IS che IS NOT), vengono attivate azioni rilevanti, come notifiche, avvio di compiti, approvazioni o altri passaggi del flusso di lavoro.
* **Condizione Falsa**: Se la condizione non è soddisfatta, il documento o il compito potrebbero seguire percorsi diversi, o potrebbero essere specificate azioni alternative.

**Interazioni Utente**

* **Configurazione e Setup**: Gli utenti configurano la scheda selezionando un operatore e specificando gli utenti rilevanti dall'Elenco Utenti. La configurazione dovrebbe essere user-friendly e intuitiva per consentire selezioni da basi utenti potenzialmente ampie.
* **Monitoraggio e Reporting**: Il sistema ERP dovrebbe fornire funzionalità per monitorare e segnalare le operazioni attivate da questa scheda, offrendo approfondimenti sull'accuratezza dell'assegnazione e sull'efficienza del processo.
* **Gestione degli Errori e Notifiche**: Gli utenti dovrebbero avere opzioni per ricevere avvisi o notifiche in caso di problemi con le assegnazioni, come compiti non assegnati o errori nella selezione dell'utente.

#### Conclusione

La scheda di flusso di lavoro "Condizione Utente Assegnato" è uno strumento critico per gestire flussi di lavoro di documenti e compiti che dipendono dalle assegnazioni degli utenti. Consentendo condizioni basate sul fatto che un compito o un documento sia assegnato a utenti specifici, garantisce che i flussi di lavoro siano attivati solo da interazioni utente appropriate, migliorando sia la responsabilità che l'allineamento dei compiti all'interno dei team. Documentare chiaramente questa scheda aiuterà gli utenti a comprendere la sua importanza e ad integrarla efficacemente nei loro flussi di lavoro, garantendo operazioni fluide ed efficienti adattate ai ruoli e alle responsabilità degli utenti.
