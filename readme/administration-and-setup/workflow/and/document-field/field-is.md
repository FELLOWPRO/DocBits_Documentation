# Verificare la presenza e il contenuto di un campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-db30554e1eb1-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

## **Scopo:**

Questa scheda di workflow è progettata per automatizzare le azioni in base alla presenza o allo stato di un campo specificato all'interno di un documento. Valutando se il campo è vuoto, mancante o popolato, consente ai workflow di gestire i documenti con precisione e accuratezza.

## **Componenti della scheda:**

1. **Nome campo**
   * **Descrizione:** Specifica il nome del campo da valutare.
   * **Dettaglio:** Deve corrispondere all'identificatore esatto utilizzato nel documento per garantire un rilevamento accurato del campo.
2. **Operatori**
   * **Descrizione**: Definisce la condizione che attiva il workflow, in base alla presenza o allo stato del campo.
   * **Opzioni**:
     * **Vuoto/Non nel documento:** Il workflow si attiva se il campo è mancante dal documento oppure è presente ma vuoto.
     * **In Document/Not Vuoto:** Il flusso di lavoro si attiva se il campo esiste nel documento e contiene un valore.

## **Funzionalità:**

* **Rilevamento dello stato:** La scheda monitora il campo specificato per valutarne la presenza e lo stato.
* **Valutazione della condizione:**
  * Il sistema valuta se il campo specificato è nello stato (Empty/Not in Document o In Document/Not Empty) definito dall'operatore selezionato.
*

**Esecuzione dell'azione:**
* **Condizione Empty/Not in Document:** Se lo stato del campo corrisponde a questa condizione (ovvero il campo è assente dal documento o presente ma vuoto), il sistema avvia le azioni associate. Queste possono includere la generazione di avvisi, la segnalazione del documento per la revisione o l'arresto del workflow.
* **Condizione In Document/Not Empty:** Se lo stato del campo corrisponde a questa condizione (ovvero il campo esiste nel documento e contiene un valore), il sistema attiva le azioni associate. Queste potrebbero comportare l'abilitazione dei passaggi successivi del workflow, l'aggiornamento di record o l'attivazione di notifiche.
## **Configurazione e impostazione:**

* Gli utenti selezionano il campo da un elenco di campi del documento disponibili. L'operatore viene scelto tramite un menu a discesa, che offre opzioni chiare per "Empty/Not in Document" o "In Document/Not Empty".

## **Conclusione:**

La scheda di workflow "Field Presence and State Validation" è uno strumento fondamentale per i workflow di elaborazione dei documenti, garantendo una gestione accurata dei campi mancanti o popolati. Automatizzando le azioni in base agli stati dei campi, questa scheda migliora l'integrità dei dati, riduce gli errori e garantisce che i workflow operino in modo fluido ed efficiente.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Rileva fatture il cui numero di fattura necessita ancora di revisione.

**Configurazione:** Selezionare il campo `invoice_number` e Vuoto/Non nel documento.

**Risultato atteso e controesempio:** Passa un campo vuoto o mancante. Un valore popolato come `DEMO-001` non soddisfa questa condizione.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
