# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni confrontando il valore di un campo del documento specificato con un valore o una condizione di riferimento. Garantisce un processo decisionale dinamico e accurato nei workflow basato sulla validazione dei dati del documento.

## **Componenti della scheda:**

1. **Field Name**
   * **Descrizione:** Specifica il nome del campo del documento da valutare.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto del campo all'interno del documento.
2. **Operators**
   * **Descrizione:** Definisce il tipo di confronto da eseguire tra il valore del campo e il valore di riferimento.
   * **Opzioni:**
     * **Equals (=):** Verifica se il valore del campo corrisponde al valore di riferimento.
     * **Not Equals (≠):** Garantisce che il valore del campo sia diverso dal valore di riferimento.
     * **Greater Than (>):** Conferma che il valore del campo sia maggiore del valore di riferimento.
     * **Greater or Equals (≥):** Verifica che il valore del campo sia uguale o maggiore del valore di riferimento.
     * **Lesser Than (<):** Verifica se il valore del campo è minore del valore di riferimento.
     * **Less or Equals (≤):** Garantisce che il valore del campo sia minore o uguale al valore di riferimento.

## **Funzionalità:**

* **Valutazione della condizione:** Il sistema verifica se il valore del campo del documento, in relazione alla colonna associata, soddisfa la condizione di confronto specificata dall'operatore e dal valore di riferimento.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se il valore del campo del documento soddisfa la condizione specificata (es. è uguale al valore di riferimento), il sistema attiva le azioni associate. Queste potrebbero includere l'aggiornamento di record, l'avanzamento del workflow o la generazione di notifiche.
  * **Condizione falsa:**\
    Se il valore del campo del documento non soddisfa la condizione specificata, vengono eseguite azioni alternative o nessuna azione, in base alla configurazione del workflow.

## **Configurazione e impostazione:**

* L'utente seleziona il nome del campo del documento pertinente e sceglie l'operatore dal menu a discesa. L'utente specifica quindi il valore del campo di riferimento per completare la configurazione.

## **Conclusione:**

La scheda di workflow "DocField Comparison Validation" è uno strumento robusto per l'elaborazione dinamica dei documenti. Automatizzando le azioni in base ai confronti dei campi, questa scheda semplifica i workflow, migliora l'accuratezza e supporta un processo decisionale basato sui dati.
