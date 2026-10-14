# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per confrontare gli ID articolo tra un ordine d'acquisto e un documento correlato per garantire che siano inclusi gli articoli corretti. La scheda valuta se l'ID articolo nell'ordine d'acquisto corrisponde all'ID articolo nel documento. Questo confronto può attivare azioni se vengono rilevate discrepanze, garantendo che gli articoli nel documento siano allineati all'ordine d'acquisto.

## **Componenti della scheda:**

1. **Any / All:**
   * **Descrizione**: Definisce se la condizione si applica ad alcune o a tutte le istanze dei confronti degli ID articolo.
   * **Opzioni**:
     * **Any**: La condizione è soddisfatta se un ID articolo qualsiasi nell'ordine d'acquisto corrisponde all'ID articolo nel documento.
     * **All**: La condizione è soddisfatta solo se tutti gli ID articolo nell'ordine d'acquisto corrispondono agli ID articolo nel documento.
2. **Operator:**
   * **Descrizione**: Definisce la condizione per confrontare l'ID articolo nell'ordine d'acquisto con l'ID articolo nel documento.
   * **Opzioni**:
     * **Equals (=)**: Verifica se l'ID articolo nell'ordine d'acquisto corrisponde esattamente all'ID articolo nel documento.
     * **Not Equals (≠)**: Garantisce che l'ID articolo nell'ordine d'acquisto non corrisponda all'ID articolo nel documento.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema confronta l'ID articolo nell'ordine d'acquisto con l'ID articolo nel documento in base all'operatore selezionato. Se la condizione di confronto è vera (es. gli ID articolo corrispondono o non corrispondono), il workflow procederà di conseguenza.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se la condizione risulta vera (es. l'ID articolo nell'ordine d'acquisto è uguale all'ID articolo nel documento), il workflow proseguirà con l'azione vera (es. approvazione o ulteriore elaborazione).
  * **Condizione falsa**: Se la condizione risulta falsa (es. l'ID articolo nell'ordine d'acquisto non corrisponde all'ID articolo nel documento), il workflow non proseguirà.

## **Configurazione e impostazione:**

* Gli utenti configurano la scheda selezionando l'ID articolo sia nell'ordine d'acquisto che nel documento. Scelgono quindi l'operatore appropriato (Equals o Not Equals) per definire come verranno confrontati gli ID articolo. Infine, gli utenti selezionano se la condizione si applica ad alcuni o a tutti gli ID articolo nel confronto.

## **Scenario di esempio:**

* Una fattura elenca un articolo con ID "ABC123" e l'ordine d'acquisto correlato include anch'esso un articolo con ID "ABC123". Utilizzando l'operatore "Equals", la scheda confronta l'ID articolo nel documento con l'ID articolo nell'ordine d'acquisto. Poiché gli ID articolo corrispondono, il workflow continua senza problemi.

## **Conclusione:**

La scheda di workflow "Item ID Comparison" garantisce che gli ID articolo nei documenti siano allineati a quelli negli ordini d'acquisto. Ciò aiuta a prevenire discrepanze negli elenchi degli articoli e garantisce che gli articoli corretti vengano elaborati secondo l'ordine d'acquisto. La possibilità di effettuare il confronto su alcune o su tutte le istanze offre flessibilità in diversi casi d'uso, migliorando l'accuratezza e l'efficienza dei workflow di approvvigionamento.
