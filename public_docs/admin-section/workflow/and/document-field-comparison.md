# Confronto dei Campi del Documento

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda di flusso è progettata per confrontare automaticamente i valori di due campi specificati all'interno di un documento in base a un operatore definito. Viene utilizzata per garantire l'integrità dei dati e assicurare che i dati del documento siano conformi alle regole aziendali o alle condizioni.

**Componenti della Scheda**

1. **Nomi dei Campi**
* **Descrizione**: Specifica i nomi dei due campi all'interno del documento che verranno confrontati.
* **Dettaglio**: Gli utenti devono inserire i nomi esatti dei campi come appaiono nel sistema. Questi campi possono essere di qualsiasi tipo di dati che supporta il confronto, come campi numerici, di data o di testo.
2. **Operatore**
* **Descrizione**: L'operatore di confronto utilizzato per valutare la relazione tra i valori dei due campi.
* **Opzioni**:
* **Uguale (==)**: Controlla se il valore del primo campo è uguale al valore del secondo campo.
* **Non Uguale (!=)**: Controlla se il valore del primo campo non è uguale al valore del secondo campo.
* **Maggiore Di (>)**: Controlla se il valore del primo campo è maggiore del valore del secondo campo.
* **Maggiore Di o Uguale (>=)**: Controlla se il valore del primo campo è maggiore o uguale al valore del secondo campo.
* **Minore Di (<)**: Controlla se il valore del primo campo è minore del valore del secondo campo.
* **Minore Di o Uguale (<=)**: Controlla se il valore del primo campo è minore o uguale al valore del secondo campo.

**Funzionalità**

* **Selezione dei Campi**: Gli utenti inseriscono o selezionano i nomi dei due campi da confrontare. Questo viene tipicamente fatto tramite un modulo o un menu a discesa all'interno della configurazione della scheda.
* **Selezione dell'Operatore**: Gli utenti scelgono un operatore da un elenco di opzioni disponibili che definiscono come i campi dovrebbero essere confrontati.
* **Esecuzione del Confronto**:
* Il sistema legge i valori dai campi specificati e applica l'operatore selezionato per valutare la relazione tra essi.
* In base al risultato del confronto (vero o falso), potrebbero essere attivate azioni successive. Ad esempio, se un confronto fallisce, il sistema potrebbe contrassegnare il documento per la revisione, bloccare ulteriori elaborazioni o notificare le parti responsabili.

**Interazioni degli Utenti**

* **Configurazione e Impostazione**: Gli utenti configurano il confronto inserendo i nomi dei campi e selezionando un operatore. Questa configurazione dovrebbe essere semplice e guidata, eventualmente con testo di aiuto o esempi.
* **Monitoraggio e Reporting**: Il sistema può fornire feedback sui risultati dei confronti, come registrare tutti i confronti effettuati, i loro esiti e le azioni intraprese in risposta ai risultati del confronto.
* **Gestione degli Errori e Notifiche**: Gli utenti ricevono avvisi se il confronto non può essere eseguito (ad esempio, se uno dei campi non viene trovato nel documento o non è in un formato confrontabile).

#### Conclusione

La scheda di flusso "Confronto dei Campi del Documento" è fondamentale per mantenere l'accuratezza e la coerenza dei dati tra i documenti in un sistema ERP. Aiuta ad automatizzare controlli che altrimenti sarebbero manuali, soggetti a errori e dispendiosi in termini di tempo, migliorando l'efficienza e l'affidabilità nell'elaborazione dei documenti. Documentare chiaramente questa scheda nel manuale del sistema ERP assisterà gli utenti nell'utilizzare efficacemente questa funzionalità, garantendo che i dati tra i documenti rimangano consistenti e conformi alle regole aziendali.
