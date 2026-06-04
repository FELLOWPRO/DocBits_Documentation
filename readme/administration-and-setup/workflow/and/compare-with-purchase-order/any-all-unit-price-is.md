# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow viene utilizzata per confrontare il prezzo unitario in un documento con il prezzo unitario in un ordine d'acquisto, garantendo che i prezzi siano allineati entro i livelli di tolleranza definiti. Il confronto può attivare azioni se il prezzo unitario non soddisfa le aspettative. La **Versione 4** aggiunge maggiore flessibilità consentendo agli utenti di scegliere entità diverse per il confronto, fornendo un livello di controllo più approfondito sui processi di prezzo e approvvigionamento.

## **Componenti della scheda:**

1. **Any / All:**
   * **Descrizione**: Definisce se la condizione si applica ad alcune o a tutte le istanze in cui il prezzo unitario viene confrontato.
   * **Opzioni**:
     * **Any**: La condizione è soddisfatta se un prezzo unitario qualsiasi soddisfa la condizione di confronto specificata.
     * **All**: La condizione è soddisfatta solo se tutti i prezzi unitari soddisfano la condizione di confronto specificata.
2. **Operator:**
   * **Descrizione**: Definisce la condizione per confrontare il prezzo unitario con il valore specificato.
   * **Opzioni**:
     * **Equals (=)**: Verifica se il prezzo unitario corrisponde al valore specificato.
     * **Not Equals (≠)**: Garantisce che il prezzo unitario sia diverso dal valore specificato.
     * **Greater Than (>)**: Verifica se il prezzo unitario è maggiore del valore specificato.
     * **Greater or Equals (≥)**: Verifica se il prezzo unitario è maggiore o uguale al valore specificato.
     * **Lesser Than (<)**: Verifica se il prezzo unitario è minore del valore specificato.
     * **Lesser or Equals (≤)**: Verifica se il prezzo unitario è minore o uguale al valore specificato.

## **Componenti aggiuntivi nella Versione 4:**

**Comparison Type:**

* **Descrizione**: Consente agli utenti di scegliere quali entità verranno confrontate oltre al prezzo unitario.
* **Opzioni**:
  * **Purchase Order to Document**: Confronta il prezzo unitario nell'ordine d'acquisto con il prezzo unitario nel documento.
  * **Received to Document**: Confronta la quantità ricevuta con il prezzo unitario nel documento.
  * **Purchase Order to Received**: Confronta il prezzo unitario nell'ordine d'acquisto con la quantità ricevuta.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema confronta il prezzo unitario nel documento con il prezzo unitario nell'ordine d'acquisto (o altra entità selezionata, nella Versione 4) in base all'operatore selezionato. Se il confronto è vero, il workflow procede secondo i passaggi successivi, attivando l'approvazione o arrestando il processo.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se la condizione risulta vera (es. il prezzo unitario nel documento è maggiore del valore specificato), il workflow proseguirà con l'azione vera (es. approvazione, elaborazione del documento).
  * **Condizione falsa**: Se la condizione risulta falsa (es. il prezzo unitario nel documento non soddisfa il confronto), il workflow non proseguirà.

## **Configurazione e impostazione:**

* **Configurazione Versione 3:** Gli utenti configurano la scheda selezionando il prezzo unitario nel documento, scegliendo l'operatore appropriato per definire come il prezzo unitario verrà confrontato con il valore specificato e impostando il valore di confronto. Inoltre, gli utenti selezionano se la condizione si applica ad alcune o a tutte le istanze del confronto del prezzo unitario.
* **Configurazione Versione 4:** Nella Versione 4, gli utenti hanno l'opzione aggiuntiva di selezionare il Comparison Type. Ciò consente loro di definire le entità da confrontare, come Purchase Order to Document, Received to Document o Purchase Order to Received. Questo migliora la flessibilità della scheda nel confrontare i prezzi unitari in scenari più complessi.

## **Scenario di esempio:**

*   **Esempio Versione 3:**&#x20;

    Una fattura mostra un prezzo unitario di $50. L'ordine d'acquisto correlato ha un prezzo unitario di $45. La scheda confronta i due prezzi unitari utilizzando l'operatore "Greater Than". Poiché il prezzo unitario nel documento ($50) è maggiore del prezzo unitario nell'ordine d'acquisto ($45), il workflow attiverà la condizione vera (es. invia il documento per la revisione).
* **Esempio Versione 4:**\
  Una fattura mostra un prezzo unitario di $50 e l'ordine d'acquisto correlato autorizzava un prezzo unitario di $45. Inoltre, la quantità ricevuta è di 60 unità. La scheda confronta la quantità ricevuta con il prezzo unitario del documento utilizzando l'operatore "Greater Than". Poiché la quantità ricevuta (60) è maggiore del prezzo unitario ($50), il workflow attiva la condizione vera e il documento viene segnalato per un'ulteriore revisione.

## **Conclusione:**

La Versione 3 della scheda di workflow "Unit Price Comparison" è progettata per garantire che i prezzi unitari nei documenti siano allineati a quelli negli ordini d'acquisto, attivando azioni in base a condizioni definite. La Versione 4 estende questa funzionalità introducendo opzioni di confronto più complesse, come il confronto tra ordini d'acquisto e documenti, quantità ricevute e documenti e ordini d'acquisto e quantità ricevute. Questa maggiore flessibilità consente alle organizzazioni di gestire scenari di prezzo e approvvigionamento più sofisticati, migliorando il controllo e l'accuratezza nei loro workflow.
