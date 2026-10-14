# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per confrontare le informazioni sul fornitore presenti su una fattura con le informazioni sul fornitore presenti sull'ordine d'acquisto correlato. La scheda garantisce che il fornitore sulla fattura corrisponda al fornitore sull'ordine d'acquisto. Questo confronto aiuta a verificare che il fornitore corretto stia fatturando l'ordine e può attivare azioni in base a eventuali discrepanze.

## **Componenti della scheda:**

1. **Operator:**
   * **Descrizione**: Definisce la condizione per confrontare il fornitore sulla fattura con il fornitore sull'ordine d'acquisto.
   * **Opzioni**:
     * **Is**: Verifica se il fornitore sulla fattura corrisponde al fornitore sull'ordine d'acquisto.
     * **Is Not**: Garantisce che il fornitore sulla fattura non corrisponda al fornitore sull'ordine d'acquisto.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema confronta il fornitore sulla fattura con il fornitore sull'ordine d'acquisto in base all'operatore selezionato. Se la condizione di confronto è vera (es. il fornitore è lo stesso o diverso come richiesto), il workflow procederà di conseguenza.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se la condizione risulta vera (es. il fornitore sulla fattura corrisponde al fornitore sull'ordine d'acquisto), il workflow continua senza attivare errori.
  * **Condizione falsa**: Se la condizione risulta falsa (es. il fornitore sulla fattura non corrisponde al fornitore sull'ordine d'acquisto), il workflow non continuerà.

## **Configurazione e impostazione:**

* Gli utenti scelgono l'operatore appropriato ("Is" o "Is Not") per definire come verranno confrontati i fornitori.

## **Scenario di esempio:**

* Una fattura elenca un fornitore con l'ID "SUP123" e l'ordine d'acquisto correlato elenca anch'esso "SUP123" come fornitore. Utilizzando l'operatore "Is", la scheda confronta i fornitori e li trova identici, quindi il workflow prosegue senza problemi.

## **Conclusione:**

La scheda di workflow "Supplier Comparison" garantisce che il fornitore corretto stia fatturando l'ordine d'acquisto, aiutando a prevenire discrepanze ed errori nel processo di approvvigionamento. Verificando automaticamente le informazioni sul fornitore, le organizzazioni possono semplificare il processo di approvazione delle fatture e ridurre il rischio di frodi o errori nella fatturazione dei fornitori.
