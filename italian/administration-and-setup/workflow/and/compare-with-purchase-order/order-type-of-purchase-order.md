# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per confrontare il tipo di ordine di un ordine d'acquisto con un valore specificato. La scheda verifica se il tipo di ordine dell'ordine d'acquisto soddisfa la condizione specificata (es. se è uguale, diverso, maggiore o soddisfa un'altra condizione) per garantire che l'ordine d'acquisto sia classificato correttamente. Questo confronto può attivare azioni in base a condizioni specifiche, come l'instradamento dell'ordine per un'ulteriore revisione o approvazione se vengono rilevate discrepanze.

## **Componenti della scheda:**

1. **Any/All:**
   * **Descrizione**: Definisce se la condizione si applica ad alcuni o a tutti gli ordini d'acquisto valutati nel workflow.
   * **Opzioni**:
     * **Any**: La condizione è soddisfatta se uno qualsiasi degli ordini d'acquisto corrisponde alla condizione specificata.
     * **All**: La condizione è soddisfatta solo se tutti gli ordini d'acquisto soddisfano la condizione specificata.
2. **Operator:**
   * **Descrizione**: Definisce la condizione che verrà applicata per confrontare il tipo di ordine con un valore specificato.
   * **Opzioni**:
     * **Equals (=)**: Verifica se il tipo di ordine corrisponde al valore specificato.
     * **Not Equals (≠)**: Garantisce che il tipo di ordine sia diverso dal valore specificato.
3. **Order Type:**
   * **Descrizione**: Specifica il valore con cui verrà confrontato il tipo di ordine dell'ordine d'acquisto.
   * **Dettaglio**: Il valore deve corrispondere al tipo di ordine o alla classificazione nel sistema.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema valuta il tipo di ordine dell'ordine d'acquisto rispetto alla condizione specificata utilizzando l'operatore selezionato. Se il tipo di ordine corrisponde (o non corrisponde) al valore specificato, il workflow procede di conseguenza.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se la condizione risulta vera (es. il tipo di ordine corrisponde al valore specificato), il workflow continuerà, eventualmente attivando azioni o passaggi di elaborazione aggiuntivi.
  * **Condizione falsa**: Se la condizione risulta falsa (es. il tipo di ordine non corrisponde al valore specificato), il workflow non continuerà.

## **Configurazione e impostazione:**

* Gli utenti configurano la scheda selezionando il campo del tipo di ordine dell'ordine d'acquisto e scegliendo l'operatore che definisce come verrà confrontato il tipo di ordine. Quindi impostano il valore specificato e decidono se applicare la condizione ad alcune o a tutte le righe dell'ordine d'acquisto.

## **Scenario di esempio:**

* Un ordine d'acquisto ha il tipo di ordine "Standard". Il workflow è configurato per verificare se il tipo di ordine è "Urgent". Utilizzando l'operatore "Equals", la scheda confronta il tipo di ordine e rileva che non corrisponde al valore specificato, attivando il workflow per inviare l'ordine alla revisione a causa della discordanza.

## **Conclusione:**

La scheda di workflow "Order Type of Purchase Order" garantisce che gli ordini d'acquisto siano classificati correttamente in base al loro tipo di ordine specificato. Automatizzando il confronto dei tipi di ordine, le organizzazioni possono garantire che gli ordini d'acquisto vengano elaborati secondo le classificazioni previste, contribuendo ad applicare la conformità e a semplificare i workflow di approvvigionamento.
