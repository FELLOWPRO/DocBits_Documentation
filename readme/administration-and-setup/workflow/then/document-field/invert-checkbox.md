# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per invertire lo stato corrente di un campo casella di controllo. Se la casella di controllo è selezionata (true), verrà deselezionata (false), e viceversa. L'inversione avviene in base alle condizioni impostate nelle sezioni **"Where"** e **"And"**. Questa scheda aiuta ad automatizzare i workflow in cui una condizione richiede di invertire una casella di controllo in base a criteri specifici.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione**: Specifica il campo casella di controllo da invertire.&#x20;
   * **Dettaglio**: Il campo casella di controllo selezionato avrà il proprio stato invertito da true a false o da false a true in base al suo stato corrente.

## **Funzionalità:**

* **Valutazione della condizione**: Il sistema valuta le condizioni definite nelle sezioni **"Where"** e **"And"**:
  * Se **entrambe le condizioni sono vere**, l'azione della sezione **"Then"** verrà eseguita, il che in questo caso significa che il campo casella di controllo verrà invertito.
  * Se **una delle condizioni è falsa**, la scheda non verrà eseguita e non verrà apportata alcuna modifica al campo casella di controllo.
* **Esecuzione dell'azione**: Se le condizioni nelle sezioni **"Where"** e **"And"** risultano vere, lo stato del campo casella di controllo verrà invertito:
  * Se la casella di controllo è selezionata (true), verrà deselezionata (false).
  * Se la casella di controllo è deselezionata (false), verrà selezionata (true).

## **Configurazione e impostazione:**

Per configurare questa scheda, gli utenti devono:

1. **Selezionare il campo casella di controllo** (Field Name) che verrà invertito. I campi casella di controllo disponibili nel documento sono elencati per la selezione.
2. Il campo casella di controllo verrà invertito solo se le condizioni in entrambe le sezioni **"Where"** e **"And"** sono vere.

## **Conclusione:**

La scheda di workflow **"Invert checkbox \[Field Name]"** offre uno strumento di automazione semplice ma potente per invertire i valori delle caselle di controllo in base a condizioni specifiche. Riducendo la necessità di aggiustamenti manuali delle caselle di controllo, questa scheda migliora l'efficienza nell'elaborazione dei documenti e garantisce coerenza tra i workflow.
