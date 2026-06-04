# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow confronta i costi totali in un campo del documento con i costi corrispondenti in un ordine d'acquisto. La scheda aiuta a garantire che i costi nel documento siano allineati a quelli nell'ordine d'acquisto, tenendo conto dei livelli di tolleranza specificati. Il confronto può attivare azioni se vengono rilevate discrepanze, come la segnalazione delle discrepanze per la revisione o l'adeguamento dei costi di conseguenza.

## **Componenti della scheda:**

1. **Field Name:**
   * **Descrizione**: Specifica il campo del documento che contiene i valori dei costi totali da confrontare con i costi nell'ordine d'acquisto.
   * **Dettaglio**: Il valore in questo campo rappresenta i costi totali applicati nel documento (es. fattura) e verrà confrontato con il costo dell'ordine d'acquisto.
2. **Operator:**
   * **Descrizione**: Definisce la condizione che verrà applicata al confronto tra il costo totale nel documento e il costo nell'ordine d'acquisto.
   * **Opzioni**:
     * **Equals (=)**: Verifica se il costo totale nel documento corrisponde al costo nell'ordine d'acquisto.
     * **Not Equals (≠)**: Garantisce che il costo totale nel documento sia diverso dal costo nell'ordine d'acquisto.
     * **Greater Than (>)**: Verifica se il costo totale nel documento è maggiore del costo nell'ordine d'acquisto.
     * **Greater or Equals (≥)**: Verifica se il costo totale nel documento è maggiore o uguale al costo nell'ordine d'acquisto.
     * **Lesser Than (<)**: Verifica se il costo totale nel documento è minore del costo nell'ordine d'acquisto.
     * **Lesser or Equals (≤)**: Verifica se il costo totale nel documento è minore o uguale al costo nell'ordine d'acquisto.
3. **Tolerance Amount**
   * **Descrizione**: Specifica la soglia di tolleranza per il confronto dei costi totali.
   * **Dettaglio**: Questo valore numerico rappresenta la varianza consentita nei costi tra il documento e l'ordine d'acquisto.
4. **Tolerance Type:**
   * **Descrizione**: Specifica il tipo di tolleranza che verrà applicato.
   * **Opzioni**:
     * **Percentage**: La tolleranza è applicata come percentuale del costo dell'ordine d'acquisto.
     * **Value**: La tolleranza è applicata come importo numerico fisso.
5. **Separator:**
   * **Descrizione**: Specifica il separatore utilizzato per distinguere il Charge ID alla fine del nome del campo.
   * **Dettaglio**: Il separatore separa il campo del costo dall'identificatore univoco Charge ID che verrà utilizzato per collegare il costo del documento al costo corrispondente nell'ordine d'acquisto.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema confronta il costo totale nel campo del documento con il costo corrispondente nell'ordine d'acquisto in base all'operatore e alla tolleranza. La tolleranza viene applicata per determinare se la differenza tra i due costi rientra in un intervallo accettabile.
* **Esecuzione dell'azione:**
  * **Condizione vera**: Se i costi corrispondono (tenendo conto della tolleranza) e la condizione è vera, il workflow proseguirà con l'azione definita, come l'approvazione del documento o l'ulteriore elaborazione.
  * **Condizione falsa**: Se la condizione è falsa (ovvero i costi non corrispondono entro la tolleranza), il workflow non proseguirà.

## **Configurazione e impostazione:**

* Gli utenti iniziano selezionando il campo del documento che contiene il valore del costo totale. Successivamente, selezionano l'operatore per definire come il costo verrà confrontato con il costo dell'ordine d'acquisto. Quindi, gli utenti impostano la quantità e il tipo di tolleranza (percentuale o assoluta). Infine, specificano il separatore e il Charge ID che verranno utilizzati per il confronto.

## **Scenario di esempio:**

Una fattura elenca un costo di $500 nel campo "total charges". Il costo corrispondente dell'ordine d'acquisto è di $480 e la tolleranza è impostata a $20 (tolleranza assoluta). La scheda confronta il costo del documento con il costo dell'ordine d'acquisto:

* Il costo totale nel documento rientra nella tolleranza di $20 rispetto all'ordine d'acquisto e il workflow continua senza problemi.
* Se il costo supera la tolleranza, il workflow segnala la discrepanza per la revisione.

## **Conclusione:**

La scheda di workflow "Compare Total Charges" garantisce che i costi nei documenti siano allineati a quelli negli ordini d'acquisto, tenendo conto dei livelli di tolleranza specificati. Ciò aiuta le organizzazioni ad automatizzare il processo di verifica, a identificare precocemente le discrepanze e a mantenere un migliore controllo sui processi relativi ai costi.
