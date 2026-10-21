# Assegna in sequenza ai gruppi

## **Scopo**

La scheda di workflow "**Assegnare il documento in sequenza ai gruppi**" consente l'assegnazione sequenziale dei documenti a uno o più gruppi selezionati. Il valore di priorità determina l'ordine di assegnazione, dove i numeri più bassi rappresentano una priorità più alta.

## **Componenti della scheda**

1. **Gruppo**
   * **Descrizione**: Specifica i gruppi che riceveranno l'assegnazione del documento.
   * **Dettaglio**: Un menu a discesa in cui è possibile selezionare uno o più gruppi per l'assegnazione del documento.
2. **Priorità (Valore)**
   * **Descrizione**: Un campo di input numerico in cui è possibile impostare il livello di priorità per i gruppi.
   * **Dettaglio**: I numeri più bassi indicano una priorità più alta, garantendo che i documenti vengano assegnati ai gruppi in ordine crescente di priorità.

## **Funzionalità**

* **Assegnazione del documento**:\
  La scheda assegna i documenti in modo sequenziale ai gruppi selezionati in base ai loro valori di priorità.\
  Se più gruppi condividono la stessa priorità, i documenti vengono assegnati nell'ordine in cui i gruppi sono stati selezionati.

## **Configurazione e impostazione**

1. Aggiungi la scheda **Assegnare il documento in sequenza** al tuo workflow.
2. Configura il campo **Gruppo**:
   * Seleziona uno o più gruppi dal menu a discesa.
3. Configura il campo **Priorità (valore)**:
   * Inserisci un valore numerico per impostare la priorità di assegnazione.
4. Salva e attiva il workflow per applicare la configurazione.

## **Conclusione**

La scheda di workflow "Assign the Document Sequentially to Groups" garantisce un'allocazione efficiente dei documenti a uno o più gruppi in base alla priorità. Questa funzionalità supporta un'elaborazione dei documenti flessibile e organizzata tra più team o reparti.

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

**Quando utilizzarlo:** Dai la priorità all'assegnazione dei documenti ai team di revisione.

**Configurazione:** Selezionare i gruppi demo configurati e impostare la priorità richiesta, ad esempio `10`.

**Risultato atteso e controesempio:** Il documento riceve le assegnazioni del gruppo selezionato con quella priorità. Testare una seconda priorità separatamente quando i gruppi devono occupare fasi diverse.

Questa è una configurazione illustrativa e il risultato atteso. Utilizza campi, utenti e gruppi configurati nella tua organizzazione di test; non si afferma che questo esempio sia stato eseguito.
