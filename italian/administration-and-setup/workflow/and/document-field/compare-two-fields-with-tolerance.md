# Compare two Fields with Tolerance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni confrontando i valori di due campi del documento specificati, con la possibilità aggiuntiva di applicare un valore di tolleranza. Questa funzionalità consente al sistema di considerare un margine di errore (tolleranza) durante il confronto dei valori dei campi, permettendo un processo decisionale più flessibile all'interno dei workflow.

## **Componenti della scheda:**

1. **Field Name (1)**
   * **Descrizione:** Specifica il primo campo del documento da confrontare.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del primo campo all'interno del documento.
2. **Operator**
   * **Descrizione:** Definisce il tipo di confronto da eseguire tra i due campi.
   * **Opzioni:**
     * **Equals (=):** Verifica se i valori dei due campi sono uguali.
     * **Not Equals (≠):** Garantisce che i valori dei due campi siano diversi.
     * **Greater Than (>):** Conferma che il valore del primo campo sia maggiore del secondo campo.
     * **Greater or Equals (≥):** Verifica che il valore del primo campo sia uguale o maggiore del secondo campo.
     * **Lesser Than (<):** Verifica se il valore del primo campo è minore del secondo campo.
     * **Less or Equals (≤):** Garantisce che il valore del primo campo sia minore o uguale al secondo campo.
3. **Field Name (2)**
   * **Descrizione:** Specifica il secondo campo del documento da confrontare con il primo campo.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del secondo campo all'interno del documento.&#x20;
4. **Tolerance Amount**
   * **Descrizione:** Definisce il margine di errore accettabile per il confronto.
   * **Dettaglio:** La quantità di tolleranza è un valore numerico che indica la differenza massima ammissibile tra i due valori dei campi affinché il confronto sia considerato vero.
5. **Tolerance Type**
   * **Descrizione:** Specifica l'unità di misura per la quantità di tolleranza.
   * **Opzioni:**
     * **Value:** La tolleranza è un valore assoluto, ovvero i due campi possono differire della quantità di tolleranza specificata.
     * **Percent:** La tolleranza è calcolata come percentuale del valore del secondo campo, consentendo un margine di errore relativo.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema valuta se i valori nei due campi specificati soddisfano la condizione di confronto, considerando la tolleranza definita. Se la differenza assoluta o relativa tra i due campi rientra nella tolleranza, la condizione è considerata vera.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se i valori dei due campi, dopo aver considerato la tolleranza, soddisfano la condizione di confronto, il sistema attiva le azioni associate. Queste azioni potrebbero includere l'avanzamento del workflow, l'aggiornamento di record, l'attivazione di avvisi o l'abilitazione di determinate operazioni.
  * **Condizione falsa:**\
    Se i valori dei due campi, dopo aver considerato la tolleranza, non soddisfano la condizione specificata, possono essere eseguite azioni alternative o nessuna azione, a seconda della configurazione del workflow.

## **Configurazione e impostazione:**

* Gli utenti configurano la scheda selezionando i due campi da confrontare da un elenco di campi disponibili nel sistema. L'operatore viene selezionato da un menu a discesa di opzioni di confronto disponibili. Gli utenti inseriscono la quantità di tolleranza e scelgono il tipo di tolleranza (value o percent).&#x20;

## **Conclusione:**

La scheda di workflow "Compare Two Fields with Tolerance" è uno strumento potente per confrontare i campi del documento tenendo conto delle deviazioni ammissibili nei dati. Applicando la tolleranza ai confronti dei campi, questa scheda aggiunge flessibilità al workflow, consentendogli di gestire le variazioni dei dati del mondo reale. Migliora il processo decisionale, supporta la validazione dei dati e potenzia l'automazione complessiva del workflow.
