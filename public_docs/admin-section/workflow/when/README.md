# Quando

<figure><img src="../../../.gitbook/assets/docbits_workflow_4.png" alt="DocBits Flusso di lavoro 4"><figcaption></figcaption></figure>

#### Comprensione del "Quando" nelle Configurazioni del Flusso di Lavoro

**Scopo del "Quando"**

* La sezione "Quando" in una configurazione del flusso di lavoro definisce le condizioni di attivazione che avviano una particolare azione del flusso di lavoro. Queste condizioni si basano su criteri specificati relativi agli attributi del documento o alle attività dell'utente all'interno del sistema ERP.

**Come Funziona**

* Nella tua interfaccia, "Quando" sembra essere un punto di partenza in cui gli utenti possono selezionare diverse schede di attivazione. Ogni scheda specifica le condizioni in base alle quali le azioni successive (definite in un'altra sezione della configurazione del flusso di lavoro, probabilmente etichettata come "Azione") verranno eseguite.

**Schede di Condizioni del Tipo di Documento**

* Le schede visualizzate nello screenshot sono variazioni delle condizioni del "Tipo di Documento", che vengono utilizzate per attivare flussi di lavoro in base al tipo di documento in fase di elaborazione. Ecco una panoramica di ciascun tipo di scheda di condizioni mostrata:
* **Tipo di documento (Operatore) uno di (Tipo)**: Questa scheda attiva un'azione quando il tipo di un documento corrisponde a uno dei tipi specificati in un elenco. L'operatore potrebbe includere opzioni come "è" o "non è", consentendo condizioni inclusive o esclusive.
* **Tipo di documento (Operatore) (Tipo)**: Questa variante più semplice si attiva in base a una singola condizione del tipo di documento. Tipicamente verificherebbe se il tipo di documento "è" o "non è" un tipo specifico, senza la possibilità di selezionare tra tipi multipli.

#### Configurazione di una Scheda di Attivazione "Quando"

1. **Selezione del Tipo di Condizione**: Gli utenti iniziano selezionando un tipo di condizione rilevante per il flusso di lavoro che desiderano automatizzare. In questo caso, i tipi di documento sono il focus.
2. **Definizione dell'Operatore**: Gli utenti devono decidere l'operatore logico, come "è" o "non è", che stabilisce la base per confrontare i tipi di documento effettivi con le condizioni definite.
3. **Specificare i Tipi di Documento**: A seconda della scheda, gli utenti possono selezionare uno o più tipi di documento che attiveranno il flusso di lavoro quando i documenti di quei tipi vengono elaborati.
4. **Finalizzazione dell'Attivazione**: Una volta impostata la condizione, diventa la base per attivare azioni specifiche definite nel flusso di lavoro. Se un documento soddisfa la condizione impostata, le azioni definite verranno avviate automaticamente.

#### Applicazione Pratica

Nella pratica, queste schede di attivazione sono cruciali per automatizzare processi come approvazioni, notifiche o qualsiasi procedura che dipende dal tipo di documento in fase di gestione. Ad esempio, se un tipo di documento "è" una "Fattura," e corrisponde alle condizioni impostate nella scheda "Quando," il flusso di lavoro potrebbe instradare automaticamente il documento per l'elaborazione del pagamento.

Questa configurazione garantisce che i flussi di lavoro siano non solo efficienti, ma anche adattati alle specifiche esigenze operative dell'organizzazione, riducendo la supervisione manuale e accelerando i processi di gestione dei documenti.

In sintesi, la parte "Quando" della configurazione del tuo flusso di lavoro riguarda la preparazione per azioni automatizzate basate su condizioni specifiche e predefinite. È uno strumento potente per garantire che il tuo sistema ERP reagisca dinamicamente alle esigenze dell'azienda, migliorando sia la produttività che l'accuratezza nella gestione dei documenti.
