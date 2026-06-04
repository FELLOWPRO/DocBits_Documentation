# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

La scheda di workflow "**Assign the Document Sequentially to User/Group Based on Decision Table**" assegna dinamicamente i documenti a un utente o a un gruppo, a seconda della valutazione della decision table. Ciò garantisce che i documenti vengano instradati in modo appropriato in base a regole predefinite.

## **Componenti della scheda**

1. **Priority (Value)**
   * **Descrizione**: Specifica il livello di priorità per le assegnazioni, dove i numeri più bassi rappresentano una priorità più alta.
   * **Dettaglio**: Un campo di input numerico in cui è possibile impostare il valore di priorità per controllare la sequenza di assegnazione.

## **Funzionalità**

* **Valutazione della decision table**:\
  La decision table valuta condizioni predefinite per decidere se il documento viene assegnato a un utente o a un gruppo.
* **Assegnazione del documento**:
  * Se la decision table restituisce un utente, il documento viene assegnato direttamente a tale utente.
  * Se la decision table restituisce un gruppo, il documento viene assegnato al gruppo in modo sequenziale, rispettando il valore di priorità specificato.

## **Configurazione e impostazione**

1. Aggiungi la scheda **Assign the Document Sequentially** al tuo workflow.
2. Configura il campo **Priority (Value)**:
   * Inserisci un valore numerico per impostare la priorità di assegnazione.
3. Salva e attiva il workflow per applicare la configurazione.

## **Conclusione**

La scheda di workflow "**Assign the Document Sequentially to User/Group Based on Decision Table**" garantisce un instradamento dei documenti efficiente e dinamico. Sfruttando la logica della decision table e i valori di priorità, la scheda facilita un'assegnazione accurata a un utente o a un gruppo, semplificando i workflow documentali.
