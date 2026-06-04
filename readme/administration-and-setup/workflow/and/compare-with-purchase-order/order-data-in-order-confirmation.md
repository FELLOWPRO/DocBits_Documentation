# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo**

Questa scheda di workflow è progettata per confrontare campi specifici — **Unit Price**, **Discount** o **Quantity** — tra una conferma d'ordine e un ordine d'acquisto. Garantisce coerenza e conformità ai termini concordati. In base al risultato del confronto, la scheda consente agli utenti di scrivere un testo specificato in un campo scelto quando la condizione risulta **vera** o **falsa**, semplificando l'elaborazione dei documenti e riducendo l'intervento manuale.

## **Componenti della scheda**

1. **Order Data**
   * **Descrizione:** Specifica il campo da confrontare tra la conferma d'ordine e l'ordine d'acquisto.
   * **Opzioni:**
     * **Unit Price**: Confronta il prezzo unitario in entrambi i documenti.
     * **Discount**: Confronta la percentuale o il valore dello sconto.
     * **Quantity**: Confronta la quantità ordinata.
2. **Operator**
   * **Descrizione:** Definisce la condizione applicata durante il confronto.
   * **Opzioni:**
     * **Equals (=):** Verifica se il valore nel campo selezionato corrisponde tra la conferma d'ordine e l'ordine d'acquisto.
     * **Not Equals (≠):** Garantisce che il valore nel campo selezionato differisca tra i due documenti.
3. **Text**
   * **Descrizione:** Specifica il testo da scrivere nel campo di destinazione al momento della valutazione della condizione.
   * **Dettaglio:** Questo testo può includere note personalizzate, aggiornamenti di stato o valori predefiniti.
4. **Field Name**
   * **Descrizione:** Specifica il campo in cui verrà scritto il testo.
   * **Dettaglio:** Il campo di destinazione viene selezionato tra i campi modificabili disponibili nel sistema.
5. **Condition Result**
   * **Descrizione:** Determina quando il testo deve essere scritto, in base al risultato del confronto.
   * **Opzioni:**
     * **True:** Scrive il testo se la condizione di confronto è soddisfatta.
     * **False:** Scrive il testo se la condizione di confronto non è soddisfatta.

## **Funzionalità**

* **Valutazione del confronto:** Il sistema confronta il campo selezionato tra la conferma d'ordine e l'ordine d'acquisto utilizzando l'operatore specificato.
* **Esecuzione dell'azione:** Se la condizione risulta **vera** o **falsa**, il testo specificato viene scritto nel campo designato.

## **Configurazione e impostazione**

* Per configurare questa scheda, gli utenti selezionano innanzitutto il campo da confrontare — **Unit Price**, **Discount** o **Quantity**. Quindi scelgono un operatore per definire la condizione di confronto, come **equals** o **not equals**. Gli utenti specificano il testo da scrivere in un campo di destinazione e selezionano quando questa azione deve verificarsi, in base al risultato della condizione (**true** o **false**).

## **Scenario di esempio**

* Una conferma d'ordine indica un prezzo unitario di $50 per un prodotto, mentre l'ordine d'acquisto specifica un prezzo di $45. Utilizzando l'operatore **Not Equals (≠)**, la scheda identifica la discrepanza e scrive il testo "Price Mismatch" in un campo designato quando la condizione risulta **vera**.

## **Conclusione**

La scheda di workflow "\[Unit Price/Discount/Quantity] in Order Confirmation" fornisce una soluzione pratica per garantire la coerenza dei documenti. Segnalando automaticamente le discrepanze e scrivendo il testo pertinente nei campi specificati, migliora l'efficienza e riduce gli errori nei processi di gestione degli ordini.
