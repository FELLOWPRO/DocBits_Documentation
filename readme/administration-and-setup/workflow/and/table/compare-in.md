# Compare In

<figure><img src="../../../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits esegue un confronto tra due colonne di una tabella specificata, consentendo agli utenti di impostare condizioni basate sui valori di ciascuna colonna. Inoltre, questa scheda include una funzionalità di dipendenza, in cui il confronto avviene solo se il valore in una terza colonna corrisponde a un pattern regex Python specificato. Questa configurazione è utile per i controlli condizionali che dipendono da più punti dati all'interno di un dataset.

## **Funzionalità:**

* **Confronto di colonne con dipendenza:** Questa scheda confronta i valori di due colonne specificate in base a una condizione impostata, che viene applicata solo se il valore in una terza colonna di "dipendenza" corrisponde a un pattern regex Python definito.
* **Operatori:** Gli utenti possono scegliere i seguenti operatori per il confronto delle colonne:
  * **Equals (=):** Verifica se i valori nelle due colonne sono esattamente uguali.
  * **Not Equals (≠):** Garantisce che i valori nelle due colonne non siano uguali.
  * **Greater Than (>):** Conferma che i valori nella prima colonna siano maggiori di quelli nella seconda colonna.
  * **Greater or Equals (≥):** Garantisce che i valori nella prima colonna siano maggiori o uguali a quelli nella seconda colonna.
  * **Lesser Than (<):** Verifica se i valori nella prima colonna sono minori di quelli nella seconda colonna.
  * **Less or Equals (≤):** Garantisce che i valori nella prima colonna siano minori o uguali a quelli nella seconda colonna.
* **Dipendenza regex:** Questa scheda include una funzionalità di dipendenza che consente agli utenti di definire un pattern regex per una terza colonna. La condizione di confronto viene applicata solo se almeno un valore nella colonna di dipendenza corrisponde al pattern regex.

## **Utilizzo:**

Questa scheda è particolarmente utile negli scenari in cui è richiesta una logica condizionale complessa, come i controlli di qualità che dipendono dalle relazioni tra punti dati, con condizioni aggiuntive basate sulla formattazione dei dati o su pattern specifici.

***

## **Scenario di esempio:**

* Un utente configura la scheda per confrontare le colonne "Quantity" e "Threshold" in una tabella "Stock" con la condizione **Quantity ≥ Threshold**. Questo confronto avviene solo se la colonna "Item Code" corrisponde al pattern regex per formati di codice specifici, come **^A\d{3}$** (che indica un codice articolo che inizia con "A" seguito da tre cifre).

Utilizzando la scheda "Conditional Column Comparison", le organizzazioni possono creare confronti avanzati e dipendenti da pattern all'interno dei dataset, consentendo un'elaborazione dei dati ottimizzata e una maggiore accuratezza nei workflow condizionali.
