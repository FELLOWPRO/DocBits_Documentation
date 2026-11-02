# Dati dell'ordine nella conferma dell'ordine

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v1-it-it.png" alt="Dati dell&#x27;ordine nella conferma dell&#x27;ordine, Versione 1" width="634"><figcaption><p>Versione 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v2-it-it.png" alt="Dati dell&#x27;ordine nella conferma dell&#x27;ordine, Versione 2" width="634"><figcaption><p>Versione 2</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v3-it-it.png" alt="Dati dell&#x27;ordine nella conferma dell&#x27;ordine, Versione 3" width="634"><figcaption><p>Versione 3</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_oc_to_po_items_v4-it-it.png" alt="Dati dell&#x27;ordine nella conferma dell&#x27;ordine, Versione 4" width="634"><figcaption><p>Versione 4</p></figcaption></figure>

## **Scopo**

Questa scheda di workflow è progettata per confrontare campi specifici — **Prezzo unitario**, **Sconto** o **Quantità** — tra una conferma d'ordine e un ordine d'acquisto. Garantisce coerenza e conformità ai termini concordati. In base al risultato del confronto, la scheda consente agli utenti di scrivere un testo specificato in un campo scelto quando la condizione risulta **vera** o **falsa**, semplificando l'elaborazione dei documenti e riducendo l'intervento manuale.

## **Componenti della scheda**

1. **Dati ordine**
   * **Descrizione:** Specifica il campo da confrontare tra la conferma d'ordine e l'ordine d'acquisto.
   * **Opzioni:**
     * **Prezzo unitario**: Confronta il prezzo unitario in entrambi i documenti.
     * **Sconto**: Confronta la percentuale o il valore dello sconto.
     * **Quantità**: Confronta la quantità ordinata.
2. **Operatore**
   * **Descrizione:** Definisce la condizione applicata durante il confronto.
   * **Opzioni:**
     * **Uguale (=):** Verifica se il valore nel campo selezionato corrisponde tra la conferma d'ordine e l'ordine d'acquisto.
     * **Diverso (≠):** Garantisce che il valore nel campo selezionato differisca tra i due documenti.
3. **Testo**
   * **Descrizione:** Specifica il testo da scrivere nel campo di destinazione al momento della valutazione della condizione.
   * **Dettaglio:** Questo testo può includere note personalizzate, aggiornamenti di stato o valori predefiniti.
4. **Nome campo**
   * **Descrizione:** Specifica il campo in cui verrà scritto il testo.
   * **Dettaglio:** Il campo di destinazione viene selezionato tra i campi modificabili disponibili nel sistema.
5. **Condizione Risultato**
   * **Descrizione:** Determina quando il testo deve essere scritto, in base al risultato del confronto.
   * **Opzioni:**
     * **True:** Scrive il testo se la condizione di confronto è soddisfatta.
     * **False:** Scrive il testo se la condizione di confronto non è soddisfatta.

## **Funzionalità**

* **Valutazione del confronto:** Il sistema confronta il campo selezionato tra la conferma d'ordine e l'ordine d'acquisto utilizzando l'operatore specificato.
* **Esecuzione dell'azione:** Se la condizione risulta **vera** o **falsa**, il testo specificato viene scritto nel campo designato.

## **Configurazione e impostazione**

* Per configurare questa scheda, gli utenti selezionano innanzitutto il campo da confrontare — **Prezzo unitario**, **Sconto** o **Quantità**. Quindi scelgono un operatore per definire la condizione di confronto, come **equals** o **non uguali**. Gli utenti specificano il testo da scrivere in un campo di destinazione e selezionano quando questa azione deve verificarsi, in base al risultato della condizione (**true** o **false**).

## **Scenario di esempio**

* Una conferma d'ordine indica un prezzo unitario di $50 per un prodotto, mentre l'ordine d'acquisto specifica un prezzo di $45. Utilizzando l'operatore **Diverso (≠)**, la scheda identifica la discrepanza e scrive il testo "Price Mismatch" in un campo designato quando la condizione risulta **vera**.

## **Conclusione**

La scheda di workflow "\[Unit Price/Discount/Quantity] in Order Confirmation" fornisce una soluzione pratica per garantire la coerenza dei documenti. Segnalando automaticamente le discrepanze e scrivendo il testo pertinente nei campi specificati, migliora l'efficienza e riduce gli errori nei processi di gestione degli ordini.
