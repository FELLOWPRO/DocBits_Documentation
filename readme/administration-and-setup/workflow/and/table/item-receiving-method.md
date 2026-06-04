# Item Receiving Method

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits verifica se gli articoli in un dataset hanno un metodo di ricezione specificato. Gli utenti possono scegliere di validare **un articolo qualsiasi** o **tutti gli articoli** del dataset in base a una condizione selezionata, rendendola adatta agli scenari in cui i workflow dipendono dai metodi di ricezione degli articoli, come nella gestione della supply chain o nel tracciamento dell'inventario.

## **Funzionalità:**

* **Validazione del metodo di ricezione:** Questa scheda verifica il metodo di ricezione degli articoli rispetto a una condizione specificata. Gli utenti possono scegliere tra **un articolo qualsiasi** o **tutti gli articoli** del dataset e impostare la condizione come **equals** o **not equals**.
* **Selezione degli articoli:** Gli utenti possono specificare:
  * **Any Item:** La scheda si attiva se almeno un articolo soddisfa la condizione del metodo di ricezione specificata.
  * **All Items:** La scheda si attiva solo se tutti gli articoli soddisfano la condizione del metodo di ricezione specificata.
* **Operatori:** Sono disponibili i seguenti operatori per definire la condizione:
  * **Equals (=):** Verifica se il metodo di ricezione corrisponde al valore specificato.
  * **Not Equals (≠):** Garantisce che il metodo di ricezione non corrisponda al valore specificato.

## **Utilizzo:**

Questa scheda è ideale per i responsabili di magazzino, i coordinatori dell'inventario o il personale logistico che devono validare i metodi di ricezione degli articoli prima di consentire ulteriori azioni, come l'elaborazione, lo stoccaggio o la spedizione.

## **Scenario di esempio:**

* Un utente configura la scheda per verificare se **tutti gli articoli** hanno il metodo di ricezione **uguale a "Direct Delivery"**. Se ogni articolo soddisfa questa condizione, il workflow procede, confermando che tutti gli articoli sono destinati alla consegna diretta.

Utilizzando la scheda "Receiving Method Validation", le organizzazioni possono garantire la conformità ai protocolli di ricezione, migliorare i workflow logistici e mantenere l'accuratezza nella gestione degli articoli in base a specifici metodi di ricezione.
