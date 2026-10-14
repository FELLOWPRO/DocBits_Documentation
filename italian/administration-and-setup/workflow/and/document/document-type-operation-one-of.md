# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda è progettata per gestire le azioni sui documenti in funzione del loro tipo, impiegando una semplice logica condizionale (is/is not) per attivare o impedire workflow specifici. Ciò consente un controllo preciso su come i diversi tipi di documenti vengono elaborati all'interno del sistema ERP.

## **Componenti della scheda:**

1. **Operator**
   * **Descrizione**: Determina la logica condizionale applicata ai tipi di documento.
   * **Opzioni**:
     * **is**: L'operazione si attiva se il tipo del documento corrisponde a uno dei tipi specificati nell'elenco.
     * **is not**: L'operazione si attiva se il tipo del documento non corrisponde a nessuno dei tipi elencati.
2. **Document Types List**
   * **Descrizione**: Specifica un elenco di tipi di documento a cui si applicherà la condizione.
   * **Dettaglio**: Comprende una varietà di tipi di documento come "Invoice", "Purchase Order", ecc., in base ai quali verrà valutata la condizione (is/is not).

## Funzionalità:

* **Valutazione della condizione:** Il sistema verifica se il tipo di documento soddisfa la condizione dell'operatore (is o is not) rispetto all'elenco specificato di tipi di documento.
* **Esecuzione dell'azione:**
  * **Condizione vera:**\
    Se il tipo di documento soddisfa la condizione specificata (is o is not nell'elenco), il workflow prosegue. Ciò potrebbe attivare processi come approvazioni di documenti, validazioni specifiche o azioni di instradamento.
  * **Condizione falsa:**\
    Se il tipo di documento non soddisfa la condizione, vengono eseguite azioni alternative, come il rifiuto del documento o l'arresto del workflow.

## Configurazione e impostazione:

* Gli utenti configurano la scheda selezionando il campo del tipo di documento e definendo l'operatore (is o is not). Specificano quindi l'elenco di tipi di documento con cui effettuare il confronto. La configurazione è semplice e prevede menu a discesa per la selezione del campo e dell'operatore e un campo per inserire l'elenco dei tipi di documento.

## Conclusione:

La scheda di workflow "Document Type Condition" svolge un ruolo cruciale nella gestione delle operazioni basate sui documenti con precisione e flessibilità. Utilizzando una semplice logica condizionale, aiuta a garantire che i documenti vengano elaborati in modo appropriato, migliorando efficienza e conformità. Documentare chiaramente questa scheda aiuterà gli utenti a comprendere come implementarla e utilizzarla efficacemente, rendendola una parte preziosa della documentazione del tuo sistema ERP.
