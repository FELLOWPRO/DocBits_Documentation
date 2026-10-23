# Tipo di documento Operazione uno di

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_list_v2-it-it.png" alt="Tipo di documento Operazione uno di, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

## **Scopo:**

Questa scheda è progettata per gestire le azioni sui documenti in funzione del loro tipo, impiegando una semplice logica condizionale (is/is not) per attivare o impedire workflow specifici. Ciò consente un controllo preciso su come i diversi tipi di documenti vengono elaborati all'interno del sistema ERP.

## **Componenti della scheda:**

1. **Operatore**
   * **Descrizione**: Determina la logica condizionale applicata ai tipi di documento.
   * **Opzioni**:
     * **is**: L'operazione si attiva se il tipo del documento corrisponde a uno dei tipi specificati nell'elenco.
     * **non lo è**: L'operazione si attiva se il tipo del documento non corrisponde a nessuno dei tipi elencati.
2. **Elenco tipi di documenti**
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

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Utilizzare la stessa convalida per diversi tipi di documenti.

**Configurazione:** Selezionare l'operatore is-one-of e i tipi `Invoice` e `Credit Note`.

**Risultato atteso e controesempio:** Un `Invoice` passa; un `Order` no.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
