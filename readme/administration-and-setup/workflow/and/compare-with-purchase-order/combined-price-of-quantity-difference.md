# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**:

Questa scheda di workflow valuta il prezzo combinato di una differenza di quantità, confrontandolo con un valore specificato. Aiuta ad automatizzare le azioni in base alle discrepanze di prezzo e quantità tra documenti correlati, migliorando i workflow di approvvigionamento e ricezione. La **Versione 4** espande questa funzionalità consentendo confronti tra entità diverse come l'ordine d'acquisto, le quantità ricevute e il documento stesso, aggiungendo maggiore flessibilità e controllo al workflow.

## **Componenti della scheda**:

1. **Operator**:&#x20;
   * **Descrizione:** La condizione per confrontare il prezzo combinato con un valore specificato.
   * **Opzioni:**
     * **Equals (=)**: Verifica se il prezzo combinato corrisponde al valore specificato.
     * **Not Equals (≠)**: Garantisce che il prezzo combinato sia diverso dal valore specificato.
     * **Greater Than (>)**: Verifica se il prezzo combinato è maggiore del valore specificato.
     * **Greater or Equals (≥)**: Verifica se il prezzo combinato è maggiore o uguale al valore specificato.
     * **Lesser Than (<)**: Verifica se il prezzo combinato è minore del valore specificato.
     * **Lesser or Equals (≤)**: Verifica se il prezzo combinato è minore o uguale al valore specificato.
2. **Value**:&#x20;
   * **Descrizione:** Specifica il valore con cui verrà confrontato il prezzo combinato della differenza di quantità.
   * **Dettaglio:** Il valore deve essere numerico.

## **Componenti aggiuntivi nella Versione 4**:

* **Comparison Type**: Seleziona le entità da confrontare. Le opzioni includono:
  * **Purchase Order to Document**: Confronta le quantità e i prezzi tra l'ordine d'acquisto e il documento correlato.
  * **Received to Document**: Confronta le quantità ricevute con le quantità nel documento.
  * **Purchase Order to Received**: Confronta le quantità dell'ordine d'acquisto con le quantità ricevute.

## **Funzionalità**:

* **Valutazione della condizione**: Calcola il prezzo combinato moltiplicando la differenza di quantità per il prezzo unitario e lo confronta con il valore specificato utilizzando l'operatore selezionato.\
  La **Versione 4** aggiunge l'opzione di confrontare entità aggiuntive in base alla configurazione dell'utente, come ordine d'acquisto verso ricevuto o ordine d'acquisto verso documento.
* **Esecuzione dell'azione**: In base al fatto che il prezzo combinato soddisfi o meno la condizione specificata, il workflow proseguirà con condizioni vere o false per attivare azioni o arrestare il workflow. La **Versione 4** consente inoltre un'esecuzione delle azioni più dinamica, in cui il tipo di condizione (es. ordine d'acquisto verso ricevuto) influenza il passaggio successivo.

## **Configurazione e impostazione**:

* **Versione 3**: Gli utenti configurano la scheda selezionando i campi del documento per la differenza di quantità e il prezzo unitario. L'operatore viene quindi scelto per definire come il prezzo combinato verrà confrontato con il valore specificato. Infine, gli utenti impostano la condizione di continuazione (vera o falsa), che determina il passaggio successivo nel workflow.
* **Versione 4**: Oltre alla configurazione della **Versione 3**, gli utenti hanno un'opzione aggiuntiva per configurare il **Comparison Type**. Questo definisce quali entità verranno confrontate, come **Purchase Order to Document**, **Received to Document** o **Purchase Order to Received**.

## **Scenario di esempio**:

* Una fattura mostra 50 unità di un prodotto a $100 ciascuna, per un totale di $5000. L'ordine d'acquisto correlato autorizzava un acquisto di $4500 per 45 unità. La differenza di quantità è di 5 unità e il prezzo combinato della differenza è di $500. La scheda confronta la quantità dell'ordine d'acquisto (45 unità) con la quantità ricevuta (50 unità) e verifica se il prezzo combinato è maggiore di $400 (il valore specificato). Utilizzando l'operatore **Greater Than (>)**, la scheda identifica la discrepanza e la segnala per la revisione da parte del team finanziario.

## **Conclusione**:

La **Versione 3** della scheda di workflow "Combined Price of Quantity Difference" offre un approccio diretto per confrontare le discrepanze di quantità e attivare azioni in base a soglie di prezzo.\
La **Versione 4** estende questa funzionalità consentendo confronti tra entità diverse (ordine d'acquisto, ricevuto, documento), fornendo maggiore flessibilità e controllo sul workflow. Le organizzazioni possono ora automatizzare scenari più complessi e applicare un controllo più stretto sui loro processi di approvvigionamento e ricezione.
