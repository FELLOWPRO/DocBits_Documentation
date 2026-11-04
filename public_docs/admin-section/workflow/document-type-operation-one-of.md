# Operazione tipo documento uno di

<figure><img src="../../../../.gitbook/assets/docbits_doc_type_op_one_of.png" alt="DocBits Doc Tipo Op One Of" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta è progettata per gestire le azioni sui documenti in base al loro tipo, utilizzando una semplice logica condizionale (è/non è) per attivare o impedire flussi di lavoro specifici. Ciò consente un controllo preciso su come i diversi tipi di documenti vengono elaborati all'interno del sistema ERP.

## **Componenti della carta:**

1. **Operatore**
   * **Descrizione**: Determina la logica condizionale applicata ai tipi di documento.
   * **Opzioni**:
     * **è (is)**: L'operazione si attiverà se il tipo del documento corrisponde a uno dei tipi specificati nell'elenco.
     * **non è (is not)**: L'operazione si attiverà se il tipo del documento non corrisponde a nessuno dei tipi elencati.
2. **Elenco tipi di documento**
   * **Descrizione**: Specifica un elenco di tipi di documento a cui si applicherà la condizione.
   * **Dettaglio**: Include una varietà di tipi di documento come "Fattura", "Ordine di acquisto", ecc., in base ai quali verrà valutata la condizione (è/non è).

## Funzionalità:

* **Valutazione della condizione:** Il sistema controlla se il tipo di documento corrisponde alla condizione dell'operatore (è o non è) rispetto all'elenco specificato di tipi di documento.
* **Esecuzione dell'azione:**
  * **Condizione vera:**
    Se il tipo di documento soddisfa la condizione specificata (è o non è nell'elenco), il flusso di lavoro continua. Ciò potrebbe attivare processi come approvazioni di documenti, convalide specifiche o azioni di instradamento.
  * **Condizione falsa:**
    Se il tipo di documento non soddisfa la condizione, vengono eseguite azioni alternative, come il rifiuto del documento o l'interruzione del flusso di lavoro.

## Installazione e configurazione:

* Gli utenti configurano la carta selezionando il campo del tipo di documento e definendo l'operatore (è o non è). Specificano quindi l'elenco dei tipi di documento da controllare. La configurazione è semplice e prevede menu a discesa per la selezione del campo e dell'operatore e un campo per l'inserimento dell'elenco dei tipi di documento.

## Conclusione:

La carta di flusso di lavoro "Condizione tipo documento" svolge un ruolo cruciale nella gestione delle operazioni basate sui documenti con precisione e flessibilità. Utilizzando una semplice logica condizionale, aiuta a garantire che i documenti vengano elaborati in modo appropriato, migliorando l'efficienza e la conformità. Documentare chiaramente questa carta aiuterà gli utenti a capire come implementarla e utilizzarla in modo efficace, rendendola una parte preziosa della documentazione del sistema ERP.
