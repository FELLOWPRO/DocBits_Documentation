# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni confrontando i valori di due campi del documento specificati. Consente un processo decisionale dinamico in base ai dati dei campi e garantisce che i workflow vengano eseguiti in base ai confronti tra i diversi valori del documento.

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
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del secondo campo all'interno del documento.

## **Funzionalità:**

**Valutazione della condizione:** Il sistema valuta se i valori nei due campi specificati soddisfano la condizione di confronto definita dall'operatore.

**Esecuzione dell'azione:**

* **Condizione vera:**\
  Se i valori dei due campi soddisfano la condizione di confronto, il sistema attiva le azioni associate. Queste azioni potrebbero includere l'aggiornamento di record o l'attivazione di avvisi.
* **Condizione falsa:**\
  Se i valori dei due campi non soddisfano la condizione specificata, possono essere eseguite azioni alternative o nessuna azione, a seconda della configurazione dei workflow.

## **Configurazione e impostazione:**&#x20;

* Gli utenti configurano la scheda selezionando i due campi da confrontare da un elenco di campi disponibili nel sistema. L'operatore viene selezionato da un menu a discesa di opzioni di confronto disponibili.

## **Conclusione:**

La scheda di workflow "Compare Two Fields" è uno strumento essenziale per confrontare i dati tra i campi all'interno dei documenti. Automatizzando le azioni in base ai confronti dei campi, questa scheda aiuta a ottimizzare il processo decisionale, supporta la validazione dei dati e potenzia l'automazione del workflow.
