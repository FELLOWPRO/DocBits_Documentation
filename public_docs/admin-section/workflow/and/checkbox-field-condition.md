# Condizione del Campo Checkbox

<figure><img src="../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Scopo**

Questa scheda di flusso di lavoro è progettata per automatizzare azioni in base allo stato (selezionato o deselezionato) di una casella di controllo all'interno del tuo sistema ERP. Valutando la condizione della casella di controllo, facilita l'attivazione di processi specifici o l'applicazione di determinate regole all'interno dell'applicazione.

**Componenti della Scheda**

1. **Nome del Campo**
* **Descrizione**: Specifica il nome del campo della casella di controllo che verrà valutato.
* **Dettaglio**: Questo dovrebbe corrispondere all'etichetta esatta del campo o all'identificatore utilizzato nel sistema. Determina quale stato della casella di controllo viene monitorato.
2. **Booleano**
* **Descrizione**: Definisce la condizione che attiva il flusso di lavoro.
* **Opzioni**:
* **True**: Il flusso di lavoro si attiva se la casella di controllo è selezionata.
* **False**: Il flusso di lavoro si attiva se la casella di controllo non è selezionata.

**Funzionalità**

* **Rilevamento dello Stato**: La scheda monitora continuamente lo stato del campo della casella di controllo specificato.
* **Valutazione della Condizione**:
* Il sistema verifica se la casella di controllo si trova nello stato (selezionato o deselezionato) specificato dalla condizione Booleana.
* **Esecuzione dell'Azione**:
* **Condizione True**: Se lo stato della casella di controllo corrisponde alla condizione Booleana specificata (vero per selezionato o falso per deselezionato), il sistema avvia le azioni associate. Queste potrebbero includere l'abilitazione o disabilitazione dei campi del modulo, l'attivazione di notifiche, l'avvio di flussi di lavoro o l'aggiornamento dei record.
* **Condizione False**: Se lo stato della casella di controllo non corrisponde alla condizione, potrebbero essere adottate azioni alternative o nessuna azione, a seconda della configurazione del flusso di lavoro.

**Interazioni con l'Utente**

* **Configurazione e Impostazione**: Gli utenti configurano la scheda selezionando il campo della casella di controllo da un elenco di campi disponibili e impostando la condizione Booleana. Questo processo di configurazione dovrebbe essere intuitivo, coinvolgendo tipicamente un semplice menu a discesa per la selezione del campo e un interruttore per la condizione Booleana.
* **Monitoraggio e Reporting**: Fornisce funzionalità agli utenti per monitorare lo stato di questa condizione, eventualmente attraverso un cruscotto che mostra aggiornamenti in tempo reale su quali condizioni sono attive o attivate.
* **Gestione degli Errori e Notifiche**: Garantisce che gli utenti siano avvisati in caso di discrepanze o errori nel processo di controllo della condizione, come fallimenti del sistema nel leggere lo stato della casella di controllo.

#### Conclusione

La scheda di flusso di lavoro "Condizione del Campo Checkbox" è uno strumento fondamentale per gestire moduli dinamici e documenti all'interno di un sistema ERP, dove gli input degli utenti possono determinare processi dati successivi. Automatizzando azioni in base allo stato di una casella di controllo, questa scheda migliora l'efficienza del flusso di lavoro e garantisce che i comportamenti del sistema siano allineati agli input degli utenti. Una documentazione chiara di questa scheda aiuterà gli utenti a implementarla efficacemente nelle loro operazioni, consentendo un migliore controllo sui comportamenti dei moduli e sulle automazioni dei processi.
