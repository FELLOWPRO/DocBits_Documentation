# Condizione Utente Singolo Assegnato

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda di flusso di lavoro facilita le operazioni basate sull'assegnazione di un compito o documento a un singolo utente specifico. Utilizzando un approccio logico condizionale diretto, gestisce flussi di lavoro che richiedono il coinvolgimento mirato dell'utente, garantendo precisione nella gestione dei compiti basati sull'utente.

**Componenti della Scheda**

1. **Operatore**
* **Descrizione**: Specifica la logica da applicare all'assegnazione dell'utente.
* **Opzioni**:
* **IS**: Attiva l'operazione se l'utente assegnato al documento o al compito corrisponde all'utente specificato.
* **IS NOT**: Attiva l'operazione se l'utente assegnato non corrisponde all'utente specificato.
2. **Utente**
* **Descrizione**: Consente la selezione di un singolo utente rispetto al quale l'utente assegnato verrà confrontato.
* **Dettaglio**: Questo implica un semplice menu a discesa o campo di autocompletamento in cui è possibile selezionare un utente alla volta.

**Funzionalità**

* **Identificazione dell'Assegnazione Utente**: Identifica l'utente attualmente assegnato a un compito o documento specifico.
* **Valutazione della Condizione**:
* Per l'operatore **IS**, la scheda verifica se l'utente assegnato è lo stesso dell'utente selezionato.
* Per l'operatore **IS NOT**, verifica che l'utente assegnato sia diverso dall'utente selezionato.
* **Esecuzione dell'Azione**:
* **Condizione Vera**: Se l'assegnazione soddisfa la condizione impostata (IS o IS NOT), attiva azioni predefinite, che potrebbero includere il proseguimento con le approvazioni, l'avvio di ulteriori compiti, l'invio di notifiche o altri flussi di lavoro correlati.
* **Condizione Falsa**: Se la condizione non viene soddisfatta, il sistema può riorientare il compito, tenerlo in attesa per la revisione o attivare azioni predefinite alternative.

**Interazioni Utente**

* **Configurazione e Impostazione**: Gli utenti configurano la scheda scegliendo un operatore e selezionando un utente dal campo utente. Questa configurazione dovrebbe essere semplice, garantendo una facile selezione e configurazione dell'utente.
* **Monitoraggio e Reporting**: Offre strumenti per monitorare le prestazioni della scheda, come il tracciamento dei compiti attivati dalle assegnazioni specifiche degli utenti e i risultati di queste attivazioni.
* **Gestione degli Errori e Notifiche**: Fornisce meccanismi per avvisare gli utenti se i compiti sono assegnati in modo errato o se si verificano errori operativi dovuti a problemi di assegnazione.

#### Conclusione

La scheda di flusso di lavoro "Condizione Utente Singolo Assegnato" è essenziale per una gestione precisa e specifica dell'utente dei documenti e dei compiti all'interno di un sistema ERP. Semplifica i flussi di lavoro concentrandosi sulle assegnazioni individuali degli utenti, garantendo così che le azioni vengano eseguite solo quando appropriato, in base al ruolo e alle responsabilità dell'utente. Documentare chiaramente questa scheda aiuterà gli utenti a comprendere la sua applicazione, consentendo loro di implementarla e gestirla in modo efficace all'interno delle loro operazioni quotidiane. Questa documentazione garantisce che tutti gli utenti potenziali possano comprendere facilmente lo scopo della scheda e integrarla senza problemi nei loro flussi di lavoro.
