# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

Questa scheda DocBits è progettata per confrontare un campo specifico dei dati dell'ordine — come quantità, sconto o prezzo unitario — tra una conferma d'ordine e un ordine d'acquisto. Consentendo un confronto mirato di un campo alla volta, garantisce precisione nella validazione dei punti dati chiave, mantenendo l'accuratezza dell'ordine. La **Versione 4** espande questa funzionalità consentendo confronti tra entità diverse come l'ordine d'acquisto, le quantità ricevute e il documento stesso, aggiungendo maggiore flessibilità e controllo al workflow.

## Componenti della scheda:

1. **Any/All**&#x20;
   * **Descrizione:** Determina se la condizione si applica ad alcune o a tutte le righe della conferma d'ordine.\
     **Opzioni:**
     * **Any**: Il confronto si attiva se il valore del campo selezionato in una riga qualsiasi della conferma d'ordine corrisponde al valore corrispondente nell'ordine d'acquisto.
     * **All**: Il confronto si attiva solo se il valore del campo selezionato in tutte le righe della conferma d'ordine corrisponde al valore corrispondente nell'ordine d'acquisto.
2. **Order Data Field**
   * **Descrizione**: Specifica il campo dati da confrontare tra la conferma d'ordine e l'ordine d'acquisto.
   * **Dettaglio**: Gli utenti possono selezionare uno dei seguenti campi per il confronto:
     * **Quantity**: Confronta la quantità ordinata con la quantità confermata.
     * **Discount**: Verifica che lo sconto nella conferma corrisponda all'ordine d'acquisto.
     * **Unit Price**: Garantisce che il prezzo unitario nella conferma sia allineato all'ordine d'acquisto.
3. **Operator**
   * **Descrizione**: Definisce la condizione applicata al confronto del campo dati selezionato.
   * **Opzioni**:
     * **Equals (=)**: Conferma che il valore corrisponda all'ordine d'acquisto.
     * **Not Equals (≠)**: Garantisce che il valore sia diverso dall'ordine d'acquisto.
     * **Greater Than (>)**: Verifica che il valore superi quello dell'ordine d'acquisto.
     * **Greater or Equals (≥)**: Conferma che il valore sia uguale o superiore a quello dell'ordine d'acquisto.
     * **Less Than (<)**: Verifica che il valore sia inferiore a quello dell'ordine d'acquisto.
     * **Less or Equals (≤)**: Conferma che il valore sia inferiore o uguale a quello dell'ordine d'acquisto.

## **Componenti aggiuntivi nella Versione 4**:

* **Comparison Type**: Seleziona le entità da confrontare. Le opzioni includono:
  * **Purchase Order to Document**: Confronta i dati dell'ordine d'acquisto con il documento correlato.
  * **Received to Document**: Confronta i dati ricevuti (es. quantità ricevute) con il documento.
  * **Purchase Order to Received**: Confronta i dati dell'ordine d'acquisto con le quantità ricevute.

## Funzionalità:

* **Confronto dei campi**: Il sistema confronta il campo dati dell'ordine selezionato (Unit Price, Discount o Quantity) della conferma d'ordine con il valore corrispondente nell'ordine d'acquisto.
* **Esecuzione dell'azione**: In base al risultato del confronto e alla condizione dell'operatore, la scheda può attivare azioni di follow-up, come notifiche o avvisi.

## Scenario di esempio:

* Una conferma d'ordine specifica un **prezzo unitario** di $50, mentre l'ordine d'acquisto indica $45. Utilizzando l'operatore "Greater Than", la scheda segnala la discrepanza, consentendo al team di approvvigionamento di gestirla prima dell'elaborazione.

## Conclusione:

Questa scheda semplifica la validazione dei singoli campi dati dell'ordine, garantendo la conformità ai termini dell'ordine d'acquisto. Isolando un campo alla volta per il confronto, supporta revisioni mirate e la prevenzione degli errori nell'elaborazione degli ordini.
