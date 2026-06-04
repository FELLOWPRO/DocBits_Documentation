# Promised delivery date for line items in table with promised delivery date

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Scopo:

Questa scheda di workflow è progettata per validare la **data di consegna promessa delle righe articolo** rispetto alla **data di consegna promessa sull'ordine d'acquisto**, utilizzando operatori di confronto e regole di tolleranza configurabili. Consente ai workflow di rilevare automaticamente date di consegna conformi, anticipate o in ritardo e di reagire di conseguenza.

## Componenti della scheda:

1. **Operator**
   * **Descrizione:**\
     Definisce come la data di consegna promessa della riga articolo viene confrontata con la data di consegna promessa dell'ordine d'acquisto.
   * **Opzioni:**
     * **Equals (=):** La data della riga articolo deve rientrare nella finestra di tolleranza.
     * **Not Equals (≠):** La data della riga articolo deve ricadere al di fuori della finestra di tolleranza.
     * **Greater Than (>):** La data della riga articolo deve essere successiva alla finestra di tolleranza.
     * **Greater or Equals (≥):** La data della riga articolo deve essere all'inizio della finestra di tolleranza o successiva.
     * **Lesser Than (<):** La data della riga articolo deve essere precedente alla finestra di tolleranza.
     * **Lesser or Equals (≤):** La data della riga articolo deve essere alla fine della finestra di tolleranza o precedente.<br>
2. **Tolerance Days**
   * **Descrizione:**\
     Specifica il numero di giorni utilizzati per calcolare la finestra di tolleranza accettabile attorno alla data di consegna promessa dell'ordine d'acquisto.
   * **Dettaglio:**\
     Questo valore è un intero e definisce quanti giorni prima e dopo la data dell'ordine d'acquisto vengono considerati durante la validazione.<br>
3. **Allowed Tolerance Days**
   * **Descrizione:**\
     Definisce quali giorni della settimana vengono conteggiati nel calcolo dei giorni di tolleranza.
   * **Dettaglio:**\
     Gli utenti possono selezionare giorni della settimana specifici (ad esempio, da lunedì a venerdì). Solo i giorni selezionati vengono inclusi nel calcolo della finestra di tolleranza.

### Funzionalità:

* **Valutazione della condizione:** Il sistema calcola una finestra di tolleranza attorno alla data di consegna promessa dell'ordine d'acquisto in base ai **Tolerance Days** e agli **Allowed Tolerance Days** configurati.\
  La data di consegna promessa di ciascuna riga articolo viene quindi confrontata con questa finestra utilizzando l'operatore selezionato.
* Esecuzione dell'azione:
  * **Condizione vera:** Se la differenza tra le date di consegna rientra nell'intervallo di tolleranza e soddisfa la condizione impostata dall'operatore, il workflow prosegue.
  * **Condizione falsa:** Se la condizione non è soddisfatta, il workflow non continuerà.

### Configurazione e impostazione:

* Seleziona l'operatore di confronto appropriato.
* Inserisci il numero di giorni di tolleranza.
* Scegli quali giorni della settimana devono essere conteggiati come giorni di tolleranza.

### Conclusione:

La scheda di workflow **Compare with Purchase Order – Promised Delivery Date for Line Items** offre un modo flessibile per applicare le regole sulle date di consegna. Combinando gli operatori con una gestione della tolleranza basata sui giorni della settimana, consente una validazione precisa degli impegni di consegna riducendo al contempo i controlli manuali e le eccezioni.
