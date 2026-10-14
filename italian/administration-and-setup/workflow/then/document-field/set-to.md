# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per impostare automaticamente un campo specificato del documento su un valore testuale predefinito in base alle condizioni definite nelle sezioni **"Where"** e **"And"**. Consente agli utenti di semplificare l'inserimento dei dati garantendo che i campi vengano popolati con valori coerenti quando determinati criteri sono soddisfatti.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione**: Specifica il campo che verrà aggiornato con il valore testuale.&#x20;
   * **Dettaglio**: Il campo selezionato verrà aggiornato con il valore testuale specificato se le condizioni nelle sezioni **"Where"** e **"And"** sono soddisfatte.
2. **Text**
   * **Descrizione**: Definisce il valore testuale che verrà impostato nel campo di destinazione quando le condizioni risultano vere.
   * **Dettaglio**: Può essere un messaggio personalizzato, uno stato o un valore predefinito che l'utente desidera scrivere nel campo. Il testo dovrebbe essere allineato al formato di input previsto del campo (es. alfanumerico, data o altri tipi di informazioni testuali).

## **Funzionalità:**

* **Valutazione della condizione**: Il sistema valuta le condizioni nelle sezioni **"Where"** e **"And"**:
  * Se **entrambe le condizioni sono vere**, verranno eseguite le azioni definite nella sezione **"Then"**. Nello specifico, il campo di destinazione (Field Name) verrà popolato con il testo specificato.
  * Se **la sezione "Where" o la sezione "And" è falsa**, non viene intrapresa alcuna azione e il campo rimane invariato. Le azioni della sezione **Then** vengono completamente saltate se una delle condizioni è falsa.
* **Esecuzione dell'azione**: Se entrambe le condizioni nelle sezioni **"Where"** e **"And"** sono soddisfatte, il sistema popola automaticamente il campo specificato con il valore testuale scelto. Se le condizioni non sono soddisfatte, non viene apportata alcuna modifica al campo.

## **Configurazione e impostazione:**

Per configurare questa scheda:

1. **Seleziona il campo** (Field Name) che verrà aggiornato con il valore testuale. I campi disponibili nel documento sono elencati per la selezione.
2. **Specifica il valore testuale** che verrà scritto nel campo di destinazione quando le condizioni sono vere.
3. L'azione verrà eseguita solo se entrambe le condizioni nelle sezioni **"Where"** e **"And"** risultano vere.

## **Conclusione:**

La scheda di workflow **"Set Field to Text"** offre un modo diretto per automatizzare il popolamento di valori testuali in campi specifici del documento in base a condizioni predefinite. Ciò riduce l'inserimento manuale dei dati e garantisce coerenza nell'elaborazione dei documenti, rendendola uno strumento utile per automatizzare i workflow e migliorare l'efficienza.
