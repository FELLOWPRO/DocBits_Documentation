# Assign Sequentially to User

<figure><img src="../../../../.gitbook/assets/image (9) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

La scheda di workflow "**Assign Sequentially to User**" automatizza l'assegnazione dei documenti a un utente selezionato in modo sequenziale. Il valore di priorità determina l'ordine di assegnazione, dove i numeri più bassi rappresentano una priorità più alta.

## **Componenti della scheda**

1. **User**
   * **Descrizione**: All'utente selezionato verrà assegnato il documento in base alla sequenza del workflow.
   * **Dettaglio**: Un menu a discesa che elenca tutti gli utenti disponibili per l'assegnazione.
2. **Priority (Value)**
   * **Descrizione**: Un campo di input numerico in cui è possibile impostare il livello di priorità per l'utente.
   * **Dettaglio**: I numeri più bassi indicano una priorità più alta. I documenti vengono assegnati agli utenti in ordine crescente di priorità.

## **Funzionalità**

* **Assegnazione del documento**:\
  La scheda assegna i documenti all'utente selezionato in modo sequenziale, considerando il livello di priorità.\
  Se più utenti hanno la stessa priorità, i documenti vengono assegnati nell'ordine in cui gli utenti appaiono nel menu a discesa.

## **Configurazione e impostazione**

1. Aggiungi la scheda **Assign the Document Sequentially** al tuo workflow.
2. Configura il campo **User**:
   * Seleziona un utente dal menu a discesa.
3. Configura il campo **Priority (Value)**:
   * Inserisci un valore numerico per impostare la priorità di assegnazione.
4. Salva e attiva il workflow per applicare la configurazione.

## **Conclusione**

La scheda di workflow "Assign the Document Sequentially to User" garantisce una distribuzione organizzata dei documenti assegnandoli in una sequenza prioritaria. Ciò migliora la gestione delle attività e riduce i ritardi nell'elaborazione.
