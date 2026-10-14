# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per confrontare la quantità in un documento con la tolleranza definita nell'ordine d'acquisto. Consente agli utenti di valutare se la quantità soddisfa determinate condizioni, come l'uguaglianza o il superamento della tolleranza specificata. Nella Versione 4, la scheda estende le funzionalità aggiungendo la possibilità di confrontare più entità, tra cui l'ordine d'acquisto, le quantità ricevute e le quantità del documento, offrendo una maggiore flessibilità nella gestione di scenari diversi.

## **Componenti della scheda:**

1. **Any / All:**
   * **Descrizione**: Specifica come il confronto debba essere applicato a più elementi o condizioni.
   * **Opzioni**:
     * **Any**: Almeno una delle condizioni deve essere vera affinché l'azione venga attivata.
     * **All**: Tutte le condizioni devono essere vere affinché l'azione proceda.
2. **Operator:**
   * **Descrizione**: Definisce la condizione che verrà applicata per confrontare la quantità del documento con la tolleranza specificata.
   * **Opzioni**:
     * **Equals (=)**: Verifica se la quantità corrisponde al valore di tolleranza specificato.
     * **Not Equals (≠)**: Garantisce che la quantità sia diversa dal valore di tolleranza specificato.
     * **Greater Than (>)**: Verifica se la quantità è maggiore della tolleranza specificata.
     * **Greater or Equals (≥)**: Verifica se la quantità è maggiore o uguale alla tolleranza specificata.
     * **Lesser Than (<)**: Verifica se la quantità è minore della tolleranza specificata.
     * **Lesser or Equals (≤)**: Verifica se la quantità è minore o uguale alla tolleranza specificata.
3. **Tolerance Amount:**
   * **Descrizione**: Specifica il valore di tolleranza con cui verrà confrontata la quantità del documento.
   * **Dettaglio**: Questo valore è numerico e rappresenta la soglia di varianza consentita nella quantità.
4. **Tolerance Type:**
   * **Descrizione**: Definisce il tipo di tolleranza che verrà applicato.
   * **Opzioni**:
     * **Percentage**: La tolleranza è calcolata come percentuale della quantità dell'ordine d'acquisto.
     * **Value**: La tolleranza è specificata come valore numerico fisso.

## **Componenti aggiuntivi nella Versione 4:**

* **Comparison Type**: Seleziona le entità da confrontare, offrendo maggiore flessibilità su come le quantità vengono valutate nella Versione 4.
  * **Purchase Order to Document**: Confronta la quantità nell'ordine d'acquisto con la quantità nel documento correlato.
  * **Received to Document**: Confronta la quantità ricevuta con la quantità nel documento.
  * **Purchase Order to Received**: Confronta la quantità dell'ordine d'acquisto con la quantità ricevuta.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema confronta la quantità nel documento con la tolleranza nell'ordine d'acquisto in base all'operatore e alla quantità/tipo di tolleranza selezionati. Nella Versione 4, il **Comparison Type** consente di confrontare quantità diverse, come ordine d'acquisto verso ricevuto o ordine d'acquisto verso documento, fornendo un confronto più dinamico.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se il confronto risulta vero (es. la quantità del documento rientra nell'intervallo di tolleranza accettabile), il workflow proseguirà.
  * **Condizione falsa**: Se il confronto risulta falso (es. la quantità non soddisfa la tolleranza), il workflow non proseguirà.

## **Configurazione e impostazione:**

**Versione 3:**

* Gli utenti configurano la scheda selezionando la quantità del documento, definendo la quantità e il tipo di tolleranza e scegliendo l'operatore appropriato per confrontare la quantità con la tolleranza. La scheda valuta se la quantità rientra nella soglia di tolleranza e procede con l'azione "True" o "False" in base al risultato.

**Versione 4:**

* Oltre alla configurazione della Versione 3, gli utenti possono selezionare il **Comparison Type**, consentendo confronti tra entità diverse, come:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Scenario di esempio:**

Una fattura mostra che sono state consegnate 100 unità, ma l'ordine d'acquisto ne autorizzava solo 90. La quantità di tolleranza è impostata a 10 unità e il tipo di tolleranza è assoluto.

* **Versione 3**: La scheda confronta le 100 unità del documento con la tolleranza dell'ordine d'acquisto di 90 unità. Se la quantità supera la tolleranza, la scheda segnala la discrepanza per un'ulteriore revisione.
* **Versione 4**: La scheda potrebbe confrontare la **quantità dell'ordine d'acquisto** (90 unità) con la **quantità ricevuta** (100 unità) o la **quantità del documento** (100 unità). A seconda del **Comparison Type** selezionato, verifica se la differenza tra le due entità supera la tolleranza e attiva l'azione corrispondente.

## **Conclusione:**

* **Versione 3**: Questa scheda di workflow confronta la quantità del documento con la tolleranza dell'ordine d'acquisto, aiutando a garantire che le discrepanze di quantità vengano segnalate e gestite in modo appropriato.
* **Versione 4**: Estende questa funzionalità consentendo agli utenti di confrontare entità diverse, come ordine d'acquisto verso ricevuto o ordine d'acquisto verso documento, fornendo una maggiore flessibilità nella gestione di scenari più complessi. La Versione 4 garantisce un controllo più stretto sui workflow di approvvigionamento e ricezione, offrendo confronti e azioni più dinamici in base al tipo di confronto scelto.
